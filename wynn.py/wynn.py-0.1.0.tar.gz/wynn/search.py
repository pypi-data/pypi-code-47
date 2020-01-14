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


def search(name):
    """Searches for guild and player names containing the search string.

    :param name: The name to search
    :type name: :class:`str`

    :returns: An object with attribute ``guilds`` containing guild name
       results and ``players`` containing player name results. The lists
       are empty if the query failed.
    :rtype: :class:`ObjectFromDict <wynn.requests.ObjectFromDict>`
    """
    res = request_legacy(
        'https://api.wynncraft.com/public_api.php?action=statsSearch&search={0}',
        name,
        )
    if 'error' in res:
        return ObjectFromDict({'guilds': [], 'players': []})
    return ObjectFromDict(res)
