import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. SYSTEM CONFIGURATION
st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide")

# 2. TACTICAL UI ENGINE (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300;500&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072');
        background-size: cover; background-attachment: fixed;
    }

    /* GLASSMORPHISM MODULES */
    .module-card {
        background: rgba(10, 25, 47, 0.85);
        border: 1px solid #38bdf8;
        border-radius: 4px;
        padding: 20px;
        margin-bottom: 20px;
        position: relative;
        overflow: hidden;
    }
    .module-card::before {
        content: "SCANNING..."; position: absolute; top: 5px; right: 10px;
        font-family: 'JetBrains Mono'; font-size: 0.6rem; color: #38bdf8; opacity: 0.5;
    }

    /* TEXT STYLING */
    .neon-text { font-family: 'Orbitron'; color: #38bdf8; text-shadow: 0 0 10px #38bdf8; }
    .label-text { font-family: 'JetBrains Mono'; color: #aaa; font-size: 0.8rem; text-transform: uppercase; }
    .value-text { font-family: 'Orbitron'; color: #fff; font-size: 2rem; }

    /* CUSTOM BUTTON */
    div.stButton > button {
        background: transparent !important; border: 1px solid #38bdf8 !important;
        color: #38bdf8 !important; font-family: 'Orbitron' !important;
        transition: 0.3s; width: 100%; border-radius: 0;
    }
    div.stButton > button:hover { background: #38bdf8 !important; color: #000 !important; box-shadow: 0 0 15px #38bdf8; }

    /* TITLES */
    .main-header { font-family: 'Orbitron'; font-size: 4rem; color: #fff; text-align: center; margin-bottom: 0; }
    .sub-header { font-family: 'Orbitron'; font-size: 1.2rem; color: #38bdf8; text-align: center; letter-spacing: 10px; }
    </style>
""", unsafe_allow_html=True)

# 3. DATA ARCHIVE (CACHE)
@st.cache_data
def load_climate_data():
    df = pd.read_csv('GlobalLandTemperaturesByCountry.csv')
    df['dt'] = pd.to_datetime(df['dt'])
    df['year'] = df['dt'].dt.year
    return df.dropna(subset=['AverageTemperature'])

# 4. SESSION MANAGEMENT
if 'state' not in st.session_state: st.session_state.state = "HOME"

# --- PAGE 1: HOME ---
if st.session_state.state == "HOME":
    st.markdown('<div style="height:25vh"></div>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">CODETOOPIA SYSTEM</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="main-header">CLIMATE VAULT</h1>', unsafe_allow_html=True)
    st.markdown('<div style="height:10vh"></div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("INITIALIZE INTERFACE"):
            st.session_state.state = "SELECT"
            st.rerun()

# --- PAGE 2: CONTINENT SELECTION ---
elif st.session_state.state == "SELECT":
    st.markdown('<h2 class="neon-text" style="text-align:center">SECTOR SELECTION</h2>', unsafe_allow_html=True)
    sectors = [
        ("ASIA", "CRITICAL", "#ff4d4d", "Monsoon destabilization"),
        ("EUROPE", "STABLE", "#00ff9d", "Industrial heat pulse"),
        ("AFRICA", "WARNING", "#ffcc00", "Aridity expansion"),
        ("OCEANIA", "STABLE", "#00ff9d", "Marine coupling"),
        ("NORTH AMERICA", "STABLE", "#00ff9d", "Latitudinal shift"),
        ("SOUTH AMERICA", "STABLE", "#00ff9d", "Eco-integrity loss")
    ]
    cols = st.columns(3)
    for i, (name, status, color, brief) in enumerate(sectors):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="module-card">
                    <p class="label-text">Sector</p>
                    <h3 class="neon-text">{name}</h3>
                    <p class="label-text">Status: <span style="color:{color}">{status}</span></p>
                    <p style="color:#aaa; font-size:0.8rem;">{brief}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"ACCESS {name}"):
                st.session_state.selected_continent = name
                st.session_state.state = "VAULT"
                st.rerun()

# --- PAGE 3: THE VAULT (THE OVERHAUL) ---
elif st.session_state.state == "VAULT":
    df = load_climate_data()
    continent = st.session_state.selected_continent
    
    # CONTINENT-SPECIFIC LOGIC (Chặn nước theo vùng)
    mapping = {
        "ASIA": ["Vietnam", "Thailand", "India", "China", "Japan", "Philippines", "Indonesia"],
        "EUROPE": ["France", "Germany", "Italy", "Spain", "United Kingdom", "Russia", "Norway"],
        "AFRICA": ["Egypt", "Nigeria", "South Africa", "Kenya", "Algeria", "Morocco"],
        "OCEANIA": ["Australia", "New Zealand", "Fiji", "Papua New Guinea"],
        "NORTH AMERICA": ["United States", "Canada", "Mexico", "Cuba"],
        "SOUTH AMERICA": ["Brazil", "Argentina", "Colombia", "Chile", "Peru"]
    }
    
    nation_options = mapping.get(continent, ["Global"])
    min_data_year, max_data_year = int(df['year'].min()), int(df['year'].max())

    # TACTICAL HEADER (Bộ điều khiển ngang - Thay thế Sidebar để dễ hiểu)
    st.markdown(f'<h2 class="neon-text">/COMMAND_CENTER/{continent}_SECTOR</h2>', unsafe_allow_html=True)
    
    ctrl_col1, ctrl_col2, ctrl_col3 = st.columns([2, 2, 1])
    with ctrl_col1:
        sel_nations = st.multiselect("📡 SELECT NODES (NATIONS)", nation_options, default=[nation_options[0]])
    with ctrl_col2:
        # THANH KÉO NĂM: Mặc định 10 năm cuối nhưng cho phép kéo full
        y_range = st.slider("⏳ TEMPORAL RANGE", min_data_year, max_data_year, (max_data_year-10, max_data_year))
    with ctrl_col3:
        mode = st.selectbox("📊 ANALYSIS MODULE", ["THERMAL TREND", "REGIONAL COMPARISON", "VOLATILITY BOX"])

    # MAIN INTERFACE
    m1, m2 = st.columns([3, 1])
    
    filtered_df = df[(df['Country'].isin(sel_nations)) & (df['year'].between(*y_range))]

    with m1:
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        if mode == "THERMAL TREND":
            fig = px.area(filtered_df, x='year', y='AverageTemperature', color='Country', 
                          template="plotly_dark", line_shape="spline")
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_family="JetBrains Mono")
            st.plotly_chart(fig, use_container_width=True)
            st.info("💡 OBSERVATION: Area chart visualizes the cumulative heat intensity across selected nodes.")
        
        elif mode == "REGIONAL COMPARISON":
            avg_data = filtered_df.groupby('Country')['AverageTemperature'].mean().reset_index()
            fig = px.bar(avg_data, x='Country', y='AverageTemperature', color='AverageTemperature',
                         color_continuous_scale="Reds", template="plotly_dark")
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
            st.info("💡 OBSERVATION: Direct comparison of thermal baselines between nations.")

        else:
            fig = px.box(filtered_df, x='Country', y='AverageTemperature', color='Country', template="plotly_dark")
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
            st.info("💡 OBSERVATION: Box plot reveals climatic instability. Wide boxes indicate extreme weather fluctuations.")
        st.markdown('</div>', unsafe_allow_html=True)

    with m2:
        # SITUATION METRICS
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        st.markdown('<p class="label-text">Mean Sector Temp</p>', unsafe_allow_html=True)
        if not filtered_df.empty:
            st.markdown(f'<p class="value-text">{filtered_df["AverageTemperature"].mean():.2f}°C</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p class="value-text">N/A</p>', unsafe_allow_html=True)
        
        st.divider()
        st.markdown('<p class="label-text">Tactical Brief</p>', unsafe_allow_html=True)
        
        # DIFFERENT HIGHLIGHTS PER CONTINENT
        briefs = {
            "ASIA": "⚠️ HIGH MONSOON RISK: Thermal anomalies detected in SE Asian nodes.",
            "EUROPE": "❄️ GLACIAL RECESSION: Northern European nodes showing abnormal warming.",
            "AFRICA": "🔥 DESERTIFICATION: Rapid baseline increase in Saharan-fringe nodes.",
            "OCEANIA": "🌊 MARINE HEATWAVE: Sea-surface coupling affecting coastal nodes.",
            "NORTH AMERICA": "🌪️ JET STREAM SHIFT: Extreme volatility in temperate nodes.",
            "SOUTH AMERICA": "🌿 HUMIDITY DROP: Amazonian nodes reporting record dry cycles."
        }
        st.write(briefs.get(continent, "Monitoring active..."))
        
        if st.button("TERMINATE SESSION"):
            st.session_state.state = "SELECT"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<p style="text-align:center; color:#555; font-family:JetBrains Mono; font-size:0.7rem;">SYSTEM_VERSION_3.0_STABLE // NO_UNAUTHORIZED_ACCESS</p>', unsafe_allow_html=True)