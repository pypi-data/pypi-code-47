"""
 Copyright (C) 2019 biqqles.

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at http://mozilla.org/MPL/2.0/.

 This module defines Python analogues of C's types for use in Structs.

 Types defined by this module should
   a) subclass CType to inherit its special behaviour;
   b) subclass a Python builtin type*;
   c) define a format character as defined in <docs.python.org/3/library/struct.html#format-strings>.

   * When a class which subclasses Struct is instantiated, these types are replaced by this built-in type in the
     resulting instance. This also assists with type hinting.

 Todo: Add support for stdint.
"""
from typing import List
from ._meta import CType

class char(bytes, CType):
    type_code = 'c'

    @classmethod
    def value_of(cls, unpacked: List[bytes]):
        return b''.join(unpacked)

class schar(int, CType): type_code = 'b'

class uchar(schar): type_code = 'B'

class short(int, CType): type_code = 'h'

class ushort(short): type_code = 'H'

class long(int, CType): type_code = 'l'

class ulong(long): type_code = 'L'

class long_long(int, CType): type_code = 'q'

class ulong_long(long_long): type_code = 'Q'

class ssize_t(int, CType): type_code = 'n'

class size_t(int, CType): type_code = 'N'

class ptr(int): type_code = 'P'

class double(float, CType): type_code = 'd'

# types that shadow built-ins below here

class bool(int, CType): type_code = '?'  # bool can't be subclassed but it's just int in disguise anyway

class float(float, CType): type_code = 'f'

class int(int, CType): type_code = 'i'

class uint(int): type_code = 'I'

