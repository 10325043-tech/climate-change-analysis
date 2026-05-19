import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Codetoopia - Climate Vault", layout="wide", initial_sidebar_state="collapsed")

if "page" not in st.session_state:
    st.session_state.page = "WELCOME"

if st.session_state.page == "WELCOME":
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Share+Tech+Mono&display=swap');
        
        .stApp {
            background: linear-gradient(rgba(2, 6, 23, 0.4), rgba(2, 6, 23, 0.4)), 
                        url('https://images.unsplash.com/photo-1506318137071-a8e063b4aec0?q=80&w=2070&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        
        .main-wrapper {
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            height: 90vh; color: #ffffff; font-family: 'Orbitron', sans-serif;
        }
        
        .title { font-size: 85px; letter-spacing: 25px; margin: 0; text-shadow: 0 0 30px rgba(0,255,255,0.5); }
        .subtitle { font-size: 18px; letter-spacing: 12px; color: #94a3b8; margin-top: 15px; margin-bottom: 40px; }
        
        .globe { width: 300px; height: 300px; margin-bottom: 40px; }
        
        div.stButton > button {
            background: transparent !important;
            color: #00ffff !important;
            border: 1px solid #00ffff !important;
            padding: 15px 60px !important;
            font-family: 'Share Tech Mono', monospace !important;
            font-size: 18px !important;
            letter-spacing: 6px !important;
            transition: 0.4s !important;
        }
        div.stButton > button:hover { background: #00ffff !important; color: #000 !important; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="main-wrapper">
            <h1 class="title">CLIMATE VAULT</h1>
            <p class="subtitle">PLANETARY THERMAL FORENSICS</p>
            <img src="https://img.icons8.com/ios/300/00ffff/earth-planet.png" class="globe">
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("INITIALIZE ANALYSIS"):
            st.session_state.page = "ANALYSIS"
            st.rerun()

elif st.session_state.page == "ANALYSIS":
    st.markdown("<style>.stApp {background: #020617; color: #fff;}</style>", unsafe_allow_html=True)
    st.title("THERMAL TELEMETRY ARCHIVE")
    
    df = pd.DataFrame({
        'Continent': ['Asia', 'Asia', 'Europe', 'Europe'],
        'Country': ['Vietnam', 'Japan', 'France', 'Germany'],
        'Year': [2020, 2021, 2020, 2021],
        'Temperature': [28.5, 27.2, 18.3, 17.8]
    })

    st.sidebar.markdown("### MISSION CONTROLS")
    cont = st.sidebar.selectbox("CONTINENT", df['Continent'].unique())
    coun = st.sidebar.selectbox("NATION", df[df['Continent'] == cont]['Country'].unique())
    
    fig = px.line(df[df['Country'] == coun], x='Year', y='Temperature', template="plotly_dark")
    fig.update_traces(line_color='#00ffff')
    st.plotly_chart(fig, use_container_width=True)
    
    if st.sidebar.button("EXIT MISSION"):
        st.session_state.page = "WELCOME"
        st.rerun()