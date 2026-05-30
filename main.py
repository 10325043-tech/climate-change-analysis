import streamlit as st

# Set page layout to wide to utilize full screen
st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide")

# CSS styling for Sci-Fi Console feel
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

    .console-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 90vh;
    }

    .brand-id {
        font-family: 'Orbitron', sans-serif;
        color: #38bdf8;
        font-size: 0.8rem;
        letter-spacing: 0.3rem;
        margin-bottom: 20px;
    }

    .main-terminal {
        background: rgba(0, 0, 0, 0.6);
        border: 1px solid #38bdf8;
        padding: 40px;
        text-align: center;
        width: 600px;
    }

    .title-text {
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        color: white;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .status-bar {
        height: 2px;
        background: #38bdf8;
        width: 100%;
        margin: 20px 0;
    }

    div.stButton > button {
        background: transparent !important;
        border: 1px solid #38bdf8 !important;
        color: #38bdf8 !important;
        font-family: 'Orbitron', sans-serif !important;
        padding: 10px 30px !important;
        transition: 0.3s !important;
    }

    div.stButton > button:hover {
        background: #38bdf8 !important;
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# Application logic
if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown("""
        <div class="console-wrapper">
            <div class="brand-id">CODETOOPIA | CLIMATE INTELLIGENCE DIVISION</div>
            <div class="main-terminal">
                <div class="title-text">CLIMATE VAULT</div>
                <div class="status-bar"></div>
                <p style="color: #94a3b8; font-family: 'Rajdhani';">SYSTEM OPERATIONAL. AWAITING ACCESS PROTOCOL.</p>
            </div>
    """, unsafe_allow_html=True)
    
    if st.button("INITIALIZE ACCESS"):
        st.session_state.state = "SELECT"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)