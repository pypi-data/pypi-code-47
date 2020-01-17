# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Structure member definition."""


class Member:

    """Structure member definition."""

    __slots__ = [
        'default',
        'name',
        'cls',
        'ignore',
    ]

    def __init__(self, default=None, ignore=None):

        self.default = default
        self.ignore = ignore
        self.name = None  # assigned during structure class construction
        self.cls = None  # assigned during structure class construction

    def assign_name_and_class(self, name, cls, members):
        """Set member name and type.

        :param str name: member name
        :param type cls: member type

        """
        # pylint: disable=unused-argument
        self.name = name
        self.cls = cls

    def adjust_members(self, members, name=None, cls=None, kwargs=None):
        """Perform adjustment to other members.

        :param dict members: structure member definitions
        :param str name: associated structure member name
        :param type cls: associated structure member member definition class
        :param dict kwargs: additional arguments to pass ``cls`` constructor

        """
        if name and cls:
            for other_name, member_ in members.items():
                if other_name == name:
                    if not isinstance(member_, cls):
                        members[name] = cls(self.name, **(kwargs or {}))
                        members[name].name = name
                        members[name].cls = member_.cls
                        members[name].default = member_.default
                    break
            else:
                raise TypeError(
                    f'{self.name!r} member referenced undefined {name!r} member')

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """


# FUTURE: look at dataclass implementation as to why this should be a function
#         rather than just leaving user instantiate class directly
#         (has something to do with IDE introspection/hints)
def member(*, default=None, ignore=False):
    """Create structure member definition.

    :param int default: initial value when unspecified
    :param bool ignore: ignore member during comparisons
    :returns: structure member definition
    :rtype: Member

    """
    return Member(default, ignore)
