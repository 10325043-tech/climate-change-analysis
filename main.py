import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CLIMATE VAULT 2.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: #050505; color: #fff; font-family: 'Orbitron', sans-serif; }
    .neon-text { color: #38bdf8; text-shadow: 0 0 10px #38bdf8; }
    .card { background: #0a0a0a; border: 1px solid #38bdf8; padding: 20px; border-radius: 10px; }
    div.stButton > button { background: transparent; border: 1px solid #38bdf8; color: #38bdf8; padding: 10px 30px; }
    div.stButton > button:hover { background: #38bdf8; color: #000; }
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
    st.markdown('<div style="text-align:center; margin-top:20vh;"><h1 style="font-size:80px;" class="neon-text">CLIMATE VAULT 2.0</h1></div>', unsafe_allow_html=True)
    if st.button("INITIALIZE SYSTEM"):
        st.session_state.state = "SELECT"
        st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h2 style="text-align:center;">SELECT SECTOR</h2>', unsafe_allow_html=True)
    continents = ["ASIA", "EUROPE", "AFRICA", "NORTH AMERICA", "SOUTH AMERICA", "OCEANIA"]
    cols = st.columns(3)
    for i, cont in enumerate(continents):
        if cols[i%3].button(cont, use_container_width=True):
            st.session_state.target = cont
            st.session_state.state = "VAULT"
            st.rerun()

elif st.session_state.state == "VAULT":
    st.markdown(f'<h2 class="neon-text">VAULT: {st.session_state.target}</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        year_range = st.slider("DECADE RANGE", 1750, 2013, (1900, 2013))
        df_f = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
        fig_map = px.choropleth(df_f, locations="Country", locationmode="country names", color="AverageTemperature", 
                                scope=st.session_state.target.lower().replace(" ", ""), template="plotly_dark")
        st.plotly_chart(fig_map, use_container_width=True)

    with col2:
        countries = st.multiselect("COMPARE COUNTRIES", sorted(df_f['Country'].unique()))
        if countries:
            fig_line = px.line(df_f[df_f['Country'].isin(countries)], x="Year", y="AverageTemperature", color="Country", template="plotly_dark")
            st.plotly_chart(fig_line, use_container_width=True)
            for c in countries:
                st.markdown(f'<div class="card"><strong>{c}</strong>: Avg Temp {(df_f[df_f["Country"]==c]["AverageTemperature"].mean()):.2f}°C</div>', unsafe_allow_html=True)

    if st.button("BACK"):
        st.session_state.state = "SELECT"
        st.rerun()