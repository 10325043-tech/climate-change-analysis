import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

# --- STAGE 0: ARCHITECTURAL CONFIG ---
st.set_page_config(page_title="THERMO-CHRONOS: THE LAST LEGACY", layout="wide", initial_sidebar_state="collapsed")

# --- STAGE 1: VISUAL SOUL (CSS & ANIMATIONS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');

    /* The Deep Void Background */
    .stApp {
        background-color: #0E1117;
        background-image: radial-gradient(circle at center, #1a1c23 0%, #000000 100%);
        color: #00f2ff;
        font-family: 'Share Tech Mono', monospace;
    }

    /* Glitch Title Effect */
    .glitch {
        font-family: 'Orbitron', sans-serif;
        font-size: 4.5rem;
        font-weight: 900;
        text-align: center;
        text-transform: uppercase;
        color: #fff;
        text-shadow: 2px 0 #ff0055, -2px 0 #00f2ff;
        position: relative;
    }

    /* Crystal Mission Button */
    .stButton>button {
        background: rgba(0, 242, 255, 0.05) !important;
        color: #00f2ff !important;
        border: 2px solid #00f2ff !important;
        font-family: 'Orbitron' !important;
        padding: 20px 60px !important;
        border-radius: 0px !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.2) !important;
        transition: all 0.3s ease !important;
        display: block; margin: auto;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 40px #00f2ff !important;
        background: #00f2ff !important;
        color: #000 !important;
    }

    /* Data Card Artficts */
    .artifact-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(0,242,255,0.2);
        padding: 20px;
        border-radius: 5px;
        transition: 0.3s;
    }
    .artifact-card:hover { border-color: #ff0055; box-shadow: 0 0 20px rgba(255,0,85,0.2); }

    /* HUD Elements */
    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- STAGE 2: DATA CORE ---
@st.cache_data
def load_historical_data():
    # Simulated data reflecting your project needs
    years = np.arange(1850, 2024)
    data = {
        'Year': years,
        'Hanoi_Heat': np.linspace(22, 28, len(years)) + np.random.normal(0, 0.5, len(years)),
        'London_Heat': np.linspace(9, 14, len(years)) + np.random.normal(0, 0.5, len(years))
    }
    return pd.DataFrame(data)

df = load_historical_data()

# --- STAGE 3: STATE MACHINE ---
if 'scene' not in st.session_state: st.session_state.scene = 'gateway'

# --- SCENE 1: THE GATEWAY ---
if st.session_state.scene == 'gateway':
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown('<div class="glitch">THERMO-CHRONOS</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; letter-spacing:10px; color:#555;'>THE LAST LEGACY | v4.0</p>", unsafe_allow_html=True)
    
    # 3D Particle Sphere Simulation (using Plotly for the "millions of points")
    phi = np.random.uniform(0, 2*np.pi, 2000)
    theta = np.random.uniform(0, np.pi, 2000)
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    
    fig_globe = go.Figure(data=[go.Scatter3d(
        x=x, y=y, z=z, mode='markers',
        marker=dict(size=1.5, color='#00f2ff', opacity=0.5)
    )])
    fig_globe.update_layout(
        scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False, bgcolor='black'),
        margin=dict(l=0, r=0, b=0, t=0), height=500, paper_bgcolor='black'
    )
    st.plotly_chart(fig_globe, use_container_width=True, config={'displayModeBar': False})

    if st.button("START MISSION"):
        st.session_state.scene = 'dashboard'
        st.rerun()

# --- SCENE 2: THE DASHBOARD LAB ---
elif st.session_state.scene == 'dashboard':
    st.markdown("<h2 style='font-family:Orbitron; color:#ff0055;'>DASHBOARD LAB // SURVIVAL STATUS</h2>", unsafe_allow_html=True)
    
    # --- A. TIMELINE SLIDER (LAB EQUIPMENT) ---
    st.markdown("### ⏲️ TEMPORAL CALIBRATOR")
    timeline = st.select_slider(
        "SELECT ERA",
        options=df['Year'].tolist(),
        value=2023,
        label_visibility="collapsed"
    )
    
    # Visual atmosphere changes based on temperature
    current_temp = df[df['Year'] == timeline]['Hanoi_Heat'].values[0]
    glow_color = "#ff4b2b" if current_temp > 26 else "#00f2ff"
    
    st.markdown(f"""
        <div style="padding:10px; border-left: 5px solid {glow_color}; background:rgba(255,255,255,0.02);">
            SYSTEM ALERT: Analysis for Year {timeline} | Thermal Level: {current_temp:.2f}°C
        </div>
    """, unsafe_allow_html=True)

    # --- B. ARTIFACTS (DATA CARDS) ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""<div class='artifact-card'><small>ZONE: HANOI</small><h4>SURVIVAL INDEX</h4><h2>{100 - (current_temp*2):.1f}%</h2></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class='artifact-card'><small>ANOMALY TYPE</small><h4>HEAT_STORM</h4><h2>CRITICAL</h2></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class='artifact-card'><small>NODES DETECTED</small><h4>ACTIVE_SENSORS</h4><h2>1,242</h2></div>""", unsafe_allow_html=True)

    # --- C. COMPARE BATTLE (HP BAR DUEL) ---
    st.markdown("<br><h3 style='font-family:Orbitron;'>⚔️ THERMAL DUEL: HANOI vs LONDON</h3>", unsafe_allow_html=True)
    
    battle_df = df[df['Year'] <= timeline]
    
    fig_battle = go.Figure()
    fig_battle.add_trace(go.Scatter(x=battle_df['Year'], y=battle_df['Hanoi_Heat'], name="HANOI HP", line=dict(color='#ff0055', width=4)))
    fig_battle.add_trace(go.Scatter(x=battle_df['Year'], y=battle_df['London_Heat'], name="LONDON HP", line=dict(color='#00f2ff', width=4)))
    
    fig_battle.update_layout(
        template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False), yaxis=dict(title="HEAT LEVEL")
    )
    st.plotly_chart(fig_battle, use_container_width=True)

    if st.button("TERMINATE SESSION"):
        st.session_state.scene = 'gateway'
        st.rerun()

# --- MICRO-DETAILS (FOOTER) ---
st.markdown("""
    <div style="position:fixed; bottom:10px; right:20px; font-size:0.7rem; opacity:0.5;">
        [ SCANNING SECTOR 07... ] | LAST_LEGACY_PROTOCOL_ACTIVE
    </div>
""", unsafe_allow_html=True)