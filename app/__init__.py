import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from config import config

bot = Bot(token=config.TELEGRAM_BOT_API_TOKEN, parse_mode=types.ParseMode.HTML)
dispatcher = Dispatcher(bot)


def _settings_before_start() -> None:
    from app.handlers import register_handlers

    register_handlers(dispatcher=dispatcher)


def run():
    logging.basicConfig(level=logging.DEBUG)
    _settings_before_start()
    executor.start_polling(dispatcher, skip_updates=True)
