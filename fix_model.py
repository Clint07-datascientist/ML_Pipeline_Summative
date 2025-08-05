#!/usr/bin/env python3
"""
Model architecture fixer - reconstructs the model with proper architecture
"""
import tensorflow as tf
import numpy as np
import os

def reconstruct_model():
    """Reconstruct the model with proper architecture"""
    print("🔧 Model Architecture Reconstruction")
    print("=" * 50)
    
    model_path = "models/maize_model.h5"
    
    if not os.path.exists(model_path):
        print("❌ Model file not found!")
        return False
    
    try:
        print("📊 Attempting to load model...")
        
        # Try to load the model
        model = tf.keras.models.load_model(model_path, compile=False)
        print("✅ Model loaded successfully!")
        
        # Print model info
        print(f"📋 Model Summary:")
        model.summary()
        
        # Try to recompile
        print("🔧 Recompiling model...")
        model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        print("✅ Model recompiled successfully!")
        
        # Save the fixed model
        fixed_path = "models/maize_model_fixed.h5"
        model.save(fixed_path)
        print(f"💾 Fixed model saved to: {fixed_path}")
        
        # Test prediction
        print("🧪 Testing prediction...")
        dummy_input = np.random.random((1, 224, 224, 3))
        prediction = model.predict(dummy_input, verbose=0)
        print(f"✅ Prediction test successful! Output shape: {prediction.shape}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n🔧 Trying alternative approach...")
        
        try:
            # Create a new model with MobileNetV2 architecture (common for this type of project)
            print("🏗️ Creating new model architecture...")
            
            base_model = tf.keras.applications.MobileNetV2(
                input_shape=(224, 224, 3),
                include_top=False,
                weights='imagenet'
            )
            base_model.trainable = False
            
            model = tf.keras.Sequential([
                base_model,
                tf.keras.layers.GlobalAveragePooling2D(),
                tf.keras.layers.Dropout(0.3),
                tf.keras.layers.Dense(128, activation='relu'),
                tf.keras.layers.Dropout(0.3),
                tf.keras.layers.Dense(7, activation='softmax')  # 7 classes
            ])
            
            model.compile(
                optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy']
            )
            
            print("✅ New model architecture created!")
            model.summary()
            
            # Save the new model template
            template_path = "models/maize_model_template.h5"
            model.save(template_path)
            print(f"💾 Model template saved to: {template_path}")
            print("⚠️ Note: This is a new model template. You'll need to retrain it.")
            
            return True
            
        except Exception as e2:
            print(f"❌ Alternative approach failed: {e2}")
            return False

if __name__ == "__main__":
    success = reconstruct_model()
    if success:
        print("\n🎉 Model reconstruction completed!")
        print("💡 If a fixed model was created, update your API to use it.")
    else:
        print("\n⚠️ Model reconstruction failed.")
        print("💡 You may need to retrain the model from scratch.")
