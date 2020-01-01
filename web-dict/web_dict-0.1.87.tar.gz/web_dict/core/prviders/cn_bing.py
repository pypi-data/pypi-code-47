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


class _BriefDefProvider(Parser):
    def val_pos(self):
        return self.select("span.pos")

    def val_def(self):
        return self.select("span.def > span")


class _AuthDefSegProvider(Parser):
    def val_topic(self):
        return [
            {"en": ent.text, "zh": zht.text}
            for ent, zht in zip(
                self.select("span.val_dis", one=False, text=False),
                self.select("span.bil_dis", one=False, text=False),
            )
        ]

    def val_defs(self):
        return [
            {"en": ent.text, "zh": zht.text}
            for ent, zht in zip(
                self.select("div.def_pa", text=False).find_all("span", class_="val"),
                self.select("div.def_pa", text=False).find_all("span", class_="bil"),
            )
        ]

    def val_examples(self):
        return [
            {"en": ent.text, "zh": zht.text}
            for ent, zht in zip(
                self.select("div.li_exs", text=False).find_all("div", class_="val_ex"),
                self.select("div.li_exs", text=False).find_all("div", class_="bil_ex"),
            )
        ]


class _AuthDefProvider(Parser):
    def val_pos(self):
        return self.select("div.pos",)

    def val_def(self):
        return self.provider_to_list(_AuthDefSegProvider, "div.de_seg")

    def val_idm(self):
        idm_tag = self.bs.find("div", class_="idm_seg")
        if not idm_tag:
            return []
        try:
            return [
                {"idm": idm.text, "example": {"en": ent.text, "zh": zht.text}}
                for idm, ent, zht in zip(
                    idm_tag.find_all("span", class_="ids"),
                    idm_tag.find_all("span", class_="val"),
                    idm_tag.find_all("span", class_="bil"),
                )
            ]
        except AttributeError:
            return []


class _EnZhDefProvider(Parser):
    def val_pos(self):
        return self.select("div.pos.pos1")

    def val_defs(self):
        return list(set(self.select("div.df_cr_w", one=False)))


class _EnEnDefProvider(Parser):
    def val_pos(self):
        return self.select("div.pos.pos1")

    def val_defs(self):
        return list(set(self.select("div.df_cr_w", one=False)))


class _DefsProvider(Parser):
    def val_auth(self):
        return self.provider_to_list(_AuthDefProvider, "div.each_seg")

    def val_ec(self):
        return self.provider_to_list(_EnZhDefProvider, "div#crossid > table > tr")

    def val_ee(self):
        return self.provider_to_list(_EnEnDefProvider, "div#homoid > table > tr")


class CNBing(BaseProvider):
    @property
    def url(self):
        return f"https://cn.bing.com/dict/search?q={self.word}"

    def __init__(self, word: str, seg=""):
        super(CNBing, self).__init__(word, seg)
        self.seg = seg

    @property
    def head_word(self):
        return self.select("div.hd_div > h1 > strong")

    @property
    def val_phone(self):
        p = re.compile(r"\[(?P<c>.+)\]")
        m = re.search(p, self.select("div.hd_pr")) if self.select("div.hd_pr") else None
        m2 = (
            re.search(p, self.select("div.hd_prUS"))
            if self.select("div.hd_prUS")
            else None
        )
        return {"uk": m.group("c") if m else None, "us": m2.group("c") if m2 else None}

    @property
    def val_images(self):
        return [
            t["src"].replace("&w=80&h=80", "")
            for t in self.select(
                "div.img_area > div.simg > a > img", one=False, text=False
            )
        ]

    @property
    def val_brief(self):
        return self.provider_to_list(
            _BriefDefProvider,
            ("li", {}),
            find_in_tag=self.bs.find("div", class_="qdef"),
        )

    @property
    def val_defs(self):
        return self.provider_to_list(_DefsProvider, "div#defid")
