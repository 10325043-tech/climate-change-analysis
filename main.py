import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: #020617; font-family: 'Orbitron', sans-serif; color: #fff; }
    
    .hero-container { display: flex; flex-direction: column; align-items: flex-end; justify-content: center; height: 40vh; padding-right: 150px; }
    .neon-title { font-size: 5rem; text-shadow: 0 0 15px #38bdf8; margin: 0; }
    
    div.stButton > button { background: transparent !important; border: 2px solid #38bdf8 !important; color: #38bdf8 !important; padding: 15px 40px !important; font-size: 1.2rem !important; margin-top: 20px; transition: 0.3s; }
    div.stButton > button:hover { background: #38bdf8 !important; color: #000 !important; }

    .globe-node { text-align: center; padding: 20px; transition: 0.5s; cursor: pointer; }
    .globe-node:hover { transform: scale(1.2); }
    .node-icon { font-size: 3rem; color: #38bdf8; }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    st.markdown('<div class="hero-container"><div style="color:#38bdf8; letter-spacing:10px;">CODETOOPIA</div><h1 class="neon-title">CLIMATE VAULT</h1></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    if col2.button("INITIALIZE SYSTEM"):
        st.session_state.page = "Globe"
        st.rerun()

elif st.session_state.page == "Globe":
    st.markdown('<h2 style="text-align:center;">PLANETARY TELEMETRY</h2>', unsafe_allow_html=True)
    
    # Layout quả cầu ảo
    c1, c2, c3 = st.columns([1, 2, 1])
    
    # Các châu lục vây quanh quả cầu
    continents = ["Asia", "Europe", "Africa", "North America", "South America", "Oceania"]
    
    with c2:
        st.markdown('<div style="text-align:center; font-size:10rem;">🌎</div>', unsafe_allow_html=True)
        
    cols = st.columns(6)
    for i, cont in enumerate(continents):
        with cols[i]:
            if st.button(cont, key=cont, use_container_width=True):
                st.session_state.target = cont
                st.session_state.page = "Zoom"
                st.rerun()

elif st.session_state.page == "Zoom":
    st.markdown(f'<div style="text-align:center; animation: fadeIn 2s;"><h1 style="font-size:8rem;">{st.session_state.target.upper()}</h1><p>ACCESSING THERMAL DATABASE...</p></div>', unsafe_allow_html=True)
    if st.button("RETURN TO GLOBE"):
        st.session_state.page = "Globe"
        st.rerun()