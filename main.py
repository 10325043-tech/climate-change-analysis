import streamlit as st
import random

# --- CORE SYSTEM CONFIG ---
st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide", initial_sidebar_state="collapsed")

# --- HIGH-TECH LABORATORY UI ENGINE (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');

    /* Lock scrollbar and force full-screen 100vh setup */
    html, body, [data-testid="stAppViewContainer"] {
        max-height: 100vh;
        overflow: hidden;
        background: radial-gradient(circle at center, #050d1f 0%, #000205 100%);
        color: #00f2ff;
        font-family: 'Share Tech Mono', monospace;
    }

    /* PAGE 1: CINEMATIC BACKGROUND */
    .landing-bg {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background: linear-gradient(rgba(0, 5, 15, 0.85), rgba(0, 2, 5, 0.95)), 
                    url('https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=1974');
        background-size: cover; background-position: center;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        z-index: 99999;
    }

    /* SEAMLESS INFINITE LED MARQUEE */
    .led-marquee-box {
        width: 100%; height: 40px; background: #000; 
        border-top: 2px solid #ff0055; border-bottom: 2px solid #ff0055;
        overflow: hidden; position: relative; display: flex; align-items: center;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.3);
    }
    .led-track {
        display: flex; width: 200%;
        animation: seamless-scroll 20s linear infinite;
    }
    .led-content {
        width: 50%; display: flex; justify-content: space-around; white-space: nowrap;
        font-family: 'Orbitron', sans-serif; font-weight: 700; font-size: 1.1rem; color: #ff0055;
        text-shadow: 0 0 8px #ff0055;
    }
    @keyframes seamless-scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }

    /* DATA TERMINAL PODS (LEFT SIDE) */
    .control-panel {
        height: calc(100vh - 80px); display: flex; flex-direction: column; justify-content: space-between;
        padding-right: 10px;
    }
    .compact-pod {
        background: rgba(0, 242, 255, 0.02);
        border: 1px solid rgba(0, 242, 255, 0.15);
        border-radius: 6px; padding: 10px 15px;
        transition: all 0.25s ease;
    }
    .compact-pod:hover {
        border-color: #ff0055; background: rgba(255, 0, 85, 0.04);
        box-shadow: 0 0 10px rgba(255, 0, 85, 0.2);
    }
    .pod-active {
        border-color: #00f2ff !important;
        background: rgba(0, 242, 255, 0.08) !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.3);
    }

    /* HOLOGRAM LAB ANALYZER (RIGHT SIDE) */
    .lab-display {
        height: calc(100vh - 90px);
        border: 2px solid #00f2ff; border-radius: 12px; padding: 20px;
        background: rgba(0, 10, 25, 0.4);
        box-shadow: inset 0 0 30px rgba(0, 242, 255, 0.1), 0 0 30px rgba(0,242,255,0.05);
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .lab-header-grid {
        display: flex; justify-content: space-between; align-items: center;
        border-bottom: 1px solid rgba(0, 242, 255, 0.3); padding-bottom: 10px;
    }

    /* Hide Streamlit default components */
    header, footer, [data-testid="stSidebar"] { visibility: hidden; }
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    </style>
""", unsafe_allow_html=True)

# --- SESSION SYSTEM STATES ---
if 'app_state' not in st.session_state: st.session_state.app_state = 'landing'
if 'selected_zone' not in st.session_state: st.session_state.selected_zone = 'ASIA'

# --- ECO-DATA DATABASE ---
zone_db = {
    "ASIA": {"temp": "+1.64°C", "co2": "418 PPM", "risk": "CRITICAL", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=600"},
    "EUROPE": {"temp": "+2.21°C", "co2": "415 PPM", "risk": "EXTREME", "img": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=600"},
    "NORTH AMERICA": {"temp": "+1.89°C", "co2": "421 PPM", "risk": "HIGH", "img": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=600"},
    "SOUTH AMERICA": {"temp": "+1.32°C", "co2": "409 PPM", "risk": "STABLE", "img": "https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?w=600"},
    "AFRICA": {"temp": "+1.58°C", "co2": "411 PPM", "risk": "HIGH", "img": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=600"},
    "OCEANIA": {"temp": "+1.15°C", "co2": "413 PPM", "risk": "STABLE", "img": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?w=600"}
}

# ==========================================
# SCREEN 1: IMPRESSIVE LANDING GATEWAY
# ==========================================
if st.session_state.app_state == 'landing':
    st.markdown("""
        <div class="landing-bg">
            <p style="font-family:'Orbitron'; color:#ff0055; letter-spacing:15px; font-weight:700; margin-bottom:5px;">CODETOOPIA SECURITY PROTOCOL</p>
            <h1 style="font-family:'Orbitron'; font-size:6rem; font-weight:900; color:#00f2ff; text-shadow: 0 0 30px #00f2ff, 0 0 60px #00f2ff; margin:0;">CLIMATE VAULT</h1>
            <p style="color:#666; font-size:1.1rem; letter-spacing:3px; margin-top:10px; max-width:600px; text-align:center;">
                AUTHORIZED PERSONNEL ONLY. SYSTEM CONTAINS 250 YEARS OF CORE TEMPERATURE RECORDS AND ATMOSPHERIC DEVIATIONS.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Transparent overlay layout to capture button click cleanly
    _, center_btn, _ = st.columns([2.2, 1, 2.2])
    with center_btn:
        st.markdown("<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
        if st.button("ACCESS CORE TERMINAL", use_container_width=True):
            st.session_state.app_state = 'laboratory'
            st.rerun()

# ==========================================
# SCREEN 2: HIGH-TECH FIXED LABORATORY
# ==========================================
elif st.session_state.app_state == 'laboratory':
    # Infinite Seamless LED Marquee Strip
    st.markdown("""
        <div class="led-marquee-box">
            <div class="led-track">
                <div class="led-content">
                    <span>✦ CODETOOPIA CORE SECURE</span>
                    <span>✦ QUANTUM CLIMATE VAULT ACTIVE</span>
                    <span>✦ WARNING: TEMPERATURE ANOMALIES DETECTED</span>
                    <span>✦ LIVE BIO-DATA STREAM ONLINE</span>
                </div>
                <div class="led-content">
                    <span>✦ CODETOOPIA CORE SECURE</span>
                    <span>✦ QUANTUM CLIMATE VAULT ACTIVE</span>
                    <span>✦ WARNING: TEMPERATURE ANOMALIES DETECTED</span>
                    <span>✦ LIVE BIO-DATA STREAM ONLINE</span>
                </div>
            </div>
        </div>
        <br>
    """, unsafe_allow_html=True)

    # Fixed Dual Column Layout (No Scrolling Required)
    col_panel, col_lab = st.columns([1, 1.6])

    with col_panel:
        st.markdown("<h3 style='font-family:Orbitron; color:#ff0055; margin:0 0 10px 0; font-size:1.3rem;'>CORE TARGETS</h3>", unsafe_allow_html=True)
        
        # Draw 6 compact pods vertically, highlighted based on selection
        for zone, info in zone_db.items():
            active_class = "pod-active" if st.session_state.selected_zone == zone else ""
            st.markdown(f"""
                <div class="compact-pod {active_class}">
                    <div style="display:flex; justify-content:between; font-weight:bold;">
                        <span style="font-family:Orbitron; color:white; font-size:1.1rem;">{zone}</span>
                        <span style="color:#ff0055; font-size:0.8rem;">{info['risk']}</span>
                    </div>
                    <div style="font-size:0.8rem; color:#666; margin-top:2px;">SYS_STATUS: LINKED // DECRYPT_OK</div>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"LOAD {zone} DATA", use_container_width=True):
                st.session_state.selected_zone = zone
                st.rerun()

    with col_lab:
        # Lab Interface showing real-time selected zone analytics
        current_zone = st.session_state.selected_zone
        data = zone_db[current_zone]
        
        st.markdown(f"""
            <div class="lab-display">
                <div class="lab-header-grid">
                    <div>
                        <h2 style="font-family:Orbitron; margin:0; color:#00f2ff; font-size:1.8rem;">ANALYZER: {current_zone}</h2>
                        <span style="color:#555; font-size:0.8rem;">VAULT_OS GRAPHICAL TERMINAL</span>
                    </div>
                    <div style="text-align: right;">
                        <span style="color:#ff0055; font-size:1.2rem; font-weight:bold;">{data['temp']}</span><br>
                        <span style="color:#888; font-size:0.8rem;">{data['co2']}</span>
                    </div>
                </div>
                
                <div style="display:flex; gap:15px; margin: 15px 0; height:180px; overflow:hidden;">
                    <img src="{data['img']}" style="width:45%; object-fit:cover; border:1px solid rgba(0,242,255,0.3); border-radius:6px;">
                    <div style="width:55%; background:rgba(0,0,0,0.3); padding:10px; border-radius:6px; font-size:0.9rem; color:#aaa; line-height:1.4;">
                        <b style="color:white; font-family:Orbitron;">ARCHIVE DECRYPTION LOG:</b><br>
                        • 250-year thermal variance mapped.<br>
                        • Industrial revolution baseline exceeded.<br>
                        • Carbon sink capacity dropping rapidly.<br>
                        • Predictive model accuracy: 99.4%
                    </div>
                </div>
        """, unsafe_allow_html=True)
        
        # Standard Streamlit chart embedded perfectly inside the lab view
        chart_data = [random.uniform(1.0, 2.5) for _ in range(30)]
        st.line_chart(chart_data, height=180, use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)