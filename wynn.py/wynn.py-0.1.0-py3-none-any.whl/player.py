"""
Copyright 2020 Zakru

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from urllib.error import HTTPError

from .requests import request_object, ObjectFromDict


def get_player(name):
    """Gets a :class:`Player` object from the Wynncraft API.

    Format: https://docs.wynncraft.com/Player-API/#player-object

    :param name: The name of the Player
    :type name: :class:`str`

    :returns: The Player returned by the API or ``None`` if not found
    :rtype: :class:`Player`
    """
    try:
        return Player(request_object(
            'https://api.wynncraft.com/v2/player/{0}/stats',
            name
            ))
    except HTTPError as e:
        if e.code == 400:
            return None
        raise e


class Player(ObjectFromDict):
    """Contains Player data in the Wynncraft API format.

    Format: https://docs.wynncraft.com/Player-API/#player-object

    :param data: The parsed JSON data from the Wynncraft API
    :type data: :class:`dict`

    :ivar classesDict: A :class:`dict` containing key-value pairs of
       character class name → character class object
    :vartype classesDict: :class:`dict`
    :ivar classNames: A :class:`list` containing the names of the
       player's character classes
    :vartype classNames: :class:`list`
    """

    def __init__(self, data):
        super(Player, self).__init__(data)
        self.classesDict = {}
        self.classNames = []
        for cls in self.classes:
            self.classesDict[cls.name] = cls
            self.classNames.append(cls.name)
