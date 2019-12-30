#!/usr/bin/python
import datetime
import uuid
import os
from olipy.queneau import Assembler, WordAssembler
import PyRSS2Gen
import config
path = os.path.join(config.BASE, "mashteroids", "olipy", "data", "minor_planets.min.json")
corpus = Assembler.load(open(path), tokens_in='citation')

class Asteroid(object):

    HTML_TEMPLATE = """<div class="asteroid"><h2 class="name">%(name)s</h2><p class="citation">%(citation)s</p></div>"""

    def __init__(self):
        sentences = []
        names = []

        for sentence, source in corpus.assemble("f.l", min_length=3):
            sentences.append((sentence, source))
            names.append(source['name'])
        name_assembler = WordAssembler(names)
        self.sentences = sentences
        self.name = name_assembler.assemble_word()

    @property
    def citation_as_html(self):
        s = []
        for sentence, source in self.sentences:
            s.append('<span title="%s">%s</span>' % (source['name'], sentence))
        return ' '.join(s)

    @property
    def as_html(self):
        d = dict(name=self.name, citation=self.citation_as_html)
        return self.HTML_TEMPLATE % d

    @property
    def as_rss_feed(self):
        now = datetime.datetime.now()
        id = uuid.uuid4().urn
        item = PyRSS2Gen.RSSItem(
            title=self.name, description=self.as_html, pubDate=now, guid=id)

        rss = PyRSS2Gen.RSS2(
            title = "Mashteroids",
            link = "http://www.crummy.com/features/asteroids",
            description = "IAU-style citations for previously unknown minor planets.",
            lastBuildDate = now,
            items = [item])
        return rss.to_xml()

if __name__ == '__main__':
    for i in range(5):
        print(Asteroid().as_html.encode("utf8"))
