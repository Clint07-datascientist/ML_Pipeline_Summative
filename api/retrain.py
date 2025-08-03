# src/api/retrain.py

import os
from src.preprocessing import load_datasets
from src.model import build_model, save_model

def retrain_model(data_dir='data/train', image_size=(224, 224), batch_size=32, epochs=5):
    train_ds, val_ds, _ = load_datasets(data_dir, image_size=image_size, batch_size=batch_size)
    
    model = build_model(input_shape=(224, 224, 3), num_classes=7)
    model.fit(train_ds, validation_data=val_ds, epochs=epochs)
    
    save_model(model, path='models/maize_disease_model.h5')
