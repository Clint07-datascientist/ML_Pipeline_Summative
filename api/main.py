# api/main.py

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
from typing import List
import sys
import json

# Add the parent directory to the path to import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = FastAPI(title="Maize Disease Classifier API", version="1.0.0")

# Global variables for model and class names
model = None
class_names = ["fall_armyworm", "grasshopper", "healthy", "leaf_beetle", "leaf_blight", "leaf_spot", "streak_virus"]

def initialize_model():
    """Initialize the model if it exists"""
    global model
    # Get the project root directory (parent of api directory)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODEL_PATH = os.path.join(project_root, "models", "maize_model.h5")
    
    print(f"🔍 Looking for model at: {MODEL_PATH}")
    
    if os.path.exists(MODEL_PATH):
        try:
            # Try to load model directly with TensorFlow first
            import tensorflow as tf
            print("🔧 Attempting to load model with TensorFlow...")
            model = tf.keras.models.load_model(MODEL_PATH, compile=False)
            print("✅ Model loaded successfully!")
        except Exception as tf_error:
            print(f"⚠️ TensorFlow loading failed: {tf_error}")
            print("🔧 Trying alternative loading method...")
            try:
                from src.prediction import load_model
                model = load_model(MODEL_PATH)
                print("✅ Model loaded successfully with custom loader!")
            except Exception as custom_error:
                print(f"⚠️ Custom loading also failed: {custom_error}")
                model = None
    else:
        print("⚠️ Model file not found. Please train the model first using the notebook.")
        model = None

# Try to initialize model on startup
initialize_model()


@app.get("/")
def root():
    return {
        "message": "Maize Disease Classifier API is running.",
        "model_loaded": model is not None,
        "available_endpoints": ["/", "/predict", "/retrain", "/health", "/upload-bulk"],
        "class_names": class_names
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "class_names": class_names
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """Predict the class of an uploaded image"""
    if model is None:
        raise HTTPException(
            status_code=503, 
            detail="Model not loaded. Please train the model first using the notebook."
        )
    
    try:
        # Create temp directory if it doesn't exist
        os.makedirs("temp", exist_ok=True)
        file_path = f"temp/{file.filename}"
        
        # Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Import prediction functions (only when needed)
        from src.prediction import preprocess_image, predict_image
        
        # Process image and make prediction
        img_array = preprocess_image(file_path)
        predicted_class, confidence = predict_image(model, img_array, class_names)
        
        # Clean up temp file
        os.remove(file_path)

        return {
            "prediction": predicted_class,
            "confidence": round(float(confidence), 3),
            "filename": file.filename
        }
        
    except Exception as e:
        # Clean up temp file if it exists
        if 'file_path' in locals() and os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@app.post("/retrain")
def retrain():
    """Retrain the model with new data"""
    try:
        # Mock retraining for now (replace with actual implementation)
        return {
            "message": "Model retraining initiated",
            "status": "success",
            "note": "Implement actual retraining logic in src/model.py"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Retraining error: {str(e)}")


@app.post("/upload-bulk")
async def upload_bulk_images(files: List[UploadFile] = File(...)):
    """Upload multiple images for retraining"""
    try:
        upload_dir = "data/uploads"
        os.makedirs(upload_dir, exist_ok=True)
        
        saved_files = []
        for file in files:
            file_path = os.path.join(upload_dir, file.filename)
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            saved_files.append(file.filename)
        
        return {
            "message": f"Successfully uploaded {len(saved_files)} files",
            "files": saved_files
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
