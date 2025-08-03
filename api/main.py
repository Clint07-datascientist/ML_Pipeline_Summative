# sapi/main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os

from src.prediction import load_model, preprocess_image, predict_image
from src.preprocessing import load_datasets
from src.api.retrain import retrain_model

app = FastAPI()

MODEL_PATH = "models/maize_disease_model.h5"
model = load_model(MODEL_PATH)

# Load class names using training set
_, _, class_names = load_datasets('data/train', image_size=(224, 224))


@app.get("/")
def root():
    return {"message": "Maize Disease Classifier API is running."}


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    file_path = f"temp/{file.filename}"
    os.makedirs("temp", exist_ok=True)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    img_array = preprocess_image(file_path)
    predicted_class, confidence = predict_image(model, img_array, class_names)
    
    os.remove(file_path)

    return {
        "prediction": predicted_class,
        "confidence": round(confidence, 3)
    }


@app.post("/retrain/")
def retrain():
    try:
        retrain_model()
        global model
        model = load_model(MODEL_PATH)
        return {"message": "Model retrained and updated successfully."}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
