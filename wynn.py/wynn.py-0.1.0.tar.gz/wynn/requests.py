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

import json
import urllib.request
import urllib.parse


def request(url, *args, **kwargs):
    """Requests a single JSON resource from the Wynncraft API.

    :param url: The URL of the resource to fetch
    :type url: :class:`str`
    :param args: Positional arguments to pass to the URL
    :param kwargs: Keyword arguments (:class:`str`) to pass to the URL

    :returns: The returned JSON object as a :class:`dict`
    :rtype: :class:`dict`
    """
    parsedArgs = (urllib.parse.quote(a) for a in args)

    parsedKwargs = {}
    for k,v in kwargs.items():
        parsedKwargs[k] = urllib.parse.quote(v)

    response = urllib.request.urlopen(url.format(*parsedArgs, **parsedKwargs))
    data = json.load(response)
    response.close()
    return data


def request_legacy(url, *args, **kwargs):
    """Requests a single JSON resource from the Wynncraft API in the
    legacy format.

    :param url: The URL of the resource to fetch
    :type url: :class:`str`
    :param args: Positional arguments to pass to the URL
    :param kwargs: Keyword arguments (:class:`str`) to pass to the URL

    :returns: The returned JSON object as a :class:`dict`
    :rtype: :class:`dict`
    """
    data = request(url, *args, **kwargs)
    if 'request' in data:
        del data['request']
    return data


def request_list(url, *args, **kwargs):
    """Requests a list of objects from the Wynncraft API in the most
    commonly used format.

    :param url: The URL of the resource to fetch
    :type url: :class:`str`
    :param args: Positional arguments to pass to the URL
    :param kwargs: Keyword arguments to pass to the URL

    :returns: The returned ``data`` as a :class:`dict`
    :rtype: :class:`dict`
    """
    return request(url, *args, **kwargs)['data']


def request_object(url, *args, **kwargs):
    """Requests a single object from the Wynncraft API in the most
    commonly used format.

    :param url: The URL of the resource to fetch
    :type url: :class:`str`
    :param args: Positional arguments to pass to the URL
    :param kwargs: Keyword arguments to pass to the URL

    :returns: The first element of the returned ``data`` as a
       :class:`dict`
    :rtype: :class:`dict`
    """
    return request_list(url, *args, **kwargs)[0]


def _wrap_object(value):
    if isinstance(value, dict):
        return ObjectFromDict(value)
    elif isinstance(value, list):
        return DictObjectList(value)
    return value


class ObjectFromDict:
    """Wraps a :class:`dict` in a Python object.

    Example use::

       >>> o = ObjectFromDict({'foo': 'bar'})
       >>> o.foo
       'bar'
       >>> o['foo']
       'bar'

    :param data: Parsed JSON data
    :type data: :class:`dict`
    """

    def __init__(self, data):
        self._data = data

    def __getattr__(self, name):
        try:
            return _wrap_object(self._data[name])
        except KeyError as e:
            raise AttributeError(e)

    def __getitem__(self, key):
        try:
            return _wrap_object(self._data[key])
        except KeyError as e:
            raise e
    
    def __contains__(self, key):
        return key in self._data

    def __repr__(self):
        return '{0}({1})'.format(type(self).__name__, repr(self._data))
    
    # pickle
    def __getstate__(self):
        return self._data
    
    # pickle
    def __setstate__(self, state):
        self._data = state


class DictObjectList:
    """Wraps a :class:`list` in such a way that :class:`dict` objects
    under it will be returned as :class:`ObjectFromDict`. Used
    internally by :class:`ObjectFromDict`.
    
    :param data: A list from parsed JSON data
    :type data: :class:`list`
    """

    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        try:
            return _wrap_object(self._data[key])
        except IndexError as e:
            raise e

    def __len__(self):
        return self._data.__len__()

    def __contains__(self, item):
        return self._data.__contains__(item)

    def __iter__(self):
        for item in self._data:
            yield _wrap_object(item)

    def __repr__(self):
        return '{0}({1})'.format(type(self).__name__, repr(self._data))
