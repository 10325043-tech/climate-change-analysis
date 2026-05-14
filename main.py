import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="TERMINAL: EARTH 2026", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        height: 100vh;
        overflow: hidden;
    }
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), 
                    url('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXZueXp3eHh3eHh3eHh3eHh3eHh3eHh3eHh3eHh3eHh3&ep=v1_internal_gif_by_id/3o7TKMGpxx3039C504/giphy.gif');
        background-size: cover;
        background-position: center;
    }
    .main-box {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 100vh; width: 100%; text-align: center; margin-top: -50px;
    }
    .glitch {
        color: #00FF00; font-family: 'Courier New', monospace; font-size: 8vw !important;
        font-weight: bold; text-transform: uppercase;
        text-shadow: 4px 4px #ff0000, -4px -4px #0000ff;
        animation: glitch 1s infinite;
        margin: 0;
    }
    @keyframes glitch {
        0% { transform: translate(0); }
        20% { transform: translate(-3px, 3px); }
        40% { transform: translate(-3px, -3px); }
        60% { transform: translate(3px, 3px); }
        80% { transform: translate(3px, -3px); }
        100% { transform: translate(0); }
    }
    .sector-card {
        background: rgba(0, 20, 0, 0.8);
        border: 2px solid #00FF00;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        transition: 0.3s;
    }
    .sector-card:hover {
        box-shadow: 0 0 40px #00FF00;
        transform: translateY(-10px);
    }
    .stButton>button {
        background-color: #000; color: #00FF00; border: 2px solid #00FF00;
        padding: 10px 40px; font-family: 'Courier New', monospace;
        font-size: 20px; font-weight: bold; width: 100%;
    }
    .stButton>button:hover {
        background-color: #00FF00; color: #000;
    }
    [data-testid="stMetricValue"] { color: #FF4B4B !important; }
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
    "Brazil": "🇧🇷", "Mexico": "🇲🇽", "Canada": "🇨🇦", "United States": "🇺🇸", "Germany": "🇩🇪"
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

if st.session_state.page == 'home':
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.markdown('<p class="glitch">CLIMATE QUEST</p>', unsafe_allow_html=True)
    st.markdown("<p style='color: #00FF00; font-family: monospace; letter-spacing: 10px;'>EST. 2026 | SATELLITE LINK ACTIVE</p>", unsafe_allow_html=True)
    if st.button("🚀 INITIATE OVERRIDE"):
        st.session_state.page = 'selection'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'selection':
    st.markdown('<div style="height: 100vh; overflow-y: auto; padding: 50px;">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #00FF00; font-size: 3rem;'>GEOGRAPHIC SECTOR SELECT</h1>", unsafe_allow_html=True)
    
    sectors = [
        ("ASIA", "🌏", "https://images.unsplash.com/photo-1535016120720-40c646bebbbb?auto=format&fit=crop&w=400"),
        ("EUROPE", "🇪🇺", "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?auto=format&fit=crop&w=400"),
        ("AMERICAS", "🌎", "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=400"),
        ("AFRICA", "🌍", "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?auto=format&fit=crop&w=400")
    ]
    
    cols = st.columns(4)
    for i, (name, icon, img) in enumerate(sectors):
        with cols[i]:
            st.markdown(f"""
            <div class='sector-card'>
                <img src='{img}' style='width:100%; border-radius:5px; height:150px; object-fit:cover;'>
                <h2 style='color:#00FF00;'>{icon} {name}</h2>
            </div>""", unsafe_allow_html=True)
            if st.button(f"DATA LINK: {name}"):
                st.session_state.continent = name
                st.session_state.page = 'dashboard'
                st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅️ TERMINATE ACCESS"):
        st.session_state.page = 'home'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 'dashboard':
    st.markdown("""<style>html, body, [data-testid="stAppViewContainer"] { overflow: auto; height: auto; }</style>""", unsafe_allow_html=True)
    
    header_col, btn_col = st.columns([5, 1])
    header_col.markdown(f"<h1 style='color: #00FF00; margin:0;'>SECTOR: {st.session_state.continent}</h1>", unsafe_allow_html=True)
    if btn_col.button("🔄 RE-SCAN"):
        st.session_state.page = 'selection'
        st.rerun()

    if data.empty:
        st.error("DATA SOURCE NOT FOUND")
    else:
        sector_countries = REGION_MAP[st.session_state.continent]
        sector_df = data[data['Country'].isin(sector_countries)]
        
        # Chronological Slider
        year_sel = st.slider("SYNCHRONIZE TIMELINE", int(sector_df['Year'].min()), int(sector_df['Year'].max()), (1990, 2013))
        
        # Reactive Filtering
        filtered = sector_df[(sector_df['Year'] >= year_sel[0]) & (sector_df['Year'] <= year_sel[1])]
        stats = filtered.groupby('Country')['AverageTemperature'].mean().reset_index()

        col_left, col_right = st.columns([2, 1])
        
        with col_left:
            st.subheader("THERMAL INTENSITY MAP")
            scope = st.session_state.continent.lower() if st.session_state.continent != "AMERICAS" else "north america"
            fig_map = px.choropleth(stats, locations="Country", locationmode='country names',
                                    color="AverageTemperature", color_continuous_scale="Reds",
                                    scope=scope, template="plotly_dark")
            fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(fig_map, use_container_width=True)

        with col_right:
            st.subheader("CRITICAL HOTSPOTS")
            top_3 = stats.sort_values('AverageTemperature', ascending=False).head(3)
            for _, row in top_3.iterrows():
                flag = COUNTRY_FLAGS.get(row['Country'], "🏳️")
                st.markdown(f"""
                <div style='background:rgba(255,0,0,0.1); border:1px solid #FF4B4B; padding:15px; border-radius:10px; margin-bottom:10px;'>
                    <h2 style='margin:0;'>{flag} {row['Country'].upper()}</h2>
                    <h1 style='color:#FF4B4B; margin:0;'>{row['AverageTemperature']:.2f}°C</h1>
                </div>
                """, unsafe_allow_html=True)

        st.write("---")
        st.subheader("HISTORICAL TRAJECTORY")
        available = sorted(sector_df['Country'].unique())
        target = st.multiselect("SELECT ASSETS FOR SCAN", available, default=[available[0]])
        
        if target:
            line_df = filtered[filtered['Country'].isin(target)].groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
            fig_line = px.line(line_df, x="Year", y="AverageTemperature", color="Country", 
                               template="plotly_dark", line_shape="spline", markers=True)
            st.plotly_chart(fig_line, use_container_width=True)

    st.error("🚨 WARNING: PLANETARY THERMAL RUNAWAY DETECTED IN THIS SECTOR")