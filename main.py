import time
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="OMNISCIENCE SYSTEM",
    page_icon="🌌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #09070f;
    }
    .terminal-line {
        font-family: 'Courier New', monospace;
        color: #00f3ff;
        font-size: 16px;
        margin: 10px 0;
        text-shadow: 0 0 5px #00f3ff;
    }
    .alert-title {
        font-family: 'Courier New', monospace;
        color: #ff0055;
        text-align: center;
        letter-spacing: 2px;
        text-shadow: 0 0 8px #ff0055;
        margin-top: 30px;
    }
    .briefing-text {
        font-family: 'Courier New', monospace;
        color: #b3ecff;
        text-align: justify;
        line-height: 1.8;
        font-size: 15px;
    }
    div.stButton > button {
        background-color: transparent !important;
        color: #00f3ff !important;
        border: 1px solid #00f3ff !important;
        font-family: 'Courier New', monospace !important;
        font-weight: bold !important;
        padding: 15px 30px !important;
        font-size: 16px !important;
        box-shadow: 0 0 10px rgba(0, 243, 255, 0.1) !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        background-color: #00f3ff !important;
        color: #09070f !important;
        box-shadow: 0 0 25px #00f3ff !important;
    }
    </style>
""", unsafe_allow_html=True)

if "current_page" not in st.session_state:
    st.session_state.current_page = "INTRO"

if "boot_complete" not in st.session_state:
    st.session_state.boot_complete = False

# =====================================================================
# STAGE 1: INTRO SCREEN (SYSTEM BOOT & MISSION BRIEFING)
# =====================================================================
if st.session_state.current_page == "INTRO":
    
    boot_container = st.empty()
    
    if not st.session_state.boot_complete:
        boot_lines = [
            "[BOOT]: Establishing deep-space uplink with OMNISCIENCE Recon Satellite...",
            "[CONNECT]: Quantum data link synchronized with Ark Ship Core v7.4...",
            "[DECRYPT]: Matrix HUD layout deciphered...",
            "[ACCESS]: GRANTED. Welcome, Lead Climate Reconnaissance Officer."
        ]
        
        current_display = ""
        for line in boot_lines:
            current_display += f'<div class="terminal-line">{line}</div>'
            boot_container.markdown(current_display, unsafe_allow_html=True)
            time.sleep(0.6) 
            
        st.session_state.boot_complete = True
        time.sleep(0.5)
    
    boot_container.empty()
    
    st.markdown('<h2 class="alert-title">CRITICAL ENVELOPE: HIGH COUNCIL DIRECTIVE</h2>', unsafe_allow_html=True)
    st.write("")
    st.markdown("""
        <p class="briefing-text">
        The Mother Planet has remained abandoned for over a century following the catastrophic global thermal cascade. 
        Ark Ship life support reserves are currently depleting. 
        Your mandate is to operationalize the Omniscience Long-Range Biosphere Scanner, analyze historical planetary degradation vectors, and locate viable sectors for atmospheric re-colonization.
        </p>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    if st.button("INITIALIZE BIOSPHERE SCANNER", use_container_width=True):
        with st.spinner("PERFORMING QUANTUM LEAP TO RADAR CONSOLE..."):
            time.sleep(1.2)
        st.session_state.current_page = "SECTOR_SELECTION"
        st.rerun()

# =====================================================================
# STAGE 2: SECTOR SELECTION (TEMPORARY PLACEHOLDER)
# =====================================================================
elif st.session_state.current_page == "SECTOR_SELECTION":
    st.markdown('<h1 class="terminal-line" style="text-align: center; font-size: 24px;">[ SECTOR SELECTION LAYER - PLACEHOLDER ]</h1>', unsafe_allow_html=True)
    st.write("")
    
    try:
        df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
        st.info(f"[SYSTEM LOG]: Climate Vault database linked successfully. {len(df):,} environmental telemetry logs online.")
    except Exception as e:
        st.error(f"[SYSTEM ERROR]: Failed to establish connection with GlobalLandTemperaturesByCountry.csv. Integrity compromised: {str(e)}")
        
    st.write("")
    if st.button("ABORT MISSION & DISCONNECT", use_container_width=True):
        st.session_state.current_page = "INTRO"
        st.session_state.boot_complete = False
        st.rerun()