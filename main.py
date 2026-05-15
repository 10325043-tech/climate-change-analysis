import streamlit as st
import time
import random

# --- SYSTEM SETTINGS ---
st.set_page_config(page_title="CHRONOS_EXTRACTOR_v2", layout="wide", initial_sidebar_state="collapsed")

# --- ADVANCED CINEMATIC CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;700&display=swap');

    .stApp {
        background: radial-gradient(circle at center, #050a15 0%, #000 100%);
        color: #00f2ff;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Claw Machine Container Transitions */
    .machine-container {
        transition: all 1.2s cubic-bezier(0.4, 0, 0.2, 1);
        text-align: center;
    }
    .pos-center { margin: 0 auto; width: 600px; }
    .pos-left { transform: translateX(-35%); width: 450px; opacity: 0.6; }

    .claw-box {
        border: 3px solid #1e3a8a;
        background: rgba(10, 20, 40, 0.8);
        border-radius: 25px;
        padding: 50px;
        position: relative;
        box-shadow: 0 0 40px rgba(0, 242, 255, 0.15);
    }

    /* Shaking animation for items inside during grab */
    @keyframes item-shake {
        0% { transform: translate(2px, 1px); }
        25% { transform: translate(-2px, -1px); }
        50% { transform: translate(1px, 2px); }
        75% { transform: translate(-1px, -2px); }
        100% { transform: translate(0, 0); }
    }
    .shaking { animation: item-shake 0.1s infinite; }

    /* Result Animation */
    .reveal-zone {
        animation: fadeInScale 1s ease-out forwards;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    @keyframes fadeInScale {
        0% { opacity: 0; transform: scale(0.7) translateY(20px); }
        100% { opacity: 1; transform: scale(1) translateY(0); }
    }

    .glow-title {
        font-family: 'Orbitron', sans-serif;
        text-shadow: 0 0 15px #00f2ff, 0 0 30px #ff0055;
        font-size: 3.5rem;
        margin: 0;
        letter-spacing: 5px;
    }

    .result-image {
        width: 100%;
        max-width: 550px;
        border: 2px solid #00f2ff;
        border-radius: 15px;
        margin-top: 20px;
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.3);
    }

    /* Custom Streamlit Button */
    .stButton>button {
        background: transparent !important;
        color: #ff0055 !important;
        border: 2px solid #ff0055 !important;
        border-radius: 0px !important;
        font-family: 'Orbitron', sans-serif !important;
        padding: 15px 30px !important;
        transition: 0.4s !important;
    }
    .stButton>button:hover {
        background: #ff0055 !important;
        color: white !important;
        box-shadow: 0 0 25px #ff0055 !important;
    }

    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZE DATA ---
if 'nav' not in st.session_state: st.session_state.nav = 'gate'
if 'remaining_sectors' not in st.session_state:
    st.session_state.remaining_sectors = [
        {"name": "NORTH AMERICA", "img": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?q=80&w=1000"},
        {"name": "EUROPE", "img": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?q=80&w=1000"},
        {"name": "ASIA", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=1000"},
        {"name": "SOUTH AMERICA", "img": "https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?q=80&w=1000"},
        {"name": "AFRICA", "img": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?q=80&w=1000"},
        {"name": "OCEANIA", "img": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?q=80&w=1000"}
    ]
if 'is_grabbing' not in st.session_state: st.session_state.is_grabbing = False
if 'current_target' not in st.session_state: st.session_state.current_target = None

# --- PAGE 1: THE MISSION BRIEF ---
if st.session_state.nav == 'gate':
    st.markdown("<br><br><br><h1 style='text-align:center; font-family:Orbitron; font-size:4rem;'>THERMO CHRONOS</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align:center; max-width:800px; margin: 0 auto; color:#888; font-size:1.3rem;'>
            <p>> SYSTEM STATUS: ARMED<br>
            > MISSION: Extract 6 critical climate data crystals from the temporal void.<br>
            > WARNING: Once a sector is extracted, it cannot be returned to the machine.</p>
        </div>
    """, unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1.5, 1, 1.5])
    with col_btn:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("INITIALIZE UNIT", use_container_width=True):
            st.session_state.nav = 'claw_room'
            st.rerun()

# --- PAGE 2: THE CLAW EXTRACTION ---
elif st.session_state.nav == 'claw_room':
    # Styling logic for machine movement
    machine_layout = "pos-left" if st.session_state.current_target else "pos-center"
    shake_effect = "shaking" if st.session_state.is_grabbing else ""
    
    col_machine, col_data = st.columns([1, 1] if st.session_state.current_target else [1, 0.01])

    with col_machine:
        st.markdown(f"""
            <div class="machine-container {machine_layout}">
                <div class="claw-box {shake_effect}">
                    <h3 style="font-family:Orbitron; color:#ff0055; margin-bottom:30px;">CLAW EXTRACTOR v2.0</h3>
                    <div style="font-size: 5rem; margin-bottom:20px;">🏗️</div>
                    <div style="display:flex; justify-content:center; gap:15px; font-size:2rem;">
                        {" ".join(["💎" for _ in range(len(st.session_state.remaining_sectors))])}
                    </div>
                    <p style="margin-top:30px; letter-spacing:3px; color:#555;">[ AVAILABLE CORES: {len(st.session_state.remaining_sectors)} ]</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Grab Button Logic
        if not st.session_state.current_target and len(st.session_state.remaining_sectors) > 0:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("EXECUTE EXTRACTION 🕹️", use_container_width=True):
                st.session_state.is_grabbing = True
                st.rerun()
            
            if st.session_state.is_grabbing:
                # Fake grabbing delay for immersion
                progress_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.02)
                    progress_bar.progress(percent_complete + 1)
                
                # Logic: Reduce from 6 -> 5 -> 4...
                selected_idx = random.randrange(len(st.session_state.remaining_sectors))
                st.session_state.current_target = st.session_state.remaining_sectors.pop(selected_idx)
                st.session_state.is_grabbing = False
                st.rerun()
        
        elif len(st.session_state.remaining_sectors) == 0 and not st.session_state.current_target:
            st.error("ALL DATA CORES EXTRACTED.")
            if st.button("RESET SYSTEM"):
                st.session_state.clear()
                st.rerun()

    with col_data:
        if st.session_state.current_target:
            target = st.session_state.current_target
            st.markdown(f"""
                <div class="reveal-zone">
                    <p style="color:#ff0055; font-weight:bold; letter-spacing:5px;">EXTRACTION SUCCESSFUL</p>
                    <h1 class="glow-title">{target['name']}</h1>
                    <img src="{target['img']}" class="result-image">
                </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("PROCEED TO DATA ANALYSIS"):
                st.session_state.nav = 'dashboard'
                st.rerun()

# --- PAGE 3: DATA DASHBOARD ---
elif st.session_state.nav == 'dashboard':
    st.markdown(f"<h1 style='font-family:Orbitron; text-align:center;'>ANALYZING: {st.session_state.current_target['name']}</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Placeholder for future climate data
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Temperature Drift", value="+1.28°C", delta="High Anomaly")
    with col2:
        st.metric(label="CO2 Concentration", value="419.7 PPM", delta="Critical")
        
    st.area_chart([random.random() for _ in range(50)])
    
    if st.button("RETURN TO EXTRACTOR"):
        st.session_state.current_target = None # Remove result so machine returns to center
        st.session_state.nav = 'claw_room'
        st.rerun()