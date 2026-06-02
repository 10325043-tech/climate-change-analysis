import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072'); background-size: cover; }
    
    .hero-box { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 60vh; }
    .brand { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 15px; font-size: 1.2rem; }
    .neon-title { font-family: 'Orbitron'; font-size: 6.5rem; color: #fff; text-shadow: 0 0 20px #38bdf8; margin-bottom: 20px; }
    
    /* Nút trang 1 siêu to */
    div.stButton > button { background: rgba(56, 189, 248, 0.2) !important; border: 2px solid #38bdf8 !important; color: #fff !important; padding: 25px 100px !important; font-size: 2.2rem !important; font-family: 'Orbitron' !important; }
    
    /* Layout trang 2 */
    .grid-container { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; padding: 20px; }
    .card { background: rgba(10, 25, 45, 0.8); border: 2px solid #38bdf8; padding: 25px; text-align: center; }
    .sector-name { font-family: 'Orbitron'; color: #fff; font-size: 1.8rem; }
    .temp { font-family: 'Orbitron'; color: #38bdf8; font-size: 3rem; margin: 10px 0; }
    .status { font-family: 'Orbitron'; color: #aaa; font-size: 1rem; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown('<div class="hero-box"><div class="brand">CODETOOPIA</div><div class="neon-title">CLIMATE VAULT</div></div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    if c2.button("INITIALIZE SYSTEM"):
        st.session_state.state = "SELECT"
        st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="color:#fff; font-family:Orbitron; text-align:center;">SELECT SECTOR</h1>', unsafe_allow_html=True)
    
    sectors = {
        "OCEANIA": "+34°C", "ASIA": "+34°C", "EUROPE": "+22°C",
        "AFRICA": "+28°C", "NORTH AMERICA": "+34.2°C", "SOUTH AMERICA": "+31.8°C"
    }
    
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    for name, temp in sectors.items():
        st.markdown(f'''
            <div class="card">
                <div class="sector-name">{name}</div>
                <div class="temp">{temp}</div>
                <div class="status">HEAT STATUS: SECURE</div>
            </div>
        ''', unsafe_allow_html=True)
        if st.button(f"OPEN {name} VAULT", key=name):
            st.session_state.target = name
            st.session_state.state = "VAULT"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.state == "VAULT":
    st.title(f"VAULT ACCESS: {st.session_state.target}")
    if st.button("RETURN"):
        st.session_state.state = "SELECT"
        st.rerun()