import streamlit as st
import time
import numpy as np
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="OMNISCIENCE SYSTEM",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR HUD STYLING & RADAR ANIMATION ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    
    .stApp {
        background-color: #050510;
        background-image: radial-gradient(circle at center, #100b20 0%, #020108 100%);
        color: #00f3ff;
        font-family: 'Share Tech Mono', 'Courier New', monospace;
    }
    
    /* Panel border decoration mimicking game HUDs */
    [data-testid="column"] {
        background: rgba(0, 15, 30, 0.4);
        border: 1px solid rgba(0, 243, 255, 0.25);
        border-radius: 6px;
        padding: 15px;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.05), inset 0 0 10px rgba(0, 243, 255, 0.05);
    }
    
    .block-container {
        padding-top: 2rem;
        max-width: 95%;
    }

    .hud-title {
        text-align: center;
        color: #00f3ff;
        font-size: 28px;
        letter-spacing: 6px;
        margin-bottom: 25px;
        text-shadow: 0 0 12px #00f3ff;
    }

    .critical-text {
        color: #ff0055;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        letter-spacing: 3px;
        text-shadow: 0 0 15px #ff0055;
        margin-bottom: 15px;
    }

    .terminal-small {
        font-size: 13px;
        color: #00f3ff;
        line-height: 1.5;
        letter-spacing: 1px;
    }

    .directive-body {
        font-size: 15px;
        color: #b3ecff;
        text-align: justify;
        line-height: 1.7;
        margin: 20px 0;
        letter-spacing: 0.5px;
    }

    /* SYSTEM RADAR ANIMATION */
    .radar-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 25px;
        margin-bottom: 25px;
    }
    .radar {
        width: 220px;
        height: 220px;
        border-radius: 50%;
        border: 2px solid rgba(0, 243, 255, 0.4);
        background: radial-gradient(circle at center, rgba(0,243,255,0.08) 0%, rgba(0,0,0,0) 75%);
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 20px rgba(0,243,255,0.15) inset;
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
        background: linear-gradient(90deg, rgba(0,243,255,0) 0%, rgba(0,243,255,0.4) 100%);
        border-right: 2px solid #00f3ff;
        animation: radar-spin 4s linear infinite;
    }
    .radar-grid {
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 1px dashed rgba(0, 243, 255, 0.15);
        transform: scale(0.66);
    }
    .radar-grid-2 {
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 1px dashed rgba(0, 243, 255, 0.15);
        transform: scale(0.33);
    }
    .radar-crosshair {
        position: absolute;
        width: 100%;
        height: 1px;
        background: rgba(0, 243, 255, 0.25);
        top: 50%;
    }
    .radar-crosshair-v {
        position: absolute;
        width: 1px;
        height: 100%;
        background: rgba(0, 243, 255, 0.25);
        left: 50%;
    }
    @keyframes radar-spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* Cyberpunk Tactical Button style */
    div.stButton > button {
        width: 100%;
        background: rgba(0, 243, 255, 0.05) !important;
        color: #00f3ff !important;
        border: 1px solid #00f3ff !important;
        padding: 12px !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 18px !important;
        letter-spacing: 3px !important;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: rgba(0, 243, 255, 0.3) !important;
        box-shadow: 0 0 25px rgba(0, 243, 255, 0.6) !important;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- HELPER FUNCTIONS FOR CHARTS ---
def create_wireframe_globe():
    fig = go.Figure(data=go.Scattergeo(lon=[], lat=[]))
    fig.update_layout(
        geo=dict(
            projection_type="orthographic",
            showcoastlines=True,
            coastlinecolor="rgba(0, 243, 255, 0.5)",
            showland=True,
            landcolor="rgba(0, 30, 60, 0.2)",
            showocean=False,
            showlakes=False,
            bgcolor="rgba(0,0,0,0)",
            framecolor="rgba(0,0,0,0)"
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=0, b=0),
        height=200
    )
    return fig

def create_hud_chart(color, seed_val):
    np.random.seed(seed_val)
    x = np.linspace(0, 100, 40)
    y = np.sin(x/8) + np.random.normal(0, 0.15, 40) + (x/60)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=y, 
        mode='lines', 
        line=dict(color=color, width=1.5), 
        fill='tozeroy', 
        fillcolor=f'rgba{tuple(list(int(color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)) + [0.1])}'
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False, visible=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(0,243,255,0.08)', zeroline=False, tickfont=dict(color='#00f3ff', size=9)),
        margin=dict(l=15, r=5, t=5, b=5),
        height=130,
        showlegend=False
    )
    return fig

# --- STATE MANAGEMENT ---
if "page" not in st.session_state:
    st.session_state.page = "INTRO"

# =====================================================================
# STAGE 1: INTRO HUD SCREEN
# =====================================================================
if st.session_state.page == "INTRO":
    st.markdown('<div class="hud-title">OMNISCIENCE SYSTEM</div>', unsafe_allow_html=True)
    
    # 3-Panel Layout
    col_left, col_center, col_right = st.columns([1.3, 2.4, 1.3], gap="medium")
    
    # --- LEFT PANEL ---
    with col_left:
        st.markdown('<div class="terminal-small">⚙️ ATMOSPHERIC SLOTS</div>', unsafe_allow_html=True)
        st.plotly_chart(create_wireframe_globe(), use_container_width=True, config={'displayModeBar': False}, key="globe_slot_1")
        
        st.markdown('<div class="terminal-small">🛰️ BIOSPHERE SCAN LAYER</div>', unsafe_allow_html=True)
        st.plotly_chart(create_wireframe_globe(), use_container_width=True, config={'displayModeBar': False}, key="globe_slot_2")
        
        st.markdown("""
        <div class="terminal-small" style="color: rgba(0, 243, 255, 0.6); border-top: 1px solid rgba(0,243,255,0.1); padding-top: 10px; margin-top: 10px;">
        DATANODE_MECH: 90X<br>
        SYSTEM_ID: SC0002K<br>
        SEC_LEVEL: ALFA-74<br>
        UPLINK_INDEX: COM-4
        </div>
        """, unsafe_allow_html=True)

    # --- CENTER PANEL ---
    with col_center:
        st.markdown("""
        <div class="terminal-small" style="color: #00f3ff; opacity: 0.85;">
        [BOOT]: Establishing deep-space uplink with OMNISCIENCE Recon Satellite...<br>
        [CONNECT]: Quantum data link synchronized with Ark Ship Core v7.4...<br>
        [DECRYPT]: Matrix HUD layout deciphered...
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<hr style='border:1px dashed rgba(0,243,255,0.2); margin:15px 0;'>", unsafe_allow_html=True)
        
        st.markdown('<div class="critical-text">CRITICAL ENVELOPE: HIGH COUNCIL DIRECTIVE</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="directive-body">
        The Mother Planet has remained abandoned for over a century following the catastrophic global thermal cascade. 
        Ark Ship life support reserves are currently depleting. 
        Your mandate is to operationalize the Omniscience Long-Range Biosphere Scanner, analyze historical planetary degradation vectors, and locate viable sectors for atmospheric re-colonization.
        </div>
        """, unsafe_allow_html=True)
        
        # Animated CSS Radar Display
        st.markdown("""
        <div class="radar-container">
            <div class="radar">
                <div class="radar-grid"></div>
                <div class="radar-grid-2"></div>
                <div class="radar-crosshair"></div>
                <div class="radar-crosshair-v"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("INITIALIZE BIOSPHERE SCANNER"):
            st.session_state.page = "SECTOR"
            st.rerun()

    # --- RIGHT PANEL ---
    with col_right:
        st.markdown('<div class="terminal-small">📈 HISTORICAL CLIMATE DEGRADATION</div>', unsafe_allow_html=True)
        st.plotly_chart(create_hud_chart("#ff0055", 42), use_container_width=True, config={'displayModeBar': False}, key="chart_right_1")
        
        st.markdown('<div class="terminal-small">🎯 VIABLE SECTOR LOCATOR</div>', unsafe_allow_html=True)
        st.plotly_chart(create_hud_chart("#00f3ff", 24), use_container_width=True, config={'displayModeBar': False}, key="chart_right_2")
        
        st.markdown('<div class="terminal-small">🔥 THERMAL CASCADE ANOMALY</div>', unsafe_allow_html=True)
        st.plotly_chart(create_hud_chart("#00ff88", 99), use_container_width=True, config={'displayModeBar': False}, key="chart_right_3")

    # --- FOOTER SYSTEM LOG ---
    st.markdown("<hr style='border:1px solid rgba(0,243,255,0.15); margin-top:20px;'>", unsafe_allow_html=True)
    st.markdown("""
    <div class="terminal-small" style="opacity:0.7;">
    [BOOT]: Establishing deep-space uplink with OMNISCIENCE Recon Satellite...<br>
    [SYSTEM LOG]: Climate Vault database linked successfully. 577,462 environmental telemetry logs online.
    </div>
    """, unsafe_allow_html=True)

# =====================================================================
# STAGE 2: SECTOR SCANNING ACTIVE
# =====================================================================
elif st.session_state.page == "SECTOR":
    st.markdown('<div class="hud-title">SECTOR SCANNING ACTIVE</div>', unsafe_allow_html=True)
    st.write("System online. Standby for target mapping.")
    if st.button("ABORT MISSION"):
        st.session_state.page = "INTRO"
        st.rerun()