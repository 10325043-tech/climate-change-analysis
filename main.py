import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                    url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .hero-box {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 60vh; gap: 10px;
    }

    .brand { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 15px; font-size: 1.2rem; }
    .neon-title {
        font-family: 'Orbitron'; font-size: 6.5rem; color: #fff; line-height: 0.9;
        text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #38bdf8, 0 0 30px #38bdf8, 0 0 40px #38bdf8;
    }

    div.stButton > button {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 2px solid #38bdf8 !important;
        color: #fff !important;
        padding: 20px 80px !important;
        font-size: 1.8rem !important;
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 5px !important;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.3) !important;
        transition: 0.3s !important;
    }

    div.stButton > button:hover { background: #38bdf8 !important; color: #000 !important; transform: scale(1.05); }

    .card {
        background: rgba(10, 25, 47, 0.85);
        border: 2px solid #38bdf8;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    .threat-card {
        background: rgba(255, 77, 77, 0.1);
        border: 1px solid #ff4d4d;
        padding: 15px;
        border-radius: 10px;
        color: #fff;
        font-family: 'Orbitron';
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown("""
        <div class="hero-box">
            <div class="brand">CODETOOPIA</div>
            <div class="neon-title">CLIMATE VAULT</div>
        </div>
    """, unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("INITIALIZE SYSTEM", use_container_width=True):
            st.session_state.state = "SELECT"
            st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="color:#fff; font-family:Orbitron; text-align:center; margin-bottom:40px;">SELECT CONTINENT</h1>', unsafe_allow_html=True)
    data = [
        ("OCEANIA", 34, 38, "SECURE", "#00ff9d"), 
        ("ASIA", 34, 32, "CRITICAL", "#ff4d4d"), 
        ("EUROPE", 22, 30, "SECURE", "#00ff9d"),
        ("AFRICA", 28, 35, "SECURE", "#00ff9d"), 
        ("NORTH AMERICA", 34.2, 36, "SECURE", "#00ff9d"), 
        ("SOUTH AMERICA", 31.8, 32, "SECURE", "#00ff9d")
    ]
    cols = st.columns(3)
    for i, (name, temp, threshold, status, color) in enumerate(data):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="card">
                    <h3 style="font-family:Orbitron; color:#fff;">{name}</h3>
                    <h1 style="font-family:Orbitron; color:#38bdf8; margin:5px 0;">{temp}°C</h1>
                    <p style="font-family:Orbitron; color:#aaa; font-size:0.9rem;">THRESHOLD: {threshold}°C</p>
                    <p style="font-family:Orbitron; color:{color}; font-weight:bold;">STATUS: {status}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"ENTER {name}", key=name, use_container_width=True):
                st.session_state.selected_continent = name
                st.session_state.state = "VAULT"
                st.rerun()

elif st.session_state.state == "VAULT":
    st.markdown(f'<h1 style="color:#38bdf8; font-family:Orbitron; text-align:center;">{st.session_state.selected_continent} VAULT ACTIVE</h1>', unsafe_allow_html=True)
    
    df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    df = df.dropna(subset=['AverageTemperature'])
    
    # Simulate continent filtering (Mapping example)
    continent_map = {"ASIA": ["Japan", "China", "Vietnam", "India"], "OCEANIA": ["Australia", "New Zealand"]}
    country_list = continent_map.get(st.session_state.selected_continent, df['Country'].unique().tolist())
    
    l_col, mid_col, r_col = st.columns([1, 2, 1])
    
    with l_col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        selected_nations = st.multiselect("NATIONS", country_list, default=[country_list[0]])
        year_range = st.slider("YEAR RANGE", 2000, 2012, (2000, 2012))
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button("BACK TO SELECTION"):
            st.session_state.state = "SELECT"
            st.rerun()
            
    with mid_col:
        with st.spinner('Decrypting...'):
            sub = df[(df['Country'].isin(selected_nations)) & (df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
            fig = px.line(sub, x="Year", y="AverageTemperature", color="Country", markers=True)
            fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="#38bdf8")
            st.plotly_chart(fig, use_container_width=True)
            if selected_nations:
                st.markdown(f'<div class="threat-card">THREAT LEVEL: {"HIGH" if sub["AverageTemperature"].mean() > 15 else "NORMAL"}</div>', unsafe_allow_html=True)
                
    with r_col:
        radar = go.Figure()
        radar.add_trace(go.Scatterpolar(r=[8, 5, 9], theta=['Temp', 'Volatility', 'Risk'], fill='toself', line_color='#38bdf8'))
        radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), paper_bgcolor="rgba(0,0,0,0)", font_color="#38bdf8")
        st.plotly_chart(radar, use_container_width=True)
        st.markdown('<div class="card">Data Intelligence active for selected sector.</div>', unsafe_allow_html=True)