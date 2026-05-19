import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

if "page" not in st.session_state:
    st.session_state.page = "WELCOME"

if st.session_state.page == "WELCOME":
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
        .stApp {
            background: url('https://images.unsplash.com/photo-1506318137071-a8e063b4aec0?q=80&w=2070&auto=format&fit=crop');
            background-size: cover; background-position: center;
        }
        .container {
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            height: 90vh; color: white; font-family: 'Share Tech Mono', monospace;
        }
        .header { text-align: center; margin-bottom: 20px; }
        .title { font-size: 80px; letter-spacing: 15px; margin: 0; }
        .subtitle { font-size: 20px; letter-spacing: 8px; color: #cbd5e1; }
        .hud { position: absolute; border: 1px solid #f97316; padding: 15px; font-size: 12px; color: #f97316; }
        .tl { top: 40px; left: 40px; } .tr { top: 40px; right: 40px; }
        .bl { bottom: 40px; left: 40px; } .br { bottom: 40px; right: 40px; }
        div.stButton > button {
            background: transparent; border: 1px solid #f97316; color: #f97316;
            padding: 15px 40px; letter-spacing: 4px; font-family: 'Share Tech Mono';
        }
        </style>
        <div class="hud tl">SYS_IDENT: OMNISCIENCE<br>PROTO_V: 9.12.0</div>
        <div class="hud tr">UPLINK: ACTIVE<br>LOC: GEO_STATIONARY</div>
        <div class="hud bl">CORE_TEMP: INCREASING<br>ANOMALY: DETECTED</div>
        <div class="hud br">CODETOOPIA SYSTEMS<br>EST. 2026</div>
        <div class="container">
            <div class="header">
                <div style="font-size: 14px; letter-spacing: 5px; color: #22d3ee;">CODETOOPIA SYSTEMS</div>
                <h1 class="title">CLIMATE VAULT</h1>
                <p class="subtitle">PLANETARY THERMAL FORENSICS</p>
            </div>
            <img src="https://img.icons8.com/ios/250/22d3ee/earth-planet.png" style="margin-bottom: 30px;">
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("INITIALIZE ANALYSIS ->"):
            st.session_state.page = "ANALYSIS"
            st.rerun()

elif st.session_state.page == "ANALYSIS":
    st.title("THERMAL TELEMETRY ARCHIVE")
    df = pd.DataFrame({'Continent': ['Asia', 'Europe'], 'Country': ['Vietnam', 'France'], 'Year': [2020, 2021], 'Temperature': [28.5, 18.3]})
    cont = st.sidebar.selectbox("CONTINENT", df['Continent'].unique())
    coun = st.sidebar.selectbox("NATION", df[df['Continent'] == cont]['Country'].unique())
    st.plotly_chart(px.line(df[df['Country'] == coun], x='Year', y='Temperature', template="plotly_dark"), use_container_width=True)
    if st.sidebar.button("EXIT"):
        st.session_state.page = "WELCOME"
        st.rerun()