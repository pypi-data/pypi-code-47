"""
Konversi html ke image (PNG atau JPEG).
"""

from io import BytesIO
from imgkit import from_url
from PIL import Image

IMAGE_FORMATS = set(
    [
        "PNG",
        "JPEG"
    ]
)

def html_to_image(url, format=None):
    if format not in IMAGE_FORMATS or not isinstance(format, str):
        format = "PNG"

    format = format.upper()
    img_bytes = from_url(url, False)
    bio = BytesIO(img_bytes)
    im = Image.open(bio)
    result = BytesIO()
    im.save(result, format=format)
    bytes = result.getvalue()
    return bytes
