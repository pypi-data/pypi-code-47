# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Sized structure member size_via() utility."""

from importlib import import_module

from .._exceptions import ExcessMemoryError
from .._plum import getbytes
from ._member import Member


def __unpack__(cls, buffer, offset, dump, parents):
    # pylint: disable=too-many-locals

    expected_size_in_bytes = getattr(parents[-1], cls.__sizemember__) * cls.__ratio__

    chunk, offset = getbytes(buffer, offset, expected_size_in_bytes, dump, cls)

    if dump:
        dump.memory = b''

    item, actual_size_in_bytes = cls.__original_unpack__(chunk, 0, dump, parents)

    extra_bytes = chunk[actual_size_in_bytes:]

    if extra_bytes:
        if dump:
            value = '<excess bytes>'
            for i in range(0, len(extra_bytes), 16):
                dump.add_row(value=value, memory=extra_bytes[i:i+16])
                value = ''

        raise ExcessMemoryError(f'{len(extra_bytes)} unconsumed bytes', extra_bytes)

    return item, offset


class SizedMember(Member):

    """Sized member definition."""

    __slots__ = [
        'cls',
        'default',
        'ignore',
        'name',
        'ratio',
        'sizemember',
    ]

    def __init__(self, sizemember, ratio, default=None, ignore=False):
        super(SizedMember, self).__init__(default, ignore)
        self.sizemember = sizemember
        self.ratio = ratio

    def adjust_members(self, members, name=None, cls=None, kwargs=None):
        """Perform adjustment to other members.

        :param dict members: structure member definitions
        :param str name: associated structure member name
        :param type cls: associated structure member member definition class
        :param dict kwargs: additional arguments to pass ``cls`` constructor

        """
        # delay import to avoid circular dependency
        size_of = import_module('._size_of', 'plum.structure')
        super().adjust_members(
            members, name=self.sizemember, cls=size_of.SizeMember,
            kwargs={'ratio': self.ratio})

    def finalize(self, members):
        """Perform final adjustments.

        :param dict members: structure member definitions

        """
        namespace = {
            '__ratio__': self.ratio,
            '__sizemember__': self.sizemember,
            '__unpack__': classmethod(__unpack__),
            '__original_unpack__': self.cls.__unpack__,
        }

        self.cls = type(self.cls)(self.cls.__name__, (self.cls,), namespace)


def size_via(size, *, ratio=1, default=None, ignore=False):
    """Configure structure member to follow size structure member.

    :param str size: size member name
    :param int ratio: number of bytes per increment of size member
    :param int default: initial value when unspecified
    :param bool ignore: ignore member during comparisons
    :returns: structure member definition
    :rtype: SizedMember

    """
    return SizedMember(size, ratio, default, ignore)
