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

    .viewport {
        height: 85vh; display: flex; flex-direction: column; align-items: center; justify-content: center;
    }

    .dashboard-grid {
        display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;
        width: 90%; max-width: 1200px;
    }

    .card {
        background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px);
        border: 1px solid rgba(56, 189, 248, 0.5); padding: 25px;
        text-align: center; transition: 0.4s; cursor: pointer;
    }

    .card:hover {
        background: rgba(56, 189, 248, 0.2); border-color: #38bdf8;
        transform: translateY(-10px); box-shadow: 0 0 20px #38bdf8;
    }

    .temp-bar-bg { height: 8px; background: #222; margin: 15px 0; }
    .temp-bar-fill { height: 100%; }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown("""
        <div class="hero-box">
            <div class="brand">CODETOOPIA</div>
            <div class="neon-title">CLIMATE VAULT</div>
        </div>
    """, unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    if c2.button("INITIALIZE SYSTEM", use_container_width=True):
        st.session_state.state = "SELECT"
        st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<div class="viewport">', unsafe_allow_html=True)
    st.markdown('<h1 style="color:#38bdf8; font-family:Orbitron; margin-bottom:30px;">SECTOR ACCESS PORTAL</h1>', unsafe_allow_html=True)
    
    sectors = {
        "ASIA": 34, "EUROPE": 18, "AFRICA": 42, 
        "NORTH AMERICA": 22, "SOUTH AMERICA": 29, "OCEANIA": 25
    }

    st.markdown('<div class="dashboard-grid">', unsafe_allow_html=True)
    for name, temp in sectors.items():
        color = "#ff4b4b" if temp > 30 else "#38bdf8"
        card_html = f'''
            <div class="card">
                <h3 style="color:#fff; font-family:Orbitron; margin:0;">{name}</h3>
                <div class="temp-bar-bg"><div class="temp-bar-fill" style="width:{temp*2}%; background:{color};"></div></div>
                <p style="color:#aaa; font-family:monospace;">TEMP: {temp}°C | SECURE</p>
            </div>
        '''
        st.markdown(card_html, unsafe_allow_html=True)
        if st.button(f"ACTIVATE {name}", key=name, use_container_width=True):
            st.session_state.target = name
            st.session_state.state = "VAULT"
            st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

elif st.session_state.state == "VAULT":
    st.markdown(f'<div class="hero-box"><h1 style="color:#38bdf8; font-family:Orbitron;">VAULT {st.session_state.target} ACTIVE</h1>', unsafe_allow_html=True)
    if st.button("TERMINATE SESSION"):
        st.session_state.state = "SELECT"
        st.rerun()