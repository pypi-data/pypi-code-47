from pydantic import BaseModel
import typing
from loguru import logger


class AuthUser(BaseModel):
    name: str
    secret: str
    allow_table: typing.Set[str]


class AuthManager(object):
    _user_dict: typing.Dict[str, AuthUser] = {}

    def __init__(self):
        raise NotImplementedError("SINGLETON CLASS")

    @classmethod
    def is_user_existed(cls, name: str) -> bool:
        return name in cls._user_dict

    @classmethod
    def add(cls, new_user: AuthUser) -> bool:
        name = new_user.name

        if cls.is_user_existed(name):
            logger.warning(f"user {name} already existed")
            return False
        cls._user_dict[name] = new_user
        return True

    @classmethod
    def remove(cls, old_user: AuthUser) -> bool:
        name = old_user.name

        if not cls.is_user_existed(name):
            logger.warning(f"user {name} not existed")
            return False
        del cls._user_dict[name]
        return True

    @classmethod
    def is_allowed(cls, name: str, secret: str, table: str) -> bool:
        # exist
        if not cls.is_user_existed(name):
            logger.warning(f"user {name} is not existed")
            return False
        user = cls._user_dict[name]

        # secret
        if not (user.secret == secret):
            logger.warning(f"user {name}'s secret does not match")
            return False

        # allow
        logger.debug(f"user {name} can access: {user.allow_table}")
        return table in user.allow_table
