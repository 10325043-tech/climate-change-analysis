import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                    url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .hero-box {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 60vh; gap: 10px;
    }

    .brand { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 15px; font-size: 1.2rem; }

    .neon-title {
        font-family: 'Orbitron'; font-size: 6.5rem; color: #fff; line-height: 0.9;
        text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #38bdf8, 0 0 30px #38bdf8, 0 0 40px #38bdf8;
    }

    div.stButton > button {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 2px solid #38bdf8 !important; color: #fff !important;
        padding: 20px 80px !important; font-size: 1.8rem !important;
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 5px !important; transition: 0.3s !important;
    }

    div.stButton > button:hover {
        background: #38bdf8 !important; color: #000 !important; transform: scale(1.05);
    }

    .grid-container {
        display: grid; grid-template-columns: repeat(3, 1fr);
        gap: 25px; padding: 40px; max-width: 1200px; margin: auto;
    }
    .sector-node {
        background: rgba(0, 20, 40, 0.7); border: 1px solid #38bdf8;
        padding: 40px; text-align: center; transition: 0.3s;
    }
    .sector-node:hover { background: rgba(56, 189, 248, 0.2); box-shadow: 0 0 20px #38bdf8; }
    .title-node { font-family: 'Orbitron'; color: #38bdf8; font-size: 1.4rem; margin-bottom: 15px; }
    .status-node { font-family: 'Courier New'; color: #fff; font-size: 0.9rem; }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: 
    st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown("""
        <div class="hero-box">
            <div class="brand">CODETOOPIA</div>
            <div class="neon-title">CLIMATE VAULT</div>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("INITIALIZE SYSTEM", use_container_width=True):
            st.session_state.state = "SELECT"
            st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="text-align:center; color:#fff; font-family:Orbitron; margin-bottom:30px;">SELECT SECTOR</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    sectors = ["ASIA", "EUROPE", "AFRICA", "NORTH AMERICA", "SOUTH AMERICA", "OCEANIA"]
    
    for sector in sectors:
        st.markdown(f'''
            <div class="sector-node">
                <div class="title-node">{sector}</div>
                <div class="status-node">ID: {sector[:3].upper()}-SEC</div>
                <div class="status-node">STATUS: READY</div>
            </div>
        ''', unsafe_allow_html=True)
        if st.button(f"ACTIVATE {sector}", key=sector, use_container_width=True):
            st.session_state.target = sector
            st.session_state.state = "VAULT"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)