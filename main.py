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

    .terminal-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin-top: 30px;
        padding: 0 50px;
    }
    .sector-card {
        background: rgba(0, 20, 40, 0.7);
        border: 1px solid #38bdf8;
        padding: 25px;
        text-align: center;
        transition: 0.4s;
    }
    .sector-card:hover {
        border-color: #fff;
        box-shadow: 0 0 15px #38bdf8;
        transform: translateY(-5px);
    }
    .data-label { font-family: 'Orbitron'; color: #38bdf8; font-size: 1.4rem; }
    .data-value { font-family: 'Courier New'; color: #fff; font-size: 1.1rem; margin: 10px 0; }
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
    if c2.button("INITIALIZE SYSTEM", use_container_width=True):
        st.session_state.state = "SELECT"
        st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="text-align:center; color:#fff; font-family:Orbitron;">SECTOR CLIMATE SCANNER</h1>', unsafe_allow_html=True)
    
    climate_data = {
        "ASIA": {"temp": "34.2°C", "status": "CRITICAL"},
        "EUROPE": {"temp": "18.5°C", "status": "STABLE"},
        "AFRICA": {"temp": "41.0°C", "status": "WARNING"},
        "NORTH AMERICA": {"temp": "22.3°C", "status": "STABLE"},
        "SOUTH AMERICA": {"temp": "28.9°C", "status": "WARNING"},
        "OCEANIA": {"temp": "25.7°C", "status": "STABLE"}
    }

    st.markdown('<div class="terminal-grid">', unsafe_allow_html=True)
    
    for name, data in climate_data.items():
        st.markdown(f'''
            <div class="sector-card">
                <div class="data-label">{name}</div>
                <div class="data-value">TEMP: {data['temp']}</div>
                <div class="data-value">STATUS: {data['status']}</div>
            </div>
        ''', unsafe_allow_html=True)
        
        if st.button(f"DECRYPT {name}", key=name, use_container_width=True):
            st.session_state.target = name
            st.session_state.state = "VAULT"
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.state == "VAULT":
    st.markdown(f'<h1 style="text-align:center; color:#38bdf8; font-family:Orbitron;">VAULT ACCESS: {st.session_state.target}</h1>', unsafe_allow_html=True)
    if st.button("RETURN TO SCANNER"):
        st.session_state.state = "SELECT"
        st.rerun()