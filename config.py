import os

from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()

        self.TELEGRAM_BOT_API_TOKEN = os.getenv('TELEGRAM_BOT_API_TOKEN')


config = Config()
