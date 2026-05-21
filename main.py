import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%);
        color: #e2e8f0;
        font-family: 'Rajdhani', sans-serif;
    }
    
    .main-wrapper {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 80vh; text-align: center;
    }
    
    .group-label { color: #38bdf8; letter-spacing: 0.5rem; font-size: 1rem; text-transform: uppercase; }
    .project-title { font-family: 'Orbitron', sans-serif; font-size: 5rem; letter-spacing: 0.8rem; color: #fff; margin: 1rem 0; text-shadow: 0 0 20px #38bdf8; }
    .project-desc { font-size: 1.2rem; letter-spacing: 0.4rem; color: #94a3b8; text-transform: uppercase; }
    
    div.stButton > button {
        background: transparent !important; border: 2px solid #38bdf8 !important;
        color: #38bdf8 !important; padding: 1rem 3rem !important;
        font-size: 1.2rem !important; letter-spacing: 0.3rem !important;
        font-family: 'Orbitron', sans-serif !important;
        transition: 0.3s !important; margin-top: 3rem !important;
    }
    div.stButton > button:hover { background: #38bdf8 !important; color: #020617 !important; box-shadow: 0 0 20px #38bdf8; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="main-wrapper">
        <div class="group-label">CODETOOPIA SYSTEMS</div>
        <h1 class="project-title">CLIMATE VAULT</h1>
        <p class="project-desc">Planetary Thermal Forensics</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("INITIALIZE ANALYSIS"):
        st.switch_page("pages/1_Country_Selection.py")