from abc import ABCMeta, abstractmethod
from typing import Optional, List, Dict, NamedTuple

from pydantic import BaseModel

from nidhoggr.models.session import UserProperty
from nidhoggr.models.texture import TextureType, TextureItem
from nidhoggr.utils.crypto import KeyPair


class User(BaseModel):
    uuid: str
    login: str
    email: str
    access: Optional[str] = None
    client: Optional[str] = None
    server: Optional[str] = None
    properties: List[UserProperty] = []

    class Config:
        allow_mutation = False


class BLConfig(NamedTuple):
    key_pair: KeyPair
    strict: bool = False
    simple_login: bool = True
    legacy_compat: bool = True


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


class BaseTextureRepo(metaclass=ABCMeta):
    variant: str

    @abstractmethod
    def get(self, *, uuid: str) -> Dict[TextureType, TextureItem]:
        pass
