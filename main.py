import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT 3.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    .stApp {
        background: radial-gradient(circle at center, #0a192f 0%, #020617 100%);
        overflow: hidden;
    }

    /* Starfield effect */
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-image: radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
                          radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px);
        background-size: 550px 550px, 350px 350px;
        background-position: 0 0, 40px 60px;
        opacity: 0.3;
    }

    .hero-box {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 100vh; position: relative; z-index: 1;
    }

    .neon-title {
        font-family: 'Orbitron', sans-serif; font-size: 8rem; color: #fff;
        text-transform: uppercase; letter-spacing: 15px;
        text-shadow: 0 0 10px #38bdf8, 0 0 20px #38bdf8, 0 0 40px #38bdf8;
        animation: flicker 3s infinite;
    }

    @keyframes flicker {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }

    .status-text {
        font-family: 'Courier New', monospace; color: #38bdf8;
        font-size: 1.2rem; margin-bottom: 50px; letter-spacing: 5px;
    }

    /* Pulse Button */
    div.stButton > button {
        background: transparent !important; border: 2px solid #38bdf8 !important;
        color: #38bdf8 !important; padding: 20px 70px !important;
        font-family: 'Orbitron', sans-serif !important; font-size: 1.5rem !important;
        letter-spacing: 8px !important; transition: 0.4s !important;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(56, 189, 248, 0.4); }
        70% { box-shadow: 0 0 0 20px rgba(56, 189, 248, 0); }
        100% { box-shadow: 0 0 0 0 rgba(56, 189, 248, 0); }
    }

    div.stButton > button:hover {
        background: #38bdf8 !important; color: #000 !important;
        box-shadow: 0 0 30px #38bdf8 !important; animation: none !important;
    }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown("""
        <div class="hero-box">
            <div class="status-text">SYSTEM STATUS: OFFLINE... AWAITING AUTHORIZATION</div>
            <div class="neon-title">CLIMATE VAULT</div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("INITIALIZE"):
            st.session_state.state = "SELECT"
            st.rerun()