# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Sized array structure dims_via() member utility."""

from importlib import import_module

from ..int import Int
from ._member import Member


def __touchup_single__(cls, value, parent):
    if value is None:
        value = cls.__default__
        if value is None:
            dims = getattr(parent, cls.__dimsmember__)
            dims = [int(dims)]
            value = cls.__make_instance__(None, dims)

    return value


def __touchup_multi__(cls, value, parent):
    if value is None:
        value = cls.__default__
        if value is None:
            dims = getattr(parent, cls.__dimsmember__)
            dims = list(dims)
            value = cls.__make_instance__(None, dims)

    return value


def __unpack_single__(cls, buffer, offset, dump, parents):
    dims = (int(getattr(parents[-1], cls.__dimsmember__)), )
    return cls.__original_unpack__(buffer, offset, dump, None, dims)


def __unpack_multi__(cls, buffer, offset, dump, parents):
    dims = tuple(int(d) for d in getattr(parents[-1], cls.__dimsmember__))
    return cls.__original_unpack__(buffer, offset, dump, None, dims)


class ArrayMember(Member):

    """Array structure member definition."""

    __slots__ = [
        'cls',
        'default',
        'dimsmember',
        'ignore',
        'name',
    ]

    def __init__(self, dimsmember, default=None, ignore=False):
        super(ArrayMember, self).__init__(default, ignore)
        self.dimsmember = dimsmember

    def adjust_members(self, members, name=None, cls=None, kwargs=None):
        """Perform adjustment to other members.

        :param dict members: structure member definitions
        :param str name: associated structure member name
        :param type cls: associated structure member member definition class
        :param dict kwargs: additional arguments to pass ``cls`` constructor

        """
        # delay import to avoid circular dependency
        dims_of = import_module('._dims_of', 'plum.structure')
        super().adjust_members(
            members, name=self.dimsmember, cls=dims_of.DimsMember)

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        dims_cls = members[self.dimsmember].cls

        namespace = {
            '__default__': self.default,
            '__dimsmember__': self.dimsmember,
            '__touchup__': classmethod(
                __touchup_single__ if issubclass(dims_cls, Int) else __touchup_multi__),
            '__unpack__': classmethod(
                __unpack_single__ if issubclass(dims_cls, Int) else __unpack_multi__),
            '__original_unpack__': self.cls.__unpack__,
        }

        if issubclass(dims_cls, Int):
            dims = (None,)
        else:
            dims = [None] * dims_cls.__dims__[0]

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace, dims=dims)


def dims_via(dims, *, default=None, ignore=False):
    """Configure array structure member to follow dims structure member.

    :param str dims: array dimensions member name
    :param int default: initial value when unspecified
    :param bool ignore: ignore member during comparisons
    :returns: structure member definition
    :rtype: ArrayMember

    """
    return ArrayMember(dims, default, ignore)
