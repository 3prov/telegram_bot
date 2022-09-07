from aiogram import types

from app.handlers import AbstractCommandHandler
from app.menus.subscribe import SubscribeMenu


class SubscribeCommandHandler(AbstractCommandHandler):

    @staticmethod
    async def process(message: types.Message, *args, **kwargs) -> None:
        await SubscribeMenu.show(chat_id=message.chat.id)
