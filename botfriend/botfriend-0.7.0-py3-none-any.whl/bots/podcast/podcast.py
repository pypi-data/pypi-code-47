import json
import re
from pdb import set_trace
import datetime
from dateutil import parser
import random
from olipy.ia import Audio
from feedgen.entry import FeedEntry

class Chooser(object):

    def __init__(self, creators, tags, files):
        self.creators = set(creators)
        self.tags = tags
        self.files = files
        self._data = None

    @property
    def data(self):
        if not self._data:
            self._data = []
            for i in self.files:
                inp = open(i)
                for j in inp:
                    podcast = json.loads(j.strip())
                    language = podcast.get('language')
                    if language and  language != 'eng':
                        continue
                    okay = True
                    for k in 'title', 'creator':
                        s = podcast.get(k)
                        if not s:
                            continue
                        reason = Episode.bad_string(s)
                        if reason:
                            #print "%s disqualifies: %s/%s" % (
                            #    reason, podcast.get('title'), podcast.get('creator')
                            #)
                            okay = False
                            break
                    if okay:
                        self._data.append(podcast['identifier'])
        return self._data

    def choose(self):
        choice = None
        data = self.data
        while (not choice or choice.is_bad(self.creators, list(self.tags.keys())) or not choice.mp3_link):
            identifier = random.choice(data)
            detail = Audio(identifier)
            choice = Episode(detail)
            if choice.is_bad(self.creators, list(self.tags.keys())):
                print("BAD! %s" % choice.is_bad(self.creators, list(self.tags.keys())))
        additional_tags = [x.lower() for x in choice.subject]
        print("Chose", choice)
        return choice, choice.creator, self.groom_tags(additional_tags)
        
    def groom_tags(self, new_tags, lifetime=7):
        now = datetime.datetime.utcnow() 
        expires = now - datetime.timedelta(days=lifetime)
        now_str = now.strftime("%Y%m%d")
        new_set = {}
        for tag, last_used in list(self.tags.items()):
            last_used_date = parser.parse(last_used)
            if last_used_date >= expires:
                new_set[tag] = last_used
        for tag in new_tags:
            if tag and tag not in Episode.ignore_subjects:
                new_set[tag] = now_str
        return new_set


def make_re(*l):
        parts = [r"\b%s\b" % x for x in l]
        return re.compile("(%s)" % "|".join(parts))
    
class Episode(object):

    MIN_SIZE = 5 * 1024 * 1024

    ignore_subjects = set(
        [
            'podcast', 'podcasts', 'podcasting', 'video', 'soundcloud',
            'news', 'daily', 'part', 'episode', 'blog', '2018', '2019',
            'talk', 'audio', 'discussion', 'podcaster', 'podcast episode',
            'guests', 'review',
        ]
    )
    
    known_bad_titles = make_re(
        'fash the nation', 'radical agenda', 'lovestreet',
        'daily shoah', 'gateway geeks', 'music free static',
    )
    known_bad_subjects = make_re(
        'alt right', 'alt-right', 'trump', 'deepstate', 'deep state',
        '4chan', '8chan', '8 chan', '4 chan', 'pepe', 'qanon', 'q anon', 'q posts',
        'spygate', 'maga', 'antifa', 'anons', 'white hats', 'fusion gps',
        'trump jr', 'infowars', 'c60', 'strzok', 'christopher cantwell',
        'rod rosenstein', 'tds', 'fox news', 'jack posobiec', 'pro-white',
        'white pill', 'whitepill', 'redpill', 'red pill', 'incel', 'incels', 'hatehouse',
        '4th watch', 'illuminati', 'nazi', 'identity politics', 'nwo',
        'alex jones', 'twitter wars', 'gab',
        'conservative', 'libertarian', # yeah, most of these suck, bite me,
        'fash', 'alternative right', 'radixjournal', 'counter-currents',
        'mra', 'pua', 'pick.up.artist',
        
        # spam
        'a great article',
    )
    known_bad_creators = make_re(
        'therightstuff.biz', 'dustin nemos', 'h. a. goodman',
        'seething frog', 'dan bongino', 'sarah westall',
        'stephen d kelley', 'fritz_machine@yahoo.com',
        'praying medic', 'christopher cantwell', 'larry ridgeway',
        'dustin nemos', 'helpfultidbits', 'mike mcginty', 'fritzie101',
        'affirmative right', 'richard spencer', 'greg johnson',
    )
    
    def __init__(self, d):
        if isinstance(d, Audio):
            self.item = d
            d = self.item.item.item_metadata
        m = d['metadata']
        self.uploader = m['uploader']
        self.creator = m.get('creator') or m.get('uploader')
        self.title = m['title']
        self.subject = m.get('subject', [])
        if isinstance(self.subject, str):
            self.subject = [x.strip() for x in re.compile("[;,]").split(self.subject)]
        self.description = m.get('description')

    @classmethod
    def bad_string(cls, s):
        if not s:
            return None
        if isinstance(s, list):
            return any(cls.bad_string(x) for x in s)
        s = s.lower()
        for bad in (
                cls.known_bad_titles, cls.known_bad_creators,
                cls.known_bad_subjects,
        ):
            match = bad.search(s)
            if match:
                return match.groups()[0]
        return None
        
    @property
    def title_is_bad(self):
        return self.bad_string(self.title)

    def creator_is_bad(self, used):
        if self.creator.lower() in used:
            return self.creator.lower()
        return self.bad_string(self.creator)

    @property
    def description_is_bad(self):
        return self.bad_string(self.description)

    def subject_is_bad(self, used):
        subjects = [x.lower() for x in self.subject]
        for x in subjects:
            v = self.bad_string(x)
            if v:
                return v
            if x in used:
                return x
        return None
    
    def is_bad(self, creators, tags):
        return (
            self.title_is_bad or self.creator_is_bad(creators)
            or self.description_is_bad or self.subject_is_bad(tags)
        ) or False

    @property
    def mp3_link(self):
        mp3s = set(
            [x.url for x in self.item.files if 'MP3' in x.format]
        )
        if not mp3s or len(mp3s) > 1:
            return None
        return list(mp3s)[0]

