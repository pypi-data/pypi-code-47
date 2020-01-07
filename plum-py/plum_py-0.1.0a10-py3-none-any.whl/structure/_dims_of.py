# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Sized array structure dims_of() member utility."""

from importlib import import_module

from ._member import Member
from ..int import Int


def __touchup_single__(cls, value, parent):
    if value is None:
        array = getattr(parent, cls.__arraymember__)
        if array is None:
            # both dims and array members not provided
            value = cls.__default_array_dims__
        else:
            value = len(array)

    return value


def __touchup_multi__(cls, value, parent):
    if value is None:
        array = getattr(parent, cls.__arraymember__)
        if array is None:
            # both dims and array members not provided
            value = cls.__default_array_dims__
        else:
            value = []
            for _ in range(cls.__dims__[0]):
                value.append(len(array))
                array = array[0]

    return value


class DimsMember(Member):

    """Dimensions structure member."""

    __slots__ = [
        'default',
        'name',
        'cls',
        'ignore',
        'arraymember',
        'default_array_dims'
    ]

    def __init__(self, arraymember, ignore=False):
        super(DimsMember, self).__init__(None, ignore)
        self.arraymember = arraymember
        self.default_array_dims = None  # filled in during adjust_members

    def adjust_members(self, members, name=None, cls=None, kwargs=None):
        """Perform adjustment to other members.

        :param dict members: structure member definitions
        :param str name: associated structure member name
        :param type cls: associated structure member member definition class
        :param dict kwargs: additional arguments to pass ``cls`` constructor

        """
        # delay import to avoid circular dependency
        dims_via = import_module('._dims_via', 'plum.structure')
        super().adjust_members(
            members, name=self.arraymember, cls=dims_via.ArrayMember)

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """

        default_array = members[self.arraymember].default

        if issubclass(self.cls, Int):
            if default_array is None:
                self.default_array_dims = 0
            else:
                self.default_array_dims = len(default_array)
        elif default_array is None:
            self.default_array_dims = [0] * self.cls.__dims__[0]
        else:
            self.default_array_dims = []
            for _ in range(self.cls.__dims__[0]):
                self.default_array_dims.append(len(default_array))
                default_array = default_array[0]

        namespace = {
            '__arraymember__': self.arraymember,
            '__default_array_dims__': self.default_array_dims,
            '__touchup__': classmethod(
                __touchup_single__ if issubclass(self.cls, Int) else __touchup_multi__),
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace)


def dims_of(array, ignore=False):
    """Configure dims structure member to follow dims of array structure member.

    :param str array: array member name
    :param bool ignore: ignore member during comparisons
    :returns: structure member definition
    :rtype: DimsMember

    """
    return DimsMember(array, ignore)
