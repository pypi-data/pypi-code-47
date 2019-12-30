from botfriend.bot import TextGeneratorBot
from .mormon import Speaker

class BotOfMormon(TextGeneratorBot):

    def generate_text(self):
        return Speaker.random().speak()
        
    def stress_test(self, rounds):
        speaker = Speaker.random()
        for i in range(rounds):
            print(speaker.speak())

Bot = BotOfMormon
