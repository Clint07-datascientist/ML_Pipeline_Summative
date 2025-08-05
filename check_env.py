#!/usr/bin/env python3
"""
Environment verification script
"""
import sys
import subprocess
import os

def check_environment():
    print("🔍 Environment Check")
    print("=" * 40)
    
    # Check Python version and path
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"Virtual environment: {'Yes' if hasattr(sys, 'real_prefix') or sys.base_prefix != sys.prefix else 'No'}")
    
    # Check if we're in the right directory
    print(f"Current directory: {os.getcwd()}")
    
    # Try to import tensorflow
    try:
        import tensorflow as tf
        print(f"✅ TensorFlow version: {tf.__version__}")
    except ImportError as e:
        print(f"❌ TensorFlow not available: {e}")
        
        # Try to install it
        print("🔧 Attempting to install TensorFlow...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "tensorflow"])
            print("✅ TensorFlow installation completed")
            
            # Try import again
            import tensorflow as tf
            print(f"✅ TensorFlow now available: {tf.__version__}")
            
        except Exception as install_error:
            print(f"❌ Installation failed: {install_error}")
    
    # Check other required packages
    required_packages = ['fastapi', 'uvicorn', 'pillow', 'numpy']
    print("\n📦 Checking other packages:")
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - missing")

if __name__ == "__main__":
    check_environment()
