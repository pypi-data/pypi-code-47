from pdb import set_trace
from botfriend.bot import Bot

class BrendanBot(Bot):

    def post_to_publisher(self, publisher, post, publication):
        if publisher.service == 'twitter' and not ' ' in post.content and not '--' in post.content:
            publication.content = '@BrendanAdkins ' + post.content
        return super(BrendanBot, self).post_to_publisher(
            publisher, post, publication
        )

    def _next_scheduled_post(self, just_published):
        """When we begin a new book, we post the first Brendan in that book
        almost immediately, rather than waiting for the normal schedule.
        """
        if just_published:
            for post in just_published:
                if post.content.startswith('BEGIN'):
                    return datetime.timedelta(minutes=2)
        return super(BrendanBot, self)._next_scheduled_post(just_published)
            
            
Bot = BrendanBot
