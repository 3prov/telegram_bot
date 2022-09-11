import os
from enum import Enum

from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()

        self.TELEGRAM_BOT_API_TOKEN = os.getenv('TELEGRAM_BOT_API_TOKEN')
        self.BACKEND_API_BASE_URL = os.getenv('BACKEND_API_BASE_URL')
        self.REDIS_OM_URL = os.getenv('REDIS_OM_URL')

        self.BACKEND_API_TOKEN = os.getenv('BACKEND_API_TOKEN')

    class BackendAPIEndpoints:
        BACKEND_API_CREATE_USER = 'authtoken/users/'
        BACKEND_API_ACTIVATE_USER = 'users/is_active/{user_uuid}'

    class BackendAPIMethods(Enum):
        POST = 'Create'
        PATCH = 'Update'


config = Config()
