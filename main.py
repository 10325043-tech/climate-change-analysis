import streamlit as st
import random

# --- CORE SYSTEM CONFIG ---
st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide", initial_sidebar_state="collapsed")

# --- UI STYLING ENGINE (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');

    /* Force full-screen view, no scrolling allowed */
    html, body, [data-testid="stAppViewContainer"] {
        max-height: 100vh;
        overflow: hidden;
        background: radial-gradient(circle at center, #050d1f 0%, #000205 100%);
        color: #00f2ff;
        font-family: 'Share Tech Mono', monospace;
    }

    /* SEAMLESS INFINITE LED MARQUEE */
    .led-marquee-box {
        width: 100%; height: 40px; background: #000; 
        border-top: 2px solid #ff0055; border-bottom: 2px solid #ff0055;
        overflow: hidden; position: relative; display: flex; align-items: center;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.3);
    }
    .led-track { display: flex; width: 200%; animation: seamless-scroll 25s linear infinite; }
    .led-content {
        width: 50%; display: flex; justify-content: space-around; white-space: nowrap;
        font-family: 'Orbitron', sans-serif; font-weight: 700; font-size: 1.1rem; color: #ff0055;
        text-shadow: 0 0 8px #ff0055;
    }
    @keyframes seamless-scroll { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

    /* NATIVE BUTTON OVERRIDE - MAKING THEM BEHAVE LIKE RADIANT PODS */
    div.stButton > button {
        background: rgba(0, 242, 255, 0.02) !important;
        border: 1px solid rgba(0, 242, 255, 0.2) !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 20px 15px !important;
        width: 100% !important;
        text-align: left !important;
        margin-bottom: 12px !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        display: block !important;
    }
    
    div.stButton > button:hover {
        border-color: #ff0055 !important;
        background: rgba(255, 0, 85, 0.08) !important;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.4) !important;
        transform: scale(1.02);
    }

    /* INJECTED HTML METRICS INSIDE BUTTONS */
    .btn-title { font-family: 'Orbitron'; font-size: 1.2rem; font-weight: 700; color: #fff; }
    .btn-meta { color: #00f2ff; font-size: 0.8rem; margin-top: 5px; display: flex; justify-content: space-between; }
    .btn-status { color: #ff0055; font-size: 0.75rem; letter-spacing: 1px; }

    /* FIXED SCI-FI LABORATORY SCREEN */
    .lab-display {
        height: calc(100vh - 100px);
        border: 2px solid #00f2ff; border-radius: 12px; padding: 25px;
        background: rgba(0, 10, 25, 0.55);
        backdrop-filter: blur(10px);
        box-shadow: inset 0 0 40px rgba(0, 242, 255, 0.15), 0 0 25px rgba(0,242,255,0.05);
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .lab-header-grid {
        display: flex; justify-content: space-between; align-items: center;
        border-bottom: 1px solid rgba(0, 242, 255, 0.2); padding-bottom: 15px;
    }

    header, footer, [data-testid="stSidebar"] { visibility: hidden; }
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    </style>
""", unsafe_allow_html=True)

# --- SESSION DATABASE SETUP ---
if 'selected_zone' not in st.session_state: st.session_state.selected_zone = 'ASIA'

zone_db = {
    "ASIA": {"temp": "+1.64°C", "co2": "418 PPM", "risk": "CRITICAL", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=600"},
    "EUROPE": {"temp": "+2.21°C", "co2": "415 PPM", "risk": "EXTREME", "img": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=600"},
    "NORTH AMERICA": {"temp": "+1.89°C", "co2": "421 PPM", "risk": "HIGH", "img": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=600"},
    "SOUTH AMERICA": {"temp": "+1.32°C", "co2": "409 PPM", "risk": "STABLE", "img": "https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?w=600"},
    "AFRICA": {"temp": "+1.58°C", "co2": "411 PPM", "risk": "HIGH", "img": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=600"},
    "OCEANIA": {"temp": "+1.15°C", "co2": "413 PPM", "risk": "STABLE", "img": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?w=600"}
}

# ==========================================
# HEADER: SEAMLESS LED RUNNING TEXT
# ==========================================
st.markdown("""
    <div class="led-marquee-box">
        <div class="led-track">
            <div class="led-content">
                <span>✦ CODETOOPIA CORE SECURE</span>
                <span>✦ QUANTUM CLIMATE VAULT ACTIVE</span>
                <span>✦ WARNING: TEMPERATURE ANOMALIES DETECTED</span>
                <span>✦ LIVE DATA STREAM ONLINE</span>
            </div>
            <div class="led-content">
                <span>✦ CODETOOPIA CORE SECURE</span>
                <span>✦ QUANTUM CLIMATE VAULT ACTIVE</span>
                <span>✦ WARNING: TEMPERATURE ANOMALIES DETECTED</span>
                <span>✦ LIVE DATA STREAM ONLINE</span>
            </div>
        </div>
    </div>
    <br>
""", unsafe_allow_html=True)

# ==========================================
# MAIN INTERFACE (NO SCROLL BAR LAYOUT)
# ==========================================
col_panel, col_lab = st.columns([1, 1.6])

with col_panel:
    st.markdown("<h3 style='font-family:Orbitron; color:#ff0055; margin:0 0 15px 0; font-size:1.3rem; letter-spacing:2px;'>CORE TARGETS</h3>", unsafe_allow_html=True)
    
    # Render native buttons but style them completely as custom HTML pods
    for zone, info in zone_db.items():
        # Inject custom text markup directly inside the button layout
        button_html = f"""
            <div style="text-align: left;">
                <div class="btn-title">{zone}</div>
                <div class="btn-meta">
                    <span>ANOMALY: {info['temp']}</span>
                    <span class="btn-status">{info['risk']}</span>
                </div>
            </div>
        """
        # When a button is clicked, change the central screen zone state
        if st.button(button_html, key=f"btn_{zone}", use_container_width=True):
            st.session_state.selected_zone = zone
            st.rerun()

with col_lab:
    current_zone = st.session_state.selected_zone
    data = zone_db[current_zone]
    
    # The Laboratory Screen UI Layout
    st.markdown(f"""
        <div class="lab-display">
            <div class="lab-header-grid">
                <div>
                    <h2 style="font-family:Orbitron; margin:0; color:#00f2ff; font-size:2rem; letter-spacing:1px;">ANALYZER: {current_zone}</h2>
                    <span style="color:#555; font-size:0.8rem;">CODETOOPIA QUANTUM VAULT DECRYPTION TERMINAL</span>
                </div>
                <div style="text-align: right;">
                    <span style="color:#ff0055; font-size:1.5rem; font-weight:bold; font-family:Orbitron;">{data['temp']}</span><br>
                    <span style="color:#888; font-size:0.8rem; letter-spacing:1px;">{data['co2']}</span>
                </div>
            </div>
            
            <div style="display:flex; gap:20px; margin: 20px 0; height:180px; overflow:hidden;">
                <img src="{data['img']}" style="width:45%; object-fit:cover; border:1px solid rgba(0,242,255,0.3); border-radius:8px; box-shadow: 0 0 15px rgba(0,242,255,0.1);">
                <div style="width:55%; background:rgba(0,0,0,0.4); padding:15px; border-radius:8px; font-size:0.9rem; color:#ccc; line-height:1.5; border: 1px solid rgba(255,255,255,0.03);">
                    <b style="color:white; font-family:Orbitron; letter-spacing:1px;">DECRYPTION REAL-TIME LOG:</b><br>
                    <span style="color:#666;">------------------------------------</span><br>
                    • Industrial thermal baseline exceeded.<br>
                    • Carbon sink saturation level critical.<br>
                    • Permafrost melt acceleration tracked.<br>
                    • System analytical fidelity: 99.86%
                </div>
            </div>
    """, unsafe_allow_html=True)
    
    # Streamlit line chart fits into the calculated container area seamlessly
    chart_data = [random.uniform(1.0, 2.8) for _ in range(40)]
    st.line_chart(chart_data, height=210, use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)