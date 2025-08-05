import os
import sys

print("🔍 Debug Model Path Resolution")
print("=" * 50)

# Current working directory
print(f"Current working directory: {os.getcwd()}")

# Script location
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Script directory: {script_dir}")

# Project root (should be the same as script dir)
project_root = script_dir
print(f"Project root: {project_root}")

# Model path
model_path = os.path.join(project_root, "models", "maize_model.h5")
print(f"Model path: {model_path}")

# Check if model exists
exists = os.path.exists(model_path)
print(f"Model exists: {exists}")

if exists:
    # Check file size
    size = os.path.getsize(model_path)
    print(f"Model file size: {size:,} bytes ({size/1024/1024:.2f} MB)")
else:
    print("❌ Model file not found!")
    print("Contents of models directory:")
    models_dir = os.path.join(project_root, "models")
    if os.path.exists(models_dir):
        for file in os.listdir(models_dir):
            print(f"  - {file}")
    else:
        print("  Models directory doesn't exist!")

# Test API path resolution (how the API sees it)
print("\n🌐 API Path Resolution")
print("=" * 30)
api_dir = os.path.join(project_root, "api")
print(f"API directory: {api_dir}")

# Simulate how the API resolves the path
api_project_root = os.path.dirname(api_dir)
api_model_path = os.path.join(api_project_root, "models", "maize_model.h5")
print(f"API model path: {api_model_path}")
print(f"API can see model: {os.path.exists(api_model_path)}")
