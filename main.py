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
        height: 40vh; gap: 10px;
    }

    .brand { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 15px; font-size: 1.2rem; }

    .neon-title {
        font-family: 'Orbitron'; font-size: 5rem; color: #fff;
        text-shadow: 0 0 10px #38bdf8, 0 0 20px #38bdf8;
    }

    .sector-card {
        border: 1px solid #38bdf8;
        background: rgba(0,0,0,0.6);
        padding: 10px;
        margin-bottom: 10px;
    }

    .sector-card img {
        width: 100%; height: 200px; object-fit: cover;
    }

    div.stButton > button {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 1px solid #38bdf8 !important;
        color: #fff !important;
        font-family: 'Orbitron' !important;
        letter-spacing: 2px !important;
        width: 100%;
    }
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
    if c2.button("INITIALIZE SYSTEM"):
        st.session_state.state = "SELECT"
        st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="text-align:center; color:#38bdf8; font-family:Orbitron;">SELECT SECTOR</h1>', unsafe_allow_html=True)
    
    sectors = {
        "ASIA": "https://images.unsplash.com/photo-1542038784456-1ea8e935640e",
        "EUROPE": "https://images.unsplash.com/photo-1499856871958-5b9627545d1a",
        "AFRICA": "https://images.unsplash.com/photo-1489493233809-6447820a4067",
        "NORTH AMERICA": "https://images.unsplash.com/photo-1449824913935-59a10b8d2000",
        "SOUTH AMERICA": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325",
        "OCEANIA": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9"
    }
    
    cols = st.columns(3)
    for i, (name, url) in enumerate(sectors.items()):
        with cols[i % 3]:
            st.markdown(f'<div class="sector-card"><img src="{url}"></div>', unsafe_allow_html=True)
            if st.button(f"ACTIVATE {name}", key=name):
                st.session_state.target = name
                st.session_state.state = "VAULT"
                st.rerun()