import os

import requests
from dotenv import load_dotenv

# LOAD ENV
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_telegram_message(message: str):
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ NOTIFICATION DISABLED, CHECK .env")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ ERROR: {e}")
