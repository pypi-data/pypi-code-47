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

import re

from bs4 import Tag

from .base_provider import BaseProvider
from ..parser import Parser


class _ExampleProvider(Parser):
    def val_sent(self):
        sent = self.select("em", one=False)[0]
        if not sent:
            sent = self.bs.contents
        return re.search("‘?(?P<c>.+)’?", sent).group("c") if sent else None

    def val_trans(self):
        try:
            return self.select("em", one=False)[1]
        except (IndexError,TypeError):
            return None


class _ExpEntryProvider(Parser):
    @property
    def val_indicators(self):
        return self.select("span.indicators")

    @property
    def val_trans(self):
        trans = self.select("div.tr")
        return re.search("‘?(?P<c>.+)’?", trans).group("c") if trans else None

    @property
    def val_exp(self):
        exp = self.select("div.exg.em")
        if not exp:
            exp = self.select(".ind")
        return re.search("‘?(?P<c>.+)’?", exp).group("c") if exp else None

    @property
    def val_examples(self):
        _ = self.provider_to_list(
            _ExampleProvider, "div.examples > div.exg > ul > li.ex"
        )
        _.insert(
            0, _ExampleProvider(self.select(".ex", one=True, text=False)).to_dict()
        )
        return _


class _GrambProvider(Parser):
    @property
    def val_pos(self):
        return self.select("span.pos")

    @property
    def val_exps(self):
        return self.provider_to_list(_ExpEntryProvider, "ul.semb > li")


class _PrimaryHeaderProvider(Parser):
    def val_head_word(self):
        sup = self.select("span.hw > sup")
        return self.select("span.hw").replace(sup if sup else "", "")

    def val_trans(self):
        return self.select("span.head-translation")


class _PhraseProvider(Parser):  # class_=senseInnerWrapper
    def val_phrases(self):
        return self.select("strong.phrase", one=False)

    def val_exps(self):
        return self.provider_to_list(_ExpEntryProvider, "ul.semb > li")


class Lexico(BaseProvider):
    @property
    def url(self):
        _ = "definition"
        if self.seg in ("es-en",):
            _ = "traducir"
        if self.seg in ("en-es",):
            _ = "translate"
        if self.seg in ("es",):
            _ = "definicion"
        return f"https://www.lexico.com/{self.seg}/{_}/{self.word}"

    def __init__(self, word: str, seg="es-en"):
        super(Lexico, self).__init__(word, seg)
        self.seg = seg

    @property
    def head_word(self):
        return _PrimaryHeaderProvider(
            self.select(".primary_homograph", text=False)
        ).to_dict()

    @property
    def val_audio(self):
        return self.select("a.headwordAudio.rsbtn_play", text=False).audio["src"]

    @property
    def val_defs(self):
        return self.provider_to_list(_GrambProvider, "section.gramb")

    @property
    def val_phrases(self):
        phrase_title_tag: Tag = self.bs.find("h3", class_="phrases-title")
        if not phrase_title_tag:
            return []
        return self.provider_to_list(
            _PhraseProvider, "section.etymology.etym > div.senseInnerWrapper"
        )
