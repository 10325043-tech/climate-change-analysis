import streamlit as st
import time
import numpy as np
import plotly.graph_objects as go

# --- ADVANCED HUD PAGE CONFIGURATION ---
st.set_page_config(
    page_title="OMNISCIENCE TACTICAL HUD",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- MAXED-OUT CYBERPUNK CSS SCIFI THEMING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    
    /* Global screen overlay & matrix vibe */
    .stApp {
        background-color: #03030b;
        background-image: 
            linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%),
            linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06)),
            radial-gradient(circle at center, #0f0a21 0%, #010105 100%);
        background-size: 100% 4px, 6px 100%, 100% 100%;
        color: #00f3ff;
        font-family: 'Share Tech Mono', 'Courier New', monospace;
    }
    
    /* Global layout container squeeze to match cinematic widescreen */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1rem;
        max-width: 96%;
    }
    
    /* High-tech modular panels with corner sub-indicators */
    [data-testid="column"] {
        background: rgba(0, 10, 25, 0.6) !important;
        border: 1px solid rgba(0, 243, 255, 0.35) !important;
        border-radius: 4px !important;
        padding: 18px !important;
        box-shadow: 0 0 20px rgba(0, 243, 255, 0.1), inset 0 0 15px rgba(0, 243, 255, 0.05);
        position: relative;
    }

    /* Outer Tech Bezel Decor for the whole app via background simulation */
    .hud-header-bar {
        border-bottom: 2px solid #00f3ff;
        padding-bottom: 5px;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        letter-spacing: 2px;
        text-shadow: 0 0 5px #00f3ff;
    }

    .hud-title {
        text-align: center;
        color: #00f3ff;
        font-size: 32px;
        font-weight: 900;
        letter-spacing: 8px;
        margin-bottom: 20px;
        text-shadow: 0 0 15px rgba(0, 243, 255, 0.8), 0 0 2px #00f3ff;
    }

    .critical-text {
        color: #ff0055;
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        letter-spacing: 4px;
        text-shadow: 0 0 12px #ff0055;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .terminal-small {
        font-size: 12px;
        color: #00f3ff;
        line-height: 1.5;
        letter-spacing: 1.5px;
    }
    
    .panel-tag {
        font-size: 10px;
        color: rgba(0, 243, 255, 0.5);
        margin-bottom: 8px;
        border-bottom: 1px solid rgba(0, 243, 255, 0.15);
        padding-bottom: 3px;
    }

    .directive-body {
        font-size: 14.5px;
        color: #c2f1ff;
        text-align: justify;
        line-height: 1.7;
        margin: 15px 0;
        background: rgba(0, 243, 255, 0.03);
        padding: 15px;
        border-left: 3px solid #ff0055;
    }

    /* DETAILED MILITARY RADAR SIMULATION */
    .radar-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 20px 0;
    }
    .radar {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        border: 2px solid rgba(0, 243, 255, 0.6);
        background: 
            linear-gradient(rgba(0,243,255,0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,243,255,0.05) 1px, transparent 1px),
            radial-gradient(circle at center, rgba(0,243,255,0.15) 0%, rgba(0,0,0,0) 80%);
        background-size: 20px 20px, 20px 20px, 100% 100%;
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 30px rgba(0,243,255,0.2) inset, 0 0 15px rgba(0,243,255,0.1);
    }
    .radar::before {
        content: '';
        display: block;
        position: absolute;
        width: 50%;
        height: 50%;
        bottom: 50%;
        left: 50%;
        transform-origin: 0% 100%;
        background: linear-gradient(90deg, rgba(0,243,255,0) 0%, rgba(0,243,255,0.6) 100%);
        border-right: 2px solid #00f3ff;
        animation: radar-spin 3s linear infinite;
    }
    .radar-grid-ring {
        position: absolute;
        width: 100%; height: 100%;
        border-radius: 50%;
        border: 1px dashed rgba(0, 243, 255, 0.3);
        transform: scale(0.66);
    }
    .radar-grid-ring-2 {
        position: absolute;
        width: 100%; height: 100%;
        border-radius: 50%;
        border: 1px dotted rgba(0, 243, 255, 0.4);
        transform: scale(0.33);
    }
    .radar-blip {
        position: absolute;
        width: 6px; height: 6px;
        background: #ff0055;
        border-radius: 50%;
        top: 35%; left: 65%;
        box-shadow: 0 0 10px #ff0055;
        animation: blink 1.5s infinite;
    }
    .radar-crosshair-h {
        position: absolute; width: 100%; height: 1px;
        background: rgba(0, 243, 255, 0.4); top: 50%;
    }
    .radar-crosshair-v {
        position: absolute; width: 1px; height: 100%;
        background: rgba(0, 243, 255, 0.4); left: 50%;
    }
    
    @keyframes radar-spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    @keyframes blink {
        0%, 100% { opacity: 0.2; }
        50% { opacity: 1; }
    }

    /* Tactical Trigger Button Styling */
    div.stButton > button {
        width: 100%;
        background: rgba(0, 243, 255, 0.08) !important;
        color: #00f3ff !important;
        border: 1px solid #00f3ff !important;
        padding: 14px !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 18px !important;
        letter-spacing: 4px !important;
        font-weight: bold !important;
        border-radius: 2px !important;
        box-shadow: 0 0 10px rgba(0, 243, 255, 0.2) !important;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background: #00f3ff !important;
        color: #03030b !important;
        box-shadow: 0 0 30px rgba(0, 243, 255, 0.8) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- HELPER FUNCTIONS FOR HIGH-DENSITY INTEL CHARTS ---
def create_hologram_globe():
    """Generates a wireframe graticule sci-fi globe mesh using Plotly."""
    fig = go.Figure(data=go.Scattergeo(lon=[], lat=[]))
    fig.update_layout(
        geo=dict(
            projection_type="orthographic",
            showcoastlines=True,
            coastlinecolor="rgba(0, 243, 255, 0.8)",
            coastlinewidth=1.5,
            showland=True,
            landcolor="rgba(0, 35, 70, 0.35)",
            showocean=False,
            showlakes=False,
            bgcolor="rgba(0,0,0,0)",
            framecolor="rgba(0,0,0,0)",
            # The Magic Element: Adds the complex grid gridlines onto the globe
            showgraticule=True,
            graticulecolor="rgba(0, 243, 255, 0.3)",
            graticulewidth=1,
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=5, r=5, t=5, b=5),
        height=190
    )
    return fig

def create_dense_hud_chart(base_color, accent_color, seed_val):
    """Generates mixed bar + overlay line charts mimicking real-time data flows."""
    np.random.seed(seed_val)
    x = np.arange(16)
    y_bars = np.random.randint(4, 22, 16) + (x * 0.4)
    y_line = y_bars + np.random.normal(0, 1.8, 16)
    
    fig = go.Figure()
    # Cyber bars
    fig.add_trace(go.Bar(
        x=x, y=y_bars,
        marker_color=base_color,
        opacity=0.35,
        marker_line_width=0
    ))
    # Tech line trace
    fig.add_trace(go.Scatter(
        x=x, y=y_line,
        mode='lines+markers',
        line=dict(color=accent_color, width=2),
        marker=dict(size=4, color=accent_color)
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False, visible=False),
        yaxis=dict(
            showgrid=True, 
            gridcolor='rgba(0, 243, 255, 0.1)', 
            zeroline=False, 
            tickfont=dict(color='rgba(0, 243, 255, 0.7)', size=9)
        ),
        margin=dict(l=20, r=5, t=5, b=5),
        height=125,
        showlegend=False,
        barmode='overlay'
    )
    return fig

# --- ROUTING SYSTEM STATE ---
if "page" not in st.session_state:
    st.session_state.page = "INTRO"

# =====================================================================
# SYSTEM MAIN INTERFACE: LAYER 1 COGNITIVE CONSOLE
# =====================================================================
if st.session_state.page == "INTRO":
    
    # Outer Framing Top-Bar Decor
    st.markdown("""
    <div class="hud-header-bar">
        <div>SYS_LOC: RECON_ORBIT_VALKYRIE // UNIT: ALFA-74</div>
        <div>OMNISCIENCE TACTICAL HUD CORE V9.12</div>
        <div>CO2: DETECTED // LIFE_SUPPORT: WARNING [34%]</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="hud-title">OMNISCIENCE SYSTEM</div>', unsafe_allow_html=True)
    
    # Precise 3-Column Sci-Fi Symmetrical Array
    col_left, col_center, col_right = st.columns([1.3, 2.4, 1.3], gap="medium")
    
    # --- LEFT INSTRUMENT PANEL (HOLOGRAM SPHERES) ---
    with col_left:
        st.markdown('<div class="panel-tag">LAYER_A // ATMOSPHERIC SLOTS</div>', unsafe_allow_html=True)
        st.plotly_chart(create_hologram_globe(), use_container_width=True, config={'displayModeBar': False}, key="globe_1")
        
        st.markdown('<div class="panel-tag">LAYER_B // BIOSPHERE SCAN GRID</div>', unsafe_allow_html=True)
        st.plotly_chart(create_hologram_globe(), use_container_width=True, config={'displayModeBar': False}, key="globe_2")
        
        st.markdown("""
        <div class="terminal-small" style="color: rgba(0, 243, 255, 0.55); border-top: 1px dashed rgba(0,243,255,0.2); padding-top: 8px; margin-top: 5px;">
        >> DATANODE_MECH: 90X / ACTIVE<br>
        >> FRAME_ID: SC0002K-THETA<br>
        >> UPLINK_INDEX: QUANTUM_COM-4
        </div>
        """, unsafe_allow_html=True)

    # --- CENTER COMMAND PANEL (CRITICAL INTEL & WEAPON RADAR) ---
    with col_center:
        st.markdown("""
        <div class="terminal-small" style="opacity: 0.9; color: #00f3ff;">
        [BOOT]: Establishing deep-space uplink with OMNISCIENCE Recon Satellite...<br>
        [CONNECT]: Quantum data link synchronized with Ark Ship Core v7.4...<br>
        [DECRYPT]: Matrix HUD layout deciphered... SECURE CODES ONLINE.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="critical-text">CRITICAL ENVELOPE: HIGH COUNCIL DIRECTIVE</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="directive-body">
        The Mother Planet has remained abandoned for over a century following the catastrophic global thermal cascade. 
        Ark Ship life support reserves are currently depleting. 
        Your mandate is to operationalize the Omniscience Long-Range Biosphere Scanner, analyze historical planetary degradation vectors, and locate viable sectors for atmospheric re-colonization.
        </div>
        """, unsafe_allow_html=True)
        
        # Highly Custom CSS Radar with Blips and Internals
        st.markdown("""
        <div class="radar-container">
            <div class="radar">
                <div class="radar-grid-ring"></div>
                <div class="radar-grid-ring-2"></div>
                <div class="radar-crosshair-h"></div>
                <div class="radar-crosshair-v"></div>
                <div class="radar-blip"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("INITIALIZE BIOSPHERE SCANNER"):
            st.session_state.page = "SECTOR"
            st.rerun()

    # --- RIGHT DATA INTERFACE PANEL (DENSE REAL-TIME STATS) ---
    with col_right:
        st.markdown('<div class="panel-tag">INTEL_1 // CLIMATE DEGRADATION VECTOR</div>', unsafe_allow_html=True)
        st.plotly_chart(create_dense_hud_chart("#ff0055", "#00f3ff", 101), use_container_width=True, config={'displayModeBar': False}, key="chart_1")
        
        st.markdown('<div class="panel-tag">INTEL_2 // VIABLE SECTOR LOCATOR MAP</div>', unsafe_allow_html=True)
        st.plotly_chart(create_dense_hud_chart("#00f3ff", "#ffffff", 202), use_container_width=True, config={'displayModeBar': False}, key="chart_2")
        
        st.markdown('<div class="panel-tag">INTEL_3 // THERMAL CASCADE TRACKER</div>', unsafe_allow_html=True)
        st.plotly_chart(create_dense_hud_chart("#00ff88", "#ff0055", 303), use_container_width=True, config={'displayModeBar': False}, key="chart_3")

    # --- BOTTOM MATRIX LOG FOOTER ---
    st.markdown("<hr style='border:1px solid rgba(0,243,255,0.2); margin-top:15px; margin-bottom:10px;'>", unsafe_allow_html=True)
    st.markdown("""
    <div class="terminal-small" style="color: rgba(0, 243, 255, 0.4); font-size: 11px;">
    [SYSTEM TELEMETRY]: Syncing database archive... Integrity 100%. 577,462 environmental telemetry data logs active.<br>
    [CONSOLE]: Awaiting commanding officer authorization to jump to sector coordinates...
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# SYSTEM CORE INTERFACE: LAYER 2 LAYER SELECTOR
# =====================================================================
elif st.session_state.page == "SECTOR":
    st.markdown('<div class="hud-title">SECTOR SCANNING ACTIVE</div>', unsafe_allow_html=True)
    st.write("System online. Standby for target mapping.")
    if st.button("ABORT MISSION & RESET DISCONNECT"):
        st.session_state.page = "INTRO"
        st.rerun()