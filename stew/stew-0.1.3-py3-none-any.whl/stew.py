#!/usr/bin/env python
# coding: utf-8
import re
from collections import defaultdict
from pathlib import Path
from typing import Tuple, List, Set

from .types import Lang, Translation, PLIndex, Key, Terms

TRANSLATION = re.compile(r'(.*)\s*=\s*.*$', re.S | re.MULTILINE)
MANY_DOTS = re.compile(r'\.{4,}')
LANG_AND_INDEX = re.compile(r'([-_a-zA-Z]+)(\[\d+\])?')


class line_reader:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.strings_txt = open(self.file_path)
        return self._lines()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.strings_txt.close()

    def _lines(self):
        for string in self.strings_txt:
            string = string.strip()
            if not string:
                continue

            yield Line(string)


class Line(str):
    def is_section(self) -> bool:
        return self.startswith('[[')


    def is_key(self) -> bool:
        return self.startswith('[')


    def is_translation(self) -> bool:
        return bool(TRANSLATION.match(self))


    def parse_translation(self) -> Tuple[Lang, Translation, PLIndex]:
        lang, _, tran = self.partition('=')
        lang, index = self._process_lang(lang)
        tran = self._process_translation(tran)
        return lang, tran, index


    def _process_translation(self, translation) -> Translation:
        if MANY_DOTS.search(translation):
            print(f'WARNING: 4 or more dots in the string: {self}')
        return Translation(translation.strip().replace("...", "…"))


    def _process_lang(self, lang) -> Tuple[Lang, PLIndex]:
        lang, index = LANG_AND_INDEX.findall(lang)[0]
        if not index:
            index = 0
        else:
            index = int(index.strip('[]'))
        return Lang(lang), PLIndex(index)


class Stew:
    def __init__(self, strings_path):
        self.strings_path: Path = strings_path
        self.terms: Terms = Terms()
        self.comments_and_tags = defaultdict(dict)
        self.keys_in_order: List[Key] = []
        self.all_langs: Set[Lang] = set()

        self._read_file()


    def _read_file(self):
        key = None
        with line_reader(self.strings_path) as lines:
            for line in lines:
                if line.is_section():
                    self._add_new_key(Key(line))
                    continue
                if line.is_key():
                    key = Key(line)
                    self._add_new_key(key)
                    continue
                if line.is_translation():
                    lang, tran, plural_index = line.parse_translation()
                    if lang == 'comment' or lang == 'tags':
                        self.comments_and_tags[key][lang] = tran
                        continue

                    self.terms[key][lang][plural_index] = tran
                    self.all_langs.add(lang)


    def _add_new_key(self, key):
        if key not in self.keys_in_order:
            self.keys_in_order.append(key)


    def formatted(self):
        for key in self.keys_in_order:
            yield key

            if key not in self.terms:
                continue

            for lang, forms in self.terms[key].key_sorted():
                for plural_index, translation in forms.key_sorted():
                    pl_index_str = f'[{plural_index}]' if len(forms) > 1 and plural_index else ''
                    yield f'    {lang}{pl_index_str} = {translation}'

            yield ''
