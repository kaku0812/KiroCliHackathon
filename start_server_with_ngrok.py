#!/usr/bin/env python3
"""
Script to start the snapshot server and provide ngrok setup instructions
"""
import subprocess
import sys
import time
import os

def check_ngrok():
    """Check if ngrok is installed"""
    try:
        result = subprocess.run(['ngrok', 'version'], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def start_server():
    """Start the FastAPI server"""
    print("🚀 Starting FastAPI server on port 8001...")
    try:
        # Start server in background
        server_process = subprocess.Popen([
            sys.executable, '-m', 'uvicorn', 
            'server:app', '--host', '127.0.0.1', '--port', '8001', '--reload'
        ])
        print("✅ Server started successfully!")
        print("📍 Local URL: http://127.0.0.1:8001")
        print("📖 API Docs: http://127.0.0.1:8001/docs")
        return server_process
    except Exception as e:
        print(f"❌ Failed to start server: {e}")
        return None

def main():
    print("🔧 Snapshot Server Setup")
    print("=" * 40)
    
    # Start the server
    server_process = start_server()
    if not server_process:
        return
    
    print("\n🌐 Setting up public access with ngrok...")
    
    if not check_ngrok():
        print("❌ ngrok not found!")
        print("\n📥 To install ngrok:")
        print("1. Go to https://ngrok.com/download")
        print("2. Download and extract ngrok.exe")
        print("3. Add to PATH or put in this folder")
        print("4. Sign up at https://ngrok.com and get auth token")
        print("5. Run: ngrok authtoken YOUR_TOKEN")
        print("\n🔧 Then run this command to create public tunnel:")
        print("   ngrok http 8001")
    else:
        print("✅ ngrok found!")
        print("\n🔧 Run this command in a new terminal:")
        print("   ngrok http 8001")
    
    print("\n📱 For your Android app:")
    print("1. Start ngrok: ngrok http 8001")
    print("2. Copy the https URL (e.g., https://abc123.ngrok.io)")
    print("3. Use this URL as BASE_URL in your Android Retrofit config")
    print("4. Your endpoints will be:")
    print("   - POST {BASE_URL}/sync/snapshots")
    print("   - GET {BASE_URL}/snapshots")
    
    print(f"\n🔄 Server running with PID: {server_process.pid}")
    print("Press Ctrl+C to stop the server")
    
    try:
        server_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Stopping server...")
        server_process.terminate()
        server_process.wait()
        print("✅ Server stopped")

if __name__ == "__main__":
    main()