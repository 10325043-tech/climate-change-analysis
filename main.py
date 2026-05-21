import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072');
        background-size: cover;
        background-position: center;
        font-family: 'Orbitron', sans-serif;
    }

    .home-header {
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        justify-content: center;
        height: 45vh;
        padding-right: 10%;
        text-align: right;
    }

    .neon-text {
        font-size: 5.5rem;
        color: #fff;
        margin: 0;
        text-shadow: 0 0 10px #38bdf8, 0 0 20px #38bdf8, 0 0 40px #38bdf8;
        letter-spacing: 15px;
    }

    .group-tag {
        color: #38bdf8;
        letter-spacing: 12px;
        font-size: 1.2rem;
        margin-bottom: 10px;
    }

    .button-container {
        display: flex;
        justify-content: flex-end;
        padding-right: 15%;
        margin-top: -20px;
    }

    div.stButton > button {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 2px solid #38bdf8 !important;
        color: #38bdf8 !important;
        padding: 15px 45px !important;
        font-size: 1.2rem !important;
        letter-spacing: 5px !important;
        font-family: 'Orbitron', sans-serif !important;
        transition: 0.5s !important;
    }

    div.stButton > button:hover {
        background: #38bdf8 !important;
        color: #000 !important;
        box-shadow: 0 0 40px #38bdf8;
    }

    .globe-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 60vh;
    }

    .massive-globe {
        font-size: 18rem;
        filter: drop-shadow(0 0 30px #38bdf8);
        animation: pulse 4s infinite ease-in-out;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    .zoom-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 70vh;
        text-align: center;
    }

    .continent-avatar {
        width: 500px;
        height: 300px;
        object-fit: cover;
        border: 3px solid #38bdf8;
        box-shadow: 0 0 30px rgba(56, 189, 248, 0.5);
        border-radius: 20px;
        cursor: pointer;
        transition: 0.5s;
    }

    .continent-avatar:hover {
        transform: scale(1.1);
        box-shadow: 0 0 50px #38bdf8;
    }
    </style>
""", unsafe_allow_html=True)

if 'app_state' not in st.session_state:
    st.session_state.app_state = "HOME"

continent_data = {
    "Asia": "https://images.unsplash.com/photo-1535139262974-676fe33f5d0c",
    "Europe": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b",
    "Africa": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e",
    "North America": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
    "South America": "https://images.unsplash.com/photo-1589519160732-57fc498494f8",
    "Oceania": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be"
}

if st.session_state.app_state == "HOME":
    st.markdown("""
        <div class="home-header">
            <div class="group-tag">CODETOOPIA</div>
            <h1 class="neon-text">CLIMATE VAULT</h1>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("INITIALIZE SYSTEM"):
        st.session_state.app_state = "GLOBE"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.app_state == "GLOBE":
    st.markdown('<h2 style="text-align:center; letter-spacing:10px; color:#38bdf8;">ORBITAL SELECTION</h2>', unsafe_allow_html=True)
    st.markdown('<div class="globe-container"><div class="massive-globe">🌎</div></div>', unsafe_allow_html=True)
    
    cols = st.columns(6)
    for i, name in enumerate(continent_data.keys()):
        if cols[i].button(name, use_container_width=True):
            st.session_state.selected_cont = name
            st.session_state.app_state = "ZOOM"
            st.rerun()

elif st.session_state.app_state == "ZOOM":
    cont = st.session_state.selected_cont
    st.markdown(f"""
        <div class="zoom-container">
            <h1 style="font-size:4rem; color:#fff; text-shadow: 0 0 20px #38bdf8;">{cont.upper()}</h1>
            <img src="{continent_data[cont]}" class="continent-avatar">
            <p style="margin-top:20px; color:#94a3b8; letter-spacing:5px;">CLICK IMAGE TO ENTER DATA VAULT</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    if col2.button(f"ACCESS {cont.upper()} ANALYSIS", use_container_width=True):
        st.session_state.app_state = "DATA"
        st.rerun()

elif st.session_state.app_state == "DATA":
    st.title(f"THERMAL ANALYSIS: {st.session_state.selected_cont.upper()}")
    st.markdown('<div style="background:rgba(30,41,59,0.8); padding:100px; border:1px solid #38bdf8; border-radius:20px; text-align:center;"><h2>DECRYPTING TELEMETRY...</h2></div>', unsafe_allow_html=True)
    
    if st.button("RESET SYSTEM"):
        st.session_state.app_state = "GLOBE"
        st.rerun()