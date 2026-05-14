import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- PREMIUM SYSTEM CONFIG ---
st.set_page_config(
    page_title="AURORA CLIMATE SYSTEMS",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- THE "LUXURY-TECH" STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;300;700&family=Montserrat:wght@700&display=swap');

    :root {
        --accent: #00d4ff;
        --glass: rgba(255, 255, 255, 0.03);
        --border: rgba(255, 255, 255, 0.1);
    }

    /* Reset to Deep Space */
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top, #0a1128 0%, #000205 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    /* MONOLITH LANDING */
    .monolith-card {
        background: var(--glass);
        backdrop-filter: blur(20px);
        border: 1px solid var(--border);
        padding: 60px;
        text-align: center;
        border-radius: 10px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.5);
        margin-top: 10vh;
    }

    .hero-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 5rem;
        font-weight: 700;
        letter-spacing: -2px;
        background: linear-gradient(180deg, #fff 0%, rgba(255,255,255,0.4) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }

    /* PREMIUM BUTTONS */
    .stButton>button {
        background: white !important;
        color: black !important;
        border: none !important;
        font-weight: 700 !important;
        font-family: 'Inter', sans-serif !important;
        padding: 15px 40px !important;
        border-radius: 50px !important;
        letter-spacing: 1px !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0, 212, 255, 0.4) !important;
        background: var(--accent) !important;
    }

    /* DATA TILES */
    .stat-box {
        background: var(--glass);
        border-top: 2px solid var(--accent);
        padding: 25px;
        border-radius: 4px;
        margin-bottom: 20px;
    }

    /* Hide Streamlit UI */
    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- DATA KERNEL ---
if 'auth_level' not in st.session_state: st.session_state.auth_level = 0

@st.cache_data
def get_clean_data():
    try:
        df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
        df['dt'] = pd.to_datetime(df['dt'])
        df['Year'] = df['dt'].dt.year
        return df.dropna(subset=['AverageTemperature'])
    except:
        return pd.DataFrame({'Country': ['Global'], 'Year': [2024], 'AverageTemperature': [15.0]})

df_main = get_clean_data()

# Clean Continent logic
ZONE_DB = {
    "EUROPEAN_UNION": ["France", "Germany", "Italy", "Spain", "Sweden", "Netherlands", "Poland"],
    "ASIA_PACIFIC": ["Vietnam", "Japan", "China", "India", "Australia", "Thailand", "Singapore"],
    "AMERICAS": ["United States", "Canada", "Brazil", "Mexico", "Argentina", "Chile"],
    "AFRICA_ME": ["South Africa", "Egypt", "Nigeria", "Saudi Arabia", "United Arab Emirates"]
}

# --- VIEW 1: THE MONOLITH (LANDING) ---
if st.session_state.auth_level == 0:
    _, center_col, _ = st.columns([1, 2, 1])
    with center_col:
        st.markdown("""
            <div class="monolith-card">
                <p style="letter-spacing: 10px; color: var(--accent); font-weight: 300; font-size: 0.8rem;">AURORA CLIMATE ARCHIVE</p>
                <h1 class="hero-title">PRECISION<br>DATA.</h1>
                <p style="color: #888; font-size: 1.1rem; margin-top: 20px; margin-bottom: 40px; font-weight: 300;">
                    Experience the evolution of our planet through <br> high-fidelity thermal telemetry.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns([1,1,1])
        with c2:
            if st.button("ENTER ARCHIVE"):
                st.session_state.auth_level = 1
                st.rerun()

# --- VIEW 2: THE ARCHIVE (DASHBOARD) ---
else:
    # Top Glass Nav
    st.markdown("""
        <div style="padding: 10px; border-bottom: 1px solid var(--border); margin-bottom: 40px; display: flex; justify-content: space-between;">
            <span style="font-weight: 700; letter-spacing: 2px;">AURORA // SYSTEM_ACTIVE</span>
        </div>
    """, unsafe_allow_html=True)

    col_side, col_viz = st.columns([1, 3])

    with col_side:
        st.markdown("<p style='color:var(--accent); font-size: 0.8rem;'>PARAMETERS</p>", unsafe_allow_html=True)
        selected_zone = st.selectbox("ZONE SELECTION", list(ZONE_DB.keys()))
        
        available_countries = ZONE_DB[selected_zone]
        target_countries = st.multiselect("ISOLATE ENTITIES", available_countries, default=available_countries[:2])
        
        timeline = st.slider("TEMPORAL SPAN", 1850, 2013, (1960, 2013))
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("EXIT"):
            st.session_state.auth_level = 0
            st.rerun()

    with col_viz:
        # Data Filter
        mask = (df_main['Country'].isin(available_countries)) & \
               (df_main['Year'] >= timeline[0]) & \
               (df_main['Year'] <= timeline[1])
        df_viz = df_main[mask].groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()

        # HIGH-END AREA CHART
        fig = go.Figure()
        
        # We only show lines for target countries to keep it clean
        colors = ['#00d4ff', '#ff00ff', '#00ff41', '#ffff00']
        for i, country in enumerate(target_countries):
            country_data = df_viz[df_viz['Country'] == country]
            fig.add_trace(go.Scatter(
                x=country_data['Year'], y=country_data['AverageTemperature'],
                name=country, fill='tozeroy', line=dict(width=3, color=colors[i % len(colors)]),
                mode='lines'
            ))

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=500,
            hovermode="x unified",
            margin=dict(l=0, r=0, t=20, b=0),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(gridcolor='rgba(255,255,255,0.05)', zeroline=False)
        
        st.plotly_chart(fig, use_container_width=True)

        # Comparative Metrics
        st.markdown("<br>", unsafe_allow_html=True)
        m1, m2, m3 = st.columns(3)
        
        avg_temp = df_viz['AverageTemperature'].mean()
        max_temp = df_viz['AverageTemperature'].max()
        growth = df_viz[df_viz['Year'] == timeline[1]]['AverageTemperature'].mean() - \
                 df_viz[df_viz['Year'] == timeline[0]]['AverageTemperature'].mean()

        with m1:
            st.markdown(f"<div class='stat-box'><small>MEAN TEMPERATURE</small><h2>{avg_temp:.2f}°C</h2></div>", unsafe_allow_html=True)
        with m2:
            st.markdown(f"<div class='stat-box'><small>PEAK RECORDED</small><h2>{max_temp:.2f}°C</h2></div>", unsafe_allow_html=True)
        with m3:
            st.markdown(f"<div class='stat-box' style='border-top-color: #ff4b4b;'><small>DELTA CHANGE</small><h2>+{growth:.2f}°C</h2></div>", unsafe_allow_html=True)

    # Minimalist Footer
    st.markdown("""
        <div style="margin-top: 100px; text-align: center; color: #444; font-size: 0.7rem; letter-spacing: 3px;">
            DESIGNED FOR HIGH-FIDELITY ANALYSIS // NO-JS KERNEL
        </div>
    """, unsafe_allow_html=True)