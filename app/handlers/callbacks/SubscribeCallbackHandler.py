from aiogram import types

from app.handlers import AbstractCallbackHandler
from app.menus.subscribe import SubscribeMenu


class SubscribeCallbackHandler(AbstractCallbackHandler):

    @staticmethod
    async def process(callback_query: types.CallbackQuery, *args, **kwargs) -> None:
        await callback_query.answer()
        await SubscribeMenu.show(chat_id=callback_query.message.chat.id)
