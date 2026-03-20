import streamlit as st

# 1. Define pages (Make sure these files exist!)
# If page_home.py doesn't exist yet, just use page_planner.py twice for now
home = st.Page("page_home.py", title="Home", icon="🏠", default=True)
planner = st.Page("page_planner.py", title="Town Planner", icon="🌳")

# 2. Setup Navigation
pg = st.navigation([home, planner])

# 3. Run (Only ONCE at the end)
pg.run()
