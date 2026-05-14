import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- ADVANCED UI CONFIGURATION ---
st.set_page_config(
    page_title="NEURAL CLIMATE INTERFACE",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a professional, futuristic cyber-terminal aesthetic
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;500;800&display=swap');

    :root {
        --glow-color: #00f3ff;
        --bg-dark: #050505;
        --accent-red: #ff003c;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background-color: var(--bg-dark);
        color: var(--glow-color);
        font-family: 'JetBrains Mono', monospace;
    }

    /* Cinematic Scanline Overlay */
    [data-testid="stAppViewContainer"]::before {
        content: " ";
        display: block;
        position: absolute;
        top: 0; left: 0; bottom: 0; right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), 
                    linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        z-index: 2;
        background-size: 100% 4px, 3px 100%;
        pointer-events: none;
    }

    /* Landing Header */
    .glitch-title {
        font-size: 6rem;
        font-weight: 800;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 20px;
        margin-top: 15vh;
        color: white;
        text-shadow: 3px 0 var(--accent-red), -3px 0 var(--glow-color);
    }

    /* Cyber Cards */
    .sector-card {
        border: 1px solid var(--glow-color);
        background: rgba(0, 243, 255, 0.05);
        padding: 0;
        border-radius: 0px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        overflow: hidden;
        cursor: pointer;
        position: relative;
    }

    .sector-card:hover {
        background: rgba(0, 243, 255, 0.15);
        box-shadow: 0 0 30px var(--glow-color);
        transform: translateY(-10px);
    }

    .img-container {
        height: 250px;
        width: 100%;
        background-size: cover;
        background-position: center;
        filter: grayscale(1) contrast(1.2);
        border-bottom: 1px solid var(--glow-color);
    }

    .sector-card:hover .img-container {
        filter: grayscale(0) contrast(1);
    }

    /* Metric Box */
    .metric-box {
        border-left: 4px solid var(--accent-red);
        background: rgba(255, 0, 60, 0.1);
        padding: 20px;
        margin: 10px 0;
    }

    /* Streamlit Overrides */
    .stButton>button {
        width: 100%;
        border-radius: 0;
        background: transparent;
        border: 1px solid var(--glow-color);
        color: var(--glow-color);
        font-weight: bold;
        letter-spacing: 2px;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background: var(--glow-color) !important;
        color: black !important;
        box-shadow: 0 0 20px var(--glow-color);
    }

    [data-testid="stSidebar"] {
        background-color: rgba(5, 5, 5, 0.9);
        border-right: 1px solid var(--glow-color);
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- STATE CONTROLLER ---
if 'nav' not in st.session_state:
    st.session_state.nav = 'terminal'
if 'active_region' not in st.session_state:
    st.session_state.active_region = None

# --- DATA PROCESSING ---
@st.cache_data
def fetch_and_clean_data():
    try:
        df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
        df['dt'] = pd.to_datetime(df['dt'])
        df['Year'] = df['dt'].dt.year
        return df.dropna(subset=['AverageTemperature'])
    except Exception:
        return pd.DataFrame()

data = fetch_and_clean_data()

# Static Mapping for visuals
REGION_METADATA = {
    "ASIA": {
        "img": "https://images.unsplash.com/photo-1490730141103-6cac27aaab94?w=800",
        "countries": ["Vietnam", "Thailand", "China", "India", "Japan", "Indonesia"],
        "codes": {"Vietnam": "vn", "Thailand": "th", "China": "cn", "India": "in", "Japan": "jp", "Indonesia": "id"}
    },
    "EUROPE": {
        "img": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=800",
        "countries": ["Germany", "France", "Italy", "Spain", "Norway", "United Kingdom"],
        "codes": {"Germany": "de", "France": "fr", "Italy": "it", "Spain": "es", "Norway": "no", "United Kingdom": "gb"}
    },
    "AMERICAS": {
        "img": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=800",
        "countries": ["United States", "Canada", "Brazil", "Mexico", "Argentina"],
        "codes": {"United States": "us", "Canada": "ca", "Brazil": "br", "Mexico": "mx", "Argentina": "ar"}
    },
    "AFRICA": {
        "img": "https://images.unsplash.com/photo-1523805081446-ed9a7bb89973?w=800",
        "countries": ["Egypt", "Nigeria", "South Africa", "Kenya", "Morocco"],
        "codes": {"Egypt": "eg", "Nigeria": "ng", "South Africa": "za", "Kenya": "ke", "Morocco": "ma"}
    }
}

# --- VIEW 1: TERMINAL ENTRANCE ---
if st.session_state.nav == 'terminal':
    st.markdown('<div class="glitch-title">NEURAL_CLIMATE</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; opacity:0.6; letter-spacing:8px;'>SATELLITE DOWNLINK STATUS: ACTIVE</p>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([2, 1, 2])
    with c2:
        if st.button("ENTER THE GRID"):
            st.session_state.nav = 'selection'
            st.rerun()

# --- VIEW 2: SECTOR SELECTION ---
elif st.session_state.nav == 'selection':
    st.markdown("<h2 style='text-align:center; letter-spacing:10px;'>CHOOSE GEOGRAPHIC SECTOR</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 0.5px solid var(--glow-color);'>", unsafe_allow_html=True)
    
    cols = st.columns(4)
    for i, (name, meta) in enumerate(REGION_METADATA.items()):
        with cols[i]:
            st.markdown(f"""
                <div class="sector-card">
                    <div class="img-container" style="background-image: url('{meta['img']}');"></div>
                    <div style="padding: 20px; text-align: center;">
                        <h3 style="margin: 0; letter-spacing: 5px;">{name}</h3>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"CONNECT TO {name}"):
                st.session_state.active_region = name
                st.session_state.nav = 'dashboard'
                st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("TERMINATE CONNECTION"):
        st.session_state.nav = 'terminal'
        st.rerun()

# --- VIEW 3: DATA DASHBOARD ---
elif st.session_state.nav == 'dashboard':
    st.markdown("<style>html, body, [data-testid='stAppViewContainer'] { overflow-y: auto !important; }</style>", unsafe_allow_html=True)
    
    # Dashboard Header
    h1, h2 = st.columns([5, 1])
    h1.markdown(f"<h1><span style='color:var(--accent-red);'>[X]</span> SECTOR_{st.session_state.active_region} DASHBOARD</h1>", unsafe_allow_html=True)
    if h2.button("BACK TO GRID"):
        st.session_state.nav = 'selection'
        st.rerun()

    meta = REGION_METADATA[st.session_state.active_region]
    df_region = data[data['Country'].isin(meta['countries'])]

    # Sidebar Controls
    with st.sidebar:
        st.markdown("### SYSTEM PARAMS")
        year_sel = st.slider("TIMELINE RANGE", int(df_region['Year'].min()), int(df_region['Year'].max()), (1900, 2013))
        selected_targets = st.multiselect("ISOLATE SIGNALS", meta['countries'], default=meta['countries'][:2])
        st.markdown("---")
        st.info(f"Scanning {st.session_state.active_region} sector using High-Resolution thermal sensors.")

    # Data Filter
    filtered = df_region[(df_region['Year'] >= year_sel[0]) & (df_region['Year'] <= year_sel[1])]
    
    # Layout Grid
    col_map, col_stats = st.columns([2, 1])
    
    with col_map:
        st.markdown("#### SATELLITE HEATMAP")
        map_stats = filtered.groupby('Country')['AverageTemperature'].mean().reset_index()
        scope_map = st.session_state.active_region.lower() if st.session_state.active_region != "AMERICAS" else "north america"
        
        fig_map = px.choropleth(
            map_stats, locations="Country", locationmode='country names',
            color="AverageTemperature", color_continuous_scale="Plasma",
            scope=scope_map, template="plotly_dark"
        )
        fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=500, paper_bgcolor='rgba(0,0,0,0)', geo_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_map, use_container_width=True)

    with col_stats:
        st.markdown("#### CRITICAL ANOMALIES")
        top_hot = map_stats.sort_values('AverageTemperature', ascending=False).head(3)
        for _, row in top_hot.iterrows():
            code = meta['codes'].get(row['Country'], "un")
            st.markdown(f"""
                <div class="metric-box">
                    <img src="https://flagcdn.com/w80/{code}.png" style="width: 30px; border: 1px solid #555;">
                    <span style="font-size: 1rem; margin-left: 10px;">{row['Country'].upper()}</span>
                    <div style="font-size: 2.2rem; font-weight: 800; color: white;">{row['AverageTemperature']:.2f}°C</div>
                    <div style="font-size: 0.7rem; color: var(--accent-red);">SENSOR STATUS: CRITICAL</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Advanced Line Chart
    st.markdown("#### TEMPORAL ANALYSIS")
    if selected_targets:
        line_data = filtered[filtered['Country'].isin(selected_targets)].groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
        fig_line = go.Figure()
        
        for country in selected_targets:
            c_data = line_data[line_data['Country'] == country]
            fig_line.add_trace(go.Scatter(
                x=c_data['Year'], y=c_data['AverageTemperature'],
                mode='lines+markers', name=country,
                line=dict(width=2),
                marker=dict(size=4)
            ))
            
        fig_line.update_layout(
            template="plotly_dark",
            height=450,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.warning("Please select at least one signal in the sidebar to visualize trends.")

    st.markdown("<p style='text-align:center; color:#444; padding: 20px;'>SECURE UPLINK // NEURAL INTERFACE ENCRYPTION ENABLED</p>", unsafe_allow_html=True)