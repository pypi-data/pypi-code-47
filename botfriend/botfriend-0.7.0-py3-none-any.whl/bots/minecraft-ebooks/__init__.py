from botfriend.bot import Bot as BasicBot
from nose.tools import set_trace
from wordfilter import blacklisted
import time
import random

class MinecraftEbooksBot(BasicBot):

    def update_state(self):
        """Gather usernames of followers to use in command block outputs."""
        state = dict()
        for publisher in self.publishers:
            if publisher.service not in ('twitter', 'mastodon'):
                continue
            api = publisher.api
            if publisher.service == 'twitter':
                followers = []
                state[publisher.service] = followers
                cursor = -1
                while cursor:
                    (page, (prev_cursor, next_cursor)) = api.followers(
                        cursor=cursor, per_page=100
                    )
                    cursor = next_cursor
                    for follower in page:
                        name = follower.name
                        if not blacklisted(name):
                            followers.append(name)
                    time.sleep(3)
            else:
                followers = []
                state[publisher.service] = followers
                api = publisher.api
                api.debug_requests = True
                me = api.account_verify_credentials()
                page = api.account_followers(me['id'])
                everything = api.fetch_remaining(page)
                for follower in everything:
                    name = follower['display_name']
                    if not blacklisted(name):
                        followers.append(name)
        return state

    def post_to_publisher(self, publisher, post, publication):
        if '%(player)s' in post.content:
            player = 'Steve'
            state = self.model.json_state
            if publisher.service in state:
                names = state[publisher.service]
                if names:
                    player = random.choice(names)
            publication.content = post.content % dict(player=player)
        return super(MinecraftEbooksBot, self).post_to_publisher(
            publisher, post, publication
        )

    
Bot = MinecraftEbooksBot
