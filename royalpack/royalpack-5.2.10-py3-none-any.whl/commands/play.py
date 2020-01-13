import pickle
import base64
import discord
from typing import *
from royalnet.commands import *
from royalnet.utils import *
from royalnet.backpack.tables import User, Discord


class PlayCommand(Command):
    name: str = "play"

    aliases = ["p"]

    description: str = "Aggiunge un url alla coda della chat vocale."

    syntax = "{url}"

    async def get_url(self, args: CommandArgs):
        return args.joined(require_at_least=1)

    async def run(self, args: CommandArgs, data: CommandData) -> None:
        # if not (url.startswith("http://") or url.startswith("https://")):
        #     raise CommandError(f"Il comando [c]{self.interface.prefix}play[/c] funziona solo per riprodurre file da"
        #                        f" un URL.\n"
        #                        f"Se vuoi cercare un video, come misura temporanea puoi usare "
        #                        f"[c]ytsearch:nomevideo[/c] o [c]scsearch:nomevideo[/c] come url.")
        if self.interface.name == "discord":
            message: discord.Message = data.message
            guild: discord.Guild = message.guild
            if guild is None:
                guild_id = None
            else:
                guild_id: Optional[int] = guild.id
        else:
            guild_id = None

        user: User = await data.get_author()
        user_str = None

        if user is not None:
            try:
                user_discord: Discord = user.discord[0]
            except (AttributeError, IndexError):
                user_str = str(user)
            else:
                user_str = str(f"<@{user_discord.discord_id}>")

        self.loop.create_task(self.interface.call_herald_event("discord", "discord_play",
                                                               url=await self.get_url(args),
                                                               guild_id=guild_id,
                                                               user=user_str))

        # await data.reply("✅ Richiesta di riproduzione inviata!")
