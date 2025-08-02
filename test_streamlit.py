#!/usr/bin/env python3
"""
Test Streamlit installation and app
"""
import sys
import os

def test_imports():
    print("🧪 Testing Required Imports")
    print("=" * 40)
    
    modules = {
        'streamlit': 'Streamlit web framework',
        'requests': 'HTTP requests library',
        'PIL': 'Pillow image processing',
        'io': 'Input/output operations (built-in)'
    }
    
    all_good = True
    for module, description in modules.items():
        try:
            if module == 'PIL':
                from PIL import Image
                print(f"✅ {module} - {description}")
            else:
                __import__(module)
                print(f"✅ {module} - {description}")
        except ImportError as e:
            print(f"❌ {module} - {description} - ERROR: {e}")
            all_good = False
    
    return all_good

def test_streamlit_app():
    print("\n🚀 Testing Streamlit App")
    print("=" * 30)
    
    app_path = "ui/app.py"
    if os.path.exists(app_path):
        print(f"✅ App file found: {app_path}")
        
        # Try to parse the app file
        try:
            with open(app_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'st.title' in content:
                    print("✅ Streamlit app structure looks good")
                else:
                    print("⚠️ App might have issues - no st.title found")
        except Exception as e:
            print(f"⚠️ Error reading app file: {e}")
    else:
        print(f"❌ App file not found: {app_path}")

def main():
    print("🔍 AgroInsightX Streamlit Diagnostics")
    print("=" * 50)
    
    imports_ok = test_imports()
    test_streamlit_app()
    
    print("\n📋 Next Steps:")
    print("=" * 20)
    
    if imports_ok:
        print("✅ All dependencies are installed!")
        print("\n🚀 To start Streamlit:")
        print("   python -m streamlit run ui/app.py")
        print("\n🌐 App will open at: http://localhost:8501")
        print("🔗 Make sure FastAPI is running at: http://localhost:8000")
    else:
        print("❌ Some dependencies are missing")
        print("💡 Run: pip install streamlit requests pillow")

if __name__ == "__main__":
    main()
