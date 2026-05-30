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
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 60vh;
        gap: 10px;
    }

    .brand { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 15px; font-size: 1.2rem; }

    .neon-title {
        font-family: 'Orbitron';
        font-size: 6.5rem;
        color: #fff;
        line-height: 0.9;
        text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #38bdf8, 0 0 30px #38bdf8, 0 0 40px #38bdf8;
    }

    div.stButton > button {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 2px solid #38bdf8 !important;
        color: #fff !important;
        padding: 20px 80px !important;
        font-size: 1.8rem !important;
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 5px !important;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.3) !important;
        transition: 0.3s !important;
    }

    div.stButton > button:hover {
        background: #38bdf8 !important;
        color: #000 !important;
        transform: scale(1.05);
    }

    .card-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        background: rgba(0, 0, 0, 0.6);
        border: 1px solid #38bdf8;
        padding: 20px;
        transition: 0.3s;
        cursor: pointer;
    }

    .card-container:hover {
        border-color: #fff;
        box-shadow: 0 0 20px #38bdf8;
    }

    .card-img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        margin-bottom: 15px;
    }

    .card-text {
        font-family: 'Orbitron';
        color: #fff;
        font-size: 1.2rem;
    }
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
    st.markdown('<h1 style="text-align:center; color:#38bdf8; font-family:Orbitron; margin-bottom:50px;">SELECT SECTOR</h1>', unsafe_allow_html=True)
    
    continents = {
        "ASIA": "https://images.unsplash.com/photo-1535139262974-676fe33f5d0c",
        "EUROPE": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b",
        "AFRICA": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e",
        "NORTH AMERICA": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
        "SOUTH AMERICA": "https://images.unsplash.com/photo-1526779233959-1e3595679c65",
        "OCEANIA": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be"
    }
    
    cols = st.columns(3)
    for i, (name, url) in enumerate(continents.items()):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="card-container">
                    <img src="{url}" class="card-img">
                    <div class="card-text">{name}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"ACTIVATE {name}", key=name, use_container_width=True):
                st.session_state.target = name
                st.session_state.state = "VAULT"
                st.rerun()
            st.write("")