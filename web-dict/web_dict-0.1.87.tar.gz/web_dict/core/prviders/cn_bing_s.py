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


from urllib.parse import parse_qs

from .base_provider import BaseProvider
from ..parser import Parser


class _SuggestionProvider(Parser):
    def val_phrase(self):
        return parse_qs(self.bs["url"].split("?")[-1])["q"][0].replace("+", " ")

    def val_exp(self):
        return self.bs["query"].replace(self.val_phrase(), "").strip()


class CNBingSuggestion(BaseProvider):
    @property
    def url(self):
        return (
            f"https://cn.bing.com/AS/Suggestions?scope=dictionary&pt=page.bingdict"
            f"&bq=dict&mkt=zh-cn&ds=bingdict&qry={self.word}"
            f"&cp=6&cvid=DCBD6682795F4F4CBE6CA0809F43ED3C"
        )

    def __init__(self, word: str, seg=""):
        super(CNBingSuggestion, self).__init__(word, seg)
        self.seg = seg

    @property
    def head_word(self):
        return None

    @property
    def val_suggestion(self):
        return self.provider_to_list(_SuggestionProvider, "li.sa_sg")
