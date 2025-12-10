import os
import streamlit as st
import pandas as pd
import time
from datetime import datetime
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import CrossEncoderReranker

# --- 1. STREAMLIT PAGE CONFIGURATION ---
st.set_page_config(
    page_title="NEXUS // Course Hunter AI (Light Halo)",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. API KEY CONFIGURATION (HARDCODED) ---
from dotenv import load_dotenv # Thêm dòng này

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY") 
# --- 3. SESSION STATE MANAGEMENT ---
if 'history' not in st.session_state:
    st.session_state.history = []
if 'theme' not in st.session_state:
    st.session_state.theme = 'Holographic Light' 

# --- 4. DYNAMIC CSS GENERATION (LIGHT HOLOGRAPHIC EDITION) ---
def get_theme_css(theme_name):
    # --- COLOR PALETTE: NEON ON LIGHT ---
    neon_blue = "#00f2fe"
    neon_purple = "#bd00ff"
    neon_pink = "#ff0080"
    
    # New Light Theme Colors
    bg_light_gradient = "linear-gradient(-45deg, #f8fafc, #edf2f7, #e2e8f0, #edf2f7)"
    glass_bg_light = "rgba(255, 255, 255, 0.7)" # White frosted glass
    text_dark = "#1A202C" # Very dark gray for readability
    text_muted = "#4A5568"
    
    # Keep the vibrant holographic border
    hologram_border = f"linear-gradient(135deg, {neon_blue}, {neon_purple}, {neon_pink})"

    return f"""
    <style>
        /* IMPORT TECH-FOCUSED FONT */
        @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;800;900&display=swap');

        /* --- 1. CORE SETUP & LIGHT MOVING BACKGROUND --- */
        .stApp {{
            background: {bg_light_gradient};
            background-size: 400% 400%;
            animation: lightGradientBG 15s ease infinite;
            font-family: 'Rajdhani', sans-serif !important;
            color: {text_dark};
            font-weight: 600;
        }}
        
        @keyframes lightGradientBG {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
        
        /* CUSTOM CYBER SCROLLBAR (Adapted for Light) */
        ::-webkit-scrollbar {{ width: 8px; }}
        ::-webkit-scrollbar-track {{ background: rgba(0,0,0,0.05); }}
        ::-webkit-scrollbar-thumb {{ background: linear-gradient(to bottom, {neon_blue}, {neon_purple}); border-radius: 10px; }}
        ::selection {{ background: {neon_blue}; color: white; }}

        /* --- 2. SIDEBAR: LIGHT GLASS CONSOLE --- */
        section[data-testid="stSidebar"] {{
            background-color: {glass_bg_light};
            backdrop-filter: blur(30px) saturate(120%);
            border-right: 1px solid rgba(255, 255, 255, 0.8);
            box-shadow: 5px 0 30px rgba(0,0,0,0.03);
        }}
        .st-emotion-cache-1wvfmsl, .st-emotion-cache-10trblm {{ color: {text_dark} !important; letter-spacing: 1px; font-weight: 600; }}
        /* Sidebar titles glow */
        .sidebar-title {{ 
            background: linear-gradient(to right, {neon_blue}, {neon_purple}); 
            -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
            font-weight: 900; letter-spacing: 2px; text-transform: uppercase;
            filter: drop-shadow(0 0 5px rgba(189, 0, 255, 0.3));
        }}

        /* --- 3. TYPOGRAPHY: DARK GLITCH TITLE --- */
        .main-title-container {{
            text-align: center; padding: 60px 0 40px 0;
            position: relative; overflow: hidden;
        }}
        .main-title {{
            font-size: 5rem; font-weight: 900; line-height: 1; text-transform: uppercase;
            color: {text_dark}; /* Dark text base */
            /* Neon glow shadow adapted for light bg */
            text-shadow: 0 0 5px {neon_blue}, 0 0 20px rgba(189, 0, 255, 0.3);
            letter-spacing: 5px;
            animation: subtle-glitch 5s infinite alternate;
        }}
        @keyframes subtle-glitch {{
            0% {{ transform: skew(0deg); }}
            20% {{ transform: skew(-1deg); }}
            40% {{ transform: skew(0.5deg); }}
            100% {{ transform: skew(0deg); }}
        }}
        .sub-title {{
            font-size: 1.3rem; color: {text_muted}; font-weight: 700;
            text-transform: uppercase; letter-spacing: 3px; margin-top: 15px;
            border-bottom: 3px solid {neon_purple}; display: inline-block; padding-bottom: 5px;
        }}

        /* --- 4. INPUT FIELD: CLEAN WHITE TERMINAL --- */
        .stTextInput > div > div > input {{
            border-radius: 8px;
            padding: 18px 30px; font-size: 1.2rem; font-family: 'Rajdhani', monospace; letter-spacing: 1px; font-weight: 700;
            background: rgba(255, 255, 255, 0.9); /* White background */
            color: {text_dark};
            border: 2px solid #E2E8F0;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
        }}
        .stTextInput > div > div > input:focus {{
            border-color: {neon_blue};
            box-shadow: 0 0 0 4px rgba(0, 242, 254, 0.2);
            background: white;
        }}
        /* Placeholder color */
        ::placeholder {{ color: #A0AEC0 !important; }}

        /* --- 5. BUTTONS: VIBRANT GRADIENTS (Keep them popping) --- */
        div.stButton > button, button[kind="primaryFormSubmit"] {{
            background: linear-gradient(90deg, {neon_blue}, {neon_purple});
            color: white !important; font-weight: 900 !important;
            border: none; border-radius: 8px;
            height: 3.8em; letter-spacing: 2px; text-transform: uppercase;
            box-shadow: 0 10px 20px -10px rgba(189, 0, 255, 0.5);
            position: relative; overflow: hidden; z-index: 1;
            clip-path: polygon(5% 0%, 100% 0, 100% 70%, 95% 100%, 0 100%, 0% 30%);
        }}
        div.stButton > button::before, button[kind="primaryFormSubmit"]::before {{
            content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
            transition: 0.6s; z-index: -1;
        }}
        div.stButton > button:hover::before, button[kind="primaryFormSubmit"]:hover::before {{
            left: 100%;
        }}
        div.stButton > button:hover, button[kind="primaryFormSubmit"]:hover {{
            box-shadow: 0 15px 30px -5px rgba(189, 0, 255, 0.7);
            transform: translateY(-3px); color: white !important;
        }}
        
        /* --- 6. LIGHT HOLOGRAPHIC RESULT CARDS (The Star Show) --- */
        .result-card-container {{
            /* White frosted glass base */
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(30px) saturate(120%);
            border-radius: 16px;
            /* Iridescent border magic */
            position: relative;
            border: 2px solid transparent; /* Transparent border for gradient fill */
            background-clip: padding-box; /* Important for border */
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05); /* Soft shadow for light mode */
            margin-bottom: 35px; overflow: hidden;
            transition: all 0.3s ease;
        }}
        /* The glowing border effect - adjusted opacity for light bg */
        .result-card-container::before {{
            content: ''; position: absolute; top: -2px; bottom: -2px; left: -2px; right: -2px;
            background: {hologram_border};
            z-index: -1; border-radius: 18px;
            filter: blur(8px); opacity: 0.5;
        }}
        /* Scanning Line Animation - lighter and faster */
        .result-card-container::after {{
            content: ''; position: absolute; top: -100%; left: 0; width: 100%; height: 30%;
            background: linear-gradient(to bottom, transparent, rgba(0, 242, 254, 0.4), transparent);
            opacity: 0.7; animation: scanline 4s linear infinite;
        }}
        @keyframes scanline {{ 0% {{ top: -100%; }} 100% {{ top: 250%; }} }}

        .result-card-container:hover {{
            transform: translateY(-5px) scale(1.01);
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.1);
        }}
        .result-card-container:hover::before {{ opacity: 0.8; filter: blur(12px); }}

        /* Card Content */
        .rank-badge {{
            position: absolute; top: 0; left: 0;
            background: linear-gradient(135deg, {neon_purple}, {neon_pink});
            color: white; padding: 10px 20px; border-bottom-right-radius: 16px;
            font-weight: 900; font-size: 1.1rem; letter-spacing: 1px;
            box-shadow: 5px 5px 15px rgba(189, 0, 255, 0.3);
        }}
        .card-content {{ padding: 50px 30px 30px 30px; }}
        .course-title {{
            font-size: 1.8rem; font-weight: 900; color: {text_dark};
            margin-bottom: 15px; line-height: 1.2; text-transform: uppercase;
            /* Gradient text fill */
            background: linear-gradient(to right, {text_dark}, #4A5568);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}

        /* Glowing Badges - Light version */
        .meta-tags {{ display: flex; gap: 15px; flex-wrap: wrap; margin-bottom: 25px; }}
        .badge {{
            padding: 8px 18px; border-radius: 8px; font-size: 0.9rem; font-weight: 800;
            background: rgba(255,255,255,0.5); border: 1px solid #E2E8F0;
            color: {text_dark}; letter-spacing: 1px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }}
        .badge i {{ margin-right: 5px; color: {neon_purple}; }}

        /* Action Buttons */
        .custom-btn-group {{ display: flex; gap: 20px; margin-top: 35px; }}
        .custom-btn {{
            flex: 1; display: inline-flex; justify-content: center; align-items: center;
            padding: 16px 25px; border-radius: 8px; font-weight: 900; text-decoration: none !important;
            transition: all 0.3s ease; font-size: 1rem; text-transform: uppercase; letter-spacing: 2px;
            clip-path: polygon(5% 0%, 100% 0, 95% 100%, 0% 100%);
        }}
        .btn-download {{
            background: linear-gradient(135deg, #11998e, #38ef7d); color: white !important;
            box-shadow: 0 10px 20px -5px rgba(56, 239, 125, 0.5);
        }}
        .btn-download:hover {{
            box-shadow: 0 15px 30px -5px rgba(56, 239, 125, 0.7); transform: translateY(-3px);
        }}
        .btn-link {{
            background: white; color: {text_dark} !important;
            border: 2px solid #E2E8F0; box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        }}
        .btn-link:hover {{ border-color: {neon_blue}; color: {neon_blue} !important; transform: translateY(-3px); box-shadow: 0 10px 25px -5px rgba(0, 242, 254, 0.3); }}

        /* Misc UI */
        .st-emotion-cache-1ujg4j2 {{ /* Expander & Status */
            background: {glass_bg_light} !important;
            backdrop-filter: blur(30px); border: 1px solid white; border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            color: {text_dark} !important;
        }}
        h5 {{ font-weight: 900 !important; color: {neon_purple} !important; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 15px !important; }}
        hr {{ border-color: #E2E8F0; }}
        /* Lịch sử */
        .history-item {{
             border-bottom: 1px dashed #E2E8F0;
             padding: 8px 0; font-family: 'Rajdhani', monospace; color: {text_dark}; font-weight: 600;
        }}
    </style>
    """

# --- 5. SIDEBAR: CONTROL CONSOLE (ENGLISH) ---
with st.sidebar:
    st.markdown("<div style='text-align:center; padding-bottom: 15px'> <span style='font-size: 4em;'>💠</span> </div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-title' style='text-align: center; margin-bottom: 25px; font-size: 1.5em;'>CONTROL NEXUS</div>", unsafe_allow_html=True)
    
    # 1. Interface Theme
    with st.expander("🎨 INTERFACE ", expanded=True):
        theme_choice = st.radio("Select Mode:", options=["Light"], index=0, key="theme_radio_sidebar")
        st.session_state.theme = theme_choice
        st.markdown(get_theme_css(theme_choice), unsafe_allow_html=True)

    st.markdown("<div style='height: 15px'></div>", unsafe_allow_html=True)

    # 2. AI Configuration
    with st.expander("🧠 SELECT MODEL", expanded=False):
        selected_model = st.selectbox("Active Model:", options=["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo", "gpt-4o-mini"], index=0)

    st.markdown("<div style='height: 15px'></div>", unsafe_allow_html=True)

    # 3. Search Filters
    with st.expander("🔍 PARAMETERS", expanded=False):
        top_n = st.slider("Max Results (Quantity):", 1, 10, 3)

    st.markdown("---")
    
    # 4. History Logs
    with st.expander("🕒 HISTORY", expanded=True):
        if len(st.session_state.history) > 0:
            history_html = f'<div style="max-height: 150px; overflow-y: auto; padding: 5px;">'
            for idx, item in enumerate(reversed(st.session_state.history)):
                time_part, query_part = item.split("] ", 1)
                history_html += f'<div class="history-item"><span style="color: #bd00ff;">{time_part}]</span> {query_part}</div>'
            history_html += '</div>'
            st.markdown(history_html, unsafe_allow_html=True)
            st.markdown("<div style='height: 10px'></div>", unsafe_allow_html=True)
            if st.button("PURGE LOGS 🗑️", type="secondary"):
                st.session_state.history = []
                st.rerun()
        else:
            st.caption("NO DATA DATA FOUND.")

# --- 6. CACHING RESOURCE ---
@st.cache_resource
def load_resources():
    embedding_model = HuggingFaceEmbeddings(model_name="keepitreal/vietnamese-sbert")
    try:
        vectorstore = FAISS.load_local(folder_path="faiss_course_index", embeddings=embedding_model, allow_dangerous_deserialization=True)
    except Exception as e:
        st.error(f"❌ FAISS ERROR: {e}")
        return None, None
    rerank_model_name = "cross-encoder/ms-marco-MiniLM-L-6-v2"
    cross_encoder_model = HuggingFaceCrossEncoder(model_name=rerank_model_name)
    return vectorstore, cross_encoder_model

vectorstore, cross_encoder_model = load_resources()
if not vectorstore: st.stop()

# --- 7. MAIN UI (HEADER & SEARCH) ---
st.markdown("""
<div class="main-title-container">
    <div class="main-title">NEXUS HUNTER AI</div>
    <div class="sub-title">EXPLORE KNOWLEDGE ACROSS THE DATA UNIVERSE</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f'<div style="text-align: center; color: #4A5568; margin-bottom: 50px; font-family: monospace; letter-spacing: 2px; font-weight: 700;">OPERATING VIA NEURAL NET: <span style="color: #bd00ff;">[{selected_model.upper()}]</span> STATUS: ONLINE</div>', unsafe_allow_html=True)

with st.form("search_form"):
    col1, col2 = st.columns([5, 2], gap="large")
    with col1:
        query = st.text_input("", placeholder="ENTER COMMAND OR SEARCH QUERY...", label_visibility="collapsed")
    with col2:
        st.markdown("<div style='height: 4px'></div>", unsafe_allow_html=True) 
        submitted = st.form_submit_button("INITIATE SEARCH SEQUENCE 🚀")

# --- 8. STREAMING FUNCTION ---
def stream_summary(content, llm_model):
    llm = ChatOpenAI(model=llm_model, temperature=0.1)
    # NOT TRANSLATING PROMPT CONTENT
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

# --- 9. LOGIC & RESULTS DISPLAY ---
if submitted:
    if not query:
        st.warning("⚠️ COMMAND REQUIRED! PLEASE ENTER QUERY.")
    else:
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.history.append(f"[{timestamp}] {query}")
        base_retriever = vectorstore.as_retriever(search_kwargs={"k": 50})
        compressor = CrossEncoderReranker(model=cross_encoder_model, top_n=top_n)
        rerank_retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=base_retriever)

        # Translate Status Messages
        with st.status("🔮 INITIATING NEURAL SCAN...", expanded=True) as status:
            st.write("Scanning multidimensional vector space...")
            time.sleep(0.3)
            st.write(f"Optimizing results via Cross-Encoder reranking...")
            try:
                results = rerank_retriever.invoke(query)
                status.update(label="✅ TARGETS ACQUIRED! DATA SIGNATURES CONFIRMED.", state="complete", expanded=False)
            except Exception as e:
                status.update(label="❌ SYSTEM CRITICAL FAILURE", state="error")
                st.error(str(e))
                st.stop()

        if not results:
             st.info("🤔 NO MATCHING DATA SIGNATURES FOUND IN THIS SECTOR.")
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
                
                # Logic xử lý link (Xử lý xong thì thôi, code chạy tiếp xuống dưới)
                if not original_link or original_link.lower() in ['không có thông tin', 'n/a', '']:
                    original_link = source_url

                # --- SỬA LỖI: ĐOẠN NÀY PHẢI NẰM NGANG HÀNG VỚI 'if', KHÔNG ĐƯỢC NẰM TRONG 'if' ---
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
                
                # Streaming Area
                c1, c2 = st.columns([1, 40])
                with c2:
                    st.markdown("<h5>⚡ AI EXECUTIVE SUMMARY (LIVE STREAM):</h5>", unsafe_allow_html=True)
                    summary_box = st.empty()
                    try:
                        stream_gen = stream_summary(doc.page_content, selected_model)
                        with summary_box.container():
                             st.write_stream(stream_gen)
                    except Exception as e:
                        st.error(f"LLM ERROR: {e}")

                st.markdown("<br>", unsafe_allow_html=True)

                # Action Buttons
                st.markdown(f"""
                    <div class="custom-btn-group">
                        <a href="{source_url}" target="_blank" class="custom-btn btn-download">
                            DOWNLOAD FREE ⬇️
                        </a>
                        <a href="{original_link}" target="_blank" class="custom-btn btn-link">
                            SOURCE UPLINK 🌐
                        </a>
                    </div>
                </div> </div> """, unsafe_allow_html=True)

                st.markdown("<br><br>", unsafe_allow_html=True)