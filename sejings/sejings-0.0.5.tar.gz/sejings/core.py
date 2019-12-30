# Created: 10/12/2019
# Author:  Emiliano Jordan,
# Project: sejings
import copy
import json
import sys
from pathlib import WindowsPath, Path, PosixPath


def _in_doctest():
    """
    Thanks! https://stackoverflow.com/questions/8116118/
    how-to-determine-whether-code-is-running-in-a-doctest
    """
    if '_pytest.doctest' in sys.modules:
        return True

    if hasattr(sys.modules['__main__'], '_SpoofOut'):
        return True

    if sys.modules['__main__'].__dict__.get('__file__', '').endswith('/pytest'):
        return True

    return False


def blank(string: str):
    return string


def decode_bool(string: str):
    if string.lower() == 'false':
        return False
    if string.lower() == 'true':
        return True


sejings_type_mapping = {
    int: (int, blank),
    float: (float, blank),
    dict: (json.loads, json.dumps),
    list: (json.loads, json.dumps),
    bool: (decode_bool, blank),
    WindowsPath: (Path, blank),
    PosixPath: (Path, blank),
    Path: (Path, blank),
}


class Sejings:

    def __init__(self, value=(..., blank, blank)):

        self._set_value(value)

        super().__setattr__('_children', dict())

    def __call__(self, value=(..., blank, blank), encode=False):

        if isinstance(value, tuple) and value[0] is ...:
            if encode:
                return self._encoder(self._val)
            return self._val

        self._set_value(value)

    def __getattr__(self, item):

        if item == '__wrapped__' and _in_doctest():
            raise AttributeError

        setattr(self, item, Sejings())
        return super().__getattribute__(item)

    def __setattr__(self, key, value):

        if key == '_val':
            super().__setattr__(key, value)
            return

        if isinstance(value, Sejings):
            super().__setattr__(key, value)
            self._children[key] = value
            return

        try:
            obj = super().__getattribute__(key)
            obj(value)
        except AttributeError:
            new_sejings = Sejings(value)
            super().__setattr__(key, new_sejings)
            self._children[key] = new_sejings
            return

    def __len__(self):
        return len(self._children)

    def __copy__(self):

        cls = self.__class__

        new = cls((self._val, self._decoder, self._encoder))

        iterator: dict = copy.copy(self._children)

        for attr, val in iterator.items():
            if isinstance(val, cls):
                setattr(new, attr, val.__copy__())
            else:
                setattr(new, attr, val)

        return new

    def __deepcopy__(self, memodict):

        new_val = copy.deepcopy(self._val, memodict)

        new = self.__class__((new_val, self._decoder, self._encoder))

        iterator: dict = copy.copy(self._children)

        for attr, val in iterator.items():

            if id(val) in memodict:
                setattr(new, attr, memodict[id(val)])

            elif hasattr(val, '__deepcopy__'):
                setattr(new, attr, val.__deepcopy__(memodict))

            elif hasattr(val, 'copy') and callable(getattr(val, 'copy')):

                attr_copy = val.copy()

                if attr is not attr_copy:
                    memodict[id(val)] = attr_copy

                setattr(new, attr, attr_copy)

            elif hasattr(val, '__copy__'):

                attr_copy = val.__copy__()

                if attr is not attr_copy:
                    memodict[id(val)] = attr_copy

                setattr(new, attr, attr_copy)

            else:

                setattr(new, attr, val)

        return new

    def _set_value(self, value):

        if isinstance(value, tuple) \
                and len(value) == 3 \
                and callable(value[1]) \
                and callable(value[2]):
            value, decoder, encoder = value

        elif isinstance(value, tuple) \
                and len(value) == 2 \
                and callable(value[1]):

            value, decoder = value
            encoder = blank

        else:

            try:

                decoder, encoder = sejings_type_mapping[type(value)]

            except KeyError:

                for key, val in sejings_type_mapping.items():
                    if isinstance(value, key):
                        encoder, decoder = val
                        break
                else:
                    encoder, decoder = blank, blank

        super().__setattr__('_val', value)
        super().__setattr__('_decoder', decoder)
        super().__setattr__('_encoder', encoder)

sejings = Sejings()
