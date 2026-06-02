import streamlit as st

st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                    url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072');
        background-size: cover; background-position: center; background-attachment: fixed;
    }

    .hero-box { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 60vh; }
    .brand { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 15px; font-size: 1.2rem; }
    .neon-title { font-family: 'Orbitron'; font-size: 6.5rem; color: #fff; text-shadow: 0 0 20px #38bdf8; margin-bottom: 20px; }

    /* Nút Initialize căn giữa và to */
    div.stButton > button { 
        background: rgba(56, 189, 248, 0.1) !important; border: 2px solid #38bdf8 !important; 
        color: #fff !important; padding: 25px 80px !important; font-size: 2rem !important; 
        font-family: 'Orbitron' !important; box-shadow: 0 0 20px rgba(56, 189, 248, 0.3) !important;
    }
    div.stButton > button:hover { background: #38bdf8 !important; color: #000 !important; transform: scale(1.05); }

    /* Lưới trang 2 */
    .grid-container { display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; padding: 40px; }
    
    /* Ô chứa nội dung */
    .sector-node {
        background: rgba(10, 25, 45, 0.7); border: 2px solid #38bdf8;
        padding: 30px; text-align: center; cursor: pointer; transition: 0.3s;
    }
    .sector-node:hover { background: rgba(56, 189, 248, 0.2); box-shadow: 0 0 30px #38bdf8; transform: translateY(-5px); }
    .node-text { font-family: 'Orbitron'; color: #fff; font-size: 1.5rem; }
    .node-temp { font-family: 'Orbitron'; color: #38bdf8; font-size: 2.5rem; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown('<div class="hero-box"><div class="brand">CODETOOPIA</div><div class="neon-title">CLIMATE VAULT</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    if c2.button("INITIALIZE SYSTEM"):
        st.session_state.state = "SELECT"
        st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="color:#fff; font-family:Orbitron; text-align:center;">SELECT SECTOR</h1>', unsafe_allow_html=True)
    st.markdown('<div class="grid-container">', unsafe_allow_html=True)
    
    sectors = {"OCEANIA": "+34°C", "ASIA": "+34°C", "EUROPE": "+22°C", "AFRICA": "+28°C", "NORTH AMERICA": "+34.2°C", "SOUTH AMERICA": "+31.8°C"}
    
    for name, temp in sectors.items():
        # Dùng st.form hoặc container button ẩn để biến cả thẻ thành nút bấm
        if st.button(f"{name}\n\n{temp}", key=name, use_container_width=True):
            st.session_state.target = name
            st.session_state.state = "VAULT"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.state == "VAULT":
    st.title(f"VAULT ACCESS: {st.session_state.target}")
    if st.button("RETURN"):
        st.session_state.state = "SELECT"
        st.rerun()