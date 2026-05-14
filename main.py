import streamlit as st
import time

# --- STAGE 0: ULTIMATE HUD CONFIG ---
st.set_page_config(
    page_title="CHRONOS_OS | v6.0",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STAGE 1: CINEMATIC VISUAL ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@200&display=swap');

    /* Cinematic Deep Space Background */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #00f2ff;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Floating Scanline Effect */
    .scanline {
        width: 100%;
        height: 100px;
        z-index: 10;
        background: linear-gradient(0deg, rgba(0, 242, 255, 0) 0%, rgba(0, 242, 255, 0.1) 50%, rgba(0, 242, 255, 0) 100%);
        opacity: 0.1;
        position: fixed;
        bottom: 100%;
        animation: scan 6s linear infinite;
    }
    @keyframes scan { 0% { bottom: 100%; } 100% { bottom: -100%; } }

    /* Glassmorphic Container */
    .glass-card {
        background: rgba(0, 20, 40, 0.6);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-radius: 15px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 0 50px rgba(0,0,0,0.5);
    }

    /* Glitch Header */
    .glitch-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 5rem;
        font-weight: 900;
        letter-spacing: 20px;
        color: #fff;
        text-shadow: 3px 0 #ff0055, -3px 0 #00f2ff;
        margin-bottom: 0px;
    }

    /* Continent Selection Hex-Tiles */
    .stButton>button {
        background: rgba(0, 242, 255, 0.05) !important;
        color: #fff !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        font-family: 'Orbitron' !important;
        height: 150px !important;
        width: 100% !important;
        font-size: 1rem !important;
        transition: 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        text-transform: uppercase;
        letter-spacing: 3px;
        border-radius: 10px !important;
    }

    .stButton>button:hover {
        background: rgba(0, 242, 255, 0.2) !important;
        border-color: #00f2ff !important;
        box-shadow: 0 0 30px #00f2ff;
        transform: translateY(-10px) !important;
    }

    /* Hide standard Streamlit clutter */
    header, footer {visibility: hidden;}
    </style>
    
    <div class="scanline"></div>
""", unsafe_allow_html=True)

# --- STAGE 2: NAVIGATION LOGIC ---
if 'page' not in st.session_state:
    st.session_state.page = 'gateway'

# --- PAGE 1: THE GATEWAY (THE PORTAL) ---
if st.session_state.page == 'gateway':
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    
    # Outer Layout Columns
    _, center_col, _ = st.columns([1, 4, 1])
    
    with center_col:
        st.markdown("""
            <div class="glass-card">
                <h1 class="glitch-title">CHRONOS</h1>
                <p style="letter-spacing: 12px; color: #ff0055; margin-bottom: 30px;">NEURAL ARCHIVE UPLINK</p>
                <p style="color: #ccc; max-width: 600px; margin: auto; line-height: 1.8;">
                    Welcome to the Last Legacy. System is synchronizing with satellite telemetry 
                    to map 250 years of thermal data. Prepare for cognitive immersion.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Center the Start Button
        _, btn_col, _ = st.columns([1, 1, 1])
        with btn_col:
            if st.button("INITIATE SYNC"):
                with st.empty():
                    for percent_complete in range(101):
                        time.sleep(0.01)
                        st.write(f"<p style='text-align:center;'>SYNCING DATA CORES... {percent_complete}%</p>", unsafe_allow_html=True)
                st.session_state.page = 'selection'
                st.rerun()

# --- PAGE 2: SECTOR SELECTION (THE WORLD MAP) ---
elif st.session_state.page == 'selection':
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; letter-spacing:10px;'>SELECT OPERATIONAL SECTOR</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ff0055;'>[ TARGETING GLOBAL HEATMAP COORDINATES ]</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Continent Buttons with distinct visual cues
    c1, c2, c3 = st.columns(3)
    c4, c5, c6 = st.columns(3)

    # Each button is styled via CSS above to look like a high-tech "Zone Token"
    with c1:
        if st.button("NORTH AMERICA\n[SECTOR 01]"):
            st.session_state.sector = "NA"
            st.toast("Accessing NA Data Core...")
    with c2:
        if st.button("EUROPE\n[SECTOR 02]"):
            st.session_state.sector = "EU"
    with c3:
        if st.button("ASIA\n[SECTOR 03]"):
            st.session_state.sector = "AS"
    with c4:
        if st.button("SOUTH AMERICA\n[SECTOR 04]"):
            st.session_state.sector = "SA"
    with c5:
        if st.button("AFRICA\n[SECTOR 05]"):
            st.session_state.sector = "AF"
    with c6:
        if st.button("OCEANIA\n[SECTOR 06]"):
            st.session_state.sector = "OC"

    st.markdown("<br><br>", unsafe_allow_html=True)
    _, exit_col, _ = st.columns([2, 1, 2])
    with exit_col:
        if st.button("DISCONNECT"):
            st.session_state.page = 'gateway'
            st.rerun()

    # Sidebar HUD for added "coolness"
    with st.sidebar:
        st.markdown("### SYSTEM HUD")
        st.write("---")
        st.write("🛰️ SAT_LINK: STABLE")
        st.write("🌡️ AVG_HEAT: +1.2°C")
        st.write("📅 DATE: MAY 2026")
        st.progress(85)
        st.markdown("---")
        st.caption("SCANNING_ENVIRONMENTAL_ARTIFACTS...")

# --- BOTTOM HUD STATUS BAR ---
st.markdown("""
    <div style="position:fixed; bottom:0; left:0; width:100%; background:rgba(0,0,0,0.8); font-size:0.6rem; color:#00f2ff; padding:5px; text-align:center; border-top: 1px solid rgba(0, 242, 255, 0.2);">
        ENCRYPTED SESSION | USER: ADMIN_7G | LOCATION: EARTH_SECTOR_7
    </div>
""", unsafe_allow_html=True)