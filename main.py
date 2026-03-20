import streamlit as st

# Using the current file (main.py) as a placeholder to stop the crashing
home = st.Page("main.py", title="Home", icon="🏠", default=True)

# ONLY add these lines if the files actually exist on GitHub
# planner = st.Page("page_planner.py", title="Town Planner", icon="🚲") 
# tracker = st.Page("page_tracker.py", title="Money", icon="💰")

pg = st.navigation([home])
pg.run()
