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
    # This acts as your 'Visual Map' placeholder
    st.info("🗺️ Interactive Map Analysis")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Malta_location_map.svg/800px-Malta_location_map.svg.png", 
             caption="Current Traffic Bottlenecks in the Village Core")

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
