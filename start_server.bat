@echo off
echo Starting Snapshot Server...
echo.
echo Server will run on: http://127.0.0.1:8001
echo API Docs available at: http://127.0.0.1:8001/docs
echo.
echo To make it public for Android app:
echo 1. Install ngrok from https://ngrok.com/download
echo 2. Run: ngrok http 8001
echo 3. Use the ngrok URL in your Android app
echo.
uvicorn server:app --host 127.0.0.1 --port 8001 --reload