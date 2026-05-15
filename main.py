import streamlit as st

# --- SYSTEM CONFIG ---
st.set_page_config(
    page_title="CHRONOS_COMMAND | v8.0",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- THE "CLIMATE-CORE" VISUAL ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');

    /* Cinematic Hybrid Background: Earth + Thermal Glitch */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url('https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=2074&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #00f2ff;
        font-family: 'Share Tech Mono', monospace;
    }

    /* Tactical Viewport Corners */
    .stApp::before {
        content: ""; position: fixed; top: 20px; left: 20px; width: 100px; height: 100px;
        border-top: 2px solid #ff0055; border-left: 2px solid #ff0055; z-index: 100; pointer-events: none;
    }
    .stApp::after {
        content: ""; position: fixed; bottom: 20px; right: 20px; width: 100px; height: 100px;
        border-bottom: 2px solid #ff0055; border-right: 2px solid #ff0055; z-index: 100; pointer-events: none;
    }

    /* Sector Card Styling */
    .sector-card {
        background: rgba(0, 10, 20, 0.8);
        border: 1px solid rgba(0, 242, 255, 0.3);
        border-radius: 5px;
        padding: 0px;
        text-align: center;
        transition: 0.4s;
        overflow: hidden;
        position: relative;
    }
    
    .sector-card:hover {
        border-color: #ff0055;
        box-shadow: 0 0 25px rgba(255, 0, 85, 0.4);
        transform: translateY(-5px);
    }

    .sector-img {
        width: 100%;
        height: 150px;
        object-fit: cover;
        filter: grayscale(100%) sepia(50%) hue-rotate(140deg) brightness(0.7);
        transition: 0.5s;
    }

    .sector-card:hover .sector-img {
        filter: grayscale(0%) brightness(1);
    }

    /* Tactical Titles */
    .os-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        text-align: center;
        letter-spacing: 15px;
        background: linear-gradient(to bottom, #fff, #00f2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 30px;
    }

    /* Custom Streamlit Button Override */
    .stButton>button {
        background: transparent !important;
        border: 1px solid #00f2ff !important;
        color: #00f2ff !important;
        border-radius: 0px !important;
        width: 100% !important;
        text-transform: uppercase;
        font-weight: bold;
        letter-spacing: 2px;
    }
    .stButton>button:hover {
        background: #00f2ff !important;
        color: #000 !important;
    }

    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
if 'view' not in st.session_state:
    st.session_state.view = 'login'

# --- PAGE 1: TERMINAL ACCESS ---
if st.session_state.view == 'login':
    st.markdown('<h1 class="os-header">CHRONOS_OS</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ff0055; letter-spacing:5px;'>SATELLITE DOWNLINK: ESTABLISHED</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background:rgba(0,242,255,0.05); border:1px solid #00f2ff; padding:30px; text-align:center;">
            <p>WARNING: You are accessing historical environmental records. <br>
            Current CO2 Concentration: <b>419.7 PPM</b><br>
            Global Anomaly: <b>+1.28°C</b></p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("INITIALIZE COMMAND"):
            st.session_state.view = 'sectors'
            st.rerun()

# --- PAGE 2: TACTICAL SECTOR MAP ---
elif st.session_state.view == 'sectors':
    st.markdown('<h2 style="font-family:Orbitron; letter-spacing:8px; text-align:center;">DEPLOYMENT_ZONES</h2>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>SELECT A CONTINENTAL SECTOR TO MONITOR THERMAL DECAY</p>", unsafe_allow_html=True)
    
    # Sector Data (Images + Info)
    sectors = [
        {"name": "NORTH AMERICA", "id": "S-01", "img": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?q=80&w=2070"},
        {"name": "EUROPE", "id": "S-02", "img": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?q=80&w=2070"},
        {"name": "ASIA", "id": "S-03", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=2070"},
        {"name": "SOUTH AMERICA", "id": "S-04", "img": "https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?q=80&w=2076"},
        {"name": "AFRICA", "id": "S-05", "img": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?q=80&w=2071"},
        {"name": "OCEANIA", "id": "S-06", "img": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?q=80&w=2030"}
    ]

    # Display 3 columns
    cols = st.columns(3)
    for i, s in enumerate(sectors):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="sector-card">
                    <img src="{s['img']}" class="sector-img">
                    <div style="padding:15px;">
                        <h4 style="margin:0; color:#00f2ff;">{s['name']}</h4>
                        <small style="color:#ff0055;">{s['id']} // ACTIVE</small>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"DECODE {s['id']}"):
                st.toast(f"Synchronizing {s['name']} Datasets...")
            st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")
    if st.button("TERMINATE UPLINK"):
        st.session_state.view = 'login'
        st.rerun()

# --- SIDEBAR HUD ---
with st.sidebar:
    st.markdown("### DATA_FEED")
    st.error("ANOMALY: Arctic Ice Sheet at 14% integrity.")
    st.warning("SENSOR_09: Thermal drift detected in Amazon Basin.")
    st.info("ARCHIVE: 250 Years of data ready for injection.")