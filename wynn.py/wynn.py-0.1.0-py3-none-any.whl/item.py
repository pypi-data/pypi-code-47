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


def search_item(*, name=None, category=None):
    """Searches for items. If a name is provided, will return a list of
    all items whose names contain the provided name (case insensitive).
    Otherwise, if a category is provided, will return a list
    of items of that type.

    .. note::

       This means that if both are provided, this function will only
       return items by name.

    :param name: A name to search for
    :type name: :class:`str`
    :param category: An item category to search for
    :type category: :class:`str`

    :returns: A list of items as
       :class:`ObjectFromDict <wynn.requests.ObjectFromDict>`
    :rtype: :class:`list`
    """
    if not name and not category:
        raise TypeError('Must provide at least one of name or category')

    if name is None:
        name = ''
    if category is None:
        category = ''

    return list(map(ObjectFromDict, request_legacy(
        'https://api.wynncraft.com/public_api.php?action=itemDB&search={0}&category={1}',
        name, category,
        )['items']))
