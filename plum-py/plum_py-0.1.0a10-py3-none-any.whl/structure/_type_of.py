# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""type_of() structure member utility."""

from importlib import import_module

from ._member import Member


def __touchup__(cls, value, parent):
    if value is None:
        variably_typed_object = getattr(parent, cls.__variably_typed_member__)

        if variably_typed_object is None:
            value = cls.__default__
            if value is None:
                raise TypeError(
                    f"__init__() missing required argument {cls.__variably_typed_member__!r}")
        else:
            variable_object_type = type(variably_typed_object)

            for type_value, object_type in cls.__mapping__.items():
                if variable_object_type is object_type:
                    value = type_value
                    break
            else:
                mapping = cls.__mapping__
                raise TypeError(
                    f'structure member {cls.__variably_typed_member__!r} must '
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
        'variably_typed_member',
    ]

    def __init__(self, variably_typed_member, mapping, ignore=False, default=None):
        super(TypeMember, self).__init__(default, ignore)
        self.variably_typed_member = variably_typed_member
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
            members, name=self.variably_typed_member, cls=type_via.VariablyTypedMember,
            kwargs={'mapping': self.mapping})

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        default_object = members[self.variably_typed_member].default
        if default_object is None:
            default = None
        else:
            default_object_type = type(default_object)
            for type_value, object_type in self.mapping.items():
                if default_object_type is object_type:
                    default = type_value
                    break
            else:
                raise TypeError(
                    f"structure member {self.variably_typed_member!r} default must "
                    f"be one of the following types in the 'mapping' {self.mapping!r} "
                    f"not {default_object_type!r}")

        namespace = {
            '__default__': default,
            '__mapping__': self.mapping,
            '__membername__': self.name,
            '__touchup__': classmethod(__touchup__),
            '__variably_typed_member__': self.variably_typed_member,
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace)


def type_of(member, mapping, *, ignore=False):
    """Configure type structure member to follow type of associated structure member.

    :param str member: variably typed member name
    :param dict mapping: type member value (key) to Plum type (value) mapping
    :param bool ignore: ignore member during comparisons
    :returns: structure member definition
    :rtype: TypeMember

    """
    return TypeMember(member, mapping, ignore)
