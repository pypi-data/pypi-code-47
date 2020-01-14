from abc import ABC, abstractmethod
from typing import Optional, Type

from pony.orm.core import Entity, Database, PrimaryKey, Required, db_session
from snek import SNEK, AbstractCog, UsesDatabase


class Sona(AbstractCog, ABC, UsesDatabase):
    def __init__(self, bot):
        self.bot: SNEK = bot

    SonaStore: Optional[Type[Entity]] = None

    async def do_db(self, db: Database) -> None:
        if self.SonaStore is not None:
            return

        class SonaStore(db.Entity):
            guild = Required(int, size=64)
            user = Required(int, size=64)
            type = Required(str)
            url = Required(str)

            PrimaryKey(guild, user, type)

        self.SonaStore = SonaStore

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    def get_sona(self, guild: int, user: int) -> Optional[str]:
        with db_session:
            sona = self.SonaStore.get(guild=guild, user=user, type=self.type)

            return sona and sona.url

    def set_sona(self, guild: int, user: int, url: str) -> None:
        with db_session:
            sona = self.SonaStore.get(guild=guild, user=user, type=self.type)

            if sona is not None:
                sona.set(url=url)
            else:
                self.SonaStore(guild=guild, user=user, type=self.type, url=url)

    def del_sona(self, guild: int, user: int) -> bool:
        with db_session:
            sona = self.SonaStore.get(guild=guild, user=user, type=self.type)

            if sona is not None:
                sona.delete()
                return True
            else:
                return False
