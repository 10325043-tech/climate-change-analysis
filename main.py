import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time

# --- SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="QUANTUM CLIMATE TERMINAL v2.0",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- HYPER-VIBRANT STYLING ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300;500&display=swap');

    :root {
        --neon-cyan: #00f2ff;
        --neon-gold: #ffaa00;
        --deep-void: #020205;
        --terminal-green: #00ff41;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background-color: var(--deep-void);
        color: white;
        font-family: 'JetBrains Mono', monospace;
        overflow: hidden;
    }

    /* Kinetic Grid Background */
    .stApp {
        background: 
            linear-gradient(rgba(0, 242, 255, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 242, 255, 0.03) 1px, transparent 1px);
        background-size: 50px 50px;
        background-attachment: fixed;
    }

    /* GLITCH TITLE EFFECT */
    .glitch-wrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        flex-direction: column;
        height: 70vh;
    }

    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 15px;
        color: white;
        position: relative;
        text-shadow: 0 0 20px var(--neon-cyan);
        animation: glitch 3s infinite;
    }

    @keyframes glitch {
        0% { text-shadow: 2px 0 red, -2px 0 blue; }
        1% { text-shadow: -2px 0 red, 2px 0 blue; }
        2% { text-shadow: 0 0 20px var(--neon-cyan); }
    }

    /* TERMINAL LOG STYLING */
    .terminal-window {
        background: rgba(0, 0, 0, 0.7);
        border: 1px solid rgba(0, 242, 255, 0.3);
        padding: 15px;
        width: 400px;
        font-size: 0.75rem;
        color: var(--terminal-green);
        text-align: left;
        margin-top: 20px;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.1);
    }

    /* PULSING BUTTON */
    .stButton>button {
        background: transparent !important;
        color: var(--neon-cyan) !important;
        border: 2px solid var(--neon-cyan) !important;
        font-family: 'Orbitron', sans-serif !important;
        padding: 20px 40px !important;
        font-size: 1.2rem !important;
        letter-spacing: 5px !important;
        transition: 0.5s !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.2) !important;
    }

    .stButton>button:hover {
        background: var(--neon-cyan) !important;
        color: black !important;
        box-shadow: 0 0 50px var(--neon-cyan) !important;
    }

    /* GLASS CARD FOR DASHBOARD */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 2px;
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- CORE LOGIC & DATA ---
if 'state' not in st.session_state: st.session_state.state = 'intro'

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
        df['dt'] = pd.to_datetime(df['dt'])
        df['Year'] = df['dt'].dt.year
        return df.dropna(subset=['AverageTemperature'])
    except:
        return pd.DataFrame()

df_master = load_data()

# DYNAMIC CONTINENT MAPPING (No missing countries)
CONTINENT_MAP = {
    "AFRICA": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Cape Verde", "Central African Republic", "Chad", "Comoros", "Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"],
    "ASIA": ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"],
    "EUROPE": ["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom"],
    "AMERICAS": ["Antigua and Barbuda", "Argentina", "Bahamas", "Barbados", "Belize", "Bolivia", "Brazil", "Canada", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "Ecuador", "El Salvador", "Grenada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Suriname", "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"],
    "OCEANIA": ["Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]
}

# --- PAGE 1: THE REBORN LANDING PAGE ---
if st.session_state.state == 'intro':
    st.markdown("""
        <div class="glitch-wrapper">
            <div style="font-size: 0.8rem; letter-spacing: 20px; color: var(--neon-cyan); margin-bottom: 20px;">[ SATELLITE CONNECTION ESTABLISHED ]</div>
            <h1 class="main-title">QUANTUM<br>CLIMATE</h1>
            <div class="terminal-window">
                <div id="term-1">> INITIALIZING CORE... OK</div>
                <div id="term-2">> FETCHING 200+ COUNTRY SIGNALS... OK</div>
                <div id="term-3">> RESOLVING THERMAL ANOMALIES... READY</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 0.8, 1])
    with col:
        if st.button("INITIALIZE SYSTEM"):
            st.session_state.state = 'dashboard'
            st.rerun()

# --- PAGE 2: THE COMMAND CENTER (DASHBOARD) ---
elif st.session_state.state == 'dashboard':
    st.markdown("<h1 style='font-family:Orbitron; font-size: 1.5rem; color:var(--neon-cyan); letter-spacing: 5px;'>COMMAND CENTER v2.0</h1>", unsafe_allow_html=True)
    
    # HUD SECTION
    col_a, col_b, col_c = st.columns([1, 3, 1])
    
    with col_a:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        target_continent = st.selectbox("SELECT DEPLOYMENT ZONE", list(CONTINENT_MAP.keys()))
        countries_in_zone = CONTINENT_MAP[target_continent]
        selected_countries = st.multiselect("ISOLATE SIGNALS", countries_in_zone, default=countries_in_zone[:2])
        year_range = st.slider("TEMPORAL DEPTH", 1850, 2013, (1950, 2013))
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("LOGOUT"):
            st.session_state.state = 'intro'
            st.rerun()

    with col_b:
        # DATA PROCESSING
        df_filtered = df_master[(df_master['Country'].isin(countries_in_zone)) & 
                                (df_master['Year'] >= year_range[0]) & 
                                (df_master['Year'] <= year_range[1])]
        
        map_data = df_filtered.groupby('Country')['AverageTemperature'].mean().reset_index()
        
        # 3D REVOLVING GLOBE
        fig_globe = px.choropleth(
            map_data, locations="Country", locationmode='country names',
            color="AverageTemperature", color_continuous_scale="Turbo",
            template="plotly_dark"
        )
        fig_globe.update_geos(
            projection_type="orthographic",
            showocean=True, oceancolor="#020205",
            showcountries=True, countrycolor="rgba(0, 242, 255, 0.2)"
        )
        fig_globe.update_layout(
            height=700, margin={"r":0,"t":0,"l":0,"b":0},
            paper_bgcolor='rgba(0,0,0,0)',
            coloraxis_colorbar=dict(title="TEMP °C", thickness=15, len=0.5)
        )
        st.plotly_chart(fig_globe, use_container_width=True)

    with col_c:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<p style='color:var(--neon-cyan); font-size: 0.7rem;'>PEAK ANOMALIES</p>", unsafe_allow_html=True)
        top_4 = map_data.sort_values('AverageTemperature', ascending=False).head(4)
        for _, row in top_4.iterrows():
            st.metric(label=row['Country'].upper(), value=f"{row['AverageTemperature']:.2f} °C")
        st.markdown("</div>", unsafe_allow_html=True)

    # LOWER ANALYTICS
    st.markdown("---")
    if selected_countries:
        df_line = df_filtered[df_filtered['Country'].isin(selected_countries)].groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
        fig_line = px.line(df_line, x="Year", y="AverageTemperature", color="Country", 
                           title="SIGNAL TREND ANALYSIS", template="plotly_dark")
        fig_line.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_line, use_container_width=True)