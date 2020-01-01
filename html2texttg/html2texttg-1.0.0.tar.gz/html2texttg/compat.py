import html.entities as htmlentitydefs
import html.parser as HTMLParser
import urllib.parse as urlparse
import urllib.request as urllib
from html import escape


def html_escape(s):
    return escape(s, quote=False)


__all__ = ['HTMLParser', 'html_escape', 'htmlentitydefs', 'urllib', 'urlparse']
