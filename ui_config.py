# ui_config.py

def get_theme_css():
    # --- COLOR PALETTE: NEON ON DARK (CYBERPUNK THEME) ---
    neon_blue = "#00f2fe"
    neon_purple = "#bd00ff"
    neon_pink = "#ff0080"
    
    # New Dark Theme Colors
    # Nền chuyển sắc tối (Deep Space)
    bg_dark_gradient = "linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f0c29)"
    # Kính tối màu
    glass_bg_dark = "rgba(15, 15, 25, 0.85)" 
    # Chữ sáng màu
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
        ::placeholder {{ color: #4A5568 !important; }}

        /* --- 5. BUTTONS --- */
        button[kind="primaryFormSubmit"] {{
            background: linear-gradient(90deg, {neon_blue}, {neon_purple});
            color: white !important; font-weight: 900 !important;
            border: none; border-radius: 8px;
            height: 3.8em; letter-spacing: 2px; text-transform: uppercase;
            box-shadow: 0 0 20px rgba(189, 0, 255, 0.4);
            position: relative; overflow: hidden; z-index: 1;
            clip-path: polygon(5% 0%, 100% 0, 100% 70%, 95% 100%, 0 100%, 0% 30%);
            transition: all 0.3s ease;
        }}
        button[kind="primaryFormSubmit"]:hover {{
            box-shadow: 0 0 40px rgba(189, 0, 255, 0.7);
            transform: translateY(-3px); text-shadow: 0 0 5px white;
        }}
        
        /* CHIPS STYLING */
        div.stButton > button {{
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid {neon_purple} !important;
            color: {text_main} !important;
            border-radius: 20px !important;
            padding: 5px 20px !important;
            font-size: 0.85rem !important;
            font-weight: 700 !important;
            box-shadow: none !important;
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

        /* Action Buttons */
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
    </style>
    """

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
    return f"""
    <div class="main-title-container" style="padding: 20px 0;"> 
        <div class="main-title" style="font-size: 4rem;">DỰ ÁN NUÔI TÔI</div>
        <div class="sub-title">EXPLORE KNOWLEDGE ACROSS THE DATA UNIVERSE</div>
    </div>
    <div style="
        text-align: center; color: #8B949E; margin-top: -20px; 
        font-family: monospace; letter-spacing: 2px; font-weight: 700;
        text-shadow: 0 0 5px rgba(0,0,0,0.5);
    ">
        OPERATING VIA NEURAL NET: <span style="color: #00f2fe; text-shadow: 0 0 10px #00f2fe;">[{model_name.upper()}]</span> STATUS: <span style="color: #38ef7d;">ONLINE</span>
    </div>
    """

def get_result_card_html(i, title, instructor, duration, size, source_url, original_link):
    # instructor, duration, size, source_url, original_link giữ nguyên logic truyền vào
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