import streamlit as st

st.title("🇲🇹 Malta 2026: Green Transport Redesign")
st.subheader("Project Lead: Luca G. | Town Planner")

# --- THE PROBLEM ---
st.header("1. The Diagnosis: Why Malta is Stalling")
col1, col2 = st.columns(2)

with col1:
    st.error("🚗 Car Dependency")
    st.write("With over 400,000 vehicles, our village cores are chocked by exhaust and double-parking.")
    
    st.error("🏗️ ODZ Loss")
    st.write("Widening roads in areas like Dingli or Attard destroys rubble walls and fertile soil forever.")

with col2:
    st.warning("📉 Quality of Life")
    st.write("- **Noise:** Average street noise exceeds 70dB.\n- **Health:** Highest asthma rates in the EU due to fine dust.")

st.divider()

# --- THE PLAN ---
st.header("2. The 'Luca Plan' for a Greener Malta")

# Proposal 1: The Ferry Link
with st.expander("🚢 Proposal 1: The Grand Harbour Ferry Extension"):
    st.write("""
    **The Change:** Extend the ferry route from Valletta/Sliema to include **Marsaxlokk** and **St. Paul's Bay**.
    **Benefit:** Removes 5,000 cars from the regional roads every morning. Uses our natural 'blue highway' instead of building more asphalt.
    """)

# Proposal 2: Pedestrianize the Pjazza
with st.expander("🌳 Proposal 2: The 'Pjazza Libera' Initiative"):
    st.write("""
    **The Change:** Close the main village square to cars from 6:00 PM to 6:00 AM daily. 
    **Benefit:** Returns the heart of the village to children and families. Reduces noise pollution and boosts local cafes.
    """)

# Proposal 3: The Vertical Lift System
with st.expander("🚲 Proposal 3: E-Bike Lifts & Shuttles"):
    st.write("""
    **The Change:** Install outdoor 'bike lifts' (like in Norway) for steep hills (e.g., climbing from Msida to University).
    **Benefit:** Makes cycling a viable option even in Malta's hilly terrain and summer heat.
    """)

# --- THE MAP ---
st.divider()
st.header("3. Visual Impact Map")
# This is where you would upload your Canva/Google Maps screenshot
st.info("📍 This is where the biggest problem of malta lays because if this is blocked EVERYWHERE IS BLOCKED!!!")
st.info("we need to find a way to fix this 🤔💭")
st.image("https://github.com/Lucathedesigner612/website-enviormental/blob/main/Capture.JPG?raw=true", 
         caption="Example of a 'Green Road' with integrated tram and cycle paths.")

# --- THE VOTE ---
st.sidebar.title("🗳️ Public Consultation")
vote = st.sidebar.radio("Which change is most urgent?", ["Ferry Extension", "Pjazza Libera", "Bike Lifts"])
st.sidebar.success(f"Thank you! You voted for: {vote}")





