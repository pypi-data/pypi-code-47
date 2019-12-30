from botfriend.bot import Bot as BasicBot
from botfriend.model import Post
import json

class MinecraftSignsBot(BasicBot):
    def _to_post_list(self, sign):
        """The input is a JSON list representing the four lines of text
        on a Minecraft sign.

        We turn this into a post by joining the four lines with newlines.
        """
        data = json.loads(sign)
        post, is_new = Post.from_content(self.model, "\n".join(data))
        return [post]

Bot = MinecraftSignsBot
