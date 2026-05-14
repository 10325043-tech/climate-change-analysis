import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# --- ADVANCED HUD CONFIGURATION ---
st.set_page_config(
    page_title="CORE_TERMINAL_V4",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- THE "HYPER-DRIVE" STYLING (CSS & JS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Audiowide&family=Quantico:wght@400;700&family=JetBrains+Mono:wght@100&display=swap');

    :root {
        --core-neon: #00f2ff;
        --core-danger: #ff0055;
        --bg-void: #02040a;
    }

    /* GLOBAL VOID */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: var(--bg-void);
        color: #e0e0e0;
        font-family: 'Quantico', sans-serif;
        cursor: crosshair;
    }

    /* SCANLINE EFFECT */
    .stApp::after {
        content: " ";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), 
                    linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        background-size: 100% 4px, 3px 100%;
        pointer-events: none;
        z-index: 9999;
    }

    /* LANDING PAGE - THE REACTOR CORE */
    .landing-wrapper {
        height: 80vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .reactor-core {
        width: 150px;
        height: 150px;
        border: 4px solid var(--core-neon);
        border-radius: 50%;
        box-shadow: 0 0 50px var(--core-neon), inset 0 0 30px var(--core-neon);
        animation: pulse 2s infinite alternate;
        margin-bottom: 40px;
    }

    @keyframes pulse {
        from { transform: scale(1); opacity: 0.8; }
        to { transform: scale(1.1); opacity: 1; box-shadow: 0 0 80px var(--core-neon); }
    }

    .glitch-title {
        font-family: 'Audiowide', cursive;
        font-size: 6rem;
        text-transform: uppercase;
        color: white;
        text-shadow: 4px 4px var(--core-danger);
        letter-spacing: 20px;
    }

    /* CYBER BUTTON */
    .stButton>button {
        background: transparent !important;
        color: var(--core-neon) !important;
        border: 2px solid var(--core-neon) !important;
        font-family: 'Audiowide' !important;
        padding: 20px 60px !important;
        font-size: 1.5rem !important;
        transition: 0.3s !important;
        clip-path: polygon(10% 0, 100% 0, 90% 100%, 0 100%);
    }

    .stButton>button:hover {
        background: var(--core-neon) !important;
        color: black !important;
        box-shadow: 0 0 40px var(--core-neon) !important;
        transform: skewX(-5deg);
    }

    /* DATA TILES */
    .metric-card {
        background: rgba(0, 242, 255, 0.05);
        border: 1px solid rgba(0, 242, 255, 0.2);
        padding: 20px;
        position: relative;
        overflow: hidden;
    }
    .metric-card::before {
        content: "LIVE_FEED";
        position: absolute;
        top: 5px; right: 5px;
        font-size: 0.5rem;
        color: var(--core-neon);
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- DATA STREAMING ENGINE ---
if 'system_auth' not in st.session_state: st.session_state.system_auth = False

@st.cache_data
def load_climate_data():
    try:
        df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
        df['dt'] = pd.to_datetime(df['dt'])
        df['Year'] = df['dt'].dt.year
        return df.dropna(subset=['AverageTemperature'])
    except:
        # Mock data if file is missing for demonstration
        return pd.DataFrame({'Country': ['Vietnam'], 'Year': [2020], 'AverageTemperature': [27.5]})

df = load_climate_data()

# DYNAMIC REGION MAPPING
REGIONS = {
    "NORTH_AMERICA": ["Canada", "Mexico", "United States"],
    "EURO_ZONE": ["France", "Germany", "Italy", "United Kingdom", "Russia", "Spain", "Sweden"],
    "ASIA_PACIFIC": ["China", "India", "Japan", "Vietnam", "Thailand", "South Korea", "Indonesia"],
    "SOUTHERN_HEM": ["Brazil", "Argentina", "Australia", "South Africa", "Chile"]
}

# --- STAGE 1: THE CORE INITIALIZATION ---
if not st.session_state.system_auth:
    st.markdown("""
        <div class="landing-wrapper">
            <div class="reactor-core"></div>
            <h1 class="glitch-title">HYPER<br>DATA</h1>
            <p style="letter-spacing: 10px; color: #555;">[ AUTHENTICATION REQUIRED ]</p>
        </div>
    """, unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("BYPASS FIREWALL"):
            st.session_state.system_auth = True
            st.rerun()

# --- STAGE 2: THE COMMAND INTERFACE ---
else:
    # Sidebar-less Navigation
    c1, c2, c3 = st.columns([1, 4, 1])
    with c1:
        st.markdown("<h3 style='color:var(--core-neon); font-family:Audiowide;'>NET_STATUS: ONLINE</h3>", unsafe_allow_html=True)
    with c3:
        if st.button("DISCONNECT"):
            st.session_state.system_auth = False
            st.rerun()

    st.markdown("---")

    # GRID LAYOUT
    col_ctrl, col_main = st.columns([1, 3])

    with col_ctrl:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        sector = st.selectbox("SELECT SECTOR", list(REGIONS.keys()))
        subset = df[df['Country'].isin(REGIONS[sector])]
        
        target_nodes = st.multiselect("ISOLATE NODES", REGIONS[sector], default=REGIONS[sector][:2])
        y_min, y_max = st.slider("TIMELINE", 1850, 2013, (1990, 2013))
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        
        # Real-time Metrics
        recent_avg = subset[subset['Year'] == y_max]['AverageTemperature'].mean()
        st.markdown(f"""
            <div class='metric-card' style='border-color: var(--core-danger);'>
                <p style='color:var(--core-danger);'>SECTOR_HEAT_INDEX</p>
                <h2 style='color:white;'>{recent_avg:.2f}°C</h2>
            </div>
        """, unsafe_allow_html=True)

    with col_main:
        # DATA VIZ - THE HEATMATRIX (Better than a Globe)
        viz_data = subset[(subset['Year'] >= y_min) & (subset['Year'] <= y_max)]
        
        # Heatmap over time for countries
        pivot_data = viz_data.groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
        
        fig = px.density_heatmap(
            pivot_data, x="Year", y="Country", z="AverageTemperature",
            color_continuous_scale="Viridis",
            title="THERMAL FREQUENCY MATRIX",
            template="plotly_dark"
        )
        fig.update_layout(
            font_family="JetBrains Mono",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)

        # WAVEFORM ANALYSIS
        if target_nodes:
            line_data = pivot_data[pivot_data['Country'].isin(target_nodes)]
            fig_line = px.line(
                line_data, x="Year", y="AverageTemperature", color="Country",
                line_shape="spline", render_mode="svg"
            )
            fig_line.update_traces(line=dict(width=4))
            fig_line.update_layout(
                title="WAVEFORM TELEMETRY",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(showgrid=False),
                yaxis=dict(gridcolor="rgba(0, 242, 255, 0.1)")
            )
            st.plotly_chart(fig_line, use_container_width=True)

    # FOOTER DECRYPTOR
    st.markdown("""
        <div style="font-family: 'JetBrains Mono'; font-size: 0.7rem; color: #333; margin-top: 50px;">
            >> DECRYPTING_LOCAL_SENSORS... [SUCCESS] <br>
            >> LOADING_CORE_KERNEL_V4.0.1... [ACTIVE] <br>
            >> SYSTEM_STATUS: NO_ANOMALIES_DETECTED
        </div>
    """, unsafe_allow_html=True)