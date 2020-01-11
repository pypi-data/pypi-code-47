import re
from typing import Optional

from discord.ext.commands import command
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientRateLimitError
from snek import SNEK, SNEKContext, AbstractCog

imgur_re = re.compile(r'https?://\S+?\.(png|jpe?g|bmp|gif)')


class ImgurCog(AbstractCog, name="Imgur"):

    def __init__(self, bot: SNEK):
        self.client_id = bot.env.str("IMGUR_CLIENT_ID", None)
        self.client_secret = bot.env.str("IMGUR_CLIENT_SECRET", None)
        if self.client_id is None or self.client_secret is None:
            raise KeyError(
                  "Need both IMGUR_CLIENT_ID and IMGUR_CLIENT_SECRET environment variables "
                  "for imgur photo uploading to work"
            )
        self.imgurc = ImgurClient(self.client_id, self.client_secret)

    @command(aliases=["i"])
    async def imgur(self, ctx: SNEKContext, url: Optional[str]):
        """Upload an image to imgur

        Upload 1 image alongside the command, or give an image url."""
        if url is None:
            try:
                ctx.message.attachments[0].height
            except Exception:
                await ctx.send("Sorry, but that doesn't look like an image...")
                await ctx.send_help("imgur")
                return
            else:
                url = ctx.message.attachments[0].url

        if imgur_re.match(url):
            async with ctx.typing():
                try:
                    await ctx.send(
                          self.imgurc.upload_from_url(url).get("link").replace(
                                ".jpg", ".png"), nocode=True)
                except ImgurClientRateLimitError as e:
                    await ctx.send("Rate limit exceeded!")
                    raise e
        else:
            await ctx.send(
                  "Sorry, but that doesn't seem to look like an image URL. "
                  "(It has to have https:// at the beginning and end with extension png, jpg, jpeg, etc.)"
            )
            return


def setup(bot: SNEK):
    bot.add_cog(ImgurCog(bot))
