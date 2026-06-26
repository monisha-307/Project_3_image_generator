import streamlit as st
from PIL import Image
import google.generativeai as genai

# API Key
genai.configure(api_key="YOUR_API_KEY")

st.title("🎨 AI Image Generator")

prompt = st.text_input("Enter image prompt:")

if st.button("Generate Image"):
    if prompt:
        st.write("Prompt:", prompt)

        st.image(
            "https://picsum.photos/600/400",
            caption=prompt
        )