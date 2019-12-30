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
from botfriend.publish.podcast import PodcastPublisher
from .podcast import Chooser, Episode

class PodcastBot(BasicBot):

    COLLECTION = "podcasts"

    def data_file(self, date):
        d = os.path.split(__file__)[0]
        part = date.strftime("%Y%m")
        path = os.path.join(d, "data", "podcasts.%s.ndjson" % part)
        return path
        
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
            if not year or not isinstance(year, str) or int(year) < 1900:
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
            if not a % 1000:
                print(a, metadata)
        # The actual state is used to keep track of every podcast
        # creator we've already used, so we don't repeat.
        self.model.state = self.model.state or {}

    def file(self, item, format_name):
        """Find a file in a specific format."""
        for f in item.files:
            if f.format == format_name:
                return f
        return None

    def get_files(self):
        """Get files going back a certain amount of time."""
        files = []
        month = datetime.datetime.utcnow()
        if random.randint(0,10) == 5:
            num_months = 96 # Pretty much everything is fair game.
        else:
            num_months = int(round(max(2, abs(random.gauss(1,8)))))
        i = 0
        while not files or i < num_months:
            file = self.data_file(month)
            if os.path.exists(file):
                files.append(file)
            month -= datetime.timedelta(days=28)
            i += 1
        return files

    def make_post(self, podcast):
        print("In make_post")
        meta = podcast.metadata
        
        mp3 = self.file(podcast, "VBR MP3")
        print("mp3:", mp3)
        if not mp3:
            # This isn't really a podcast.
            print("not a podcast")
            return None, False
        if mp3.size < Episode.MIN_SIZE:
            # This is a really short 'podcast', possibly spam.
            print("too short")
            return None, False
        title = meta.get('title')
        date = parser.parse(
            meta.get('date') or meta.get('publicdate')
        ).strftime("%d %b %Y")
        description = meta.get('description', '')
        creator = meta.get('creator')
        if creator:
            byline = " by %s" % creator
        else:
            byline = ""
        detail_url = 'https://archive.org/details/%s' % meta['identifier']
        detail_link='<p>Archived at <a href="%s">%s</a>' % (detail_url, detail_url)
        template = '<p>Originally published%(byline)s on %(date)s.</p>\n\n%(description)s\n\n%(details)s'
        description = template % dict(
            details=detail_link,
            title=title,
            description=description,
            date=date,
            byline=byline
        )
        print("description")
        print(detail_link)
        print(date)
        print(byline)
        print(description)
        # Create a post compatible with the PodcastPublisher.
        print("About to call PodcastPublisher.make_post")
        return PodcastPublisher.make_post(
            self.model, title, mp3.url, description, 
            media_size=mp3.size, guid=detail_url
        )

    def new_post(self):
        state = self.model.json_state or {}

        # We never repeat a creator
        creators = set(state.get('creators', []))

        # We don't repeat a tag within 7 days
        tags = state.get('tags', {})
               
        # Get at least a month's worth of data, usually 3 months worth
        files = self.get_files()

        chooser = Chooser(creators, tags, files)
        episode, creator, new_tags = chooser.choose()
        post = None
        post, is_new = self.make_post(episode.item)
        if not post:
            raise Exception("Could not find post")
        # Quietly update the state.
        if creator:
            creator = creator.lower()
            creators.add(creator)
        self.model._state = json.dumps(
            dict(creators=list(creators), tags=new_tags)
        )
        #for k, v in sorted(new_tags.items(), key=lambda x: x[-1], reverse=True):
        #    print k, v

        return post

Bot = PodcastBot
