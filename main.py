import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- ARCHITECTURAL CONFIGURATION ---
st.set_page_config(
    page_title="QUANTUM CLIMATE TERMINAL",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- QUANTUM STYLING ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Space+Grotesk:wght@300;500;700&display=swap');

    :root {
        --glow: #00fff2;
        --deep-space: #050508;
        --neon-matrix: #0f0;
        --hazard: #ff003c;
    }

    html, body, [data-testid="stAppViewContainer"] {
        background-color: var(--deep-space);
        color: #ffffff;
        font-family: 'Space Grotesk', sans-serif;
    }

    /* Cinematic Background Overlay */
    .stApp {
        background: radial-gradient(circle at 50% 50%, rgba(0, 255, 242, 0.05) 0%, transparent 80%);
    }

    /* Landing Page - EXPLOSIVE DESIGN */
    .landing-hero {
        height: 90vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .quantum-title {
        font-family: 'Syncopate', sans-serif;
        font-size: 8vw;
        font-weight: 700;
        letter-spacing: -5px;
        line-height: 0.9;
        background: linear-gradient(180deg, #fff 0%, #00fff2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 30px rgba(0, 255, 242, 0.5));
        animation: pulse 4s infinite alternate;
    }

    @keyframes pulse {
        0% { transform: scale(1); filter: drop-shadow(0 0 20px rgba(0, 255, 242, 0.3)); }
        100% { transform: scale(1.02); filter: drop-shadow(0 0 50px rgba(0, 255, 242, 0.6)); }
    }

    /* Interactive Sector Grid */
    .sector-box {
        position: relative;
        height: 500px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        overflow: hidden;
        border-radius: 0px;
        transition: 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        margin-bottom: 20px;
    }

    .sector-box:hover {
        border-color: var(--glow);
        box-shadow: 0 0 60px rgba(0, 255, 242, 0.4);
        transform: scale(1.02);
        z-index: 10;
    }

    .sector-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: saturate(0) brightness(0.4);
        transition: 1s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .sector-box:hover .sector-img {
        filter: saturate(1) brightness(0.8);
        transform: scale(1.1);
    }

    .sector-overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, transparent 50%);
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        padding: 40px;
    }

    .sector-name {
        font-family: 'Syncopate', sans-serif;
        font-size: 2.5rem;
        letter-spacing: 5px;
        color: var(--glow);
        margin: 0;
    }

    /* Dashboard UI */
    .glass-panel {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 25px;
        margin-bottom: 20px;
    }

    .stButton>button {
        width: 100%;
        background: transparent !important;
        border: 1px solid var(--glow) !important;
        color: var(--glow) !important;
        font-family: 'Syncopate', sans-serif !important;
        font-size: 0.8rem !important;
        border-radius: 0px !important;
        padding: 15px !important;
        transition: 0.4s !important;
    }

    .stButton>button:hover {
        background: var(--glow) !important;
        color: #000 !important;
        box-shadow: 0 0 20px var(--glow);
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- DATA & LOGIC ENGINE ---
if 'flow' not in st.session_state:
    st.session_state.flow = 'hero'
if 'active_zone' not in st.session_state:
    st.session_state.active_zone = None

@st.cache_data
def get_master_data():
    try:
        df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
        df['dt'] = pd.to_datetime(df['dt'])
        df['Year'] = df['dt'].dt.year
        return df.dropna(subset=['AverageTemperature'])
    except:
        return pd.DataFrame()

master_df = get_master_data()

ZONE_MAP = {
    "EUROPE": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=1200",
    "ASIA": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=1200",
    "AMERICAS": "https://images.unsplash.com/photo-1449034446853-66c86144b0ad?w=1200",
    "AFRICA": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=1200",
    "OCEANIA": "https://images.unsplash.com/photo-1523482580672-f109ba8cb9be?w=1200"
}

# Accurate Continent Mapping for 100% Coverage
@st.cache_data
def get_continent_countries(zone):
    mapping = {
        "EUROPE": ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia And Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom'],
        "ASIA": ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor Leste', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen'],
        "AMERICAS": ['Antigua And Barbuda', 'Argentina', 'Bahamas', 'Barbados', 'Belize', 'Bolivia', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Grenada', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Saint Kitts And Nevis', 'Saint Lucia', 'Saint Vincent And The Grenadines', 'Suriname', 'Trinidad And Tobago', 'United States', 'Uruguay', 'Venezuela'],
        "AFRICA": ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Central African Republic', 'Chad', 'Comoros', 'Congo', 'Congo (Democratic Republic Of The)', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea Bissau', 'Ivory Coast', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome And Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Swaziland', 'Tanzia', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'],
        "OCEANIA": ['Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu']
    }
    return mapping.get(zone, [])

# --- PHASE 1: THE QUANTUM CORE ---
if st.session_state.flow == 'hero':
    st.markdown(f"""
        <div class="landing-hero">
            <div style="font-size: 0.8rem; letter-spacing: 15px; color: var(--glow); margin-bottom: 20px;">SYSTEM ARCHIVE // 2026</div>
            <h1 class="quantum-title">QUANTUM<br>CLIMATE</h1>
            <div style="margin-top: 50px;">
                <p style="opacity: 0.5; letter-spacing: 5px;">WORLD THERMAL SENSOR NETWORK IS ONLINE</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    _, btn_col, _ = st.columns([2, 1, 2])
    with btn_col:
        if st.button("OPEN TERMINAL"):
            st.session_state.flow = 'selector'
            st.rerun()

# --- PHASE 2: SECTOR TARGETING ---
elif st.session_state.flow == 'selector':
    st.markdown("<h2 style='text-align:center; font-family:Syncopate; margin: 40px 0;'>SELECT DEPLOYMENT ZONE</h2>", unsafe_allow_html=True)
    
    # 5-Sector Grid
    row1_cols = st.columns(3)
    row2_cols = st.columns(2)
    all_cols = row1_cols + row2_cols
    
    for i, (name, img) in enumerate(ZONE_MAP.items()):
        with all_cols[i]:
            st.markdown(f"""
                <div class="sector-box">
                    <img src="{img}" class="sector-img">
                    <div class="sector-overlay">
                        <p style="color:white; opacity:0.6; margin:0; font-size:0.7rem;">GEOGRAPHIC DATA STREAM</p>
                        <h3 class="sector-name">{name}</h3>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"ENGAGE {name}"):
                st.session_state.active_zone = name
                st.session_state.flow = 'dashboard'
                st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("BACK TO CORE"):
        st.session_state.flow = 'hero'
        st.rerun()

# --- PHASE 3: THE COMMAND CENTER ---
elif st.session_state.flow == 'dashboard':
    st.markdown("<style>html, body, [data-testid='stAppViewContainer'] { overflow-y: auto !important; }</style>", unsafe_allow_html=True)
    
    # Header
    h_col1, h_col2 = st.columns([5, 1])
    h_col1.markdown(f"<h1 style='font-family:Syncopate; color:var(--glow);'>ACCESSING: {st.session_state.active_zone}_SECTOR</h1>", unsafe_allow_html=True)
    if h_col2.button("EXIT"):
        st.session_state.flow = 'selector'
        st.rerun()

    # Dynamic Data Load
    zone_list = get_continent_countries(st.session_state.active_zone)
    df_zone = master_df[master_df['Country'].isin(zone_list)]
    
    if df_zone.empty:
        st.error("ERROR: NO DATA PACKETS FOUND FOR THIS SECTOR")
    else:
        # CONTROLS PANEL
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        c1, c2 = st.columns([1, 1])
        with c1:
            years = st.slider("TEMPORAL RESOLUTION", int(df_zone['Year'].min()), int(df_zone['Year'].max()), (1900, 2013))
        with c2:
            selection = st.multiselect("ISOLATE COUNTRY SIGNALS", zone_list, default=zone_list[:3])
        st.markdown("</div>", unsafe_allow_html=True)

        filtered = df_zone[(df_zone['Year'] >= years[0]) & (df_zone['Year'] <= years[1])]
        
        # MAIN ANALYTICS
        l_col, r_col = st.columns([2, 1])
        
        with l_col:
            st.markdown("#### SATELLITE HEATMAP")
            map_stats = filtered.groupby('Country')['AverageTemperature'].mean().reset_index()
            scope_val = st.session_state.active_zone.lower() if st.session_state.active_zone != "AMERICAS" else "north america"
            
            fig_map = px.choropleth(
                map_stats, locations="Country", locationmode='country names',
                color="AverageTemperature", color_continuous_scale="RdBu_r",
                scope=scope_val, template="plotly_dark"
            )
            fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=600, paper_bgcolor='rgba(0,0,0,0)', geo_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_map, use_container_width=True)

        with r_col:
            st.markdown("#### CRITICAL HOTSPOTS")
            peaks = map_stats.sort_values('AverageTemperature', ascending=False).head(4)
            for _, row in peaks.iterrows():
                st.markdown(f"""
                    <div style="background:rgba(255,0,60,0.05); border-left:4px solid var(--hazard); padding:20px; margin-bottom:10px;">
                        <span style="font-size:0.7rem; color:var(--hazard);">SIGNAL STRENGTH: MAX</span>
                        <h3 style="margin:5px 0;">{row['Country'].upper()}</h3>
                        <h2 style="color:white; margin:0;">{row['AverageTemperature']:.2f}°C</h2>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### TEMPORAL VARIATION ANALYSIS")
        if selection:
            line_df = filtered[filtered['Country'].isin(selection)].groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
            fig_line = px.line(line_df, x="Year", y="AverageTemperature", color="Country", template="plotly_dark")
            fig_line.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis=dict(showgrid=False))
            st.plotly_chart(fig_line, use_container_width=True)
        else:
            st.warning("PLEASE SELECT AT LEAST ONE COUNTRY SIGNAL.")

st.markdown("<div style='text-align:center; padding:100px; color:#222; font-size:0.7rem; letter-spacing:10px;'>DECODED BY QUANTUM INTERFACE // RSA-8192 SECURED</div>", unsafe_allow_html=True)