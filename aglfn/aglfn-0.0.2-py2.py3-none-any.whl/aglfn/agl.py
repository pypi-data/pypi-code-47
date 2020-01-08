import unicodedata
from pathlib import Path
from functools import lru_cache


class AGL:
    def __init__(self):
        self.glyph_list = self.__parse_file('glyphlist')

    @staticmethod
    def __parse_file(name):
        file = Path(__file__).parent / f'agl-aglfn/{name}.txt'
        return file.read_text().splitlines()

    @lru_cache(maxsize=2)
    def glyph_names(self):
        result = {}
        for line in self.glyph_list:
            if '#' in line: continue
            value, key = line.split(";")
            result.setdefault(key, []).append(value)
        return result

    @lru_cache(maxsize=2)
    def all_glyphs(self):
        return [self.__glyph_name(ucp) for ucp in range(0, 0x10FFFF+1)]

    @staticmethod
    def char_to_usv(char: str):
        return hex(ord(char))[2:].upper().zfill(4)

    @staticmethod
    def char_to_ucp(char: str):
        return ord(char)

    def char_to_glyph_names(self, char: str):
        return self.__glyph_name(self.char_to_ucp(char))

    # @staticmethod
    # def usv_to_ucp(usv: str):
    #     return int(usv, 16)
    #
    # def usv_to_char(self, usv: str):
    #     return chr(self.usv_to_ucp(usv))
    #
    # def usv_to_glyph_name(self, usv: str):
    #     return self.__glyph_name(self.usv_to_ucp(usv))

    @staticmethod
    def ucp_to_str(ucp: int):
        return hex(ucp)[2:].upper().zfill(4)

    def __glyph_name(self, ucp: int):
        return self.glyph_names().get(self.ucp_to_str(ucp))

    @lru_cache(maxsize=0)
    def lookup(self, char: str):
        return dict(
            char=char,
            unicode_code_point=self.char_to_ucp(char),
            unicode_standard_value=self.char_to_usv(char),
            agl_glyph_names=self.char_to_glyph_names(char),
            unicode_character_name=unicodedata.name(char, None)
        )
