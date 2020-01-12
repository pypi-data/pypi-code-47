#   Copyright (c) 2019 Julien Lepiller <julien@lepiller.eu>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
####
""" The strings.xml format for Android translations. """

import androidstringslib
import os
from pathlib import Path

from .entry import AndroidStringsEntry

class AndroidStringsFormat:
    def __init__(self, conf):
        self.conf = conf
        self.translationfilename = conf["file"]
        self.enfilename = conf["template"]
        if not os.path.isfile(self.translationfilename):
            # Create an empty initial file if none exists yet
            Path(self.translationfilename).parent.mkdir(parents=True, exist_ok=True)
            with open(self.translationfilename, 'w') as f:
                f.write('<resource></resource>')
        self.conf = conf
        self.reload()

    def content(self):
        aresources = []
        for entry in self.translation:
            aresources.append(AndroidStringsEntry(entry))
        return aresources

    def save(self):
        self.translation.save()

    def merge(self, older, callback):
        for entry in self.translation:
            key = entry.id
            envalue = entry.orig
            ntranslated = entry.dst
            oentry = older.translation.getValuesById(key)
            oenvalue = oentry[0]
            otranslated = oentry[1]
            if otranslated == ntranslated:
                continue
            if otranslated == "":
                continue
            if ntranslated == "":
                entry.dst = otranslated
                continue
            # otherwise, ntranslated and otranslated have a different value
            entry.dst = callback(envalue, otranslated, ntranslated)
        self.translation.save()

    def getExternalFiles(self):
        return [self.enfilename, self.translationfilename]

    def reload(self):
        self.translation = androidstringslib.android(self.conf["template"], self.conf["file"], self.conf['lang'])

    def translationFiles(self):
        return [self.translationfilename]
