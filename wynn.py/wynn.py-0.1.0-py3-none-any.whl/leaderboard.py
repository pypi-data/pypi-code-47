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


def get_guild_leaderboard(timeframe=None):
    """Gets a guild leaderboard from Wynncraft.

    :param timeframe: A time frame to get the leaderboard from. If
       ``None``, ``'alltime'`` will be used.

       .. note::

          The format is not disclosed in the Wynncraft API documentation
    :type timeframt: :class:`str`

    :returns: A :class:`list` of guild leaderboard objects (Format:
       https://docs.wynncraft.com/Leaderboard-API/#guild-leaderboard-object)
       as :class:`ObjectFromDict <wynn.requests.ObjectFromDict>`
    :rtype: :class:`list`
    """
    if timeframe is None:
        timeframe = 'alltime'

    return list(ObjectFromDict(request_legacy(
        'https://api.wynncraft.com/public_api.php?action=statsLeaderboard&type=guild&timeframe={0}',
        timeframe
        )).data)


def get_player_leaderboard(timeframe=None):
    """Gets a player leaderboard from Wynncraft.

    :param timeframe: A time frame to get the leaderboard from. If
       ``None``, ``'alltime'`` will be used.

       .. note::

          The format is not disclosed in the Wynncraft API documentation
    :type timeframt: :class:`str`

    :returns: A :class:`list` of player leaderboard objects (Format:
       https://docs.wynncraft.com/Leaderboard-API/#player-leaderboard-object)
       as :class:`ObjectFromDict <wynn.requests.ObjectFromDict>`
    :rtype: :class:`list`
    """
    if timeframe is None:
        timeframe = 'alltime'

    return list(ObjectFromDict(request_legacy(
        'https://api.wynncraft.com/public_api.php?action=statsLeaderboard&type=player&timeframe={0}',
        timeframe
        )).data)


def get_pvp_leaderboard(timeframe=None):
    """Gets a player leaderboard from Wynncraft sorted by PvP kills.

    :param timeframe: A time frame to get the leaderboard from. If
       ``None``, ``'alltime'`` will be used.

       .. note::

          The format is not disclosed in the Wynncraft API documentation
    :type timeframt: :class:`str`

    :returns: A :class:`list` of player leaderboard objects (Format:
       https://docs.wynncraft.com/Leaderboard-API/#player-leaderboard-object)
       as :class:`ObjectFromDict <wynn.requests.ObjectFromDict>`
    :rtype: :class:`list`
    """
    if timeframe is None:
        timeframe = 'alltime'

    return list(ObjectFromDict(request_legacy(
        'https://api.wynncraft.com/public_api.php?action=statsLeaderboard&type=pvp&timeframe={0}',
        timeframe
        )).data)
