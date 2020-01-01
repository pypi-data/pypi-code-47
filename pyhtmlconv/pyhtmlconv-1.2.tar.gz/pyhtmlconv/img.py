"""
Konversi html ke image (PNG atau JPEG).
"""

from io import BytesIO
from imgkit import from_url
from PIL import Image, ImageFile

ImageFile.MAXBLOCK = 2 ** 20

IMAGE_FORMATS = set(
    [
        "PNG",
        "JPEG"
    ]
)

def html_to_image(url, format=None):
    # fix image format.
    if not isinstance(format, str):
        format = ""

    format = format.upper()
    if format not in IMAGE_FORMATS:
        format = "PNG"
        print("default format PNG")

    img_bytes = from_url(url, False)
    bio = BytesIO(img_bytes)
    im = Image.open(bio)
    # rgb_im = im.convert("RGB")
    result = BytesIO()
    im.save(result, format)
    bytes = result.getvalue()
    return bytes
