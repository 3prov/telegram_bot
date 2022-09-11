from abc import abstractmethod


class AbstractHelper:

    @staticmethod
    @abstractmethod
    async def process(*args, **kwargs) -> None:
        raise NotImplementedError
