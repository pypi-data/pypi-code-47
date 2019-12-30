from botfriend.bot import TextGeneratorBot

class LimerickBot(TextGeneratorBot):
    
    def generate_text(self):
        from .limerick import Limerick
        return str(Limerick())

Bot = LimerickBot
