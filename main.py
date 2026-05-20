import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CLIMATE VAULT", layout="wide", initial_sidebar_state="collapsed")

if "page" not in st.session_state:
    st.session_state.page = "WELCOME"

if st.session_state.page == "WELCOME":
    st.markdown("""
        <style>
        .stApp { background-color: #050505; }
        
        /* Tao luoi grid bang CSS (khong can anh) */
        .grid-bg {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            background-image: linear-gradient(rgba(45, 212, 191, 0.1) 1px, transparent 1px),
                              linear-gradient(90deg, rgba(45, 212, 191, 0.1) 1px, transparent 1px);
            background-size: 40px 40px;
            z-index: 0;
        }
        
        .main-wrapper {
            position: relative; z-index: 1; display: flex; flex-direction: column; 
            align-items: center; justify-content: center; height: 80vh; color: #e2e8f0;
        }
        
        .title { font-size: 70px; letter-spacing: 20px; font-weight: 800; color: #2dd4bf; margin: 0; }
        .subtitle { font-size: 16px; letter-spacing: 10px; text-transform: uppercase; margin-bottom: 50px; }
        
        div.stButton > button {
            background: transparent; border: 2px solid #2dd4bf; color: #2dd4bf;
            padding: 15px 50px; font-weight: bold; letter-spacing: 3px;
        }
        div.stButton > button:hover { background: #2dd4bf; color: #050505; }
        </style>
        
        <div class="grid-bg"></div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="main-wrapper">
            <h1 class="title">CLIMATE VAULT</h1>
            <p class="subtitle">PLANETARY THERMAL FORENSICS</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("INITIALIZE ANALYSIS"):
            st.session_state.page = "ANALYSIS"
            st.rerun()

elif st.session_state.page == "ANALYSIS":
    st.title("DATA INTERFACE")
    df = pd.DataFrame({'Year': [2020, 2021, 2022], 'Temp': [28, 29, 30]})
    fig = px.line(df, x='Year', y='Temp', template="plotly_dark")
    fig.update_traces(line_color='#2dd4bf')
    st.plotly_chart(fig, use_container_width=True)
    if st.button("BACK"):
        st.session_state.page = "WELCOME"
        st.rerun()