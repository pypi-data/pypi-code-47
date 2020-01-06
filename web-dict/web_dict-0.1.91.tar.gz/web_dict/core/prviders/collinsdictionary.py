#  Copyright (C) 2016-2019  Kyle.Hwang <upday7[at]163.com>
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

from .base_provider import BaseProvider
from ..parser import Parser


class _PhraseProvider(Parser):
    to_dict_fields = (
        "phrase",
        "trans",
    )

    @property
    def phrase(self):
        return self.select("span.type-phr > span.orth")

    @property
    def trans(self):
        return self.select("span.cit.type-translation > span.quote")


class _IdiomProvider(Parser):
    to_dict_fields = ("orth", "trans")

    @property
    def orth(self):
        return self.select("span.orth")

    @property
    def trans(self):
        return self.select("span.cit.type-translation > span")


class _GrammarProvider(Parser):
    to_dict_fields = {
        "content",
        "trans",
    }

    @property
    def content(self):
        content = self.select("span.colloc")
        if content:
            return re.match(r"\[(?P<c>.+)\]", content).group("c")
        return content

    @property
    def trans(self):
        return self.select("span.cit.type-translation")


class _ExampleProvider(Parser):
    to_dict_fields = {"sent", "trans"}

    @property
    def sent(self):
        try:
            return re.sub(r"\s+", " ", self.contents[0]).strip()
        except IndexError:
            return None

    @property
    def trans(self):
        try:
            return re.sub(r"\s+", " ", "; ".join(self.contents[1:])).strip()
        except IndexError:
            return None

    @property
    def contents(self):
        _ = self.select("span.quote", one=False)
        if _:
            if len(_) == 2:
                return _
            r = [t.text.replace("⇒", "").strip() for t in self.bs.find_all("q")]
            if r:
                return r
            return _
        else:
            return [self.bs.text, ]


class _SenseProvider(Parser):
    to_dict_fields = (
        "exp",
        "examples",
        "syn",
        "grammars",
        "idioms",
        "phrases" "senses",
    )

    @property
    def syn(self):
        syn_pattern = re.compile(r"\)?\s*\(=?\s*(?P<c>.+)\)")
        t1 = self.select("span.lbl.type-geo > span.lbl.type-syn", text=False)
        if t1:
            syn = re.match(syn_pattern, t1.text).group("c")
            geo_txt = self.select("span.lbl.type-geo")

            return {
                "syn": syn,
                "geo": re.match(r"\((?P<g>.+)\)\s*\(.+\)", geo_txt).group("g"),
            }
        try:
            syn = re.match(syn_pattern, self.select("span.lbl.type-syn")).group("c")
        except:
            syn = ""
        return {"syn": syn, "geo": None}

    @property
    def exp(self):
        exp = "; ".join(
            t.text
            for t in self.bs.find_all(
                "span",
                class_=re.compile(r"cit\s(cit-)?type-translation"),
                recursive=False,
            )
        )

        if not exp:
            exp = self.select("div.def")
            if not exp and 'def' in self.bs.attrs['class']:
                exp = self.bs.text.replace("\n", " ")
        return exp

    @property
    def idioms(self):
        return self.provider_to_list(_IdiomProvider, "div.re.type-idm")

    @property
    def examples(self):
        return self.provider_to_list(
            _ExampleProvider, "div.cit.type-example"
        ) or self.provider_to_list(_ExampleProvider, "div.cit.cit-type-example")

    @property
    def phrases(self):
        return self.provider_to_list(_PhraseProvider, "div.type-phr")

    # @property
    # def grammars(self):
    #     return self.provider_to_list(_GrammarProvider, "div.sense")

    def val_senses(self):
        return self.provider_to_list(_SenseProvider, "div.sense")


class _DefProvider(Parser):
    to_dict_fields = ("pos", "senses", "misc")

    def __init__(self, markup: str):
        super(_DefProvider, self).__init__(markup=markup)

    @property
    def pos(self):
        return self.select("span.pos")

    @property
    def misc(self):
        misc = self.select("span.lbl.type-misc")
        return re.match(r"\((?P<c>.+)\)", misc).group("c") if misc else misc

    @property
    def senses(self):
        senses = [
            s
            for s in self.provider_to_list(
                _SenseProvider, ("div", dict(class_="sense", recursive=False))
            )
            if any(s.values())
        ]
        if not senses:
            senses = [
                s
                for s in self.provider_to_list(
                    _SenseProvider,
                    ("li", dict(class_="sense_list_item", recursive=True)),
                )
                if any(s.values())
            ]
        return senses


class CollinsWeb(BaseProvider):
    to_dict_fields = ("head_word", "pron", "rank", "audio", "defs")

    @property
    def url(self):
        url = f"https://www.collinsdictionary.com/dictionary/{self.seg}/{self.word}"
        print(f"Requesting {url}")
        return url

    def __init__(self, word: str, seg: str = "spanish-english"):
        super(CollinsWeb, self).__init__(word, seg)

    @property
    def bs(self):
        bs = super(BaseProvider, self).bs
        return bs.find("div", class_=re.compile(r"cB\scB-def.+")) or bs.find(
            "div", class_=re.compile(r"cB\scB-t")
        )

    @property
    def pron(self):
        try:
            return self.select("span.pron.type-") or re.match(
                r"\((?P<pron>.+)\)", self.select("div.cB-h > div > span.pron")
            ).group("pron")
        except TypeError:
            return None

    @property
    def rank(self):
        try:
            return int(
                self.select("span.word-frequency-img", one=True, text=False)[
                    "data-band"
                ]
            )
        except Exception as exc:
            return None

    @property
    def head_word(self):
        try:
            return self.select("h2.h2_entry > span.orth") or self.select("h2.h2_entry")
        except AttributeError:
            return None

    @property
    def audio(self):
        return self.select("a.audio_play_button", text=False).get("data-src-mp3")

    @property
    def defs(self):
        return [
            s for s in self.provider_to_list(_DefProvider, "div.hom") if any(s.values())
        ]
