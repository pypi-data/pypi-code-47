# Copyright (C) 2016-present the asyncpg authors and contributors
# <see AUTHORS file>
#
# This module is part of asyncpg and is released under
# the Apache 2.0 License: http://www.apache.org/licenses/LICENSE-2.0


__all__ = (
    'BitString', 'Point', 'Path', 'Polygon',
    'Box', 'Line', 'LineSegment', 'Circle',
)


class BitString:
    """Immutable representation of PostgreSQL `bit` and `varbit` types."""

    __slots__ = '_bytes', '_bitlength'

    def __init__(self, bitstring=None):
        if not bitstring:
            self._bytes = bytes()
            self._bitlength = 0
        else:
            bytelen = len(bitstring) // 8 + 1
            bytes_ = bytearray(bytelen)
            byte = 0
            byte_pos = 0
            bit_pos = 0

            for i, bit in enumerate(bitstring):
                if bit == ' ':
                    continue
                bit = int(bit)
                if bit != 0 and bit != 1:
                    raise ValueError(
                        'invalid bit value at position {}'.format(i))

                byte |= bit << (8 - bit_pos - 1)
                bit_pos += 1
                if bit_pos == 8:
                    bytes_[byte_pos] = byte
                    byte = 0
                    byte_pos += 1
                    bit_pos = 0

            if bit_pos != 0:
                bytes_[byte_pos] = byte

            bitlen = byte_pos * 8 + bit_pos
            bytelen = byte_pos + (1 if bit_pos else 0)

            self._bytes = bytes(bytes_[:bytelen])
            self._bitlength = bitlen

    @classmethod
    def frombytes(cls, bytes_=None, bitlength=None):
        if bitlength is None and bytes_ is None:
            bytes_ = bytes()
            bitlength = 0

        elif bitlength is None:
            bitlength = len(bytes_) * 8

        else:
            if bytes_ is None:
                bytes_ = bytes(bitlength // 8 + 1)
                bitlength = bitlength
            else:
                bytes_len = len(bytes_) * 8

                if bytes_len == 0 and bitlength != 0:
                    raise ValueError('invalid bit length specified')

                if bytes_len != 0 and bitlength == 0:
                    raise ValueError('invalid bit length specified')

                if bitlength < bytes_len - 8:
                    raise ValueError('invalid bit length specified')

                if bitlength > bytes_len:
                    raise ValueError('invalid bit length specified')

        result = cls()
        result._bytes = bytes_
        result._bitlength = bitlength

        return result

    @property
    def bytes(self):
        return self._bytes

    def as_string(self):
        s = ''

        for i in range(self._bitlength):
            s += str(self._getitem(i))
            if i % 4 == 3:
                s += ' '

        return s.strip()

    def to_int(self, bitorder='big', *, signed=False):
        """Interpret the BitString as a Python int.
        Acts similarly to int.from_bytes.

        :param bitorder:
            Determines the bit order used to interpret the BitString. By
            default, this function uses Postgres conventions for casting bits
            to ints. If bitorder is 'big', the most significant bit is at the
            start of the string (this is the same as the default). If bitorder
            is 'little', the most significant bit is at the end of the string.

        :param bool signed:
            Determines whether two's complement is used to interpret the
            BitString. If signed is False, the returned value is always
            non-negative.

        :return int: An integer representing the BitString. Information about
                     the BitString's exact length is lost.

        .. versionadded:: 0.18.0
        """
        x = int.from_bytes(self._bytes, byteorder='big')
        x >>= -self._bitlength % 8
        if bitorder == 'big':
            pass
        elif bitorder == 'little':
            x = int(bin(x)[:1:-1].ljust(self._bitlength, '0'), 2)
        else:
            raise ValueError("bitorder must be either 'big' or 'little'")

        if signed and self._bitlength > 0 and x & (1 << (self._bitlength - 1)):
            x -= 1 << self._bitlength
        return x

    @classmethod
    def from_int(cls, x, length, bitorder='big', *, signed=False):
        """Represent the Python int x as a BitString.
        Acts similarly to int.to_bytes.

        :param int x:
            An integer to represent. Negative integers are represented in two's
            complement form, unless the argument signed is False, in which case
            negative integers raise an OverflowError.

        :param int length:
            The length of the resulting BitString. An OverflowError is raised
            if the integer is not representable in this many bits.

        :param bitorder:
            Determines the bit order used in the BitString representation. By
            default, this function uses Postgres conventions for casting ints
            to bits. If bitorder is 'big', the most significant bit is at the
            start of the string (this is the same as the default). If bitorder
            is 'little', the most significant bit is at the end of the string.

        :param bool signed:
            Determines whether two's complement is used in the BitString
            representation. If signed is False and a negative integer is given,
            an OverflowError is raised.

        :return BitString: A BitString representing the input integer, in the
                           form specified by the other input args.

        .. versionadded:: 0.18.0
        """
        # Exception types are by analogy to int.to_bytes
        if length < 0:
            raise ValueError("length argument must be non-negative")
        elif length < x.bit_length():
            raise OverflowError("int too big to convert")

        if x < 0:
            if not signed:
                raise OverflowError("can't convert negative int to unsigned")
            x &= (1 << length) - 1

        if bitorder == 'big':
            pass
        elif bitorder == 'little':
            x = int(bin(x)[:1:-1].ljust(length, '0'), 2)
        else:
            raise ValueError("bitorder must be either 'big' or 'little'")

        x <<= (-length % 8)
        bytes_ = x.to_bytes((length + 7) // 8, byteorder='big')
        return cls.frombytes(bytes_, length)

    def __repr__(self):
        return '<BitString {}>'.format(self.as_string())

    __str__ = __repr__

    def __eq__(self, other):
        if not isinstance(other, BitString):
            return NotImplemented

        return (self._bytes == other._bytes and
                self._bitlength == other._bitlength)

    def __hash__(self):
        return hash((self._bytes, self._bitlength))

    def _getitem(self, i):
        byte = self._bytes[i // 8]
        shift = 8 - i % 8 - 1
        return (byte >> shift) & 0x1

    def __getitem__(self, i):
        if isinstance(i, slice):
            raise NotImplementedError('BitString does not support slices')

        if i >= self._bitlength:
            raise IndexError('index out of range')

        return self._getitem(i)

    def __len__(self):
        return self._bitlength


class Point(tuple):
    """Immutable representation of PostgreSQL `point` type."""

    __slots__ = ()

    def __new__(cls, x, y):
        return super().__new__(cls, (float(x), float(y)))

    def __repr__(self):
        return '{}.{}({})'.format(
            type(self).__module__,
            type(self).__name__,
            tuple.__repr__(self)
        )

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]


class Box(tuple):
    """Immutable representation of PostgreSQL `box` type."""

    __slots__ = ()

    def __new__(cls, high, low):
        return super().__new__(cls, (Point(*high), Point(*low)))

    def __repr__(self):
        return '{}.{}({})'.format(
            type(self).__module__,
            type(self).__name__,
            tuple.__repr__(self)
        )

    @property
    def high(self):
        return self[0]

    @property
    def low(self):
        return self[1]


class Line(tuple):
    """Immutable representation of PostgreSQL `line` type."""

    __slots__ = ()

    def __new__(cls, A, B, C):
        return super().__new__(cls, (A, B, C))

    @property
    def A(self):
        return self[0]

    @property
    def B(self):
        return self[1]

    @property
    def C(self):
        return self[2]


class LineSegment(tuple):
    """Immutable representation of PostgreSQL `lseg` type."""

    __slots__ = ()

    def __new__(cls, p1, p2):
        return super().__new__(cls, (Point(*p1), Point(*p2)))

    def __repr__(self):
        return '{}.{}({})'.format(
            type(self).__module__,
            type(self).__name__,
            tuple.__repr__(self)
        )

    @property
    def p1(self):
        return self[0]

    @property
    def p2(self):
        return self[1]


class Path:
    """Immutable representation of PostgreSQL `path` type."""

    __slots__ = '_is_closed', 'points'

    def __init__(self, *points, is_closed=False):
        self.points = tuple(Point(*p) for p in points)
        self._is_closed = is_closed

    @property
    def is_closed(self):
        return self._is_closed

    def __eq__(self, other):
        if not isinstance(other, Path):
            return NotImplemented

        return (self.points == other.points and
                self._is_closed == other._is_closed)

    def __hash__(self):
        return hash((self.points, self.is_closed))

    def __iter__(self):
        return iter(self.points)

    def __len__(self):
        return len(self.points)

    def __getitem__(self, i):
        return self.points[i]

    def __contains__(self, point):
        return point in self.points


class Polygon(Path):
    """Immutable representation of PostgreSQL `polygon` type."""

    __slots__ = ()

    def __init__(self, *points):
        # polygon is always closed
        super().__init__(*points, is_closed=True)


class Circle(tuple):
    """Immutable representation of PostgreSQL `circle` type."""

    __slots__ = ()

    def __new__(cls, center, radius):
        return super().__new__(cls, (center, radius))

    @property
    def center(self):
        return self[0]

    @property
    def radius(self):
        return self[1]
