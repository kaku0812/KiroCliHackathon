import subprocess
import time
import sys
import os

def test_ngrok():
    """Test if ngrok is properly set up"""
    try:
        # Test ngrok version
        result = subprocess.run(['./ngrok.exe', 'version'], capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            print("✅ ngrok is installed and working")
            print(f"   Version: {result.stdout.strip()}")
        else:
            print("❌ ngrok installation issue")
            return False
            
        # Test if auth token is set
        result = subprocess.run(['./ngrok.exe', 'config', 'check'], capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            print("✅ ngrok auth token is configured")
        else:
            print("❌ ngrok auth token not set")
            print("   Please run: .\\ngrok.exe authtoken YOUR_TOKEN")
            return False
            
        return True
    except Exception as e:
        print(f"❌ Error testing ngrok: {e}")
        return False

def main():
    print("🔧 Testing ngrok setup...")
    print("=" * 40)
    
    if test_ngrok():
        print("\n🎉 ngrok is ready!")
        print("\n📋 Next steps:")
        print("1. Start your server: python -m uvicorn server:app --host 127.0.0.1 --port 8001 --reload")
        print("2. In another terminal, run: .\\ngrok.exe http 8001")
        print("3. Copy the https URL from ngrok")
        print("4. Use that URL in your Android app")
    else:
        print("\n❌ Setup incomplete. Please fix the issues above.")

if __name__ == "__main__":
    main()