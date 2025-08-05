import requests
import json

def test_api_status():
    try:
        response = requests.get("http://127.0.0.1:8000/")
        if response.status_code == 200:
            data = response.json()
            print("📊 API Status:")
            print(json.dumps(data, indent=2))
            return data.get('model_loaded', False)
        else:
            print(f"❌ API request failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing API Status...")
    model_loaded = test_api_status()
    print(f"\n🎯 Model loaded: {model_loaded}")
