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

from .requests import request_list, request_object, ObjectFromDict


def get_recipe_ids():
    """Gets a :class:`list` of :class:`str` objects containing all
    recipe IDs from the Wynncraft API.

    :returns: A list of all recipeIDs as :class:`str`
    :rtype: :class:`list`
    """
    return request_list('https://api.wynncraft.com/v2/recipe/list')


def get_recipe(id):
    """Gets a Recipe as an
    :class:`ObjectFromDict <wynn.requests.ObjectFromDict>` object from
    the Wynncraft API.

    Format: https://docs.wynncraft.com/Recipe-API/#recipe-object

    :param name: The ID of the Recipe
    :type name: :class:`str`

    :returns: The Recipe returned by the API
    :rtype: :class:`ObjectFromDict <wynn.requests.ObjectFromDict>`
    """
    try:
        response = request_list(
            'https://api.wynncraft.com/v2/recipe/get/{0}',
            id
            )
        if not response:
            return None
        return ObjectFromDict(response[0])
    except HTTPError as e:
        if e.code == 400:
            return None
        raise e


def search_recipes(query, args):
    """Searches for recipes from the Wynncraft API. See
    https://docs.wynncraft.com/Recipe-API/#search for query
    format.

    :param query: See above link
    :type query: :class:`str`
    :param args: See above link
    :type args: :class:`str`

    :returns: A list of recipes as
       :class:`ObjectFromDict <wynn.requests.ObjectFromDict>`. Empty if
       the query failed.
    :rtype: :class:`list`
    """
    try:
        return list(map(ObjectFromDict, request_list(
            'https://api.wynncraft.com/v2/recipe/search/{0}/{1}',
            query, args,
            )))
    except HTTPError as e:
        if e.code == 400:
            return []
        raise e
