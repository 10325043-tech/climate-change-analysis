import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
        font-family: 'Orbitron', sans-serif;
        color: #fff;
    }

    .hero-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 60vh;
        text-align: center;
    }

    .brand-tag { color: #38bdf8; letter-spacing: 15px; font-size: 1rem; margin-bottom: 20px; }
    
    .main-header {
        font-size: 8rem;
        font-weight: 700;
        text-shadow: 0 0 20px #38bdf8, 0 0 40px #38bdf8;
        margin: 0;
        letter-spacing: 25px;
    }

    .init-btn {
        margin-top: 50px;
    }

    div.stButton > button {
        background: transparent !important;
        border: 2px solid #38bdf8 !important;
        color: #38bdf8 !important;
        padding: 20px 60px !important;
        font-size: 1.5rem !important;
        letter-spacing: 8px !important;
        transition: 0.4s !important;
    }

    div.stButton > button:hover {
        background: #38bdf8 !important;
        color: #000 !important;
        box-shadow: 0 0 50px #38bdf8;
    }

    .globe-pulse {
        font-size: 20rem;
        text-align: center;
        filter: drop-shadow(0 0 50px rgba(56, 189, 248, 0.6));
        animation: rotate 20s linear infinite;
    }

    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

    .continent-img {
        width: 100%;
        height: 350px;
        object-fit: cover;
        border: 2px solid #38bdf8;
        border-radius: 15px;
        transition: 0.4s;
    }

    .continent-img:hover {
        transform: scale(1.05);
        box-shadow: 0 0 30px #38bdf8;
    }
    </style>
""", unsafe_html=True)

if 'state' not in st.session_state: st.session_state.state = "HOME"

continent_data = {
    "Asia": "https://images.unsplash.com/photo-1535139262974-676fe33f5d0c",
    "Europe": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b",
    "Africa": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e",
    "North America": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
    "South America": "https://images.unsplash.com/photo-1589519160732-57fc498494f8",
    "Oceania": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be"
}

if st.session_state.state == "HOME":
    st.markdown("""
        <div class="hero-box">
            <div class="brand-tag">CODETOOPIA</div>
            <h1 class="main-header">CLIMATE VAULT</h1>
        </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    if col2.button("INITIALIZE SYSTEM"):
        st.session_state.state = "GLOBE"
        st.rerun()

elif st.session_state.state == "GLOBE":
    st.markdown('<h1 style="text-align:center; letter-spacing:15px; margin-bottom:50px;">PLANETARY SYSTEM</h1>', unsafe_allow_html=True)
    st.markdown('<div class="globe-pulse">🌎</div>', unsafe_allow_html=True)
    
    cols = st.columns(6)
    for i, name in enumerate(continent_data.keys()):
        if cols[i].button(name, use_container_width=True):
            st.session_state.target = name
            st.session_state.state = "ZOOM"
            st.rerun()

elif st.session_state.state == "ZOOM":
    cont = st.session_state.target
    st.markdown(f'<h1 style="text-align:center; font-size:4rem; margin-bottom:40px;">{cont.upper()}</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("", key="img_trigger", use_container_width=True):
            st.session_state.state = "DATA"
            st.rerun()
        st.markdown(f'<img src="{continent_data[cont]}" class="continent-img">', unsafe_allow_html=True)

elif st.session_state.state == "DATA":
    st.markdown(f'<h1 style="text-align:center;">{st.session_state.target.upper()} ANALYSIS</h1>', unsafe_allow_html=True)
    st.markdown('<div style="background:#1e293b; padding:100px; border-radius:20px; text-align:center; border:1px solid #38bdf8;"><h2>TELEMETRY ACTIVE</h2></div>', unsafe_allow_html=True)
    
    if st.button("RESET"):
        st.session_state.state = "HOME"
        st.rerun()