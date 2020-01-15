"""
 Copyright (C) 2019 biqqles.

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""

import struct
from enum import Enum
from typing import Any, List
from ._meta import CType, OnlyCTypeFieldsPermitted, classproperty


class ByteOrder(Enum):
    NATIVE = '='
    BIG_ENDIAN = '>'
    LITTLE_ENDIAN = '<'


class TypeSizes(Enum):
    NATIVE = '@'
    STANDARD = ''


class Struct(metaclass=OnlyCTypeFieldsPermitted):
    __byte_order__: ByteOrder = ByteOrder.NATIVE
    __type_sizes__: TypeSizes = TypeSizes.STANDARD

    def __init__(self, buffer: bytes):
        # using this (base) class directly is nonsensical; it must be subclassed to be used
        if self.__class__ is Struct:
            raise TypeError('This class must be subclassed to be used')

        if self.__type_sizes__ is TypeSizes.NATIVE and self.__byte_order__ is not TypeSizes.NATIVE:
            raise AttributeError('Native type sizes must be used with native byte order. This is a limitation of '
                                 'Python\'s struct')

        # unpack buffer
        unpacked: List[Any] = list(struct.unpack(self.format_string, buffer))

        # and set fields
        for field_name, field_type in self.__annotations__.items():  # type: str, CType
            if field_type.length > 1:
                field_value = tuple(unpacked.pop(0) for i in range(field_type.length))
            else:
                field_value = unpacked.pop(0)
            self.__setattr__(field_name, field_type.value_of(field_value))

    @classproperty
    def format_string(cls) -> str:
        """Return a format string (understood by struct) that is calculated from this Struct's definition.
        This works because, according to the source for dataclasses.py in the standard library, __annotations__ 'is
        guaranteed to be ordered' (thanks to the new dict implementation in Python 3.6)."""
        prefix = cls.__type_sizes__.value or cls.__byte_order__.value
        return prefix + ''.join(t.format_string for t in cls.__annotations__.values())

    @classproperty
    def sizeof(cls) -> int:
        """The total size in bytes of the struct. Equivalent to C's sizeof."""
        return struct.calcsize(cls.format_string)
