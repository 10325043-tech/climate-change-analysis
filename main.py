import streamlit as st
import random

# --- CORE SYSTEM CONFIG ---
st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide", initial_sidebar_state="collapsed")

# --- MASTER LABORATORY GRAPHICS ENGINE (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');

    /* Lock layout to avoid page scrolling completely */
    html, body, [data-testid="stAppViewContainer"] {
        max-height: 100vh;
        overflow: hidden;
        background: #000205;
        color: #00f2ff;
        font-family: 'Share Tech Mono', monospace;
    }

    /* -------------------------------------------
       PAGE 1: CINEMATIC GATEWAY BACKGROUND
       ------------------------------------------- */
    .landing-screen {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background: linear-gradient(rgba(0, 8, 20, 0.8), rgba(0, 2, 5, 0.95)), 
                    url('https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=1974');
        background-size: cover; background-position: center;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        z-index: 1;
    }

    /* -------------------------------------------
       INFINITE LOOP SEAMLESS LED MARQUEE
       ------------------------------------------- */
    .led-marquee-container {
        width: 100%; height: 42px; background: #000; 
        border-top: 2px solid #ff0055; border-bottom: 2px solid #ff0055;
        overflow: hidden; position: relative; display: flex; align-items: center;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.35);
    }
    .led-marquee-track { display: flex; width: 200%; animation: led-scroll 20s linear infinite; }
    .led-marquee-content {
        width: 50%; display: flex; justify-content: space-around; white-space: nowrap;
        font-family: 'Orbitron', sans-serif; font-weight: 700; font-size: 1.15rem; color: #ff0055;
        text-shadow: 0 0 8px #ff0055;
    }
    @keyframes led-scroll { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

    /* -------------------------------------------
       FIXED: GLOWING NATIVE STREAMLIT BUTTONS
       ------------------------------------------- */
    div.stButton > button {
        background: rgba(0, 242, 255, 0.05) !important;
        border: 2px solid #00f2ff !important;
        color: #ffffff !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 2px !important;
        border-radius: 8px !important;
        padding: 15px 25px !important;
        width: 100% !important;
        text-align: center !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.2) !important;
        transition: all 0.25s ease-in-out !important;
    }
    div.stButton > button:hover {
        border-color: #ff0055 !important;
        color: #ffffff !important;
        background: rgba(255, 0, 85, 0.15) !important;
        box-shadow: 0 0 25px rgba(255, 0, 85, 0.6) !important;
        transform: scale(1.02);
    }
    
    /* Specific styling for Card Selection in Page 2 */
    .card-container {
        background: rgba(0, 242, 255, 0.02);
        border: 1px solid rgba(0, 242, 255, 0.1);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .active-card {
        border-color: #ff0055 !important;
        box-shadow: 0 0 20px rgba(255, 0, 85, 0.2) !important;
    }

    /* Pod Typography Inside Cards */
    .pod-title { font-family: 'Orbitron'; font-size: 1.4rem; font-weight: 700; color: #fff; margin-bottom: 5px;}
    .pod-grid { display: flex; justify-content: space-between; font-size: 0.9rem; color: #00f2ff; margin-bottom: 12px; }
    .pod-status-alert { color: #ff0055; font-weight: bold; letter-spacing: 1px; }

    /* -------------------------------------------
       PAGE 3: EXPERIMENTAL LABORATORY SYSTEM
       ------------------------------------------- */
    .lab-dashboard {
        height: calc(100vh - 160px);
        border: 2px solid #00f2ff; border-radius: 16px; padding: 30px;
        background: rgba(0, 8, 22, 0.65); backdrop-filter: blur(15px);
        box-shadow: inset 0 0 50px rgba(0, 242, 255, 0.15), 0 0 30px rgba(0,242,255,0.05);
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .lab-banner {
        display: flex; justify-content: space-between; align-items: center;
        border-bottom: 2px solid rgba(0, 242, 255, 0.25); padding-bottom: 15px;
    }
    .lab-main-layout { display: flex; gap: 25px; margin: 20px 0; height: calc(100% - 300px); }
    .lab-visual { width: 45%; object-fit: cover; border: 1px solid rgba(0,242,255,0.3); border-radius: 10px; }
    .lab-logger {
        width: 55%; background: rgba(0,0,0,0.5); padding: 20px; border-radius: 10px;
        font-size: 0.95rem; color: #ccc; line-height: 1.6; border: 1px solid rgba(255,255,255,0.02);
    }

    /* System clean up styles */
    header, footer, [data-testid="stSidebar"] { visibility: hidden; }
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    </style>
""", unsafe_allow_html=True)

# --- SYSTEM STATES & ROUTING ---
if 'page_router' not in st.session_state: st.session_state.page_router = 'p1_landing'
if 'selected_continent' not in st.session_state: st.session_state.selected_continent = 'ASIA'

# --- DATABASE ARCHIVE ---
climate_archive = {
    "ASIA": {"temp": "+1.64°C", "co2": "418 PPM", "risk": "CRITICAL", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=800"},
    "EUROPE": {"temp": "+2.21°C", "co2": "415 PPM", "risk": "EXTREME", "img": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=800"},
    "NORTH AMERICA": {"temp": "+1.89°C", "co2": "421 PPM", "risk": "HIGH", "img": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800"},
    "SOUTH AMERICA": {"temp": "+1.32°C", "co2": "409 PPM", "risk": "STABLE", "img": "https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?w=800"},
    "AFRICA": {"temp": "+1.58°C", "co2": "411 PPM", "risk": "HIGH", "img": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=800"},
    "OCEANIA": {"temp": "+1.15°C", "co2": "413 PPM", "risk": "STABLE", "img": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?w=800"}
}

# ==============================================================================
# TRANG 1: CINEMATIC LANDING GATEWAY
# ==============================================================================
if st.session_state.page_router == 'p1_landing':
    st.markdown("""
        <div class="landing-screen">
            <p style="font-family:'Orbitron'; color:#ff0055; letter-spacing:14px; font-weight:700; margin-bottom:5px;">CODETOOPIA PROJECT NETWORK</p>
            <h1 style="font-family:'Orbitron'; font-size:6rem; font-weight:900; color:#00f2ff; text-shadow: 0 0 30px #00f2ff, 0 0 60px #00f2ff; margin:0;">CLIMATE VAULT</h1>
            <p style="color:#666; font-size:1.1rem; letter-spacing:3px; margin-top:15px; max-width:700px; text-align:center; line-height:1.6; margin-bottom:40px;">
                DECRYPTION KEY COMPLETED. ENTER QUANTUM ARCHIVE PROTOCOL TO REVIEW GLOBAL ANOMALIES.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Đặt nút bấm ra ngoài thẻ div tuyệt đối để Streamlit bắt được sự kiện click
    _, click_box, _ = st.columns([1.8, 1.2, 1.8])
    with click_box:
        if st.button("INITIALIZE SYSTEM", key="enter_p1"):
            st.session_state.page_router = 'p2_console'
            st.rerun()

# ==============================================================================
# TRANG 2: THE VAULT SELECTION CONSOLE
# ==============================================================================
elif st.session_state.page_router == 'p2_console':
    st.markdown("""
        <div class="led-marquee-container">
            <div class="led-marquee-track">
                <div class="led-marquee-content">
                    <span>✦ SYSTEM SECURE // MONITORING CO2 LIFELINE</span>
                    <span>✦ CHOOSE CODETOOPIA TARGET CONTINENT SECTOR</span>
                    <span>✦ COMPILING HISTORICAL TEMPERATURE LOGS</span>
                    <span>✦ ARCHIVE SYNCED ONLINE</span>
                </div>
                <div class="led-marquee-content">
                    <span>✦ SYSTEM SECURE // MONITORING CO2 LIFELINE</span>
                    <span>✦ CHOOSE CODETOOPIA TARGET CONTINENT SECTOR</span>
                    <span>✦ COMPILING HISTORICAL TEMPERATURE LOGS</span>
                    <span>✦ ARCHIVE SYNCED ONLINE</span>
                </div>
            </div>
        </div>
        <br>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='font-family:Orbitron; text-align:center; color:#fff; letter-spacing:4px; margin: 0 0 20px 0;'>QUANTUM CONSOLE: SELECT SECTOR</h2>", unsafe_allow_html=True)
    
    # Vẽ Ma trận Thẻ 3x2 bằng Columns
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    row2_col1, row2_col2, row2_col3 = st.columns(3)
    all_grid_slots = [row1_col1, row1_col2, row1_col3, row2_col1, row2_col2, row2_col3]
    
    for idx, (zone, info) in enumerate(climate_archive.items()):
        with all_grid_slots[idx]:
            is_active_class = "active-card" if st.session_state.selected_continent == zone else ""
            
            # Khung thông tin tĩnh
            st.markdown(f"""
                <div class="card-container {is_active_class}">
                    <div class="pod-title">{zone}</div>
                    <div class="pod-grid">
                        <span>BASE LEVEL: {info['temp']}</span>
                        <span class="pod-status-alert">{info['risk']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Nút chọn Native nằm ngay dưới hộp thông tin để nhấn kích hoạt
            if st.button(f"CONNECT TO {zone}", key=f"btn_{zone}"):
                st.session_state.selected_continent = zone
                st.rerun()
            
    # Nút chuyển tiếp lớn dẫn thẳng vào Trang 3 nằm ở đáy màn hình
    st.markdown("<br>", unsafe_allow_html=True)
    _, action_center, _ = st.columns([1.5, 1, 1.5])
    with action_center:
        current_sel = st.session_state.selected_continent
        if st.button(f"OPEN {current_sel} RESEARCH LAB ➔", key="goto_p3"):
            st.session_state.page_router = 'p3_lab'
            st.rerun()

# ==============================================================================
# TRANG 3: THE HIGH-FIDELITY RESEARCH LABORATORY
# ==============================================================================
elif st.session_state.page_router == 'p3_lab':
    st.markdown("""
        <div class="led-marquee-container">
            <div class="led-marquee-track">
                <div class="led-marquee-content">
                    <span>✦ LABORATORY DEPLOYED // LIVE FEED SENSOR ACTIVE // ANALYZING ANOMALIES</span>
                    <span>✦ LABORATORY DEPLOYED // LIVE FEED SENSOR ACTIVE // ANALYZING ANOMALIES</span>
                </div>
            </div>
        </div>
        <br>
    """, unsafe_allow_html=True)
    
    cur_zone = st.session_state.selected_continent
    cur_data = climate_archive[cur_zone]
    
    # Giao diện Phòng Lab chính
    st.markdown(f"""
        <div class="lab-dashboard">
            <div class="lab-banner">
                <div>
                    <h1 style="font-family:Orbitron; margin:0; color:#00f2ff; letter-spacing:2px;">LABORATORY DECRYPTOR: {cur_zone}</h1>
                    <span style="color:#555; font-size:0.8rem; font-family:Orbitron;">CODETOOPIA ENVIRONMENTAL CORE DATA VISUALIZER</span>
                </div>
                <div style="text-align: right;">
                    <span style="color:#ff0055; font-size:1.8rem; font-weight:bold; font-family:Orbitron;">{cur_data['temp']}</span><br>
                    <span style="color:#888; font-size:0.85rem; letter-spacing:1px;">CO2 LEVEL: {cur_data['co2']}</span>
                </div>
            </div>
            
            <div class="lab-main-layout">
                <img src="{cur_data['img']}" class="lab-visual">
                <div class="lab-logger">
                    <b style="color:white; font-family:Orbitron; font-size:1.1rem; letter-spacing:1px;">SYSTEM CORE LOG ANALYSIS:</b><br>
                    <span style="color:#333;">-------------------------------------------------------------------------</span><br>
                    • Historical 250-year geographical data decompressed successfully.<br>
                    • Surface temperature deviation verified against pre-industrial data.<br>
                    • Carbon saturation anomaly requires urgent corrective measures.<br>
                    • Model status: Streaming core analytical database...<br>
                    • Integrity check: SECURE (99.94% accuracy rate).
                </div>
            </div>
    """, unsafe_allow_html=True)
    
    # Biểu đồ phân tích nằm gọn dưới đáy phòng Lab
    lab_chart_data = [random.uniform(1.2, 2.9) for _ in range(45)]
    st.line_chart(lab_chart_data, height=200, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Nút quay về Trang 2
    st.markdown("<br>", unsafe_allow_html=True)
    _, back_col, _ = st.columns([2.2, 1, 2.2])
    with back_col:
        if st.button("⬅ RETURN TO CONSOLE", key="back_to_p2"):
            st.session_state.page_router = 'p2_console'
            st.rerun()