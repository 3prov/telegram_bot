from aiogram import types

from app.handlers import AbstractCallbackHandler
from app.helpers.general import RegisterOrActivateHelper
from app.menus.activate import ActivateMenu
from app.models.users import UserModel


class ActivateUserCallbackHandler(AbstractCallbackHandler):

    @staticmethod
    async def process(callback_query: types.CallbackQuery, *args, **kwargs) -> None:

        _message = callback_query.message
        user: UserModel = await UserModel.get_by_telegram_id(_message.chat.id)
        if await RegisterOrActivateHelper.process(user, _message):
            return await ActivateMenu.show(_message)
        await callback_query.answer('Ты уже зарегистрирован.')
