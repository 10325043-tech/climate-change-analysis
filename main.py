import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp { background: #000; }
    
    .hero-box {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 60vh; gap: 10px;
    }
    
    .brand { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 15px; font-size: 1.2rem; }
    
    .neon-title {
        font-family: 'Orbitron'; font-size: 6.5rem; color: #fff;
        text-shadow: 0 0 20px #38bdf8;
    }
    
    div.stButton > button {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 2px solid #38bdf8 !important; color: #fff !important;
        padding: 20px 80px !important; font-size: 1.8rem !important;
        font-family: 'Orbitron', sans-serif !important;
    }

    .radar-grid {
        display: grid; grid-template-columns: 2fr 1fr; gap: 30px;
        padding: 50px; height: 80vh; align-items: center;
    }
    
    .radar-screen {
        position: relative; height: 500px; border: 2px solid #38bdf8;
        background: radial-gradient(circle, #051020 0%, #000 100%);
    }

    .pulse {
        position: absolute; width: 15px; height: 15px; border-radius: 50%;
        background: #38bdf8; box-shadow: 0 0 15px #38bdf8;
        animation: blink 1.5s infinite;
    }

    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }
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
    if st.button("INITIALIZE SYSTEM"):
        st.session_state.state = "SELECT"
        st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h2 style="color:#fff; font-family:Orbitron; text-align:center;">LIVE SECTOR SCANNER</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="radar-grid">', unsafe_allow_html=True)
    
    # Left side: Radar Simulation
    st.markdown('<div class="radar-screen">', unsafe_allow_html=True)
    # Positioning 6 sectors on the radar
    coords = [
        {"top": "150px", "left": "500px"}, {"top": "100px", "left": "200px"},
        {"top": "300px", "left": "150px"}, {"top": "350px", "left": "400px"},
        {"top": "250px", "left": "600px"}, {"top": "400px", "left": "500px"}
    ]
    for pos in coords:
        st.markdown(f'<div class="pulse" style="top:{pos["top"]}; left:{pos["left"]};"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Right side: Control Panel
    with st.container():
        st.markdown('<div style="color:#38bdf8; font-family:monospace;">', unsafe_allow_html=True)
        sectors = ["ASIA", "EUROPE", "AFRICA", "NORTH AMERICA", "SOUTH AMERICA", "OCEANIA"]
        for s in sectors:
            if st.button(f"DECRYPT {s} DATA", key=s, use_container_width=True):
                st.session_state.target = s
                st.session_state.state = "VAULT"
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.state == "VAULT":
    st.title(f"VAULT {st.session_state.target} ACCESS GRANTED")
    if st.button("TERMINATE"):
        st.session_state.state = "SELECT"
        st.rerun()