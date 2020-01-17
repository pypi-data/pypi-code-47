# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""type_of() structure member utility."""

from importlib import import_module

from ._member import Member


def __touchup__(cls, value, parent):
    if value is None:
        variably_typed_object = getattr(parent, cls.__variably_typed_member_name__)

        if variably_typed_object is None:
            variably_typed_object = cls.__variably_typed_member__.default

        if variably_typed_object is None:
            value = cls.__default__
            if value is None:
                raise TypeError(
                    f"__init__() missing required argument {cls.__variably_typed_member_name__!r}")
        else:
            variable_object_type = type(variably_typed_object)

            for type_value, object_type in cls.__mapping__.items():
                if variable_object_type is object_type:
                    value = type_value
                    break
            else:
                value = cls.__default__
                if value is None:
                    mapping = cls.__mapping__
                    raise TypeError(
                        f'structure member {cls.__variably_typed_member_name__!r} must '
                        f'be one of the following types: '
                        f'{list(repr(c) for c in mapping.values())} not {variable_object_type!r}')

    return value


class TypeMember(Member):

    """Structure variably typed member definition."""

    __slots__ = [
        'cls',
        'default',
        'ignore',
        'mapping',
        'name',
        'variably_typed_member_name',
    ]

    def __init__(self, variably_typed_member_name, mapping, default=None, ignore=False):
        super(TypeMember, self).__init__(default, ignore)
        self.variably_typed_member_name = variably_typed_member_name
        self.mapping = mapping

    def adjust_members(self, members, name=None, cls=None, kwargs=None):
        """Perform adjustment to other members.

        :param dict members: structure member definitions
        :param str name: associated structure member name
        :param type cls: associated structure member member definition class
        :param dict kwargs: additional arguments to pass ``cls`` constructor

        """
        # delay import to avoid circular dependency
        type_via = import_module('._type_via', 'plum.structure')
        super().adjust_members(
            members, name=self.variably_typed_member_name, cls=type_via.VariablyTypedMember,
            kwargs={'mapping': self.mapping})

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        namespace = {
            '__default__': self.default,
            '__mapping__': self.mapping,
            '__membername__': self.name,
            '__touchup__': classmethod(__touchup__),
            '__variably_typed_member_name__': self.variably_typed_member_name,
            '__variably_typed_member__': members[self.variably_typed_member_name],
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace)


def type_of(member, mapping, *, default=None, ignore=False):
    """Configure type structure member to follow type of associated structure member.

    :param str member: variably typed member name
    :param dict mapping: type member value (key) to Plum type (value) mapping
    :param object default: initial value when unspecified and can't be determined
    :param bool ignore: ignore member during comparisons
    :returns: structure member definition
    :rtype: TypeMember

    """
    return TypeMember(member, mapping, default, ignore)
