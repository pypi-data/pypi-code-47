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

from .base_provider import BaseProvider


class YoudaoEC(BaseProvider):
    @property
    def url(self):
        # return f"https://www.vocabulary.com/dictionary/{self.word}"
        return f"http://dict.youdao.com/jsonapi?q={self.word}&doctype=json"

    def __init__(self, word: str, seg=""):
        super(YoudaoEC, self).__init__(word, seg)
        self.seg = seg

    @property
    def head_word(self):
        return self.json['rel_word']['word']

    @property
    def val_audios(self):
        return [
            f'http://dict.youdao.com/dictvoice?audio={self.word}&type=1',
            f'http://dict.youdao.com/dictvoice?audio={self.word}&type=2'
        ]

    @property
    def val_exam_type(self):
        return self.json.get('ec', {}).get('exam_type')

    @property
    def val_phones(self):
        return [
            self.json.get('ec', {}).get('word', [{}, ])[0].get('ukphone'),
            self.json.get('ec', {}).get('word', [{}, ])[0].get('usphone'),
        ]

    @property
    def val_defs(self):
        return [
            d['tr'][0]['l']['i'][0] for d in self.json.get('ec', {}).get('word', [{}, ])[0].get('trs', [])
        ]

    def to_dict(self):
        return super(YoudaoEC, self).to_dict()
