# ui_config.py

def get_theme_css(theme_mode="Dark"):
    
    # --- A. DARK MODE (GIỮ NGUYÊN BẢN 100% CODE CỦA BẠN) ---
    if "Dark" in theme_mode:
        neon_blue = "#00f2fe"
        neon_purple = "#bd00ff"
        neon_pink = "#ff0080"
        bg_dark_gradient = "linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f0c29)"
        glass_bg_dark = "rgba(15, 15, 25, 0.85)" 
        text_main = "#F0F6FC" 
        text_muted = "#8B949E"
        hologram_border = f"linear-gradient(135deg, {neon_blue}, {neon_purple}, {neon_pink})"

        return f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;800;900&display=swap');

            /* --- 1. CORE SETUP & DARK MOVING BACKGROUND --- */
            .stApp {{
                background: {bg_dark_gradient};
                background-size: 400% 400%;
                animation: lightGradientBG 15s ease infinite;
                font-family: 'Rajdhani', sans-serif !important;
                color: {text_main};
                font-weight: 600;
            }}
            
            @keyframes lightGradientBG {{
                0% {{ background-position: 0% 50%; }}
                50% {{ background-position: 100% 50%; }}
                100% {{ background-position: 0% 50%; }}
            }}
            
            /* CUSTOM CYBER SCROLLBAR - DARK MODE */
            ::-webkit-scrollbar {{ width: 8px; }}
            ::-webkit-scrollbar-track {{ background: #0f0c29; }}
            ::-webkit-scrollbar-thumb {{ background: linear-gradient(to bottom, {neon_blue}, {neon_purple}); border-radius: 10px; }}
            ::-selection {{ background: {neon_blue}; color: #000; }}

            /* --- 2. SIDEBAR --- */
            section[data-testid="stSidebar"] {{
                background-color: {glass_bg_dark};
                backdrop-filter: blur(20px) saturate(150%);
                border-right: 1px solid rgba(255, 255, 255, 0.1);
                box-shadow: 5px 0 30px rgba(0,0,0,0.5);
            }}
            .st-emotion-cache-1wvfmsl, .st-emotion-cache-10trblm {{ color: {text_main} !important; letter-spacing: 1px; font-weight: 600; }}
            
            /* Sidebar Titles */
            .sidebar-title {{ 
                background: linear-gradient(to right, {neon_blue}, {neon_purple}); 
                -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                font-weight: 900; letter-spacing: 2px; text-transform: uppercase;
                filter: drop-shadow(0 0 5px rgba(189, 0, 255, 0.5));
            }}
            /* Sidebar Inputs Label */
            .st-emotion-cache-1qg05tj {{ color: {text_main} !important; }}

            /* --- 3. TYPOGRAPHY --- */
            .main-title-container {{
                text-align: center; padding: 60px 0 40px 0;
                position: relative; overflow: hidden;
            }}
            .main-title {{
                font-size: 5rem; font-weight: 900; line-height: 1; text-transform: uppercase;
                color: #fff;
                text-shadow: 0 0 10px {neon_blue}, 0 0 30px rgba(189, 0, 255, 0.6);
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
            /* [MỚI] KHUNG BAO NGOÀI FORM SEARCH (CÁI VIỀN LỚN) */
            [data-testid="stForm"] {{
                border: 2px solid #4A3F63  !important; /* Viền đen đậm sắc nét */
                background-color: rgba(74, 63, 99, 0.25) !important; /* Nền mờ nhẹ */
                border-radius: 16px !important; /* Bo góc cho đẹp */
                box-shadow: 4px 4px 0px rgba(0,0,0,0.1) !important; /* Bóng nhẹ */
                box-shadow: 4px 4px 0px rgba(0,0,0,0.1) !important;
            }}

            /* --- 4. INPUT FIELD --- */
            .stTextInput > div > div > input {{
                border-radius: 8px;
                padding: 18px 30px; font-size: 1.2rem; font-family: 'Rajdhani', monospace; letter-spacing: 1px; font-weight: 700;
                background: rgba(20, 20, 35, 0.9); /* Nền input tối */
                color: #fff;
                border: 2px solid #2D3748;
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
                transition: all 0.3s ease;
            }}
            .stTextInput > div > div > input:focus {{
                border-color: {neon_blue};
                box-shadow: 0 0 15px rgba(0, 242, 254, 0.3);
                background: #000;
            }}
            /* [MỚI] CHỈNH RIÊNG SIZE CHỮ PLACEHOLDER (Dòng gợi ý mờ) */
            .stTextInput input::placeholder {{
                font-size: 1rem !important; /* Nhỏ hơn chữ nhập bình thường (1.2rem) */
                font-weight: 400 !important;   /* Nét mảnh hơn */
                opacity: 0.9 !important;       /* Hơi mờ đi cho tinh tế */
                font-style: italic !important; /* (Tùy chọn) In nghiêng nhẹ cho đẹp */
                color: #8B949E !important;     /* Đảm bảo màu xám dễ chịu */
            }}
            ::placeholder {{ color: #4A5568 !important; }}

            /* --- 5. BUTTONS (CHIPS STYLING) --- */
            /* Nút History Chips */
            div.stButton > button {{
                background: rgba(255, 255, 255, 0.05) !important;
                border: 1px solid {neon_purple} !important;
                color: {text_main} !important;
                border-radius: 20px !important;
                padding: 5px 20px !important;
                font-size: 0.85rem !important;
                font-weight: 700 !important;
                box-shadow: 4px 4px 0px rgba(0, 0, 0, 0.9) !important;
                height: auto !important;
                transition: all 0.3s ease !important;
            }}
            div.stButton > button:hover {{
                background: {neon_purple} !important;
                color: white !important;
                box-shadow: 0 0 20px {neon_purple} !important;
                border-color: {neon_purple} !important;
                transform: translateY(-2px) !important;
            }}

            /* --- 6. RESULT CARDS (DARK MODE) --- */
            .result-card-container {{
                background: rgba(20, 25, 40, 0.6); /* Thẻ tối màu bán trong suốt */
                backdrop-filter: blur(20px);
                border-radius: 16px;
                position: relative;
                border: 1px solid rgba(255,255,255,0.08);
                background-clip: padding-box;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
                margin-bottom: 35px; overflow: hidden;
                transition: all 0.3s ease;
            }}
            .result-card-container::before {{
                content: ''; position: absolute; top: -1px; bottom: -1px; left: -1px; right: -1px;
                background: {hologram_border};
                z-index: -1; border-radius: 16px;
                filter: blur(10px); opacity: 0.4;
            }}
            .result-card-container::after {{
                content: ''; position: absolute; top: -100%; left: 0; width: 100%; height: 30%;
                background: linear-gradient(to bottom, transparent, rgba(0, 242, 254, 0.2), transparent);
                opacity: 0.5; animation: scanline 4s linear infinite;
            }}
            @keyframes scanline {{ 0% {{ top: -100%; }} 100% {{ top: 250%; }} }}

            .result-card-container:hover {{
                transform: translateY(-5px) scale(1.01);
                box-shadow: 0 30px 60px rgba(0, 0, 0, 0.6);
                border-color: rgba(255,255,255,0.2);
            }}

            /* Card Elements */
            .rank-badge {{
                position: absolute; top: 0; left: 0;
                background: linear-gradient(135deg, {neon_purple}, {neon_pink});
                color: white; padding: 10px 20px; border-bottom-right-radius: 16px;
                font-weight: 900; font-size: 1.1rem; letter-spacing: 1px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.3);
                z-index: 2;
            }}
            .card-content {{ padding: 50px 30px 30px 30px; position: relative; z-index: 1; }}
            
            .course-title {{
                font-size: 1.8rem; font-weight: 900; color: #fff;
                margin-bottom: 15px; line-height: 1.2; text-transform: uppercase;
                /* Gradient text trắng sang xám */
                background: linear-gradient(to right, #ffffff, #a0aec0);
                -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            }}

            .meta-tags {{ display: flex; gap: 15px; flex-wrap: wrap; margin-bottom: 25px; }}
            .badge {{
                padding: 8px 18px; border-radius: 8px; font-size: 0.9rem; font-weight: 800;
                background: rgba(255,255,255,0.05); /* Badge nền tối */
                border: 1px solid rgba(255,255,255,0.1);
                color: #E2E8F0; letter-spacing: 1px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            }}
            .badge i {{ margin-right: 5px; color: {neon_blue}; }}

            /* Action Buttons inside Card */
            .custom-btn-group {{ display: flex; gap: 20px; margin-top: 35px; }}
            .custom-btn {{
                flex: 1; display: inline-flex; justify-content: center; align-items: center;
                padding: 16px 25px; border-radius: 8px; font-weight: 900; text-decoration: none !important;
                transition: all 0.3s ease; font-size: 1rem; text-transform: uppercase; letter-spacing: 2px;
                clip-path: polygon(5% 0%, 100% 0, 95% 100%, 0% 100%);
            }}
            .btn-download {{
                background: linear-gradient(135deg, #11998e, #38ef7d); color: #000 !important;
                box-shadow: 0 0 20px rgba(56, 239, 125, 0.3);
            }}
            .btn-download:hover {{
                box-shadow: 0 0 30px rgba(56, 239, 125, 0.6); transform: translateY(-3px); color: white !important;
            }}
            .btn-link {{
                background: transparent; color: {text_main} !important;
                border: 1px solid rgba(255,255,255,0.3); 
            }}
            .btn-link:hover {{ 
                border-color: {neon_blue}; color: {neon_blue} !important; 
                transform: translateY(-3px); box-shadow: 0 0 20px rgba(0, 242, 254, 0.2); 
                background: rgba(0, 242, 254, 0.05);
            }}

            /* Misc */
            .st-emotion-cache-1ujg4j2 {{
                background: {glass_bg_dark} !important;
                backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                color: {text_main} !important;
            }}
            h5 {{ font-weight: 900 !important; color: {neon_purple} !important; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 15px !important; }}
            hr {{ border-color: rgba(255,255,255,0.1); }}
            .history-item {{
                 border-bottom: 1px dashed rgba(255,255,255,0.2);
                 padding: 8px 0; font-family: 'Rajdhani', monospace; color: {text_muted}; font-weight: 600;
            }}
            .history-item:hover {{ color: {neon_blue}; }}

            /* =============================================
               PHẦN 7: SEARCH BUTTON STYLE (VŨ TRỤ - COSMIC STYLE)
               ============================================= */
            
            /* 1. Tạo nền Gradient chuyển động (Cosmic Flow) */
            [data-testid="stForm"] button {{
                /* Pha trộn 4 màu: Tím đậm, Xanh Neon, Hồng Neon, Tím đậm (lặp lại để loop mượt) */
                background: linear-gradient(90deg, #6a11cb, #2575fc, #ff0080, #6a11cb);
                background-size: 300% 100%; /* Kéo dài nền để tạo không gian trượt */
                
                color: white !important;
                border: none !important;
                font-weight: 800 !important;
                font-size: 1rem !important;
                text-transform: uppercase;
                letter-spacing: 2px;
                border-radius: 50px !important; /* Bo tròn kiểu viên thuốc (Pill shape) hiện đại */
                
                position: relative;
                z-index: 1;
                overflow: hidden; /* Để cắt phần vệt sáng chạy qua */
                transition: all 0.4s ease-in-out;
                
                /* Animation cho màu nền tự trôi */
                animation: cosmic-shift 8s linear infinite;
                
                box-shadow: 0 0 10px rgba(106, 17, 203, 0.5); /* Glow nhẹ ban đầu */
                height: 3.8em !important;
                margin-top: 0px !important;
            }}

            /* 2. Tạo hiệu ứng "Óng Ánh" (Vệt sáng quét qua - Shine Effect) */
            [data-testid="stForm"] button::before {{
                content: '';
                position: absolute;
                top: 0;
                left: -100%; /* Bắt đầu từ ngoài bên trái */
                width: 100%;
                height: 100%;
                
                /* Vệt sáng trắng mờ chéo */
                background: linear-gradient(
                    120deg, 
                    transparent, 
                    rgba(255, 255, 255, 0.1), 
                    rgba(255, 255, 255, 0.6), 
                    rgba(255, 255, 255, 0.1), 
                    transparent
                );
                
                transition: all 0.6s;
                transform: skewX(-25deg); /* Nghiêng vệt sáng */
            }}

            /* 3. Animation cho vệt sáng tự động chạy mãi mãi */
            [data-testid="stForm"] button::after {{
                content: '';
                position: absolute;
                top: 0; left: -100%;
                width: 50%; height: 100%;
                background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,0.3) 100%);
                transform: skewX(-25deg);
                animation: shine-flow 4s infinite linear; /* Chạy liên tục mỗi 4 giây */
                opacity: 0.5;
            }}

            /* 4. Hiệu ứng khi Hover (Di chuột vào) */
            [data-testid="stForm"] button:hover {{
                background-size: 150% 100%; /* Thu hẹp khoảng màu lại để rực hơn */
                box-shadow: 0 0 30px rgba(37, 117, 252, 0.8), 0 0 60px rgba(255, 0, 128, 0.6); /* Glow cực mạnh */
                transform: scale(1.02); /* Phóng to nhẹ */
                text-shadow: 0 0 8px white;
            }}
            
            /* 5. Hiệu ứng khi Bấm (Active) */
            [data-testid="stForm"] button:active {{
                transform: scale(0.95);
                box-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
            }}

            /* --- CÁC KEYFRAMES CHUYỂN ĐỘNG --- */
            
            /* Di chuyển màu nền (Cosmic Shift) */
            @keyframes cosmic-shift {{
                0% {{ background-position: 0% 50%; }}
                100% {{ background-position: 100% 50%; }}
            }}
            
            /* Di chuyển vệt sáng (Shine Flow) */
            @keyframes shine-flow {{
                0% {{ left: -100%; opacity: 0; }}
                10% {{ opacity: 0.5; }}
                20% {{ left: 200%; opacity: 0; }} /* Chạy vụt qua sang phải */
                100% {{ left: 200%; opacity: 0; }}
            }}
            /* =============================================
               PHẦN 8: KHUNG BAO NGOÀI (EXPANDER) - VIỀN SÁNG FULL
               ============================================= */
            /* Target vào thẻ details (khung chính) */
            [data-testid="stSidebar"] [data-testid="stExpander"] {{
                border: 1px solid rgba(100, 200, 255, 0.3) !important;
                border-radius: 8px !important;
                box-shadow: 0 0 10px rgba(100, 200, 255, 0.1) !important;
                background-color: rgba(26, 28, 36, 0.4) !important;
                margin-bottom: 0px !important;
                overflow: hidden !important; /* Đảm bảo nội dung không tràn ra ngoài viền */
            }}

            /* Hiệu ứng Glow khi di chuột vào */
            [data-testid="stSidebar"] [data-testid="stExpander"]:hover {{
                border: 1px solid rgba(100, 200, 255, 0.6) !important;
                box-shadow: 0 0 15px rgba(100, 200, 255, 0.2) !important;
            }}

            /* Nội dung bên trong khi mở ra (Fix lỗi mất viền dưới) */
            [data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderContent"] {{
                color: white !important;
                padding-bottom: 10px !important; /* Thêm khoảng trống ở đáy để không dính viền */
            }}

            /* =============================================
               PHẦN 9: ĐỒNG BỘ MÀU CHỮ (LABEL, CAPTION, SLIDER)
               ============================================= */
            /* 1. Label của Slider (Number of results), Selectbox, Radio */
            [data-testid="stSidebar"] label[data-testid="stWidgetLabel"] p,
            [data-testid="stSidebar"] .stSlider label,
            [data-testid="stSidebar"] .stSelectbox label p,
            [data-testid="stSidebar"] .stRadio label p {{
                color: #e6e6e6 !important; /* Màu xám sáng đồng bộ */
                font-weight: 500 !important;
            }}

            /* 2. Dòng caption (NO DATA FOUND) */
            [data-testid="stSidebar"] [data-testid="stCaptionContainer"],
            [data-testid="stSidebar"] .stCaption {{
                color: #e6e6e6 !important;
                opacity: 0.8 !important;
            }}

            /* 3. Số hiển thị của Slider (số 3, 5, 10...) */
            [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{
                color: {neon_purple} !important; /* Giữ màu tím cho số liệu */
            }}

            /* =============================================
               PHẦN 10: TIÊU ĐỀ EXPANDER (HEADER)
               ============================================= */
            [data-testid="stSidebar"] [data-testid="stExpander"] summary p {{
                color: #ffffff !important;
                font-weight: 700 !important;
                font-size: 1.1rem !important;
            }}
            
            [data-testid="stSidebar"] [data-testid="stExpander"] summary svg {{
                fill: #ffffff !important;
                color: #ffffff !important;
            }}
            
            [data-testid="stSidebar"] [data-testid="stExpander"] summary {{
                background-color: transparent !important;
                border: none !important;
            }}

            /* =============================================
               PHẦN 11: DROPDOWN & INPUT BOX (MÀU TỐI)
               ============================================= */
            /* Hộp chọn chính (Selectbox Main) */
            [data-testid="stSidebar"] [data-baseweb="select"] > div {{
                background-color: #1a1c24 !important;
                color: white !important;
                border-color: #555 !important;
            }}
            [data-testid="stSidebar"] [data-baseweb="select"] span {{
                color: white !important;
            }}
            [data-testid="stSidebar"] [data-baseweb="select"] svg {{
                fill: white !important;
            }}

            /* Menu thả xuống (Dropdown List) */
            ul[data-testid="stSelectboxVirtualDropdown"] {{
                background-color: #1a1c24 !important;
                border: 1px solid #444 !important;
            }}
            ul[data-testid="stSelectboxVirtualDropdown"] li {{
                background-color: #1a1c24 !important;
                color: #ffffff !important;
                border-bottom: 1px solid #2d2f36 !important;
            }}
            ul[data-testid="stSelectboxVirtualDropdown"] li:hover,
            ul[data-testid="stSelectboxVirtualDropdown"] li[aria-selected="true"] {{
                background-color: {neon_purple} !important;
                color: #ffffff !important;
            }}

            /* =============================================
               [FIX ULTIMATE] PHẦN 12: SỬA MÀU THANH TRẠNG THÁI (SCANNING...)
               ============================================= */
            
            /* 1. Thiết lập màu nền TỐI cho lớp vỏ ngoài cùng */
            div[data-testid="stStatusWidget"] {{
                background-color: #1a1c24 !important; /* Nền tối */
                border: 1px solid {neon_purple} !important;  /* Viền Tím Neon */
                border-radius: 8px !important;
            }}

            /* 2. KỸ THUẬT "NUCLEAR": Ép TẤT CẢ các phần tử con bên trong phải trong suốt */
            div[data-testid="stStatusWidget"] * {{
                background-color: transparent !important; /* Xóa nền trắng */
                color: #ffffff !important;                /* Ép chữ trắng */
            }}

            /* 3. Đảm bảo Icon (Spinner/Check) cũng phải màu trắng */
            div[data-testid="stStatusWidget"] svg,
            div[data-testid="stStatusWidget"] svg > * {{
                fill: #ffffff !important;
                stroke: #ffffff !important;
                color: #ffffff !important;
            }}
            
            /* 4. (Phòng hờ) Nếu Streamlit dùng thẻ 'header' cho dòng tiêu đề */
            div[data-testid="stStatusWidget"] header {{
                background-color: transparent !important;
            }}
        </style>
        """

# --- B. LIGHT MODE (GEN DESIGN: LIGHT EDITION - ĐÃ FIX FONT & MÀU SLIDER) ---
    else:
        # Bảng màu Light Mode (Giữ nguyên các biến màu Neon để làm điểm nhấn)
        neon_blue = "#00f2fe"
        neon_purple = "#bd00ff"
        neon_pink = "#ff0080"
        
        # Nền sáng & Chữ tối
        bg_light_gradient = "linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)" 
        glass_bg_light = "rgba(255, 255, 255, 0.75)" 
        text_dark = "#1a1c24" # Màu đen xám đậm (Dùng cho chữ chính)
        text_gray = "#4b5563" # Màu xám đậm (Dùng cho chữ phụ)
        
        # Viền Hologram phiên bản sáng
        hologram_border = f"linear-gradient(135deg, {neon_blue}, {neon_purple}, {neon_pink})"

        return f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;800;900&display=swap');

            /* --- 1. CORE SETUP --- */
            .stApp {{
                background: {bg_light_gradient};
                background-size: cover;
                font-family: 'Rajdhani', sans-serif !important;
                color: {text_dark};
                font-weight: 600;
            }}
            
            /* SCROLLBAR (Light Version) */
            ::-webkit-scrollbar {{ width: 8px; }}
            ::-webkit-scrollbar-track {{ background: #f0f0f0; }}
            ::-webkit-scrollbar-thumb {{ background: linear-gradient(to bottom, {neon_blue}, {neon_purple}); border-radius: 10px; }}

            /* --- 2. SIDEBAR --- */
            section[data-testid="stSidebar"] {{
                background-color: {glass_bg_light};
                backdrop-filter: blur(20px);
                border-right: 1px solid rgba(0, 0, 0, 0.1);
                box-shadow: 5px 0 30px rgba(0,0,0,0.05);
            }}
            /* Sidebar Titles */
            .sidebar-title {{ 
                background: linear-gradient(to right, {neon_blue}, {neon_purple}); 
                -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                font-weight: 900; letter-spacing: 2px; text-transform: uppercase;
                filter: drop-shadow(0 0 2px rgba(189, 0, 255, 0.2)); /* Bóng nhẹ hơn Dark */
            }}
            /* 1. [GPT-4O-MINI] - Màu Tím Đậm + Phát sáng Tím */
            .main-title-container + div span:nth-of-type(1) {{
                color: #7c3aed !important; /* Tím đậm (Violet) để đọc rõ */
                font-weight: 900 !important;
                background: none !important;
                -webkit-text-fill-color: initial !important;
                animation: glow-pulse-purple 2s infinite ease-in-out;
            }}
            
            /* 2. ONLINE - Màu Xanh Lá Đậm + Phát sáng Xanh */
            .main-title-container + div span:nth-of-type(2) {{
                color: #059669 !important; /* Xanh lá đậm (Emerald) */
                font-weight: 900 !important;
                background: none !important;
                -webkit-text-fill-color: initial !important;
                animation: glow-pulse-green 2s infinite ease-in-out;
            }}
            /* --- 3. TYPOGRAPHY (GIỮ NGUYÊN FORM, ĐỔI MÀU) --- */
            .main-title-container {{ text-align: center; padding: 60px 0 40px 0; position: relative; overflow: hidden; }}
            
            .main-title {{
                font-size: 5rem; font-weight: 900; line-height: 1; text-transform: uppercase;
                letter-spacing: 5px;
                /* Chữ màu tối có hiệu ứng bóng nhẹ */
                color: {text_dark}; 
                text-shadow: 2px 2px 0px rgba(0,0,0,0.1); 
                animation: subtle-glitch 5s infinite alternate;
            }}
            @keyframes subtle-glitch {{ 0% {{ transform: skew(0deg); }} 20% {{ transform: skew(-1deg); }} 40% {{ transform: skew(0.5deg); }} 100% {{ transform: skew(0deg); }} }}
            
            .sub-title {{
                font-size: 1.3rem; color: {text_gray}; font-weight: 700;
                text-transform: uppercase; letter-spacing: 3px; margin-top: 15px;
                border-bottom: 3px solid {neon_purple}; display: inline-block; padding-bottom: 5px;
            }}

            /* Dòng trạng thái (Status Line) */
            .main-title-container + div {{ color: {text_dark} !important; font-weight: 700 !important; text-shadow: none !important; }}

            /* Tiêu đề chính: DỰ ÁN NUÔI TÔI (Light Mode) */
            .main-title {{
                font-size: 5rem; 
                font-weight: 900; 
                line-height: 1; 
                text-transform: uppercase;
                letter-spacing: 5px;

                /* 1. HIỆU ỨNG ÓNG ÁNH (Gradient chạy mượt mà) */
                /* Pha trộn giữa màu Đen (chủ đạo) và các màu Neon để tạo vệt sáng */
                background: linear-gradient(
                    to right, 
                    #1a1c24 0%, 
                    #1a1c24 10%, 
                    #00f2fe 65%, /* Xanh Neon */
                    #bd00ff 100%, /* Tím Neon */
                    #ff0080 105%, /* Hồng Neon */
                    #1a1c24 70%, 
                    #1a1c24 100%
                );
                background-size: 200% auto;
                
                /* Cắt nền theo khuôn chữ */
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                
                /* Animation cho màu chạy */
                animation: shimmer-text 4s linear infinite;

                /* 2. HIỆU ỨNG PHÁT SÁNG HIỆN ĐẠI (Neon Glow) */
                /* Dùng filter drop-shadow giúp chữ phát sáng ngay cả khi text-fill là transparent */
                filter: drop-shadow(0 0 2px rgba(189, 0, 255, 0.3)) 
                        drop-shadow(0 0 10px rgba(0, 242, 254, 0.4));
            }}
            /* --- 4. INPUT FIELD (LIGHT THEME) --- */
            .stTextInput > div > div > input {{
                border-radius: 8px; padding: 18px 30px; font-size: 1.2rem; font-family: 'Rajdhani', monospace; letter-spacing: 1px; font-weight: 700;
                background: #ffffff; /* Nền trắng */
                color: {text_dark};   /* Chữ đen */
                border: 2px solid #ccc;
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
                transition: all 0.3s ease;
                caret-color: #000000 !important; /* Con trỏ đen */
            }}
            .stTextInput > div > div > input:focus {{
                border-color: {neon_blue};
                box-shadow: 0 0 15px rgba(0, 242, 254, 0.3);
                background: #ffffff;
            }}
            .stTextInput input::placeholder {{ 
                font-size: 1rem !important; font-weight: 400 !important; opacity: 0.8 !important;
                font-style: italic !important; color: #999 !important; 
            }}

            /* [MỚI] KHUNG BAO NGOÀI FORM SEARCH */
            [data-testid="stForm"] {{
                border: 2px solid #1a1c24 !important; /* Viền đen đậm */
                background-color: rgba(255, 255, 255, 0.4) !important;
                border-radius: 16px !important;
                box-shadow: 4px 4px 0px rgba(0,0,0,0.1) !important;
            }}

            /* --- 5. BUTTONS (GIỮ NGUYÊN NÚT VŨ TRỤ VÌ NÓ ĐẸP) --- */
            [data-testid="stForm"] button {{
                background: linear-gradient(90deg, #6a11cb, #2575fc, #ff0080, #6a11cb);
                background-size: 300% 100%; color: white !important; border: none !important; font-weight: 800 !important; font-size: 1rem !important;
                text-transform: uppercase; letter-spacing: 2px; border-radius: 50px !important;
                height: 3.8em !important; margin-top: 0px !important;
                animation: cosmic-shift 8s linear infinite; position: relative; overflow: hidden;
                
                /* Thêm viền đen cho nút ở chế độ sáng để nổi bật */
                border: 2px solid #000000 !important;
                box-shadow: 4px 4px 0px rgba(0,0,0,0.8) !important;
            }}
            [data-testid="stForm"] button::before {{
                content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
                background: linear-gradient(120deg, transparent, rgba(255,255,255,0.4), transparent);
                transform: skewX(-25deg); animation: shine-flow 4s infinite linear;
            }}
            [data-testid="stForm"] button:hover {{
                background-size: 150% 100%; transform: translate(-2px, -2px);
                box-shadow: 6px 6px 0px rgba(0,0,0,1) !important;
            }}
            [data-testid="stForm"] button:active {{
                transform: translate(2px, 2px); box-shadow: 0px 0px 0px rgba(0,0,0,1) !important;
            }}
            @keyframes cosmic-shift {{ 0% {{ background-position: 0% 50%; }} 100% {{ background-position: 100% 50%; }} }}
            @keyframes shine-flow {{ 0% {{ left: -100%; opacity: 0; }} 20% {{ left: 200%; opacity: 0; }} 100% {{ left: 200%; opacity: 0; }} }}

            /* Chips */
            div.stButton > button {{
                background: rgba(0,0,0,0.05) !important;
                border: 1px solid #ccc !important;
                color: {text_dark} !important;
                border-radius: 20px !important; font-weight: 700 !important;
            }}
            div.stButton > button:hover {{
                background: {neon_purple} !important; color: white !important;
            }}

            /* --- 6. EXPANDER & DROPDOWN (LIGHT THEME) --- */
            [data-testid="stSidebar"] [data-testid="stExpander"] {{
                border: 1px solid rgba(0,0,0,0.1) !important;
                border-radius: 8px !important;
                box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
                background-color: #ffffff !important;
                margin-bottom: 0px !important; overflow: hidden !important;
            }}
            [data-testid="stSidebar"] [data-testid="stExpander"]:hover {{
                border: 1px solid {neon_purple} !important;
            }}
            [data-testid="stSidebar"] [data-testid="stExpander"] summary p {{ color: {text_dark} !important; font-weight: 700 !important; font-size: 1.1rem !important; }}
            [data-testid="stSidebar"] [data-testid="stExpander"] summary svg {{ fill: {text_dark} !important; color: {text_dark} !important; }}
            [data-testid="stSidebar"] [data-testid="stExpander"] summary {{ background-color: transparent !important; border: none !important; }}
            [data-testid="stSidebar"] [data-testid="stExpander"] [data-testid="stExpanderContent"] {{ color: {text_dark} !important; padding-bottom: 10px !important; }}

            /* Dropdown */
            [data-testid="stSidebar"] [data-baseweb="select"] > div {{
                background-color: #ffffff !important; color: {text_dark} !important; border-color: #ccc !important;
            }}
            [data-testid="stSidebar"] [data-baseweb="select"] span {{ color: {text_dark} !important; }}
            [data-testid="stSidebar"] [data-baseweb="select"] svg {{ fill: {text_dark} !important; }}
            ul[data-testid="stSelectboxVirtualDropdown"] {{ background-color: #ffffff !important; border: 1px solid {neon_purple} !important; }}
            ul[data-testid="stSelectboxVirtualDropdown"] li {{ background-color: #ffffff !important; color: #333 !important; border-bottom: 1px solid #eee !important; }}
            ul[data-testid="stSelectboxVirtualDropdown"] li:hover {{ background-color: {neon_purple} !important; color: #ffffff !important; }}

            /* --- 7. LABELS (ĐÃ SỬA THEO YÊU CẦU CỦA BẠN) --- */
            
            /* 1. Tiêu đề Widget (IN ĐẬM) */
            [data-testid="stSidebar"] label[data-testid="stWidgetLabel"] p,
            [data-testid="stSidebar"] .stSelectbox label p {{
                color: {text_dark} !important; font-weight: 800 !important;
            }}

            /* 2. [FIX] Lựa chọn Radio (MẢNH/MỜ - Font thường) */
            [data-testid="stSidebar"] .stRadio label p {{
                color: {text_dark} !important; 
                font-weight: 400 !important; /* Không in đậm */
            }}

            /* 3. [FIX] Slider Label (MÀU ĐEN - Giống No Data Found) */
            [data-testid="stSidebar"] .stSlider label p {{
                color: {text_dark} !important; /* Màu đen */
                font-weight: 600 !important;
            }}
            
            /* 4. No Data Found (MÀU ĐEN ĐẬM) */
            [data-testid="stSidebar"] .stCaption, [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {{
                color: {text_dark} !important; font-weight: 700 !important; opacity: 1 !important; text-transform: uppercase !important;
            }}

            /* [FIX] 2. SLIDER LABEL "Number of results" -> ÉP SANG MÀU ĐEN */
            /* Dùng selector dài hơn để ghi đè mọi màu tím cũ */
            [data-testid="stSidebar"] .stSlider label[data-testid="stWidgetLabel"] p,
            [data-testid="stSidebar"] .stSlider [data-testid="stMarkdownContainer"] p {{
                color: {text_dark} !important; /* Đen đậm */
                font-weight: 550 !important;
            }}
            /* Số Slider (Vẫn giữ tím cho đẹp) */
            [data-testid="stSidebar"] .stSlider [data-testid="stMarkdownContainer"] p {{ color: {neon_purple} !important; }}

            /* --- 8. RESULT CARDS & ACTION BUTTONS (FIX: NÚT VŨ TRỤ Y HỆT DARK MODE) --- */
            .result-card-container {{
                background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(20px);
                border-radius: 16px; position: relative;
                border: 1px solid rgba(189, 0, 255, 0.15);
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
                margin-bottom: 35px; overflow: hidden; transition: all 0.3s ease;
            }}
            /* Hiệu ứng viền hologram mờ phía sau */
            .result-card-container::before {{
                content: ''; position: absolute; top: -1px; bottom: -1px; left: -1px; right: -1px;
                background: {hologram_border};
                z-index: -1; border-radius: 16px; filter: blur(10px); opacity: 0.3;
            }}
            .result-card-container:hover {{
                transform: translateY(-5px) scale(1.01);
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
                border-color: rgba(189, 0, 255, 0.4);
            }}
            
            .rank-badge {{
                position: absolute; top: 0; left: 0;
                background: linear-gradient(135deg, {neon_purple}, {neon_pink});
                color: white; padding: 10px 20px; border-bottom-right-radius: 16px;
                font-weight: 900; font-size: 1.1rem; box-shadow: 0 5px 15px rgba(0,0,0,0.3); z-index: 2;
            }}
            .card-content {{ padding: 50px 30px 30px 30px; position: relative; z-index: 1; }}
            
            .course-title {{
                font-size: 1.8rem; font-weight: 900; 
                background: linear-gradient(to right, #1a1c24, #4a5568); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                text-transform: uppercase; margin-bottom: 15px;
            }}
            
            /* Badges (Instructor, Duration...) */
            .badge {{ background: #f0f2f6; border: 1px solid #ccc; color: {text_dark}; padding: 8px 18px; border-radius: 8px; font-weight: 800; }}

            /* [FIX QUAN TRỌNG] GROUP NÚT BẤM - STYLE CYBERPUNK */
            .custom-btn-group {{ display: flex; gap: 20px; margin-top: 35px; }}

            .custom-btn {{
                flex: 1; display: inline-flex; justify-content: center; align-items: center;
                padding: 16px 25px; border-radius: 8px;
                font-weight: 900 !important; /* Đậm y hệt bên Dark */
                font-size: 1rem; text-transform: uppercase; letter-spacing: 2px;
                text-decoration: none !important;
                transition: all 0.3s ease;
                /* Cắt góc vát chéo (Polygon) y hệt Dark Mode */
                clip-path: polygon(5% 0%, 100% 0, 95% 100%, 0% 100%);
            }}

            /* 1. NÚT DOWNLOAD: MÀU XANH GRADIENT (Y HỆT ẢNH MẪU) */
            .btn-download {{
                background: linear-gradient(135deg, #11998e, #38ef7d);
                color: #000000 !important; /* Chữ đen trên nền xanh sáng */
                border: none !important;
                box-shadow: 0 0 20px rgba(56, 239, 125, 0.4); /* Glow xanh */
            }}
            .btn-download:hover {{
                transform: translateY(-3px);
                box-shadow: 0 0 30px rgba(56, 239, 125, 0.7);
                color: #000000 !important;
            }}

            /* 2. NÚT SOURCE LINK: VIỀN ĐEN ĐẬM (CHO NỔI TRÊN NỀN TRẮNG) */
            .btn-link {{
                background: transparent;
                color: #1a1c24 !important; /* Chữ đen đậm */
                border: 2px solid #1a1c24 !important; /* Viền đen đậm sắc nét */
            }}
            .btn-link:hover {{
                border-color: {neon_purple} !important;
                color: {neon_purple} !important;
                background: rgba(189, 0, 255, 0.05);
                box-shadow: 0 0 15px rgba(189, 0, 255, 0.2);
                transform: translateY(-3px);
            }}
            
            /* --- 8. STATUS WIDGET (FIX: LUÔN DÙNG GIAO DIỆN TỐI CHO DỄ ĐỌC) --- */
            /* Ép về giao diện Dark Mode: Nền đen, Viền tím, Chữ trắng */
/* --- STATUS WIDGET (DARK MODE - DESIGN MỚI) --- */
            div[data-testid="stStatusWidget"] {{
                background-color: #0e1117 !important; /* Nền đen sâu */
                border: 1px solid #bd00ff !important; /* Viền Tím Neon */
                border-radius: 12px !important;
                padding: 10px 15px !important;
                /* Hiệu ứng phát sáng nhẹ */
                box-shadow: 0 0 15px rgba(189, 0, 255, 0.15) !important; 
            }}
            /* Chữ trạng thái */
            div[data-testid="stStatusWidget"] summary span {{
                color: #bd00ff !important; /* Chữ Tím Neon rực rỡ */
                font-weight: 700 !important;
                font-size: 1.1rem !important;
                letter-spacing: 1px !important;
            }}
            /* Icon (Spinner/Check) */
            div[data-testid="stStatusWidget"] svg {{
                fill: #00f2fe !important; /* Icon màu Xanh Neon */
                color: #00f2fe !important;
            }}

            /* --- 9. RESULT CARDS --- */
            .result-card-container {{
                background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(20px);
                border-radius: 16px; position: relative;
                border: 1px solid rgba(189, 0, 255, 0.15); /* Viền tím nhạt */
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
                margin-bottom: 35px; overflow: hidden; transition: all 0.3s ease;
            }}
            .result-card-container::before {{
                content: ''; position: absolute; top: -1px; bottom: -1px; left: -1px; right: -1px;
                background: {hologram_border};
                z-index: -1; border-radius: 16px; filter: blur(10px); opacity: 0.3;
            }}
            .result-card-container:hover {{
                transform: translateY(-5px) scale(1.01);
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
                border-color: rgba(189, 0, 255, 0.4);
            }}
            
            .rank-badge {{
                position: absolute; top: 0; left: 0;
                background: linear-gradient(135deg, {neon_purple}, {neon_pink});
                color: white; padding: 10px 20px; border-bottom-right-radius: 16px;
                font-weight: 900; font-size: 1.1rem; box-shadow: 0 5px 15px rgba(0,0,0,0.3); z-index: 2;
            }}
            .card-content {{ padding: 50px 30px 30px 30px; position: relative; z-index: 1; }}
            .course-title {{
                font-size: 1.8rem; font-weight: 900; color: {text_dark};
                margin-bottom: 15px; line-height: 1.2; text-transform: uppercase;
                background: none; -webkit-text-fill-color: initial;
            }}
            .badge {{ background: #f0f2f6; border: 1px solid #ccc; color: {text_dark}; padding: 8px 18px; border-radius: 8px; font-weight: 800; }}
            .btn-download {{ background: linear-gradient(135deg, #11998e, #38ef7d); color: #fff !important; box-shadow: 0 0 20px rgba(56, 239, 125, 0.3); }}
            .btn-link {{ background: transparent; color: {text_dark} !important; border: 1px solid #999; }}
            .btn-link:hover {{ border-color: {neon_purple}; color: {neon_purple} !important; }}
            
            /* --- History Items (Light Mode - Fix Font giống Dark Mode) --- */
            /* --- 6. Chips (History Buttons - Hiện đại hóa & Đổ bóng 3D) --- */
            div.stButton > button {{
                /* Hình dáng viên thuốc bo tròn hiện đại */
                border-radius: 20px !important;
                padding: 10px 24px !important;
                border: 1px solid rgba(0, 0, 0, 0.5) !important; /* Viền trắng mờ */

                /* Nền gradient sáng nhẹ tạo độ sâu */
                background: linear-gradient(145deg, #ffffff, #e6e6e6) !important;
                color: {text_dark} !important;
                font-weight: 700 !important;
                font-size: 0.95rem !important;

                /* [TÍNH NĂNG CHÍNH] ĐỔ BÓNG MỀM MẠI (Soft 3D Shadow) */
                /* Tạo cảm giác nút nổi lên khỏi nền */
                box-shadow: 5px 5px 10px rgba(0,0,0,0.1),
                            -5px -5px 10px rgba(255,255,255,0.8) !important;

                transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important; /* Chuyển động mượt */
                display: inline-flex; align-items: center; justify-content: center;
            }}

            /* Tô màu vàng cam cho icon tia sét để nổi bật */
            div.stButton > button p span:first-of-type {{
                 color: #f59e0b !important; /* Màu vàng cam */
                 font-size: 1.1em !important;
                 margin-right: 6px !important;
            }}

            /* Hiệu ứng khi di chuột vào (Hover) - Bay lên và sáng hơn */
            div.stButton > button:hover {{
                transform: translateY(-3px) !important; /* Nút bay lên nhẹ */
                background: linear-gradient(145deg, #ffffff, #f0f0f0) !important; /* Nền sáng hơn */
                color: {neon_purple} !important; /* Chữ đổi màu tím neon */
                border-color: {neon_purple} !important;

                /* Bóng đổ sâu hơn và rộng hơn khi bay lên */
                box-shadow: 8px 8px 15px rgba(189, 0, 255, 0.15),
                            -8px -8px 15px rgba(255,255,255,1) !important;
            }}

            /* Hiệu ứng khi bấm (Active) - Lún xuống tạo cảm giác thật */
            div.stButton > button:active {{
                transform: translateY(1px) scale(0.98) !important; /* Lún xuống và thu nhỏ nhẹ */
                /* Đổi sang bóng đổ vào trong (Inset shadow) */
                box-shadow: inset 3px 3px 5px rgba(0,0,0,0.1),
                            inset -3px -3px 5px rgba(255,255,255,0.7) !important;
                background: #e6e6e6 !important;
            }}
            /* --- History Items (Fix: Font Rajdhani y hệt Dark Mode, nhưng màu Đen) --- */
            .history-item {{
                color: #1a1c24 !important; /* Chữ màu Đen Đậm (High Contrast) */
                border-bottom: 1px dashed #ccc !important; /* Gạch kẻ đứt quãng */
                padding: 8px 0;
                
                /* [QUAN TRỌNG] COPY FONT Y HỆT BÊN DARK MODE */
                font-family: 'Rajdhani', monospace !important; 
                font-weight: 600 !important; 
                font-size: 1rem !important;
            }}
            
            /* Hover vào thì đổi màu tím */
            .history-item:hover {{
                color: {neon_purple} !important; 
                cursor: pointer;
            }}
        """
# --- CÁC HÀM HTML (GIỮ NGUYÊN) ---
def get_donation_html():
    return """
    <div style="text-align: center; margin-bottom: 20px;">
        <span style="
            font-family: 'Nunito Sans', sans-serif;
            font-size: 1.5rem; font-weight: 900; letter-spacing: 2px;
            text-transform: uppercase;
            background: linear-gradient(to right, #bd00ff, #ff0080);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            text-shadow: 0 0 15px rgba(189, 0, 255, 0.5);
        ">
            Mọi lòng hảo tâm xin vui lòng gửi về 2 số tài khoản phía dưới
        </span>
    </div>
    """

def get_header_html(model_name):
    # Lưu ý: Phần style inline ở đây có thể hiện màu #8B949E (xám) ở cả 2 chế độ, 
    # nhưng vì nó là tiêu đề phụ nên chấp nhận được ở Light Mode (vẫn đọc tốt).
    return f"""
    <div class="main-title-container" style="padding: 20px 0;"> 
        <div class="main-title" style="font-size: 4rem;">DỰ ÁN NUÔI TÔI</div>
        <div class="sub-title">EXPLORE KNOWLEDGE ACROSS THE DATA UNIVERSE</div>
    </div>
    <div style="
        text-align: center; color: #8B949E; margin-top: -20px; 
        font-family: monospace; letter-spacing: 2px; font-weight: 700;
        text-shadow: 0 0 5px rgba(0,0,0,0.1);
    ">
        OPERATING VIA NEURAL NET: <span style="color: #00f2fe; text-shadow: 0 0 10px #00f2fe;">[{model_name.upper()}]</span> STATUS: <span style="color: #38ef7d;">ONLINE</span>
    </div>
    """

def get_result_card_html(i, title, instructor, duration, size, source_url, original_link):
    return f"""
    <div class="result-card-container">
        <div class="rank-badge">RANK #{i+1}</div>
        <div class="card-content">
            <div class="course-title">{title}</div>
            <div class="meta-tags">
                <span class="badge badge-instructor"><i>👤</i> {instructor}</span>
                <span class="badge badge-duration"><i>⏱️</i> {duration}</span>
                <span class="badge badge-size"><i>💾</i> {size}</span>
            </div>
            
            <div class="custom-btn-group">
                <a href="{source_url}" target="_blank" class="custom-btn btn-download">DOWNLOAD FREE ⬇️</a>
                <a href="{original_link}" target="_blank" class="custom-btn btn-link">SOURCE UPLINK 🌐</a>
            </div>
        </div>
    </div>
    """
