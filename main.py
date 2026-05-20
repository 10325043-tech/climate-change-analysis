import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

if "page" not in st.session_state:
    st.session_state.page = "WELCOME"

# --- CSS CORE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Share+Tech+Mono&display=swap');
    
    /* NỀN KHÔNG GIAN SÂU (CSS THUẦN) */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1e1b4b 0%, #020617 80%);
        color: #e2e8f0; font-family: 'Share Tech Mono', monospace;
    }
    
    /* HUD 4 GÓC (CỐ ĐỊNH) */
    .hud { position: absolute; border: 1px solid #fb923c; padding: 15px; color: #fb923c; font-size: 11px; z-index: 10; }
    .tl { top: 40px; left: 40px; } .tr { top: 40px; right: 40px; }
    .bl { bottom: 40px; left: 40px; } .br { bottom: 40px; right: 40px; }
    
    /* TRUNG TÂM */
    .center-ui { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 85vh; text-align: center; }
    .title { font-family: 'Orbitron', sans-serif; font-size: 75px; letter-spacing: 15px; margin: 0; color: #fff; }
    .subtitle { font-size: 16px; letter-spacing: 8px; color: #cbd5e1; margin-bottom: 40px; }
    
    /* NÚT BẤM NEON */
    div.stButton > button {
        background: transparent !important; border: 1px solid #fb923c !important; 
        color: #fb923c !important; padding: 15px 40px !important; 
        font-size: 16px !important; letter-spacing: 4px !important;
        transition: 0.3s !important;
    }
    div.stButton > button:hover { background: #fb923c !important; color: #020617 !important; }
    </style>

    <div class="hud tl">SYS_IDENT: OMNISCIENCE<br>PROTO_V: 9.12.0</div>
    <div class="hud tr">UPLINK: ACTIVE<br>LOC: GEO_STATIONARY</div>
    <div class="hud bl">CORE_TEMP: INCREASING<br>ANOMALY: DETECTED</div>
    <div class="hud br">CODETOOPIA SYSTEMS<br>EST. 2026</div>
""", unsafe_allow_html=True)

# --- LOGIC ---
if st.session_state.page == "WELCOME":
    st.markdown("""
        <div class="center-ui">
            <h1 class="title">CLIMATE VAULT</h1>
            <p class="subtitle">PLANETARY THERMAL FORENSICS</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("INITIALIZE ANALYSIS ->"):
            st.session_state.page = "ANALYSIS"
            st.rerun()

elif st.session_state.page == "ANALYSIS":
    st.markdown("<style>.stApp {background: #020617;}</style>", unsafe_allow_html=True)
    st.title("THERMAL TELEMETRY ARCHIVE")
    
    df = pd.DataFrame({'Year': [2020, 2021, 2022], 'Temp': [28.1, 29.5, 30.2]})
    fig = px.line(df, x='Year', y='Temp', template="plotly_dark")
    fig.update_traces(line_color='#fb923c', line_width=3)
    st.plotly_chart(fig, use_container_width=True)
    
    if st.button("EXIT MISSION"):
        st.session_state.page = "WELCOME"
        st.rerun()