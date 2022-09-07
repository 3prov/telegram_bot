from abc import abstractmethod

from aiogram import types


class AbstractCommandHandler:

    @staticmethod
    @abstractmethod
    async def process(callback_query: types.CallbackQuery, *args, **kwargs):
        raise NotImplementedError()
