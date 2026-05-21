import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072');
        background-size: cover;
        background-position: center;
        color: #e2e8f0;
        font-family: 'Orbitron', sans-serif;
    }
    
    .hero-wrapper {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 60vh; text-align: center;
    }
    
    .group-label { color: #38bdf8; letter-spacing: 12px; font-size: 1rem; text-transform: uppercase; }
    .main-title { font-size: 5rem; letter-spacing: 15px; color: #ffffff; margin: 10px 0; }
    .sub-title { font-size: 1.2rem; letter-spacing: 8px; color: #94a3b8; text-transform: uppercase; }
    
    /* Bố cục nút bấm */
    div.stButton > button {
        background: transparent !important; border: 2px solid #38bdf8 !important;
        color: #38bdf8 !important; padding: 15px 50px !important;
        font-size: 1.2rem !important; letter-spacing: 5px !important;
        font-family: 'Orbitron', sans-serif !important;
        transition: 0.4s !important; margin-top: 30px !important;
    }
    div.stButton > button:hover { background: #38bdf8 !important; color: #020617 !important; box-shadow: 0 0 30px #38bdf8; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero-wrapper">
        <div class="group-label">CODETOOPIA SYSTEMS</div>
        <h1 class="main-title">CLIMATE VAULT</h1>
        <p class="sub-title">PLANETARY THERMAL FORENSICS</p>
    </div>
""", unsafe_allow_html=True)

# Nút bấm căn giữa
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("INITIALIZE SYSTEM"):
        st.switch_page("pages/1_Continent_Selection.py")