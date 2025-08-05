# src/prediction.py

import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

def load_model(model_path='models/maize_disease_model.h5'):
    """Load model with error handling for architecture issues"""
    try:
        # Try loading without compiling first
        model = tf.keras.models.load_model(model_path, compile=False)
        
        # Recompile the model with fresh settings
        model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        return model
        
    except Exception as e:
        print(f"Error loading model: {e}")
        # If there are architecture issues, try loading weights only
        raise e

def preprocess_image(img_path, target_size=(224, 224)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Add batch dimension
    img_array /= 255.0  # Normalize to [0, 1]
    return img_array

def predict_image(model, img_array, class_names):
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions, axis=1)[0]
    predicted_class = class_names[predicted_index]
    confidence = predictions[0][predicted_index]
    return predicted_class, confidence
