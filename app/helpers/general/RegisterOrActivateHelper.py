from aiogram import types

from app.helpers.api import ActivateUserAPIHelper, CreateUserAPIHelper
from app.models.users import UserModel


class RegisterOrActivateHelper:

    @staticmethod
    async def process(user: UserModel, message: types.Message) -> bool:

        if await UserModel.is_active(user.telegram_id):
            return False
        elif await UserModel.is_exist(user.telegram_id):  # not active and exist
            await ActivateUserAPIHelper.call(user_site_uuid=user.site_uuid)
        else:  # not active and not exist
            response = await CreateUserAPIHelper.call(
                first_name=message.chat.first_name,
                last_name=message.chat.last_name,
                vkontakte_id=0,
                telegram_id=message.chat.id
            )
            await UserModel(telegram_id=user.telegram_id, site_uuid=response['server_uuid'], active=True).save()
        return True
