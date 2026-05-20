import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

if "page" not in st.session_state:
    st.session_state.page = "WELCOME"

if st.session_state.page == "WELCOME":
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700&display=swap');
        .stApp {
            background: radial-gradient(circle at 50% 50%, #1e1b4b 0%, #020617 70%);
            color: white; font-family: 'Share Tech Mono', monospace;
        }
        .hud { position: absolute; border: 1px solid #fb923c; padding: 10px; font-size: 10px; color: #fb923c; }
        .tl { top: 30px; left: 30px; } .tr { top: 30px; right: 30px; }
        .bl { bottom: 30px; left: 30px; } .br { bottom: 30px; right: 30px; }
        .main-ui { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 90vh; text-align: center; }
        .title { font-family: 'Orbitron', sans-serif; font-size: 70px; letter-spacing: 15px; margin: 0; }
        .subtitle { font-size: 16px; letter-spacing: 8px; color: #cbd5e1; margin-bottom: 40px; }
        div.stButton > button {
            background: transparent !important; border: 1px solid #fb923c !important; color: #fb923c !important;
            padding: 12px 40px !important; font-size: 16px !important; letter-spacing: 4px !important;
        }
        </style>
        <div class="hud tl">SYS_IDENT: OMNISCIENCE<br>PROTO_V: 9.12.0</div>
        <div class="hud tr">UPLINK: ACTIVE<br>LOC: GEO_STATIONARY</div>
        <div class="hud bl">CORE_TEMP: INCREASING<br>ANOMALY: DETECTED</div>
        <div class="hud br">CODETOOPIA SYSTEMS<br>EST. 2026</div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="main-ui">
            <div style="color: #22d3ee; letter-spacing: 5px;">CODETOOPIA SYSTEMS</div>
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
    st.markdown("<style>.stApp {background: #020617; color: white;}</style>", unsafe_allow_html=True)
    st.title("THERMAL TELEMETRY ARCHIVE")
    df = pd.DataFrame({'Continent': ['Asia', 'Europe'], 'Country': ['Vietnam', 'France'], 'Year': [2020, 2021], 'Temperature': [28.5, 18.3]})
    cont = st.sidebar.selectbox("CONTINENT", df['Continent'].unique())
    coun = st.sidebar.selectbox("NATION", df[df['Continent'] == cont]['Country'].unique())
    fig = px.line(df[df['Country'] == coun], x='Year', y='Temperature', template="plotly_dark")
    fig.update_traces(line_color='#fb923c')
    st.plotly_chart(fig, use_container_width=True)
    if st.sidebar.button("EXIT MISSION"):
        st.session_state.page = "WELCOME"
        st.rerun()