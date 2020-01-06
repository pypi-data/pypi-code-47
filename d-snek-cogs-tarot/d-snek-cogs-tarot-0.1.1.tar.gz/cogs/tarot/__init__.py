import re
import time
from random import shuffle
from typing import Optional

from discord import Embed
from discord.ext.commands import Cog, command
from snek import SNEK, SNEKContext

from .t_data import gen_deck, tarot_spreads, all_cards

QUARTER = 15 * 60
TAROT_CARD_FORMAT = """You picked "{}"
Which stands for:
```
{}
```({})"""
CHOICES = list({i * i2 for i2 in range(1, 21) for i in range(1, 9)})
EMOJIS = ['📗', '🔷', '🔴']
DECK = gen_deck()

__all__ = ['Tarot', 'setup']


def do_the_harlem_shuffle():
    shuffle(DECK)


class Tarot(Cog):
    def __init__(self, bot: SNEK):
        self.bot = bot
        self.latest_cards = {}

    @command()
    async def tarot(self, ctx: SNEKContext):
        C = await self.pick_card(ctx)

        if C is not None:
            await ctx.send(TAROT_CARD_FORMAT.format(C.name, C.formatted_fields, C.skin()), no_code=True)
            self.latest_cards[ctx.author.id] = (C, time.time(), ctx.channel.id)

    @command()
    async def spread(self, ctx: SNEKContext, *, name: str):
        sp = tarot_spreads.get(name)
        if not sp:
            await ctx.send("Sorry, I don't know this spread, use !help spread for available spreads.\n"
                           f"Contact @{await self.bot.owner()!s} to suggest a spread.")
        else:
            results = {}
            for r in sp['each']:
                m = await ctx.send(r + ":")
                res = await self.pick_card(ctx, [val for val in results.values()])
                await m.delete()
                if not res:
                    await ctx.send("Spread failed, stopping...")
                    return
                results[r] = res

            a = "`Results:`\n"
            for r in sp['each']:
                a += f'`{r}:` "{results[r].name}"\n'

            await ctx.send(a, no_code=True)

    @command(aliases=["card"])
    async def explain(self, ctx: SNEKContext, *, card: Optional[str]):
        async def splain(card):
            embed = Embed(title=card.name, color=0x308DFC)
            embed.set_thumbnail(url=card.skin())
            for k, v in card.fields.items():
                embed.add_field(name=k.capitalize(), value=v, inline=True)
            embed.set_footer(text="Tarot card picker")
            await ctx.send(embed=embed)

        c = self.latest_cards.get(ctx.author.id)

        if card is None:
            if c and (time.time() - c[1]) < QUARTER and c[2] == ctx.channel.id:
                await splain(c[0])
            else:
                await ctx.send_help("explain")
        else:
            c = all_cards.get(card.lower())
            if c:
                await splain(c)
            else:
                await ctx.send(
                      "Card not found. (try names like \"the fool\", or \"the tower\", or \"ace of pentacles\")")

    async def pick_card(self, ctx: SNEKContext, exclude=[]):
        msg = await ctx.send("Pick some of these, and type a number from 1 to 20.")
        for e in EMOJIS:
            await msg.add_reaction(e)
        i = await self.bot.wait_for("message", check=lambda m: m.channel == ctx.channel and m.author == ctx.author)
        msg = await ctx.fetch_message(msg.id)
        first = 1
        second = None
        for r in [r.emoji for r in msg.reactions if r.count > 1 and r.emoji in EMOJIS]:
            first += 2 ** EMOJIS.index(r)
        if re.match(r'^\d+$', i.content) and 1 <= int(i.content) <= 20:
            second = int(i.content)
        else:
            await ctx.send("This is either not a number or not one from 1 to 20, try again.")

        the_number = None
        if second is not None:
            the_number = CHOICES.index(first * second)

        await msg.delete()
        await i.delete()

        if the_number is not None:
            while True:
                if the_number > 77:
                    the_number = the_number - ((the_number % 77) * 2)
                card = DECK[the_number]
                if card not in exclude:
                    break
                the_number += 1
            do_the_harlem_shuffle()
            return card


def setup(bot: SNEK):
    bot.add_cog(Tarot(bot))
