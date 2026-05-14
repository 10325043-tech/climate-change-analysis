import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- ADVANCED SYSTEM ARCHITECTURE ---
st.set_page_config(
    page_title="NEURAL CLIMATE TERMINAL v3.0",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- THE "WOW" ENGINE (CSS & JAVASCRIPT) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Space+Grotesk:wght@300;400;700&display=swap');

    :root {
        --glow-cyan: #00ffff;
        --glow-magenta: #ff00ff;
        --void-black: #030305;
        --matrix-green: #00ff41;
    }

    /* Cinematic Reset */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: var(--void-black);
        color: #fff;
        font-family: 'Space Grotesk', sans-serif;
    }

    /* HYPER-INTERACTIVE BACKGROUND (CSS Animation) */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0a1a2f 0%, #030305 100%);
    }
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: url('https://www.transparenttextures.com/patterns/stardust.png');
        opacity: 0.2;
        pointer-events: none;
    }

    /* THE GLITCH HERO UNIT */
    .hero-container {
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        perspective: 1000px;
    }

    .title-h1 {
        font-family: 'Syncopate', sans-serif;
        font-size: 8vw;
        font-weight: 700;
        letter-spacing: -2px;
        line-height: 0.8;
        background: linear-gradient(to bottom, #fff 30%, var(--glow-cyan) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 40px rgba(0, 255, 255, 0.4));
        margin: 0;
        animation: float 6s ease-in-out infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0) rotateX(0deg); }
        50% { transform: translateY(-20px) rotateX(5deg); }
    }

    /* CYBERPUNK BUTTONS */
    .stButton>button {
        position: relative;
        background: transparent !important;
        border: 1px solid var(--glow-cyan) !important;
        color: var(--glow-cyan) !important;
        font-family: 'Syncopate', sans-serif !important;
        padding: 1.5rem 3rem !important;
        text-transform: uppercase !important;
        letter-spacing: 5px !important;
        overflow: hidden;
        transition: 0.4s cubic-bezier(0.19, 1, 0.22, 1) !important;
        border-radius: 0 !important;
    }

    .stButton>button:hover {
        background: var(--glow-cyan) !important;
        color: black !important;
        box-shadow: 0 0 50px var(--glow-cyan), inset 0 0 20px rgba(0,0,0,0.5);
    }

    .stButton>button::after {
        content: "";
        position: absolute;
        top: -50%; left: -50%; width: 200%; height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.2), transparent);
        transform: rotate(45deg);
        transition: 0.6s;
    }

    .stButton>button:hover::after {
        left: 100%;
    }

    /* DATA CARD HUD */
    .hud-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(0, 255, 255, 0.1);
        border-left: 5px solid var(--glow-cyan);
        padding: 20px;
        backdrop-filter: blur(10px);
        margin-bottom: 15px;
    }

    /* STREAMLIT ELEMENT OVERRIDES */
    .stSelectbox, .stSlider, .stMultiSelect {
        background: rgba(0,0,0,0.4);
        border-radius: 0px !important;
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- QUANTUM DATA ENGINE ---
if 'flow_state' not in st.session_state: st.session_state.flow_state = 'init'

@st.cache_data
def fetch_master_data():
    try:
        df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
        df['dt'] = pd.to_datetime(df['dt'])
        df['Year'] = df['dt'].dt.year
        return df.dropna(subset=['AverageTemperature'])
    except:
        return pd.DataFrame()

master_df = fetch_master_data()

# Robust Continent Logic
CONTINENT_DB = {
    "EUROPE": ["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom"],
    "ASIA": ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"],
    "AFRICA": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Cape Verde", "Central African Republic", "Chad", "Comoros", "Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"],
    "AMERICAS": ["Antigua and Barbuda", "Argentina", "Bahamas", "Barbados", "Belize", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "Ecuador", "El Salvador", "Grenada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Suriname", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"],
    "OCEANIA": ["Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]
}

# --- SCREEN 1: THE NEXUS (LANDING) ---
if st.session_state.flow_state == 'init':
    st.markdown("""
        <div class="hero-container">
            <div style="font-size: 0.7rem; letter-spacing: 25px; color: var(--glow-cyan); margin-bottom: 30px; opacity: 0.6;">
                ESTABLISHING NEURAL LINK...
            </div>
            <h1 class="title-h1">NEURAL<br>CLIMATE</h1>
            <div style="margin-top: 40px; border-left: 2px solid var(--glow-cyan); padding-left: 20px;">
                <p style="color: #666; font-family: 'Space Grotesk'; letter-spacing: 3px; font-size: 0.9rem;">
                    GLOBAL THERMAL ANALYTICS SYSTEM <br>
                    VERSION 3.0.4 [BUILD_QUANTUM]
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    _, btn_col, _ = st.columns([1, 0.6, 1])
    with btn_col:
        if st.button("EXECUTE SYSTEM"):
            st.session_state.flow_state = 'active'
            st.rerun()

# --- SCREEN 2: THE WAR ROOM (DASHBOARD) ---
elif st.session_state.flow_state == 'active':
    # Top HUD Bar
    h1, h2 = st.columns([4, 1])
    with h1:
        st.markdown(f"<h2 style='font-family:Syncopate; letter-spacing:10px; color:var(--glow-cyan);'>NEURAL_WAR_ROOM</h2>", unsafe_allow_html=True)
    with h2:
        if st.button("TERMINATE"):
            st.session_state.flow_state = 'init'
            st.rerun()

    # Main Command Interface
    c_left, c_mid, c_right = st.columns([1, 2.5, 1])

    with c_left:
        st.markdown("### COMMANDS")
        with st.container():
            st.markdown("<div class='hud-card'>", unsafe_allow_html=True)
            active_sector = st.radio("SECTOR TARGETING", list(CONTINENT_DB.keys()))
            target_countries = CONTINENT_DB[active_sector]
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='hud-card'>", unsafe_allow_html=True)
            selected_nodes = st.multiselect("ISOLATE NODES", target_countries, default=target_countries[:1])
            time_frame = st.slider("TEMPORAL WINDOW", 1850, 2013, (1980, 2013))
            st.markdown("</div>", unsafe_allow_html=True)

    with c_mid:
        # Data Filtering
        mask = (master_df['Country'].isin(target_countries)) & \
               (master_df['Year'] >= time_frame[0]) & \
               (master_df['Year'] <= time_frame[1])
        df_active = master_df[mask]
        
        map_stats = df_active.groupby('Country')['AverageTemperature'].mean().reset_index()

        # 3D GLOBE WITH HUD OVERLAY
        fig_globe = px.choropleth(
            map_stats, locations="Country", locationmode='country names',
            color="AverageTemperature", color_continuous_scale="Plasma",
            template="plotly_dark"
        )
        fig_globe.update_geos(
            projection_type="orthographic",
            showocean=True, oceancolor="#030305",
            showcountries=True, countrycolor="rgba(0, 255, 255, 0.3)",
            bgcolor='rgba(0,0,0,0)'
        )
        fig_globe.update_layout(
            height=750, margin={"r":0,"t":0,"l":0,"b":0},
            paper_bgcolor='rgba(0,0,0,0)',
            coloraxis_colorbar=dict(
                title="TEMP", thickness=15, len=0.4, 
                bgcolor="rgba(0,0,0,0.5)", tickfont=dict(color="cyan")
            )
        )
        st.plotly_chart(fig_globe, use_container_width=True)

    with c_right:
        st.markdown("### TELEMETRY")
        peaks = map_stats.sort_values('AverageTemperature', ascending=False).head(5)
        for i, row in peaks.iterrows():
            st.markdown(f"""
                <div class="hud-card" style="border-left-color: var(--glow-magenta);">
                    <small style="color: var(--glow-magenta); font-size: 0.6rem;">NODE_0{i}_CRITICAL</small>
                    <div style="font-size: 1.2rem; font-weight: 700;">{row['Country']}</div>
                    <div style="font-size: 1.5rem; color: #fff;">{row['AverageTemperature']:.2f}°C</div>
                </div>
            """, unsafe_allow_html=True)

    # Bottom Stream
    st.markdown("---")
    if selected_nodes:
        st.markdown("### SIGNAL WAVEFORM ANALYSIS")
        df_line = df_active[df_active['Country'].isin(selected_nodes)].groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
        fig_line = px.line(df_line, x="Year", y="AverageTemperature", color="Country", template="plotly_dark")
        fig_line.update_traces(line=dict(width=3))
        fig_line.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0.1)',
            xaxis=dict(showgrid=False, color="cyan"),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)", color="cyan")
        )
        st.plotly_chart(fig_line, use_container_width=True)

# Footer Info
st.markdown("""
    <div style="position: fixed; bottom: 10px; right: 10px; font-size: 0.6rem; color: #333; letter-spacing: 5px;">
        SECURED BY NEURAL-GRID | ENCRYPTED | 2026
    </div>
""", unsafe_allow_html=True)