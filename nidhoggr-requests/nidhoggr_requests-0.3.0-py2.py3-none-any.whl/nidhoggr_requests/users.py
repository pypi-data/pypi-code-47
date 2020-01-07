from typing import Dict, Optional, Union

from nidhoggr_core.repository import BaseUserRepo
from nidhoggr_core.response import StatusResponse
from nidhoggr_core.user import User

from nidhoggr_requests.core import RequestsRepo


class RequestsUserRepo(BaseUserRepo, RequestsRepo):
    def get_user(self, **kwargs: Dict[str, str]) -> Union[StatusResponse, Optional[User]]:
        result = self.fetch(endpoint='/user/get', payload=kwargs)

        if result is StatusResponse:
            return result

        if not result:
            # Encode absence of user as emtpy JSON object on transport layer
            # However, this is still valid response
            return None

        return User.parse_obj(result)

    def check_password(self, *, clean: str, uuid: str) -> StatusResponse:
        payload = {'uuid': uuid, 'password': clean}
        result = self.fetch(endpoint='/user/check_password', payload=payload)

        if result is StatusResponse:
            return result

        return StatusResponse(**result)

    def save_user(self, *, user: User) -> StatusResponse:
        payload = user.dict()
        result = self.fetch(endpoint='/user/save', payload=payload)

        if result is StatusResponse:
            return result

        return StatusResponse(**result)
