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
    
    /* Style the Streamlit columns to look like HUD panels */
    [data-testid="column"] {
        background: rgba(0, 20, 40, 0.4);
        border: 1px solid rgba(0, 243, 255, 0.3);
        border-radius: 5px;
        padding: 10px;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.05);
    }
    
    /* Hide top padding */
    .block-container {
        padding-top: 2rem;
        max-width: 95%;
    }

    .hud-title {
        text-align: center;
        color: #00f3ff;
        font-size: 24px;
        letter-spacing: 4px;
        margin-bottom: 20px;
        text-shadow: 0 0 10px #00f3ff;
    }

    .critical-text {
        color: #ff0055;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        letter-spacing: 3px;
        text-shadow: 0 0 15px #ff0055;
        margin-bottom: 10px;
    }

    .terminal-small {
        font-size: 12px;
        color: #00f3ff;
        line-height: 1.4;
    }

    .directive-body {
        font-size: 15px;
        color: #b3ecff;
        text-align: justify;
        line-height: 1.6;
        margin: 20px 0;
    }

    /* CSS RADAR ANIMATION */
    .radar-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    .radar {
        width: 250px;
        height: 250px;
        border-radius: 50%;
        border: 2px solid rgba(0, 243, 255, 0.5);
        background: radial-gradient(circle at center, rgba(0,243,255,0.1) 0%, rgba(0,0,0,0) 70%);
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 30px rgba(0,243,255,0.2) inset;
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
        background: linear-gradient(90deg, rgba(0,243,255,0) 0%, rgba(0,243,255,0.5) 100%);
        border-right: 2px solid #00f3ff;
        animation: radar-spin 3s linear infinite;
    }
    .radar-grid {
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 1px dashed rgba(0, 243, 255, 0.2);
        transform: scale(0.66);
    }
    .radar-grid-2 {
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 1px dashed rgba(0, 243, 255, 0.2);
        transform: scale(0.33);
    }
    .radar-crosshair {
        position: absolute;
        width: 100%;
        height: 1px;
        background: rgba(0, 243, 255, 0.3);
        top: 50%;
    }
    .radar-crosshair-v {
        position: absolute;
        width: 1px;
        height: 100%;
        background: rgba(0, 243, 255, 0.3);
        left: 50%;
    }
    @keyframes radar-spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    div.stButton > button {
        width: 100%;
        background: rgba(0, 243, 255, 0.1) !important;
        color: #00f3ff !important;
        border: 1px solid #00f3ff !important;
        padding: 10px !important;
        font-family: 'Share Tech Mono', monospace !important;
        font-size: 18px !important;
        letter-spacing: 2px !important;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: rgba(0, 243, 255, 0.4) !important;
        box-shadow: 0 0 20px #00f3ff !important;
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
            coastlinecolor="rgba(0, 243, 255, 0.6)",
            showland=True,
            landcolor="rgba(0, 0, 0, 0)",
            showocean=True,
            oceancolor="rgba(0, 0, 0, 0)",
            showlakes=False,
            bgcolor="rgba(0,0,0,0)",
            framecolor="rgba(0,0,0,0)"
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=0, b=0),
        height=220
    )
    return fig

def create_hud_chart(color):
    x = np.linspace(0, 100, 50)
    y = np.sin(x/10) + np.random.normal(0, 0.2, 50) + (x/50)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color=color, width=2), fill='tozeroy', fillcolor=f'rgba{tuple(list(int(color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)) + [0.2])}'))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False, visible=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(0,243,255,0.1)', zeroline=False, tickfont=dict(color='#00f3ff', size=9)),
        margin=dict(l=20, r=5, t=5, b=5),
        height=150,
        showlegend=False
    )
    return fig

# --- STATE MANAGEMENT ---
if "page" not in st.session_state:
    st.session_state.page = "INTRO"

# --- PAGE 1: FULL HUD ---
if st.session_state.page == "INTRO":
    st.markdown('<div class="hud-title">OMNISCIENCE SYSTEM</div>', unsafe_allow_html=True)
    
    # 3-COLUMN LAYOUT EXACTLY LIKE THE IMAGE
    col_left, col_center, col_right = st.columns([1.2, 2.5, 1.2], gap="medium")
    
    # --- LEFT PANEL: GLOBES ---
    with col_left:
        st.markdown('<div class="terminal-small">ATMOSPHERIC SLOTS</div>', unsafe_allow_html=True)
        st.plotly_chart(create_wireframe_globe(), use_container_width=True, config={'displayModeBar': False})
        st.markdown('<div class="terminal-small" style="text-align:right;">BIOSPHERE SCAN</div>', unsafe_allow_html=True)
        st.plotly_chart(create_wireframe_globe(), use_container_width=True, config={'displayModeBar': False})
        st.markdown("""
        <div class="terminal-small">
        DATANODE_MECH: 50X<br>
        SYSTEM_ID: 9C0000X<br>
        SEC_LVL: ALPHA-74
        </div>
        """, unsafe_allow_html=True)

    # --- CENTER PANEL: DIRECTIVE & RADAR ---
    with col_center:
        st.markdown("""
        <div class="terminal-small">
        [BOOT]: Establishing deep-space uplink with OMNISCIENCE Recon Satellite...<br>
        [CONNECT]: Quantum data link synchronized with Ark Ship Core v7.4...<br>
        [DECRYPT]: Matrix HUD layout deciphered...
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<hr style='border:1px solid rgba(0,243,255,0.2);'>", unsafe_allow_html=True)
        
        st.markdown('<div class="critical-text">CRITICAL ENVELOPE: HIGH COUNCIL DIRECTIVE</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="directive-body">
        The Mother Planet has remained abandoned for over a century following the catastrophic global thermal cascade. Ark Ship life support reserves are currently depleting. Your mandate is to operationalize the Omniscience Long-Range Biosphere Scanner, analyze historical planetary degradation vectors, and locate viable sectors for atmospheric re-colonization.
        </div>
        """, unsafe_allow_html=True)
        
        # The Custom CSS Radar
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

    # --- RIGHT PANEL: CHARTS ---
    with col_right:
        st.markdown('<div class="terminal-small">HISTORICAL CLIMATE DEGRADATION VECTOR</div>', unsafe_allow_html=True)
        st.plotly_chart(create_hud_chart("#ff0055"), use_container_width=True, config={'displayModeBar': False})
        
        st.markdown('<div class="terminal-small">VIABLE SECTOR LOCATOR</div>', unsafe_allow_html=True)
        st.plotly_chart(create_hud_chart("#00f3ff"), use_container_width=True, config={'displayModeBar': False})
        
        st.markdown('<div class="terminal-small">THERMAL ANOMALY TRACKER</div>', unsafe_allow_html=True)
        st.plotly_chart(create_hud_chart("#00ff88"), use_container_width=True, config={'displayModeBar': False})

    # --- BOTTOM LOG ---
    st.markdown("<hr style='border:1px solid rgba(0,243,255,0.2);'>", unsafe_allow_html=True)
    st.markdown("""
    <div class="terminal-small">
    [SYSTEM LOG]: Climate Vault database linked successfully. 577,462 environmental telemetry logs online.<br>
    [STATUS]: WAITING FOR OFFICER INPUT...
    </div>
    """, unsafe_allow_html=True)

# --- PAGE 2 ---
elif st.session_state.page == "SECTOR":
    st.markdown('<div class="hud-title">SECTOR SCANNING ACTIVE</div>', unsafe_allow_html=True)
    if st.button("ABORT MISSION"):
        st.session_state.page = "INTRO"
        st.rerun()