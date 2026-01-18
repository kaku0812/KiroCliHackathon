import os
import requests
from mcp.server.fastmcp import FastMCP

BOT_TOKEN = "8344328725:AAGiUKZNnHSx0mQxvU-By1JQMDgzWPuqmS4"
CHAT_ID = "1622643260"

if not BOT_TOKEN or not CHAT_ID:
    raise RuntimeError("BOT_TOKEN and CHAT_ID must be set as environment variables")

# Initialize FastMCP server
mcp = FastMCP("telegram-actions")

@mcp.tool()
def send_telegram_message(message: str) -> str:
    """
    Send a Telegram message using a bot.
    
    Args:
        message: Message to send on Telegram
        
    Returns:
        A confirmation message
    """
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
    }

    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()

    return "Telegram message sent successfully ✅"

if __name__ == "__main__":
    mcp.run(transport="stdio")
