import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Climate Quest: Earth 2026", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    url('https://img.freepik.com/free-vector/pixel-art-mystical-night-sky-background_52683-119106.jpg');
        background-size: cover;
    }
    .start-container {
        display: flex; flex-direction: column; align-items: center; justify-content: center; height: 80vh;
    }
    h1 { color: #00FF00 !important; font-family: 'Courier New', monospace !important; text-shadow: 3px 3px #FF0000; font-size: 4rem !important; }
    h2, h3 { color: #00FF00 !important; font-family: 'Courier New', monospace !important; }
    .stButton>button {
        background-color: #ff4b4b; color: white; border-radius: 0px;
        padding: 20px 60px; font-size: 28px; font-weight: bold;
        border: 4px solid #fff; box-shadow: 0 0 25px #ff4b4b;
        font-family: 'Courier New', monospace;
    }
    .stButton>button:hover { background-color: #00FF00; color: black; box-shadow: 0 0 50px #00FF00; border-color: #000; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'continent' not in st.session_state:
    st.session_state.continent = None

@st.cache_data
def load_data():
    df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    df = df.dropna(subset=['AverageTemperature'])
    return df

try:
    data = load_data()
except:
    data = pd.DataFrame()

if st.session_state.page == 'home':
    st.markdown('<div class="start-container">', unsafe_allow_html=True)
    st.markdown("<h1>CLIMATE QUEST</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white !important;'>MISSION: ANALYZE PLANETARY WARMING</h3>", unsafe_allow_html=True)
    if st.button("🚀 START MISSION"):
        st.session_state.page = 'selection'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'selection':
    st.markdown("<h2 style='text-align: center;'>SELECT SECTOR</h2>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/2483/2483030.png", width=100)
        if st.button("EUROPE"):
            st.session_state.continent = "Europe"
            st.session_state.page = 'dashboard'
            st.rerun()

    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/2483/2483011.png", width=100)
        if st.button("ASIA"):
            st.session_state.continent = "Asia"
            st.session_state.page = 'dashboard'
            st.rerun()

    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/2483/2483023.png", width=100)
        if st.button("AMERICAS"):
            st.session_state.continent = "Americas"
            st.session_state.page = 'dashboard'
            st.rerun()

    with col4:
        st.image("https://cdn-icons-png.flaticon.com/512/2483/2483018.png", width=100)
        if st.button("AFRICA"):
            st.session_state.continent = "Africa"
            st.session_state.page = 'dashboard'
            st.rerun()
            
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ ABORT MISSION"):
        st.session_state.page = 'home'
        st.rerun()

elif st.session_state.page == 'dashboard':
    st.sidebar.header("SYSTEM MENU")
    if st.sidebar.button("🎮 SECTOR SELECT"):
        st.session_state.page = 'selection'
        st.rerun()
    if st.sidebar.button("🏠 MAIN MENU"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown(f"<h2>DATA FEED: {st.session_state.continent.upper()}</h2>", unsafe_allow_html=True)
    
    if data.empty:
        st.error("DATABASE ERROR: GlobalLandTemperaturesByCountry.csv not found.")
    else:
        year_range = st.slider("CHRONOLOGICAL RANGE", 1850, 2013, (1950, 2013))
        filtered_df = data[(data['Year'] >= year_range[0]) & (data['Year'] <= year_range[1])]
        
        c1, c2 = st.columns([2, 1])
        
        with c1:
            st.subheader("THERMAL ANOMALY MAP")
            map_data = filtered_df.groupby('Country')['AverageTemperature'].mean().reset_index()
            fig_map = px.choropleth(map_data, locations="Country", locationmode='country names',
                                    color="AverageTemperature", color_continuous_scale="Reds", template="plotly_dark")
            st.plotly_chart(fig_map, use_container_width=True)
            
        with c2:
            st.subheader("CRITICAL SECTORS")
            top_10 = map_data.sort_values('AverageTemperature', ascending=False).head(10)
            fig_bar = px.bar(top_10, x='AverageTemperature', y='Country', orientation='h', 
                             color='AverageTemperature', color_continuous_scale="Reds", template="plotly_dark")
            st.plotly_chart(fig_bar, use_container_width=True)

        st.write("---")
        st.subheader("HISTORICAL TEMPERATURE TRAJECTORY")
        countries = st.multiselect("SELECT NATIONS", data['Country'].unique(), default=["Vietnam", "Norway"])
        trend_df = filtered_df[filtered_df['Country'].isin(countries)]
        trend_year = trend_df.groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
        fig_line = px.line(trend_year, x="Year", y="AverageTemperature", color="Country", template="plotly_dark")
        st.plotly_chart(fig_line, use_container_width=True)

    st.error("🚨 WARNING: GLOBAL TEMPERATURE LEVELS EXCEED SAFETY THRESHOLD")