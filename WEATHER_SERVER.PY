import os
import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import logging

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY not found in .env file")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler()])
logger = logging.getLogger("weather-mcp-server")

# Initialize FastMCP server
mcp = FastMCP("weather-service")

@mcp.tool()
def get_current_weather(city: str) -> str:
    """
    Get the current weather conditions for a specified city.
    Use this tool when the user asks for the weather, temperature, or conditions.

    Args:
        city: The name of the city (e.g., "London", "Tokyo").

    Returns:
        A string with the current weather summary.
    """
    logger.info(f"Tool called: get_current_weather({city})")
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Extract and format relevant data
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        return f"The weather in {city} is currently {description} with a temperature of {temp}°C. Humidity is {humidity}% and wind speed is {wind_speed} m/s."
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching weather data: {str(e)}")
        return f"Error fetching weather data: {str(e)}"

if __name__ == "__main__":
    logger.info("Starting MCP Server...")
    mcp.run(transport="stdio") # Use "stdio" for local development or "sse" for web deployment
