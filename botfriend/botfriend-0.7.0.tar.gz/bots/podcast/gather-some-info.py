import re
import json
from pdb import set_trace
from collections import Counter, defaultdict

class Detail(object):

    ignore_subjects = ['podcast', 'podcasts']
    
    known_bad_titles = [
        'fash the nation', 'radical agenda', 'lovestreet',
        'daily shoah', 'gateway geeks', 'music free static',
    ]
    known_bad_subjects = [
        'alt right', 'alt-right', 'trump', 'deepstate', 'deep state',
        '4chan', '8chan', '8 chan', '4 chan', 'pepe', 'qanon', 'q anon', 'q posts',
        'spygate', 'maga', 'antifa', 'anons', 'white hats', 'fusion gps',
        'trump jr', 'infowars', 'c60', 'strzok', 'christopher cantwell',
        'rod rosenstein', 'tds', 'fox news', 'jack posobiec', 'pro-white',
        'white pill', 'whitepill', 'redpill', 'red pill', 'incel', 'incels', 'hatehouse',
        '4th watch', 'illuminati', 'nazi', 'identity politics', 'nwo',
        'alex jones', 'twitter wars',
        'conservative', 'libertarian', # yeah, most of these suck, bite me
    ]
    known_bad_creators = [
        'therightstuff.biz', 'dustin nemos', 'h. a. goodman',
        'seething frog', 'dan bongino', 'sarah westall',
        'stephen d kelley', 'fritz_machine@yahoo.com',
        'praying medic', 'christopher cantwell', 'larry ridgeway',
        'dustin nemos', 'helpfultidbits', 'mike mcginty'
    ]                          
    
    def __init__(self, d):
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
            for k in bad:
                if re.compile(r"\b%s\b" % k, re.I).search(s):
                    return k
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
        )

bad = []
good = []

for filename in ['details.201705-06.ndjson']: #'details.201505-06.ndjson', 'details.201808-09.ndjson', 'details.ndjson':
    for i in open(filename):
        try:
            item = Detail(json.loads(i.strip()))
        except Exception as e:
            continue
        if item.is_bad:
            bad.append(item)
        else:
            good.append(item)

authors = defaultdict(list)
for b in bad:
    authors[b.creator].append(b)

for k, bads in sorted(list(authors.items()), key=lambda x: -len(x[1])):
    if len(bads) < 2:
        break
    print(k.encode("utf8"), [x.title for x in bads])
print()
            
tags = Counter()
for b in bad:
    print(b.is_bad, b.title.encode("utf8"))
    for s in b.subject:
        if not Detail.bad_string(s):
            tags[s.lower()] += 1

for k, v in tags.most_common():
    if v < 2:
        break
    print(k.encode("utf8"), v)
