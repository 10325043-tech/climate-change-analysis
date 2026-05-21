import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: linear-gradient(135deg, #020617 0%, #1e1b4b 100%); color: #e2e8f0; font-family: 'Orbitron', sans-serif; }
    .hero { text-align: center; margin-top: 15vh; }
    .group { color: #38bdf8; letter-spacing: 10px; font-size: 14px; }
    .title { font-size: 80px; font-weight: 800; color: #fff; margin: 10px 0; text-shadow: 0 0 30px #38bdf8; }
    .desc { font-size: 16px; letter-spacing: 8px; color: #94a3b8; }
    div.stButton > button { background: transparent; border: 2px solid #38bdf8; color: #38bdf8; padding: 15px 50px; font-size: 18px; letter-spacing: 5px; margin-top: 50px; transition: 0.3s; }
    div.stButton > button:hover { background: #38bdf8; color: #020617; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero">
        <div class="group">CODETOOPIA</div>
        <h1 class="title">CLIMATE VAULT</h1>
        <p class="desc">PLANETARY THERMAL FORENSICS</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("INITIALIZE ANALYSIS"):
        st.switch_page("pages/1_Country_Selection.py")