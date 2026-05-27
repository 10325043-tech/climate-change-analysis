import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                    url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Page 1: Dashboard */
    .home-wrapper {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        justify-content: flex-start;
        height: 80vh;
        padding-top: 80px;
        padding-right: 8%;
    }

    .group-brand {
        font-family: 'Orbitron', sans-serif;
        color: #38bdf8;
        letter-spacing: 12px;
        font-size: 1.4rem;
        margin-bottom: 5px;
    }

    .main-hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 6.5rem;
        color: #fff;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.8);
        margin: 0;
        line-height: 0.9;
        text-align: right;
    }

    /* Professional Neon Button */
    div.stButton > button {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 2px solid #38bdf8 !important;
        color: #38bdf8 !important;
        padding: 15px 50px !important;
        font-size: 1.2rem !important;
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 4px !important;
        transition: 0.4s !important;
        margin-top: 40px !important;
    }

    div.stButton > button:hover {
        background: #38bdf8 !important;
        color: #000 !important;
        box-shadow: 0 0 40px #38bdf8;
    }

    /* Page 2: Continent Selection */
    .selection-container {
        text-align: center;
        padding: 20px;
    }

    .continent-card {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid #1e293b;
        border-radius: 15px;
        padding: 10px;
        transition: 0.4s;
        margin-bottom: 20px;
    }

    .continent-card:hover {
        border-color: #38bdf8;
        transform: translateY(-10px);
        background: rgba(30, 41, 59, 0.9);
    }

    .img-fluid {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 15px;
    }

    .cont-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.2rem;
        color: #fff;
        letter-spacing: 3px;
    }
    </style>
""", unsafe_allow_html=True)

if 'app_state' not in st.session_state:
    st.session_state.app_state = "HOME"

assets = {
    "Asia": "https://images.unsplash.com/photo-1535139262974-676fe33f5d0c",
    "Europe": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b",
    "Africa": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e",
    "North America": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
    "South America": "https://images.unsplash.com/photo-1589519160732-57fc498494f8",
    "Oceania": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be"
}

if st.session_state.app_state == "HOME":
    st.markdown("""
        <div class="home-wrapper">
            <div class="group-brand">CODETOOPIA</div>
            <h1 class="main-hero-title">CLIMATE<br>VAULT</h1>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1, 0.4])
    with c3:
        if st.button("INITIALIZE"):
            st.session_state.app_state = "SELECT"
            st.rerun()

elif st.session_state.app_state == "SELECT":
    st.markdown('<h1 style="text-align:center; font-family:Orbitron; letter-spacing:10px; color:#38bdf8; margin-bottom:40px;">MISSION SELECTION</h1>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    for i, (name, url) in enumerate(assets.items()):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="continent-card">
                    <img src="{url}" class="img-fluid">
                    <div class="cont-title">{name.upper()}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"SELECT {name.upper()}", use_container_width=True):
                st.session_state.target = name
                st.session_state.app_state = "VAULT"
                st.rerun()

elif st.session_state.app_state == "VAULT":
    st.markdown(f'<h1 style="text-align:center; font-family:Orbitron; letter-spacing:5px;">VAULT: {st.session_state.target.upper()}</h1>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background:rgba(30,41,59,0.8); padding:100px; border-radius:20px; border:1px solid #38bdf8; text-align:center; margin-top:50px;">
            <h2 style="color:#38bdf8; font-family:Orbitron;">ACCESS GRANTED</h2>
            <p style="font-size:1.5rem; letter-spacing:3px;">SYSTEM ONLINE - TELEMETRY DECRYPTED</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("RETURN TO SYSTEM"):
        st.session_state.app_state = "SELECT"
        st.rerun()