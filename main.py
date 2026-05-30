import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');

    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .branding-top {
        position: fixed; top: 30px; left: 50px;
        font-family: 'Orbitron', sans-serif; color: #38bdf8;
        letter-spacing: 5px; font-size: 1rem;
    }

    .main-layout {
        display: flex; flex-direction: column; justify-content: center;
        height: 100vh; padding-left: 100px;
    }

    .title-main {
        font-family: 'Orbitron', sans-serif; font-size: 8rem;
        color: #ffffff; line-height: 0.9; text-transform: uppercase;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.5);
    }

    .subtitle-main {
        font-family: 'Rajdhani', sans-serif; font-size: 2rem;
        color: #38bdf8; letter-spacing: 10px; margin-top: 20px;
    }

    .btn-container { margin-top: 60px; }

    div.stButton > button {
        background: transparent !important; border: 2px solid #38bdf8 !important;
        color: #fff !important; font-family: 'Orbitron', sans-serif !important;
        font-size: 1.8rem !important; padding: 25px 80px !important;
        transition: 0.3s !important; border-radius: 0 !important;
    }

    div.stButton > button:hover {
        background: #38bdf8 !important; color: #000 !important;
        box-shadow: 0 0 40px #38bdf8 !important;
    }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown("""
        <div class="branding-top">CODETOOPIA | CLIMATE INTELLIGENCE DIVISION</div>
        <div class="main-layout">
            <h1 class="title-main">CLIMATE<br>VAULT</h1>
            <div class="subtitle-main">SYSTEM OPERATIONAL. AWAITING ACCESS PROTOCOL.</div>
            <div class="btn-container">
    """, unsafe_allow_html=True)
    
    if st.button("INITIALIZE SYSTEM"):
        st.session_state.state = "SELECT"
        st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)