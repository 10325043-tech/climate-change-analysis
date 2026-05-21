import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .stApp { background-color: #020617; color: #e2e8f0; font-family: 'Segoe UI', sans-serif; }
    .hero { text-align: center; padding-top: 15vh; }
    .title { font-size: 80px; font-weight: 800; color: #38bdf8; margin: 0; }
    .subtitle { font-size: 20px; color: #94a3b8; letter-spacing: 5px; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1 class="title">CLIMATE VAULT</h1><p class="subtitle">Planetary Thermal Forensics</p></div>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### SYSTEM STATUS")
st.sidebar.success("CORE: OPERATIONAL")
st.sidebar.info("UPLINK: STABLE")