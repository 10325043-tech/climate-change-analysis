import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- ADVANCED SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="TERMINAL X: CLIMATE ENGINE",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for high-end cinematic visuals and interactive UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap');

    :root {
        --neon-blue: #00f3ff;
        --neon-purple: #bc13fe;
        --deep-bg: #030303;
        --glitch-red: rgba(255,0,80,0.8);
    }

    html, body, [data-testid="stAppViewContainer"] {
        background-color: var(--deep-bg);
        color: white;
        font-family: 'Space Mono', monospace;
        overflow-x: hidden;
    }

    /* Cinematic Landing Page Overlay */
    .hero-wrapper {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background: radial-gradient(circle at center, rgba(0, 243, 255, 0.1) 0%, transparent 70%);
        position: relative;
    }

    .main-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 8vw;
        font-weight: 700;
        letter-spacing: -2px;
        line-height: 1;
        margin: 0;
        background: linear-gradient(to bottom, #fff 40%, #555 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        position: relative;
        z-index: 10;
    }

    .sub-glitch {
        font-size: 1.2rem;
        letter-spacing: 12px;
        text-transform: uppercase;
        color: var(--neon-blue);
        margin-top: 10px;
        text-shadow: 0 0 10px var(--neon-blue);
    }

    /* Interactive Sector Image Buttons */
    .img-btn-frame {
        position: relative;
        width: 100%;
        height: 400px;
        border: 1px solid rgba(255,255,255,0.1);
        overflow: hidden;
        transition: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
    }

    .img-btn-frame img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: grayscale(1) brightness(0.5);
        transition: 0.8s;
    }

    .img-btn-frame:hover {
        border-color: var(--neon-blue);
        box-shadow: 0 0 40px rgba(0, 243, 255, 0.3);
    }

    .img-btn-frame:hover img {
        filter: grayscale(0) scale(1.1);
    }

    .sector-label {
        position: absolute;
        bottom: 20px;
        left: 20px;
        font-family: 'Syncopate', sans-serif;
        font-size: 1.5rem;
        color: white;
        text-shadow: 2px 2px 4px black;
        z-index: 5;
    }

    /* Dashboard Widgets */
    .stSlider > div > div > div > div {
        background-color: var(--neon-blue) !important;
    }

    .stMultiSelect div[data-baseweb="select"] {
        background-color: rgba(255,255,255,0.05) !important;
        border: 1px solid var(--neon-blue) !important;
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- APP STATE LOGIC ---
if 'view' not in st.session_state:
    st.session_state.view = 'hero'
if 'selected_sector' not in st.session_state:
    st.session_state.selected_sector = None

@st.cache_data
def load_climate_engine():
    try:
        df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
        df['dt'] = pd.to_datetime(df['dt'])
        df['Year'] = df['dt'].dt.year
        return df.dropna(subset=['AverageTemperature'])
    except:
        return pd.DataFrame()

data = load_climate_engine()

# Region Config
SECTORS = {
    "ASIA": {
        "src": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=1000",
        "list": ["Vietnam", "Thailand", "China", "India", "Japan", "South Korea"]
    },
    "EUROPE": {
        "src": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=1000",
        "list": ["Germany", "France", "Italy", "Spain", "United Kingdom", "Norway"]
    },
    "AMERICAS": {
        "src": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=1000",
        "list": ["United States", "Canada", "Brazil", "Mexico", "Argentina"]
    },
    "AFRICA": {
        "src": "https://images.unsplash.com/photo-1523805081446-ed9a7bb89973?w=1000",
        "list": ["Egypt", "Nigeria", "South Africa", "Kenya", "Mali"]
    }
}

# --- SCREEN 1: THE HERO ---
if st.session_state.view == 'hero':
    st.markdown("""
        <div class="hero-wrapper">
            <div class="sub-glitch">GLOBAL_THERMAL_ENGINE</div>
            <h1 class="main-title">TERMINAL<br>X-2026</h1>
            <div style="margin-top: 40px; color:rgba(255,255,255,0.4); font-size:0.8rem; letter-spacing:5px;">
                DECRYPTING ENVIRO-DATA... 100% COMPLETE
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("INITIALIZE UPLINK", use_container_width=True):
            st.session_state.view = 'selection'
            st.rerun()

# --- SCREEN 2: INTERACTIVE SECTOR SELECTION ---
elif st.session_state.view == 'selection':
    st.markdown("<h2 style='text-align:center; font-family:Syncopate; margin-top:50px;'>SELECT OPERATIONAL SECTOR</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#555;'>CLICK IMAGE TO TARGET COORDINATES</p>", unsafe_allow_html=True)
    
    cols = st.columns(2)
    
    # Render Asia & Europe
    for i, (name, content) in enumerate(list(SECTORS.items())[:2]):
        with cols[i]:
            st.markdown(f"""
                <div class="img-btn-frame">
                    <img src="{content['src']}">
                    <div class="sector-label">{name}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"LOCK {name}", use_container_width=True):
                st.session_state.selected_sector = name
                st.session_state.view = 'dashboard'
                st.rerun()

    # Render Americas & Africa
    cols2 = st.columns(2)
    for i, (name, content) in enumerate(list(SECTORS.items())[2:]):
        with cols2[i]:
            st.markdown(f"""
                <div class="img-btn-frame">
                    <img src="{content['src']}">
                    <div class="sector-label">{name}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"LOCK {name}", use_container_width=True):
                st.session_state.selected_sector = name
                st.session_state.view = 'dashboard'
                st.rerun()

# --- SCREEN 3: PROFESSIONAL DASHBOARD ---
elif st.session_state.view == 'dashboard':
    st.markdown("<style>html, body, [data-testid='stAppViewContainer'] { overflow-y: auto !important; }</style>", unsafe_allow_html=True)
    
    # NAV BAR
    n1, n2 = st.columns([5, 1])
    n1.markdown(f"<h1>📡 {st.session_state.selected_sector} CORE DATA</h1>", unsafe_allow_html=True)
    if n2.button("TERMINATE"):
        st.session_state.view = 'selection'
        st.rerun()

    sector_cfg = SECTORS[st.session_state.selected_sector]
    df_raw = data[data['Country'].isin(sector_cfg['list'])]

    # INTEGRATED FILTERS (Top Bar)
    st.markdown("<div style='background:rgba(255,255,255,0.03); padding:20px; border:1px solid #222; margin-bottom:20px;'>", unsafe_allow_html=True)
    f1, f2 = st.columns([1, 1])
    with f1:
        years = st.slider("SELECT TIMELINE RANGE", int(df_raw['Year'].min()), int(df_raw['Year'].max()), (1950, 2013))
    with f2:
        countries = st.multiselect("ISOLATE NATIONAL SIGNALS", sector_cfg['list'], default=sector_cfg['list'][:2])
    st.markdown("</div>", unsafe_allow_html=True)

    # DATA SLICING
    filtered = df_raw[(df_raw['Year'] >= years[0]) & (df_raw['Year'] <= years[1])]
    
    # VISUALIZATION GRID
    m1, m2 = st.columns([2, 1])
    
    with m1:
        st.markdown("### SPATIAL HEATMAP")
        map_df = filtered.groupby('Country')['AverageTemperature'].mean().reset_index()
        scope = st.session_state.selected_sector.lower() if st.session_state.selected_sector != "AMERICAS" else "north america"
        
        fig_map = px.choropleth(
            map_df, locations="Country", locationmode='country names',
            color="AverageTemperature", color_continuous_scale="Turbo",
            scope=scope, template="plotly_dark"
        )
        fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=500, paper_bgcolor='rgba(0,0,0,0)', geo_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_map, use_container_width=True)

    with m2:
        st.markdown("### LIVE METRICS")
        top_hot = map_df.sort_values('AverageTemperature', ascending=False).head(3)
        for _, row in top_hot.iterrows():
            st.markdown(f"""
                <div style="border-left: 5px solid var(--neon-blue); background:rgba(0,243,255,0.05); padding:25px; margin-bottom:15px;">
                    <div style="font-size:0.8rem; color:rgba(255,255,255,0.5);">SIGNAL IDENTIFIED:</div>
                    <div style="font-size:1.4rem; font-weight:bold; color:white;">{row['Country'].upper()}</div>
                    <div style="font-size:2.8rem; color:var(--neon-blue); font-family:Syncopate;">{row['AverageTemperature']:.2f}°C</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### TEMPORAL SIGNAL TRENDS")
    if countries:
        trend_data = filtered[filtered['Country'].isin(countries)].groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
        fig_trend = px.line(
            trend_data, x="Year", y="AverageTemperature", color="Country",
            template="plotly_dark", markers=True
        )
        fig_trend.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False),
            yaxis=dict(gridcolor='rgba(255,255,255,0.05)')
        )
        st.plotly_chart(fig_trend, use_container_width=True)
    else:
        st.info("Awaiting country selection for signal analysis.")

st.markdown("<p style='text-align:center; margin-top:50px; color:#222; font-size:0.7rem;'>ENCRYPTED VIA RSA-4096 // CONNECTION STABLE</p>", unsafe_allow_html=True)