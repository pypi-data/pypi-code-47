import re
from datetime import timedelta, datetime
from typing import Optional

from discord import Member, User
from discord.ext.commands import command, group
from emoji import demojize
from pony.orm import Database, PrimaryKey, Required, db_session
from snek import SNEK, SNEKContext, UsesDatabase, AbstractCog

cust_em_re = re.compile(r"<a?:([^:\s]+):(\d+)>")
emoji_pattern = re.compile(r"^:\S+:$", flags=re.UNICODE)


class Send(AbstractCog, UsesDatabase):
    async def do_db(self, db: Database) -> None:
        class Send(db.Entity):
            id = PrimaryKey(int, auto=True)
            sender = Required(int, size=64)
            receiver = Required(int, size=64)
            what = Required(str)
            at = Required(datetime)

        self.Send = Send

    @command(aliases=["give"])
    async def send(self, ctx: SNEKContext, user: Member, emoji: str):
        emoji = emoji.strip("\ufe0f")
        if cust_em_re.match(emoji):
            await ctx.send(
                "That is a custom emoji, I don't support those (yet), sorry!"
            )
            return
        elif not emoji_pattern.match(demojize(emoji)) or demojize(emoji) == emoji:
            owner = await ctx.bot.owner()
            await ctx.send(
                f"I don't know if this is an emoji or not, message @{owner!s} if it is, please!"
            )
            await owner.send(f"`Emoji not detected;{demojize(emoji)} % {emoji}`")
            return
        elif not re.match(r"^:[^:]+:$", demojize(emoji)):
            await ctx.send("These are multiple emojis!")
            return

        with db_session:
            last = self.Send.select(
                lambda s: s.sender == ctx.author.id and s.receiver == user.id
            ).first()

        now = datetime.now()

        if last is not None and (now - last.at) < timedelta(hours=1):
            await ctx.send(
                "You have already sent an emoji to this user in the last hour!"
            )
            return
        elif user == ctx.author:
            await ctx.send("Sorry, but you can't send something to yourself.")
            return
        else:
            with db_session:
                self.Send(sender=ctx.author.id, receiver=user.id, what=emoji, at=now)

            await ctx.send(f"You've given {emoji!r} to @{user!s}!")

    def user_emojis(self, user: User, lately: bool = False):
        with db_session:
            emojis = self.Send.select(lambda s: s.receiver == user.id)[:]

            if emojis:
                emojis = list(emojis)

                if lately:
                    now = datetime.now()
                    emojis = [e for e in emojis if (now - e.at) < timedelta(weeks=1)]

            return emojis

    def top_ten(self, emojis: list):
        everything = {}

        for emoji in emojis:
            everything[emoji.what] = (
                everything.get(emoji.what) and everything[emoji.what] + 1
            ) or 1

        return sorted(
            [ev for ev in everything.items()], key=lambda a: a[1], reverse=True
        )[:10]

    @group()
    async def jar(self, ctx: SNEKContext, of: Optional[User]):
        """Shows top 10 received emojis of all time."""
        if ctx.invoked_subcommand is None:
            emojis = self.user_emojis(of or ctx.author)
            top10 = self.top_ten(emojis)
            formatted_list = "\n".join(f"`{i[1]:4d} times:` {i[0]}" for i in top10)

            await ctx.send(
                f"`Emojis sent:`\n\n{formatted_list}", no_code=True,
            )

    @jar.command(name="amount")
    async def jar_amount(self, ctx: SNEKContext, of: Optional[User]):
        """Shows top 10 people who sent emojis, and the amount."""
        emojis = self.user_emojis(of or ctx.author)
        top10 = self.top_ten(emojis)
        formatted_list = "\n".join(
            f"{str(ctx.guild.get_member(i[0])):20} sent {i[1]} emojis"
            for i in top10
            if ctx.guild.get_member(i[0])
        )

        await ctx.send(f"Emojis sent by people:\n\n{formatted_list}")

    @jar.command(name="lately")
    async def jar_lately(self, ctx: SNEKContext, of: Optional[User]):
        """Shows top 10 received emojis from last week."""
        emojis = self.user_emojis(of or ctx.author, True)
        top10 = self.top_ten(emojis)
        formatted_list = "\n".join(f"`{i[1]:4d} times:` {i[0]}" for i in top10)

        await ctx.send(
            f"`Emojis sent:`\n\n{formatted_list}", no_code=True,
        )

    @jar.command(name="recently")
    async def jar_recently(self, ctx: SNEKContext):
        """Shows last 10 received emojis"""
        await ctx.send("Not yet implemented")  # TODO

    @jar.command(name="report")
    async def jar_report(self, ctx: SNEKContext):
        await ctx.send("Not yet implemented")  # TODO


def setup(bot: SNEK):
    bot.add_cog(Send(bot))
