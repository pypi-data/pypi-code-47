import base64
from PIL import Image

def get_base64image(image: bytes, format: str = "png") -> str:
    return """data:image/{format};base64,{data}""".format(
        format=format,
        data=base64.encodebytes(image).decode(),
        )

def resize(src: Image, scale: float) -> Image:
    src_size = src.size
    dst_size = (int(src_size[0] * scale), int(src_size[1] * scale))
    dst = src.resize(dst_size)
    return dst
