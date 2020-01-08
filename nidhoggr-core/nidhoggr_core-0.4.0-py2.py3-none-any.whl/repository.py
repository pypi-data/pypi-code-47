from abc import ABCMeta, abstractmethod
from typing import Dict, Optional, Union

from nidhoggr_core.response import StatusResponse, ErrorResponse
from nidhoggr_core.texture import TextureType, TextureItem
from nidhoggr_core.user import User


class BaseTextureRepo(metaclass=ABCMeta):
    variant: str

    @abstractmethod
    def get(self, *, uuid: str) -> Union[ErrorResponse, Dict[TextureType, TextureItem]]:
        pass


class BaseUserRepo(metaclass=ABCMeta):

    @abstractmethod
    def get_user(self, **kw: Dict[str, str]) -> Union[ErrorResponse, Optional[User]]:
        pass

    @abstractmethod
    def check_password(self, *, clean: str, uuid: str) -> StatusResponse:
        pass

    @abstractmethod
    def save_user(self, *, user: User) -> ErrorResponse:
        pass
