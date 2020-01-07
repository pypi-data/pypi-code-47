# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""type_via() member type utility."""

from importlib import import_module

from .._plum import Plum, PlumType
from ._member import Member


class Varies(Plum, metaclass=PlumType):

    """Variably typed member."""

    # overwritten in subclass (in VariablyTypedMember.finalize)
    __default__ = None
    __mapping__ = {}
    __membername__ = ''
    __type_member__ = ''

    # def __new__(cls, value):
    #    return value

    @classmethod
    def __touchup__(cls, value, parent):
        if value is None:
            value = cls.__default__
            if value is None:
                raise TypeError(
                    f"__init__() missing argument {cls.__membername__!r}")
        else:
            type_member = getattr(parent, cls.__type_member__)
            member_cls = cls.__mapping__[type_member]
            value = member_cls(value)
        return value

    @classmethod
    def __unpack__(cls, buffer, offset, dump, parents):
        type_member = getattr(parents[-1], cls.__type_member__)
        member_cls = cls.__mapping__[type_member]
        item, offset = member_cls.__unpack__(buffer, offset, dump, parents)
        if not isinstance(item, member_cls):
            # always create instance so that it may be re-packed (e.g. don't let
            # both UInt8 and UInt16 types produce int ... coerce into Plum type)
            item = member_cls(item)
        return item, offset

    @classmethod
    def __pack__(cls, buffer, offset, value, dump):
        return value.__pack__(buffer, offset, value, dump)

    __baserepr__ = object.__repr__


class VariablyTypedMember(Member):

    """Variably typed member definition."""

    __slots__ = [
        'cls',
        'default',
        'ignore',
        'mapping',
        'name',
        'type_member',
    ]

    def __init__(self, type_member, mapping, default=None, ignore=False):
        super(VariablyTypedMember, self).__init__(default, ignore)
        self.type_member = type_member
        self.mapping = mapping

    def adjust_members(self, members, name=None, cls=None, kwargs=None):
        """Perform adjustment to other members.

        :param dict members: structure member definitions
        :param str name: associated structure member name
        :param type cls: associated structure member member definition class
        :param dict kwargs: additional arguments to pass ``cls`` constructor

        """
        # delay import to avoid circular dependency
        type_of = import_module('._type_of', 'plum.structure')
        super().adjust_members(
            members, name=self.type_member, cls=type_of.TypeMember,
            kwargs={'mapping': self.mapping})

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        namespace = {
            '__default__': self.default,
            '__mapping__': self.mapping,
            '__membername__': self.name,
            '__type_member__': self.type_member,
        }
        self.cls = type('Varies', (Varies,), namespace)


def type_via(member, mapping, *, default=None, ignore=False):
    """Configure member's type to follow that specified by associated member.

    :param str member: variably typed member name
    :param dict mapping: type member value (key) to Plum type (value) mapping
    :param varies default: initial value when unspecified
    :param bool ignore: ignore member during comparisons
    :returns: structure member definition
    :rtype: VariablyTypedMember

    """
    return VariablyTypedMember(member, mapping, default, ignore)
