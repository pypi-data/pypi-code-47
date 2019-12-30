from botfriend.bot import TextGeneratorBot
from olipy.gibberish import Gibberish

class SmoothUnicodeBot(TextGeneratorBot):

    def generate_text(self):
        return Gibberish.random().tweet()

Bot = SmoothUnicodeBot
