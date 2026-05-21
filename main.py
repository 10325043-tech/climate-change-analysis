import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072');
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Rajdhani', sans-serif;
        color: #e2e8f0;
    }

    .hero-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 55vh;
        text-align: center;
    }

    .group-tag {
        font-family: 'Orbitron', sans-serif;
        color: #38bdf8;
        letter-spacing: 15px;
        font-size: 1.2rem;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .neon-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 6rem;
        color: #fff;
        text-shadow: 0 0 10px #38bdf8, 0 0 20px #38bdf8, 0 0 40px #38bdf8;
        margin: 0;
        letter-spacing: 20px;
    }

    .tagline {
        font-size: 1.5rem;
        letter-spacing: 10px;
        color: #94a3b8;
        text-transform: uppercase;
        margin-top: 20px;
    }

    .init-button-container {
        display: flex;
        justify-content: center;
        padding-left: 150px;
        margin-top: -30px;
    }

    div.stButton > button {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 2px solid #38bdf8 !important;
        color: #38bdf8 !important;
        padding: 15px 50px !important;
        font-size: 1.3rem !important;
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 5px !important;
        transition: 0.5s !important;
    }

    div.stButton > button:hover {
        background: #38bdf8 !important;
        color: #000 !important;
        box-shadow: 0 0 50px #38bdf8;
    }

    .continent-card {
        position: relative;
        height: 350px;
        border-radius: 15px;
        overflow: hidden;
        border: 1px solid #334155;
        transition: 0.4s;
        margin-bottom: 20px;
    }

    .continent-card:hover {
        border-color: #38bdf8;
        transform: translateY(-10px);
    }

    .card-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .card-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(transparent, rgba(2, 6, 23, 0.9));
        padding: 20px;
        text-align: center;
    }

    .card-hint {
        font-size: 0.8rem;
        color: #38bdf8;
        letter-spacing: 3px;
        opacity: 0;
        transition: 0.4s;
    }

    .continent-card:hover .card-hint {
        opacity: 1;
    }

    h2 { font-family: 'Orbitron', sans-serif; letter-spacing: 3px; color: #fff; }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    st.markdown("""
        <div class="hero-section">
            <div class="group-tag">CODETOOPIA</div>
            <h1 class="neon-title">CLIMATE VAULT</h1>
            <p class="tagline">Planetary Thermal Forensics</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="init-button-container">', unsafe_allow_html=True)
    if st.button("INITIALIZE SYSTEM"):
        st.session_state.page = "Continent"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "Continent":
    st.markdown('<h1 style="text-align:center; font-family:Orbitron; letter-spacing:10px; margin-bottom:50px;">SELECT REGION</h1>', unsafe_allow_html=True)
    
    continents = {
        "Asia": "https://images.unsplash.com/photo-1535139262974-676fe33f5d0c",
        "Europe": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b",
        "Africa": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e",
        "North America": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29",
        "South America": "https://images.unsplash.com/photo-1589519160732-57fc498494f8",
        "Oceania": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be"
    }
    
    cols = st.columns(3)
    for i, (name, img) in enumerate(continents.items()):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="continent-card">
                    <img src="{img}" class="card-img">
                    <div class="card-overlay">
                        <div class="card-hint">ACCESS THERMAL TELEMETRY</div>
                        <h3 style="margin:5px 0; color:white; font-family:Orbitron;">{name.upper()}</h3>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"OPEN {name.upper()} VAULT", key=name, use_container_width=True):
                st.session_state.target = name
                st.session_state.page = "Data"
                st.rerun()

elif st.session_state.page == "Data":
    st.markdown(f'<h1 style="text-align:center; font-family:Orbitron; letter-spacing:5px;">VAULT: {st.session_state.target.upper()}</h1>', unsafe_allow_html=True)
    st.markdown('<div style="background:rgba(30,41,59,0.5); padding:50px; border-radius:20px; border:1px solid #38bdf8; text-align:center;">', unsafe_allow_html=True)
    st.write("Thermal Telemetry Decryption in Progress...")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("RETURN TO SELECTION"):
        st.session_state.page = "Continent"
        st.rerun()