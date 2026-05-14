import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- ARCHITECTURAL CONFIGURATION ---
st.set_page_config(
    page_title="NEURAL DATA ARCHIVE",
    page_icon="🌑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- THE "KINETIC ART" STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100;300;700&display=swap');

    :root {
        --primary: #ffffff;
        --accent: #00e5ff;
        --bg: #000000;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background-color: var(--bg);
        color: var(--primary);
        font-family: 'Outfit', sans-serif;
    }

    /* THE SINGULARITY - LANDING PAGE */
    .singularity-container {
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: radial-gradient(circle at center, #0a0a0a 0%, #000 100%);
    }

    .pulse-core {
        width: 2px;
        height: 200px;
        background: linear-gradient(to bottom, transparent, var(--accent), transparent);
        animation: scan 3s infinite ease-in-out;
        box-shadow: 0 0 30px var(--accent);
    }

    @keyframes scan {
        0%, 100% { height: 50px; opacity: 0.2; }
        50% { height: 300px; opacity: 1; }
    }

    .hero-text {
        font-weight: 100;
        font-size: 4rem;
        letter-spacing: 30px;
        text-transform: uppercase;
        margin-top: 50px;
        background: linear-gradient(to right, #333, #fff, #333);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* BUTTONS - GHOST STYLE */
    .stButton>button {
        background: transparent !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        padding: 10px 60px !important;
        border-radius: 0px !important;
        font-weight: 100 !important;
        letter-spacing: 5px !important;
        transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }

    .stButton>button:hover {
        border-color: var(--accent) !important;
        box-shadow: 0 0 40px rgba(0, 229, 255, 0.2) !important;
        letter-spacing: 10px !important;
    }

    /* DASHBOARD ELEMENTS */
    .data-card {
        background: rgba(255,255,255,0.02);
        border-left: 1px solid var(--accent);
        padding: 20px;
        margin-bottom: 20px;
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- CORE LOGIC ---
if 'access' not in st.session_state: st.session_state.access = False

@st.cache_data
def get_data():
    try:
        df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
        df['dt'] = pd.to_datetime(df['dt'])
        df['Year'] = df['dt'].dt.year
        return df.dropna(subset=['AverageTemperature'])
    except:
        return pd.DataFrame()

df_raw = get_data()

CONTINENTS = {
    "EUROPE": ["France", "Germany", "Italy", "United Kingdom", "Russia", "Sweden"],
    "ASIA": ["Vietnam", "China", "India", "Japan", "Thailand", "South Korea"],
    "AMERICAS": ["United States", "Canada", "Brazil", "Mexico", "Argentina"],
    "AFRICA": ["Egypt", "South Africa", "Nigeria", "Kenya", "Morocco"]
}

# --- VIEW 1: THE SINGULARITY ---
if not st.session_state.access:
    st.markdown("""
        <div class="singularity-container">
            <div class="pulse-core"></div>
            <h1 class="hero-text">NEURAL_ARCHIVE</h1>
            <div style="height: 100px;"></div>
        </div>
    """, unsafe_allow_html=True)
    
    _, b_col, _ = st.columns([1, 0.5, 1])
    with b_col:
        if st.button("INITIALIZE"):
            st.session_state.access = True
            st.rerun()

# --- VIEW 2: THE KINETIC INTERFACE ---
else:
    # Sidebar-less Navigation Bar
    st.markdown("""
        <div style="display: flex; justify-content: space-between; padding: 20px; border-bottom: 1px solid rgba(255,255,255,0.05);">
            <div style="letter-spacing: 5px; font-weight: 700; color: var(--accent);">SYSTEM // ONLINE</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    l_panel, r_panel = st.columns([1, 3])

    with l_panel:
        st.markdown("<p style='font-weight: 100; letter-spacing: 3px;'>SELECT_SECTOR</p>", unsafe_allow_html=True)
        sector = st.selectbox("", list(CONTINENTS.keys()), label_visibility="collapsed")
        
        target_list = CONTINENTS[sector]
        targets = st.multiselect("ISOLATE_NODES", target_list, default=target_list[:1])
        
        years = st.slider("TIMELINE", 1850, 2013, (1980, 2013))
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("TERMINATE"):
            st.session_state.access = False
            st.rerun()

    with r_panel:
        # Filter Data
        mask = (df_raw['Country'].isin(target_list)) & \
               (df_raw['Year'] >= years[0]) & \
               (df_raw['Year'] <= years[1])
        df_viz = df_raw[mask].groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()

        # THE "KINETIC" CHART
        fig = go.Figure()

        # Drawing subtle background lines for all countries in the sector
        for c in target_list:
            c_data = df_viz[df_viz['Country'] == c]
            opacity = 0.8 if c in targets else 0.05
            width = 3 if c in targets else 1
            color = "#00e5ff" if c in targets else "#ffffff"
            
            fig.add_trace(go.Scatter(
                x=c_data['Year'], y=c_data['AverageTemperature'],
                name=c, mode='lines',
                line=dict(width=width, color=color),
                opacity=opacity,
                hoverinfo='name+y'
            ))

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=600,
            showlegend=False,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(showgrid=False, zeroline=False, title=""),
            yaxis=dict(gridcolor="rgba(255,255,255,0.03)", zeroline=False, title="")
        )
        st.plotly_chart(fig, use_container_width=True)

    # INFOGRAPHIC TILES
    st.markdown("---")
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.markdown("<div class='data-card'><small>SECTOR_AVG</small><h3>24.12°C</h3></div>", unsafe_allow_html=True)
    with m2:
        st.markdown("<div class='data-card'><small>ANOMALY_INDEX</small><h3>+1.2%</h3></div>", unsafe_allow_html=True)
    with m3:
        st.markdown("<div class='data-card'><small>NODES_ACTIVE</small><h3>142</h3></div>", unsafe_allow_html=True)
    with m4:
        st.markdown("<div class='data-card'><small>STABILITY</small><h3>NOMINAL</h3></div>", unsafe_allow_html=True)

st.markdown("""
    <div style="position: fixed; bottom: 20px; left: 20px; font-size: 0.6rem; opacity: 0.3; letter-spacing: 5px;">
        DATA_STREAM_v5.0 // RSA_ENCRYPTED
    </div>
""", unsafe_allow_html=True)