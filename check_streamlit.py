#!/usr/bin/env python3
"""
Check Streamlit installation and provide startup instructions
"""
import sys
import subprocess

def check_streamlit():
    print("🔍 Checking Streamlit Installation")
    print("=" * 40)
    
    try:
        import streamlit as st
        print(f"✅ Streamlit is installed! Version: {st.__version__}")
        return True
    except ImportError:
        print("❌ Streamlit is not installed")
        return False

def install_streamlit():
    print("📦 Installing Streamlit...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
        print("✅ Streamlit installation completed!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Installation failed: {e}")
        return False

def main():
    if not check_streamlit():
        if install_streamlit():
            check_streamlit()
    
    print("\n🚀 How to start Streamlit:")
    print("=" * 30)
    print("Option 1 (Recommended):")
    print("  python -m streamlit run ui/app.py")
    print("\nOption 2 (If PATH is configured):")
    print("  streamlit run ui/app.py")
    print("\nOption 3 (Use batch file):")
    print("  start_streamlit.bat")
    
    print("\n💡 Tips:")
    print("- Make sure your virtual environment is activated")
    print("- FastAPI should be running on http://localhost:8000")
    print("- Streamlit will open on http://localhost:8501")

if __name__ == "__main__":
    main()
