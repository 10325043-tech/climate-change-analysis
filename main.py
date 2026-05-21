import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Share+Tech+Mono&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%);
        color: #e2e8f0;
        font-family: 'Share Tech Mono', monospace;
    }
    
    .hud-container {
        display: grid;
        grid-template-columns: 1fr 2fr 1fr;
        grid-template-rows: 100px 1fr 100px;
        height: 85vh;
        padding: 20px;
    }
    
    .hud-element { border: 1px solid #38bdf8; padding: 15px; color: #38bdf8; font-size: 12px; background: rgba(56, 189, 248, 0.05); }
    .tl { grid-column: 1; grid-row: 1; align-self: start; }
    .tr { grid-column: 3; grid-row: 1; align-self: start; text-align: right; }
    .bl { grid-column: 1; grid-row: 3; align-self: end; }
    .br { grid-column: 3; grid-row: 3; align-self: end; text-align: right; }
    
    .center-vault {
        grid-column: 2;
        grid-row: 2;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    
    .title { font-family: 'Orbitron', sans-serif; font-size: 70px; letter-spacing: 20px; color: #fff; margin: 0; text-shadow: 0 0 20px #38bdf8; }
    .subtitle { font-size: 14px; letter-spacing: 10px; color: #38bdf8; margin-top: 10px; text-transform: uppercase; }
    
    div.stButton > button {
        background: transparent !important;
        border: 2px solid #38bdf8 !important;
        color: #38bdf8 !important;
        padding: 15px 40px !important;
        font-size: 18px !important;
        letter-spacing: 5px !important;
        font-family: 'Orbitron', sans-serif !important;
        transition: 0.4s !important;
        margin-top: 50px !important;
    }
    div.stButton > button:hover { background: #38bdf8 !important; color: #020617 !important; box-shadow: 0 0 30px #38bdf8; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hud-container">
        <div class="hud-element tl">MODULE: CLIMATE_CORE<br>STATUS: OPERATIONAL</div>
        <div class="hud-element tr">UPLINK: ACTIVE<br>SATELLITE: GEO-7</div>
        <div class="center-vault">
            <h1 class="title">CLIMATE VAULT</h1>
            <p class="subtitle">Planetary Thermal Forensics</p>
        </div>
        <div class="hud-element bl">ANOMALY: DETECTED<br>TEMP_INDEX: CRITICAL</div>
        <div class="hud-element br">CODETOOPIA SYSTEMS<br>VERSION: 2.0.4</div>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("ENTER ARCHIVE"):
        st.switch_page("pages/1_Country_Selection.py")