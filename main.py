import streamlit as st
import random
import time

# --- SYSTEM SETTINGS ---
st.set_page_config(page_title="CHRONOS_CLAW_OS", layout="wide", initial_sidebar_state="collapsed")

# --- ADVANCED CYBER-GAMING CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');

    .stApp {
        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 
                    url('https://images.unsplash.com/photo-1614730321146-b6fa6a46bcb4?q=80&w=2074');
        background-size: cover;
        color: #00f2ff;
        font-family: 'Share Tech Mono', monospace;
    }

    /* Claw Machine Styling */
    .claw-machine {
        background: rgba(20, 20, 20, 0.9);
        border: 4px solid #333;
        border-top: 10px solid #ff0055;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.2);
        min-height: 400px;
        position: relative;
    }

    /* The "Transformed" Result Card */
    .result-card {
        background: rgba(0, 242, 255, 0.1);
        border: 2px solid #00f2ff;
        border-radius: 15px;
        padding: 20px;
        animation: glow-pulse 2s infinite alternate, slideIn 0.5s ease-out;
        text-align: center;
    }

    @keyframes glow-pulse {
        from { box-shadow: 0 0 10px #00f2ff; border-color: #00f2ff; }
        to { box-shadow: 0 0 30px #ff0055; border-color: #ff0055; }
    }

    @keyframes slideIn {
        from { transform: translateX(50px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    .transformed-img {
        width: 100%;
        border-radius: 10px;
        margin-bottom: 15px;
        filter: drop-shadow(0 0 10px #00f2ff);
    }

    .status-terminal {
        background: black;
        color: #0f0;
        padding: 10px;
        font-size: 0.8rem;
        border-radius: 5px;
        margin-top: 10px;
        height: 100px;
        overflow-y: hidden;
    }

    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- DATA INITIALIZATION ---
if 'page' not in st.session_state:
    st.session_state.page = 'gate'
if 'remaining_sectors' not in st.session_state:
    st.session_state.remaining_sectors = [
        {"name": "NORTH AMERICA", "id": "S-01", "img": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?q=80&w=600"},
        {"name": "EUROPE", "id": "S-02", "img": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?q=80&w=600"},
        {"name": "ASIA", "id": "S-03", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=600"},
        {"name": "SOUTH AMERICA", "id": "S-04", "img": "https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?q=80&w=600"},
        {"name": "AFRICA", "id": "S-05", "img": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?q=80&w=600"},
        {"name": "OCEANIA", "id": "S-06", "img": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?q=80&w=600"}
    ]
if 'current_grab' not in st.session_state:
    st.session_state.current_grab = None

# --- PAGE 1: THE GATEWAY ---
if st.session_state.page == 'gate':
    st.markdown("<br><br><br><h1 style='text-align:center; font-family:Orbitron; font-size:4rem;'>CHRONOS_OS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#ff0055; letter-spacing:10px;'>TEMPORAL CLAW UNIT READY</p>", unsafe_allow_html=True)
    
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("INITIALIZE MISSION", use_container_width=True):
            st.session_state.page = 'claw'
            st.rerun()

# --- PAGE 2: THE CLAW MACHINE ---
elif st.session_state.page == 'claw':
    st.markdown("<h2 style='text-align:center; font-family:Orbitron;'>SECTOR RETRIEVAL UNIT</h2>", unsafe_allow_html=True)
    
    col_machine, col_result = st.columns([1.5, 1])
    
    with col_machine:
        st.markdown("""
            <div class="claw-machine">
                <h3 style="color:#ff0055;">CLAW_EXTRACTOR_v2</h3>
                <div style="font-size: 5rem;">🏗️</div>
                <p style="color:#555;">[ DATA PACKETS REMAINING: """ + str(len(st.session_state.remaining_sectors)) + """ ]</p>
            </div>
        """, unsafe_allow_html=True)
        
        if len(st.session_state.remaining_sectors) > 0:
            if st.button("EXECUTE GRAB 🕹️", use_container_width=True):
                # Logic: Grab a random one, then remove it so no duplicates
                with st.spinner("EXTRACTING SECTOR DATA..."):
                    time.sleep(1.5) # Fake animation time
                    selected_index = random.randrange(len(st.session_state.remaining_sectors))
                    st.session_state.current_grab = st.session_state.remaining_sectors.pop(selected_index)
                    st.rerun()
        else:
            st.warning("ALL SECTORS EXTRACTED. REBOOT SYSTEM TO RESET.")

    with col_result:
        if st.session_state.current_grab:
            s = st.session_state.current_grab
            st.markdown(f"""
                <div class="result-card">
                    <p style="color:#ff0055; font-weight:bold; letter-spacing:3px;">SYSTEM TRANSFORMED</p>
                    <img src="{s['img']}" class="transformed-img">
                    <h2 style="font-family:Orbitron; color:white; margin:0;">{s['name']}</h2>
                    <p style="color:#00f2ff; margin-top:10px;">SECTOR {s['id']} LOADED</p>
                    <button style="width:100%; background:#00f2ff; color:black; border:none; padding:10px; font-weight:bold; cursor:pointer; margin-top:10px;">PROCEED TO LAB</button>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="border:1px dashed #333; height:400px; display:flex; align-items:center; justify-content:center; color:#333;">
                    WAITING FOR EXTRACTION...
                </div>
            """, unsafe_allow_html=True)

    # Status Terminal below
    st.markdown("""
        <div class="status-terminal">
            > Initializing Claw Logic... OK<br>
            > Checking for Duplicate Prevention... ACTIVE<br>
            > Awaiting User Command...
        </div>
    """, unsafe_allow_html=True)

    if st.button("ABORT MISSION"):
        st.session_state.page = 'gate'
        st.session_state.remaining_sectors = [] # Reset logic
        st.rerun()