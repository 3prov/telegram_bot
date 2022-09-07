from aiogram import types

from app.handlers import AbstractCommandHandler
from app.menus.unsubscribe import UnsubscribeMenu


class UnsubscribeCommandHandler(AbstractCommandHandler):

    @staticmethod
    async def process(message: types.Message, *args, **kwargs) -> None:
        await UnsubscribeMenu.show(chat_id=message.chat.id)
