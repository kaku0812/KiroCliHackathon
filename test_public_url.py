import requests
import json
from datetime import datetime

# Test data
test_snapshots = [
    {
        "local_id": 100,
        "timestamp": int(datetime.now().timestamp() * 1000),
        "battery": 95,
        "network": True,
        "lat": 28.7041,
        "lng": 77.1025
    }
]

def test_public_server():
    base_url = "https://simona-unwifely-enchantedly.ngrok-free.dev"
    
    try:
        print("🌐 Testing public ngrok URL...")
        
        # Test sync endpoint
        print("Testing /sync/snapshots endpoint...")
        response = requests.post(f"{base_url}/sync/snapshots", json=test_snapshots)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print(f"✅ Response: {response.json()}")
        else:
            print(f"❌ Error: {response.text}")
        
        # Test get snapshots endpoint
        print("\nTesting /snapshots endpoint...")
        response = requests.get(f"{base_url}/snapshots")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            snapshots = response.json()
            print(f"✅ Found {len(snapshots)} snapshots")
            if snapshots:
                print(f"Latest: {snapshots[-1]}")
        else:
            print(f"❌ Error: {response.text}")
        
    except requests.exceptions.ConnectionError as e:
        print(f"❌ Connection error: {e}")
        print("Make sure both your server and ngrok are running")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_public_server()