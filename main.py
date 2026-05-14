import streamlit as st
import time

# --- ADVANCED HUD CONFIGURATION ---
st.set_page_config(page_title="THERMO-CHRONOS", layout="wide", initial_sidebar_state="collapsed")

# --- THE "WAR ROOM" STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');

    /* Background Setup */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80');
        background-size: cover;
        color: #e0fbfc;
        font-family: 'Share Tech Mono', monospace;
    }

    /* HUD Brackets (The Corners) */
    .hud-corner {
        position: fixed;
        width: 30px;
        height: 30px;
        border: 2px solid #00f2ff;
        z-index: 999;
    }
    .top-left { top: 20px; left: 20px; border-right: none; border-bottom: none; }
    .top-right { top: 20px; right: 20px; border-left: none; border-bottom: none; }
    .bottom-left { bottom: 20px; left: 20px; border-right: none; border-top: none; }
    .bottom-right { bottom: 20px; right: 20px; border-left: none; border-top: none; }

    /* Main Title Section */
    .hero-container {
        text-align: center;
        padding-top: 5vh;
    }
    .glitch-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 5.5rem;
        letter-spacing: 15px;
        color: #fff;
        text-shadow: 3px 3px #ff0055, -3px -3px #00f2ff;
        margin-bottom: 0px;
    }
    .mission-subtitle {
        font-size: 1.2rem;
        letter-spacing: 5px;
        color: #00f2ff;
        text-transform: uppercase;
        border-bottom: 1px solid #00f2ff;
        display: inline-block;
        padding-bottom: 10px;
        margin-bottom: 30px;
    }

    /* Node Selection Styling */
    .stButton>button {
        background: rgba(0, 242, 255, 0.05) !important;
        color: #00f2ff !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        font-family: 'Orbitron' !important;
        width: 100% !important;
        height: 80px !important;
        transition: 0.4s !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .stButton>button:hover {
        background: rgba(0, 242, 255, 0.2) !important;
        border: 1px solid #00f2ff !important;
        box-shadow: 0 0 20px #00f2ff;
        transform: scale(1.02);
    }

    /* Hide redundant elements */
    header, footer {visibility: hidden;}
    </style>

    <!-- Visual HUD Overlays -->
    <div class="hud-corner top-left"></div>
    <div class="hud-corner top-right"></div>
    <div class="hud-corner bottom-left"></div>
    <div class="hud-corner bottom-right"></div>
""", unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
if 'scene' not in st.session_state:
    st.session_state.scene = 'gateway'

# --- 1. THE GATEWAY (LANDING) ---
if st.session_state.scene == 'gateway':
    st.markdown("""
        <div class="hero-container">
            <h1 class="glitch-header">THERMO-CHRONOS</h1>
            <p class="mission-subtitle">Planetary Thermal Archive & Historical Telemetry</p>
            <p style="opacity: 0.6; max-width: 600px; margin: auto;">
                Warning: You are accessing the Last Legacy data core. This interface visualizes 
                global climate anomalies from 1750 to present. Proceed with caution.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1.5, 1, 1.5])
    with col_btn:
        if st.button("INITIALIZE MISSION"):
            st.session_state.scene = 'world_map'
            st.rerun()

# --- 2. THE COMMAND CENTER (SELECTION) ---
elif st.session_state.scene == 'world_map':
    st.markdown("""
        <div style="text-align: center;">
            <h2 style="font-family:Orbitron; letter-spacing: 5px;">TACTICAL ZONE SELECTION</h2>
            <p style="color:#ff0055;">[ SELECT A CONTINENTAL SECTOR TO DECODE DATA ]</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3x2 Grid for All Continents
    m1, m2, m3 = st.columns(3)
    m4, m5, m6 = st.columns(3)

    with m1: 
        if st.button("NORTH AMERICA\n[Sector 01]"): st.session_state.target = "NA"
    with m2: 
        if st.button("EUROPE\n[Sector 02]"): st.session_state.target = "EU"
    with m3: 
        if st.button("ASIA\n[Sector 03]"): st.session_state.target = "AS"
    with m4: 
        if st.button("SOUTH AMERICA\n[Sector 04]"): st.session_state.target = "SA"
    with m5: 
        if st.button("AFRICA\n[Sector 05]"): st.session_state.target = "AF"
    with m6: 
        if st.button("OCEANIA\n[Sector 06]"): st.session_state.target = "OC"

    st.markdown("<br><br>", unsafe_allow_html=True)
    _, back_col, _ = st.columns([2, 1, 2])
    with back_col:
        if st.button("ABORT MISSION"):
            st.session_state.scene = 'gateway'
            st.rerun()

    # Sidebar HUD Data
    with st.sidebar:
        st.markdown("### SYSTEM STATUS")
        st.write("CORE: ACTIVE")
        st.write("ENCRYPTION: RSA-256")
        st.progress(85)
        st.markdown("---")
        st.info("Select a sector to view the survival index and temperature fluctuations.")