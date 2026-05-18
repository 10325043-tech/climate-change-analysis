import streamlit as st
import time

st.set_page_config(
    page_title="ARK-SHIP: OMNISCIENCE TERMINAL",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #1a1033 0%, #09070f 100%);
        color: #00f3ff;
        font-family: 'Courier New', monospace;
    }

    .hud-container {
        border: 2px solid rgba(0, 243, 255, 0.3);
        padding: 40px;
        border-radius: 15px;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 0 50px rgba(0, 243, 255, 0.1), inset 0 0 20px rgba(0, 243, 255, 0.05);
        backdrop-filter: blur(10px);
        margin-top: 50px;
    }

    .terminal-text {
        color: #00f3ff;
        text-shadow: 0 0 10px #00f3ff;
        font-size: 18px;
        margin-bottom: 10px;
    }

    .critical-alert {
        color: #ff0055;
        text-shadow: 0 0 15px #ff0055;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        letter-spacing: 5px;
        margin-bottom: 30px;
    }

    .mission-desc {
        color: #b3ecff;
        font-size: 18px;
        line-height: 1.6;
        text-align: center;
        max-width: 800px;
        margin: 0 auto;
    }

    div.stButton > button {
        width: 100%;
        background: transparent !important;
        color: #00f3ff !important;
        border: 2px solid #00f3ff !important;
        padding: 20px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        letter-spacing: 3px !important;
        text-transform: uppercase !important;
        transition: all 0.4s ease-in-out !important;
        margin-top: 40px !important;
    }

    div.stButton > button:hover {
        background: rgba(0, 243, 255, 0.2) !important;
        box-shadow: 0 0 40px #00f3ff !important;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "INTRO"

# =====================================================================
# STAGE 1: INTRO SCREEN (SYSTEM BOOT & MISSION BRIEFING)
# =====================================================================
if st.session_state.page == "INTRO":
    
    placeholder = st.empty()
    
    with placeholder.container():
        st.write("")
        st.write("")
        boot_msg = [
            "> INITIALIZING ARK-SHIP OMNISCIENCE OS...",
            "> ESTABLISHING QUANTUM LINK WITH RECON_SATELLITE_ALPHA...",
            "> DECRYPTING TERRESTRIAL THERMAL DATA... DONE.",
            "> BIOSPHERE SCANNER READY. ACCESS GRANTED."
        ]
        full_text = ""
        for line in boot_msg:
            full_text += f'<div class="terminal-text">{line}</div>'
            st.markdown(full_text, unsafe_allow_html=True)
            time.sleep(0.4)
        time.sleep(1)
    
    placeholder.empty()

    with st.container():
        # Top HUD bar 100% English
        col1, col2, col3 = st.columns([1,2,1])
        with col1: 
            st.write("🛰️ STATUS: UPLINK_ONLINE")
        with col2: 
            st.write("<div style='text-align:center'>// ARK SHIP RECON CONSOLE V7.4 //</div>", unsafe_allow_html=True)
        with col3: 
            st.write("<div style='text-align:right'>O2 RESERVES: 34% [CRITICAL] ⚠️</div>", unsafe_allow_html=True)

        # Central Envelope Panel
        st.markdown("""
            <div class="hud-container">
                <div class="critical-alert">MISSION DIRECTIVE</div>
                <div class="mission-desc">
                    Humanity drifts in the void. Earth is a furnace. 
                    Resources on the Ark are failing. 
                    Your mission: Re-activate the <b>Omniscience Deep-Space Scanner</b>. 
                    Peer through the radiation clouds, analyze centuries of heat data, 
                    and locate a single coordinate where life can begin again.
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.write("")
        if st.button("ACTIVATE SCANNER"):
            with st.spinner("INITIATING QUANTUM LEAP TO EARTH ORBIT..."):
                time.sleep(1.5)
            st.session_state.page = "SECTOR"
            st.rerun()

# =====================================================================
# STAGE 2: SECTOR SELECTION (TEMPORARY PLACEHOLDER)
# =====================================================================
elif st.session_state.page == "SECTOR":
    st.markdown("<h1 style='text-align:center; color:#00f3ff; font-family:\"Courier New\";'>[ SECTOR SCANNING LAYER ACTIVE ]</h1>", unsafe_allow_html=True)
    st.write("")
    
    # Placeholder layout for Page 2
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("> TARGETING PLANET MOTHER... SECTOR SELECTION REQUIRED.")
    with col2:
        st.write("> QUANTUM DATABASE: CONNECTED.")
        
    st.write("")
    if st.button("RETURN TO COMMAND"):
        st.session_state.page = "INTRO"
        st.rerun()