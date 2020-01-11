import json
from typing import Union

import discord
from discord import User, Message
from discord.ext.commands import command, group
from discord.utils import snowflake_time
from pony.orm import Database, PrimaryKey, Required, db_session, Optional
from pony.orm.core import Entity, commit, select
from snek import SNEK, SNEKContext, AbstractCog, UsesDatabase


class QuoteCog(AbstractCog, UsesDatabase, name="Quote"):
    cache = {}

    BANNED = [
          "rename",
          "capture", "cap",
          "delete", "del",
          "info",
          "transfer",
          "list",
          "export",
          "random"
    ]

    async def do_db(self, db: Database) -> None:
        class SavedMessage(db.Entity):
            id = PrimaryKey(int, size=64)
            author = Required(int, size=64)
            channel = Required(int, size=64)
            guild = Required(int, size=64)
            content = Required(str, max_len=2000)
            _quote = Optional("Quote")

        class Quote(db.Entity):
            id = PrimaryKey(int, auto=True)
            name = Required(str, unique=True)
            owner = Required(int, size=64)
            message = Required(SavedMessage, unique=True)

        self.Quote = Quote
        self.SavedMessage = SavedMessage

    @staticmethod
    def trunctilldone(names):
        trunced = False
        while True:
            names_json = json.dumps(names)
            if len(names_json) + 12 > 2000:
                names.pop()
                trunced = True
            else:
                break

        return trunced, names_json

    def save_message(self, message: discord.Message) -> Entity:
        with db_session:
            if not self.SavedMessage.exists(id=message.id):
                saved_message = self.SavedMessage(
                      id=message.id,
                      author=message.author.id,
                      channel=message.channel.id,
                      guild=message.guild.id,
                      # content=message.content.replace('\ufe0f', '').encode('unicode-escape')
                      content=message.content
                )
            else:
                saved_message = self.SavedMessage.get(id=message.id)
            return saved_message

    async def make_embed(self, quote: Entity, ctx: SNEKContext) -> discord.Embed:
        with db_session:
            mess_owner = await ctx.get_user(quote.message.author)
            mess_content = quote.message.content

        if isinstance(mess_owner, discord.Member):
            color = mess_owner.color
        else:
            color = 0xAAAAAA

        embed = discord.Embed(
              # description=quote.message.content.encode("utf-8").decode("unicode-escape"),
              description=mess_content,
              color=color
        )
        embed.set_author(name=mess_owner.display_name,
                         icon_url=mess_owner.avatar_url)
        time = snowflake_time(quote.message.id)
        embed.set_footer(text=f"Message Quote | {time.strftime('%d/%m/%Y %H:%M')}")
        return embed

    ### COMMANDS

    @command(aliases=["an"])
    async def assignname(self, ctx: SNEKContext, name: str):
        """
        Assign a new name to a just-made quote.
        """
        if not self.cache.get(ctx.author.id):
            await ctx.send("You don't have an un-named quote cached!")
            return

        if name in self.BANNED:  # fixme: make this work better
            await ctx.send(
                  "Sorry, you cannot name your quote like one of the subcommands!"
            )
            return

        with db_session:
            if self.Quote.exists(name=name):
                await ctx.send(f'Cannot assign name; Quote "{name}" already exists.')
                return

        cached = self.cache.get(ctx.author.id)

        if not isinstance(cached, discord.Message):
            raise ValueError("assignname: cached value is not a discord message")

        with db_session:
            saved_message = self.save_message(cached)

            self.Quote(name=name, owner=ctx.author.id, message=saved_message)

        await ctx.send(f'Added quote "{name}"!')
        await ctx.bot.log(
              f"Quote '{name}' has been made (by {ctx.author}) (through assignname).",
              _for="QUOTE")

    @group(aliases=["q"], invoke_without_command=True)
    async def quote(self, ctx: SNEKContext, *, name: str):
        """Capture messages or abstract quotes"""
        if ctx.invoked_subcommand is not None:
            return

        if name == "":
            await ctx.send_help("quote")
            return

        with db_session:
            if not self.Quote.exists(name=name):
                await ctx.send(f'Quote "{name}" does not exist')
                return

            await ctx.send(embed=await self.make_embed(self.Quote.get(name=name), ctx))

    # @quote.command(name="add")
    # async def quote_add(self, ctx: SNEKContext, name: str, *, q: str):
    #     if await ctx.check_perm("capture_quote") is not True:
    #         await ctx.send(
    #               "You're not allowed to capture (and by extension, add) "
    #               "quotes, please ask for your "
    #               "local neighborhood moderator about this")
    #         return
    #
    #     if name in self.BANNED:
    #         self.cache[ctx.author.id] = q
    #         await ctx.send(
    #               "Sorry, you cannot name your quote like one of the "
    #               "subcommands!\nAssign a new "
    #               "name with '{}assignname <name>'!".format(
    #                     ctx.bot.command_prefix))
    #         return
    #
    #     if ctx.bot.db.quotes(ctx.bot.db.quotes.name == name):
    #         self.cache[ctx.author.id] = q
    #         await ctx.send(
    #               "\"{0}\" already exists, either change that, or/and assign a "
    #               "new name to your just-made quote "
    #               " with '{1}assignname <name>'! ".format(name,
    #                                                       ctx.bot.command_prefix))
    #         return
    #     ctx.bot.db.quotes.insert(name=name, ownedby=ctx.author.id,
    #                              ismessage=False, content=q)
    #     m = await ctx.send("Added quote \"{}\"!".format(name))
    #     await ctx.bot.log(
    #           "Quote '{}' has been made (by {}).".format(name, ctx.author),
    #           _for="QUOTE")
    #     await m.delete(delay=10)

    @quote.command(name="rename")
    async def quote_rename(self, ctx: SNEKContext,
                           oldname: str,
                           newname: str):
        if newname in self.BANNED:
            await ctx.send(
                  "Sorry, this name is one of the subcommands, can't name a "
                  "quote like that!")
            return

        with db_session:
            if not self.Quote.exists(name=oldname):
                await ctx.send(
                      "Hmmm, this quote does not seem to exist, did you miss-spell the first name?"
                )
            else:
                quote = self.Quote.get(name=oldname)
                if quote.owner == ctx.author.id or await ctx.mod():
                    if self.Quote.exists(name=newname):
                        await ctx.send(
                              "Oh, a quote with your new name already exists, "
                              "you cannot rename your quote to something that already exists!"
                        )
                    else:
                        quote.set(name=newname)
                        commit()
                        await ctx.send("Renamed!")
                        await ctx.bot.log(
                              f"Quote '{oldname}' has been renamed to '{newname}' (by {ctx.author}).",
                              _for="QUOTE"
                        )
                else:
                    await ctx.send(
                          f"Hmmm, you don't seem to be the owner of this quote, "
                          f"check with '{ctx.bot.command_prefix}quote info {oldname}'!"
                    )

    @quote.command(name="capture", aliases=["cap"])
    async def quote_capture(self, ctx: SNEKContext, name: str,
                            message: Message):
        if await ctx.check_perm("capture_quote") is False:
            await ctx.send(
                  "You're not allowed to capture quotes, please ask your moderator about this."
            )
            return

        if name in self.BANNED:  # fixme: think up better way to find banned words in quote names
            self.cache[ctx.author.id] = message
            await ctx.send(
                  "Sorry, you cannot name your quote like one of the subcommands!\n"
                  f"Assign a new name with '{ctx.bot.command_prefix}assignname <name>'!!")
            return

        with db_session:
            if self.Quote.exists(name=name):
                self.cache[ctx.author.id] = message
                await ctx.send(
                      f"{name!r} already exists, either change that, "
                      f"or/and assign a new name to your just-made quote with "
                      f"'{ctx.bot.command_prefix}assignname <name>'! ")
                return

            saved_message = self.save_message(message)

            self.Quote(name=name, owner=ctx.author.id, message=saved_message)

        await ctx.send(f"Added quote '{name}'!")
        await ctx.bot.log(
              f"Quote '{name}' has been captured (by {ctx.author}) (for message {message.id}).",
              _for="QUOTE"
        )

    @quote.command(name="delete", aliases=["del"])
    async def quote_delete(self, ctx: SNEKContext, name: str):
        with db_session:
            if not self.Quote.exists(name=name):
                await ctx.send(
                      "Hmmm, this quote does not seem to exist, did you miss-spell the name?"
                )
            else:
                quote = self.Quote.get(name=name)
                if quote.owner == ctx.author.id or await ctx.mod():
                    quote.delete()
                    commit()
                    await ctx.send("Quote deleted!")
                    await ctx.bot.log(
                          f"Quote '{name}' has been deleted (by {ctx.author!s}).",
                          _for="QUOTE"
                    )
                else:
                    await ctx.send(
                          "Hmmm, you don't seem to be the owner of this quote, "
                          f"check with '{ctx.bot.command_prefix}quote info {name}'!"
                    )

    @quote.command(name="info")
    async def quote_info(self, ctx: SNEKContext, name: str):
        with db_session:
            if not self.Quote.exists(name=name):
                await ctx.send(
                      "Hmmm, this quote does not seem to exist, did you miss-spell the name?"
                )
            else:
                quote = self.Quote.get(name=name)

                await ctx.send(
                      f'## Quote {name}:\n\n'
                      f'* Name: {name!r}\n'
                      f'* Owner: '
                      f'{(quote.owner == ctx.author.id and "You!") or await ctx.bot.fetch_user(quote.owner)!s}\n'
                      f'* Quoted User ID: @{quote.message.author}\n'
                      f'* Message ID: @{quote.message.id}\n'
                      f'* Channel ID: @{quote.message.channel}', lang="md"
                )

    @quote.command(name="transfer")
    async def quote_transfer(self, ctx: SNEKContext, name: str,
                             new_owner: Union[User, str]):
        with db_session:
            if not self.Quote.exists(name=name):
                await ctx.send(
                      "Hmmm, this quote does not seem to exist, did you miss-spell the name?"
                )
            else:
                quote = self.Quote.get(name=name)
                ismod = await ctx.mod()
                if quote.owner == ctx.author.id or ismod:
                    if isinstance(new_owner, User) or (ismod and new_owner == "me"):
                        new_owner_id: int
                        if ismod and new_owner == "me":
                            new_owner_id = ctx.author.id
                        else:
                            new_owner_id = new_owner.id

                        quote.set(owner=new_owner_id)
                        commit()

                        await ctx.send("Transferred!")
                        await ctx.bot.log(
                              f"Quote '{name}' has been transferred to {new_owner_id} (by {ctx.author}).",
                              _for="QUOTE"
                        )
                    else:
                        await ctx.send('Sorry, the new owner does not look like a user mention')

    @quote.group(name="random", invoke_without_command=True)
    async def quote_random(self, ctx: SNEKContext):
        """Selects a random quote from the database."""
        if ctx.invoked_subcommand is not None:
            return

        with db_session:
            quote_l: Entity = self.Quote.select_random(1)

            if len(quote_l) == 0:
                await ctx.send(
                      f"No quotes exist (yet), make some with {ctx.bot.command_prefix}quote capture <message_id>!")
                return
            else:
                quote = quote_l[0]

            await ctx.send(f'Quote {quote.name!r}:', embed=await self.make_embed(quote, ctx))

    @quote_random.command(name="from")
    async def quote_random_from(self, ctx: SNEKContext, user: User):
        """Selects a random quote made by a user."""
        with db_session:
            quotes = select(q for q in self.Quote if q.owner == user.id).random(1)

            if len(quotes) == 0:
                await ctx.send("Sorry, but there are no quotes made by that user.")
                return
            else:
                quote = quotes[0]

            await ctx.send(f'Quote {quote.name!r}:', embed=await self.make_embed(quote, ctx))

    @quote_random.command(name="about")
    async def quote_random_about(self, ctx: SNEKContext, user: User):
        """Selects a random message quote about a user."""
        with db_session:
            messages = select(m for m in self.SavedMessage
                              if m.author == user.id and m._quote is not None).random(1)

            if len(messages) == 0:
                await ctx.send("Sorry, but there are no quotes about that user.")
                return
            else:
                quote = messages[0]._quote

            await ctx.send(f'Quote {quote.name!r}:', embed=await self.make_embed(quote, ctx))

    @quote.command(name="export")
    async def quote_export(self, ctx: SNEKContext):
        await ctx.send("Not yet implimented")  # TODO

        # if len(info.args) == 1:
        #     trunced, names_json = trunctilldone([r.name for r in info.db().select(info.db.quotes.name)])
        #
        #     if trunced:
        #         await info.PM("The results had to the truncated, use '\\quote export complete' to get a json file "
        #                       "with all quotes!")
        #     await info.PM("```json\n{}\n```".format(names_json), nocode=True)
        #     await info.reply("Sent to PM!")
        # elif 3 >= len(info.args) >= 2:
        #     complete = False
        #
        #     if "complete" in info.args:
        #         complete = True
        #         info.args.remove("complete")
        #
        #     if len(info.args) == 2:
        #         query = info.args[1]
        #     else:
        #         query = None
        #
        #     if query:
        #         names = [r.name for r in info.db().select(info.db.quotes.name)]
        #     elif not complete:
        #         if not user_re.match(query) and query != "public":
        #             await info.reply('Sorry, that does not look like "public" or an user mention')
        #             return
        #
        #         of = query == "public" and query or user_re.match(query).group(1)
        #         names = [r.name for r in info.db(info.db.quotes.ownedby == of).select(info.db.quotes.name)]
        #     else:
        #         names = [r.name for r in info.db().select(info.db.quotes.name)]
        #
        #     names.sort()
        #
        #     if complete:
        #         names_json = json.dumps(names)
        #         await info.typing()
        #         await info.client.send_file(info.author, StringIO(names_json), filename="quote_names.json")
        #         m = await info.reply("Sent to PM!")
        #     else:
        #         trunced, names_json = trunctilldone(names)
        #
        #         if trunced:
        #             await info.PM(
        #                 "The results had to the truncated, use '\\quote export complete' to get a json file "
        #                 "with all quotes!")
        #         await info.PM("```json\n{}\n```".format(names_json), nocode=True)
        #         m = await info.reply("Sent to PM!")
        #     await dwml(m)
        #
        # else:
        #     raise Exception()

    @quote.group(name="list")
    async def quote_list(self, ctx: SNEKContext):
        if ctx.invoked_subcommand is None:
            await ctx.send_help("quote list")

    @quote_list.command("from")
    async def quote_list_from(self, ctx: SNEKContext, user: User):
        with db_session:
            rows = [row.name for row in select(q for q in self.Quote if q.owner == user.id)]

        trunced, names_json = self.trunctilldone(rows)

        if trunced:
            await ctx.send("The results had to the truncated.")
        await ctx.send("```json\n{}\n```".format(names_json), no_code=True)

    @quote_list.command("about")
    async def quote_list_about(self, ctx: SNEKContext, user: User):
        with db_session:
            rows = [r._quote.name for r in select(m for m in self.SavedMessage
                                                  if m.author == user.id and m._quote is not None)]

        trunced, names_json = self.trunctilldone(rows)

        if trunced:
            await ctx.send("The results had to the truncated.")
        await ctx.send(f"```json\n{names_json}\n```", no_code=True)


def setup(bot: SNEK):
    bot.add_cog(QuoteCog(bot))
