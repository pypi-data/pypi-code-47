# -*- coding: utf-8 -*-
from typing import Optional, Union

import discord
from discord.ext.commands import Cog, command
from ruamel.yaml import YAML, StringIO
from snek import SNEK, SNEKContext

yaml = YAML()

yaml.boolean_representation = ['No', 'Yes']

strftime_format = "%c"


def dump_yaml(obj):
    sio = StringIO()

    yaml.dump(obj, sio)

    return sio.getvalue()


def format_url(url: discord.Asset):
    return str(url).strip("https://").strip("http://")


class FindResults:
    def __init__(self, channel, guild, user, member, role, message):
        self.channel: Optional[Union[discord.TextChannel, discord.VoiceChannel]] = channel
        self.guild: Optional[discord.Guild] = guild
        self.user: Optional[discord.User] = user
        self.member: Optional[discord.Member] = member
        self.message: Optional[discord.Message] = message
        self.role: Optional[discord.Role] = role


async def find(any_id: int, ctx: SNEKContext):
    bot = ctx.bot

    chan = bot.get_channel(any_id)

    if isinstance(chan, discord.DMChannel):
        chan = None

    guild = bot.get_guild(any_id)

    user = None
    try:
        user = await bot.fetch_user(any_id)
    except (discord.NotFound, discord.HTTPException, AttributeError):
        pass

    role = ctx.guild.get_role(any_id)

    member = None
    if user is not None:
        member = ctx.guild.get_member(any_id)

    message = None
    for ch in ctx.guild.channels:
        try:
            message = await ch.fetch_message(any_id)
            break
        except (discord.NotFound, discord.Forbidden, discord.HTTPException,
                AttributeError):
            pass

    return FindResults(chan, guild, user, member, role, message)


class Find(Cog):
    @command(hidden=True, aliases=['nani', '何', "なに", "what"])
    @SNEK.is_mod()
    async def find(self, ctx: SNEKContext, any_id: int):
        async with ctx.typing():
            results = await find(any_id, ctx)

            message = results.message
            channel = results.channel
            server = results.guild
            user = results.user
            member = results.member
            role = results.role

            result_y = {
                  "Results": {
                        "Message": "Not Found" if message is None else {
                              "Sent": f"{message.created_at.strftime(strftime_format)} GMT",
                              "By":   f"{message.author!s}",
                              "In":   f"#{message.channel.name}",
                        },
                        "Channel": "Not Found" if channel is None else {
                              "In":   f"^{channel.guild.name}",
                              "Name": f"#{channel.name}",
                        },
                        "Server":  "Not Found" if server is None else {
                              "Name": server.name,
                        },
                        "User":    "Not Found" if user is None else {
                              "Name": f"{user!s}",
                        },
                        "Member":  "Not Found" if member is None else {
                              "Nick": member.nick or "(not set)",
                        },
                        "Role":    "Not Found" if role is None else {
                              "Name": role.name,
                        }
                  }
            }

            await ctx.send(dump_yaml(result_y), lang="yaml")

    @command(hidden=True, aliases=["なにこれ", "何これ", "nanikore", "whatis"])
    @SNEK.is_mod()
    async def findmore(self, ctx: SNEKContext, any_id: int):
        async with ctx.typing():
            results = await find(any_id, ctx)

            message = results.message
            channel = results.channel
            guild = results.guild
            user = results.user
            member = results.member
            role = results.role

            result_y = {
                  "Results": {
                        "Message": "Not Found" if message is None else {
                              "Sent":    f"{message.created_at.strftime(strftime_format)} GMT",
                              "By":      f"{message.author!s} (@{message.author.id})",
                              "In":      f"#{message.channel.name} (@{message.channel.id})",

                              # extra
                              "Content": f"{message.content!r}",
                              "Embed":   message.embeds,
                              "Pinned":  "Yes" if message.pinned else "No",
                        },
                        "Channel": "Not Found" if channel is None else {
                              "In":          f"^{channel.guild.name}",
                              "Name":        f"#{channel.name}",

                              # extra
                              "Permissions": [{"target": {"id": o[0], "type": o[3]},
                                               "allow":  o[1], "deny": o[2]} for o in
                                              channel._overwrites],
                              # "Type": str(channel.type),
                              "Position":    channel.position,
                              "Topic":       channel.topic,

                              # created
                              "Created":     f"{channel.created_at.strftime(strftime_format)} GMT"
                        },
                        "Server":  "Not Found" if guild is None else {
                              "Name":    guild.name,

                              # extra
                              "Icon":    format_url(guild.icon_url_as(format="png")),
                              "Splash":  format_url(guild.splash_url_as(format="png")),
                              "OwnerID": f"@{guild.owner_id}",

                              # created
                              "Created": f"{guild.created_at.strftime(strftime_format)} GMT"
                        },
                        "User":    "Not Found" if user is None else {
                              "Name":    f"{user!s}",

                              # extra
                              "Avatar":  "(Default)" if user.avatar is None else
                                         format_url(user.avatar_url_as(format="png")),
                              "Bot":     "Yes" if user.bot else "No",

                              # created
                              "Created": f"{user.created_at.strftime(strftime_format)} GMT"
                        },
                        "Member":  "Not Found" if member is None else {
                              "Nick":   member.nick or "(not set)",

                              # extra
                              "Joined": f"{member.joined_at.strftime(strftime_format)} GMT",
                              "Roles":  {r.id: r.name for r in results.member.roles}
                        },
                        "Role":    "Not Found" if role is None else {
                              "Name":        f"{role.name!r}",

                              # extra
                              "Colour":      role.color.__str__(),
                              "Permissions": role.permissions.value,

                              # created
                              "Created":     f"{role.created_at.strftime(strftime_format)} GMT"
                        }
                  }
            }

            await ctx.send(dump_yaml(result_y), lang="yaml")


def setup(bot: SNEK):
    bot.add_cog(Find())
