# src/model.py

import tensorflow as tf
from tensorflow.keras import layers, models

def build_model(input_shape=(224, 224, 3), num_classes=7):
    base_model = tf.keras.applications.MobileNetV2(
        input_shape=input_shape,
        include_top=False,
        weights='imagenet'
    )
    base_model.trainable = False  # fine-tune later if needed

    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dropout(0.3),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

def save_model(model, path='models/maize_disease_model.h5'):
    model.save(path)

def load_model(path='models/maize_disease_model.h5'):
    return tf.keras.models.load_model(path)

def retrain_model(existing_model_path, new_data_dir, model_output_path):
    from src.preprocessing import load_data
    X_new, y_new, class_names = load_data(new_data_dir)

    # Load original model and existing data
    base_model = tf.keras.models.load_model(existing_model_path)
    
    # Optionally freeze some layers or use the model as-is
    base_model.fit(X_new, y_new, epochs=5, validation_split=0.2)

    base_model.save(model_output_path)
    return model_output_path

