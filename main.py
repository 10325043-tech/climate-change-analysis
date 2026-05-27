import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
        font-family: 'Rajdhani', sans-serif;
        color: #e2e8f0;
    }

    /* PAGE 1: HOME */
    .home-container {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        justify-content: flex-start;
        height: 80vh;
        padding-top: 100px;
        padding-right: 10%;
        text-align: right;
    }

    .group-name {
        font-family: 'Orbitron', sans-serif;
        color: #38bdf8;
        letter-spacing: 15px;
        font-size: 1.5rem;
        margin-bottom: 0px;
    }

    .project-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 7rem;
        color: #fff;
        text-shadow: 0 0 20px #38bdf8, 0 0 40px #38bdf8;
        margin: 0;
        line-height: 1.1;
    }

    /* NEON BUTTON */
    div.stButton > button {
        background: rgba(56, 189, 248, 0.05) !important;
        border: 2px solid #38bdf8 !important;
        color: #38bdf8 !important;
        padding: 15px 50px !important;
        font-size: 1.2rem !important;
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 5px !important;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.2);
        transition: 0.4s;
    }

    div.stButton > button:hover {
        background: #38bdf8 !important;
        color: #000 !important;
        box-shadow: 0 0 50px #38bdf8;
    }

    /* PAGE 2: SELECTION */
    .selection-header {
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 10px;
        margin-bottom: 50px;
    }

    .earth-center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 400px;
        position: relative;
    }

    .earth-img {
        width: 350px;
        filter: drop-shadow(0 0 50px rgba(56, 189, 248, 0.4));
    }

    /* PAGE 3: ZOOM */
    .zoom-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 70vh;
        text-align: center;
    }

    .continent-banner {
        width: 70%;
        max-width: 900px;
        border-radius: 20px;
        border: 2px solid #38bdf8;
        box-shadow: 0 0 40px rgba(56, 189, 248, 0.3);
        cursor: pointer;
        transition: 0.5s;
    }

    .continent-banner:hover {
        transform: scale(1.02);
        box-shadow: 0 0 60px #38bdf8;
    }

    .vault-status {
        background: rgba(30, 41, 59, 0.7);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid #38bdf8;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

if 'app_state' not in st.session_state:
    st.session_state.app_state = "HOME"

continent_assets = {
    "Asia": "https://images.unsplash.com/photo-1535139262974-676fe33f5d0c",
    "Europe": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b",
    "Africa": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e",
    "North America": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
    "South America": "https://images.unsplash.com/photo-1589519160732-57fc498494f8",
    "Oceania": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be"
}

if st.session_state.app_state == "HOME":
    st.markdown("""
        <div class="home-container">
            <div class="group-name">CODETOOPIA</div>
            <h1 class="project-title">CLIMATE<br>VAULT</h1>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 0.5])
    with col2:
        st.write("") 
    with col3:
        if st.button("INITIALIZE"):
            st.session_state.app_state = "SELECTION"
            st.rerun()

elif st.session_state.app_state == "SELECTION":
    st.markdown('<h2 class="selection-header">ORBITAL SYSTEM</h2>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="earth-center">
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/22/Earth_Western_Hemisphere_transparent_background.png" class="earth-img">
        </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(6)
    for i, name in enumerate(continent_assets.keys()):
        if cols[i].button(name.upper(), use_container_width=True):
            st.session_state.selected_cont = name
            st.session_state.app_state = "ZOOM"
            st.rerun()

elif st.session_state.app_state == "ZOOM":
    target = st.session_state.selected_cont
    st.markdown(f'<h1 style="text-align:center; font-family:Orbitron; letter-spacing:10px;">{target.upper()}</h1>', unsafe_allow_html=True)
    
    st.markdown('<div class="zoom-box">', unsafe_allow_html=True)
    st.image(continent_assets[target], use_column_width=False, width=800)
    
    if st.button(f"OPEN {target.upper()} DATA VAULT", use_container_width=True):
        st.session_state.app_state = "VAULT"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.app_state == "VAULT":
    st.markdown(f'<h1 style="text-align:center; font-family:Orbitron;">VAULT: {st.session_state.selected_cont.upper()}</h1>', unsafe_allow_html=True)
    st.markdown("""
        <div class="vault-status">
            <h3 style="color:#38bdf8;">TELEMETRY STATUS: ACTIVE</h3>
            <p>Decrypting thermal dataset... 100% Complete</p>
            <p>Ready for environmental analysis.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("BACK TO SYSTEM"):
        st.session_state.app_state = "SELECTION"
        st.rerun()