import streamlit as st

# Keep your existing Page Config and CSS
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

    /* Page 2 Styles */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-template-rows: repeat(2, 1fr);
        gap: 20px;
        padding: 20px;
        height: 80vh;
    }

    .sector-card {
        background: rgba(10, 25, 45, 0.7);
        border: 2px solid rgba(56, 189, 248, 0.3);
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: 0.3s;
    }

    .sector-card:hover {
        border-color: #38bdf8;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.5);
    }

    .sector-title { font-family: 'Orbitron'; color: #fff; font-size: 1.5rem; margin-bottom: 10px; }
    .sector-temp { font-family: 'Orbitron'; color: #38bdf8; font-size: 2.5rem; }
    .sector-status { font-family: 'Orbitron'; color: #aaa; font-size: 0.9rem; margin-bottom: 15px; }

    div.stButton > button {
        background: rgba(56, 189, 248, 0.2) !important;
        border: 1px solid #38bdf8 !important; color: #fff !important;
        padding: 10px 20px !important; width: 100% !important;
    }
    
    div.stButton > button:hover { background: #38bdf8 !important; color: #000 !important; }
    </style>
""", unsafe_allow_html=True)

# State management
if 'state' not in st.session_state: st.session_state.state = "HOME"

# Page 1: Home
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

# Page 2: Selection
elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="color:#fff; font-family:Orbitron; text-align:center;">SELECT SECTOR</h1>', unsafe_allow_html=True)
    
    sectors = {
        "OCEANIA": {"temp": "+34°C", "status": "HEAT STATUS: SECURE"},
        "ASIA": {"temp": "+34°C", "status": "HEAT STATUS: CRITICAL"},
        "EUROPE": {"temp": "+22°C", "status": "HEAT STATUS: SECURE"},
        "AFRICA": {"temp": "+28°C", "status": "HEAT STATUS: SECURE"},
        "NORTH AMERICA": {"temp": "+34.2°C", "status": "HEAT STATUS: SECURE"},
        "SOUTH AMERICA": {"temp": "+31.8°C", "status": "HEAT STATUS: SECURE"}
    }

    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    for name, data in sectors.items():
        st.markdown(f'''
            <div class="sector-card">
                <div>
                    <div class="sector-title">{name}</div>
                    <div class="sector-temp">{data['temp']}</div>
                    <div class="sector-status">{data['status']}</div>
                </div>
            </div>
        ''', unsafe_allow_html=True)
        if st.button(f"OPEN VAULT", key=name):
            st.session_state.target = name
            st.session_state.state = "VAULT"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Page 3: Vault Access
elif st.session_state.state == "VAULT":
    st.markdown(f'<div class="hero-box"><h1 style="color:#38bdf8; font-family:Orbitron;">VAULT: {st.session_state.target}</h1>', unsafe_allow_html=True)
    if st.button("RETURN TO SCANNER"):
        st.session_state.state = "SELECT"
        st.rerun()