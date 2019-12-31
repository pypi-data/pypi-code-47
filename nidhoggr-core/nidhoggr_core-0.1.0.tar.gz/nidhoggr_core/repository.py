from abc import ABCMeta, abstractmethod
from typing import Dict, Optional

from nidhoggr_core.user import User
from nidhoggr_core.texture import TextureType, TextureItem


class BaseTextureRepo(metaclass=ABCMeta):
    variant: str

    @abstractmethod
    def get(self, *, uuid: str) -> Dict[TextureType, TextureItem]:
        pass


class BaseUserRepo(metaclass=ABCMeta):

    @abstractmethod
    def get_user(self, **kw: Dict[str, str]) -> Optional[User]:
        pass

    @abstractmethod
    def check_password(self, *, clean: str, uuid: str) -> bool:
        pass

    @abstractmethod
    def save_user(self, *, user: User) -> bool:
        pass
