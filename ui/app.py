import streamlit as st
import requests
from PIL import Image
import io

st.title("Maize Disease Classifier 🌽")

# --- Image prediction ---
st.header("1. Predict from Image")
uploaded_img = st.file_uploader("Upload a maize leaf image", type=["jpg", "png"])

if uploaded_img:
    image = Image.open(uploaded_img)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    files = {"file": uploaded_img.getvalue()}
    response = requests.post("http://localhost:8000/predict", files=files)

    if response.ok:
        st.success(f"Prediction: {response.json()['prediction']}")

# --- Retraining ---
st.header("2. Retrain Model with New Images")
uploaded_files = st.file_uploader("Upload images", type=["jpg", "png"], accept_multiple_files=True)
if st.button("Retrain Model") and uploaded_files:
    for file in uploaded_files:
        with open(f"data/uploads/{file.name}", "wb") as f:
            f.write(file.getbuffer())
    res = requests.post("http://localhost:8000/retrain/")
    st.write(res.json())
