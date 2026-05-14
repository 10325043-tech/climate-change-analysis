import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

# --- ARCHITECTURAL SETUP ---
st.set_page_config(
    page_title="NEURAL-CHRONOS | SYSTEM_v5.0", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- THE CYBER-CORE ENGINE (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@200;500&display=swap');

    /* Global UI Reset */
    .stApp {
        background: #020205;
        color: #00f2ff;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Ambient HUD Background */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: 
            linear-gradient(rgba(0, 242, 255, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 242, 255, 0.03) 1px, transparent 1px);
        background-size: 30px 30px;
        pointer-events: none;
        z-index: 0;
    }

    /* Tactical Header */
    .tactical-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: 15px;
        text-align: left;
        color: #fff;
        text-shadow: 0 0 20px #00f2ff;
        border-left: 10px solid #ff0055;
        padding-left: 20px;
        margin-bottom: 5px;
    }

    /* Data Tiles (Artifacts) */
    .data-tile {
        background: rgba(0, 242, 255, 0.02);
        border: 1px solid rgba(0, 242, 255, 0.2);
        padding: 15px;
        margin-bottom: 10px;
        border-radius: 2px;
        position: relative;
        overflow: hidden;
    }
    .data-tile::after {
        content: "SCANNING...";
        position: absolute;
        top: 0; right: 5px;
        font-size: 0.5rem;
        color: #ff0055;
    }

    /* Sci-Fi Buttons */
    .stButton>button {
        background: transparent !important;
        color: #00f2ff !important;
        border: 1px solid #00f2ff !important;
        border-radius: 0px !important;
        width: 100% !important;
        font-family: 'Orbitron' !important;
        transition: 0.3s !important;
        letter-spacing: 2px;
    }
    .stButton>button:hover {
        background: #00f2ff !important;
        color: #000 !important;
        box-shadow: 0 0 20px #00f2ff;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 5px; }
    ::-webkit-scrollbar-thumb { background: #ff0055; }
    </style>
""", unsafe_allow_html=True)

# --- SYSTEM STATE ---
if 'uplink' not in st.session_state:
    st.session_state.uplink = False

# --- LOGIC: DATA GENERATOR ---
def get_telemetry():
    years = np.arange(1900, 2026)
    temp = np.linspace(14, 16.5, len(years)) + np.random.normal(0, 0.1, len(years))
    return pd.DataFrame({"Year": years, "Global_Index": temp})

df = get_telemetry()

# --- INTERFACE: THE GATEWAY ---
if not st.session_state.uplink:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown('<div class="tactical-header">CHRONOS_OS</div>', unsafe_allow_html=True)
        st.markdown("<p style='letter-spacing:5px;'>PLANETARY DEFENSE & THERMAL ARCHIVE</p>", unsafe_allow_html=True)
        st.markdown("""
        > **UPLINK STATUS:** OFFLINE  
        > **ENCRYPTION:** NEURAL-SYNC REQUIRED  
        > **MISSION:** RECONSTRUCT HISTORICAL THERMAL DECAY
        """)
        if st.button("ESTABLISH UPLINK"):
            st.session_state.uplink = True
            st.rerun()
    with col2:
        # Animated HUD Graphic (Radar)
        theta = np.linspace(0, 2*np.pi, 100)
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatter(x=np.cos(theta), y=np.sin(theta), mode='lines', line=dict(color='#00f2ff', width=1)))
        fig_radar.update_layout(width=300, height=300, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', showlegend=False, xaxis_visible=False, yaxis_visible=False)
        st.plotly_chart(fig_radar, config={'displayModeBar': False})

# --- INTERFACE: THE TACTICAL DECK ---
else:
    # TOP HUD
    h1, h2, h3 = st.columns([2, 1, 1])
    with h1:
        st.markdown('<div class="tactical-header" style="font-size:1.5rem;">NEURAL-CHRONOS: ACTIVE</div>', unsafe_allow_html=True)
    with h2:
        st.markdown(f"**UPLINK_TIME:** {datetime.now().strftime('%H:%M:%S')}")
    with h3:
        if st.button("TERMINATE"):
            st.session_state.uplink = False
            st.rerun()

    st.markdown("---")

    # MAIN THREE-PANEL LAYOUT
    left_wing, center_core, right_wing = st.columns([1, 2.5, 1])

    with left_wing:
        st.markdown("### [ SYSTEM LOGS ]")
        st.markdown("""
        <div class="data-tile">
            <small>CORE_TEMP</small><br><b style="color:#ff0055;">CRITICAL: +1.2°C</b>
        </div>
        <div class="data-tile">
            <small>SURVIVAL_INDEX</small><br><b>84.2%</b>
        </div>
        <div class="data-tile">
            <small>ATMOS_CARBON</small><br><b>420.1 PPM</b>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("SENSORS: Detected thermal drift in Sector 7-G (Arctic).")
        st.warning("ALERT: Permafrost integrity failing.")

    with center_core:
        # THE QUANTUM GRID (Dynamic Graph)
        st.markdown("### [ TEMPORAL ANALYSIS GRID ]")
        
        # Timeline Manipulator
        target_year = st.select_slider("TEMPORAL_FOCUS", options=df['Year'].tolist(), value=2025)
        
        filtered_df = df[df['Year'] <= target_year]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=filtered_df['Year'], 
            y=filtered_df['Global_Index'],
            mode='lines',
            line=dict(color='#00f2ff', width=3),
            fill='tozeroy',
            fillcolor='rgba(0, 242, 255, 0.1)'
        ))
        
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', title="DECAY_INDEX"),
            margin=dict(l=0, r=0, t=0, b=0),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown(f"""
            <div style="background:rgba(255,0,85,0.1); border: 1px solid #ff0055; padding:20px; text-align:center;">
                <h2 style="margin:0; font-family:Orbitron;">YEAR {target_year} TELEMETRY</h2>
                <small>ANOMALY DETECTED: {0.01 * (target_year-1900):.2f} SIGMA</small>
            </div>
        """, unsafe_allow_html=True)

    with right_wing:
        st.markdown("### [ ARTIFACTS ]")
        
        # Conditional information based on the slider
        if target_year < 1950:
            st.markdown('<div class="data-tile"><b>ARTIFACT: COAL_ERA</b><br>Industrial expansion begins. Smoke obscures the sun.</div>', unsafe_allow_html=True)
        elif target_year < 2000:
            st.markdown('<div class="data-tile"><b>ARTIFACT: PLASTIC_AGE</b><br>Global temperatures break 100-year records.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="data-tile"><b>ARTIFACT: THE_TIPPING_POINT</b><br>Feedback loops active. System destabilization imminent.</div>', unsafe_allow_html=True)
        
        if st.button("SCAN SECTOR 01"): st.toast("Scanning North America...")
        if st.button("SCAN SECTOR 02"): st.toast("Scanning Europe...")
        if st.button("SCAN SECTOR 03"): st.toast("Scanning Asia...")

# --- AMBIENT FOOTER ---
st.markdown("""
    <div style="position:fixed; bottom:0; left:0; width:100%; background:rgba(0,0,0,0.8); font-size:0.6rem; color:#444; padding:5px; text-align:center; z-index:1000;">
        NEURAL-CHRONOS ENGINE v5.0 | ACCESSING NOAA_GISS_ENCRYPTED_DATABASE | LATENCY: 14MS | AUTH: ADMIN_LEGACY
    </div>
""", unsafe_allow_html=True)