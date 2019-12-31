"""
HTML Converter.
"""

from io import BytesIO
from PIL import Image
from base64 import b64encode
from random import randint
from time import sleep
from .img import html_to_image as _to_image
from .pdf import html_to_pdf as _to_pdf

def catch_error_and_try_again(func, *args, **kwds):
    n = 0
    m = 5
    bytes = None
    while n != m:
        try:
            bytes = func(*args, **kwds)
        except:
            pass

        if bytes:
            break
        else:
            sleep(randint(2, 5))
            n += 1

    return bytes

def html_converter(url, to, format=None):
    """
    HTML Converter ke format lain.
    """

    assert isinstance(url, str)
    assert isinstance(to, str)

    retVal = None
    to = to.lower()
    if to == "image":
        retVal = catch_error_and_try_again(_to_image, url, format=format)
    elif to == "pdf":
        retVal = catch_error_and_try_again(_to_pdf, url)
    else:
        raise TypeError("Invalid file type: {!r}".format(to))

    if isinstance(retVal, bytes):
        retVal = retVal.decode("utf-8", "ignore")

    return retVal

def convert_to_image(url, format, datauri=False):
    """
    Konversi url sebagai gambar (PNG atau JPEG).
    """

    retVal = html_converter(url, "image", format)
    if datauri:
        mimetype = "image/" + format.lower()
        retVal = convert_to_data_uri(retVal, mimetype)

    return retVal

def convert_to_pdf(url, datauri=False):
    """
    Konversi url ke PDF.
    """

    retVal = html_converter(url, "pdf")
    if datauri:
        mimetype = "application/pdf"
        retVal = convert_to_data_uri(retVal, mimetype)

    return retVal

def convert_to_data_uri(data, mimetype):
    if isinstance(data, str):
        data = data.encode("utf-8")

    data = b64encode(data).decode("utf-8")
    uri = "data:{0};base64,{1}".format(mimetype, data)
    return uri
