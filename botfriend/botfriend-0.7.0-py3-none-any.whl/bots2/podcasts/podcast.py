import json
import re
from pdb import set_trace
import datetime
from dateutil import parser
import random
from olipy.ia import Audio
from feedgen.entry import FeedEntry

class Chooser(object):

    def __init__(self, authors, tags, files):
        self.authors = set(authors)
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
        while (not choice or choice.is_bad or not choice.mp3_link):
            identifier = random.choice(data)
            detail = Audio(identifier)
            choice = Episode(detail)
        xml, tags = choice.to_xml
        new_tags = self.groom_tags(tags)
        return xml, new_tags
        
    def groom_tags(self, new_tags, lifetime=7):
        now = datetime.datetime.utcnow() 
        expires = now - datetime.timedelta(days=lifetime)
        now_str = now.strftime("%Y%m%d")
        new_set = {}
        for tag, last_used in self.tags:
            last_used_date = parser.parse(last_used)
            if last_used_date >= expires:
                new_set[tag] = last_used
        for tag in new_tags:
            new_set[tag] = now_str
        return new_tags


def make_re(*l):
        parts = [r"\b%s\b" % x for x in l]
        return re.compile("(%s)" % "|".join(parts))
    
class Episode(object):

    ignore_subjects = make_re('podcast', 'podcasts')
    
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
        'alex jones', 'twitter wars',
        'conservative', 'libertarian', # yeah, most of these suck, bite me
    )
    known_bad_creators = make_re(
        'therightstuff.biz', 'dustin nemos', 'h. a. goodman',
        'seething frog', 'dan bongino', 'sarah westall',
        'stephen d kelley', 'fritz_machine@yahoo.com',
        'praying medic', 'christopher cantwell', 'larry ridgeway',
        'dustin nemos', 'helpfultidbits', 'mike mcginty'
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
        if isinstance(self.subject, basestring):
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

    @property
    def creator_is_bad(self):
        return self.bad_string(self.creator)

    @property
    def description_is_bad(self):
        return self.bad_string(self.description)

    @property
    def subject_is_bad(self):
        subjects = [x.lower() for x in self.subject]
        for x in subjects:
            v = self.bad_string(x)
            if v:
                return v
        return None
    
    @property
    def is_bad(self):
        return (
            self.title_is_bad or self.creator_is_bad or self.description_is_bad
            or self.subject_is_bad
        ) or False

    @property
    def mp3_link(self):
        mp3 = [x for x in self.item.files if 'MP3' in x.format]
        urls = set([x.url for x in mp3])
        if not urls or len(urls) > 1:
            return None
        return list(urls)[0]

    @property
    def to_xml(self):
        metadata = self.item.metadata
        entry = FeedEntry()
        entry.load_extension("podcast")
        title = metadata.get("title")
        author = metadata.get('creator')
        uploader = metadata.get("uploader")
        if uploader:
            entry.author(name=author, email=uploader)
        description = metadata.get('description') or ''
        date = metadata.get('createdate') or metadata.get('publicdate') or metadata.get('date') or year
        parsed = parser.parse(date)
        description = '<p>%s (originally published %s)<p>%s' % (
            title, parsed, description
        )
        if description:
            entry.description(description)
        mp3 = self.mp3_link
        entry.id(mp3)
        entry.enclosure(mp3, 0, 'audio/mpeg')
        from lxml import etree
        xml = etree.tostring(entry.rss_entry())
        return xml, metadata.get("subject")
