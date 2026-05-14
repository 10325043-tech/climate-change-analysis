import streamlit as st
import time

# --- SYSTEM INITIALIZATION ---
st.set_page_config(page_title="THERMO-CHRONOS", layout="wide", initial_sidebar_state="collapsed")

# --- CYBERPUNK CSS CORE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@300&display=swap');

    :root {
        --neon-cyan: #00f2ff;
        --neon-magenta: #ff0055;
        --deep-void: #030509;
    }

    /* Cinematic Background */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80');
        background-size: cover;
        color: white;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Glitch Title */
    .glitch-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 5rem;
        font-weight: 900;
        text-transform: uppercase;
        text-align: center;
        color: white;
        text-shadow: 2px 2px var(--neon-magenta), -2px -2px var(--neon-cyan);
        animation: glitch 1s linear infinite;
    }

    @keyframes glitch {
        2%, 64% { transform: translate(2px,0) skew(0deg); }
        4%, 60% { transform: translate(-2px,0) skew(0deg); }
        62% { transform: translate(0,0) skew(5deg); }
    }

    /* Crystal Button */
    .stButton>button {
        background: rgba(0, 242, 255, 0.1) !important;
        color: var(--neon-cyan) !important;
        border: 2px solid var(--neon-cyan) !important;
        font-family: 'Orbitron' !important;
        padding: 20px 80px !important;
        font-size: 1.5rem !important;
        border-radius: 0px !important;
        transition: 0.5s !important;
        backdrop-filter: blur(10px);
        display: block;
        margin: auto;
    }

    .stButton>button:hover {
        background: var(--neon-cyan) !important;
        color: black !important;
        box-shadow: 0 0 50px var(--neon-cyan);
    }

    /* Loading Ring */
    .loader {
        border: 4px solid transparent;
        border-top: 4px solid var(--neon-cyan);
        border-radius: 50%;
        width: 100px;
        height: 100px;
        animation: spin 1s linear infinite;
        margin: auto;
    }

    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE FOR NAVIGATION ---
if 'scene' not in st.session_state:
    st.session_state.scene = 'gateway'

# --- 1. THE GATEWAY (TRANG BÌA) ---
if st.session_state.scene == 'gateway':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<h1 class="glitch-header">THERMO<br>CHRONOS</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; letter-spacing:10px; color:#555;'>THE LAST LEGACY | v3.0.4</p>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if st.button("START MISSION"):
        st.session_state.scene = 'loading'
        st.rerun()

# --- 2. THE LOADING SEQUENCE ---
elif st.session_state.scene == 'loading':
    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="loader"></div>', unsafe_allow_html=True)
    placeholder = st.empty()
    
    codes = ["INITIALIZING QUANTUM CORE...", "FETCHING HISTORICAL TELEMETRY...", "MAPPING THERMAL GRIDS...", "READY TO JUMP."]
    for code in codes:
        placeholder.markdown(f"<p style='text-align:center; color:cyan; font-family:monospace;'>{code}</p>", unsafe_allow_html=True)
        time.sleep(0.8)
    
    st.session_state.scene = 'world_map'
    st.rerun()

# --- 3. THE WORLD MAP SELECTION (GIAO DIỆN CHỌN VÙNG) ---
elif st.session_state.scene == 'world_map':
    st.markdown("<h2 style='font-family:Orbitron; color:cyan;'>SELECT TARGET ZONE</h2>", unsafe_allow_html=True)
    
    # Ở đây chúng ta sẽ chèn bản đồ 3D bằng pydeck hoặc plotly
    st.info("MISSION: Hover over continents to detect anomalies. Target: Global Temperature Datasets.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("ASIA SECTOR"): pass
    with col2:
        if st.button("EUROPE SECTOR"): pass
    with col3:
        if st.button("BACK TO VOID"):
            st.session_state.scene = 'gateway'
            st.rerun()