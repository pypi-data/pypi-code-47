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

from .requests import request_legacy, ObjectFromDict


def get_guilds():
    """Gets a list of guild names from the Wynncraft API.

    :returns: A :class:`list` of :class:`str` containing the names of
       all Wynncraft guilds.
    :rtype: :class:`list`
    """
    return request_legacy(
        'https://api.wynncraft.com/public_api.php?action=guildList'
        )['guilds']


def get_guild(name):
    """Gets a guild's information from the Wynncraft API.

    Format: https://docs.wynncraft.com/Guild-API/#guild-object

    :param name:
    :type name: :class:`str`

    :returns: The information of the guild as returned by the API or
       ``None`` if not found
    :rtype: :class:`Guild`
    """
    res = request_legacy(
        'https://api.wynncraft.com/public_api.php?action=guildStats&command={0}',
        name
        )
    if 'error' in res:
        return None        
    return Guild(res)


class Guild(ObjectFromDict):
    """Contains Guild data in the Wynncraft API format.

    Format: https://docs.wynncraft.com/Guild-API/#guild-object

    :param data: The parsed JSON data from the Wynncraft API
    :type data: :class:`dict`

    :ivar owner: The owner member of this guild
    :vartype owner: :class:`ObjectFromDict <wynn.requests.ObjectFromDict>`
    """

    def __init__(self, data):
        super(Guild, self).__init__(data)
        self.owner = [member for member in self.members if member.rank == 'OWNER'][0]
