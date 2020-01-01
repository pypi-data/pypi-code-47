#  Copyright (C) 2016-2020  Kyle.Hwang <upday7[at]163.com>
#  #
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version, with the additions
#  listed at the end of the accompanied license file.
#  #
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#  #
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#  #
#  NOTE: This program is subject to certain additional terms pursuant to
#  Section 7 of the GNU Affero General Public License.  You should have
#  received a copy of these additional terms immediately following the
#  terms and conditions of the GNU Affero General Public License which
#  accompanied this program.

import abc
import re
import unicodedata
from typing import Union, Tuple

import requests
from bs4 import BeautifulSoup, Tag
from requests import Response, HTTPError

from .utils import STD_HEADERS


def _norm_str(s: str):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKD", s)).strip()


class Parser:
    to_dict_fields = ()

    def __init__(self, markup: Union[BeautifulSoup, str, Tag]):
        self._markup = markup
        self._bs = None

    @property
    def markup(self) -> Union[BeautifulSoup, str, Tag]:
        return self._markup

    @property
    def bs(self) -> Union[BeautifulSoup, Tag]:
        if not self._bs:
            if isinstance(self.markup, (BeautifulSoup, Tag)):
                self._bs = self.markup
            else:
                if not self.markup:
                    return None
                self._bs = BeautifulSoup(markup=self.markup, features="html.parser")
        return self._bs

    def select(self, p: str, one=True, text=True):

        if one:
            if not self.bs:
                return None
            t = self.bs.select_one(p)
            if t and text:
                return _norm_str(t.text)
            return t
        else:
            if not self.bs:
                return [None, ]
            ts = self.bs.select(p)
            if ts and text:
                return [_norm_str(t.text) for t in ts]
            return ts

    def get_by_cls(self, name: str, cls: str, **attrs) -> Tag:
        return self.bs.find(name, class_=cls, attrs=attrs)

    def to_dict(self):
        _ = {}

        fields = []
        fields.extend(self.to_dict_fields)
        fields.extend(
            [
                prop.lower().split("val_")[-1]
                for prop in dir(self)
                if prop.startswith("val_")
            ]
        )

        for field in set([f.lower() for f in fields]):
            try:
                val = getattr(self, field, getattr(self, f"val_{field}", None))
                if callable(val):
                    val = val()
                if isinstance(val, str):
                    val = unicodedata.normalize("NFKD", val)
                    # remove brackets
                    m = re.match(r"\((?P<c>.+)\)", val)
                    if m:
                        val = m.group("c")
                if val not in [None, ""]:
                    _[field.split("val_")[-1]] = val
            except AttributeError:
                ...
                # _[field.split('val_')[-1]] = None
        return _

    def provider_to_list(
            self,
            provider_cls,
            block_selector: Union[str, Tuple[str, dict],],
            find_in_tag: Union[BeautifulSoup, Tag] = None,
    ):
        if not find_in_tag:
            find_in_tag = self.bs
        try:
            if isinstance(block_selector, str):
                blocks = self.select(block_selector, one=False, text=False)
            else:
                blocks = find_in_tag.find_all(block_selector[0], **block_selector[1])
        except AttributeError:
            return []
        return [d for d in [provider_cls(d).to_dict() for d in blocks] if d]


class WebParser(Parser):
    def __init__(self, word: str):
        self.word = word
        super(WebParser, self).__init__(markup="")
        self._rsp = None

    @property
    @abc.abstractmethod
    def url(self):
        ...

    @property
    def rsp(self) -> Response:
        if not self._rsp:
            self._rsp = requests.get(self.url, headers=STD_HEADERS)
            self._rsp.raise_for_status()
        return self._rsp

    @property
    def json(self) -> dict:
        return self.rsp.json()

    @property
    def markup(self) -> str:
        if not self._markup:
            try:
                self._markup = self.rsp.content.decode()
            except HTTPError:
                self._markup = ""
        return self._markup
