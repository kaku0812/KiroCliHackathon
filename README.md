# Kiro CLI Hackathon - Weather MCP Server

A comprehensive weather and safety monitoring system built with Python and MCP (Model Context Protocol).

## Features

- Weather data fetching and monitoring
- Safety report generation
- RSS feed processing
- Geographic clustering
- Web dashboard interface
- Telegram integration
- MCP server implementation

## Files

- `server.py` - Main MCP server implementation
- `WEATHER_SERVER*.PY` - Various weather server configurations
- `app.py` - Main application
- `fetcher.py` - Data fetching utilities
- `processor.py` - Data processing logic
- `models.py` - Data models
- `geocode.py` - Geographic utilities
- `clustering.py` - Data clustering algorithms
- `html_generator.py` - Report generation
- `telegram_mcp.py` - Telegram integration

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Configure environment variables in `.env`
3. Run the server: `python server.py`

## MCP Configuration

Multiple MCP configuration files are provided for different setups:
- `mcp_config.json` - Standard configuration
- `mcp_config_simple.json` - Simplified setup
- `mcp_config_portable.json` - Portable configuration