import requests
import json

def test_api():
    base_url = "http://localhost:8000"
    
    print("🧪 Testing AgroInsightX ML Pipeline API")
    print("=" * 50)
    
    # Test 1: Root endpoint
    try:
        print("1. Testing root endpoint...")
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("   ✅ Root endpoint working!")
            data = response.json()
            print(f"   📊 Model loaded: {data.get('model_loaded', 'Unknown')}")
            print(f"   📝 Available endpoints: {len(data.get('available_endpoints', []))}")
        else:
            print(f"   ❌ Root endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Connection error: {e}")
    
    print()
    
    # Test 2: Health check
    try:
        print("2. Testing health endpoint...")
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("   ✅ Health check working!")
            data = response.json()
            print(f"   🏥 Status: {data.get('status', 'Unknown')}")
        else:
            print(f"   ❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Connection error: {e}")
    
    print()
    
    # Test 3: Prediction endpoint (without file - should fail gracefully)
    try:
        print("3. Testing prediction endpoint (no file)...")
        response = requests.post(f"{base_url}/predict")
        print(f"   📝 Status code: {response.status_code}")
        if response.status_code == 422:
            print("   ✅ Properly rejecting requests without files!")
        elif response.status_code == 503:
            print("   ⚠️ Model not loaded (expected if no trained model)")
    except Exception as e:
        print(f"   ❌ Connection error: {e}")
    
    print()
    print("🎯 API Test Complete!")
    print("\n💡 To start the server, run: start_api.bat")
    print("💡 Then test with: python test_api.py")

if __name__ == "__main__":
    test_api()
