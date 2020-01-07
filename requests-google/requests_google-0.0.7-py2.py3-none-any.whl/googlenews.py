# -*- coding: utf-8 -*-
"""
requests_google.googlenews
"""

import feedparser
import requests

from collections import namedtuple
from six.moves.urllib.parse import quote_plus 

# Reference: 
# https://stackoverflow.com/questions/51537063/url-format-for-google-news-rss-feed
GEOLOCATION_URL = 'https://news.google.com/news/rss/headlines/section/geo/{location}'

GoogleNewsResult = namedtuple('GoogleNewsResult', ['title', 'url', 'description'])


def get_rss_url_by_geolocation(city, state):
    location = '{}, {}, {}'.format(city, state, 'United States')
    return GEOLOCATION_URL.format(location=quote_plus(location))


def get_news_by_geolocation(city, state, **kwargs):
    url = get_rss_url_by_geolocation(city, state)
    r = requests.get(url, **kwargs)
    if r.status_code != 200:
        raise RuntimeError('requests fail, url={} status_code={}'.format(url, r.status_code))
    d = feedparser.parse(r.text)
    for entry in d.entries:
        yield GoogleNewsResult(entry.title, entry.link, entry.description)