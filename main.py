import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                    url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072');
        background-size: cover;
        background-attachment: fixed;
    }

    .hero-box {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 60vh; gap: 10px;
    }

    .brand { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 15px; font-size: 1.2rem; }
    
    .neon-title {
        font-family: 'Orbitron'; font-size: 6.5rem; color: #fff;
        text-shadow: 0 0 10px #38bdf8, 0 0 20px #38bdf8;
    }

    /* Grid Layout */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        padding: 40px;
    }

    .continent-card {
        background: rgba(10, 20, 35, 0.85);
        border: 2px solid rgba(56, 189, 248, 0.5);
        padding: 30px;
        text-align: center;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }

    .continent-card:hover {
        border-color: #38bdf8;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.3);
        transform: translateY(-10px);
    }

    .card-title { font-family: 'Orbitron'; font-size: 1.8rem; color: #fff; margin-bottom: 5px; }
    .card-temp { font-family: 'Orbitron'; font-size: 2.5rem; color: #38bdf8; }
    .status-badge { font-family: 'Orbitron'; font-size: 0.8rem; letter-spacing: 2px; margin-top: 10px; }
    
    .status-critical { color: #ff4d4d; text-shadow: 0 0 8px #ff4d4d; animation: blink 1.5s infinite; }
    .status-secure { color: #00ff9d; }

    @keyframes blink { 50% { opacity: 0.5; } }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: 
    st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown("""
        <div class="hero-box">
            <div class="brand">CODETOOPIA</div>
            <div class="neon-title">CLIMATE VAULT</div>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1, 1])
    if c2.button("INITIALIZE SYSTEM", use_container_width=True):
        st.session_state.state = "SELECT"
        st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="color:#fff; font-family:Orbitron; text-align:center;">SELECT CONTINENT</h1>', unsafe_allow_html=True)
    
    # Data structure: Name, Temp, Status
    continents = [
        ("OCEANIA", "+34°C", "SECURE"), ("ASIA", "+34°C", "CRITICAL"), ("EUROPE", "+22°C", "SECURE"),
        ("AFRICA", "+28°C", "SECURE"), ("NORTH AMERICA", "+34.2°C", "SECURE"), ("SOUTH AMERICA", "+31.8°C", "SECURE")
    ]
    
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    cols = st.columns(3)
    for i, (name, temp, status) in enumerate(continents):
        status_class = "status-critical" if status == "CRITICAL" else "status-secure"
        
        with cols[i % 3]:
            st.markdown(f'''
                <div class="continent-card">
                    <div class="card-title">{name}</div>
                    <div class="card-temp">{temp}</div>
                    <div class="status-badge {status_class}">STATUS: {status}</div>
                </div>
            ''', unsafe_allow_html=True)
            
            if st.button(f"OPEN {name} VAULT", key=name, use_container_width=True):
                st.session_state.target = name
                st.session_state.state = "VAULT"
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.state == "VAULT":
    st.markdown(f'<h1 style="color:#38bdf8; font-family:Orbitron; text-align:center;">{st.session_state.target} VAULT</h1>', unsafe_allow_html=True)
    if st.button("BACK TO SELECTION"):
        st.session_state.state = "SELECT"
        st.rerun()