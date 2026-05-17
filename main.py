import streamlit as st
import time
import random

# --- CONFIG ---
st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide", initial_sidebar_state="collapsed")

# --- UI STYLING (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');

    .stApp {
        background: radial-gradient(circle at center, #050a15 0%, #000 100%);
        color: #00f2ff;
        font-family: 'Share Tech Mono', monospace;
    }

    /* CHỮ LED CHẠY TRÊN ĐẦU TRANG */
    .led-bar {
        height: 45px; background: #000; border: 1px solid #ff0055;
        overflow: hidden; position: relative; display: flex; align-items: center;
        margin-bottom: 20px; box-shadow: 0 0 10px #ff005533;
    }
    .led-text {
        white-space: nowrap; position: absolute; font-family: 'Orbitron';
        color: #ff0055; font-size: 1.1rem; animation: marquee 15s linear infinite;
    }
    @keyframes marquee {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }

    /* THE TERMINAL PODS */
    .data-pod {
        background: rgba(0, 242, 255, 0.03);
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-radius: 8px; padding: 15px; margin-bottom: 10px;
        transition: all 0.3s;
    }
    .data-pod:hover {
        border-color: #ff0055; background: rgba(255, 0, 85, 0.05);
    }

    /* HOLOGRAM VIEW */
    .hologram-display {
        border: 2px solid #00f2ff; border-radius: 15px; padding: 30px;
        background: rgba(0, 242, 255, 0.02); text-align: center;
        box-shadow: 0 0 30px rgba(0,242,255,0.2);
    }

    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- STATE ---
if 'step' not in st.session_state: st.session_state.step = 'gate'
if 'active_target' not in st.session_state: st.session_state.active_target = None

# --- MAP DATA ---
continents = {
    "ASIA": {"status": "DECRYPTED", "temp": "+1.5°C", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=800"},
    "EUROPE": {"status": "DECRYPTED", "temp": "+2.1°C", "img": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=800"},
    "NORTH AMERICA": {"status": "DECRYPTED", "temp": "+1.8°C", "img": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800"},
    "SOUTH AMERICA": {"status": "DECRYPTED", "temp": "+1.2°C", "img": "https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?w=800"},
    "AFRICA": {"status": "DECRYPTED", "temp": "+1.4°C", "img": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=800"},
    "OCEANIA": {"status": "DECRYPTED", "temp": "+1.1°C", "img": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?w=800"}
}

# --- LANDING PAGE ---
if st.session_state.step == 'gate':
    st.markdown("<br><br><br><p style='text-align:center; font-family:Orbitron; color:#ff0055; letter-spacing:8px;'>CODETOOPIA LABS</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-family:Orbitron; font-size:4.5rem; margin:0; text-shadow:0 0 20px #00f2ff;'>CLIMATE VAULT</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#555;'>[ ECO-SYSTEM HISTORICAL ANOMALY TERMINAL ]</p><br>", unsafe_allow_html=True)
    _, cb, _ = st.columns([2, 1, 2])
    with cb:
        if st.button("INITIALIZE SYSTEM", use_container_width=True):
            st.session_state.step = 'console'
            st.rerun()

# --- MAIN CONSOLE PAGE ---
elif st.session_state.step == 'console':
    # Chữ LED chạy trên cùng
    st.markdown("""
        <div class="led-bar">
            <div class="led-text">CODETOOPIA CORE SYSTEM SECURE // MONITORING CARBON ANOMALIES GLOBALLY // CHOOSE SECTOR...</div>
        </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1.2])

    with col_left:
        st.markdown("<h3 style='font-family:Orbitron; color:#ff0055;'>SELECT DATA CORE</h3>", unsafe_allow_html=True)
        for name in continents.keys():
            st.markdown(f"""
                <div class="data-pod">
                    <span style="font-family:Orbitron; font-weight:bold; color:white;">{name}</span><br>
                    <span style="color:#00f2ff; font-size:0.8rem;">STATUS: READY // TRANSMISSION SECURE</span>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"CONNECT TO {name}", use_container_width=True):
                st.session_state.active_target = name
                st.rerun()

    with col_right:
        if st.session_state.active_target:
            target = st.session_state.active_target
            data = continents[target]
            st.markdown(f"""
                <div class="hologram-display">
                    <h2 style="font-family:Orbitron; margin:0; color:#ff0055;">{target}</h2>
                    <p style="color:#888; margin-bottom:15px;">ANOMALY DETECTED: {data['temp']}</p>
                    <img src="{data['img']}" style="width:100%; border-radius:8px; margin-bottom:20px;">
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"OPEN {target} RESEARCH LAB", use_container_width=True):
                st.session_state.step = 'lab'
                st.rerun()
        else:
            st.markdown("""
                <div style="border:1px dashed #444; border-radius:15px; height:400px; display:flex; align-items:center; justify-content:center; color:#444;">
                    <h3>[ AWAITING CORE SELECTION ]</h3>
                </div>
            """, unsafe_allow_html=True)

# --- LAB PAGE ---
elif st.session_state.step == 'lab':
    st.markdown(f"<h1 style='font-family:Orbitron; text-align:center;'>LAB: {st.session_state.active_target}</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Biểu đồ chuẩn môn học
    st.subheader("Temperature Anomaly Over Time (1850 - 2026)")
    st.line_chart([random.uniform(1.0, 2.5) for _ in range(50)])
    
    if st.button("RETURN TO MAIN CONSOLE"):
        st.session_state.active_target = None
        st.session_state.step = 'console'
        st.rerun()