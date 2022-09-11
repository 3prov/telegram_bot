from abc import ABC

from aredis_om import HashModel, NotFoundError


class BaseModel(HashModel, ABC):

    @classmethod
    async def find_one(cls, *expressions):
        try:
            return await cls.find(*expressions).first()
        except NotFoundError:
            return None
