"""
Adds to the python dict by:
- Allowing access through the dict.key notation
- Allowing a default value to be set, which is returned if the key is not in the dictionary
- Option to warn if a default value is being returned
- Items may be set by dict.key = value notation
"""
# https://github.com/pdrharris/dictobject
# Copyright Peter Harris 2020
# Licence: MIT

from copy import deepcopy
from warnings import warn

DEFAULT_NOT_SET = '<<Default Value Not Set>>'


class DictObject(dict):
    """
    Adds to the python dict by:
    - Allowing access through the dict.key notation
    - New items may be set by dict.key = value notation
    - Allowing a default value to be set, which is returned if the key is not in the dictionary
    - Optionally warn if the key is not found and default value is being returned
    - Recursively change any nested dicts to DictObjects and back again
    - Deepcopy implemented

    Parameters:
        input_dict(dict): Optional. If not set, an empty dictionary is initialised.
        default_to: Optional. If set, this is the value that is returned if a key
            is not in the dictionary.
        warn_key_not_found (bool): Optional prints a warning if a key is not found and
            default_to is returned. Defaults to False.

    Example usage:
        from dictobject import DictObject
        dob = DictObject({'foo': 1, 'bar': 2}, default_to='Not Set')
        # default_to returned if the key is not found

        # Probably more normal would be to set default_to to None
        dob.foo
        # 1
        dob['bar']
        # 2

        # Return default value if key not found
        dob.baz
        # 'Not Set'

        dob.baz = 3 # Key baz not previously set
        dob.baz
        # 3

        # set default_to after instantiation
        dob = DictObject({'foo': 1, 'bar': 2})
        dob.bootle
        # Raises KeyError
        dob.set_default_to['Key not set']
        dob.bootle
        # 'Key not set'

        # Nesting
        ---------
        # (See later for converting nested dictionaries)

        dob.baz = DictObject({'a': 3, 'b': 4})
        dob
        # Note: Display indenting added for clarity
        # DictObject({
        #     'foo': 1,
        #     'bar': 2,
        #     'baz': DictObject({
        #         'a': 3,
        #         'b': 4
        #         })
        #     })

        dob.baz.a
        # 3

        dob.baz.c = 5
        dob
        # DictObject({
        #     'foo': 1,
        #     'bar': 2,
        #     'baz': DictObject({
        #         'a': 3,
        #         'b': 4,
        #         'c': 5
        #         })
        #     })

        # Optional warning
        # ----------------
        # Warn if a key is not found and default_to is being returned.
        # Particularlyl useful if default_to is set to None

        dob.set_default_to(None)
        dob = DictObject({'foo': 1, 'bar': 2}, default_to=None, warn_key_not_found=True)
        dob.not_a_key
        # => UserWarning: Key not_a_key not found in DictTuple. Returning None
        # Returns None

        # Set turn warnings on or off after instantiation
        dob.warn_key_not_found() # turns warnings on
        dob.warn_key_not_found(False) # turns warnings off

        # Converting to / from a dict
        # ----------------------------

        # Convert any nested dictionaries to DictObject
        dob.zonk = {'a': 'zonk', 'b': 'zonky'}
        dob
        # DictObject({'foo': 1, 'bar': 2, 'zonk': {'a': 'zonk', 'b': 'zonky'}})
        dob.zonk.c = {'d': 3, 'e': 4}
        dob
        # DictObject({
        #   'foo': 1,
        #   'bar': 2,
        #   'zonk': {
        #       'a': 'zonk',
        #       'b': 'zonky' 'c': {
        #           'd': 3,
        #           'e': 4
        #            }
        #       }
        #   })
        dob.convert_dicts(recursive=True)
        dob
        # DictObject({
        #   'foo': 1,
        #   'bar': 2,
        #   'zonk': DictObject{
        #       'a': 'zonk',
        #       'b': 'zonky',
        #       'c': DictObject{
        #           'd': 3,
        #           'e': 4}
        #       }
        #   })
        dob.zonk.c.d
        # 3

        # Convert back to a dict, including any nested objects
        dob.todict() # Defaults to recursive
        # {'foo': 1, 'bar': 2, 'zonk': {'a': 'zonk', 'b': 'zonky' 'c': {'d': 3, 'e': 4}}}

        dob.todict(False) # Nested DictObjects not converted to dict
        # {
        #   'foo': 1,
        #   'bar': 2,
        #   'zonk': DictObject{
        #       'a': 'zonk',
        #       'b': 'zonky',
        #       'c': DictObject{
        #           'd': 3,
        #           'e': 4}
        #       }
        #   }

        # All standard python dict functions work
        # --------------------------------------

        dob = DictObject({'foo': 1, 'bar': 2}, default_to='Not Set')
        dob.update({'bar': 'Two', 'baz': 3})
        dob
        # DictObject{'foo': 1, 'bar': 'Two', 'baz': 3}
        dob['bar'] = 'II'
        dob
        # DictObject{'foo': 1, 'bar': 'II', 'baz': 3}

        dob.keys()
        # dict_keys(['foo', 'bar', 'baz'])
        for key in dob:
            print(f'{key} = {dob[key]}')
        # foo = 1
        # bar = II
        # baz = 3

        'bazz' in dob
        # False

        dob = DictObject({'foo': 1, 'bar': 2}) # default_to is not set
        dob.baz
        # Raises KeyError

        dob['baz']
        # Raises KeyError

        dob.get('baz', 3)
        # 3

        # Copying
        # -------

        # Deepcopy
        from copy import deepcopy
        dob = DictObject({'foo': 1, 'bar': 2}, warn_key_not_found=True, default_to=None)
        dob.baz = {'a': 1, 'b': {'c': 3, 'd': 4}}
        dob.convert_dicts()
        dob
        # => DictObject{'foo': 1, 'bar': 2, 'baz': DictObject{'a': 1, 'b': {'c': 3, 'd': 4}}}
        dob2 = deepcopy(dob)
        dob.baz.a = 3
        dob
        # => DictObject{'foo': 1, 'bar': 2, 'baz': DictObject{'a': 3, 'b': {'c': 3, 'd': 4}}}
        dob2
        # => DictObject{'foo': 1, 'bar': 2, 'baz': DictObject{'a': 1, 'b': {'c': 3, 'd': 4}}}

        # Shallow copy
        # In the example above,
        # if dob2 is created with using
        # dob2 = dob.copy()
        # setting dob.baz.a = 3 would also change dob2.baz.a to 3

    """

    def __init__(
        self,
        input_dict: dict = None,
        default_to=DEFAULT_NOT_SET,
        warn_key_not_found: bool = False,
        convert_nested=False,
    ):
        super(DictObject, self).__init__(input_dict)
        self.__default_to__ = default_to
        self.__warn_key_not_found__ = warn_key_not_found
        if convert_nested:
            self.convert_dicts(recursive=True)

    def __getattr__(self, key):
        """Called by dob.key, e.g. x = dob.x"""
        return self.__getitem__(key)

    def __getitem__(self, key):
        """Called by dob[key, default], e.g. x = dob['x']"""
        try:
            return super(DictObject, self).__getitem__(key)
        except KeyError:
            return self._not_found(key)

    def _not_found(self, key):
        """
        If key is not found:
            1) If a default value has been passed, return it.
            2) if default_to has been set, return that value
                - Warn, if warn_key_not_found has been set.
            3) Raise KeyError
        """
        if self.__default_to__ != DEFAULT_NOT_SET:
            if self.__warn_key_not_found__:
                warning_text = (
                    f'Key {key} not found in DictObject. ' f'Returning {str(self.__default_to__)}'
                )
                warn(warning_text, stacklevel=3)
            return self.__default_to__

        raise KeyError('Key name {} not found and default_to not set.'.format(key))

    def __setattr__(self, key, value):
        """Called by dob.key = value, e.g. dob.x = 1"""
        if key in ('__default_to__', '__warn_key_not_found__'):
            # This condition is run during the init call,
            # to set up the original __default_to__ and __warn_key_not_found__ attributes
            super(DictObject, self).__setattr__(key, value)
            return
        self.__setitem__(key, value)

    def __repr__(self):
        """Called in an interactive session, e.g.
        dob = DictObject{'x', 1: 'y': 2}
        dob # __repr__ is called here
        => DictObject{'x', 1: 'y': 2}
        """
        return f'DictObject{super(DictObject, self).__repr__()}'

    def set_default_to(self, value):
        """Sets the value to default to if a field is not found."""
        self.__default_to__ = value

    def convert_dicts(self, recursive=False):
        """
        Converts all dictionaries in the DictObject to DictObjects
        Parameters:
            recursive (bool): Optional. If True, this is done recursively through all dictionaries
            to any number of levels i.e. any dictionaries that are members of dictionaries
            and so on.
            Defaults to False.
        """
        for key in super(DictObject, self).keys():
            value = super(DictObject, self).__getitem__(key)
            if isinstance(value, dict):
                super(DictObject, self).__setitem__(
                    key,
                    DictObject(
                        value,
                        default_to=self.__default_to__,
                        warn_key_not_found=self.__warn_key_not_found__,
                    ),
                )
            value = super(DictObject, self).__getitem__(key)
            if recursive and isinstance(value, self.__class__):
                self[key].convert_dicts(recursive=True)

    def todict(self, recursive=True):
        """
        Returns the DictObject as a dict.
        If recursive is set to True, any nested DictObjects will also be converted.

        Args:
            recursive (bool, optional): Convert any nested DictObjects. Defaults to True.

        Returns:
            dict: the DictObject as a dict
        """

        return_dict = dict(self)
        for key in return_dict:
            value = return_dict[key]
            if isinstance(value, self.__class__) and recursive:
                return_dict[key] = value.todict(recursive=recursive)

        return return_dict

    def warn_key_not_found(self, warning: bool = True):
        """
        Switches warning behaviour if key is not found and default value is returned.
        dob.warn_key_not_found() turns on warning.
        dob.warn_key_not_found(False) turns off warning.
        """
        self.__warn_key_not_found__ = warning

    def copy(self):
        """Creates a shallow copy of the dictionary."""
        return DictObject(
            input_dict=super(DictObject, self).copy(),
            default_to=self.__default_to__,
            warn_key_not_found=self.__warn_key_not_found__,
        )

    def __deepcopy__(self, memo):
        """
        # Required for:
        from copy import deepcopy
        dob2 = deepcopy(dob)

        # Returns a copy of the object with new copies of all nested items.
        """

        return_item = DictObject(
            input_dict={},
            default_to=self.__default_to__,
            warn_key_not_found=self.__warn_key_not_found__,
        )
        for key, value in self.items():
            return_item[key] = deepcopy(value, memo)

        return return_item
