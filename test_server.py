import requests
import json
from datetime import datetime

# Test data
test_snapshots = [
    {
        "local_id": 1,
        "timestamp": int(datetime.now().timestamp() * 1000),
        "battery": 85,
        "network": True,
        "lat": 28.6139,
        "lng": 77.2090
    },
    {
        "local_id": 2,
        "timestamp": int(datetime.now().timestamp() * 1000),
        "battery": 72,
        "network": False,
        "lat": 28.6129,
        "lng": 77.2080
    }
]

def test_server():
    base_url = "http://127.0.0.1:8001"
    
    try:
        # Test sync endpoint
        print("Testing /sync/snapshots endpoint...")
        response = requests.post(f"{base_url}/sync/snapshots", json=test_snapshots)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Test get snapshots endpoint
        print("\nTesting /snapshots endpoint...")
        response = requests.get(f"{base_url}/snapshots")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
    except requests.exceptions.ConnectionError:
        print("Server is not running. Please start it with: uvicorn server:app --host 127.0.0.1 --port 8000")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_server()