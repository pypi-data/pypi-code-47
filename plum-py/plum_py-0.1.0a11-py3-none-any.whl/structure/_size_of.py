# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Sized structure member size_of() utility."""

from importlib import import_module

from .. import pack
from ._member import Member


def __touchup__(cls, value, parent):
    if value is None:
        sized_member = cls.__sizedmember__
        sized_object = getattr(parent, sized_member)

        if sized_object is None:
            # both size and sized member not provided,
            # use pre-calculated default from size of default sized member
            value = cls.__default__
        else:
            so_cls = cls.__sizedmember_type__
            if isinstance(sized_object, so_cls):
                value = sized_object.nbytes // cls.__ratio__
            else:
                value = len(pack(so_cls, sized_object)) // cls.__ratio__

    return value


class SizeMember(Member):

    """Structure size member definition."""

    __slots__ = [
        'cls',
        'default',
        'ignore',
        'name',
        'ratio',
        'sizedmember',
    ]

    def __init__(self, sizedmember, ratio, ignore=False, default=None):
        super(SizeMember, self).__init__(default, ignore)
        self.sizedmember = sizedmember
        self.ratio = ratio

    def adjust_members(self, members, name=None, cls=None, kwargs=None):
        """Perform adjustment to other members.

        :param dict members: structure member definitions
        :param str name: associated structure member name
        :param type cls: associated structure member member definition class
        :param dict kwargs: additional arguments to pass ``cls`` constructor

        """
        # delay import to avoid circular dependency
        size_via = import_module('._size_via', 'plum.structure')
        super().adjust_members(
            members, name=self.sizedmember, cls=size_via.SizedMember,
            kwargs={'ratio': self.ratio})

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        sized_member = members[self.sizedmember]
        if sized_member.default is None:
            default = 0
        else:
            default = sized_member.cls(sized_member.default).nbytes // self.ratio

        namespace = {
            '__default__': default,
            '__ratio__': self.ratio,
            '__sizedmember__': self.sizedmember,
            '__sizedmember_type__': sized_member.cls,
            '__touchup__': classmethod(__touchup__),
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace)


def size_of(sized, *, ratio=1, ignore=False):
    """Configure size structure member to follow size of associated structure member.

    :param str sized: sized member name
    :param int ratio: number of bytes per increment of member
    :param bool ignore: ignore member during comparisons
    :returns: structure member definition
    :rtype: SizeMember

    """
    return SizeMember(sized, ratio, ignore)
