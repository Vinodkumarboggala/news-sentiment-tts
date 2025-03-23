import streamlit as st
import requests

st.title("🔎 News Sentiment & Hindi TTS Generator")

company = st.text_input("Enter Company Name")

if st.button("Analyze"):
    response = requests.get(f"http://127.0.0.1:8000/analyze?company={company}")
    if response.status_code == 200:
        result = response.json()
        st.json(result)  # Display JSON result
        st.audio("output.mp3", format="audio/mp3")
    else:
        st.error("Error fetching results")
