from aiogram import types

from app.handlers import AbstractCommandHandler
from app.menus.start import StartMenu


class StartCommandHandler(AbstractCommandHandler):

    @staticmethod
    async def process(message: types.Message, *args, **kwargs) -> None:
        await StartMenu.show(message)
