import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CORE: TERMINAL 2026", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Full height and hidden scroll for static pages */
    html, body, [data-testid="stAppViewContainer"] {
        height: 100vh;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }
    
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 
                    url('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXZueXp3eHh3eHh3eHh3eHh3eHh3eHh3eHh3eHh3eHh3&ep=v1_internal_gif_by_id/3o7TKMGpxx3039C504/giphy.gif');
        background-size: cover;
        background-position: center;
    }

    /* Global Title Styling */
    .glitch-title {
        color: #00FF00; font-family: 'Courier New', monospace; font-size: 6vw !important;
        font-weight: 900; text-transform: uppercase; margin: 0;
        text-shadow: 3px 3px #ff0000, -3px -3px #0000ff;
        animation: glitch 2s infinite;
    }
    
    @keyframes glitch {
        0% { transform: skew(0deg); }
        5% { transform: skew(5deg); }
        10% { transform: skew(-5deg); }
        15% { transform: skew(0deg); }
        100% { transform: skew(0deg); }
    }

    /* Remove Streamlit Padding */
    .block-container {
        padding: 0rem 1rem !important;
    }

    /* Sector Selection Card Design */
    .sector-btn-container {
        border: 2px solid #00FF00;
        border-radius: 10px;
        padding: 0px;
        overflow: hidden;
        background: rgba(0, 40, 0, 0.4);
        transition: 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .sector-btn-container:hover {
        box-shadow: 0 0 30px #00FF00;
        transform: scale(1.02);
    }

    /* Button Overrides */
    .stButton>button {
        width: 100%;
        background-color: transparent !important;
        color: #00FF00 !important;
        border: 1px solid #00FF00 !important;
        border-radius: 0px !important;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        padding: 10px;
        text-transform: uppercase;
    }
    .stButton>button:hover {
        background-color: #00FF00 !important;
        color: #000 !important;
    }

    /* Metric Boxes */
    .hotspot-card {
        background: rgba(255, 0, 0, 0.1);
        border-left: 5px solid #FF0000;
        padding: 15px;
        margin-bottom: 10px;
    }

    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'continent' not in st.session_state:
    st.session_state.continent = None

REGION_MAP = {
    "EUROPE": ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom'],
    "ASIA": ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Laos', 'Lebanon', 'Malaysia', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Thailand', 'Turkey', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen'],
    "AMERICAS": ['Argentina', 'Bahamas', 'Belize', 'Bolivia', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Suriname', 'United States', 'Uruguay', 'Venezuela'],
    "AFRICA": ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burundi', 'Cameroon', 'Chad', 'Congo', 'Egypt', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Ivory Coast', 'Kenya', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Senegal', 'Somalia', 'South Africa', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']
}

COUNTRY_FLAGS = {
    "Vietnam": "🇻🇳", "Thailand": "🇹🇭", "Mali": "🇲🇱", "Djibouti": "🇩🇯", "Senegal": "🇸🇳", "Burkina Faso": "🇧🇫",
    "United Arab Emirates": "🇦🇪", "Saudi Arabia": "🇸🇦", "India": "🇮🇳", "Qatar": "🇶🇦", "Norway": "🇳🇴",
    "Brazil": "🇧🇷", "Mexico": "🇲🇽", "Canada": "🇨🇦", "United States": "🇺🇸", "Germany": "🇩🇪",
    "Portugal": "🇵🇹", "Greece": "🇬🇷", "Spain": "🇪🇸", "Italy": "🇮🇹", "France": "🇫🇷"
}

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
        df['dt'] = pd.to_datetime(df['dt'])
        df['Year'] = df['dt'].dt.year
        df = df.dropna(subset=['AverageTemperature'])
        return df
    except:
        return pd.DataFrame()

data = load_data()

# --- PAGE: LANDING ---
if st.session_state.page == 'home':
    st.markdown('<div style="display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh;">', unsafe_allow_html=True)
    st.markdown('<h1 class="glitch-title">CLIMATE QUEST</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#00FF00; font-family:monospace; font-size:1.5rem;">SATELLITE INTERFACE ACTIVE // 2026</p>', unsafe_allow_html=True)
    st.markdown('<div style="width:200px; margin-top:30px;">', unsafe_allow_html=True)
    if st.button("CONNECT"):
        st.session_state.page = 'selection'
        st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- PAGE: SECTOR SELECTION ---
elif st.session_state.page == 'selection':
    st.markdown('<div style="padding-top: 5vh; text-align:center;">', unsafe_allow_html=True)
    st.markdown('<h2 style="color:#00FF00; font-family:monospace; letter-spacing:5px;">SELECT SCAN SECTOR</h2>', unsafe_allow_html=True)
    
    sectors = [
        ("ASIA", "https://images.unsplash.com/photo-1535016120720-40c646bebbbb?q=80&w=600", "🌏"),
        ("EUROPE", "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?q=80&w=600", "🇪🇺"),
        ("AMERICAS", "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?q=80&w=600", "🌎"),
        ("AFRICA", "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?q=80&w=600", "🌍")
    ]
    
    st.markdown('<br>', unsafe_allow_html=True)
    cols = st.columns(4)
    for i, (name, img, icon) in enumerate(sectors):
        with cols[i]:
            st.markdown(f"""
                <div class="sector-btn-container">
                    <img src="{img}" style="width:100%; height:250px; object-fit:cover;">
                    <div style="padding:15px; background:black;">
                        <h2 style="color:#00FF00; margin:0;">{icon} {name}</h2>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"INITIALIZE {name}"):
                st.session_state.continent = name
                st.session_state.page = 'dashboard'
                st.rerun()
    
    st.markdown('<div style="width:200px; margin: 40px auto;">', unsafe_allow_html=True)
    if st.button("DISCONNECT"):
        st.session_state.page = 'home'
        st.rerun()
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- PAGE: DASHBOARD ---
elif st.session_state.page == 'dashboard':
    st.markdown("""<style>html, body, [data-testid="stAppViewContainer"] { overflow: auto; height: auto; }</style>""", unsafe_allow_html=True)
    
    # Top Bar
    t1, t2 = st.columns([4, 1])
    with t1:
        st.markdown(f"<h1 style='color:#00FF00; margin:0;'>CORE ANALYTICS: {st.session_state.continent}</h1>", unsafe_allow_html=True)
    with t2:
        if st.button("BACK TO SECTORS"):
            st.session_state.page = 'selection'
            st.rerun()

    if data.empty:
        st.error("DATABASE OFFLINE")
    else:
        # Filter Logic
        sector_countries = REGION_MAP[st.session_state.continent]
        sector_df = data[data['Country'].isin(sector_countries)]
        
        # Chronological Controller
        st.markdown("<p style='color:#00FF00; font-family:monospace; margin-bottom:0;'>TIMELINE SYNCHRONIZATION</p>", unsafe_allow_html=True)
        year_sel = st.slider("", int(sector_df['Year'].min()), int(sector_df['Year'].max()), (1900, 2013), label_visibility="collapsed")
        
        # Reactive Data
        filtered = sector_df[(sector_df['Year'] >= year_sel[0]) & (sector_df['Year'] <= year_sel[1])]
        stats = filtered.groupby('Country')['AverageTemperature'].mean().reset_index()

        col_left, col_right = st.columns([2, 1])
        
        with col_left:
            st.markdown("<h3 style='color:#00FF00; font-family:monospace;'>LIVE THERMAL MAP</h3>", unsafe_allow_html=True)
            scope = st.session_state.continent.lower() if st.session_state.continent != "AMERICAS" else "north america"
            fig_map = px.choropleth(stats, locations="Country", locationmode='country names',
                                    color="AverageTemperature", color_continuous_scale="Turbo",
                                    scope=scope, template="plotly_dark")
            fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=500, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_map, use_container_width=True, config={'displayModeBar': False})

        with col_right:
            st.markdown("<h3 style='color:#00FF00; font-family:monospace;'>HOTSPOT OVERRIDE</h3>", unsafe_allow_html=True)
            top_3 = stats.sort_values('AverageTemperature', ascending=False).head(3)
            for _, row in top_3.iterrows():
                flag = COUNTRY_FLAGS.get(row['Country'], "🏳️")
                st.markdown(f"""
                    <div class="hotspot-card">
                        <span style="font-size:1.5rem;">{flag}</span>
                        <span style="color:white; font-size:1.2rem; font-weight:bold; font-family:monospace;"> {row['Country'].upper()}</span>
                        <h1 style="color:#FF4B4B; margin:0; font-size:3rem;">{row['AverageTemperature']:.2f}°C</h1>
                    </div>
                """, unsafe_allow_html=True)

        # Comparison Section
        st.markdown("<hr style='border-color:#00FF00;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#00FF00; font-family:monospace;'>COMPARISON SENSORS</h3>", unsafe_allow_html=True)
        available = sorted(sector_df['Country'].unique())
        target = st.multiselect("ADD COUNTRIES TO SCANNER", available, default=[available[0]])
        
        if target:
            line_df = filtered[filtered['Country'].isin(target)].groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
            fig_line = px.line(line_df, x="Year", y="AverageTemperature", color="Country", 
                               template="plotly_dark", line_shape="hv", markers=True)
            fig_line.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_line, use_container_width=True)

    st.markdown("<p style='color:red; text-align:center; font-family:monospace; animation: pulse 1s infinite;'>🚨 SYSTEM WARNING: THERMAL ANOMALY DETECTED 🚨</p>", unsafe_allow_html=True)