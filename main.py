import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

# Thiết lập kiểu dáng chuyên nghiệp bằng CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp { background-color: #050505; color: #00f2ff; font-family: 'Orbitron', sans-serif; }
    
    /* Khung viền HUD 4 góc */
    .hud-box {
        position: absolute; border: 1px solid #00f2ff; padding: 15px;
        background: rgba(0, 242, 255, 0.05); font-size: 11px;
    }
    .top-left { top: 20px; left: 20px; }
    .top-right { top: 20px; right: 20px; }
    .bottom-left { bottom: 20px; left: 20px; }
    .bottom-right { bottom: 20px; right: 20px; }
    
    /* Tiêu đề chính */
    .hero { text-align: center; margin-top: 150px; }
    .hero h1 { font-size: 80px; letter-spacing: 20px; color: #fff; text-shadow: 0 0 20px #00f2ff; }
    .hero p { font-size: 18px; letter-spacing: 10px; color: #00f2ff; }
    
    /* Nút bấm */
    div.stButton > button {
        background: transparent; border: 2px solid #00f2ff; color: #00f2ff;
        padding: 15px 40px; font-weight: bold; letter-spacing: 5px; transition: 0.3s;
    }
    div.stButton > button:hover { background: #00f2ff; color: #000; }
    </style>
""", unsafe_allow_html=True)

# Khởi tạo trang
if "page" not in st.session_state: st.session_state.page = "HOME"

if st.session_state.page == "HOME":
    # Vẽ HUD bằng HTML
    st.markdown("""
        <div class="hud-box top-left">SYS_IDENT: OMNISCIENCE<br>STATUS: OPERATIONAL</div>
        <div class="hud-box top-right">UPLINK: STABLE<br>ZONE: SECTOR_7</div>
        <div class="hud-box bottom-left">CORE_TEMP: 42.4°C<br>ANOMALY: NONE</div>
        <div class="hud-box bottom-right">CODETOOPIA<br>EST. 2026</div>
        
        <div class="hero">
            <h1>CLIMATE VAULT</h1>
            <p>PLANETARY THERMAL FORENSICS</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("INITIALIZE ANALYSIS"):
            st.session_state.page = "ANALYSIS"
            st.rerun()

elif st.session_state.page == "ANALYSIS":
    st.subheader("TELEMETRY DATA FEED")
    df = pd.DataFrame({'Time': ['08:00', '12:00', '16:00', '20:00'], 'Value': [24, 28, 32, 26]})
    fig = px.line(df, x='Time', y='Value', template="plotly_dark")
    fig.update_traces(line_color='#00f2ff', line_width=3)
    st.plotly_chart(fig, use_container_width=True)
    
    if st.button("RETURN"):
        st.session_state.page = "HOME"
        st.rerun()