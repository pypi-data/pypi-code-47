"""
Konversi html ke image (PNG atau JPEG).
"""

from requests import get as http_get

from io import BytesIO
from imgkit import from_url, from_string
from PIL import Image, ImageFile
from .tools import get_base_url, convert_static_link_to_absolute

ImageFile.MAXBLOCK = 2 ** 20

IMAGE_FORMATS = set(
    [
        "PNG",
        "JPEG"
    ]
)

def html_to_image(url, format=None, absolute_link=True):
    # fix image format.
    if not isinstance(format, str):
        format = ""

    format = format.upper()
    if format not in IMAGE_FORMATS:
        format = "PNG"

    if absolute_link:
        base_url = get_base_url(url)
        r = http_get(url)
        content = r.text
        html = convert_static_link_to_absolute(content, base_url)
        img_bytes = from_string(html, False)
    else:
        img_bytes = from_url(url, False)

    bio = BytesIO(img_bytes)
    im = Image.open(bio)
    result = BytesIO()
    im.save(result, format)
    bytes = result.getvalue()
    return bytes
