from app.helpers import AbstractAPIHelper

from config import config


class CreateUserAPIHelper(AbstractAPIHelper):

    # pylint: disable=arguments-differ
    @staticmethod
    async def call(**kwargs) -> dict:

        _username = f"tg@{kwargs.get('first_name')}' if telegram_id else f'vk@{kwargs.get('vkontakte_id')}"
        data = {
          "username": _username,
          "first_name": kwargs.get('first_name'),
          "last_name": kwargs.get('last_name'),
          "vkontakte_id": kwargs.get('vkontakte_id'),
          "telegram_id": kwargs.get('telegram_id'),
        }
        return await AbstractAPIHelper._make_request(
            endpoint=config.BackendAPIEndpoints.BACKEND_API_CREATE_USER,
            method_type=config.BackendAPIMethods.POST,
            data=data
        )
