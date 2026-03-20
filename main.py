import streamlit as st

# Define the pages
home = st.Page("page_home.py", title="Dashboard", icon="🏠", default=True)
planner = st.Page("page_planner.py", title="Town Planner", icon="🚲") # New Page!
tracker = st.Page("page_tracker.py", title="Expense Vault", icon="💰")
vision = st.Page("page_vision.py", title="2026 Vision", icon="🚀")

# Organize the menu
pg = st.navigation({
    "Government Projects": [planner],
    "Financial Apps": [tracker],
    "Personal": [home, vision]
})

pg.run()
