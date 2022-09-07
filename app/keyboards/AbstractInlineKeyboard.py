from abc import abstractmethod


class AbstractInlineKeyboard:

    @staticmethod
    @abstractmethod
    async def show() -> None:
        raise NotImplementedError
