from uuid import UUID

from app.helpers import AbstractAPIHelper

from config import config


class DeactivateAPIHelper(AbstractAPIHelper):

    @staticmethod
    async def call(user_site_uuid: UUID) -> bool:

        data = {
            "is_active": False
        }
        await AbstractAPIHelper._make_request(
            endpoint=config.BackendAPIEndpoints.BACKEND_API_ACTIVATE_USER.format(user_uuid=user_site_uuid),
            method_type=config.BackendAPIMethods.PATCH,
            data=data,
            need_authorization=True
        )
        return True
