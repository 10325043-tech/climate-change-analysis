import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072'); background-size: cover; font-family: 'Orbitron', sans-serif; }
    
    .hero-wrapper { display: flex; flex-direction: column; align-items: flex-end; justify-content: center; height: 50vh; padding-right: 100px; }
    .neon-title { font-size: 6rem; color: #fff; text-shadow: 0 0 15px #38bdf8, 0 0 30px #38bdf8; margin: 0; }
    
    div.stButton > button { background: transparent !important; border: 2px solid #38bdf8 !important; color: #38bdf8 !important; padding: 15px 40px !important; font-size: 1.2rem !important; margin-top: 20px !important; transition: 0.3s; }
    div.stButton > button:hover { background: #38bdf8 !important; color: #000 !important; box-shadow: 0 0 30px #38bdf8; }
    
    .node-btn { background: #1e293b; border: 1px solid #38bdf8; color: white; padding: 20px; border-radius: 50%; width: 150px; height: 150px; text-align: center; display: flex; align-items: center; justify-content: center; cursor: pointer; margin: 10px; }
    .zoom-view { animation: fadeIn 1s; text-align: center; }
    @keyframes fadeIn { from { opacity: 0; transform: scale(0.9); } to { opacity: 1; transform: scale(1); } }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "Home"

if st.session_state.page == "Home":
    st.markdown('<div class="hero-wrapper"><div style="color:#38bdf8; letter-spacing:15px;">CODETOOPIA</div><h1 class="neon-title">CLIMATE VAULT</h1></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    if col2.button("INITIALIZE SYSTEM"):
        st.session_state.page = "Globe"
        st.rerun()

elif st.session_state.page == "Globe":
    st.markdown('<h2 style="text-align:center;">ORBITAL SELECTION</h2>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown('<div style="text-align:center; font-size:15rem;">🌎</div>', unsafe_allow_html=True)
    
    continents = ["Asia", "Europe", "Africa", "North America", "South America", "Oceania"]
    cols = st.columns(6)
    for i, cont in enumerate(continents):
        with cols[i]:
            if st.button(cont, key=cont, use_container_width=True):
                st.session_state.target = cont
                st.session_state.page = "Zoom"
                st.rerun()

elif st.session_state.page == "Zoom":
    st.markdown(f'<div class="zoom-view"><h1>{st.session_state.target.upper()}</h1><div style="font-size:10rem;">📍</div><p>THERMAL VORTEX IDENTIFIED</p></div>', unsafe_allow_html=True)
    if st.button("ENTER VAULT"):
        st.session_state.page = "Data"
        st.rerun()

elif st.session_state.page == "Data":
    st.title(f"VAULT ACCESS: {st.session_state.target.upper()}")
    st.write("Temperature database synced.")
    if st.button("RESET ORBIT"):
        st.session_state.page = "Globe"
        st.rerun()