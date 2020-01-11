import re

from discord.ext.commands import group, command
from pony.orm import Database, db_session, Required, PrimaryKey, commit
from snek import SNEK, UsesDatabase, IAlias, SNEKContext


class AliasCog(IAlias, UsesDatabase, name="Alias"):
    def __init__(self, bot):
        self.bot = bot  # type: SNEK

    async def do_db(self, db: Database) -> None:
        class Alias(db.Entity):
            key = PrimaryKey(str)
            val = Required(str)

        self.Alias = Alias

    def get(self, name):
        for k, v in self.get_all().items():
            if re.match(f"^{k}$", name):
                return v

    @db_session
    def get_all(self):
        j = dict()
        for p in self.Alias.select():
            j[p.key] = p.val
        return j

    @group()
    @SNEK.is_mod()
    async def alias(self, ctx: SNEKContext):
        """Set global aliases."""
        if ctx.invoked_subcommand is None:
            await ctx.send_help("alias")

    @alias.command(name="get")
    async def alias_get(self, ctx: SNEKContext, name: str):
        """Gets an alias from the database."""
        v = self.get(name)
        if v:
            await ctx.send(f"Alias {name!r}:\n    {v!r}")
        else:
            await ctx.send(f"Alias {name!r} does not exist.")

    @alias.command(name="set")
    async def alias_set(self, ctx: SNEKContext, name: str, *,
                        val: str):
        """Sets an alias."""
        with db_session:
            if not self.Alias.exists(key=name):
                self.Alias(key=name, val=val)
            else:
                self.Alias[name].set(val=val)

        await ctx.send("Set alias.")

    @alias.command(name="del")
    async def alias_del(self, ctx: SNEKContext, name: str):
        """Deletes an alias from the database."""
        with db_session:
            if self.Alias.exists(key=name):
                a = self.Alias[name]
                a_val = a.val
                a.delete()
                commit()
                await ctx.send("Deleted alias.")
                await self.bot.log(f"Alias {name!r} deleted, it contained {a_val!r}", _for="ALIAS")
            else:
                await ctx.send("Alias doesn't exist.")

    @command()
    async def aliases(self, ctx: SNEKContext):
        """List all known aliases."""
        await ctx.send(f"`Alias commands:`\n```py\n{self.get_formatted()}\n```",
                       no_code=True)


def setup(bot: SNEK):
    bot.add_cog(AliasCog(bot))
