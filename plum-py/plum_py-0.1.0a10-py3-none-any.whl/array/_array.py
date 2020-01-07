# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Interpret bytes as a list of uniformly typed items."""

from .._plum import Plum, getbytes
from ..int.little import UInt8
from ._arraytype import ArrayType, GREEDY_DIMS


class Array(list, Plum, metaclass=ArrayType):

    """Interpret bytes as a list of uniformly typed items.

    :param iterable iterable: items

    """

    # filled in by metaclass
    __dims__ = GREEDY_DIMS
    __item_cls__ = UInt8
    __nbytes__ = None

    @classmethod
    def __unpack__(cls, buffer, offset, dump, parents, dims=None, outer_level=True):
        # pylint: disable=too-many-branches,too-many-locals,
        # pylint: disable=too-many-arguments,arguments-differ
        if dims is None:
            dims = cls.__dims__

        if dump and outer_level:
            dump.cls = cls

        self = list()

        if dims == GREEDY_DIMS:
            chunk, offset = getbytes(buffer, offset, cls.__nbytes__, dump, cls)

            _offset = 0
            _limit = None
            _len_chunk = len(chunk)

            i = 0
            item_cls = cls.__item_cls__
            if dump:
                dump.memory = b''
                while _offset < _len_chunk:
                    subdump = dump.add_level(access=f'[{i}]')
                    item, _offset, = item_cls.__unpack__(chunk, _offset, subdump, None)
                    self.append(item)
                    i += 1
            else:
                while _offset < _len_chunk:
                    item, _offset = item_cls.__unpack__(chunk, _offset, None, None)
                    self.append(item)
                    i += 1
        elif None in dims:
            raise TypeError(
                'greedy multidimensional array types do not support unpack operation')
        else:
            itemdims = dims[1:]
            if dump:
                if itemdims:
                    for i in range(dims[0]):
                        subdump = dump.add_level(access=f'[{i}]')
                        item, offset = cls.__unpack__(
                            buffer, offset, subdump, None, itemdims, False)
                        self.append(item)
                else:
                    item_cls = cls.__item_cls__
                    for i in range(dims[0]):
                        subdump = dump.add_level(access=f'[{i}]')
                        item, offset = item_cls.__unpack__(
                            buffer, offset, subdump, None)
                        self.append(item)
            else:
                if itemdims:
                    for i in range(dims[0]):
                        item, offset = cls.__unpack__(
                            buffer, offset, None, None, itemdims, False)
                        self.append(item)
                else:
                    item_cls = cls.__item_cls__
                    for i in range(dims[0]):
                        item, offset = item_cls.__unpack__(buffer, offset, None, None)
                        self.append(item)

        return self, offset

    @classmethod
    def __pack__(cls, buffer, offset, value, dump, dims=None, outer_level=True):
        # pylint: disable=too-many-arguments, arguments-differ

        if not isinstance(value, cls):
            value = cls(value)

        if dims is None:
            dims = value.__dims__

        itemdims = dims[1:]

        if dump:
            if outer_level:
                dump.cls = cls

            if itemdims:
                for i, item in enumerate(value):
                    offset = item.__pack__(
                        buffer, offset, item, dump.add_level(access=f'[{i}]'),
                        itemdims, False)
            else:
                item_cls = cls.__item_cls__
                for i, item in enumerate(value):
                    offset = item_cls.__pack__(
                        buffer, offset, item, dump.add_level(access=f'[{i}]'))
        else:
            if itemdims:
                for item in value:
                    offset = item.__pack__(buffer, offset, item, None, itemdims, False)
            else:
                item_cls = cls.__item_cls__
                for item in value:
                    offset = item_cls.__pack__(buffer, offset, item, None)

        return offset

    def __str__(self):
        lst = []
        for item in self:
            try:
                rpr = item.__baserepr__
            except AttributeError:
                rpr = item.__repr__

            lst.append(rpr())

        return f"[{', '.join(lst)}]"

    __baserepr__ = __str__

    def __repr__(self):
        # pylint: disable=no-member
        return f'{self.__class_name__}({self.__baserepr__()})'
