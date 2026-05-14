import streamlit as st
import pandas as pd
import plotly.express as px

# Full-screen and Game Theme Configuration
st.set_page_config(page_title="CLIMATE QUEST: GLOBAL WARMING", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for Full-Screen, Pixel-Art Background, and Neon UI
st.markdown("""
    <style>
    /* Force full-height and hide scrollbars for the landing page */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url('https://wallpaperaccess.com/full/3960007.gif');
        background-size: cover;
        background-position: center;
        height: 100vh;
        overflow: hidden;
    }
    
    /* Landing Page Container */
    .landing-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 85vh;
        text-align: center;
    }

    h1 { color: #00FF00 !important; font-family: 'Courier New', monospace !important; text-shadow: 4px 4px #FF0000; font-size: 5rem !important; margin-bottom: 0px; }
    h2, h3 { color: #00FF00 !important; font-family: 'Courier New', monospace !important; text-transform: uppercase; }
    
    /* Neon Button Styling */
    .stButton>button {
        background-color: #000; color: #00FF00; border: 3px solid #00FF00;
        padding: 15px 50px; font-size: 24px; font-weight: bold;
        font-family: 'Courier New', monospace;
        box-shadow: 0 0 15px #00FF00;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00FF00; color: #000; box-shadow: 0 0 40px #00FF00;
    }
    
    /* Hide Streamlit Header/Footer */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Session Management
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'continent' not in st.session_state:
    st.session_state.continent = None

# Region Mapping Logic
REGION_MAP = {
    "EUROPE": ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia And Herzegovina', 'Bulgaria', 'Croatia', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom'],
    "ASIA": ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia', 'China', 'Cyprus', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor Leste', 'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen'],
    "AMERICAS": ['Argentina', 'Bahamas', 'Barbados', 'Belize', 'Bolivia', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Grenada', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Saint Kitts And Nevis', 'Saint Lucia', 'Saint Vincent And The Grenadines', 'Suriname', 'Trinidad And Tobago', 'United States', 'Uruguay', 'Venezuela'],
    "AFRICA": ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Central African Republic', 'Chad', 'Comoros', 'Congo', 'Congo (Democratic Republic Of The)', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea Bissau', 'Ivory Coast', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome And Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Swaziland', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']
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

# --- PAGE 1: HOME (STRICT FULL SCREEN) ---
if st.session_state.page == 'home':
    st.markdown('<div class="landing-container">', unsafe_allow_html=True)
    st.markdown("<h1>CLIMATE QUEST</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #00FF00; letter-spacing: 5px;'>SYSTEM INITIALIZED: MONITORING PLANET EARTH</h3>", unsafe_allow_html=True)
    if st.button("🚀 INITIATE MISSION"):
        st.session_state.page = 'selection'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 2: SECTOR SELECTION ---
elif st.session_state.page == 'selection':
    st.markdown("<div style='height: 10vh;'></div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 3rem !important;'>SELECT GEOGRAPHIC SECTOR</h1>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2, col3, col4 = st.columns(4)
    sectors = [("EUROPE", "https://cdn-icons-png.flaticon.com/512/2483/2483030.png"),
               ("ASIA", "https://cdn-icons-png.flaticon.com/512/2483/2483011.png"),
               ("AMERICAS", "https://cdn-icons-png.flaticon.com/512/2483/2483023.png"),
               ("AFRICA", "https://cdn-icons-png.flaticon.com/512/2483/2483018.png")]

    for i, (name, icon) in enumerate(sectors):
        with [col1, col2, col3, col4][i]:
            st.image(icon, width=120)
            if st.button(f"ENTER {name}"):
                st.session_state.continent = name
                st.session_state.page = 'dashboard'
                st.rerun()
            
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("⬅️ ABORT MISSION"):
        st.session_state.page = 'home'
        st.rerun()

# --- PAGE 3: DYNAMIC DASHBOARD ---
elif st.session_state.page == 'dashboard':
    st.markdown("""<style>.stApp { overflow: auto; height: auto; }</style>""", unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.markdown(f"<h2 style='color: #00FF00;'>MISSION LOG</h2>", unsafe_allow_html=True)
    st.sidebar.info(f"CURRENT SECTOR: {st.session_state.continent}")
    if st.sidebar.button("🎮 CHANGE SECTOR"):
        st.session_state.page = 'selection'
        st.rerun()
    if st.sidebar.button("🏠 EXIT TO MENU"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown(f"<h1>ANALYSIS: {st.session_state.continent}</h1>", unsafe_allow_html=True)
    
    if data.empty:
        st.error("CRITICAL ERROR: SATELLITE DATA OFFLINE (CSV MISSING)")
    else:
        # Filter data based on Continent mapping
        continent_countries = REGION_MAP[st.session_state.continent]
        sector_data = data[data['Country'].isin(continent_countries)]
        
        # Chronological Filter
        year_range = st.slider("SET CHRONOLOGICAL TIMELINE", 1850, 2013, (1970, 2013))
        filtered_df = sector_data[(sector_data['Year'] >= year_range[0]) & (sector_data['Year'] <= year_range[1])]
        
        # Row 1: Map and Sector Rankings
        c1, c2 = st.columns([2, 1])
        map_stats = filtered_df.groupby('Country')['AverageTemperature'].mean().reset_index()
        
        with c1:
            st.subheader(f"🌐 {st.session_state.continent} THERMAL SCAN")
            # Map focused ONLY on the selected continent's countries
            fig_map = px.choropleth(map_stats, locations="Country", locationmode='country names',
                                    color="AverageTemperature", color_continuous_scale="Hot", 
                                    scope=st.session_state.continent.lower() if st.session_state.continent != "AMERICAS" else "north america",
                                    template="plotly_dark")
            fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(fig_map, use_container_width=True)
            
        with c2:
            st.subheader("🔥 TOP 3 HEAT ZONES")
            top_3 = map_stats.sort_values('AverageTemperature', ascending=False).head(3)
            fig_top3 = px.bar(top_3, x='AverageTemperature', y='Country', orientation='h', 
                             color='AverageTemperature', color_continuous_scale="Reds", template="plotly_dark")
            st.plotly_chart(fig_top3, use_container_width=True)

        # Row 2: Advanced Comparison
        st.write("---")
        st.subheader("📊 SECTOR TREND COMPARISON")
        # Only allow countries belonging to the selected continent
        available_countries = sorted(sector_data['Country'].unique())
        selected_nations = st.multiselect("SELECT ASSETS FOR COMPARISON", available_countries, 
                                          default=[available_countries[0]] if available_countries else None)
        
        if selected_nations:
            comp_df = filtered_df[filtered_df['Country'].isin(selected_nations)]
            comp_year = comp_df.groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
            
            # Diverse Chart: Area Chart for visual impact
            fig_area = px.area(comp_year, x="Year", y="AverageTemperature", color="Country", 
                               template="plotly_dark", title="Surface Temperature Trajectory")
            st.plotly_chart(fig_area, use_container_width=True)

    st.error("🚨 ALERT: PLANETARY HEAT LEVELS EXCEEDING STABILITY PARAMETERS")