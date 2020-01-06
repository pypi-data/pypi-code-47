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


class _SuggestionProvider(Parser):
    def val_phrase(self):
        return self.select("span.word")

    def val_exp(self):
        return self.select("span.definition")

    def val_freq(self):
        try:
            return float(self.bs.attrs.get("freq", 0))
        except ValueError:
            return -1


class VocabularySuggestion(BaseProvider):
    @property
    def url(self):
        return f"https://www.vocabulary.com/dictionary/autocomplete?search={self.word}"

    def __init__(self, word: str, seg=""):
        super(VocabularySuggestion, self).__init__(word, seg)
        self.seg = seg

    @property
    def head_word(self):
        return None

    @property
    def val_suggestion(self):
        return self.provider_to_list(_SuggestionProvider, "li")
