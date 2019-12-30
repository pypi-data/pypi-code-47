from pdb import set_trace
import base64
import random
from botfriend.bot import TextGeneratorBot
from .fusion import Fusion

class FusionBot(TextGeneratorBot):

        BIO_TEMPLATE = "We are the Crystal Gems.\n(Right now, we are %s.)"

        def __init__(self, *args, **kwargs):
            super(FusionBot, self).__init__(*args, **kwargs)
            for publisher in self.publishers:
                if publisher.service == 'mastodon':
                    self.mastodon = publisher.api
        
        def generate_text(self):
            bot_state = self.model.json_state
            fusion = None
            new_fusion = False
            if not bot_state:
                fusion = Fusion.random()
                new_fusion = True
            else:
                # Maybe it's time to become a new fusion.
                if bot_state['toots'] > 12 and random.random() < 0.3:
                    old_name = bot_state['fusion']
                    new_name = old_name
                    while old_name == new_name:
                        fusion = Fusion.random()
                        new_name = fusion.name
                    new_fusion = True
                else:
                    fusion = Fusion(bot_state['fusion'])
            use = None
            while not use:
                use = fusion.assemble()
                if new_fusion:
                    use = fusion.name.upper() + ": " + use
                if len(use) > 500 or not ' ' in use:
                    use = None
            if new_fusion:
                bot_state = dict(fusion=fusion.name, toots=1)
                bio =  self.BIO_TEMPLATE % fusion.name
                avatar = self.local_path("data/avatars/%s.png" % fusion.name)
                avatar = open(avatar).read()
                avatar = "data:image/png;base64,%s" % base64.encodestring(avatar)
                self.mastodon.account_update_credentials(note=bio, avatar=avatar)
            else:
                bot_state['toots'] += 1
            self.model.json_state = bot_state
            return use

Bot = FusionBot
