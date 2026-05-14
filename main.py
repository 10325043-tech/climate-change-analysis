import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CORE: TERMINAL 2026", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        height: 100vh;
        margin: 0;
        padding: 0;
        overflow: hidden !important;
        background-color: #000;
        color: #00FF00;
        font-family: 'Share Tech Mono', monospace;
    }
    
    .stApp {
        background: radial-gradient(circle, rgba(0,20,0,1) 0%, rgba(0,0,0,1) 100%);
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* Landing Page - No scrolling */
    .hero-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100vw;
        border: 20px solid rgba(0, 255, 0, 0.1);
        box-sizing: border-box;
    }

    .glitch-title {
        font-size: 10vw;
        font-weight: bold;
        text-transform: uppercase;
        margin: 0;
        color: #fff;
        text-shadow: 0.05em 0 0 #00fffc, -0.03em -0.04em 0 #fc00ff, 0.025em 0.04em 0 #fffc00;
        animation: glitch 725ms infinite;
    }

    @keyframes glitch {
        0% { text-shadow: 0.05em 0 0 #00fffc, -0.03em -0.04em 0 #fc00ff, 0.025em 0.04em 0 #fffc00; }
        15% { text-shadow: 0.05em 0 0 #00fffc, -0.03em -0.04em 0 #fc00ff, 0.025em 0.04em 0 #fffc00; }
        16% { text-shadow: -0.05em -0.025em 0 #00fffc, 0.025em 0.035em 0 #fc00ff, -0.05em -0.05em 0 #fffc00; }
        49% { text-shadow: -0.05em -0.025em 0 #00fffc, 0.025em 0.035em 0 #fc00ff, -0.05em -0.05em 0 #fffc00; }
        50% { text-shadow: 0.05em 0.035em 0 #00fffc, 0.03em 0 0 #fc00ff, 0 -0.04em 0 #fffc00; }
        99% { text-shadow: 0.05em 0.035em 0 #00fffc, 0.03em 0 0 #fc00ff, 0 -0.04em 0 #fffc00; }
        100% { text-shadow: -0.05em 0 0 #00fffc, -0.025em -0.04em 0 #fc00ff, -0.04em -0.035em 0 #fffc00; }
    }

    /* Sector Selection */
    .selection-container {
        padding: 40px;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .sector-card {
        border: 1px solid #00FF00;
        background: rgba(0, 40, 0, 0.3);
        border-radius: 4px;
        height: 350px;
        position: relative;
        overflow: hidden;
        margin-bottom: 10px;
    }

    .sector-img {
        width: 100%;
        height: 220px;
        object-fit: cover;
        opacity: 0.7;
        filter: grayscale(100%) sepia(100%) hue-rotate(90deg);
    }

    .sector-card:hover .sector-img {
        filter: none;
        opacity: 1;
    }

    /* Dashboard Elements */
    .stat-card {
        background: rgba(0, 20, 0, 0.8);
        border: 1px solid #00FF00;
        padding: 20px;
        margin-bottom: 10px;
        text-align: center;
    }

    .flag-icon {
        width: 60px;
        height: 40px;
        object-fit: cover;
        margin-bottom: 10px;
        border: 1px solid #555;
    }

    .stButton>button {
        width: 100%;
        background: transparent !important;
        border: 1px solid #00FF00 !important;
        color: #00FF00 !important;
        font-family: 'Share Tech Mono', monospace;
        border-radius: 0;
        text-transform: uppercase;
    }

    .stButton>button:hover {
        background: #00FF00 !important;
        color: #000 !important;
        box-shadow: 0 0 15px #00FF00;
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'continent' not in st.session_state:
    st.session_state.continent = None

# Using High-res CDN for flags to ensure cross-platform compatibility
FLAG_BASE = "https://flagcdn.com/w160/"
COUNTRY_MAP = {
    "Vietnam": "vn", "Thailand": "th", "China": "cn", "India": "in", "Japan": "jp",
    "Germany": "de", "France": "fr", "Greece": "gr", "Portugal": "pt", "Spain": "es",
    "Brazil": "br", "United States": "us", "Canada": "ca", "Mexico": "mx",
    "Egypt": "eg", "Nigeria": "ng", "South Africa": "za", "Mali": "ml"
}

REGION_DATA = {
    "EUROPE": ['Germany', 'France', 'Greece', 'Portugal', 'Spain', 'United Kingdom', 'Italy', 'Norway'],
    "ASIA": ['Vietnam', 'Thailand', 'China', 'India', 'Japan', 'South Korea', 'Singapore'],
    "AMERICAS": ['United States', 'Canada', 'Mexico', 'Brazil', 'Argentina', 'Chile'],
    "AFRICA": ['Egypt', 'Nigeria', 'South Africa', 'Mali', 'Kenya', 'Ethiopia']
}

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
        df['dt'] = pd.to_datetime(df['dt'])
        df['Year'] = df['dt'].dt.year
        df = df.dropna(subset=['AverageTemperature'])
        return df
    except: return pd.DataFrame()

data = load_data()

# --- PAGE 1: HERO ---
if st.session_state.page == 'home':
    st.markdown("""
        <div class="hero-section">
            <div class="glitch-title">CLIMATE QUEST</div>
            <div style="font-size: 1.5rem; letter-spacing: 0.5rem; margin: 20px 0 50px 0;">SYSTEM STATUS: ONLINE // 2026</div>
        </div>
    """, unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1.5, 1, 1.5])
    with c2:
        if st.button("INITIALIZE CONNECTION"):
            st.session_state.page = 'selection'
            st.rerun()

# --- PAGE 2: SELECTION ---
elif st.session_state.page == 'selection':
    st.markdown('<div class="selection-container">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; margin-bottom:50px;'>GEOGRAPHIC SECTOR UPLINK</h1>", unsafe_allow_html=True)
    
    sectors = [
        ("ASIA", "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=800"),
        ("EUROPE", "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=800"),
        ("AMERICAS", "https://images.unsplash.com/photo-1449034446853-66c86144b0ad?w=800"),
        ("AFRICA", "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=800")
    ]
    
    cols = st.columns(4)
    for i, (name, img) in enumerate(sectors):
        with cols[i]:
            st.markdown(f"""
                <div class="sector-card">
                    <img src="{img}" class="sector-img">
                    <div style="padding:15px; text-align:center;">
                        <h2 style="margin:0; color:#00FF00;">{name}</h2>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"CONNECT {name}"):
                st.session_state.continent = name
                st.session_state.page = 'dashboard'
                st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("DISCONNECT"):
        st.session_state.page = 'home'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 3: DASHBOARD ---
elif st.session_state.page == 'dashboard':
    st.markdown("""<style>html, body, [data-testid="stAppViewContainer"] { overflow-y: auto !important; height: auto !important; }</style>""", unsafe_allow_html=True)
    
    # Sidebar-like top bar
    t1, t2 = st.columns([4, 1])
    with t1:
        st.markdown(f"<h1 style='color:#00FF00; margin: 20px;'>{st.session_state.continent} SENSOR FEED</h1>", unsafe_allow_html=True)
    with t2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("TERMINATE SCAN"):
            st.session_state.page = 'selection'
            st.rerun()

    if not data.empty:
        c_list = REGION_DATA[st.session_state.continent]
        df_sub = data[data['Country'].isin(c_list)]
        
        # Dashboard Grid
        col_main, col_side = st.columns([2.5, 1])
        
        with col_main:
            scope = st.session_state.continent.lower() if st.session_state.continent != "AMERICAS" else "north america"
            latest_stats = df_sub.groupby('Country')['AverageTemperature'].mean().reset_index()
            
            fig_map = px.choropleth(latest_stats, locations="Country", locationmode='country names',
                                    color="AverageTemperature", color_continuous_scale="Viridis",
                                    scope=scope, template="plotly_dark")
            fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=600, paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_map, use_container_width=True)
            
            st.markdown("### HISTORICAL ANALYTICS")
            selected_c = st.multiselect("ISOLATE SIGNALS", c_list, default=[c_list[0]])
            if selected_c:
                line_data = df_sub[df_sub['Country'].isin(selected_c)].groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
                fig_line = px.line(line_data, x="Year", y="AverageTemperature", color="Country",
                                   template="plotly_dark", color_discrete_sequence=px.colors.qualitative.Plotly)
                fig_line.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_line, use_container_width=True)

        with col_side:
            st.markdown("<h3 style='text-align:center;'>TOP ANOMALIES</h3>", unsafe_allow_html=True)
            top_countries = latest_stats.sort_values('AverageTemperature', ascending=False).head(3)
            
            for _, row in top_countries.iterrows():
                c_name = row['Country']
                code = COUNTRY_MAP.get(c_name, "un")
                st.markdown(f"""
                    <div class="stat-card">
                        <img src="{FLAG_BASE}{code}.png" class="flag-icon">
                        <div style="font-size:1.2rem; font-weight:bold;">{c_name.upper()}</div>
                        <div style="font-size:2.5rem; color:#ff4b4b;">{row['AverageTemperature']:.1f}°C</div>
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown("<hr style='border-color:#00FF00;'>", unsafe_allow_html=True)
            st.warning("WARNING: THERMAL DATA IRREGULARITY DETECTED IN UPPER STRATOSPHERE")

st.markdown("<div style='position:fixed; bottom:10px; width:100%; text-align:center; font-size:0.7rem; color:#555;'>ENCRYPTED CHANNEL SECURED // AES-256</div>", unsafe_allow_html=True)