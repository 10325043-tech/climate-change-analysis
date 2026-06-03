import streamlit as st
import pandas as pd
import plotly.express as px

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
    
    .metric-box {
        background: rgba(10, 25, 47, 0.9);
        border: 1px solid #38bdf8;
        padding: 15px;
        text-align: center;
        border-radius: 5px;
        color: #38bdf8;
        font-family: 'Orbitron';
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
    if st.button("BACK TO SELECTION"):
        st.session_state.state = "SELECT"
        st.rerun()

    df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    df = df.dropna(subset=['AverageTemperature'])
    
    countries_in_continent = df['Country'].unique().tolist()
    
    l_col, r_col = st.columns([1, 4])
    
    with l_col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        selected_nations = st.multiselect("SELECT NATIONS", countries_in_continent, default=[countries_in_continent[0]])
        years = st.slider("SELECT YEAR RANGE", int(df['Year'].min()), int(df['Year'].max()), (2000, 2012))
        simulate = st.checkbox("SIMULATE FUTURE (+10Y)")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with r_col:
        with st.spinner('DECRYPTING VAULT DATA...'):
            subset = df[(df['Country'].isin(selected_nations)) & (df['Year'] >= years[0]) & (df['Year'] <= years[1])]
            
            c1, c2 = st.columns(2)
            c1.markdown(f'<div class="metric-box">DEVIATION<br><span style="font-size:2rem;">+{subset["AverageTemperature"].std():.2f}°C</span></div>', unsafe_allow_html=True)
            c2.markdown(f'<div class="metric-box">RISK INDEX<br><span style="font-size:2rem;">{"HIGH" if subset["AverageTemperature"].mean() > 15 else "LOW"}</span></div>', unsafe_allow_html=True)
            
            fig = px.line(subset, x="Year", y="AverageTemperature", color="Country", markers=True)
            if simulate:
                fig.add_scatter(x=[years[1], years[1]+10], y=[subset["AverageTemperature"].iloc[-1], subset["AverageTemperature"].iloc[-1]+2], line=dict(dash='dash'), name="Projection")
            
            fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="#38bdf8", xaxis=dict(gridcolor="#222"), yaxis=dict(gridcolor="#222"))
            st.plotly_chart(fig, use_container_width=True)