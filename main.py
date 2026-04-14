import streamlit as st
import os

st.set_page_config(page_title="Malta Green Transit", layout="wide")

# Define the pages with a safety check
pages_to_show = []

# Home Page (Check if it exists)
if os.path.exists("page_home.py"):
    pages_to_show.append(st.Page("page_home.py", title="Home", icon="🏠", default=True))
else:
    # If home is missing, use main.py as a temporary placeholder so it doesn't crash
    st.warning("⚠️ page_home.py not found on GitHub!")

# Planner Page (Check if it exists)
if os.path.exists("page_planner.py"):
    pages_to_show.append(st.Page("page_planner.py", title="Town Planner", icon="🌳"))
else:
    st.error("🚨 page_planner.py is missing from your GitHub repository!")

# Only run navigation if we found at least one page
if pages_to_show:
    pg = st.navigation(pages_to_show)
    pg.run()

else:
    st.title("Welcome to Luca's App")
    st.write("Please upload your .py files to GitHub to see the full site.")
