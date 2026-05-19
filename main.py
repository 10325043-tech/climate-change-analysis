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
            background: linear-gradient(rgba(2, 6, 23, 0.7), rgba(2, 6, 23, 0.7)), 
                        url('https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=2070&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
        }
        
        .hud-corner {
            position: absolute;
            font-family: 'Share Tech Mono', monospace;
            font-size: 12px;
            color: rgba(0, 255, 255, 0.6);
            padding: 20px;
            z-index: 100;
        }
        .tl { top: 10px; left: 10px; border-left: 1px solid #00ffff; border-top: 1px solid #00ffff; }
        .tr { top: 10px; right: 10px; border-right: 1px solid #00ffff; border-top: 1px solid #00ffff; text-align: right; }
        .bl { bottom: 10px; left: 10px; border-left: 1px solid #00ffff; border-bottom: 1px solid #00ffff; }
        .br { bottom: 10px; right: 10px; border-right: 1px solid #00ffff; border-bottom: 1px solid #00ffff; text-align: right; }

        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 85vh;
            color: white;
            text-align: center;
        }
        
        .group-name {
            font-family: 'Orbitron', sans-serif;
            font-size: 18px;
            letter-spacing: 8px;
            color: #00ffff;
            margin-bottom: 10px;
        }
        
        .title {
            font-family: 'Orbitron', sans-serif;
            font-size: 90px;
            font-weight: 700;
            letter-spacing: 20px;
            margin: 0;
            text-shadow: 0 0 30px rgba(0, 255, 255, 0.4);
        }
        
        .subtitle {
            font-family: 'Share Tech Mono', monospace;
            font-size: 22px;
            letter-spacing: 6px;
            margin-top: 10px;
            color: #94a3b8;
        }

        .globe-placeholder {
            width: 280px;
            height: 280px;
            margin: 30px 0;
            background: radial-gradient(circle, rgba(0, 255, 255, 0.2) 0%, rgba(0, 0, 0, 0) 70%);
            border-radius: 50%;
            border: 1px solid rgba(0, 255, 255, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 0 50px rgba(0, 255, 255, 0.1);
        }

        div.stButton > button {
            background: rgba(0, 255, 255, 0.1) !important;
            color: #00ffff !important;
            border: 1px solid #00ffff !important;
            padding: 15px 50px !important;
            font-family: 'Share Tech Mono', monospace !important;
            font-size: 20px !important;
            letter-spacing: 4px !important;
            transition: 0.3s !important;
            text-transform: uppercase;
        }
        
        div.stButton > button:hover {
            background: #00ffff !important;
            color: #020617 !important;
            box-shadow: 0 0 30px #00ffff !important;
        }
        </style>

        <div class="hud-corner tl">SYSTEM: OMNISCIENCE<br>CORE_TEMP: 32.4°C</div>
        <div class="hud-corner tr">UPLINK: SECURE<br>STATION: VALKYRIE_01</div>
        <div class="hud-corner bl">THERMAL_DATA: ACTIVE<br>SCAN_FREQ: 44.1 GHZ</div>
        <div class="hud-corner br">CODETOOPIA SYSTEMS<br>EST. 2026</div>

        <div class="main-container">
            <div class="group-name">CODETOOPIA SYSTEMS</div>
            <h1 class="title">CLIMATE VAULT</h1>
            <p class="subtitle">PLANETARY THERMAL FORENSICS</p>
            <div class="globe-placeholder">
                <img src="https://img.icons8.com/ios/150/00ffff/earth-globe.png" style="opacity: 0.6;">
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("INITIALIZE ANALYSIS"):
            st.session_state.page = "ANALYSIS"
            st.rerun()

elif st.session_state.page == "ANALYSIS":
    st.markdown("<style>.stApp {background: #020617; color: #f8fafc;}</style>", unsafe_allow_html=True)
    st.title("CLIMATE VAULT // ANALYTICS INTERFACE")
    
    mock_data = {
        'Continent': ['Asia', 'Asia', 'Asia', 'Europe', 'Europe', 'Africa', 'Americas'],
        'Country': ['Vietnam', 'Japan', 'China', 'France', 'Germany', 'Egypt', 'Canada'],
        'Year': [2020, 2021, 2022, 2020, 2021, 2022, 2023],
        'Temperature': [28.5, 27.2, 29.1, 18.3, 17.8, 31.5, 5.2]
    }
    df = pd.DataFrame(mock_data)

    st.sidebar.markdown("### MISSION CONTROLS")
    
    selected_continent = st.sidebar.selectbox("SELECT CONTINENT", df['Continent'].unique())
    
    filtered_continent = df[df['Continent'] == selected_continent]
    selected_country = st.sidebar.selectbox("SELECT NATION", filtered_continent['Country'].unique())
    
    year_range = st.sidebar.slider("TEMPORAL RANGE", 1990, 2026, (2020, 2024))

    st.subheader(f"THERMAL TELEMETRY: {selected_country.upper()}")
    
    plot_df = filtered_continent[filtered_continent['Country'] == selected_country]
    fig = px.line(plot_df, x='Year', y='Temperature', markers=True, template="plotly_dark")
    fig.update_traces(line_color='#00ffff')
    st.plotly_chart(fig, use_container_width=True)
    
    if st.sidebar.button("TERMINATE SESSION"):
        st.session_state.page = "WELCOME"
        st.rerun()