import streamlit as st
import time

# --- HIGH-FIDELITY HUD CONFIG ---
st.set_page_config(page_title="THERMO-CHRONOS", layout="wide", initial_sidebar_state="collapsed")

# --- THE "DEEP SPACE" STYLING ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=JetBrains+Mono:wght@100;400&display=swap');

    /* Global Foundation */
    .stApp {
        background: radial-gradient(circle at center, #0a1128 0%, #000205 100%);
        color: #00f2ff;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Moving Scanline Effect */
    .stApp::before {
        content: " ";
        position: fixed;
        top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 242, 255, 0.02) 50%), 
                    linear-gradient(90deg, rgba(255, 0, 0, 0.01), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.01));
        background-size: 100% 4px, 3px 100%;
        z-index: 10;
        pointer-events: none;
    }

    /* HUD Brackets - Redesigned for Sharpness */
    .hud-frame {
        position: fixed;
        width: 100px; height: 100px;
        border: 2px solid #00f2ff;
        z-index: 100;
        opacity: 0.5;
    }
    .tl { top: 30px; left: 30px; border-right: none; border-bottom: none; }
    .tr { top: 30px; right: 30px; border-left: none; border-bottom: none; }
    .bl { bottom: 30px; left: 30px; border-right: none; border-top: none; }
    .br { bottom: 30px; right: 30px; border-left: none; border-top: none; }

    /* Centered Hero Container */
    .hero-box {
        text-align: center;
        margin-top: 15vh;
        padding: 40px;
    }

    .title-glitch {
        font-family: 'Orbitron', sans-serif;
        font-size: 6rem;
        font-weight: 900;
        letter-spacing: 20px;
        color: white;
        text-shadow: 0 0 20px #00f2ff;
        margin-bottom: 10px;
    }

    .mission-status {
        color: #ff0055;
        font-size: 0.9rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 40px;
    }

    /* Glassmorphic Tactical Buttons */
    .stButton>button {
        background: rgba(0, 242, 255, 0.03) !important;
        color: #00f2ff !important;
        border: 1px solid rgba(0, 242, 255, 0.2) !important;
        font-family: 'Orbitron', sans-serif !important;
        border-radius: 4px !important;
        padding: 25px !important;
        transition: 0.4s cubic-bezier(0.19, 1, 0.22, 1) !important;
        backdrop-filter: blur(10px);
        width: 100% !important;
        font-size: 0.8rem !important;
        letter-spacing: 2px !important;
    }

    .stButton>button:hover {
        background: rgba(0, 242, 255, 0.2) !important;
        border-color: #00f2ff !important;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.4);
        transform: translateY(-2px);
    }

    header, footer {visibility: hidden;}
    </style>

    <div class="hud-frame tl"></div>
    <div class="hud-frame tr"></div>
    <div class="hud-frame bl"></div>
    <div class="hud-frame br"></div>
""", unsafe_allow_html=True)

# --- NAV STATE ---
if 'scene' not in st.session_state: st.session_state.scene = 'gateway'

# --- GATEWAY (FIXING IMAGE_8749DD) ---
if st.session_state.scene == 'gateway':
    st.markdown("""
        <div class="hero-box">
            <h1 class="title-glitch">CHRONOS</h1>
            <div class="mission-status">[ SYSTEM STATUS: SECURE ]</div>
            <p style="color: #666; font-size: 1rem; max-width: 600px; margin: 0 auto 50px auto; line-height: 1.6;">
                DECODING PLANETARY THERMAL ANOMALIES FROM THE LAST LEGACY DATA CORE. 
                SENSORS DETECTING SIGNIFICANT DRIFT IN SECTORS 01-06.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    _, btn_col, _ = st.columns([1.8, 1, 1.8])
    with btn_col:
        if st.button("INITIATE UPLINK"):
            st.session_state.scene = 'sectors'
            st.rerun()

# --- SECTOR GRID (FIXING IMAGE_8749A1) ---
elif st.session_state.scene == 'sectors':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; letter-spacing:10px;'>SECTOR MAP</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ff0055; margin-bottom:50px;'>LATENCY: 12ms | TARGETING GLOBAL DATA POINTS</p>", unsafe_allow_html=True)

    # Balanced 3x2 Grid
    c1, c2, c3 = st.columns(3)
    c4, c5, c6 = st.columns(3)

    sectors = [
        (c1, "NORTH AMERICA", "S-01"), (c2, "EUROPE", "S-02"), (c3, "ASIA", "S-03"),
        (c4, "SOUTH AMERICA", "S-04"), (c5, "AFRICA", "S-05"), (c6, "OCEANIA", "S-06")
    ]

    for col, name, code in sectors:
        with col:
            if st.button(f"{name}\n{code}"): 
                st.session_state.selected_sector = name
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, exit_col, _ = st.columns([2, 1, 2])
    with exit_col:
        if st.button("TERMINATE"):
            st.session_state.scene = 'gateway'
            st.rerun()

    # Sidebar HUD
    with st.sidebar:
        st.markdown("<h3 style='color:#00f2ff;'>TELEMETRY</h3>", unsafe_allow_html=True)
        st.write("---")
        st.write("DATA SOURCE: NOAA / GISS")
        st.write("TIME RANGE: 1750 - 2026")
        st.progress(92)
        st.caption("SCANNING LATEST TEMPERATURE ANOMALIES...")