# app.py
import os
import streamlit as st
import pandas as pd
import time
import pickle 
from datetime import datetime
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.retrievers import BM25Retriever 
from langchain_classic.retrievers import EnsembleRetriever 
from langchain_classic.retrievers import MultiQueryRetriever 
import logging
from dotenv import load_dotenv 

# --- IMPORT GIAO DIỆN TỪ FILE UI ---
import ui_config as ui 

# --- KHAI BÁO DOCUMENTS GỐC ---
DOCUMENTS_FILE = "documents_goc.pkl"

# --- 1. CONFIG (PHẢI ĐỂ ĐẦU TIÊN) ---
st.set_page_config(
    page_title="DỰ ÁN NUÔI TÔI",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. API KEY ---
# app.py
import os
import streamlit as st
import pandas as pd
import time
import pickle 
from datetime import datetime
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.retrievers import BM25Retriever 
from langchain_classic.retrievers import EnsembleRetriever 
from langchain_classic.retrievers import MultiQueryRetriever 
import logging
from dotenv import load_dotenv 

# --- IMPORT GIAO DIỆN TỪ FILE UI ---
import ui_config as ui 

# --- KHAI BÁO DOCUMENTS GỐC ---
DOCUMENTS_FILE = "documents_goc.pkl"

# --- 1. CONFIG (PHẢI ĐỂ ĐẦU TIÊN) ---
st.set_page_config(
    page_title="DỰ ÁN NUÔI TÔI",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. API KEY CONFIGURATION (HARDCODED) ---
from dotenv import load_dotenv 

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY") 

# --- 3. STATE ---
if 'history' not in st.session_state:
    st.session_state.history = []

# --- 4. SIDEBAR (VẼ TRƯỚC ĐỂ LẤY THEME CHOICE) ---
with st.sidebar:
    st.markdown("<div style='text-align:center; padding-bottom: 15px'> <span style='font-size: 4em;'>💠</span> </div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-title' style='text-align: center; margin-bottom: 25px; font-size: 1.5em;'>CONTROL CENTER</div>", unsafe_allow_html=True)
    
    with st.expander("🎨 INTERFACE ", expanded=True):
        # Lấy giá trị Dark/Light ở đây
        theme_choice = st.radio("Select Mode:", options=["Dark Ultraviolet ", "Light Lavender"], index=0, key="theme_radio_sidebar")
        
    st.markdown("<div style='height: 15px'></div>", unsafe_allow_html=True)

    with st.expander("🧠 SELECT MODEL", expanded=True):
        selected_model = st.selectbox("Active Model:", options=["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo", "gpt-4o-mini"], index=3)

    st.markdown("<div style='height: 15px'></div>", unsafe_allow_html=True)

    with st.expander("🔍 FILTER", expanded=True):
        top_n = st.slider("Number of results:", 1, 10, 3)

    st.markdown("<div style='height: 10px'></div>", unsafe_allow_html=True)
    
    with st.expander("🕒 HISTORY", expanded=True):
        if len(st.session_state.history) > 0:
            history_html = f'<div style="max-height: 150px; overflow-y: auto; padding: 5px;">'
            for idx, item in enumerate(reversed(st.session_state.history)):
                time_part, query_part = item.split("] ", 1)
                # Dòng này sẽ tự ăn màu theo CSS
                history_html += f'<div class="history-item"><span style="color: #bd00ff;">{time_part}]</span> {query_part}</div>'
            history_html += '</div>'
            st.markdown(history_html, unsafe_allow_html=True)
            st.markdown("<div style='height: 10px'></div>", unsafe_allow_html=True)
            if st.button("PURGE LOGS 🗑️", type="secondary"):
                st.session_state.history = []
                st.rerun()
        else:
            st.caption("NO DATA FOUND")

# --- 5. LOAD CSS (LOAD SAU KHI ĐÃ CÓ BIẾN theme_choice) ---
st.markdown(ui.get_theme_css(theme_choice), unsafe_allow_html=True)

# --- 6. CACHING RESOURCE (LOGIC GIỮ NGUYÊN) ---
@st.cache_resource
def load_resources():
    # 1. Load Documents Gốc (cho BM25)
    documents_goc = []
    try:
        with open(DOCUMENTS_FILE, "rb") as f:
            documents_goc = pickle.load(f)
        print(f"✅ Loaded {len(documents_goc)} source documents for BM25.")
    except FileNotFoundError:
        st.error(f"❌ Documents file not found: {DOCUMENTS_FILE}. BM25 will be skipped.")
        return None, None
    except Exception as e:
        st.error(f"❌ Error loading documents for BM25: {e}")
        return None, None

    # 2. Load FAISS (Dense Retrieval)
    embedding_model = HuggingFaceEmbeddings(model_name="keepitreal/vietnamese-sbert")
    try:
        vectorstore = FAISS.load_local(folder_path="faiss_course_index", embeddings=embedding_model, allow_dangerous_deserialization=True)
    except Exception as e:
        st.error(f"❌ FAISS ERROR: {e}")
        return None, None
    
    # SETUP RAG
    faiss_base_retriever = vectorstore.as_retriever(search_kwargs={"k": 30})
    llm_expansion = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    faiss_expanded_retriever = MultiQueryRetriever.from_llm(
        retriever=faiss_base_retriever,
        llm=llm_expansion,
        include_original=True
    )
    logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)

    if documents_goc:
        bm25_retriever = BM25Retriever.from_documents(documents_goc)
        bm25_retriever.k = 30
        base_retriever = EnsembleRetriever(
            retrievers=[bm25_retriever, faiss_expanded_retriever],
            weights=[0.6, 0.4]
        )
    else:
        base_retriever = faiss_expanded_retriever

    rerank_model_name = "cross-encoder/ms-marco-MiniLM-L-6-v2"
    cross_encoder_model = HuggingFaceCrossEncoder(model_name=rerank_model_name)
    
    return base_retriever, cross_encoder_model

base_retriever_hybrid, cross_encoder_model = load_resources()
if not base_retriever_hybrid: st.stop()

# --- 7. MAIN UI LAYOUT ---
# Hiển thị dòng Donation
st.markdown(ui.get_donation_html(), unsafe_allow_html=True)

# Layout 3 cột (QR - Tiêu đề - QR)
c1, c2, c3 = st.columns([1.5, 7, 1.5], gap="medium", vertical_alignment="center")

with c1:
    try: st.image("image_094658.png", use_container_width=True)
    except: st.error("Missing img1")

with c2:
    # Hiển thị Header
    st.markdown(ui.get_header_html(selected_model), unsafe_allow_html=True)

with c3:
    try: st.image("image_094655.png", use_container_width=True)
    except: st.error("Missing img2")

# --- 7.1 HISTORY CHIPS LOGIC ---
unique_history = []
for item in reversed(st.session_state.history):
    clean_item = item.split("] ", 1)[1] if "] " in item else item
    if clean_item not in unique_history:
        unique_history.append(clean_item)
recent_chips = unique_history[:5]

history_query_clicked = None

if recent_chips:
    cols = st.columns([0.5, 1, 1, 1, 1, 1, 0.5])
    max_chips_to_display = min(5, len(recent_chips)) 
    for i in range(max_chips_to_display):
        with cols[i+1]:
            if st.button(f"⚡ {recent_chips[i]}", key=f"chip_{i}", use_container_width=True):
                history_query_clicked = recent_chips[i]

st.markdown("<div style='height: 10px'></div>", unsafe_allow_html=True)

# --- SEARCH FORM ---
with st.form("search_form"):
    # [FIX] Thêm vertical_alignment="bottom" để nút và ô nhập tự động thẳng hàng dưới
    col1, col2 = st.columns([5, 2], gap="large", vertical_alignment="center")
    
    with col1:
        query_input = st.text_input("", placeholder="NHẬP KHÓA HỌC BẠN MUỐN TÌM KIẾM (Ex: Khóa học machine learning)", label_visibility="collapsed")
    
    with col2:
        # [FIX] Xóa dòng st.markdown spacer cũ, thêm use_container_width=True cho nút to đẹp
        submitted_btn = st.form_submit_button("CLICK TO SEARCH 🚀", use_container_width=True)

# --- 8. STREAMING LOGIC ---
def stream_summary(content, llm_model):
    llm = ChatOpenAI(model=llm_model, temperature=0.1)
    prompt = f"""
    Bạn là trợ lý chuyên tóm tắt khóa học. 
    Hãy tóm tắt ngắn gọn trong khoảng 150-200 từ. Tóm tắt sao cho đầy đủ ý và người dùng cảm thấy dễ hiểu.
    Format bắt buộc:
    **Nội dung chính:**
    - (Ý 1)
    - (Ý 2)
    - (Ý 3)

    **Phù hợp với:**
    - (Đối tượng 1)
    - (Đối tượng 2)
    - (Đối tượng 3)
    
    {content}
    """
    return llm.stream(prompt)

# --- 9. EXECUTION ---
final_submitted = submitted_btn or (history_query_clicked is not None)
query = history_query_clicked if history_query_clicked else query_input

if final_submitted:
    if not query:
        st.warning("⚠️ COMMAND REQUIRED! PLEASE ENTER QUERY.")
    else:
        timestamp = datetime.now().strftime("%H:%M")
        log_entry = f"[{timestamp}] {query}"
        if not st.session_state.history or st.session_state.history[-1] != log_entry:
            st.session_state.history.append(log_entry)
            
        compressor = CrossEncoderReranker(model=cross_encoder_model, top_n=top_n)
        rerank_retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=base_retriever_hybrid)


        with st.status("🔄 ĐANG TRUY VẤN CƠ SỞ DỮ LIỆU... (VUI LÒNG ĐỢI)", expanded=False) as status:
            try:
                results = rerank_retriever.invoke(query)
            except Exception as e:
                status.update(label="❌ SYSTEM ERROR", state="error")
                st.error(str(e))
                st.stop()

        if not results:
             st.info("🤔 NO MATCHING DATA FOUND.")
        else:
            st.markdown("<br><br>", unsafe_allow_html=True)
            
            for i, doc in enumerate(results):
                meta = doc.metadata
                title = meta.get('title', 'No Title')
                instructor = meta.get('instructor', 'Unknown')
                duration = meta.get('duration', '--')
                size = meta.get('size', '--')
                source_url = meta.get('source_url', '#')
                original_link = meta.get('original_link')
                
                if not original_link or str(original_link).lower() in ['không có thông tin', 'n/a', '', 'nan']:
                    original_link = source_url

                # GỌI UI TỪ FILE CONFIG: Render Result Card HTML
                card_html = ui.get_result_card_html(i, title, instructor, duration, size, source_url, original_link)
                
                # Render nửa trên của card
                # Lưu ý: Do cấu trúc CSS cũ dùng div đóng mở hơi phức tạp, tôi đã gộp card HTML lại.
                # Tuy nhiên, để chèn Streamlit widget vào giữa HTML (streaming text), ta phải cắt đôi HTML
                # hoặc dùng column như cũ. Ở đây tôi dùng column như cũ nhưng lấy HTML từ file config cho gọn.
                
                # CÁCH XỬ LÝ: Tách HTML Card thành Header và Footer để nhét Stream vào giữa
                st.markdown(f"""
                <div class="result-card-container">
                    <div class="rank-badge">RANK #{i+1}</div>
                    <div class="card-content">
                        <div class="course-title">{title}</div>
                        <div class="meta-tags">
                            <span class="badge badge-instructor"><i>👤</i> {instructor}</span>
                            <span class="badge badge-duration"><i>⏱️</i> {duration}</span>
                            <span class="badge badge-size"><i>💾</i> {size}</span>
                        </div>
                """, unsafe_allow_html=True)
                
                # Streaming Area (Logic App)
                c1_stream, c2_stream = st.columns([1, 40])
                with c2_stream:
                    st.markdown("<h5>⚡ AI EXECUTIVE SUMMARY:</h5>", unsafe_allow_html=True)
                    summary_box = st.empty()
                    try:
                        stream_gen = stream_summary(doc.page_content, selected_model)
                        with summary_box.container():
                             st.write_stream(stream_gen)
                    except Exception as e:
                        st.error(f"LLM ERROR: {e}")

                st.markdown("<br>", unsafe_allow_html=True)

                # Footer Buttons (Render từ UI Config hoặc viết thẳng)
                st.markdown(f"""
                    <div class="custom-btn-group">
                        <a href="{source_url}" target="_blank" class="custom-btn btn-download">DOWNLOAD FREE ⬇️</a>
                        <a href="{original_link}" target="_blank" class="custom-btn btn-link">SOURCE UPLINK 🌐</a>
                    </div>
                </div></div> 
                """, unsafe_allow_html=True)

                st.markdown("<br><br>", unsafe_allow_html=True)
# --- 3. STATE ---
if 'history' not in st.session_state:
    st.session_state.history = []

# --- 4. SIDEBAR (VẼ TRƯỚC ĐỂ LẤY THEME CHOICE) ---
with st.sidebar:
    st.markdown("<div style='text-align:center; padding-bottom: 15px'> <span style='font-size: 4em;'>💠</span> </div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-title' style='text-align: center; margin-bottom: 25px; font-size: 1.5em;'>CONTROL CENTER</div>", unsafe_allow_html=True)
    
    with st.expander("🎨 INTERFACE ", expanded=True):
        # Lấy giá trị Dark/Light ở đây
        theme_choice = st.radio("Select Mode:", options=["Dark Ultraviolet ", "Light Lavender"], index=0, key="theme_radio_sidebar")
        
    st.markdown("<div style='height: 15px'></div>", unsafe_allow_html=True)

    with st.expander("🧠 SELECT MODEL", expanded=True):
        selected_model = st.selectbox("Active Model:", options=["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo", "gpt-4o-mini"], index=3)

    st.markdown("<div style='height: 15px'></div>", unsafe_allow_html=True)

    with st.expander("🔍 FILTER", expanded=True):
        top_n = st.slider("Number of results:", 1, 10, 3)

    st.markdown("<div style='height: 10px'></div>", unsafe_allow_html=True)
    
    with st.expander("🕒 HISTORY", expanded=True):
        if len(st.session_state.history) > 0:
            history_html = f'<div style="max-height: 150px; overflow-y: auto; padding: 5px;">'
            for idx, item in enumerate(reversed(st.session_state.history)):
                time_part, query_part = item.split("] ", 1)
                # Dòng này sẽ tự ăn màu theo CSS
                history_html += f'<div class="history-item"><span style="color: #bd00ff;">{time_part}]</span> {query_part}</div>'
            history_html += '</div>'
            st.markdown(history_html, unsafe_allow_html=True)
            st.markdown("<div style='height: 10px'></div>", unsafe_allow_html=True)
            if st.button("PURGE LOGS 🗑️", type="secondary"):
                st.session_state.history = []
                st.rerun()
        else:
            st.caption("NO DATA FOUND")

# --- 5. LOAD CSS (LOAD SAU KHI ĐÃ CÓ BIẾN theme_choice) ---
st.markdown(ui.get_theme_css(theme_choice), unsafe_allow_html=True)

# --- 6. CACHING RESOURCE (LOGIC GIỮ NGUYÊN) ---
@st.cache_resource
def load_resources():
    # 1. Load Documents Gốc (cho BM25)
    documents_goc = []
    try:
        with open(DOCUMENTS_FILE, "rb") as f:
            documents_goc = pickle.load(f)
        print(f"✅ Loaded {len(documents_goc)} source documents for BM25.")
    except FileNotFoundError:
        st.error(f"❌ Documents file not found: {DOCUMENTS_FILE}. BM25 will be skipped.")
        return None, None
    except Exception as e:
        st.error(f"❌ Error loading documents for BM25: {e}")
        return None, None

    # 2. Load FAISS (Dense Retrieval)
    embedding_model = HuggingFaceEmbeddings(model_name="keepitreal/vietnamese-sbert")
    try:
        vectorstore = FAISS.load_local(folder_path="faiss_course_index", embeddings=embedding_model, allow_dangerous_deserialization=True)
    except Exception as e:
        st.error(f"❌ FAISS ERROR: {e}")
        return None, None
    
    # SETUP RAG
    faiss_base_retriever = vectorstore.as_retriever(search_kwargs={"k": 30})
    llm_expansion = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    faiss_expanded_retriever = MultiQueryRetriever.from_llm(
        retriever=faiss_base_retriever,
        llm=llm_expansion,
        include_original=True
    )
    logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)

    if documents_goc:
        bm25_retriever = BM25Retriever.from_documents(documents_goc)
        bm25_retriever.k = 30
        base_retriever = EnsembleRetriever(
            retrievers=[bm25_retriever, faiss_expanded_retriever],
            weights=[0.6, 0.4]
        )
    else:
        base_retriever = faiss_expanded_retriever

    rerank_model_name = "cross-encoder/ms-marco-MiniLM-L-6-v2"
    cross_encoder_model = HuggingFaceCrossEncoder(model_name=rerank_model_name)
    
    return base_retriever, cross_encoder_model

base_retriever_hybrid, cross_encoder_model = load_resources()
if not base_retriever_hybrid: st.stop()

# --- 7. MAIN UI LAYOUT ---
# Hiển thị dòng Donation
st.markdown(ui.get_donation_html(), unsafe_allow_html=True)

# Layout 3 cột (QR - Tiêu đề - QR)
c1, c2, c3 = st.columns([1.5, 7, 1.5], gap="medium", vertical_alignment="center")

with c1:
    try: st.image("image_094658.png", use_container_width=True)
    except: st.error("Missing img1")

with c2:
    # Hiển thị Header
    st.markdown(ui.get_header_html(selected_model), unsafe_allow_html=True)

with c3:
    try: st.image("image_094655.png", use_container_width=True)
    except: st.error("Missing img2")

# --- 7.1 HISTORY CHIPS LOGIC ---
unique_history = []
for item in reversed(st.session_state.history):
    clean_item = item.split("] ", 1)[1] if "] " in item else item
    if clean_item not in unique_history:
        unique_history.append(clean_item)
recent_chips = unique_history[:5]

history_query_clicked = None

if recent_chips:
    cols = st.columns([0.5, 1, 1, 1, 1, 1, 0.5])
    max_chips_to_display = min(5, len(recent_chips)) 
    for i in range(max_chips_to_display):
        with cols[i+1]:
            if st.button(f"⚡ {recent_chips[i]}", key=f"chip_{i}", use_container_width=True):
                history_query_clicked = recent_chips[i]

st.markdown("<div style='height: 10px'></div>", unsafe_allow_html=True)

# --- SEARCH FORM ---
with st.form("search_form"):
    # [FIX] Thêm vertical_alignment="bottom" để nút và ô nhập tự động thẳng hàng dưới
    col1, col2 = st.columns([5, 2], gap="large", vertical_alignment="center")
    
    with col1:
        query_input = st.text_input("", placeholder="NHẬP KHÓA HỌC BẠN MUỐN TÌM KIẾM (Ex: Khóa học machine learning)", label_visibility="collapsed")
    
    with col2:
        # [FIX] Xóa dòng st.markdown spacer cũ, thêm use_container_width=True cho nút to đẹp
        submitted_btn = st.form_submit_button("CLICK TO SEARCH 🚀", use_container_width=True)

# --- 8. STREAMING LOGIC ---
def stream_summary(content, llm_model):
    llm = ChatOpenAI(model=llm_model, temperature=0.1)
    prompt = f"""
    Bạn là trợ lý chuyên tóm tắt khóa học. 
    Hãy tóm tắt ngắn gọn trong khoảng 150-200 từ. Tóm tắt sao cho đầy đủ ý và người dùng cảm thấy dễ hiểu.
    Format bắt buộc:
    **Nội dung chính:**
    - (Ý 1)
    - (Ý 2)
    - (Ý 3)

    **Phù hợp với:**
    - (Đối tượng 1)
    - (Đối tượng 2)
    - (Đối tượng 3)
    
    {content}
    """
    return llm.stream(prompt)

# --- 9. EXECUTION ---
final_submitted = submitted_btn or (history_query_clicked is not None)
query = history_query_clicked if history_query_clicked else query_input

if final_submitted:
    if not query:
        st.warning("⚠️ COMMAND REQUIRED! PLEASE ENTER QUERY.")
    else:
        timestamp = datetime.now().strftime("%H:%M")
        log_entry = f"[{timestamp}] {query}"
        if not st.session_state.history or st.session_state.history[-1] != log_entry:
            st.session_state.history.append(log_entry)
            
        compressor = CrossEncoderReranker(model=cross_encoder_model, top_n=top_n)
        rerank_retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=base_retriever_hybrid)


        with st.status("🔄 ĐANG TRUY VẤN CƠ SỞ DỮ LIỆU... (VUI LÒNG ĐỢI)", expanded=False) as status:
            try:
                results = rerank_retriever.invoke(query)
            except Exception as e:
                status.update(label="❌ SYSTEM ERROR", state="error")
                st.error(str(e))
                st.stop()

        if not results:
             st.info("🤔 NO MATCHING DATA FOUND.")
        else:
            st.markdown("<br><br>", unsafe_allow_html=True)
            
            for i, doc in enumerate(results):
                meta = doc.metadata
                title = meta.get('title', 'No Title')
                instructor = meta.get('instructor', 'Unknown')
                duration = meta.get('duration', '--')
                size = meta.get('size', '--')
                source_url = meta.get('source_url', '#')
                original_link = meta.get('original_link')
                
                if not original_link or str(original_link).lower() in ['không có thông tin', 'n/a', '', 'nan']:
                    original_link = source_url

                # GỌI UI TỪ FILE CONFIG: Render Result Card HTML
                card_html = ui.get_result_card_html(i, title, instructor, duration, size, source_url, original_link)
                
                # Render nửa trên của card
                # Lưu ý: Do cấu trúc CSS cũ dùng div đóng mở hơi phức tạp, tôi đã gộp card HTML lại.
                # Tuy nhiên, để chèn Streamlit widget vào giữa HTML (streaming text), ta phải cắt đôi HTML
                # hoặc dùng column như cũ. Ở đây tôi dùng column như cũ nhưng lấy HTML từ file config cho gọn.
                
                # CÁCH XỬ LÝ: Tách HTML Card thành Header và Footer để nhét Stream vào giữa
                st.markdown(f"""
                <div class="result-card-container">
                    <div class="rank-badge">RANK #{i+1}</div>
                    <div class="card-content">
                        <div class="course-title">{title}</div>
                        <div class="meta-tags">
                            <span class="badge badge-instructor"><i>👤</i> {instructor}</span>
                            <span class="badge badge-duration"><i>⏱️</i> {duration}</span>
                            <span class="badge badge-size"><i>💾</i> {size}</span>
                        </div>
                """, unsafe_allow_html=True)
                
                # Streaming Area (Logic App)
                c1_stream, c2_stream = st.columns([1, 40])
                with c2_stream:
                    st.markdown("<h5>⚡ AI EXECUTIVE SUMMARY:</h5>", unsafe_allow_html=True)
                    summary_box = st.empty()
                    try:
                        stream_gen = stream_summary(doc.page_content, selected_model)
                        with summary_box.container():
                             st.write_stream(stream_gen)
                    except Exception as e:
                        st.error(f"LLM ERROR: {e}")

                st.markdown("<br>", unsafe_allow_html=True)

                # Footer Buttons (Render từ UI Config hoặc viết thẳng)
                st.markdown(f"""
                    <div class="custom-btn-group">
                        <a href="{source_url}" target="_blank" class="custom-btn btn-download">DOWNLOAD FREE ⬇️</a>
                        <a href="{original_link}" target="_blank" class="custom-btn btn-link">SOURCE UPLINK 🌐</a>
                    </div>
                </div></div> 
                """, unsafe_allow_html=True)

                st.markdown("<br><br>", unsafe_allow_html=True)
