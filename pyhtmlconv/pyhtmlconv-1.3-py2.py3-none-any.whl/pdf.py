"""
Konversi html ke PDF.
"""

from requests import get as http_get

from pdfkit import from_url, from_string
from .tools import get_base_url, convert_static_link_to_absolute


def html_to_pdf(url, absolute_link=True):
    if absolute_link:
        base_url = get_base_url(url)
        r = http_get(url)
        content = r.text
        html = convert_static_link_to_absolute(content, base_url)
        img_bytes = from_string(html, False)
    else:
        img_bytes = from_url(url, False)

    return img_bytes
