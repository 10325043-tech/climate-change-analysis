import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- ADVANCED UI ENGINE CONFIGURATION ---
st.set_page_config(
    page_title="NEURAL TERMINAL v2.0",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a professional, high-fidelity cybernetic interface
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300;500&display=swap');

    :root {
        --primary: #00fff2;
        --secondary: #7000ff;
        --bg-dark: #0a0a0c;
        --panel-bg: rgba(20, 20, 25, 0.8);
    }

    html, body, [data-testid="stAppViewContainer"] {
        background-color: var(--bg-dark);
        color: #e0e0e0;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Cinematic Landing Section */
    .hero-container {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: radial-gradient(circle at center, rgba(112, 0, 255, 0.15) 0%, transparent 75%);
        border: 1px solid rgba(0, 255, 242, 0.1);
        margin: 10px;
    }

    .glitch-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 7rem;
        font-weight: 700;
        letter-spacing: 15px;
        color: white;
        text-shadow: 2px 2px var(--secondary), -2px -2px var(--primary);
        margin-bottom: 0;
    }

    /* Interactive Sector Grid */
    .sector-wrap {
        position: relative;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: 0.5s cubic-bezier(0.2, 1, 0.3, 1);
        height: 450px;
    }

    .sector-wrap:hover {
        border-color: var(--primary);
        box-shadow: 0 0 30px rgba(0, 255, 242, 0.2);
        transform: translateY(-5px);
    }

    .sector-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: grayscale(1) contrast(1.2) brightness(0.6);
        transition: 0.8s;
    }

    .sector-wrap:hover .sector-img {
        filter: grayscale(0) brightness(0.8);
        transform: scale(1.05);
    }

    .overlay-text {
        position: absolute;
        bottom: 30px;
        left: 30px;
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem;
        z-index: 10;
        color: var(--primary);
        pointer-events: none;
    }

    /* Dashboard UI Elements */
    .metric-card {
        background: var(--panel-bg);
        border: 1px solid rgba(0, 255, 242, 0.2);
        padding: 25px;
        border-radius: 4px;
        margin-bottom: 20px;
    }

    /* Global Button Overrides */
    .stButton>button {
        background: transparent !important;
        border: 1px solid var(--primary) !important;
        color: var(--primary) !important;
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 2px;
        border-radius: 0 !important;
        transition: 0.3s !important;
    }

    .stButton>button:hover {
        background: var(--primary) !important;
        color: black !important;
        box-shadow: 0 0 15px var(--primary);
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE CORE ---
if 'state' not in st.session_state:
    st.session_state.state = 'intro'
if 'region' not in st.session_state:
    st.session_state.region = None

@st.cache_data
def load_global_dataset():
    try:
        df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
        df['dt'] = pd.to_datetime(df['dt'])
        df['Year'] = df['dt'].dt.year
        return df.dropna(subset=['AverageTemperature'])
    except:
        return pd.DataFrame()

data = load_global_dataset()

# Sector Configuration
REGION_CONFIG = {
    "ASIA": {
        "img": "https://images.unsplash.com/photo-1535139262971-c3f8477c2eeb?w=1200",
        "targets": ["Vietnam", "Thailand", "China", "India", "Japan", "South Korea"]
    },
    "EUROPE": {
        "img": "https://images.unsplash.com/photo-1490642914619-7955a3fd483c?w=1200",
        "targets": ["Germany", "France", "Italy", "Spain", "United Kingdom", "Sweden"]
    },
    "AMERICAS": {
        "img": "https://images.unsplash.com/photo-1485738422979-f5c462d49f74?w=1200",
        "targets": ["United States", "Canada", "Brazil", "Mexico", "Argentina"]
    },
    "AFRICA": {
        "img": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=1200",
        "targets": ["Egypt", "Nigeria", "South Africa", "Kenya", "Morocco"]
    }
}

# --- VIEW 01: CINEMATIC ENTRANCE ---
if st.session_state.state == 'intro':
    st.markdown("""
        <div class="hero-container">
            <p style="letter-spacing: 10px; color: var(--primary); margin-bottom: 0;">SATELLITE DOWNLINK // 2026</p>
            <h1 class="glitch-title">CLIMATE CORE</h1>
            <p style="opacity: 0.4; margin-top: 20px;">ENCRYPTED GEOSPATIAL ANALYSIS TERMINAL</p>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([2, 1, 2])
    with c2:
        if st.button("INITIALIZE SYSTEM", use_container_width=True):
            st.session_state.state = 'grid'
            st.rerun()

# --- VIEW 02: SECTOR TARGETING ---
elif st.session_state.state == 'grid':
    st.markdown("<h2 style='text-align:center; font-family:Orbitron; margin: 40px 0;'>GEOGRAPHIC SECTOR LOCK</h2>", unsafe_allow_html=True)
    
    cols = st.columns(2)
    sectors_list = list(REGION_CONFIG.items())
    
    for i in range(2): # First Row
        name, meta = sectors_list[i]
        with cols[i]:
            st.markdown(f'<div class="sector-wrap"><img src="{meta["img"]}" class="sector-img"><div class="overlay-text">{name}</div></div>', unsafe_allow_html=True)
            if st.button(f"ENGAGE {name}", use_container_width=True):
                st.session_state.region = name
                st.session_state.state = 'monitor'
                st.rerun()

    cols2 = st.columns(2)
    for i in range(2, 4): # Second Row
        name, meta = sectors_list[i]
        with cols2[i-2]:
            st.markdown(f'<div class="sector-wrap"><img src="{meta["img"]}" class="sector-img"><div class="overlay-text">{name}</div></div>', unsafe_allow_html=True)
            if st.button(f"ENGAGE {name}", use_container_width=True):
                st.session_state.region = name
                st.session_state.state = 'monitor'
                st.rerun()

# --- VIEW 03: LIVE MONITORING DASHBOARD ---
elif st.session_state.state == 'monitor':
    st.markdown("<style>html, body, [data-testid='stAppViewContainer'] { overflow-y: auto !important; }</style>", unsafe_allow_html=True)
    
    # TOP NAVIGATION
    t1, t2 = st.columns([5, 1])
    t1.markdown(f"<h1 style='font-family:Orbitron; color:var(--primary);'>🛰️ MONITORING: {st.session_state.region}_SECTOR</h1>", unsafe_allow_html=True)
    if t2.button("DISCONNECT"):
        st.session_state.state = 'grid'
        st.rerun()

    cfg = REGION_CONFIG[st.session_state.region]
    df_sector = data[data['Country'].isin(cfg['targets'])]

    # GLOBAL CONTROLS (Floating Effect)
    st.markdown("<div style='border: 1px solid var(--primary); padding:20px; background:rgba(0,255,242,0.05); margin-bottom:30px;'>", unsafe_allow_html=True)
    ctrl1, ctrl2 = st.columns([1, 1])
    with ctrl1:
        timeline = st.slider("TEMPORAL RESOLUTION (YEARS)", int(df_sector['Year'].min()), int(df_sector['Year'].max()), (1960, 2013))
    with ctrl2:
        isolation = st.multiselect("ISOLATE NATIONAL SIGNALS", cfg['targets'], default=cfg['targets'][:2])
    st.markdown("</div>", unsafe_allow_html=True)

    # DATA SLICE
    filtered = df_sector[(df_sector['Year'] >= timeline[0]) & (df_sector['Year'] <= timeline[1])]
    
    # VISUAL ANALYTICS GRID
    m1, m2 = st.columns([2, 1])
    
    with m1:
        st.markdown("#### GEOSPATIAL THERMAL SCAN")
        map_data = filtered.groupby('Country')['AverageTemperature'].mean().reset_index()
        scope_val = st.session_state.region.lower() if st.session_state.region != "AMERICAS" else "north america"
        
        fig_map = px.choropleth(
            map_data, locations="Country", locationmode='country names',
            color="AverageTemperature", color_continuous_scale="Electric",
            scope=scope_val, template="plotly_dark"
        )
        fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=550, paper_bgcolor='rgba(0,0,0,0)', geo_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_map, use_container_width=True)

    with m2:
        st.markdown("#### PEAK ANOMALIES")
        top_list = map_data.sort_values('AverageTemperature', ascending=False).head(3)
        for _, row in top_list.iterrows():
            st.markdown(f"""
                <div class="metric-card">
                    <p style="color:var(--primary); font-size:0.7rem; letter-spacing:3px; margin:0;">TARGET: {row['Country'].upper()}</p>
                    <h2 style="font-family:Orbitron; margin:10px 0;">{row['AverageTemperature']:.2f}°C</h2>
                    <div style="height:2px; width:100%; background:linear-gradient(90deg, var(--primary), transparent);"></div>
                    <p style="color:#555; font-size:0.6rem; margin-top:5px;">SIGNAL STRENGTH: 98.4%</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### TEMPORAL VARIATION ANALYSIS")
    if isolation:
        trend_df = filtered[filtered['Country'].isin(isolation)].groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
        fig_line = px.line(trend_df, x="Year", y="AverageTemperature", color="Country", template="plotly_dark")
        fig_line.update_traces(line=dict(width=3))
        fig_line.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(gridcolor='rgba(255,255,255,0.05)', zeroline=False)
        )
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.warning("PLEASE SELECT TARGET SIGNALS IN THE CONTROL PANEL.")

st.markdown("<div style='text-align:center; padding:40px; color:#333; font-size:0.7rem; letter-spacing:5px;'>CONNECTION ENCRYPTED // AES-256 // LOCALHOST:CORE</div>", unsafe_allow_html=True)