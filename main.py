import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: radial-gradient(circle at center, #0f172a 0%, #020617 100%); font-family: 'Orbitron', sans-serif; color: #fff; }
    
    .hero-box { display: flex; flex-direction: column; align-items: flex-end; justify-content: center; height: 50vh; padding-right: 15%; }
    .brand-tag { color: #38bdf8; letter-spacing: 20px; text-transform: uppercase; margin-bottom: 10px; }
    .main-title { font-size: 8rem; letter-spacing: 30px; text-shadow: 0 0 20px #38bdf8; margin: 0; }
    
    div.stButton > button { background: transparent !important; border: 2px solid #38bdf8 !important; color: #38bdf8 !important; padding: 20px 60px !important; font-size: 1.5rem !important; margin-top: 50px !important; transition: 0.4s; }
    div.stButton > button:hover { background: #38bdf8 !important; color: #000 !important; box-shadow: 0 0 60px #38bdf8; }
    
    .earth-node { font-size: 20rem; text-align: center; filter: drop-shadow(0 0 80px #38bdf8); animation: rotate 30s linear infinite; }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    
    .continent-img { width: 100%; border-radius: 30px; border: 3px solid #38bdf8; box-shadow: 0 0 40px #38bdf8; }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: st.session_state.state = "HOME"

continent_map = {
    "Asia": "https://images.unsplash.com/photo-1535139262974-676fe33f5d0c",
    "Europe": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b",
    "Africa": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e",
    "North America": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
    "South America": "https://images.unsplash.com/photo-1589519160732-57fc498494f8",
    "Oceania": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be"
}

if st.session_state.state == "HOME":
    st.markdown('<div class="hero-box"><div class="brand-tag">CODETOOPIA</div><h1 class="main-title">CLIMATE VAULT</h1></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    if col2.button("INITIALIZE SYSTEM"):
        st.session_state.state = "GLOBE"
        st.rerun()

elif st.session_state.state == "GLOBE":
    st.markdown('<h1 style="text-align:center; letter-spacing:20px;">ORBITAL SELECTION</h1>', unsafe_allow_html=True)
    st.markdown('<div class="earth-node">🌎</div>', unsafe_allow_html=True)
    cols = st.columns(6)
    for i, name in enumerate(continent_map.keys()):
        if cols[i].button(name, use_container_width=True):
            st.session_state.target = name
            st.session_state.state = "ZOOM"
            st.rerun()

elif st.session_state.state == "ZOOM":
    st.markdown(f'<h1 style="text-align:center; font-size:5rem; margin-bottom:50px;">{st.session_state.target.upper()}</h1>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f'<img src="{continent_map[st.session_state.target]}" class="continent-img">', unsafe_allow_html=True)
        if st.button("ENTER DATA VAULT", use_container_width=True):
            st.session_state.state = "DATA"
            st.rerun()

elif st.session_state.state == "DATA":
    st.markdown(f'<h1 style="text-align:center;">{st.session_state.target.upper()} ANALYSIS</h1>', unsafe_allow_html=True)
    st.markdown('<div style="background:#1e293b; padding:100px; border-radius:30px; text-align:center; border:2px solid #38bdf8;"><h2>TELEMETRY DECRYPTED</h2></div>', unsafe_allow_html=True)
    if st.button("RETURN TO ORBIT"):
        st.session_state.state = "GLOBE"
        st.rerun()