import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
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
        height: 70vh;
        gap: 0px;
    }
    
    .brand { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 15px; font-size: 1rem; }
    
    /* Neon Text Effect */
    .neon-title {
        font-family: 'Orbitron';
        font-size: 5.5rem;
        color: #fff;
        line-height: 0.9;
        text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #38bdf8, 0 0 30px #38bdf8, 0 0 40px #38bdf8;
    }
    
    /* Optimized Cards */
    .card { 
        background: rgba(0, 0, 0, 0.4); 
        padding: 8px; 
        border-radius: 15px; 
        border: 1px solid rgba(56, 189, 248, 0.5); 
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .card:hover { border-color: #38bdf8; box-shadow: 0 0 15px rgba(56, 189, 248, 0.4); }
    .card img { width: 100%; height: 140px; object-fit: cover; border-radius: 10px; }
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
    
    c1, c2, c3 = st.columns([1, 0.4, 1])
    with c2:
        if st.button("INITIALIZE SYSTEM", use_container_width=True):
            st.session_state.state = "SELECT"
            st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h2 style="text-align:center; color:#38bdf8; font-family:Orbitron; margin-bottom:30px;">ORBITAL SELECTION</h2>', unsafe_allow_html=True)
    
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
            st.markdown(f'<div class="card"><img src="{url}"><h4 style="text-align:center; color:#fff; font-family:Orbitron; margin:10px 0;">{name}</h4></div>', unsafe_allow_html=True)
            if st.button(f"ACCESS {name}", key=name, use_container_width=True):
                st.session_state.target = name
                st.session_state.state = "VAULT"
                st.rerun()

elif st.session_state.state == "VAULT":
    st.markdown(f'<h2 style="text-align:center; color:#38bdf8; font-family:Orbitron;">VAULT: {st.session_state.target}</h2>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; padding:60px; border:1px solid #38bdf8; background:rgba(0,0,0,0.5);"><h3>SYSTEM ACCESS ACTIVE</h3></div>', unsafe_allow_html=True)
    if st.button("BACK TO ORBIT"):
        st.session_state.state = "SELECT"
        st.rerun()