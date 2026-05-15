import streamlit as st
import time
import random

# --- CORE CONFIG ---
st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide", initial_sidebar_state="collapsed")

# --- THE CLIMATE VAULT ENGINE (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');

    .stApp {
        background: radial-gradient(circle at center, #050a15 0%, #000 100%);
        color: #00f2ff;
        font-family: 'Share Tech Mono', monospace;
    }

    /* 3D CABINET STRUCTURE */
    .arcade-machine {
        width: 100%; max-width: 550px; height: 750px;
        background: #1a1a1a;
        border: 10px solid #333;
        border-top: 20px solid #ff0055;
        border-radius: 20px;
        position: relative;
        margin: 0 auto;
        transition: all 1s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 0 50px rgba(0,0,0,1), inset 0 0 30px rgba(0,242,255,0.1);
    }

    /* Header Matrix */
    .machine-header {
        height: 60px; background: #000; margin: 10px;
        border: 2px solid #ff0055; display: flex;
        align-items: center; justify-content: center;
        overflow: hidden;
    }
    .header-text {
        font-family: 'Orbitron'; color: #ff0055;
        font-size: 1.2rem; text-shadow: 0 0 10px #ff0055;
        animation: blink 1.5s infinite;
    }

    /* Glass Chamber */
    .glass-chamber {
        position: absolute; top: 100px; left: 30px; right: 30px; bottom: 180px;
        background: rgba(0, 242, 255, 0.02);
        border: 2px solid rgba(255,255,255,0.1);
        box-shadow: inset 0 0 50px rgba(0,0,0,0.8);
        overflow: hidden;
    }

    /* Claw Mechanism */
    .claw-rod {
        position: absolute; top: 0; left: 50%;
        width: 6px; background: #555;
        transform: translateX(-50%);
        transition: height 1.5s ease-in-out;
        z-index: 10; border-bottom: 4px solid #888;
    }
    .claw-head { position: absolute; bottom: -35px; left: -22px; font-size: 45px; }

    /* Joystick Console (The Bệ Điều Khiển) */
    .console-shelf {
        position: absolute; bottom: 20px; left: -20px; right: -20px;
        height: 120px; background: #222;
        border: 4px solid #444; border-radius: 10px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
        display: flex; align-items: center; justify-content: center;
        transform: perspective(500px) rotateX(20deg);
    }

    /* Item Heap */
    .heap {
        position: absolute; bottom: 10px; width: 100%;
        display: flex; justify-content: center; gap: 10px;
    }

    /* Animations & States */
    .move-aside { transform: translateX(-35%) scale(0.9); opacity: 0.6; }
    
    .reward-hologram {
        text-align: center;
        animation: float 3s ease-in-out infinite, glow 1.5s alternate infinite;
    }

    @keyframes blink { 0%, 100% {opacity: 1;} 50% {opacity: 0.3;} }
    @keyframes float { 0%, 100% {transform: translateY(0);} 50% {transform: translateY(-20px);} }
    @keyframes glow { from {filter: drop-shadow(0 0 5px #00f2ff);} to {filter: drop-shadow(0 0 20px #ff0055);} }

    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION ---
if 'view' not in st.session_state: st.session_state.view = 'landing'
if 'vault_items' not in st.session_state:
    st.session_state.vault_items = [
        {"name": "ASIA", "url": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=800"},
        {"name": "EUROPE", "url": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=800"},
        {"name": "NORTH AMERICA", "url": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800"},
        {"name": "SOUTH AMERICA", "url": "https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?w=800"},
        {"name": "AFRICA", "url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=800"},
        {"name": "OCEANIA", "url": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?w=800"}
    ]
if 'selected' not in st.session_state: st.session_state.selected = None
if 'grabbing' not in st.session_state: st.session_state.grabbing = False

# --- PAGE 1: LANDING ---
if st.session_state.view == 'landing':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; letter-spacing:12px; color:#ff0055;'>CODETOOPIA</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-family:Orbitron; font-size:5rem; margin:0;'>CLIMATE VAULT</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#555;'>[ SYSTEM STATUS: ENCRYPTED | 250 YEARS OF THERMAL DATA ]</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    _, c_btn, _ = st.columns([2, 1, 2])
    with c_btn:
        if st.button("BYPASS SECURITY", use_container_width=True):
            st.session_state.view = 'machine'
            st.rerun()

# --- PAGE 2: THE MACHINE ---
elif st.session_state.view == 'machine':
    has_item = st.session_state.selected is not None
    shift_class = "move-aside" if has_item else ""
    rod_h = "420px" if st.session_state.grabbing else "100px"

    col_m, col_r = st.columns([1.3, 1] if has_item else [1, 0.01])

    with col_m:
        # Drawing the Machine Structure
        st.markdown(f"""
            <div class="arcade-machine {shift_class}">
                <div class="machine-header">
                    <span class="header-text">CODETOOPIA VAULT</span>
                </div>
                <div class="glass-chamber">
                    <div class="claw-rod" style="height: {rod_h};">
                        <div class="claw-head">🏗️</div>
                    </div>
                    <div class="heap">
                        {" ".join(["<span style='font-size:30px;'>💎</span>" for _ in range(len(st.session_state.vault_items))])}
                    </div>
                </div>
                <div class="console-shelf">
                    <div style="width:30px; height:30px; background:red; border-radius:50%; box-shadow:0 0 10px red;"></div>
                    <div style="margin-left:20px; color:#444; font-size:0.7rem;">VAULT_OS v1.0</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        if not has_item and len(st.session_state.vault_items) > 0:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("ACTIVATE CLAW", use_container_width=True):
                st.session_state.grabbing = True
                st.rerun()
            
            if st.session_state.grabbing:
                time.sleep(1.5)
                st.session_state.selected = st.session_state.vault_items.pop(random.randrange(len(st.session_state.vault_items)))
                st.session_state.grabbing = False
                st.rerun()

    with col_r:
        if has_item:
            obj = st.session_state.selected
            st.markdown(f"""
                <div class="reward-hologram">
                    <h1 style="font-family:Orbitron; font-size:3.5rem; margin:0;">{obj['name']}</h1>
                    <p style="color:#ff0055; letter-spacing:5px;">CORE EXTRACTED</p>
                    <img src="{obj['url']}" style="width:100%; border:1px solid #00f2ff; border-radius:10px; margin:20px 0;">
                </div>
            """, unsafe_allow_html=True)
            if st.button("DECRYPT DATA CORE"):
                st.session_state.view = 'lab'
                st.rerun()

# --- PAGE 3: LAB ---
elif st.session_state.view == 'lab':
    st.markdown(f"<h1 style='font-family:Orbitron; text-align:center;'>LAB: {st.session_state.selected['name']}</h1>", unsafe_allow_html=True)
    st.line_chart([random.random() for _ in range(50)])
    
    if st.button("RE-ENTER VAULT"):
        st.session_state.selected = None
        st.session_state.view = 'machine'
        st.rerun()