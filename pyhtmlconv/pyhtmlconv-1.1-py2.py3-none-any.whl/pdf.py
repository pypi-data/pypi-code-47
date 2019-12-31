"""
Konversi html ke PDF.
"""

from os import unlink
from tempfile import NamedTemporaryFile
from pdfkit import from_url

def html_to_pdf(url):
    with NamedTemporaryFile(delete=False) as outfile:
        from_url(url, outfile.name)

    bytes = b""
    with open(outfile.name, "rb") as fp:
        bytes = fp.read()

    unlink(fp.name)
    return bytes
