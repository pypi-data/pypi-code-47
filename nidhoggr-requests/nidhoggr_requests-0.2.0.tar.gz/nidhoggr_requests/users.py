from typing import Dict, Optional

from nidhoggr_core.repository import BaseUserRepo
from nidhoggr_core.user import User

from nidhoggr_requests.core import RequestsRepo


class RequestsUserRepo(BaseUserRepo, RequestsRepo):
    def get_user(self, **kwargs: Dict[str, str]) -> Optional[User]:
        result = self.fetch(endpoint='/user/get', payload=kwargs)
        if result is not None:
            return User.parse_obj(result)

    def check_password(self, *, clean: str, uuid: str) -> bool:
        payload = {'uuid': uuid, 'password': clean}
        result = self.fetch(endpoint='/user/check_password', payload=payload)
        if result is not None:
            return result.get('authenticated', False)

    def save_user(self, *, user: User) -> bool:
        payload = user.dict()
        result = self.fetch(endpoint='/user/save', payload=payload)
        if result is not None:
            return result.get('saved', False)
