import datetime
from dateutil import parser
from pdb import set_trace
import os
import json
import random
import requests

from olipy.ia import Audio
from botfriend.bot import BasicBot
from botfriend.model import Post
from podcast import Chooser

class PodcastBot(BasicBot):

    COLLECTION = "podcasts"

    def data_file(self, date):
        if isinstance(date, basestring):
            set_trace()
        d = os.path.split(__file__)[0]
        part = date.strftime("%Y%m")
        return os.path.join(d, "data", "podcasts.%s.ndjson" % part)
    
    def update_state(self):
        cutoff = self.model.last_state_update_time
        query = Audio.recent(
            "collection:%s" % self.COLLECTION, cutoff=cutoff, fields=[
                'createdate', 'title', 'identifier', 'publicdate', 'date', 'creator', 'forumSubject', 'year',
                'avg_rating', 'downloads', 'language'
            ]
        )
        outs = {}
        a = 0
        for audio in query:
            metadata = audio.metadata
            year = metadata.get('year')
            if not year or not isinstance(year, basestring) or int(year) < 1900:
                year = None
            date = metadata.get('createdate') or metadata.get('publicdate') or metadata.get('date') or year
            parsed = parser.parse(date)
            outputfile = self.data_file(parsed)
            if not outputfile in outs:
                outs[outputfile] = open(outputfile, "a")
            out = outs[outputfile]
            out.write(json.dumps(metadata))
            out.write("\n")
            a += 1
            if True or not a % 1000:
                print a, metadata

        # The actual state is used to keep track of every podcast
        # creator we've already used, so we don't repeat.
        self.model.state = self.model.state or {}
                
    def new_post(self):
        state = self.model.json_state or {}

        # Never repeat an author
        authors = set(state.get('authors', []))

        # Don't repeat a tag within 7 days
        tags = state.get('tags', {})
        
        # Set ._state so we don't update the last checked time.
        self._state = state
        
        # Get at least a month's worth of data, usually 2 months worth
        this_month = datetime.datetime.utcnow()
        last_month = this_month - datetime.timedelta(days=28)
        files = set([self.data_file(x) for x in [this_month, last_month]])

        chooser = Chooser(authors, tags, files)
        episode, new_tags = chooser.choose()
        set_trace()
        
        # Create the post.
        text = "%s\n\n%s" % (title, reader_url)
        post,  is_new = Post.from_content(
            self.model, text, reuse_existing=False
        )

        # Attache the image.
        if not image_url:
            return None
        response = requests.get(image_url)
        media_type = response.headers['Content-Type']
        post.attach(media_type, content=response.content)
        return post

Bot = PodcastBot
