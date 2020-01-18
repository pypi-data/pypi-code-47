import logging
import os
import platform
import pprint
import sys

from discord import DMChannel, GroupChannel, Message
from discord.ext.commands import Cog

from snek import SNEK
from snek.abc import AbstractCog

logger = logging.getLogger(__name__)


class IdentityCog(AbstractCog):
    def __init__(self, bot: SNEK):
        self.bot: SNEK = bot

    @Cog.listener()  # type: ignore  # fixme
    async def on_message(self, message: Message) -> None:
        content: str = message.content
        if isinstance(message.channel, (DMChannel, GroupChannel)):
            if message.author == (await self.bot.owner()):
                if content in [">identify", ">identity"]:
                    login = hasattr(os, "getlogin") and os.getlogin() or None

                    identity = {
                        "exec_prefix": sys.exec_prefix,
                        "executable": sys.executable,
                        "implementation": sys.implementation.__dict__,
                        "login": login,
                        "uname": platform.uname(),
                    }
                    await message.channel.send(
                        f"`IDENTITY:`\n```py\n{pprint.pformat(identity)}\n```"
                    )
                elif content == ">pid":
                    await message.channel.send(f"`PID:`\n```py\n{os.getpid()!r}\n```")
                elif content == ">prefix":
                    await message.channel.send(
                        f"`PREFIX:`\n```py\n{self.bot.command_prefix!r}\n```"
                    )
                elif content == ">cogs":
                    cogs = {k: v.__module__ for k, v in self.bot.cogs.items()}
                    await message.channel.send(
                        f"`COGS:`\n```py\n{pprint.pformat(cogs)}\n```"
                    )
                elif content == ">extensions":
                    extensions = {k: v.__name__ for k, v in self.bot.extensions.items()}
                    await message.channel.send(
                        f"`EXTENSIONS:`\n```py\n{pprint.pformat(extensions)}\n```"
                    )
            if content == ">owner":
                await message.channel.send(
                    f"`OWNER:`\n```py\n{(await self.bot.owner()).id}\n```"
                )


def setup(bot: SNEK) -> None:
    bot.add_cog(IdentityCog(bot))
