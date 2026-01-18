import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def test_weather(city: str):
    """Test the weather API directly"""
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

if __name__ == "__main__":
    print(test_weather("Meerut"))
