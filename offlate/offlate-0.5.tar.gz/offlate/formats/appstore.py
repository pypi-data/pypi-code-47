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
""" The appstore format for Android translations (fastlane). """

import os
from pathlib import Path

from .entry import AppstoreEntry

def findRecursive(directory):
    ans = []
    for f in os.listdir(directory):
        f = os.path.join(directory, f)
        if os.path.isfile(f):
            ans.append(f)
        elif os.path.isdir(f):
            ans.extend(findRecursive(f))
    return ans

class AppstoreFormat:
    def __init__(self, conf):
        self.conf = conf
        self.translationpath = conf["file"]
        self.enpath = conf["template"]
        self.conf = conf
        self.reload()

    def content(self):
        return self.resources

    def save(self):
        for r in self.resources:
            # create parent directory if it doesn't exist yet.
            Path(r.filename).parent.mkdir(parents=True, exist_ok=True)
            with open(r.filename, 'w') as f:
                f.write(r.tr)

    def merge(self, older, callback):
        for r in self.resources:
            for oldr in older.resources:
                nfile = r.filename[len(self.translationpath):]
                ofile = oldr.filename[len(older.translationpath):]
                if nfile != ofile:
                    continue
                ncontent = r.tr
                ocontent = oldr.tr
                if ncontent == ocontent:
                    continue
                if ocontent == "":
                    continue
                if ncontent == "":
                    r.tr = oldr.tr
                    continue
                r.tr = callback(r.en, ocontent, ncontent)

    def getExternalFiles(self):
        return findRecursive(self.enpath).extend(findRecursive(self.translationpath))

    def reload(self):
        enresources = findRecursive(self.enpath)
        resources = []
        for r in enresources:
            enr = r[len(self.enpath):]
            filename = r.replace(self.enpath, self.translationpath)
            if enr.endswith('.txt'):
                enval = open(r).read()
                trval = ""
                if os.path.isfile(filename):
                    trval = open(filename).read()
                resources.append(AppstoreEntry(filename, enval, trval))
        self.resources = resources

    def translationFiles(self):
        return [x.filename for x in self.resources]
