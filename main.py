import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072');
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    .hero-box { 
        display: flex; flex-direction: column; align-items: center; justify-content: center; height: 70vh; 
    }
    
    .brand { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 20px; font-size: 1.5rem; margin-bottom: 15px; }
    
    .neon-title { 
        font-family: 'Orbitron'; font-size: 8rem; color: #fff; 
        text-shadow: 0 0 15px #fff, 0 0 30px #38bdf8, 0 0 60px #38bdf8;
        margin-bottom: 50px;
    }

    div.stButton { display: flex; justify-content: center; width: 100%; }
    
    div.stButton > button { 
        background: rgba(56, 189, 248, 0.1) !important; border: 2px solid #38bdf8 !important; 
        color: #fff !important; padding: 25px 80px !important; font-size: 2rem !important; 
        font-family: 'Orbitron' !important; box-shadow: 0 0 25px rgba(56, 189, 248, 0.5) !important;
        transition: 0.4s !important;
    }
    div.stButton > button:hover { background: #38bdf8 !important; color: #000 !important; transform: scale(1.05); box-shadow: 0 0 50px #38bdf8 !important; }

    .grid-container { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; padding: 50px; }
    
    .sector-card {
        background: rgba(10, 25, 45, 0.6); border: 2px solid #38bdf8;
        padding: 40px; text-align: center; transition: 0.4s;
    }
    .sector-card:hover { 
        background: rgba(56, 189, 248, 0.15); box-shadow: 0 0 40px #38bdf8; transform: translateY(-10px); 
    }
    
    .card-name { font-family: 'Orbitron'; color: #fff; font-size: 2rem; letter-spacing: 5px; }
    .card-temp { font-family: 'Orbitron'; color: #38bdf8; font-size: 4rem; margin-top: 20px; text-shadow: 0 0 10px #38bdf8; }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown('<div class="hero-box"><div class="brand">CODETOOPIA</div><div class="neon-title">CLIMATE VAULT</div>', unsafe_allow_html=True)
    if st.button("INITIALIZE SYSTEM"):
        st.session_state.state = "SELECT"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.state == "SELECT":
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    sectors = {"OCEANIA": "+34°C", "ASIA": "+34°C", "EUROPE": "+22°C", "AFRICA": "+28°C", "NORTH AMERICA": "+34.2°C", "SOUTH AMERICA": "+31.8°C"}
    
    for name, temp in sectors.items():
        st.markdown(f'''
            <div class="sector-card">
                <div class="card-name">{name}</div>
                <div class="card-temp">{temp}</div>
            </div>
        ''', unsafe_allow_html=True)
        if st.button(f"ACCESS {name}", key=name):
            st.session_state.target = name
            st.session_state.state = "VAULT"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.state == "VAULT":
    st.markdown(f'<h1 style="color:#38bdf8; font-family:Orbitron; text-align:center; font-size:4rem;">SYSTEM BREACH: {st.session_state.target}</h1>', unsafe_allow_html=True)
    if st.button("RETURN TO SCANNER"):
        st.session_state.state = "SELECT"
        st.rerun()