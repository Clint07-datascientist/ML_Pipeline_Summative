import streamlit as st
import requests
from PIL import Image
import io

st.title("🌽 AgroInsightX Maize Disease Classifier")
st.markdown("Upload an image of a maize leaf to detect diseases and pests")

# --- Image prediction ---
st.header("📸 1. Predict from Image")

# Check if API is running
try:
    health_response = requests.get("http://localhost:8000/health", timeout=2)
    if health_response.status_code == 200:
        health_data = health_response.json()
        if health_data.get("model_loaded", False):
            st.success("✅ AI Model is ready!")
        else:
            st.warning("⚠️ AI Model is not loaded. Please check your FastAPI server.")
    else:
        st.error("❌ Cannot connect to AI server. Make sure FastAPI is running on http://localhost:8000")
except requests.exceptions.RequestException:
    st.error("❌ Cannot connect to AI server. Make sure FastAPI is running on http://localhost:8000")

uploaded_img = st.file_uploader("Upload a maize leaf image", type=["jpg", "png", "jpeg"])

if uploaded_img:
    image = Image.open(uploaded_img)
    st.image(image, caption="Uploaded Image", width=400)

    if st.button("🔍 Analyze Image"):
        with st.spinner("Analyzing image..."):
            try:
                files = {"file": uploaded_img.getvalue()}
                response = requests.post("http://localhost:8000/predict", files=files)

                if response.status_code == 200:
                    result = response.json()
                    prediction = result.get('prediction', 'Unknown')
                    confidence = result.get('confidence', 0)
                    
                    st.success(f"🎯 Prediction: **{prediction}**")
                    st.info(f"📊 Confidence: **{confidence:.1%}**")
                    
                    # Display class information
                    class_descriptions = {
                        "healthy": "🟢 The plant appears healthy with no visible diseases or pests.",
                        "fall_armyworm": "🐛 Fall armyworm detected. This pest can cause significant damage to maize crops.",
                        "grasshopper": "🦗 Grasshopper damage detected. Monitor for further infestations.",
                        "leaf_beetle": "🪲 Leaf beetle damage identified. Consider pest management strategies.",
                        "leaf_blight": "🟤 Leaf blight disease detected. This fungal disease can reduce yield.",
                        "leaf_spot": "🔴 Leaf spot disease identified. Monitor spread and consider treatment.",
                        "streak_virus": "🦠 Streak virus detected. This viral disease can severely impact crop health."
                    }
                    
                    if prediction.lower() in class_descriptions:
                        st.markdown("### 📋 Information:")
                        st.write(class_descriptions[prediction.lower()])
                    
                elif response.status_code == 503:
                    st.error("⚠️ AI Model is not loaded. Please train the model first.")
                else:
                    st.error(f"❌ Prediction failed: {response.status_code}")
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# --- Retraining ---
st.header("🔄 2. Retrain Model with New Images")
st.markdown("Upload multiple images to improve the model (Feature in development)")

uploaded_files = st.file_uploader("Upload images for retraining", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"📁 Selected {len(uploaded_files)} images")
    
    if st.button("🚀 Upload for Retraining"):
        with st.spinner("Uploading images..."):
            try:
                # Create form data for multiple files
                files = []
                for uploaded_file in uploaded_files:
                    files.append(("files", (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)))
                
                response = requests.post("http://localhost:8000/upload-bulk", files=files)
                
                if response.status_code == 200:
                    result = response.json()
                    st.success(f"✅ Successfully uploaded {len(result.get('files', []))} images!")
                    
                    # Trigger retraining
                    retrain_response = requests.post("http://localhost:8000/retrain/")
                    if retrain_response.status_code == 200:
                        st.info("🔄 Model retraining initiated (simulated)")
                else:
                    st.error(f"❌ Upload failed: {response.status_code}")
                    
            except Exception as e:
                st.error(f"❌ Upload error: {str(e)}")

# --- Footer ---
st.markdown("---")
st.markdown("### 🚀 AgroInsightX ML Pipeline")
st.markdown("Powered by FastAPI, TensorFlow, and Streamlit")
