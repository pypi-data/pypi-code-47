"""
HTML Converter Tools.
"""

from bs4 import BeautifulSoup
from .compat import urlparse, urljoin

def get_base_url(url):
    p = urlparse(url)
    scheme = p.scheme + "://"
    host = p.netloc
    base = scheme + host
    return base

def path_converter(elements, attr, base_url):
    for l in elements:
        href = l.get(attr, "")
        if not href.startswith(("http://", "https://")):
            href = urljoin(base_url, href)
        l[attr] = href

def convert_static_link_to_absolute(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("link")
    scripts = soup.find_all("script")
    path_converter(links, "href", base_url)
    path_converter(scripts, "src", base_url)
    new = str(soup)
    # FIXME
    # with open("test_meta.html", "w", encoding="utf-8") as fp:
    #     fp.write(new)
    return new
