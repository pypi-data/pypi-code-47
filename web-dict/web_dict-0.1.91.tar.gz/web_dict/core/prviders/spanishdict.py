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

import json
import re

from .base_provider import BaseProvider


class SpanishDict(BaseProvider):
    @property
    def url(self):
        return f"https://www.spanishdict.com/translate/{self.word}"

    def __init__(self, word: str, seg="es-en"):
        super(SpanishDict, self).__init__(word, seg)
        self.seg = seg

    @property
    def json(self) -> dict:
        return json.loads(
            re.search(
                "SD_DICTIONARY_RESULTS_PROPS\s?=(?P<c>.+);.+global.SD_WORD_ROOT_PROPS.+",
                self.rsp.content.decode().replace("\n", ""),
                re.MULTILINE,
            ).group(1)
        )["es"]["entry"]

    @property
    def head_word(self):
        return self.select("div#headword-es")

    @property
    def val_audio(self):
        return f"http://audio1.spanishdict.com/audio?lang=es&text={self.head_word}"

    @property
    def val_neodict(self):
        return self.json["neodict"]
