import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CODETOOPIA // CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

if "page" not in st.session_state:
    st.session_state.page = "WELCOME"

if st.session_state.page == "WELCOME":
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700&display=swap');
        
        .stApp {
            background: url('https://i.imgur.com/G5yYn5V.jpeg') no-repeat center center fixed;
            background-size: cover;
            background-color: #020617;
        }
        
        .main-wrapper {
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            height: 90vh; color: #fff; font-family: 'Share Tech Mono', monospace;
        }
        
        .title { font-family: 'Orbitron', sans-serif; font-size: 80px; letter-spacing: 15px; margin: 0; }
        .subtitle { font-size: 20px; letter-spacing: 8px; color: #cbd5e1; margin-bottom: 20px; }
        
        div.stButton > button {
            background: transparent !important;
            border: 1px solid #f97316 !important;
            color: #f97316 !important;
            padding: 15px 50px !important;
            font-size: 18px !important;
            letter-spacing: 6px !important;
            transition: 0.3s !important;
        }
        div.stButton > button:hover { background: #f97316 !important; color: #000 !important; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="main-wrapper">
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
    fig.update_traces(line_color='#f97316')
    st.plotly_chart(fig, use_container_width=True)
    
    if st.sidebar.button("EXIT MISSION"):
        st.session_state.page = "WELCOME"
        st.rerun()