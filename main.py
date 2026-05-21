import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072');
        background-size: cover;
        background-position: center;
        color: #e2e8f0;
        font-family: 'Rajdhani', sans-serif;
    }
    
    .hero-container {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 60vh; text-align: center;
    }
    
    .group-tag { color: #38bdf8; letter-spacing: 12px; font-size: 1.2rem; font-weight: 500; text-transform: uppercase; }
    .main-title { font-family: 'Orbitron', sans-serif; font-size: 5rem; letter-spacing: 15px; color: #ffffff; margin: 10px 0; }
    .sub-tagline { font-size: 1.2rem; letter-spacing: 8px; color: #94a3b8; text-transform: uppercase; }

    div.stButton > button {
        background: transparent !important; border: 2px solid #38bdf8 !important;
        color: #38bdf8 !important; padding: 15px 50px !important;
        font-size: 1.2rem !important; letter-spacing: 5px !important;
        font-family: 'Orbitron', sans-serif !important;
        transition: 0.4s !important; margin-top: 20px !important;
    }
    div.stButton > button:hover { background: #38bdf8 !important; color: #020617 !important; box-shadow: 0 0 30px #38bdf8; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero-container">
        <div class="group-tag">CODETOOPIA SYSTEMS</div>
        <h1 class="main-title">CLIMATE VAULT</h1>
        <p class="sub-tagline">Planetary Thermal Forensics</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("INITIALIZE SYSTEM"):
        st.switch_page("pages/1_Continent_Selection.py")