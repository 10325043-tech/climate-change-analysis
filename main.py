import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CORE: TERMINAL 2026", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        height: 100vh;
        margin: 0;
        padding: 0;
        overflow: hidden !important;
        background-color: #000;
    }
    
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    url('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXZueXp3eHh3eHh3eHh3eHh3eHh3eHh3eHh3eHh3eHh3&ep=v1_internal_gif_by_id/3o7TKMGpxx3039C504/giphy.gif');
        background-size: cover;
        background-position: center;
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    .full-screen-center {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        text-align: center;
    }

    .glitch-text {
        color: #00FF00;
        font-family: 'Courier New', monospace;
        font-size: 8vw !important;
        font-weight: 900;
        text-transform: uppercase;
        text-shadow: 4px 4px #ff0000, -4px -4px #0000ff;
        margin: 0;
    }

    .sector-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        width: 90%;
        margin-top: 20px;
    }

    .sector-card {
        border: 2px solid #00FF00;
        background: rgba(0, 30, 0, 0.6);
        border-radius: 15px;
        overflow: hidden;
        transition: 0.3s ease;
        height: 450px;
        display: flex;
        flex-direction: column;
    }

    .sector-card:hover {
        box-shadow: 0 0 50px #00FF00;
        transform: scale(1.03);
    }

    .img-box {
        width: 100%;
        height: 280px;
        object-fit: cover;
        border-bottom: 2px solid #00FF00;
    }

    .stButton>button {
        background-color: transparent !important;
        color: #00FF00 !important;
        border: 2px solid #00FF00 !important;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        font-size: 1.2rem;
        width: 100%;
        height: 60px;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #00FF00 !important;
        color: #000 !important;
    }

    .hotspot-item {
        background: rgba(255, 0, 0, 0.15);
        border-left: 8px solid #FF0000;
        padding: 15px;
        margin: 10px 0;
        border-radius: 0 10px 10px 0;
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'continent' not in st.session_state:
    st.session_state.continent = None

COUNTRY_FLAGS = {
    "Vietnam": "🇻🇳", "Thailand": "🇹🇭", "China": "🇨🇳", "India": "🇮🇳", "Japan": "🇯🇵",
    "Norway": "🇳🇴", "Germany": "🇩🇪", "France": "🇫🇷", "Greece": "🇬🇷", "Portugal": "🇵🇹",
    "Spain": "🇪🇸", "Brazil": "🇧🇷", "USA": "🇺🇸", "Canada": "🇨🇦", "Mexico": "🇲🇽",
    "Egypt": "🇪🇬", "Nigeria": "🇳🇬", "Mali": "🇲🇱", "Djibouti": "🇩🇯"
}

REGION_MAP = {
    "EUROPE": ['Albania', 'Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom'],
    "ASIA": ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Laos', 'Lebanon', 'Malaysia', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Thailand', 'Turkey', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen'],
    "AMERICAS": ['Argentina', 'Bahamas', 'Belize', 'Bolivia', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Suriname', 'United States', 'Uruguay', 'Venezuela'],
    "AFRICA": ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burundi', 'Cameroon', 'Chad', 'Congo', 'Egypt', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Ivory Coast', 'Kenya', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Senegal', 'Somalia', 'South Africa', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']
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

# --- LANDING PAGE ---
if st.session_state.page == 'home':
    st.markdown('<div class="full-screen-center">', unsafe_allow_html=True)
    st.markdown('<h1 class="glitch-text">CLIMATE QUEST</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#00FF00; font-family:monospace; letter-spacing:10px; margin-bottom:40px;">GLOBAL SATELLITE ACCESS</p>', unsafe_allow_html=True)
    if st.button("🔴 ACCESS SYSTEM"):
        st.session_state.page = 'selection'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- SELECTION PAGE ---
elif st.session_state.page == 'selection':
    st.markdown('<div class="full-screen-center">', unsafe_allow_html=True)
    st.markdown('<h2 style="color:#00FF00; font-family:monospace; margin-bottom:30px;">SELECT GEOGRAPHIC SECTOR</h2>', unsafe_allow_html=True)
    
    sectors = [
        ("ASIA", "https://images.unsplash.com/photo-1464817739973-0128fe77a1b7?q=80&w=800", "🌏"),
        ("EUROPE", "https://images.unsplash.com/photo-1491557345352-5929e343eb89?q=80&w=800", "🇪🇺"),
        ("AMERICAS", "https://images.unsplash.com/photo-1475503562775-177cba17ad1e?q=80&w=800", "🌎"),
        ("AFRICA", "https://images.unsplash.com/photo-1523805081446-ed9a7bb89973?q=80&w=800", "🌍")
    ]
    
    cols = st.columns(4)
    for i, (name, img, icon) in enumerate(sectors):
        with cols[i]:
            st.markdown(f"""
                <div class="sector-card">
                    <img src="{img}" class="img-box">
                    <div style="padding:20px; flex-grow:1; display:flex; flex-direction:column; justify-content:center;">
                        <h2 style="color:#00FF00; text-align:center; margin:0;">{icon} {name}</h2>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"SCAN {name}"):
                st.session_state.continent = name
                st.session_state.page = 'dashboard'
                st.rerun()
    
    st.markdown('<div style="width:250px; margin-top:40px;">', unsafe_allow_html=True)
    if st.button("⬅️ EXIT TO HOME"):
        st.session_state.page = 'home'
        st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- DASHBOARD PAGE ---
elif st.session_state.page == 'dashboard':
    st.markdown("""<style>html, body, [data-testid="stAppViewContainer"] { overflow-y: auto !important; height: auto !important; }</style>""", unsafe_allow_html=True)
    
    # Static Header
    h1, h2 = st.columns([5, 1])
    h1.markdown(f"<h1 style='color:#00FF00; margin-left:20px;'>{st.session_state.continent} SECTOR SCAN</h1>", unsafe_allow_html=True)
    if h2.button("BACK"):
        st.session_state.page = 'selection'
        st.rerun()

    if data.empty:
        st.error("DATABASE OFFLINE")
    else:
        sector_countries = REGION_MAP[st.session_state.continent]
        sector_df = data[data['Country'].isin(sector_countries)]
        
        # Timeline Controller
        st.markdown("<div style='padding:0 20px;'>", unsafe_allow_html=True)
        year_sel = st.slider("SYNCHRONIZE TIMELINE", int(sector_df['Year'].min()), int(sector_df['Year'].max()), (1980, 2013))
        
        # Reactive Logic
        filtered = sector_df[(sector_df['Year'] >= year_sel[0]) & (sector_df['Year'] <= year_sel[1])]
        stats = filtered.groupby('Country')['AverageTemperature'].mean().reset_index()

        col_left, col_right = st.columns([2.5, 1.5])
        
        with col_left:
            scope = st.session_state.continent.lower() if st.session_state.continent != "AMERICAS" else "north america"
            fig_map = px.choropleth(stats, locations="Country", locationmode='country names',
                                    color="AverageTemperature", color_continuous_scale="Hot",
                                    scope=scope, template="plotly_dark")
            fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=550, paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_map, use_container_width=True)

        with col_right:
            st.markdown("<h2 style='color:#00FF00; font-family:monospace;'>HOTSPOT OVERRIDE</h2>", unsafe_allow_html=True)
            top_3 = stats.sort_values('AverageTemperature', ascending=False).head(3)
            for _, row in top_3.iterrows():
                flag = COUNTRY_FLAGS.get(row['Country'], "🏴")
                st.markdown(f"""
                    <div class="hotspot-item">
                        <h2 style="color:white; margin:0;">{flag} {row['Country'].upper()}</h2>
                        <h1 style="color:#FF4B4B; margin:0; font-size:4rem;">{row['AverageTemperature']:.2f}°C</h1>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("<hr style='border-color:#00FF00;'>", unsafe_allow_html=True)
        available = sorted(sector_df['Country'].unique())
        selected = st.multiselect("ADD SATELLITE ASSETS", available, default=[available[0]])
        
        if selected:
            line_df = filtered[filtered['Country'].isin(selected)].groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
            fig_line = px.line(line_df, x="Year", y="AverageTemperature", color="Country", 
                               template="plotly_dark", line_shape="spline", markers=True)
            fig_line.update_layout(height=400, paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_line, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<p style='color:red; text-align:center; font-family:monospace; padding-bottom:20px;'>🚨 SATELLITE ALERT: CRITICAL TEMPERATURE GRADIENT DETECTED 🚨</p>", unsafe_allow_html=True)