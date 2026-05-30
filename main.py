import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    .stApp {
        background: linear-gradient(rgba(0, 10, 20, 0.5), rgba(0, 10, 20, 0.5)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .main-wrapper {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 100vh;
    }

    .glass-box {
        background: rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(56, 189, 248, 0.3);
        padding: 60px;
        text-align: center;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
        margin-bottom: 40px;
    }

    .neon-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 5rem;
        color: #fff;
        text-transform: uppercase;
        margin: 0;
        text-shadow: 0 0 10px #38bdf8, 0 0 20px #38bdf8, 0 0 40px #38bdf8;
    }

    .sub-text {
        font-family: 'Orbitron', sans-serif;
        color: #38bdf8;
        letter-spacing: 5px;
        margin-top: 10px;
    }

    div.stButton > button {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 2px solid #38bdf8 !important;
        color: #fff !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 1.5rem !important;
        padding: 20px 60px !important;
        transition: 0.4s !important;
        border-radius: 10px !important;
    }

    div.stButton > button:hover {
        background: #38bdf8 !important;
        color: #000 !important;
        box-shadow: 0 0 30px #38bdf8 !important;
    }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown("""
        <div class="main-wrapper">
            <div class="glass-box">
                <h1 class="neon-title">CLIMATE VAULT</h1>
                <div class="sub-text">PLANETARY CLIMATE INTELLIGENCE SYSTEM</div>
            </div>
    """, unsafe_allow_html=True)
    
    if st.button("INITIALIZE SYSTEM"):
        st.session_state.state = "SELECT"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)