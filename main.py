import streamlit as st
import time
import random

# --- CORE CONFIGURATION ---
st.set_page_config(page_title="CODETOOPIA | CHRONOS", layout="wide", initial_sidebar_state="collapsed")

# --- ULTIMATE CINEMATIC CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;700&display=swap');

    /* Background for Landing Page */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    url('https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=2074');
        background-size: cover;
        color: #00f2ff;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Claw Machine Physical Structure */
    .machine-shell {
        width: 100%;
        max-width: 550px;
        height: 650px;
        background: #111;
        border: 8px solid #222;
        border-top: 15px solid #ff0055;
        border-radius: 20px 20px 0 0;
        position: relative;
        box-shadow: 0 0 60px rgba(0,0,0,1);
        margin: 0 auto;
        transition: all 1s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }

    .glass-chamber {
        position: absolute;
        top: 20px; left: 20px; right: 20px; bottom: 120px;
        background: rgba(0, 242, 255, 0.03);
        border: 1px solid rgba(255,255,255,0.1);
        overflow: hidden;
    }

    /* The Mechanical Claw */
    .claw-arm {
        position: absolute;
        top: 0; left: 50%;
        width: 6px; height: 80px;
        background: #555;
        transform: translateX(-50%);
        z-index: 5;
        transition: height 1s ease-in-out;
    }
    
    .claw-head {
        position: absolute;
        bottom: -30px; left: -22px;
        font-size: 45px;
        filter: drop-shadow(0 0 10px #ff0055);
    }

    /* Result Animation */
    .reveal-card {
        text-align: center;
        animation: energy-pulse 1.5s infinite alternate, slideLeft 0.8s ease-out;
    }
    @keyframes energy-pulse {
        from { filter: drop-shadow(0 0 10px #00f2ff); }
        to { filter: drop-shadow(0 0 30px #ff0055); }
    }
    @keyframes slideLeft {
        from { opacity: 0; transform: translateX(50px); }
        to { opacity: 1; transform: translateX(0); }
    }

    .machine-left { transform: translateX(-20%) scale(0.9); opacity: 0.7; }
    
    /* Layout Refinements */
    .stButton>button {
        background: #ff0055 !important;
        color: white !important;
        border: none !important;
        font-family: 'Orbitron' !important;
        letter-spacing: 2px !important;
    }

    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- SYSTEM INITIALIZATION ---
if 'nav' not in st.session_state: st.session_state.nav = 'gate'
if 'continents' not in st.session_state:
    st.session_state.continents = [
        {"name": "NORTH AMERICA", "img": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=600"},
        {"name": "EUROPE", "img": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=600"},
        {"name": "ASIA", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=600"},
        {"name": "SOUTH AMERICA", "img": "https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?w=600"},
        {"name": "AFRICA", "img": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=600"},
        {"name": "OCEANIA", "img": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?w=600"}
    ]
if 'grabbed' not in st.session_state: st.session_state.grabbed = None
if 'animating' not in st.session_state: st.session_state.animating = False

# --- PAGE 1: THE MISSION ---
if st.session_state.nav == 'gate':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-family:Orbitron; color:#ff0055; letter-spacing:8px;'>CODETOOPIA_INITIATIVE</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-family:Orbitron; font-size:5rem; margin:0;'>THERMO CHRONOS</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align:center; max-width:800px; margin: 0 auto; color:#888; font-size:1.2rem; line-height:1.6;'>
            The Earth is talking, but are we listening? <br>
            Behind every degree of warming lies a story of a changing world. 
            Extract the data crystals from the temporal vault to witness 250 years of climate shift.
        </div>
    """, unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([2, 1, 2])
    with col_btn:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("OPEN THE VAULT", use_container_width=True):
            st.session_state.nav = 'claw'
            st.rerun()

# --- PAGE 2: THE CLAW MACHINE ---
elif st.session_state.nav == 'claw':
    machine_pos = "machine-left" if st.session_state.grabbed else ""
    arm_height = "350px" if st.session_state.animating else "80px"
    
    col_machine, col_result = st.columns([1.2, 1] if st.session_state.grabbed else [1, 0.01])

    with col_machine:
        st.markdown(f"""
            <div class="machine-shell {machine_pos}">
                <div class="glass-chamber">
                    <div class="claw-arm" style="height: {arm_height};">
                        <div class="claw-head">🏗️</div>
                    </div>
                    <div style="position:absolute; bottom:20px; width:100%; display:flex; justify-content:center; gap:10px;">
                        {" ".join(["<span style='font-size:30px;'>💎</span>" for _ in range(len(st.session_state.continents))])}
                    </div>
                </div>
                <div style="position:absolute; bottom:40px; width:100%; text-align:center; font-family:Orbitron; color:#444;">
                    CRYSTALS REMAINING: {len(st.session_state.continents)}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.grabbed and len(st.session_state.continents) > 0:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("RELEASE THE CLAW 🕹️", use_container_width=True):
                st.session_state.animating = True
                st.rerun()
            
            if st.session_state.animating:
                time.sleep(1.5) # The drop
                st.session_state.grabbed = st.session_state.continents.pop(random.randrange(len(st.session_state.continents)))
                st.session_state.animating = False
                st.rerun()

    with col_result:
        if st.session_state.grabbed:
            target = st.session_state.grabbed
            st.markdown(f"""
                <div class="reveal-card">
                    <h1 style="font-family:Orbitron; font-size:3.5rem; margin:0;">{target['name']}</h1>
                    <p style="color:#ff0055; letter-spacing:5px;">DATA CRYSTAL DECODED</p>
                    <img src="{target['img']}" style="width:100%; border:2px solid #00f2ff; border-radius:20px; box-shadow: 0 0 30px rgba(0,242,255,0.4);">
                </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("ENTER RESEARCH LAB"):
                st.session_state.nav = 'lab'
                st.rerun()

# --- PAGE 3: THE LAB ---
elif st.session_state.nav == 'lab':
    st.markdown(f"<h1 style='text-align:center; font-family:Orbitron;'>LAB: {st.session_state.grabbed['name']}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>Analyzing 250 years of temperature anomalies...</p>", unsafe_allow_html=True)
    
    st.line_chart([random.random() for _ in range(40)])
    
    if st.button("BACK TO VAULT"):
        st.session_state.grabbed = None
        st.session_state.nav = 'claw'
        st.rerun()