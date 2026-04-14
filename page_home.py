import streamlit as st
import pandas as pd

st.title("🏙️ Green Transport Redesign: Village of the Future")
st.write("Town Planner: **Luca G.** | Location: **No specific location**")

# --- SECTION 1: THE DIAGNOSIS ---
st.header("1. Current Urban Crisis")
col1, col2 = st.columns(2)

with col1:
    st.error("🚨 Problem: ODZ Encroachment")
    st.write("Building more roads is eating into our Outside Development Zone (ODZ) land, destroying the natural landscape.")
    
    st.error("🔊 Problem: Noise & Stress")
    st.write("Constant traffic congestion in narrow village cores leads to high decibel levels and resident burnout.")

with col2:


st.image("https://github.com/Lucathedesigner612/website-enviormental/blob/main/Capture.JPG?raw=true", caption="Click below to visit the site")

if st.button("🌐 Open External Link"):
    # This works best if you use a link component or a simple redirect
    st.write(f"Check it out here: [Click Me]({https://www.google.com/maps/@35.8817017,14.4852276,3a,75y,304.02h,87.72t/data=!3m7!1e1!3m5!1sZZndRNNn8ZPZRn_sed8fAg!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D2.2797142157755417%26panoid%3DZZndRNNn8ZPZRn_sed8fAg%26yaw%3D304.02009826192295!7i13312!8i6656!5m1!1e1?authuser=0&entry=ttu&g_ep=EgoyMDI2MDQwOC4wIKXMDSoASAFQAw%3D%3D})")
st.divider()

# --- SECTION 2: THE 3 PROPOSALS ---
st.header("2. The Green Redesign")

tab1, tab2, tab3 = st.tabs(["🚲 The Cycle Superhighway", "🚇 The Mini-Metro", "🚶 Pedestrian Sanctuary"])

with tab1:
    st.subheader("Change 1: Dedicated E-Bike Lanes")
    st.write("Connecting the village to the nearest business hub with a protected, solar-lit cycle track.")
    st.metric("Impact", "CO2 Reduction", "-35%")

with tab2:
    st.subheader("Change 2: Underground Electric Shuttle")
    st.write("A small-scale 'Mini-Metro' that keeps heavy transit underground, preserving the traditional street views.")
    st.metric("Impact", "Noise Level", "-20 dB")

with tab3:
    st.subheader("Change 3: The 'Silent Core' Zone")
    st.write("Converting the main square into a pedestrian-only zone with greenery and water features.")
    st.metric("Impact", "Retail Growth", "+50%")

# --- SECTION 3: QUALITY OF LIFE ---
st.divider()
st.subheader("3. Quality of Life Improvement")
st.write("""
By prioritizing **people over pistons**, we regain our open spaces. 
Less cars = more trees. More trees = cooler air. Cooler air = a happier, healthier village.
""")
