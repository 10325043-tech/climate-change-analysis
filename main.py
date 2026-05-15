import streamlit as st
import time
import random

# --- SETTINGS ---
st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide", initial_sidebar_state="collapsed")

# --- CSS WITH LED MARQUEE EFFECT ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');

    .stApp {
        background: radial-gradient(circle at center, #050a15 0%, #000 100%);
        color: #00f2ff;
        font-family: 'Share Tech Mono', monospace;
    }

    /* THE LED MARQUEE HEADER */
    .led-header {
        height: 60px;
        background: #000;
        margin: 10px;
        border: 2px solid #333;
        border-radius: 5px;
        position: relative;
        overflow: hidden; /* Quan trọng để chữ không tràn ra ngoài */
        display: flex;
        align-items: center;
        box-shadow: inset 0 0 10px #ff005533;
    }

    .led-text {
        white-space: nowrap;
        position: absolute;
        font-family: 'Orbitron', sans-serif;
        color: #ff0055;
        font-size: 1.5rem;
        font-weight: 900;
        text-shadow: 0 0 10px #ff0055, 0 0 20px #ff0055;
        /* Hiệu ứng chạy chữ */
        animation: marquee 10s linear infinite;
        padding-left: 100%; /* Bắt đầu từ ngoài cùng bên phải */
    }

    @keyframes marquee {
        0% { transform: translateX(0); }
        100% { transform: translateX(-100%); }
    }

    /* ARCADE MACHINE BODY */
    .arcade-machine {
        width: 100%; max-width: 550px; height: 780px;
        background: #1a1a1a;
        border: 10px solid #333;
        border-top: 15px solid #444;
        border-radius: 20px;
        position: relative;
        margin: 0 auto;
        transition: all 1s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 0 80px rgba(0,0,0,1);
    }

    .glass-chamber {
        position: absolute; top: 100px; left: 30px; right: 30px; bottom: 180px;
        background: rgba(0, 242, 255, 0.02);
        border: 2px solid rgba(255,255,255,0.05);
        box-shadow: inset 0 0 60px rgba(0,0,0,0.9);
        overflow: hidden;
    }

    .claw-rod {
        position: absolute; top: 0; left: 50%;
        width: 6px; background: #444;
        transform: translateX(-50%);
        transition: height 1.5s ease-in-out;
        z-index: 10;
    }
    .claw-head { position: absolute; bottom: -35px; left: -22px; font-size: 45px; }

    /* CONSOLE & BUTTONS */
    .console-shelf {
        position: absolute; bottom: 0; left: 0; right: 0;
        height: 180px; background: #222;
        border-top: 5px solid #444;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
    }

    /* Layout States */
    .move-aside { transform: translateX(-35%) scale(0.9); opacity: 0.5; }

    .result-hologram {
        text-align: center;
        animation: fadeIn 1s ease-out;
    }
    @keyframes fadeIn { from {opacity: 0;} to {opacity: 1;} }

    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- APP LOGIC ---
if 'view' not in st.session_state: st.session_state.view = 'landing'
if 'vault' not in st.session_state:
    st.session_state.vault = ["ASIA", "EUROPE", "NORTH AMERICA", "SOUTH AMERICA", "AFRICA", "OCEANIA"]
if 'selected' not in st.session_state: st.session_state.selected = None
if 'grabbing' not in st.session_state: st.session_state.grabbing = False

# --- LANDING PAGE ---
if st.session_state.view == 'landing':
    st.markdown("<br><br><br><h1 style='text-align:center; font-family:Orbitron; font-size:4rem;'>CLIMATE VAULT</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; letter-spacing:5px;'>INITIALIZING CODETOOPIA ARCHIVE...</p>", unsafe_allow_html=True)
    _, c_btn, _ = st.columns([2, 1, 2])
    with c_btn:
        if st.button("ENTER THE VAULT", use_container_width=True):
            st.session_state.view = 'machine'
            st.rerun()

# --- MACHINE PAGE ---
elif st.session_state.view == 'machine':
    has_item = st.session_state.selected is not None
    shift = "move-aside" if has_item else ""
    rod_h = "420px" if st.session_state.grabbing else "80px"

    col_m, col_r = st.columns([1.3, 1] if has_item else [1, 0.01])

    with col_m:
        # THE MACHINE HTML
        st.markdown(f"""
            <div class="arcade-machine {shift}">
                <div class="led-header">
                    <div class="led-text">
                        CODETOOPIA VAULT - ACCESSING DATA CORE - PLANET EARTH ARCHIVE - CODETOOPIA VAULT
                    </div>
                </div>
                
                <div class="glass-chamber">
                    <div class="claw-rod" style="height: {rod_h};">
                        <div class="claw-head">🏗️</div>
                    </div>
                    <div style="position:absolute; bottom:20px; width:100%; text-align:center; gap:10px; display:flex; justify-content:center;">
                        {" ".join(["<span style='font-size:30px;'>💎</span>" for _ in range(len(st.session_state.vault))])}
                    </div>
                </div>
                
                <div class="console-shelf">
                    <div style="width:50px; height:50px; background:radial-gradient(#ff0055, #88002b); border-radius:50%; box-shadow: 0 0 20px #ff0055;"></div>
                    <p style="margin-top:10px; color:#444; font-size:0.8rem;">[ PULL TO EXTRACT ]</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

        if not has_item and len(st.session_state.vault) > 0:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("ACTIVATE CLAW", use_container_width=True):
                st.session_state.grabbing = True
                st.rerun()
            
            if st.session_state.grabbing:
                time.sleep(1.5)
                st.session_state.selected = st.session_state.vault.pop(random.randrange(len(st.session_state.vault)))
                st.session_state.grabbing = False
                st.rerun()

    with col_r:
        if has_item:
            st.markdown(f"""
                <div class="result-hologram">
                    <h1 style="font-family:Orbitron; font-size:4rem; color:white; margin:0;">{st.session_state.selected}</h1>
                    <p style="color:#ff0055; letter-spacing:10px;">SECTOR LOADED</p>
                    <div style="width:100%; height:300px; background:#111; border:1px solid #00f2ff; margin:20px 0; display:flex; align-items:center; justify-content:center;">
                        <span style="color:#333;">[ IMAGE PLACEHOLDER ]</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("ANALYZE SECTOR"):
                st.session_state.view = 'lab'
                st.rerun()

# --- LAB PAGE ---
elif st.session_state.view == 'lab':
    st.markdown(f"<h1 style='text-align:center; font-family:Orbitron;'>LAB: {st.session_state.selected}</h1>", unsafe_allow_html=True)
    st.line_chart([random.random() for _ in range(50)])
    if st.button("RETURN TO VAULT"):
        st.session_state.selected = None
        st.session_state.view = 'machine'
        st.rerun()