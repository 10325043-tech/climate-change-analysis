import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CLIMATE VAULT 3.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp { background: #000; color: #fff; font-family: 'Orbitron', sans-serif; }
    
    .hero-container {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 80vh; text-align: center;
    }
    
    .neon-title {
        font-size: 8rem; color: #fff; text-transform: uppercase; letter-spacing: 10px;
        text-shadow: 0 0 20px #38bdf8, 0 0 40px #38bdf8;
    }
    
    div.stButton > button {
        background: rgba(56, 189, 248, 0.1); border: 2px solid #38bdf8; color: #38bdf8;
        padding: 20px 60px; font-size: 2rem; border-radius: 50px; transition: 0.3s;
    }
    
    div.stButton > button:hover { background: #38bdf8; color: #000; box-shadow: 0 0 30px #38bdf8; }
    
    .card {
        background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px;
        border: 1px solid #38bdf8; margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/10325043-tech/climate-change-analysis/refs/heads/main/GlobalLandTemperaturesByCountry.csv")
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    return df.dropna(subset=['AverageTemperature'])

if 'state' not in st.session_state: st.session_state.state = "HOME"
df = load_data()

if st.session_state.state == "HOME":
    st.markdown('<div class="hero-container"><div class="neon-title">CLIMATE VAULT</div></div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    if c2.button("INITIALIZE SYSTEM"):
        st.session_state.state = "SELECT"
        st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="text-align:center;">SELECT SECTOR</h1>', unsafe_allow_html=True)
    cols = st.columns(3)
    continents = ["ASIA", "EUROPE", "AFRICA", "NORTH AMERICA", "SOUTH AMERICA", "OCEANIA"]
    for i, cont in enumerate(continents):
        if cols[i % 3].button(cont, use_container_width=True):
            st.session_state.target = cont
            st.session_state.state = "VAULT"
            st.rerun()

elif st.session_state.state == "VAULT":
    st.markdown(f'<h1 style="color:#38bdf8;">{st.session_state.target} SECTOR</h1>', unsafe_allow_html=True)
    
    with st.sidebar:
        st.header("CONTROL CENTER")
        year_range = st.slider("TIMELINE", 1750, 2013, (1900, 2013))
        countries = st.multiselect("TARGET COUNTRIES", sorted(df['Country'].unique()))
    
    df_f = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
    
    tab1, tab2 = st.tabs(["GEOGRAPHIC VIEW", "ANALYTICS"])
    
    with tab1:
        if not df_f.empty:
            fig = px.choropleth(df_f, locations="Country", locationmode="country names", color="AverageTemperature",
                                scope=st.session_state.target.lower().replace(" ", ""), template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)
            
    with tab2:
        if countries:
            fig_line = px.line(df_f[df_f['Country'].isin(countries)], x="Year", y="AverageTemperature", color="Country", template="plotly_dark")
            st.plotly_chart(fig_line, use_container_width=True)
            for c in countries:
                temp_avg = df_f[df_f["Country"] == c]["AverageTemperature"].mean()
                st.markdown(f'<div class="card"><strong>{c}</strong> | AVG TEMP: {temp_avg:.2f}°C</div>', unsafe_allow_html=True)
        else:
            st.info("SELECT COUNTRIES IN SIDEBAR TO START ANALYSIS")

    if st.button("RESET"):
        st.session_state.state = "SELECT"
        st.rerun()