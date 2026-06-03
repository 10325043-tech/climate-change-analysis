import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                    url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072');
        background-size: cover;
        background-attachment: fixed;
    }

    .hero-box {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 60vh; gap: 10px;
    }

    .brand { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 15px; font-size: 1.2rem; }
    
    .neon-title {
        font-family: 'Orbitron'; font-size: 6.5rem; color: #fff;
        text-shadow: 0 0 10px #38bdf8, 0 0 20px #38bdf8;
    }

    div.stButton > button {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 2px solid #38bdf8 !important;
        color: #fff !important;
        padding: 20px 80px !important;
        font-family: 'Orbitron', sans-serif !important;
        transition: 0.3s !important;
    }

    .card-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 25px;
        padding: 20px;
    }

    .continent-card {
        background: rgba(20, 30, 45, 0.8);
        border: 1px solid #38bdf8;
        padding: 30px;
        text-align: center;
        transition: 0.4s;
    }

    .continent-card:hover {
        background: rgba(56, 189, 248, 0.15);
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
        transform: translateY(-5px);
    }

    .c-name { font-family: 'Orbitron'; color: #fff; font-size: 1.8rem; margin-bottom: 10px; }
    .c-temp { font-family: 'Orbitron'; color: #38bdf8; font-size: 2.5rem; }
    .c-status { font-family: 'Orbitron'; font-size: 0.9rem; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: 
    st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown('<div class="hero-box"><div class="brand">CODETOOPIA</div><div class="neon-title">CLIMATE VAULT</div></div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    if c2.button("INITIALIZE SYSTEM"):
        st.session_state.state = "SELECT"
        st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="color:#fff; font-family:Orbitron; text-align:center; margin-bottom:40px;">SELECT CONTINENT</h1>', unsafe_allow_html=True)
    
    data = [
        ("OCEANIA", "+34°C", "SECURE", "#00ff9d"), ("ASIA", "+34°C", "CRITICAL", "#ff4d4d"), 
        ("EUROPE", "+22°C", "SECURE", "#00ff9d"), ("AFRICA", "+28°C", "SECURE", "#00ff9d"),
        ("NORTH AMERICA", "+34.2°C", "SECURE", "#00ff9d"), ("SOUTH AMERICA", "+31.8°C", "SECURE", "#00ff9d")
    ]
    
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    cols = st.columns(3)
    for i, (name, temp, status, color) in enumerate(data):
        with cols[i % 3]:
            st.markdown(f'''
                <div class="continent-card">
                    <div class="c-name">{name}</div>
                    <div class="c-temp">{temp}</div>
                    <div class="c-status" style="color:{color}">STATUS: {status}</div>
                </div>
            ''', unsafe_allow_html=True)
            if st.button(f"OPEN {name} VAULT", key=name, use_container_width=True):
                st.session_state.target = name
                st.session_state.state = "VAULT"
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.state == "VAULT":
    st.markdown(f'<h1 style="color:#38bdf8; font-family:Orbitron; text-align:center;">{st.session_state.target} VAULT ACTIVE</h1>', unsafe_allow_html=True)
    if st.button("BACK TO SELECTION"):
        st.session_state.state = "SELECT"
        st.rerun()