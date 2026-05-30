import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');

    .stApp {
        background: linear-gradient(rgba(0, 10, 20, 0.7), rgba(0, 10, 20, 0.7)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 85vh;
        text-align: center;
    }

    .brand-header {
        font-family: 'Orbitron', sans-serif;
        color: #38bdf8;
        letter-spacing: 12px;
        font-size: 1rem;
        margin-bottom: 10px;
        opacity: 0.8;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 60px 100px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
    }

    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 5.5rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0;
        line-height: 1.1;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.5);
    }

    .sub-text {
        font-family: 'Rajdhani', sans-serif;
        color: #94a3b8;
        font-size: 1.4rem;
        margin-top: 20px;
        letter-spacing: 4px;
        text-transform: uppercase;
    }

    .system-line {
        width: 100px;
        height: 2px;
        background: #38bdf8;
        margin: 30px auto;
        box-shadow: 0 0 10px #38bdf8;
    }

    /* Sci-fi Button Styling */
    div.stButton > button {
        background: transparent !important;
        border: 1px solid #38bdf8 !important;
        color: #38bdf8 !important;
        padding: 15px 50px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-size: 1.2rem !important;
        letter-spacing: 5px !important;
        border-radius: 0px !important;
        transition: all 0.4s ease !important;
        position: relative;
        overflow: hidden;
    }

    div.stButton > button:hover {
        background: rgba(56, 189, 248, 0.2) !important;
        color: #fff !important;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.6) !important;
        transform: translateY(-2px);
    }

    div.stButton > button:active {
        transform: translateY(0);
    }

    /* Scanning line effect */
    .glass-card::after {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 2px;
        background: rgba(56, 189, 248, 0.3);
        animation: scan 4s linear infinite;
    }

    @keyframes scan {
        0% { top: 0; }
        100% { top: 100%; }
    }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown("""
        <div class="main-container">
            <div class="brand-header">CODETOOPIA PRESENTATION</div>
            <div class="glass-card">
                <h1 class="main-title">CLIMATE<br>VAULT</h1>
                <div class="system-line"></div>
                <p class="sub-text">Planetary Climate Intelligence System</p>
            </div>
            <div style="margin-top: 50px;">
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        if st.button("ENTER THE VAULT", use_container_width=True):
            st.session_state.state = "SELECT"
            st.rerun()
            
    st.markdown("</div></div>", unsafe_allow_html=True)