"""
 Copyright (C) 2019 biqqles.

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at http://mozilla.org/MPL/2.0/.

 This module contains the meta-programmatic magic that implements this package's special behaviour.
"""
from typing import Type, Any


class classproperty:
    """A class property decorator, analogous to the builtin @classmethod."""
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, instance, owner):
        return self.fget(owner)


class ArrayLengthSpecifiable(type):
    """Metaclass: repurposes square-bracket syntax to allow the definition of fixed-size arrays of a type - just like
    in C! (Though strictly speaking the syntax is more like C#'s.)
    E.g. char[10].length == 10 -- note that the use of type() here restricts arrays to one dimension."""
    def __getitem__(cls, length: int) -> Type:
        if length < 1:
            raise TypeError('Arrays of length < 1 are not permitted')
        return type(cls.__name__, cls.__bases__, dict(cls.__dict__, length=length))  # a copy of cls with altered length


class CType(metaclass=ArrayLengthSpecifiable):
    """A type supported by the built-in struct module."""
    type_code: str = None
    length: int = 1

    # todo: consider backwards compatibility: it would be fairly trivial to backport this library to much earlier Python
    #  versions by overriding __new__ and incrementing some counter on each class definition

    def __init__(self, length=1):
        # todo remove debug lines here
        print(f"init: Being called with length {length} as {type(self)}")
        self.length = length

    @classproperty
    def format_string(cls) -> str:
        """Forms a struct.py-compliant format string comprising of the length and type code."""
        assert cls.type_code
        return f'{cls.length}{cls.type_code}'

    @classmethod
    def value_of(cls, unpacked: Any):
        """Subclasses may override this method to define special conversion logic (after unpacking) if required."""
        return unpacked


class OnlyCTypeFieldsPermitted(type):
    """Metaclass: once applied to a class, only permits fields of types which are defined in this module."""
    def __new__(mcs, name, bases, dict_):
        if bases:  # if class being created subclasses something - i.e. ignore base class
            for field_type in dict_['__annotations__'].values():
                if not issubclass(field_type, CType):
                    raise TypeError('Only fixed-width types (defined in this module) can be used in Structs')
        return super().__new__(mcs, name, bases, dict_)