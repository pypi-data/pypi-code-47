# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2019 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Packable/Unpacked bytes base class."""

# pylint: disable=too-many-lines

import functools

from ._dump import Dump

from ._exceptions import (
    ExcessMemoryError,
    ImplementationError,
    InsufficientMemoryError,
    PackError,
    SizeError,
    UnpackError,
)
from ._plumtype import PlumType


def _abbreviate_repr(item):
    rep = repr(item)
    if len(rep) > 30:
        rep = rep[0:27] + '...'
    return rep


class SizeProperty:

    """Size in bytes of packed plum instance."""

    def __get__(self, obj, objtype):
        nbytes = objtype.__nbytes__

        if nbytes is None:
            if obj is None:
                raise SizeError(f'{objtype.__name__!r} instance sizes vary')

            nbytes = len(pack_freeform(obj))

        return nbytes


class PackMethod:

    """Pack class/instance method facilitator."""

    def __init__(self, method):
        self.method = method.__func__

    def __get__(self, obj, objtype):
        if obj is None:
            method = functools.partial(self.method, objtype)
        else:
            method = functools.partial(self.method, objtype, item=obj)

        return method


class Plum:

    """Packable/Unpacked bytes base class."""

    __nbytes__ = None

    nbytes = SizeProperty()

    @classmethod
    def __unpack__(cls, buffer, offset, dump, parents):
        raise NotImplementedError(f'{cls.__name__!r} does not support plum.unpack()')

    @classmethod
    def __pack__(cls, buffer, offset, value, dump):
        raise NotImplementedError(f'{cls.__name__!r} does not support plum.pack()')

    def __baserepr__(self):
        raise NotImplementedError(f'{type(self).__name__!r} does not support repr()')

    def __repr__(self):
        return f'{type(self).__name__}({self.__baserepr__()})'

    @classmethod
    def __view__(cls, buffer, offset=0):
        """Create plum view of bytes buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. ``bytes``, ``bytearray``, ``memoryview``)
        :param int offset: byte offset

        """
        raise TypeError(f'{cls.__name__!r} does not support view()')

    @property
    def dump(self):
        """Packed bytes summary.

        :returns: summary table of view detailing bytes and layout
        :rtype: str

        """
        dump = Dump()
        _pack_freeform(bytearray(), 0, (self,), {}, dump)
        return dump

    @PackMethod
    @classmethod
    def pack(cls, item=None):  # pylint: disable=no-self-argument
        """Pack item as bytes.

        :param object item: packable item
        :returns: bytes buffer
        :rtype: bytearray

        For example:

            >>> from plum.int.little import UInt16
            >>> # use as class method (pass a value)
            >>> UInt16.pack(2)
            bytearray(b'\x02\x00')
            >>> # use as instance method (pass value to constructor))
            >>> UInt16(2).pack()
            bytearray(b'\x02\x00')

        """
        return pack_freeform(cls, item)

    @PackMethod
    @classmethod
    def pack_and_dump(cls, item=None):  # pylint: disable=no-self-argument
        """Pack item as bytes and produce bytes summary.

        :param object item: packable item
        :returns: bytes buffer, packed bytes summary
        :rtype: bytearray, Dump

        For example:

            >>> from plum.int.little import UInt16
            >>> # use as class method (pass a value as last argument)
            >>> membytes, dump = UInt16.pack_and_dump(2)
            >>> membytes
            bytearray(b'\x02\x00')
            >>> print(dump)
            +--------+-------+-------+--------+
            | Offset | Value | Bytes | Type   |
            +--------+-------+-------+--------+
            | 0      | 2     | 02 00 | UInt16 |
            +--------+-------+-------+--------+
            >>> # use as instance method (pass value to constructor))
            >>> membytes, dump = UInt16(2).pack_and_dump()
            >>> membytes
            bytearray(b'\x02\x00')
            >>> print(dump)
            +--------+-------+-------+--------+
            | Offset | Value | Bytes | Type   |
            +--------+-------+-------+--------+
            | 0      | 2     | 02 00 | UInt16 |
            +--------+-------+-------+--------+

        """
        return pack_freeform_and_dump(cls, item)

    @PackMethod
    @classmethod
    def pack_into(cls, buffer, offset, item=None):  # pylint: disable=no-self-argument
        r"""Pack item as bytes into a buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytearray, memoryview)
        :param int offset: start location within bytes buffer
        :param object item: packable item

        For example:

            >>> from plum.int.little import UInt8
            >>>
            >>> buffer = bytearray(4)
            >>> # use as class method (pass a value as last argument)
            >>> UInt8.pack_into(buffer, 1, 0x11)
            >>> # use as instance method (pass value to constructor))
            >>> UInt8(0x12).pack_into(buffer, 2)
            >>> buffer
            bytearray(b'\x00\x11\x12\x00')

        """
        pack_freeform_into(buffer, offset, cls, item)

    @PackMethod
    @classmethod
    def pack_into_and_dump(cls, buffer, offset, item=None):
        r"""Pack item as bytes into a buffer and produce bytes summary.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytearray, memoryview)
        :param int offset: start location within bytes buffer
        :param object item: packable item
        :returns: packed bytes summary
        :rtype: Dump

        For example:

            >>> from plum.int.little import UInt8
            >>>
            >>> buffer = bytearray(4)
            >>> # use as class method (pass a value as last argument)
            >>> dump = UInt8.pack_into_and_dump(buffer, 1, 0x11)
            >>> print(dump)
            +--------+-------+-------+-------+
            | Offset | Value | Bytes | Type  |
            +--------+-------+-------+-------+
            | 1      | 17    | 11    | UInt8 |
            +--------+-------+-------+-------+
            >>> # use as instance method (pass value to constructor))
            >>> dump = UInt8(0x12).pack_into_and_dump(buffer, 2)
            >>> print(dump)
            +--------+-------+-------+-------+
            | Offset | Value | Bytes | Type  |
            +--------+-------+-------+-------+
            | 2      | 18    | 12    | UInt8 |
            +--------+-------+-------+-------+
            >>> buffer
            bytearray(b'\x00\x11\x12\x00')

        """
        # pylint: disable=no-self-argument
        return pack_freeform_into_and_dump(buffer, offset, cls, item)

    @classmethod
    def unpack(cls, buffer):
        r"""Unpack item from bytes.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
        :returns: unpacked value
        :rtype: object (cls or type associated with cls)
        :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

        For example:
            >>> from plum.int.little import UInt16
            >>> UInt16.unpack(b'\x01\x02')
            513

        """
        return unpack(cls, buffer)

    @classmethod
    def unpack_and_dump(cls, buffer):
        r"""Unpack item from bytes and produce packed bytes summary.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
        :returns: tuple of (unpacked value, bytes summary)
        :rtype: object (cls or type associated with cls), Dump
        :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

        For example:
            >>> from plum.int.little import UInt16
            >>> value, dump = UInt16.unpack_and_dump(b'\x01\x02')
            >>> value
            513
            >>> print(dump)
            +--------+-------+-------+--------+
            | Offset | Value | Bytes | Type   |
            +--------+-------+-------+--------+
            | 0      | 513   | 01 02 | UInt16 |
            +--------+-------+-------+--------+

        """
        return unpack_and_dump(cls, buffer)

    @classmethod
    def unpack_from(cls, buffer, offset=None):
        r"""Unpack item from within a bytes buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
        :param int offset: starting byte offset (``None`` indicates current file position)
        :returns: unpacked value
        :rtype: object (cls or type associated with cls)
        :raises: ``UnpackError`` if insufficient bytes or value error

        For example:
            >>> from plum.int.little import UInt8
            >>> buffer = b'\x99\x01\x99'
            >>> UInt8.unpack_from(buffer, offset=1)
            1

        """
        return unpack_from(cls, buffer, offset)

    @classmethod
    def unpack_from_and_dump(cls, buffer, offset=None):
        """Unpack item from within a bytes buffer and produce packed bytes summary.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
        :param int offset: starting byte offset (``None`` indicates current file position)
        :returns: tuple of (unpacked items, bytes summary)
        :rtype: Plum (or tuple of Plum, or dict of Plum, dependent on ``fmt``), Dump
        :raises: ``UnpackError`` if insufficient bytes, or value error

        For example:
            >>> from plum.int.little import UInt8
            >>> buffer = b'\x99\x01\x99'
            >>> value, dump = UInt8.unpack_from_and_dump(buffer, offset=1)
            >>> value
            1
            >>> print(dump)
            +--------+-------+-------+-------+
            | Offset | Value | Bytes | Type  |
            +--------+-------+-------+-------+
            | 1      | 1     | 01    | UInt8 |
            +--------+-------+-------+-------+

        """
        return unpack_from_and_dump(cls, buffer, offset)

    @classmethod
    def view(cls, buffer, offset=0):
        """Create plum view of bytes buffer.

        :param buffer: bytes buffer
        :type buffer: bytes-like (e.g. bytes, bytearray, memoryview)
        :param int offset: byte offset

        For example:
            >>> from plum.int.little import UInt16
            >>> buffer = b'\x01\x02\x03\x04'
            >>> value = UInt16.view(buffer, offset=1)
            >>> value
            <view at 0x1: UInt16(770)>
            >>> value == 770
            True

        """
        return cls.__view__(buffer, offset)


def getbytes(buffer, offset, nbytes, dump, cls):
    """Get bytes from buffer.

    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
    :param int offset: offset into bytes buffer
    :param int nbytes: bytes to consume (``None`` returns remainder)
    :param Dump dump: bytes summary dump (``None`` skips dump annotation)
    :param type cls: plum type of item that consumed bytes are for
    :returns: tuple of (requested bytes, offset)
    :rtype: bytes-like, int, int or None

    """
    if nbytes is None:
        try:
            chunk = buffer[offset:]
        except TypeError:
            chunk = buffer.read()
        else:
            offset += len(chunk)

        if dump:
            dump.cls = cls
            dump.memory = chunk

    else:
        start = offset
        offset += nbytes
        try:
            chunk = buffer[start: offset]
        except TypeError:
            chunk = buffer.read(nbytes)

        if len(chunk) < nbytes:
            if dump:
                dump.cls = cls
                dump.value = '<insufficient bytes>'
                if len(chunk) > 16:
                    dump.add_extra_bytes('', chunk)
                else:
                    dump.memory = chunk

            cls_name = '' if cls is None else f'{cls.__name__} '

            unpack_shortage = (
                f'{nbytes - len(chunk)} too few bytes to unpack {cls_name}'
                f'({nbytes} needed, only {len(chunk)} available)')

            raise InsufficientMemoryError(unpack_shortage)

        if dump:
            dump.cls = cls
            dump.memory = chunk

    return chunk, offset


def _pack_item_with_format(fmt, buffer, offset, value, dump, indent):
    if isinstance(fmt, PlumType):
        offset = _pack_with_format(fmt, buffer, offset, [value], {}, dump, indent)

    elif isinstance(fmt, dict):
        if isinstance(value, dict):
            offset = _pack_with_format(fmt, buffer, offset, [], value, dump, indent)
        else:
            # fail nicely
            offset = _pack_with_format(fmt, buffer, offset, value, {}, dump, indent)

    elif isinstance(fmt, (tuple, list)):
        if isinstance(value, (tuple, list)):
            offset = _pack_with_format(fmt, buffer, offset, value, {}, dump, indent)
        else:
            # support len(fmt)==1, otherwise fail nicely
            offset = _pack_with_format(fmt, buffer, offset, [value], {}, dump, indent)

    else:
        # unknown format, fail nicely
        offset = _pack_with_format(fmt, buffer, offset, [value], {}, dump, indent)

    return offset


def _pack_with_format(fmt, buffer, offset, args, kwargs, dump, indent=0):
    # pylint: disable=too-many-statements,too-many-branches,too-many-nested-blocks
    # pylint: disable=too-many-locals,too-many-arguments
    try:
        if isinstance(fmt, PlumType):
            if args:
                if dump and not indent:
                    dump = dump.add_row(cls=fmt, indent=-1)

                offset = fmt.__pack__(buffer, offset, args[0], dump)

            if len(args) != 1:
                value_s = 'value' if len(args) == 1 else 'values'
                raise TypeError(f'{len(args)} {value_s} given, expected 1')

            if kwargs:
                value_s = 'value' if len(kwargs) == 1 else 'values'
                names = ", ".join(repr(k) for k in kwargs)
                raise TypeError(
                    f'unexpected keyword argument {value_s}: {names}')

        elif isinstance(fmt, (tuple, list)):

            for i, (subfmt, value) in enumerate(zip(fmt, args)):
                if dump:
                    dump = dump.add_row(access=f'[{i}]', indent=indent)

                offset = _pack_item_with_format(
                    subfmt, buffer, offset, value, dump, indent + 1)

            if len(args) != len(fmt):
                if dump:
                    if len(args) < len(fmt):
                        for i in range(len(args), len(fmt)):
                            dump.add_row(
                                cls=fmt[i], value='(missing)', access=f'[{i}]',
                                indent=indent)
                    else:
                        dump.last = True
                        for i in range(len(fmt), len(args)):
                            dump.add_row(
                                cls='(unexpected)', value=args[i], access=f'[{i}]',
                                indent=indent)

                value_s = "value" if len(args) == 1 else "values"
                raise TypeError(f'{len(args)} {value_s} given, expected {len(fmt)}')

            if kwargs:
                if dump:
                    dump.last = True
                    for key, value in kwargs.items():
                        dump.add_row(
                            access=f'[{key!r}]', value=value, cls='(unexpected)',
                            indent=indent)

                value_s = 'value' if len(kwargs) == 1 else 'values'
                names = ", ".join(repr(k) for k in kwargs)
                raise TypeError(f'unexpected keyword argument {value_s}: {names}')

        elif isinstance(fmt, dict):
            for key, subfmt in fmt.items():
                if dump:
                    dump = dump.add_row(access=f'[{key!r}]')

                try:
                    value = kwargs[key]
                except KeyError:
                    break

                offset = _pack_item_with_format(subfmt, buffer, offset, value, dump, indent + 1)

            if set(fmt) != set(kwargs):
                missing_names = set(fmt) - set(kwargs)
                if missing_names:
                    if dump:
                        for name in missing_names:
                            dump.value = '(missing)'
                            dump.cls = fmt[name]
                    value_s = "value" if len(missing_names) == 1 else "values"
                    names = ", ".join(repr(name) for name in missing_names)
                    raise TypeError(f'missing {value_s}: {names}')

                extra_kwargs = set(kwargs) - set(fmt)

                if dump:
                    dump.last = True
                    for name in extra_kwargs:
                        dump.add_row(
                            access=f'[{name!r}]', value=kwargs[name], cls='(unexpected)',
                            indent=indent)

                value_s = "value" if len(extra_kwargs) == 1 else "values"
                names = ", ".join(repr(name) for name in extra_kwargs)
                raise TypeError(f'unexpected {value_s}: {names}')

            if args:
                if dump:
                    dump.last = True
                    for arg in args:
                        dump.add_row(value=arg, cls='(unexpected)', indent=indent)
                        dump.last = True
                value_s = "value" if len(args) == 1 else "values"
                raise TypeError(f'got {len(args)} unexpected {value_s}')

        else:
            if dump:
                if not indent:
                    dump = dump.add_row()
                try:
                    dump.cls = fmt.__name__ + ' (invalid)'
                except AttributeError:
                    dump.cls = str(fmt) + ' (invalid)'

            raise TypeError(f'bad format type')

    except Exception as exc:
        if dump and not indent:
            unexpected_exception = (
                f"\n\n{dump}\n\n"
                f"{type(exc).__name__} occurred during pack operation:"
                f"\n\n{exc}")

            raise PackError(unexpected_exception)

        raise

    return offset


def pack(fmt, *args, **kwargs):
    r"""Pack values as bytes following a format.

    :param fmt: byte format of values
    :type fmt: Plum, tuple/list of Plum, or dict of Plum
    :param tuple args: packable values
    :param kwargs: packable values
    :returns: bytes buffer
    :rtype: bytearray

    For example:

        >>> from plum import pack
        >>> from plum.int.little import UInt8, UInt16
        >>> pack(UInt8, 1)
        bytearray(b'\x01')
        >>> pack((UInt8, UInt8), 1, 2)
        bytearray(b'\x01\x02')
        >>> pack({'a': UInt8, 'b': UInt8}, a=1, b=2)
        bytearray(b'\x01\x02')


    """
    buffer = bytearray()

    try:
        # attempt w/o dump for performance
        _pack_with_format(fmt, buffer, 0, args, kwargs, None)
    except Exception:
        # do it over to include dump in exception message
        _pack_with_format(fmt, buffer, 0, args, kwargs, Dump())
        raise ImplementationError()  # pragma: no cover

    return buffer


def pack_and_dump(fmt, *args, **kwargs):
    """Pack values as bytes and produce bytes summary following a format.

    :param fmt: byte format of values
    :type fmt: Plum, tuple/list of Plum, or dict of Plum
    :param tuple args: packable values
    :param kwargs: packable values
    :returns: bytes buffer, packed bytes summary
    :rtype: bytearray, Dump

    For example:

        >>> from plum import pack_and_dump
        >>> from plum.int.little import UInt8, UInt16
        >>>
        >>> buffer, dump = pack_and_dump(UInt8, 1)
        >>> buffer
        bytearray(b'\x01')
        >>> print(dump)
        +--------+-------+-------+-------+
        | Offset | Value | Bytes | Type  |
        +--------+-------+-------+-------+
        | 0      | 1     | 01    | UInt8 |
        +--------+-------+-------+-------+
        >>>
        >>> buffer, dump = pack_and_dump((UInt8, UInt8), 1, 2)
        >>> buffer
        bytearray(b'\x01\x02')
        >>> print(dump)
        +--------+--------+-------+-------+-------+
        | Offset | Access | Value | Bytes | Type  |
        +--------+--------+-------+-------+-------+
        | 0      | [0]    | 1     | 01    | UInt8 |
        | 1      | [1]    | 2     | 02    | UInt8 |
        +--------+--------+-------+-------+-------+
        >>>
        >>> buffer, dump = pack_and_dump({'a': UInt8, 'b': UInt8}, a=1, b=2)
        >>> buffer
        bytearray(b'\x01\x02')
        >>> print(dump)
        +--------+--------+-------+-------+-------+
        | Offset | Access | Value | Bytes | Type  |
        +--------+--------+-------+-------+-------+
        | 0      | ['a']  | 1     | 01    | UInt8 |
        | 1      | ['b']  | 2     | 02    | UInt8 |
        +--------+--------+-------+-------+-------+

    """
    buffer = bytearray()
    dump = Dump()
    _pack_with_format(fmt, buffer, 0, args, kwargs, dump)
    return buffer, dump


def pack_into(fmt, buffer, offset, *args, **kwargs):
    r"""Pack values as bytes into a buffer following a format.

    :param fmt: byte format of values
    :type fmt: Plum, tuple/list of Plum, or dict of Plum
    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytearray, memoryview)
    :param int offset: start location within bytes buffer
    :param tuple args: packable values
    :param kwargs: packable values

    For example:

        >>> from plum import pack_into
        >>> from plum.int.little import UInt8, UInt16
        >>>
        >>> fmt = (UInt8, UInt16)
        >>> buffer = bytearray(5)
        >>> offset = 1
        >>>
        >>> pack_into(fmt, buffer, offset, 0x11, 0x0302)
        >>> buffer
        bytearray(b'\x00\x11\x02\x03\x00')

    """
    offset = _adjust_and_validate_offset(buffer, offset)

    try:
        # attempt w/o dump for performance
        temp_buffer = pack(fmt, *args, **kwargs)
    except Exception:
        # do it over to include dump in exception message
        _pack_with_format(fmt, bytearray(), 0, args, kwargs, Dump(offset=offset))
        raise ImplementationError()  # pragma: no cover

    try:
        buffer[offset:offset + len(temp_buffer)] = temp_buffer
    except Exception as exc:
        unexpected_exception = (
            f"{type(exc).__name__} occurred during pack operation:"
            f"\n\n{exc}")

        raise PackError(unexpected_exception)


def pack_into_and_dump(fmt, buffer, offset, *args, **kwargs):
    r"""Pack values as bytes into a buffer following a format and produce bytes summary.

    :param fmt: byte format of values
    :type fmt: Plum, tuple/list of Plum, or dict of Plum
    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytearray, memoryview)
    :param int offset: start location within bytes buffer
    :param tuple args: packable values
    :param kwargs: packable values
    :returns: packed bytes summary
    :rtype: Dump

    For example:

        >>> from plum import pack_into_and_dump
        >>> from plum.int.little import UInt8, UInt16
        >>>
        >>> fmt = (UInt8, UInt16)
        >>> buffer = bytearray(5)
        >>> offset = 1
        >>>
        >>> dump = pack_into_and_dump(fmt, buffer, offset, 0x11, 0x0302)
        >>> print(dump)
        +--------+--------+-------+-------+--------+
        | Offset | Access | Value | Bytes | Type   |
        +--------+--------+-------+-------+--------+
        | 1      | [0]    | 17    | 11    | UInt8  |
        | 2      | [1]    | 770   | 02 03 | UInt16 |
        +--------+--------+-------+-------+--------+
        >>> buffer
        bytearray(b'\x00\x11\x02\x03\x00')

    """
    offset = _adjust_and_validate_offset(buffer, offset)

    dump = Dump(offset=offset)

    temp_buffer = bytearray()
    _pack_with_format(fmt, temp_buffer, 0, args, kwargs, dump)

    try:
        buffer[offset:offset + len(temp_buffer)] = temp_buffer
    except Exception as exc:
        unexpected_exception = (
            f"{type(exc).__name__} occurred during pack operation:"
            f"\n\n{exc}")

        raise PackError(unexpected_exception)

    return dump


def _pack_freeform(buffer, offset, items, kwargs, dump):
    # pylint: disable=too-many-branches, too-many-nested-blocks, too-many-statements
    original_dump = dump
    try:
        cls = None
        for item in items:
            if cls is None:
                if isinstance(item, PlumType):
                    cls = item
                    continue

                if isinstance(item, Plum):
                    cls = type(item)
                else:
                    try:
                        # get PlumType from the PlumView instance
                        cls = item.__type__
                    except AttributeError:
                        # not a PlumView instance, must be (cls, item) pair
                        try:
                            cls, item = item
                        except (TypeError, ValueError):
                            # TypeError -> not iterable, ValueError -> wrong size
                            if dump:
                                dump.add_row(
                                    value=str(item), cls=type(item).__name__ + ' (invalid)')
                            raise TypeError('value specified without a plum type')

                        if not isinstance(cls, PlumType):
                            if dump:
                                cls = cls.__name__ if isinstance(cls, type) else str(item)
                                dump.add_row(value=str(item), cls=cls + ' (invalid)')
                            raise TypeError('invalid plum type')

            if isinstance(item, PlumType):
                if dump:
                    dump.add_row(cls=cls, value='(missing)')
                raise TypeError('plum type specified without a value')

            if dump:
                dump = dump.add_row(cls=cls)
                dump.indent = -1

            offset = cls.__pack__(buffer, offset, item, dump)
            cls = None
            if dump:
                dump.rows[-1].last = True

        if cls is not None:
            if dump:
                dump.add_row(cls=cls, value='(missing)')
            raise TypeError('plum type specified without a value')

        for name, item in kwargs.items():
            if dump:
                dump = dump.add_row(access=name)

            if isinstance(item, Plum):
                offset = item.__pack__(buffer, offset, item, dump)
            else:
                try:
                    # get PlumType from the PlumView instance
                    cls = item.__type__
                except AttributeError:
                    # not a PlumView instance, must be (cls, item) pair
                    try:
                        cls, item = item
                    except (TypeError, ValueError):
                        # TypeError -> not iterable, ValueError -> wrong size
                        if dump:
                            dump.cls = type(item).__name__ + ' (invalid)'
                            dump.value = str(item)
                        raise TypeError('value specified without a plum type')

                    if not isinstance(cls, PlumType):
                        if dump:
                            cls = cls.__name__ if isinstance(cls, type) else str(cls)
                            dump.cls = cls + ' (invalid)'
                            dump.value = str(item)
                        raise TypeError('invalid plum type')

                offset = cls.__pack__(buffer, offset, item, dump)

            if dump:
                dump.rows[-1].last = True

    except Exception as exc:
        if original_dump:
            unexpected_exception = (
                f"\n\n{original_dump}\n\n"
                f"{type(exc).__name__} occurred during pack operation:"
                f"\n\n{exc}")

            raise PackError(unexpected_exception)

        raise


def pack_freeform(*args, **kwargs):
    r"""Pack values as bytes.

    :param tuple args: packable types and values or plum instances
    :param dict kwargs: packable types and values or plum instances
    :returns: bytes buffer
    :rtype: bytearray

    For example:

        >>> from plum import pack_freeform
        >>> from plum.int.little import UInt8, UInt16
        >>>
        >>> pack_freeform(UInt8, 1, UInt16(2))
        bytearray(b'\x01\x02\x00')

    """
    buffer = bytearray()
    try:
        # attempt w/o dump for performance
        _pack_freeform(buffer, 0, args, kwargs, None)
    except Exception:
        # do it over to include dump in exception message
        _pack_freeform(buffer, 0, args, kwargs, Dump())
        raise ImplementationError()  # pragma: no cover

    return buffer


def pack_freeform_and_dump(*args, **kwargs):
    """Pack values as bytes and produce bytes summary.

    :param tuple args: packable types and values or plum instances
    :param dict kwargs: packable types and values or plum instances
    :returns: bytes buffer, packed bytes summary
    :rtype: bytearray, Dump

    For example:

        >>> from plum import pack_freeform_and_dump
        >>> from plum.int.little import UInt8, UInt16
        >>>
        >>> buffer, dump = pack_freeform_and_dump(UInt8, 1, UInt16(2))
        >>> buffer
        bytearray(b'\x01\x02\x00')
        >>> print(dump)
        +--------+-------+-------+--------+
        | Offset | Value | Bytes | Type   |
        +--------+-------+-------+--------+
        | 0      | 1     | 01    | UInt8  |
        +--------+-------+-------+--------+
        | 1      | 2     | 02 00 | UInt16 |
        +--------+-------+-------+--------+

    """
    buffer = bytearray()
    dump = Dump()
    _pack_freeform(buffer, 0, args, kwargs, dump)
    return buffer, dump


def _adjust_and_validate_offset(buffer, offset):
    buffer_len = len(buffer)

    if offset < 0:
        adjusted_offset = buffer_len + offset
    else:
        adjusted_offset = offset

    if (adjusted_offset < 0) or (adjusted_offset > buffer_len):
        raise PackError(
            f'offset {offset} out of range for {buffer_len}-byte buffer')

    return adjusted_offset


def pack_freeform_into(buffer, offset, *args, **kwargs):
    r"""Pack values as bytes into a buffer.

    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytearray, memoryview)
    :param int offset: start location within bytes buffer
    :param tuple args: packable types and values or plum instances
    :param dict kwargs: packable types and values or plum instances

    For example:

        >>> from plum import pack_freeform_into
        >>> from plum.int.little import UInt8, UInt16
        >>>
        >>> buffer = bytearray(5)
        >>> pack_freeform_into(buffer, 1, UInt8(0x11))
        >>> pack_freeform_into(buffer, 2, UInt16, 0x0302)
        >>> buffer
        bytearray(b'\x00\x11\x02\x03\x00')

    """
    offset = _adjust_and_validate_offset(buffer, offset)

    try:
        # attempt w/o dump for performance
        temp_buffer = pack_freeform(*args, **kwargs)
    except Exception:
        # do it over to include dump in exception message
        _pack_freeform(bytearray(), 0, args, kwargs, Dump(offset=offset))
        raise ImplementationError()  # pragma: no cover

    try:
        buffer[offset:offset + len(temp_buffer)] = temp_buffer
    except Exception as exc:
        unexpected_exception = (
            f"{type(exc).__name__} occurred during pack operation:"
            f"\n\n{exc}")

        raise PackError(unexpected_exception)


def pack_freeform_into_and_dump(buffer, offset, *args, **kwargs):
    r"""Pack values as bytes into a buffer and produce bytes summary.

    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytearray, memoryview)
    :param int offset: start location within bytes buffer
    :param args: packable types and values
    :type args: tuple of plum types and/or values
    :param kwargs: packable items
    :type kwargs:  {name: plum instance} pairs
    :returns: packed bytes summary
    :rtype: Dump

    For example:

        >>> from plum import pack_freeform_into_and_dump
        >>> from plum.int.little import UInt8, UInt16
        >>>
        >>> buffer = bytearray(5)
        >>> dump = pack_freeform_into_and_dump(buffer, 1, UInt8(0x11), UInt16, 0x0302)
        >>> print(dump)
        +--------+-------+-------+--------+
        | Offset | Value | Bytes | Type   |
        +--------+-------+-------+--------+
        | 1      | 17    | 11    | UInt8  |
        +--------+-------+-------+--------+
        | 2      | 770   | 02 03 | UInt16 |
        +--------+-------+-------+--------+
        >>> buffer
        bytearray(b'\x00\x11\x02\x03\x00')

    """
    offset = _adjust_and_validate_offset(buffer, offset)

    dump = Dump(offset=offset)

    temp_buffer = bytearray()
    _pack_freeform(temp_buffer, 0, args, kwargs, dump)

    try:
        buffer[offset:offset + len(temp_buffer)] = temp_buffer
    except Exception as exc:
        unexpected_exception = (
            f"{type(exc).__name__} occurred during pack operation:"
            f"\n\n{exc}")

        raise PackError(unexpected_exception)

    return dump


def _unpack(fmt, buffer, offset, dump, prohibit_excess, indent=0):
    # pylint: disable=too-many-branches, too-many-locals
    original_dump = dump
    original_offset = offset

    try:
        if isinstance(fmt, PlumType):
            if dump and not indent:
                dump = dump.add_row(indent=-1)
            items, offset = fmt.__unpack__(buffer, offset, dump, None)

        elif isinstance(fmt, tuple):
            items = []
            for i, cls in enumerate(fmt):
                if dump:
                    dump = dump.add_row(access=f'[{i}]', indent=indent)
                item, offset = _unpack(cls, buffer, offset, dump, False, indent + 1)
                items.append(item)
            items = tuple(items)

        elif isinstance(fmt, list):
            items = []
            for i, cls in enumerate(fmt):
                if dump:
                    dump = dump.add_row(access=f'[{i}]', indent=indent)
                item, offset = _unpack(cls, buffer, offset, dump, False, indent + 1)
                items.append(item)

        elif isinstance(fmt, dict):
            items = {}
            for name, cls in fmt.items():
                if dump:
                    dump = dump.add_row(access=f'[{name!r}]', indent=indent)
                item, offset = _unpack(cls, buffer, offset, dump, False, indent + 1)
                items[name] = item

        else:
            raise TypeError('fmt must specify a Plum type (or a dict, tuple, or list of them)')

        if prohibit_excess:
            try:
                extra_bytes = buffer.read()
            except AttributeError:
                extra_bytes = buffer[offset:]

            if extra_bytes:
                if dump and dump.rows:
                    dump.rows[-1].last = True
                    for i in range(0, len(extra_bytes), 16):
                        dump.add_row(value='<excess bytes>', memory=extra_bytes[i:i+16])

                raise ExcessMemoryError(
                    f'{len(extra_bytes)} unconsumed bytes', extra_bytes)

    except Exception as exc:
        try:
            buffer.seek(original_offset)
        except AttributeError:
            pass  # must be bytes or bytearray

        if original_dump:
            unexpected_exception = (
                f"\n\n{original_dump}\n\n"
                f"{type(exc).__name__} occurred during unpack operation:"
                f"\n\n{exc}")

            raise UnpackError(unexpected_exception)

        raise

    return items, offset


def unpack(fmt, buffer):
    r"""Unpack item(s) from bytes.

    :param fmt: plum type, tuple of types, or dict of types
    :type fmt: Plum, tuple of Plum, or dict
    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
    :returns: unpacked items
    :rtype: Plum, tuple of Plum, or dict of Plum (dependent on ``fmt``)
    :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

    For example:
        >>> from plum import unpack
        >>> from plum.int.little import UInt8, UInt16
        >>> unpack(UInt16, b'\x01\x02')
        513
        >>> unpack((UInt8, UInt16), b'\x00\x01\x02')
        (0, 513)
        >>> unpack({'a': UInt8, 'b': UInt16}, b'\x00\x01\x02')
        {'a': 0, 'b': 513}

    """
    try:
        # _unpack(fmt, buffer, offset, dump, prohibit_excess)
        items, _offset = _unpack(fmt, buffer, 0, None, True)
    except Exception:
        # do it over to include dump in exception message
        unpack_and_dump(fmt, buffer)
        raise ImplementationError()  # pragma: no cover

    return items


def unpack_and_dump(fmt, buffer):
    r"""Unpack item(s) from bytes and produce packed bytes summary.

    :param fmt: plum type, tuple of types, or dict of types
    :type fmt: Plum, tuple of Plum, or dict
    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
    :returns: tuple of (unpacked items, bytes summary)
    :rtype: Plum (or tuple of Plum, or dict of Plum, dependent on ``fmt``), Dump
    :raises: ``UnpackError`` if insufficient bytes, excess bytes, or value error

    For example:
        >>> from plum import unpack_and_dump
        >>> from plum.int.little import UInt8, UInt16
        >>>
        >>> value, dump = unpack_and_dump((UInt8, UInt16), b'\x00\x01\x02')
        >>> value
        (0, 513)
        >>> print(dump)
        +--------+--------+-------+-------+--------+
        | Offset | Access | Value | Bytes | Type   |
        +--------+--------+-------+-------+--------+
        | 0      | [0]    | 0     | 00    | UInt8  |
        | 1      | [1]    | 513   | 01 02 | UInt16 |
        +--------+--------+-------+-------+--------+

    """
    dump = Dump()

    items, _offset = _unpack(fmt, buffer, 0, dump, True)

    return items, dump


def unpack_from(fmt, buffer, offset=None):
    r"""Unpack item from within a bytes buffer.

    :param fmt: plum type, tuple of types, or dict of types
    :type fmt: Plum, tuple of Plum, or dict
    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
    :param int offset: starting byte offset (``None`` indicates current file position)
    :returns: unpacked items
    :rtype: Plum, tuple of Plum, or dict of Plum (dependent on ``fmt``)
    :raises: ``UnpackError`` if insufficient bytes or value error

    For example:
        >>> from plum import unpack_from
        >>> from plum.int.little import UInt8
        >>>
        >>> buffer = b'\x99\x01\x99'
        >>> offset = 1
        >>>
        >>> unpack_from(UInt8, buffer, offset)
        1

    """
    if offset is None:
        try:
            offset = buffer.tell()
        except AttributeError:
            offset = 0
    else:
        try:
            buffer.seek(offset)
        except AttributeError:
            pass

    try:
        # _unpack(fmt, buffer, offset, dump, prohibit_excess)
        items, _offset = _unpack(fmt, buffer, offset, None, False)
    except Exception:
        # do it over to include dump in exception message
        unpack_from_and_dump(fmt, buffer, offset)
        raise ImplementationError()  # pragma: no cover

    return items


def unpack_from_and_dump(fmt, buffer, offset=None):
    r"""Unpack item from within a bytes buffer and produce packed bytes summary.

    :param fmt: plum type, tuple of types, or dict of types
    :type fmt: Plum, tuple of Plum, or dict
    :param buffer: bytes buffer
    :type buffer: bytes-like (e.g. bytes, bytearray, memoryview) or binary file
    :param int offset: starting byte offset (``None`` indicates current file position)
    :returns: tuple of (unpacked items, bytes summary)
    :rtype: Plum (or tuple of Plum, or dict of Plum, dependent on ``fmt``), Dump
    :raises: ``UnpackError`` if insufficient bytes or value error

    For example:
        >>> from plum import unpack_from_and_dump
        >>> from plum.int.little import UInt8
        >>>
        >>> buffer = b'\x99\x01\x99'
        >>> offset = 1
        >>>
        >>> value, dump = unpack_from_and_dump(UInt8, buffer, offset)
        >>> value
        1
        >>> print(dump)
        +--------+-------+-------+-------+
        | Offset | Value | Bytes | Type  |
        +--------+-------+-------+-------+
        | 1      | 1     | 01    | UInt8 |
        +--------+-------+-------+-------+

    """
    if offset is None:
        try:
            offset = buffer.tell()
        except AttributeError:
            offset = 0
    else:
        try:
            buffer.seek(offset)
        except AttributeError:
            pass

    dump = Dump(offset=offset)

    # _unpack(fmt, buffer, offset, dump, prohibit_excess)
    items, _offset = _unpack(fmt, buffer, offset, dump, False)

    return items, dump


plum_namespace = globals()
