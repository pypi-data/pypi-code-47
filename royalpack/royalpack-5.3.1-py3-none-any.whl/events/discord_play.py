import discord
import pickle
import base64
import datetime
from typing import *
from royalnet.commands import *
from royalnet.serf.discord import *
from royalnet.bard import *
from royalnet.backpack.tables.users import User
from ..utils import RoyalQueue


class DiscordPlayEvent(Event):
    name = "discord_play"

    async def run(self,
                  url: str,
                  guild_id: Optional[int] = None,
                  user: Optional[str] = None,
                  **kwargs) -> dict:
        if not isinstance(self.serf, DiscordSerf):
            raise UnsupportedError()

        serf: DiscordSerf = self.serf
        client: discord.Client = self.serf.client

        # TODO: fix this in Royalnet sometime
        candidate_players: List[VoicePlayer] = []
        for player in serf.voice_players:
            player: VoicePlayer
            if not player.voice_client.is_connected():
                continue
            if guild_id is not None:
                guild = client.get_guild(guild_id)
                if guild != player.voice_client.guild:
                    continue
            candidate_players.append(player)

        if len(candidate_players) == 0:
            raise UserError("Il bot non è in nessun canale vocale.\n"
                            "Evocalo prima con [c]summon[/c]!")
        elif len(candidate_players) == 1:
            voice_player = candidate_players[0]
        else:
            raise CommandError("Non so in che Server riprodurre questo file...\n"
                               "Invia il comando su Discord, per favore!")

        ytds = await YtdlDiscord.from_url(url)
        added: List[YtdlDiscord] = []
        too_long: List[YtdlDiscord] = []
        if isinstance(voice_player.playing, RoyalQueue):
            for index, ytd in enumerate(ytds):
                if ytd.info.duration >= datetime.timedelta(seconds=self.config["Play"]["max_song_duration"]):
                    too_long.append(ytd)
                    continue
                await ytd.convert_to_pcm()
                added.append(ytd)
                voice_player.playing.contents.append(ytd)
            if not voice_player.voice_client.is_playing():
                await voice_player.start()
        else:
            raise CommandError(f"Non so come aggiungere musica a [c]{voice_player.playing.__class__.__qualname__}[/c]!")

        main_channel: discord.TextChannel = client.get_channel(self.config["Discord"]["main_channel_id"])

        if len(added) > 0:
            if user:
                await main_channel.send(escape(f"▶️ {user} ha aggiunto {len(added)} file alla coda:"))
            else:
                await main_channel.send(escape(f"▶️ Aggiunt{'o' if len(added) == 1 else 'i'} {len(added)} file alla"
                                               f" coda:"))
        for ytd in added:
            await main_channel.send(embed=ytd.embed())

        if len(too_long) > 0:
            if user:
                await main_channel.send(escape(
                    f"⚠ {len(too_long)} file non {'è' if len(too_long) == 1 else 'sono'}"
                    f" stat{'o' if len(too_long) == 1 else 'i'} scaricat{'o' if len(too_long) == 1 else 'i'}"
                    f" perchè durava{'' if len(too_long) == 1 else 'no'}"
                    f" più di [c]{self.config['Play']['max_song_duration']}[/c] secondi."
                ))

        if len(added) + len(too_long) == 0:
            raise

        return {
            "added": [{
                "title": ytd.info.title,
                "stringified_base64_pickled_discord_embed": str(base64.b64encode(pickle.dumps(ytd.embed())),
                                                                encoding="ascii")
            } for ytd in added],
            "too_long": [{
                "title": ytd.info.title,
                "stringified_base64_pickled_discord_embed": str(base64.b64encode(pickle.dumps(ytd.embed())),
                                                                encoding="ascii")
            } for ytd in too_long]
        }
