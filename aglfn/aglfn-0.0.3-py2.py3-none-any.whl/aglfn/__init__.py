import unicodedata
from pathlib import Path
from .agl import AGL


def __parse_file(filename):
    file = Path(__file__).parent / f'agl-aglfn/{filename}.txt'
    lines = file.read_text().splitlines()
    return {unicodedata.lookup(_.split(';')[2]): _.split(';') for _ in lines if not _.startswith('#')}


__db = __parse_file('aglfn')


def __glyphs():
    return list(__db.keys())


def to_glyph(aglfn):
    result = [k for k, v in __db.items() if v[1] == aglfn]
    return result[0] if result else None


def __names():
    return [v[1] for k, v in __db.items()]


def name(glyph):
    result = __db.get(glyph)
    return result[1] if result else None


names = __names()
glyphs = __glyphs()
__all__ = ['name', 'names', 'glyphs', 'to_glyph', 'AGL']
