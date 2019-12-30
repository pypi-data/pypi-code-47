from pdb import set_trace
from botfriend.bot import TextGeneratorBot
import json
from .ghostbusters import GhostbusterCastingOffice

class GhostbustersBot(TextGeneratorBot):

    def generate_text(self):
        office = GhostbusterCastingOffice(self.model.state)
        tweet = office.tweet()
        self.model.state = json.dumps(office.recently_used)
        return tweet
    
    def stress_test(self, rounds):
        office = GhostbusterCastingOffice(self.model.state)
        for i in range(rounds):
            print(office.tweet())

Bot = GhostbustersBot
