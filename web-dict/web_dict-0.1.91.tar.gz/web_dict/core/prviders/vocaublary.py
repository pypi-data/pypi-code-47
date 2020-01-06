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

from .base_provider import BaseProvider
from ..parser import Parser


class _PrimaryDefinitionProvider(Parser):
    def val_pos(self):
        return self.select("td.posList > a", one=False)

    def val_exp(self):
        return self.select("td > div.def").replace(f"{self.val_pos()} ", "")


class _FullDefinitionItemProvider(Parser):
    def val_pos(self):
        return self.select("h3.definition > a")

    def val_exp(self):
        return self.select("h3.definition").lstrip(self.val_pos()).strip()

    def val_examples(self):
        sentences = self.select("div.example", one=False)
        sentence_highlight = self.select("div.example > strong", one=False)
        return [
            {"sentence": s, "highlight": w}
            for s, w in zip(sentences, sentence_highlight)
        ]


class _FullDefinitionGroupProvider(Parser):
    def val_items(self):
        return self.provider_to_list(_FullDefinitionItemProvider, "div.ordinal")


class _DefinitionsProvider(Parser):
    def val_primary(self):
        return self.provider_to_list(_PrimaryDefinitionProvider, ("tr", {}))

    def val_full(self):
        return self.provider_to_list(
            _FullDefinitionItemProvider, "div.group > div.ordinal"
        )


class Vocabulary(BaseProvider):
    @property
    def url(self):
        # return f"https://www.vocabulary.com/dictionary/{self.word}"
        return f"https://www.vocabulary.com/dictionary/definition.ajax?search={self.word}&lang=en"

    def __init__(self, word: str, seg=""):
        super(Vocabulary, self).__init__(word, seg)
        self.seg = seg

    @property
    def head_word(self):
        return self.select("h1.dynamictext")

    @property
    def val_audio(self):
        audio_id = self.select("h1.dynamictext", text=False).a["data-audio"]
        if audio_id:
            return f"https://audio.vocab.com/1.0/us/{audio_id}.mp3"

    @property
    def val_short_def(self):
        return self.select("p.short")

    @property
    def val_long_def(self):
        return self.select("p.long")

    # @property
    # def val_sentences(self):
    #     try:
    #         return [
    #             sd['sentence'] for sd in
    #             requests.get(f'https://corpus.vocabulary.com/api/1.0/examples.json'
    #                          f'?query={self.head_word}&maxResults=24').json()
    #             ['result']['sentences']
    #         ]
    #     except KeyError:
    #         return None

    @property
    def val_defs(self):
        return _DefinitionsProvider(self.bs.find("div", class_="definitions")).to_dict()
