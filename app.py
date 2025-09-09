import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Disaster Management Drone Control Center", layout="wide")

# Load your HTML
with open("sih.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Render inside Streamlit
components.html(html_code, height=800, scrolling=True)
