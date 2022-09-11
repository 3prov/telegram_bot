from abc import abstractmethod
from urllib.parse import urljoin
from uuid import UUID

import aiohttp

from config import config


class AbstractAPIHelper:

    @staticmethod
    @abstractmethod
    async def call(user_site_uuid: UUID) -> None:
        raise NotImplementedError

    @staticmethod
    async def _make_request(
        endpoint: config.BackendAPIEndpoints,
        method_type: config.BackendAPIMethods,
        data: dict,
        need_authorization: bool = False
    ) -> dict:
        headers = dict()
        if need_authorization:
            headers['Authorization'] = f'Token {config.BACKEND_API_TOKEN}'

        async with aiohttp.ClientSession() as session:
            match method_type:
                case method_type.PATCH:
                    async with session.patch(urljoin(
                        config.BACKEND_API_BASE_URL, endpoint), data=data, headers=headers,
                    ) as resp:
                        if resp.status != 200:
                            raise Exception(f'Backend API returned: {await resp.text()}')  # FIXME: add custom exception
                        return await resp.json()

                case method_type.POST:
                    async with session.post(urljoin(
                            config.BACKEND_API_BASE_URL, endpoint), data=data, headers=headers,
                    ) as resp:
                        if resp.status != 201:
                            raise Exception(f'Backend API returned: {await resp.text()}')  # FIXME: add custom exception
                        return await resp.json()
