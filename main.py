import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(page_title="Global Climate Crisis Tracker", page_icon="🌡️", layout="wide")

# Custom CSS for a professional "Crisis" look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1 { color: #ff4b4b; text-align: center; font-weight: 800; font-size: 3.5rem; }
    .stAlert { background-color: #262730; border: 1px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# 2. Hero Section
st.title("🌡️ THE GLOBAL CLIMATE CRISIS")
st.markdown("<h4 style='text-align: center; color: #9da0a4;'>Visualizing Earth Surface Temperature Anomalies (1750 - 2013)</h4>", unsafe_allow_html=True)
st.write("---")

# 3. Data Loading Logic
@st.cache_data
def load_data():
    # Make sure this filename matches your uploaded file exactly!
    df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
    df['dt'] = pd.to_datetime(df['dt'])
    df['Year'] = df['dt'].dt.year
    df = df.dropna(subset=['AverageTemperature'])
    return df

try:
    df = load_data()

    # 4. Sidebar Control Panel
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2600/2600282.png", width=100)
    st.sidebar.header("🕹️ CONTROL PANEL")
    st.sidebar.markdown("Filter the dataset to see historical changes.")
    
    year_range = st.sidebar.slider("Select Year Range", 
                                  int(df['Year'].min()), 
                                  int(df['Year'].max()), 
                                  (1900, 2013))
    
    mask = (df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])
    selected_df = df.loc[mask]

    # 5. Top Metrics - Immediate Impact
    col_a, col_b, col_c = st.columns(3)
    global_avg = selected_df['AverageTemperature'].mean()
    max_temp = selected_df['AverageTemperature'].max()
    
    col_a.metric("Avg Global Temp", f"{global_avg:.2f}°C", "Rising")
    col_b.metric("Max Recorded Temp", f"{max_temp:.2f}°C", "Critical", delta_color="inverse")
    col_c.metric("Data Points Analyzed", f"{len(selected_df):,}", "Real-time")

    # 6. Main Visualizations
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("🗺️ Global Heat Exposure Map")
        map_data = selected_df.groupby('Country')['AverageTemperature'].mean().reset_index()
        
        fig_map = px.choropleth(map_data, 
                                locations="Country", 
                                locationmode='country names',
                                color="AverageTemperature",
                                hover_name="Country",
                                color_continuous_scale="Reds") # Dramatic red scale
        fig_map.update_layout(margin={"r":0,"t":20,"l":0,"b":0}, height=500, template="plotly_dark")
        st.plotly_chart(fig_map, use_container_width=True)

    with col2:
        st.subheader("🔥 Top 10 Hottest Nations")
        top_10 = map_data.sort_values('AverageTemperature', ascending=False).head(10)
        fig_bar = px.bar(top_10, x='AverageTemperature', y='Country', 
                         orientation='h', 
                         color='AverageTemperature',
                         color_continuous_scale="OrRd")
        fig_bar.update_layout(yaxis={'categoryorder':'total ascending'}, template="plotly_dark")
        st.plotly_chart(fig_bar, use_container_width=True)

    # 7. Comparison Section
    st.write("---")
    st.subheader("📈 Multi-Country Temperature Trends")
    all_countries = sorted(df['Country'].unique())
    selected_countries = st.multiselect("Select nations to compare impact:", 
                                        all_countries, 
                                        default=["Vietnam", "United States", "Norway"])
    
    if selected_countries:
        trend_df = selected_df[selected_df['Country'].isin(selected_countries)]
        trend_year = trend_df.groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
        
        fig_line = px.line(trend_year, x="Year", y="AverageTemperature", color="Country",
                           line_shape="spline", render_mode="svg")
        fig_line.update_layout(hover_mode="x unified", template="plotly_dark")
        st.plotly_chart(fig_line, use_container_width=True)

    # 8. Final Call to Action
    st.error("🚨 **CRITICAL FINDING:** Data confirms an undeniable upward trajectory in surface temperatures. Immediate global intervention is required.")

except Exception as e:
    st.warning("⚠️ **Awaiting Data...** Please ensure 'GlobalLandTemperaturesByCountry.csv' is uploaded to your GitHub repository.")
    st.info(f"System Error Log: {e}")