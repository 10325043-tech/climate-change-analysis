import streamlit as st
import time

# --- INITIAL SYSTEM CONFIG ---
st.set_page_config(
    page_title="CHRONOS_ELITE | v7.0",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- THE "ELITE" VISUAL ENGINE (EXTREME CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Syncopate:wght@700&family=JetBrains+Mono:wght@200&display=swap');

    /* Cinematic Animated Background */
    .stApp {
        background: black;
        background-image: 
            radial-gradient(circle at 50% 50%, rgba(0, 242, 255, 0.1) 0%, transparent 80%),
            url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Floating Digital Fog */
    .stApp::after {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: repeating-linear-gradient(0deg, rgba(0,0,0,0.15) 0px, rgba(0,0,0,0.15) 1px, transparent 1px, transparent 2px);
        background-size: 100% 3px;
        pointer-events: none;
        z-index: 10;
    }

    /* Neon Glitch Title */
    .main-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 6rem;
        text-align: center;
        color: transparent;
        -webkit-text-stroke: 1px #00f2ff;
        filter: drop-shadow(0 0 15px #00f2ff);
        letter-spacing: 25px;
        margin-top: 50px;
        animation: pulse 4s infinite alternate;
    }

    @keyframes pulse {
        0% { opacity: 0.5; filter: drop-shadow(0 0 5px #00f2ff); }
        100% { opacity: 1; filter: drop-shadow(0 0 30px #ff0055); }
    }

    /* Sector Selection Hex-Tiles */
    .stButton>button {
        background: rgba(0, 5, 10, 0.7) !important;
        color: #00f2ff !important;
        border: 1px solid #00f2ff !important;
        border-radius: 0px !important;
        clip-path: polygon(10% 0, 90% 0, 100% 50%, 90% 100%, 10% 100%, 0 50%) !important;
        height: 180px !important;
        width: 100% !important;
        font-family: 'Orbitron' !important;
        font-size: 0.9rem !important;
        transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1) !important;
        border-left: 5px solid #ff0055 !important;
    }

    .stButton>button:hover {
        background: rgba(0, 242, 255, 0.2) !important;
        transform: scale(1.05) rotateX(10deg) !important;
        color: white !important;
        box-shadow: 0 0 40px rgba(0, 242, 255, 0.5) !important;
        border-left: 10px solid #00f2ff !important;
    }

    /* Glass Panels */
    .glass-container {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 50px;
        border-radius: 20px;
        text-align: center;
    }

    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- SESSION NAVIGATION ---
if 'nav' not in st.session_state:
    st.session_state.nav = 'gate'

# --- PAGE 1: THE GATEWAY ---
if st.session_state.nav == 'gate':
    st.markdown('<h1 class="main-title">CHRONOS</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; letter-spacing:15px; color:#ff0055; font-weight:bold;'>[ NO_LIMIT_EDITION ]</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div class="glass-container">
                <p style="font-family:'JetBrains Mono'; font-size:0.8rem; color:#888;">// SYSTEM STATUS: ARMED<br>// ENCRYPTION: 1024-BIT NEURAL</p>
                <p style="margin: 30px 0; font-size:1.1rem; line-height:1.6;">
                    Accessing the global thermal archive. Millions of data points are being 
                    reconstructed for temporal visualization.
                </p>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("ENTER THE VOID"):
            st.session_state.nav = 'map'
            st.rerun()

# --- PAGE 2: SECTOR SELECTION ---
elif st.session_state.nav == 'map':
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; letter-spacing:10px; color:#fff;'>CHOOSE SECTOR</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ff0055;'>TARGETING NEURAL COORDINATES</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Continent Grid
    row1_c1, row1_c2, row1_c3 = st.columns(3)
    row2_c1, row2_c2, row2_c3 = st.columns(3)

    with row1_c1:
        if st.button("01_NORTH_AMERICA\n[DATA_SYNC]"): st.toast("Connecting to NA Servers...")
    with row1_c2:
        if st.button("02_EUROPE\n[DATA_SYNC]"): st.toast("Connecting to EU Servers...")
    with row1_c3:
        if st.button("03_ASIA\n[DATA_SYNC]"): st.toast("Connecting to AS Servers...")
    
    with row2_c1:
        if st.button("04_SOUTH_AMERICA\n[DATA_SYNC]"): st.toast("Connecting to SA Servers...")
    with row2_c2:
        if st.button("05_AFRICA\n[DATA_SYNC]"): st.toast("Connecting to AF Servers...")
    with row2_c3:
        if st.button("06_OCEANIA\n[DATA_SYNC]"): st.toast("Connecting to OC Servers...")

    st.markdown("<br><br>", unsafe_allow_html=True)
    _, exit_btn, _ = st.columns([2, 1, 2])
    with exit_btn:
        if st.button("LOGOUT"):
            st.session_state.nav = 'gate'
            st.rerun()

# --- HUD DECORATION ---
st.sidebar.markdown("### TERMINAL_HUD")
st.sidebar.code("""
> CPU: 98%
> MEM: 4.2GB
> SYNC: ACTIVE
> LATENCY: 2ms
""")
st.sidebar.progress(98)