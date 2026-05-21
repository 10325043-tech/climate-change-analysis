import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072');
        background-size: cover;
        background-position: center;
        font-family: 'Orbitron', sans-serif;
    }
    
    .hero-wrapper {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 50vh; text-align: center;
    }
    
    .main-title { 
        font-size: 5rem; color: #fff; margin: 0;
        text-shadow: 0 0 10px #38bdf8, 0 0 20px #38bdf8, 0 0 40px #38bdf8; 
    }
    
    /* Điều chỉnh nút bấm */
    div.stButton > button {
        background: transparent !important; 
        border: 2px solid #38bdf8 !important;
        color: #38bdf8 !important; 
        padding: 15px 40px !important;
        font-size: 1.2rem !important; 
        letter-spacing: 4px !important;
        transition: 0.3s !important;
        box-shadow: 0 0 10px #38bdf8;
    }
    div.stButton > button:hover { 
        background: #38bdf8 !important; 
        color: #000 !important; 
        box-shadow: 0 0 30px #38bdf8;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero-wrapper">
        <h1 class="main-title">CLIMATE VAULT</h1>
        <p style="color: #94a3b8; letter-spacing: 8px;">PLANETARY THERMAL FORENSICS</p>
    </div>
""", unsafe_allow_html=True)

# BẮT BUỘC: Lệnh chuyển trang nằm trong khối if
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("INITIALIZE SYSTEM"):
        st.switch_page("pages/1_Continent_Selection.py")