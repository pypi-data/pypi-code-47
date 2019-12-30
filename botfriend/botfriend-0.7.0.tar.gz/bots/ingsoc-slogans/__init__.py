from pdb import set_trace
import random
import string
from botfriend.bot import TextGeneratorBot
from olipy import corpora

# Requires `pip install PyDictionary`
#from PyDictionary import PyDictionary

class SloganBot(TextGeneratorBot):

    BIO_TEMPLATE = "The Party's eternal slogans are your surest ally in the war against %s."
    
    def __init__(self, *args, **kwargs):
        super(SloganBot, self).__init__(*args, **kwargs)
        for publisher in self.publishers:
            if publisher.service == 'twitter':
                self.twitter = publisher.api
            elif publisher.service == 'mastodon':
                self.mastodon = publisher.api
        #self.dictionary = PyDictionary()
        
    @property
    def slogan(self):
        if random.random() < 0.25:
            corpus = 'abstract_nouns'
        else:
            corpus = 'adjectives'
        data = corpora.load(corpus)
        pairs = []
        tries = 0
        while len(pairs) < 3 and tries < 4:
            seed = random.choice(data)
            antonyms = self.dictionary.antonym(seed)
            if antonyms:
                antonym = random.choice(antonyms)
                pairs.append((seed, antonym))
            else:
                tries += 1
        if len(pairs) < 2:
            self.log.error("Giving up.")
        slogans = ["%s IS %s" % tuple(map(string.upper, x)) for x in pairs]
        return "\n".join(slogans)
        
    def generate_text(self):
        # Generate a new slogan.
        slogan = self.slogan

        # Reset the bio.
        bio = self.BIO_TEMPLATE % random.choice(["Eurasia", "Eastasia"])
        self.twitter.update_profile(description=bio)
        mastodon_id = self.mastodon.account_update_credentials(note=bio)['id']
        # Delete all previous tweets and records of same.        
        for tweet in self.twitter.user_timeline():
            self.twitter.destroy_status(tweet.id)

        try:
            for toot in self.mastodon.account_statuses(mastodon_id):
                self.mastodon.status_delete(toot['id'])
        except KeyError as e:
            # This can happen when nothing is posted.
            pass
        return slogan
        
Bot = SloganBot
