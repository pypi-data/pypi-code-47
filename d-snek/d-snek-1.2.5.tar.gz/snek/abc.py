from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Optional, Union

from discord import Guild, Member, TextChannel
from discord.ext.commands import Bot, Cog, CogMeta
from pony.orm import Database


class UsesDatabase(metaclass=ABCMeta):
    db: Database

    def add_db(self, db: Database) -> None:
        self.db = db

    @abstractmethod
    async def do_db(self, db: Database) -> None:
        ...


class CogABCMeta(CogMeta, ABCMeta):
    pass


class AbstractCog(Cog, metaclass=CogABCMeta):
    pass


class IUseCase(AbstractCog):
    def __init__(self, bot: Bot):
        self.bot = bot

    def main_server(self) -> Optional[Guild]:
        return self.bot.get_guild(self.main_server_id)

    @property
    @abstractmethod
    def main_server_id(self) -> int:
        ...

    @abstractmethod
    def log_channel(self, server: Optional[Union[int, Guild]]) -> Optional[TextChannel]:
        ...


class IPerm(AbstractCog):
    @dataclass
    class PGroup:
        name: str
        order: int
        roles: List[int]
        data: Dict[str, bool]
        perm: bool

    @abstractmethod
    async def check_perm(
        self, perm: str, guild: Guild, author: Member
    ) -> Optional[bool]:
        ...

    @abstractmethod
    def get_pgroup(self, group: str) -> Optional["PGroup"]:
        ...


class IAlias(AbstractCog):
    @abstractmethod
    def get(self, name: str) -> Optional[str]:
        ...

    @abstractmethod
    def get_all(self) -> Dict[str, str]:
        ...

    def get_formatted(self) -> List[str]:
        everything = self.get_all()
        new = set()
        for k in everything.keys():
            if "+" in k:
                new.add("/{}/ (regex)".format(k))
            else:
                new.add("{}".format(k))
        return list(new)
