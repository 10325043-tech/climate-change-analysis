import streamlit as st
import time
import random

# --- CORE CONFIG ---
st.set_page_config(page_title="CODETOOPIA | CHRONOS", layout="wide", initial_sidebar_state="collapsed")

# --- HIGH-FIDELITY CSS ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;700&display=swap');

    /* Global Atmosphere */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072');
        background-size: cover;
        color: #00f2ff;
        font-family: 'Rajdhani', sans-serif;
    }

    /* Landing Page Branding */
    .group-tag {
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 10px;
        color: #ff0055;
        font-size: 1.2rem;
        text-shadow: 0 0 10px #ff0055;
    }

    /* REAL CLAW MACHINE UI */
    .arcade-cabinet {
        width: 100%;
        max-width: 500px;
        height: 600px;
        background: linear-gradient(180deg, #111 0%, #222 100%);
        border: 10px solid #333;
        border-radius: 20px;
        position: relative;
        box-shadow: 0 0 50px rgba(0,0,0,1), inset 0 0 20px rgba(0,242,255,0.2);
        overflow: hidden;
        margin: 0 auto;
        transition: all 1s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .glass-front {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 100px;
        background: rgba(255,255,255,0.05);
        border-bottom: 5px solid #444;
        z-index: 2;
    }

    .claw-mechanism {
        position: absolute;
        top: 0; left: 50%;
        width: 4px; height: 150px;
        background: #888;
        transform: translateX(-50%);
        z-index: 3;
    }
    
    .claw-head {
        position: absolute;
        bottom: -20px; left: -18px;
        font-size: 40px;
        transition: 0.3s;
    }

    .item-pit {
        position: absolute;
        bottom: 120px;
        width: 100%;
        display: flex;
        justify-content: center;
        gap: 15px;
        flex-wrap: wrap;
        padding: 20px;
    }

    /* Animation States */
    .pos-left { transform: translateX(-25%); opacity: 0.8; }
    
    @keyframes claw-drop {
        0% { height: 150px; }
        50% { height: 400px; }
        100% { height: 150px; }
    }
    .active-claw { animation: claw-drop 2s ease-in-out; }

    @keyframes shake {
        0%, 100% { transform: translate(0,0); }
        25% { transform: translate(5px, 5px); }
        50% { transform: translate(-5px, 0); }
    }
    .vibrate { animation: shake 0.1s infinite; }

    /* Result Card */
    .continent-card {
        background: rgba(0, 242, 255, 0.05);
        border: 1px solid #00f2ff;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        animation: slideInRight 0.8s ease-out;
    }

    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(100px); }
        to { opacity: 1; transform: translateX(0); }
    }

    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'page' not in st.session_state: st.session_state.page = 'start'
if 'vault' not in st.session_state:
    st.session_state.vault = [
        {"name": "NORTH AMERICA", "url": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?q=80&w=600"},
        {"name": "EUROPE", "url": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?q=80&w=600"},
        {"name": "ASIA", "url": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=600"},
        {"name": "SOUTH AMERICA", "url": "https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?q=80&w=600"},
        {"name": "AFRICA", "url": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?q=80&w=600"},
        {"name": "OCEANIA", "url": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?q=80&w=600"}
    ]
if 'extracted' not in st.session_state: st.session_state.extracted = None
if 'busy' not in st.session_state: st.session_state.busy = False

# --- LANDING PAGE ---
if st.session_state.page == 'start':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<p class='group-tag' style='text-align:center;'>CODETOOPIA PRESENTS</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; font-family:Orbitron; font-size:5rem; font-weight:900;'>THERMO CHRONOS</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align:center; max-width:700px; margin: 0 auto; color:#ccc; line-height:1.6;'>
            Tracing the invisible scars of our planet. As the ice retreats and the mercury rises, 
            we reach back through the archives of time. Explore the thermal legacy of 6 continents.
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([2, 1, 2])
    with col_btn:
        if st.button("ENTER THE ARCHIVE", use_container_width=True):
            st.session_state.page = 'claw'
            st.rerun()

# --- CLAW MACHINE PAGE ---
elif st.session_state.page == 'claw':
    # Layout Logic
    machine_style = "pos-left" if st.session_state.extracted else ""
    claw_anim = "active-claw" if st.session_state.busy else ""
    shake_anim = "vibrate" if st.session_state.busy else ""
    
    col_machine, col_display = st.columns([1.2, 1] if st.session_state.extracted else [1, 0.01])

    with col_machine:
        # The Machine HTML Structure
        st.markdown(f"""
            <div class="arcade-cabinet {machine_style}">
                <div class="glass-front"></div>
                <div class="claw-mechanism {claw_anim}">
                    <div class="claw-head">🏗️</div>
                </div>
                <div class="item-pit {shake_anim}">
                    {" ".join(["<span style='font-size:35px;'>💎</span>" for _ in range(len(st.session_state.vault))])}
                </div>
                <div style="position:absolute; bottom:20px; width:100%; text-align:center; color:#555; font-family:Orbitron;">
                    DATA PACKETS: {len(st.session_state.vault)}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.extracted and len(st.session_state.vault) > 0:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("EXECUTE GRAB", use_container_width=True):
                st.session_state.busy = True
                st.rerun()
            
            if st.session_state.busy:
                time.sleep(2) # Mechanical delay
                st.session_state.extracted = st.session_state.vault.pop(random.randrange(len(st.session_state.vault)))
                st.session_state.busy = False
                st.rerun()

    with col_display:
        if st.session_state.extracted:
            data = st.session_state.extracted
            st.markdown(f"""
                <div class="continent-card">
                    <p style="color:#ff0055; font-weight:bold;">SIGNAL ACQUIRED</p>
                    <h1 style="font-family:Orbitron; margin-bottom:20px;">{data['name']}</h1>
                    <img src="{data['url']}" style="width:100%; border-radius:10px; margin-bottom:20px;">
                </div>
            """, unsafe_allow_html=True)
            if st.button("ACCESS LAB TERMINAL", use_container_width=True):
                st.session_state.page = 'lab'
                st.rerun()

# --- LAB PAGE (Simplified Preview) ---
elif st.session_state.page == 'lab':
    st.markdown(f"<h1 style='font-family:Orbitron;'>LAB: {st.session_state.extracted['name']}</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("Decoding thermal anomalies from 1850-2024...")
    st.line_chart([random.uniform(14, 16) for _ in range(50)])
    
    if st.button("RETURN TO EXTRACTOR"):
        st.session_state.extracted = None
        st.session_state.page = 'claw'
        st.rerun()