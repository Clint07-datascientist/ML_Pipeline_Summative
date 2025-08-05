#!/usr/bin/env python3
"""
Minimal model loading test
"""
import os
import sys

# Add src to path
sys.path.append('.')

def main():
    print("🔍 Minimal Model Test")
    print("=" * 30)
    
    # Check current directory
    cwd = os.getcwd()
    print(f"Working directory: {cwd}")
    
    # Check if we can find the model
    model_path = os.path.join(cwd, "models", "maize_model.h5")
    print(f"Model path: {model_path}")
    print(f"Model exists: {os.path.exists(model_path)}")
    
    if os.path.exists(model_path):
        try:
            print("Attempting to load TensorFlow...")
            import tensorflow as tf
            print("✅ TensorFlow imported")
            
            print("Attempting to load model...")
            model = tf.keras.models.load_model(model_path)
            print("✅ Model loaded successfully!")
            print(f"Model input shape: {model.input_shape}")
            print(f"Model output shape: {model.output_shape}")
            
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            print(f"Error type: {type(e).__name__}")
    else:
        print("❌ Model file not found")
        
        # List what's in models directory
        models_dir = os.path.join(cwd, "models")
        if os.path.exists(models_dir):
            print(f"Contents of {models_dir}:")
            for item in os.listdir(models_dir):
                item_path = os.path.join(models_dir, item)
                if os.path.isfile(item_path):
                    size = os.path.getsize(item_path)
                    print(f"  📄 {item} ({size:,} bytes)")
                else:
                    print(f"  📁 {item}/")

if __name__ == "__main__":
    main()
