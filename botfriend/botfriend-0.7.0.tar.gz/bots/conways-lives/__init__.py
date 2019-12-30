from botfriend.bot import Bot as BasicBot
import json
from botfriend.model import Post

class ConwayBot(BasicBot):

    def _to_post_list(self, content):
        """The input is a JSON string, not a regular Python string."""
        content = json.loads(content)
        return super(ConwayBot, self)._to_post_list(content)
Bot = ConwayBot

