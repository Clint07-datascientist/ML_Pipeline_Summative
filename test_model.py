#!/usr/bin/env python3
"""
Quick test to verify model loading
"""
import os
import sys

# Add the parent directory to the path to import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_model_loading():
    print("🧪 Testing Model Loading...")
    print("=" * 40)
    
    # Check if model file exists - use absolute path
    MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "maize_model.h5")
    print(f"📁 Looking for model at: {MODEL_PATH}")
    
    if os.path.exists(MODEL_PATH):
        print("✅ Model file found!")
        
        try:
            from src.prediction import load_model
            model = load_model(MODEL_PATH)
            print("✅ Model loaded successfully!")
            print(f"📊 Model summary:")
            print(f"   - Input shape: {model.input_shape}")
            print(f"   - Output shape: {model.output_shape}")
            print(f"   - Total parameters: {model.count_params():,}")
            return True
            
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            return False
    else:
        print("❌ Model file not found!")
        return False

if __name__ == "__main__":
    success = test_model_loading()
    if success:
        print("\n🎉 Model is ready for use in the API!")
    else:
        print("\n⚠️ Model loading failed. Check the error above.")
