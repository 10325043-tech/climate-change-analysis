import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    .centered-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh;
        text-align: center;
    }
    
    .brand-text { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 10px; font-size: 1.2rem; }
    .title-text { font-family: 'Orbitron'; font-size: 6rem; color: #fff; line-height: 1; margin-bottom: 30px; }
    
    .card { background: rgba(15, 23, 42, 0.6); padding: 15px; border-radius: 15px; border: 1px solid #38bdf8; margin-bottom: 20px; transition: 0.3s; }
    .card:hover { transform: scale(1.05); border-color: #fff; }
    .card img { width: 100%; height: 180px; object-fit: cover; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown("""
        <div class="centered-container">
            <div class="brand-text">CODETOOPIA</div>
            <div class="title-text">CLIMATE VAULT</div>
        </div>
    """, unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("INITIALIZE SYSTEM", use_container_width=True):
            st.session_state.state = "SELECT"
            st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="text-align:center; font-family:Orbitron; color:#38bdf8;">ORBITAL SELECTION</h1>', unsafe_allow_html=True)
    
    continents = {
        "ASIA": "https://images.unsplash.com/photo-1535139262974-676fe33f5d0c",
        "EUROPE": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b",
        "AFRICA": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e",
        "NORTH AMERICA": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
        "SOUTH AMERICA": "https://images.unsplash.com/photo-1483729558449-99ef09a8c371",
        "OCEANIA": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be"
    }
    
    cols = st.columns(3)
    for i, (name, url) in enumerate(continents.items()):
        with cols[i % 3]:
            st.markdown(f'<div class="card"><img src="{url}"><h3 style="text-align:center; color:#fff; font-family:Orbitron;">{name}</h3></div>', unsafe_allow_html=True)
            if st.button(f"SELECT {name}", key=name, use_container_width=True):
                st.session_state.target = name
                st.session_state.state = "VAULT"
                st.rerun()

elif st.session_state.state == "VAULT":
    st.markdown(f'<h1 style="text-align:center; font-family:Orbitron; color:#38bdf8;">VAULT: {st.session_state.target}</h1>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; padding:50px; border:2px dashed #38bdf8; margin-top:50px;"><h2>SYSTEM ACCESS GRANTED</h2></div>', unsafe_allow_html=True)
    if st.button("BACK"):
        st.session_state.state = "SELECT"
        st.rerun()