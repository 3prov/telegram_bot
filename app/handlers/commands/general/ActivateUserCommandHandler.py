from aiogram import types

from app.handlers import AbstractCommandHandler
from app.helpers.general import RegisterOrActivateHelper
from app.menus.activate import ActivateMenu
from app.models.users import UserModel


class ActivateUserCommandHandler(AbstractCommandHandler):

    @staticmethod
    async def process(message: types.Message, *args, **kwargs) -> None:

        user: UserModel = await UserModel.get_by_telegram_id(message.chat.id)
        if await RegisterOrActivateHelper.process(user, message):
            await user.activate()
            return await ActivateMenu.show(message)
        await message.answer('Ты уже зарегистрирован.')
