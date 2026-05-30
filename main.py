import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CLIMATE VAULT 3.0", layout="wide")

# CUSTOM CSS FOR THE "WOW" FACTOR
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    /* Global Styles */
    .stApp { background: #050505; color: #fff; font-family: 'Orbitron', sans-serif; }
    
    /* Page 1 Hero */
    .hero { text-align: center; margin-top: 15vh; }
    .neon-text { font-size: 80px; color: #fff; text-shadow: 0 0 10px #38bdf8, 0 0 20px #38bdf8; }
    
    /* Interactive Elements */
    .stButton>button { 
        background: transparent !important; border: 1px solid #38bdf8 !important; 
        color: #38bdf8 !important; padding: 15px 40px !important; border-radius: 0 !important;
        transition: 0.4s;
    }
    .stButton>button:hover { background: #38bdf8 !important; color: #000 !important; }
    
    /* Dashboard Cards */
    .metric-card { 
        background: rgba(255, 255, 255, 0.03); border: 1px solid #38bdf8;
        padding: 20px; border-radius: 0; box-shadow: 0 0 10px rgba(56, 189, 248, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# DATA LOADING WITH ERROR HANDLING
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("https://raw.githubusercontent.com/10325043-tech/climate-change-analysis/refs/heads/main/GlobalLandTemperaturesByCountry.csv")
        df['dt'] = pd.to_datetime(df['dt'])
        df['Year'] = df['dt'].dt.year
        return df.dropna(subset=['AverageTemperature'])
    except:
        return pd.DataFrame()

df = load_data()
if 'state' not in st.session_state: st.session_state.state = "HOME"

# PAGE 1: HOME
if st.session_state.state == "HOME":
    st.markdown('<div class="hero"><h1 class="neon-text">CLIMATE VAULT 3.0</h1><p>PLANETARY THERMAL DATA SYSTEM</p></div>', unsafe_allow_html=True)
    if st.button("ACTIVATE SYSTEM"):
        st.session_state.state = "SELECT"
        st.rerun()

# PAGE 2: SELECTION
elif st.session_state.state == "SELECT":
    st.markdown('<h2 style="text-align:center; color:#38bdf8;">SELECT SECTOR</h2>', unsafe_allow_html=True)
    sectors = ["ASIA", "EUROPE", "AFRICA", "NORTH AMERICA", "SOUTH AMERICA", "OCEANIA"]
    cols = st.columns(3)
    for i, s in enumerate(sectors):
        if cols[i%3].button(s, use_container_width=True):
            st.session_state.target = s
            st.session_state.state = "VAULT"
            st.rerun()

# PAGE 3: DATA LAB
elif st.session_state.state == "VAULT":
    st.sidebar.markdown(f"### {st.session_state.target} CONTROL")
    year = st.sidebar.slider("YEAR RANGE", 1750, 2013, (1900, 2013))
    
    df_f = df[(df['Year'] >= year[0]) & (df['Year'] <= year[1])]
    countries = st.sidebar.multiselect("COUNTRIES", sorted(df_f['Country'].unique()))
    
    if st.button("BACK TO SELECTION"):
        st.session_state.state = "SELECT"
        st.rerun()
    
    col1, col2 = st.columns([2, 1])
    with col1:
        if not df_f.empty:
            fig = px.choropleth(df_f, locations="Country", locationmode="country names", 
                                color="AverageTemperature", scope=st.session_state.target.lower().replace(" ", ""),
                                template="plotly_dark", color_continuous_scale="RdBu_r")
            st.plotly_chart(fig, use_container_width=True)
            
    with col2:
        if countries:
            fig_line = px.line(df_f[df_f['Country'].isin(countries)], x="Year", y="AverageTemperature", 
                               color="Country", template="plotly_dark")
            st.plotly_chart(fig_line, use_container_width=True)
            st.markdown('<div class="metric-card">ANALYSIS: DATA SYNCED</div>', unsafe_allow_html=True)
        else:
            st.info("AWAITING COUNTRY SELECTION...")