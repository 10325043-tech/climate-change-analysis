import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    .stApp { background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072'); background-size: cover; font-family: 'Orbitron', sans-serif; }
    .hero { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 50vh; }
    .neon-title { font-size: 5rem; color: #fff; text-shadow: 0 0 10px #38bdf8, 0 0 20px #38bdf8, 0 0 40px #38bdf8; margin: 0; }
    div.stButton > button { background: transparent !important; border: 2px solid #38bdf8 !important; color: #38bdf8 !important; padding: 15px 40px !important; font-size: 1.2rem !important; margin-top: 30px !important; }
    div.stButton > button:hover { background: #38bdf8 !important; color: #000 !important; box-shadow: 0 0 30px #38bdf8; }
    .card { background: #1e293b; border: 1px solid #38bdf8; padding: 30px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    st.markdown('<div class="hero"><h1 class="neon-title">CLIMATE VAULT</h1><p style="color:white; letter-spacing:8px;">PLANETARY THERMAL FORENSICS</p></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    if col2.button("INITIALIZE SYSTEM"):
        st.session_state.page = "Continent"
        st.rerun()

elif st.session_state.page == "Continent":
    st.title("SELECT CONTINENT")
    continents = ["Asia", "Europe", "Africa", "North America", "South America", "Oceania"]
    cols = st.columns(3)
    for i, cont in enumerate(continents):
        with cols[i % 3]:
            st.markdown(f'<div class="card"><h2>{cont}</h2></div>', unsafe_allow_html=True)
            if st.button(f"Analyze {cont}", key=cont, use_container_width=True):
                st.session_state.target = cont
                st.session_state.page = "Data"
                st.rerun()

elif st.session_state.page == "Data":
    st.title(f"THERMAL DATA: {st.session_state.get('target', 'N/A').upper()}")
    st.write("Temperature analysis module active.")
    if st.button("BACK TO SELECTION"):
        st.session_state.page = "Continent"
        st.rerun()