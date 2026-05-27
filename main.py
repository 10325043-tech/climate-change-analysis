import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CLIMATE VAULT", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072'); background-size: cover; background-attachment: fixed; }
    .hero-box { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 60vh; }
    .neon-title { font-family: 'Orbitron'; font-size: 6.5rem; color: #fff; text-shadow: 0 0 20px #38bdf8; text-align: center; margin-bottom: 20px; }
    div.stButton > button { background: rgba(56, 189, 248, 0.1) !important; border: 2px solid #38bdf8 !important; color: #fff !important; padding: 20px 80px !important; font-size: 1.8rem !important; font-family: 'Orbitron'; }
    div.stButton > button:hover { background: #38bdf8 !important; color: #000 !important; }
    .card { background: rgba(0, 0, 0, 0.4); border: 2px solid rgba(56, 189, 248, 0.3); border-radius: 15px; padding: 10px; transition: 0.3s; }
    .card:hover { border-color: #38bdf8; box-shadow: 0 0 20px #38bdf8; transform: scale(1.03); }
    .card img { width: 100%; height: 250px; object-fit: cover; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/10325043-tech/climate-change-analysis/refs/heads/main/GlobalLandTemperaturesByCountry.csv")
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    df = df.dropna(subset=['AverageTemperature'])
    return df

if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown('<div class="hero-box"><h1 class="neon-title">CLIMATE VAULT</h1></div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("INITIALIZE SYSTEM"):
            st.session_state.state = "SELECT"
            st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="text-align:center; color:#38bdf8; font-family:Orbitron; font-size: 3.5rem;">CONTINENT SELECTION</h1>', unsafe_allow_html=True)
    continents = {
        "ASIA": "https://images.unsplash.com/photo-1535139262974-676fe33f5d0c",
        "EUROPE": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b",
        "AFRICA": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e",
        "NORTH AMERICA": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
        "SOUTH AMERICA": "https://images.unsplash.com/photo-1526779233959-1e3595679c65",
        "OCEANIA": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be"
    }
    cols = st.columns(3)
    for i, (name, url) in enumerate(continents.items()):
        with cols[i % 3]:
            st.markdown(f'<div class="card"><img src="{url}"></div>', unsafe_allow_html=True)
            if st.button(name, key=name, use_container_width=True):
                st.session_state.target = name
                st.session_state.state = "VAULT"
                st.rerun()

elif st.session_state.state == "VAULT":
    df = load_data()
    st.markdown(f'<h1 style="text-align:center; color:#38bdf8; font-family:Orbitron;">VAULT: {st.session_state.target}</h1>', unsafe_allow_html=True)
    y = st.select_slider("SELECT YEAR", options=sorted(df['Year'].unique()))
    c1, c2 = st.columns([1, 1])
    with c1:
        fig = px.choropleth(df[df['Year']==y], locations="Country", locationmode="country names", color="AverageTemperature", color_continuous_scale="RdYlBu_r")
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"))
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        sel = st.multiselect("SELECT COUNTRIES", df['Country'].unique())
        if sel:
            fig_l = px.line(df[df['Country'].isin(sel)], x="Year", y="AverageTemperature", color="Country", template="plotly_dark")
            fig_l.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_l, use_container_width=True)
    if st.button("RETURN TO SELECTION"):
        st.session_state.state = "SELECT"
        st.rerun()