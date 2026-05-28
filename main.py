import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CLIMATE VAULT", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072'); background-size: cover; background-position: center; background-attachment: fixed; }
    .hero-box { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 60vh; gap: 10px; }
    .brand { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 15px; font-size: 1.2rem; }
    .neon-title { font-family: 'Orbitron'; font-size: 6.5rem; color: #fff; line-height: 0.9; text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #38bdf8, 0 0 30px #38bdf8, 0 0 40px #38bdf8; }
    div.stButton > button { background: rgba(56, 189, 248, 0.1) !important; border: 2px solid #38bdf8 !important; color: #fff !important; padding: 20px 80px !important; font-size: 1.8rem !important; font-family: 'Orbitron', sans-serif !important; letter-spacing: 5px !important; box-shadow: 0 0 20px rgba(56, 189, 248, 0.3) !important; }
    div.stButton > button:hover { background: #38bdf8 !important; color: #000 !important; transform: scale(1.05); }
    .card { background: rgba(0, 0, 0, 0.4); padding: 0; border-radius: 15px; border: 2px solid rgba(56, 189, 248, 0.3); overflow: hidden; cursor: pointer; transition: 0.3s; }
    .card:hover { border-color: #38bdf8; box-shadow: 0 0 20px #38bdf8; transform: scale(1.03); }
    .card img { width: 100%; height: 250px; object-fit: cover; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/10325043-tech/climate-change-analysis/refs/heads/main/GlobalLandTemperaturesByCountry.csv")
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    return df.dropna(subset=['AverageTemperature'])

if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown('<div class="hero-box"><div class="brand">CODETOOPIA</div><div class="neon-title">CLIMATE VAULT</div></div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    if c2.button("INITIALIZE SYSTEM", use_container_width=True):
        st.session_state.state = "SELECT"
        st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="text-align:center; color:#38bdf8; font-family:Orbitron; margin-bottom:50px; font-size: 3.5rem;">CONTINENT SELECTION</h1>', unsafe_allow_html=True)
    continents = {"ASIA": "https://images.unsplash.com/photo-1535139262974-676fe33f5d0c", "EUROPE": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b", "AFRICA": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e", "NORTH AMERICA": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29", "SOUTH AMERICA": "https://images.unsplash.com/photo-1526779233959-1e3595679c65", "OCEANIA": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be"}
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
    
    y_range = st.slider("SELECT TIME RANGE", 1750, 2013, (1900, 2013))
    df_f = df[(df['Year'] >= y_range[0]) & (df['Year'] <= y_range[1])]
    
    col_map, col_controls = st.columns([2.5, 1])
    
    with col_map:
        fig_map = px.choropleth(df_f.groupby('Country')['AverageTemperature'].mean().reset_index(), 
                                locations="Country", locationmode="country names", color="AverageTemperature",
                                scope=st.session_state.target.lower().replace(" ", ""), 
                                color_continuous_scale="RdYlBu_r")
        fig_map.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), margin=dict(l=0,r=0,t=0,b=0), geo=dict(bgcolor='rgba(0,0,0,0)'))
        st.plotly_chart(fig_map, use_container_width=True)
        
    with col_controls:
        countries_in_scope = sorted(df_f['Country'].unique())
        sel = st.multiselect("SELECT COUNTRIES", countries_in_scope)
        if sel:
            df_sel = df_f[df_f['Country'].isin(sel)]
            fig_line = px.line(df_sel, x="Year", y="AverageTemperature", color="Country", template="plotly_dark")
            fig_line.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_line, use_container_width=True)
            
    if st.button("RETURN TO SELECTION"):
        st.session_state.state = "SELECT"
        st.rerun()