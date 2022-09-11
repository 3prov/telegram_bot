from __future__ import annotations

from datetime import datetime
from uuid import UUID

from aredis_om import Field
from redis_om import Migrator

from app.models import BaseModel


class UserModel(BaseModel):
    telegram_id: int = Field(index=True)
    site_uuid: UUID = Field(index=True)
    join_date: datetime = datetime.now()
    active: str = Field(index=True)  # TODO: replace to bool - https://github.com/redis/redis-om-python/issues/193

    @classmethod
    async def get_by_telegram_id(cls, telegram_id: int) -> UserModel | None:
        return await cls.find_one(cls.telegram_id == telegram_id)

    @classmethod
    async def is_exist(cls, telegram_id: int) -> bool:
        return await cls.get_by_telegram_id(telegram_id) is not None

    @classmethod
    async def is_active(cls, telegram_id: int) -> bool:
        user = await cls.get_by_telegram_id(telegram_id)
        return user.active == 'True' if user else False  # FIXME: https://github.com/redis/redis-om-python/issues/193

    async def activate(self) -> None:
        self.active = 'True'  # FIXME: https://github.com/redis/redis-om-python/issues/193
        await self.save()

    async def deactivate(self) -> None:
        self.active = 'False'  # FIXME: https://github.com/redis/redis-om-python/issues/193
        await self.save()


Migrator().run()
