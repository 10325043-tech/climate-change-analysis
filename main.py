import streamlit as st

st.set_page_config(page_title="Codetoopia - Welcome", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #001f3f, #ff4136); 
        background-size: 200% 200%;
        animation: gradient-shift 10s ease infinite;
    }
    @keyframes gradient-shift { 
        0% {background-position: 0% 50%;} 
        50% {background-position: 100% 50%;} 
        100% {background-position: 0% 50%;} 
    }
    .hero { 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        justify-content: center; 
        height: 80vh; 
        text-align: center;
    }
    .team { font-family: sans-serif; font-size: 20px; letter-spacing: 4px; color: #00f3ff; }
    .title { font-family: sans-serif; font-size: 80px; letter-spacing: 15px; color: #ffffff; text-shadow: 0 0 20px rgba(0,0,0,0.5); }
    .subtitle { font-size: 18px; letter-spacing: 3px; color: #e0e0e0; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero">
        <div class="team">GROUP: CODETOOPIA</div>
        <h1 class="title">OMNISCIENCE</h1>
        <div class="subtitle">TRACKING THE THERMAL CASCADE OF OUR PLANET</div>
    </div>
""", unsafe_allow_html=True)

if st.button("INITIALIZE MISSION"):
    st.session_state.page = "ANALYSIS"
    st.rerun()