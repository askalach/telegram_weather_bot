import os

from dotenv import load_dotenv


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPEN_WEATHER_MAP_ID = os.getenv('OPEN_WEATHER_MAP_ID')
