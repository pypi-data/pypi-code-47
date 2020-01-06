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
from urllib.parse import quote as urlquote
from urllib.request import urlopen

UD_DEFID_URL = "https://api.urbandictionary.com/v0/define?defid="
UD_DEFINE_URL = "https://api.urbandictionary.com/v0/define?term="
UD_RANDOM_URL = "https://api.urbandictionary.com/v0/random"


class UrbanDefinition(object):
    def __init__(self, word, definition, example, upvotes, downvotes):
        self.word = word
        self.definition = definition
        self.example = example
        self.upvotes = upvotes
        self.downvotes = downvotes

    def __str__(self):
        return "%s: %s%s (%d, %d)" % (
            self.word,
            self.definition[:50],
            "..." if len(self.definition) > 50 else "",
            self.upvotes,
            self.downvotes,
        )


def _get_urban_json(url):
    f = urlopen(url)
    data = json.loads(f.read().decode("utf-8"))
    f.close()
    return data


def _parse_urban_json(json, check_result=True):
    result = []
    if json is None or any(e in json for e in ("error", "errors")):
        raise Exception("UD: Invalid input for Urban Dictionary API")
    if check_result and ("list" not in json or len(json["list"]) == 0):
        return result
    for definition in json["list"]:
        d = UrbanDefinition(
            definition["word"],
            definition["definition"],
            definition["example"],
            int(definition["thumbs_up"]),
            int(definition["thumbs_down"]),
        )
        result.append(d)
    return result


def define(term):
    """Search for term/phrase and return list of UrbanDefinition objects.

    Keyword arguments:
    term -- term or phrase to search for (str)
    """
    json = _get_urban_json(UD_DEFINE_URL + urlquote(term))
    return _parse_urban_json(json)


def defineID(defid):
    """Search for UD's definition ID and return list of UrbanDefinition objects.

    Keyword arguments:
    defid -- definition ID to search for (int or str)
    """
    json = _get_urban_json(UD_DEFID_URL + urlquote(str(defid)))
    return _parse_urban_json(json)


def random():
    """Return random definitions as a list of UrbanDefinition objects."""
    json = _get_urban_json(UD_RANDOM_URL)
    return _parse_urban_json(json, check_result=False)
