from aiogram import types

from app.handlers import AbstractCommandHandler
from app.helpers.api import DeactivateAPIHelper
from app.menus.deactivate import DeactivateMenu
from app.models.users import UserModel


class DeactivateUserCommandHandler(AbstractCommandHandler):

    @staticmethod
    async def process(message: types.Message, *args, **kwargs) -> None:

        _telegram_id = message.chat.id
        user: UserModel = await UserModel.find_one(UserModel.telegram_id == _telegram_id)
        if await DeactivateAPIHelper.call(user_site_uuid=user.site_uuid):
            await user.deactivate()
            await DeactivateMenu.show(message)
