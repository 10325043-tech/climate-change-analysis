import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CLIMATE VAULT | CODETOOPIA", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                    url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=2072');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .hero-box {
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        height: 60vh; gap: 10px;
    }

    .brand { font-family: 'Orbitron'; color: #38bdf8; letter-spacing: 15px; font-size: 1.2rem; }
    .neon-title {
        font-family: 'Orbitron'; font-size: 6.5rem; color: #fff; line-height: 0.9;
        text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 20px #38bdf8, 0 0 30px #38bdf8, 0 0 40px #38bdf8;
    }

    div.stButton > button {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 2px solid #38bdf8 !important;
        color: #fff !important;
        padding: 20px 80px !important;
        font-size: 1.8rem !important;
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 5px !important;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.3) !important;
        transition: 0.3s !important;
    }

    div.stButton > button:hover { background: #38bdf8 !important; color: #000 !important; transform: scale(1.05); }

    .card {
        background: rgba(10, 25, 47, 0.85);
        border: 2px solid #38bdf8;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

if 'state' not in st.session_state: st.session_state.state = "HOME"

if st.session_state.state == "HOME":
    st.markdown("""
        <div class="hero-box">
            <div class="brand">CODETOOPIA</div>
            <div class="neon-title">CLIMATE VAULT</div>
        </div>
    """, unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("INITIALIZE SYSTEM", use_container_width=True):
            st.session_state.state = "SELECT"
            st.rerun()

elif st.session_state.state == "SELECT":
    st.markdown('<h1 style="color:#fff; font-family:Orbitron; text-align:center; margin-bottom:40px;">SELECT CONTINENT</h1>', unsafe_allow_html=True)
    
    data = [
        ("OCEANIA", 34, 38, "SECURE", "#00ff9d"), 
        ("ASIA", 34, 32, "CRITICAL", "#ff4d4d"), 
        ("EUROPE", 22, 30, "SECURE", "#00ff9d"),
        ("AFRICA", 28, 35, "SECURE", "#00ff9d"), 
        ("NORTH AMERICA", 34.2, 36, "SECURE", "#00ff9d"), 
        ("SOUTH AMERICA", 31.8, 32, "SECURE", "#00ff9d")
    ]
    
    cols = st.columns(3)
    for i, (name, temp, threshold, status, color) in enumerate(data):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="card">
                    <h3 style="font-family:Orbitron; color:#fff;">{name}</h3>
                    <h1 style="font-family:Orbitron; color:#38bdf8; margin:5px 0;">{temp}°C</h1>
                    <p style="font-family:Orbitron; color:#aaa; font-size:0.9rem;">THRESHOLD: {threshold}°C</p>
                    <p style="font-family:Orbitron; color:{color}; font-weight:bold;">STATUS: {status}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"ENTER {name}", key=name, use_container_width=True):
                st.session_state.selected_continent = name
                st.session_state.state = "VAULT"
                st.rerun()

elif st.session_state.state == "VAULT":
    @st.cache_data
    def load_vault_data():
        df = pd.read_csv('GlobalLandTemperaturesByCountry.csv')
        df['dt'] = pd.to_datetime(df['dt'])
        df['year'] = df['dt'].dt.year
        return df

    df = load_vault_data()
    continent = st.session_state.selected_continent
    
    mapping = {
        "ASIA": ["Vietnam", "Thailand", "India", "China", "Japan", "Indonesia"],
        "EUROPE": ["France", "Germany", "Italy", "Spain", "United Kingdom"],
        "AFRICA": ["Egypt", "Nigeria", "South Africa", "Kenya"],
        "OCEANIA": ["Australia", "New Zealand"],
        "NORTH AMERICA": ["United States", "Canada", "Mexico"],
        "SOUTH AMERICA": ["Brazil", "Argentina", "Colombia", "Chile"]
    }
    target_countries = mapping.get(continent, df['Country'].unique()[:5])

    st.markdown(f'<h1 style="color:#38bdf8; font-family:Orbitron; text-align:center;">{continent} COMMAND CENTER</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.markdown('<div class="card"><h3>FILTERS</h3></div>', unsafe_allow_html=True)
        sel_nations = st.multiselect("SELECT NATIONS", target_countries, default=[target_countries[0]])
        min_y, max_y = int(df['year'].min()), int(df['year'].max())
        y_range = st.slider("YEAR RANGE", min_y, max_y, (max_y - 20, max_y))
        
        st.markdown('<div class="card"><h3>AI INTEL FEED</h3></div>', unsafe_allow_html=True)
        if sel_nations:
            for n in sel_nations:
                subset = df[df['Country'] == n]
                baseline = subset[subset['year'].between(1850, 1900)]['AverageTemperature'].mean()
                current_val = subset[subset['year'].between(y_range[0], y_range[1])]['AverageTemperature'].mean()
                
                delta = current_val - baseline
                status = "EMERGENCY" if delta > 1.5 else "WARNING" if delta > 0.5 else "STABLE"
                color = "#ff4d4d" if status == "EMERGENCY" else "#ffcc00" if status == "WARNING" else "#00ff9d"
                st.markdown(f"**{n}:** <span style='color:{color}'>{status}</span> (Δ: {delta:+.2f}°C)", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h3>MAIN VISUALIZER</h3></div>', unsafe_allow_html=True)
        filtered_df = df[(df['Country'].isin(sel_nations)) & (df['year'].between(y_range[0], y_range[1]))]
        
        fig = px.line(filtered_df, x='year', y='AverageTemperature', color='Country', template="plotly_dark")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", hovermode="x unified")
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        st.markdown('<div class="card"><h3>SITUATION METRICS</h3></div>', unsafe_allow_html=True)
        if sel_nations:
            avg_temp = df[(df['Country'].isin(sel_nations)) & (df['year'].between(y_range[0], y_range[1]))]['AverageTemperature'].mean()
            st.metric("AVG TEMP", f"{avg_temp:.1f}°C")
            st.metric("ACTIVE NODES", len(sel_nations))
            risk_idx = (avg_temp / 25) * 100
            st.metric("RISK INDEX", f"{risk_idx:.0f}%")
            st.markdown('<div class="card" style="font-size:0.7rem;">TACTICAL NOTE: DATA SOURCED DIRECTLY FROM GLOBAL ARCHIVES.</div>', unsafe_allow_html=True)

    if st.button("BACK TO SELECTION"):
        st.session_state.state = "SELECT"
        st.rerun()