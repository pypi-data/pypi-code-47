import logging
import os
import pathlib
from typing import Dict, Optional

from pony.orm import Database, set_sql_debug

from snek import SNEK
from snek.abc import AbstractCog, UsesDatabase

logger = logging.getLogger(__name__)


class DataBaseCog(AbstractCog):
    def __init__(self, bot: SNEK):
        self.bot: SNEK = bot
        self.db = Database()
        set_sql_debug(self.bot.debug)

    @property
    def config(self) -> Optional[Dict[str, str]]:
        c = self.bot.env.dict(
            "SNEK_DB", {"provider": "sqlite", "filename": ":memory:"}, subcast=str
        )

        if (
            "filename" in c
            and c["filename"] != ":memory:"
            and not os.path.isabs(c["filename"])
        ):
            c["filename"] = str(pathlib.Path(os.getcwd()) / c["filename"])
            c["create_db"] = True

        return c

    async def map_db(self) -> None:
        for cog in self.bot.cogs.values():
            if isinstance(cog, UsesDatabase):
                cog.add_db(self.db)
                await cog.do_db(self.db)

        logger.debug(f"Binding database with {self.config}")

        self.db.bind(**self.config)

        self.db.generate_mapping(create_tables=True)


def setup(bot: SNEK) -> None:
    bot.add_cog(DataBaseCog(bot))
