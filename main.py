import streamlit as st
import time
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide", initial_sidebar_state="collapsed")

# --- ULTIMATE ARCADE CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');

    .stApp {
        background: radial-gradient(circle at center, #050a15 0%, #000 100%);
        color: #00f2ff;
        font-family: 'Share Tech Mono', monospace;
    }

    /* THE LED MARQUEE STRIP */
    .led-marquee-container {
        height: 50px;
        background: #000;
        border: 2px solid #333;
        overflow: hidden;
        position: relative;
        display: flex;
        align-items: center;
        margin: 10px 20px;
        box-shadow: inset 0 0 15px #ff0055;
    }

    .led-text {
        white-space: nowrap;
        position: absolute;
        font-family: 'Orbitron', sans-serif;
        color: #ff0055;
        font-size: 1.4rem;
        font-weight: 900;
        text-shadow: 0 0 10px #ff0055;
        animation: marquee 12s linear infinite;
    }

    @keyframes marquee {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }

    /* THE MACHINE CABINET */
    .machine-frame {
        width: 100%; max-width: 500px; height: 700px;
        background: #1a1a1a;
        border: 8px solid #222;
        border-radius: 15px;
        position: relative;
        margin: 0 auto;
        transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 0 50px rgba(0,0,0,1);
    }

    .glass-chamber {
        position: absolute; top: 80px; left: 20px; right: 20px; bottom: 150px;
        background: rgba(0, 242, 255, 0.03);
        border: 1px solid rgba(255,255,255,0.1);
        overflow: hidden;
    }

    /* MECHANICAL CLAW */
    .claw-string {
        position: absolute; top: 0; left: 50%;
        width: 4px; background: #444;
        transform: translateX(-50%);
        z-index: 10;
    }

    .claw-head { position: absolute; bottom: -30px; left: -22px; font-size: 40px; }

    /* LAYOUT POSITIONING */
    .center-pos { transform: translateX(0); }
    .left-pos { transform: translateX(-30%) scale(0.9); opacity: 0.7; }

    /* PRIZE DISPLAY */
    .prize-card {
        text-align: center;
        animation: zoomIn 0.5s ease-out;
        border: 1px solid #00f2ff;
        padding: 20px;
        background: rgba(0, 242, 255, 0.05);
        border-radius: 15px;
    }

    @keyframes zoomIn { from { opacity: 0; transform: scale(0.8); } to { opacity: 1; transform: scale(1); } }

    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- SESSION LOGIC ---
if 'page' not in st.session_state: st.session_state.page = 'gate'
if 'inventory' not in st.session_state:
    st.session_state.inventory = [
        {"name": "ASIA", "src": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=800"},
        {"name": "EUROPE", "src": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=800"},
        {"name": "NORTH AMERICA", "src": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800"},
        {"name": "SOUTH AMERICA", "src": "https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?w=800"},
        {"name": "AFRICA", "src": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=800"},
        {"name": "OCEANIA", "src": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?w=800"}
    ]
if 'won_item' not in st.session_state: st.session_state.won_item = None
if 'claw_active' not in st.session_state: st.session_state.claw_active = False

# --- PAGE 1: GATEWAY ---
if st.session_state.page == 'gate':
    st.markdown("<br><br><br><h1 style='text-align:center; font-family:Orbitron; font-size:4rem;'>CLIMATE VAULT</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ff0055;'>CODETOOPIA PROJECT ALPHA</p>", unsafe_allow_html=True)
    _, col_b, _ = st.columns([2, 1, 2])
    with col_b:
        if st.button("CONNECT TO VAULT", use_container_width=True):
            st.session_state.page = 'vault'
            st.rerun()

# --- PAGE 2: THE MACHINE ---
elif st.session_state.page == 'vault':
    is_shifted = "left-pos" if st.session_state.won_item else "center-pos"
    claw_height = "380px" if st.session_state.claw_active else "60px"
    
    col_mach, col_info = st.columns([1.2, 1] if st.session_state.won_item else [1, 0.01])

    with col_mach:
        st.markdown(f"""
            <div class="machine-frame {is_shifted}">
                <div class="led-marquee-container">
                    <div class="led-text">CODETOOPIA VAULT - EXTRACTING CLIMATE CORE - SECTOR STATUS: ACTIVE</div>
                </div>
                <div class="glass-chamber">
                    <div class="claw-string" style="height: {claw_height};">
                        <div class="claw-head">🏗️</div>
                    </div>
                    <div style="position:absolute; bottom:20px; width:100%; display:flex; justify-content:center; gap:10px;">
                        {" ".join(["<span style='font-size:30px;'>💎</span>" for _ in range(len(st.session_state.inventory))])}
                    </div>
                </div>
                <div style="position:absolute; bottom:40px; width:100%; text-align:center; color:#444;">
                    [ {len(st.session_state.inventory)} CORES REMAINING ]
                </div>
            </div>
        """, unsafe_allow_html=True)

        if not st.session_state.won_item and len(st.session_state.inventory) > 0:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("ACTIVATE CLAW", use_container_width=True):
                st.session_state.claw_active = True
                st.rerun()
            
            if st.session_state.claw_active:
                time.sleep(1) # Drop time
                st.session_state.won_item = st.session_state.inventory.pop(random.randrange(len(st.session_state.inventory)))
                st.session_state.claw_active = False
                st.rerun()

    with col_info:
        if st.session_state.won_item:
            item = st.session_state.won_item
            st.markdown(f"""
                <div class="prize-card">
                    <h2 style="font-family:Orbitron; margin:0;">{item['name']}</h2>
                    <p style="color:#ff0055; font-size:0.8rem;">CORE EXTRACTION SUCCESSFUL</p>
                    <img src="{item['src']}" style="width:100%; border-radius:10px; margin:15px 0;">
                </div>
            """, unsafe_allow_html=True)
            if st.button("DECODE DATA"):
                st.session_state.page = 'lab'
                st.rerun()

# --- PAGE 3: RESEARCH LAB ---
elif st.session_state.page == 'lab':
    st.markdown(f"<h1 style='font-family:Orbitron; text-align:center;'>LAB: {st.session_state.won_item['name']}</h1>", unsafe_allow_html=True)
    st.line_chart([random.random() for _ in range(40)])
    if st.button("RETURN TO VAULT"):
        st.session_state.won_item = None
        st.session_state.page = 'vault'
        st.rerun()