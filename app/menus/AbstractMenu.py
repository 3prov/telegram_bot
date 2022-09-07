from abc import abstractmethod


class AbstractMenu:

    @staticmethod
    @abstractmethod
    async def show(chat_id: int) -> None:
        raise NotImplementedError
