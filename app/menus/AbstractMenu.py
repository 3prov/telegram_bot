from abc import abstractmethod

from aiogram import types


class AbstractMenu:

    @staticmethod
    @abstractmethod
    async def show(message: types.Message) -> None:
        raise NotImplementedError
