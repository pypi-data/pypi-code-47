#!/usr/bin/env python
from setuptools import setup
setup(
  name = 'cs.binary',
  description = 'Facilities associated with binary data parsing and transcription.',
  author = 'Cameron Simpson',
  author_email = 'cs@cskk.id.au',
  version = '20191230.3',
  url = 'https://bitbucket.org/cameron_simpson/css/commits/all',
  classifiers = ['Development Status :: 4 - Beta', 'Environment :: Console', 'Programming Language :: Python :: 3', 'Intended Audience :: Developers', 'Operating System :: OS Independent', 'Topic :: Software Development :: Libraries :: Python Modules', 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'],
  include_package_data = True,
  install_requires = ['cs.buffer'],
  keywords = ['python3'],
  license = 'GNU General Public License v3 or later (GPLv3+)',
  long_description = '*Latest release 20191230.3*:\nDocstring tweak.\n\nFacilities associated with binary data parsing and transcription.\n\nThe classes in this module support easy parsing of binary data\nstructures.\n\nThese classes work in conjuction with a `cs.buffer.CornuCopyBuffer`\n(henceforce a "buffer"),\nwhich presents an iterable of bytes-like values\nvia various useful methods\nand with factory methods to make one from a variety of sources\nsuch as bytes, iterables, binary files, `mmap`ped files,\nTCP data streams, etc.\n\nNote: this module requires Python 3 and recommends Python 3.6+\nbecause it uses abc.ABC, because a Python 2 bytes object is too\nweak (just a `str`) as also is my `cs.py3.bytes` hack class and\nbecause the keyword based `Packet` initiialisation benefits from\nkeyword argument ordering.\n\nIn the description below I use the word "chunk" to mean a piece\nof binary data obeying the buffer protocol, almost always a\n`bytes` instance or a `memoryview`, but in principle also things\nlike `bytearray`.\n\nThe functions and classes in this module the following:\n\nThe two base classes for binary data:\n* `PacketField`: an abstract class for a binary field, with a\n  factory method to parse it, a transcription method to transcribe\n  it back out in binary form and usually a `.value` attribute\n  holding the parsed value.\n* `Packet`: a `PacketField` subclass for parsing multiple\n  `PacketField`s into a larger structure with ordered named\n  fields.\n  The fields themselves may be `Packet`s for complex structures.\n\nSeveral presupplied subclasses for common basic types such\nas `UInt32BE` (an unsigned 32 bit big endian integer).\n\nClasses built from `struct` format strings:\n* `struct_field`: a factory for making PacketField classes for\n  `struct` formats with a single value field.\n* `multi_struct_field` and `structtuple`: factories for making\n  `PacketField`s from `struct` formats with multiple value\n  fields;\n  `structtuple` makes `PacketField`s which are also `namedtuple`s,\n  supporting trivial access to the parsed values.\n\nYou don\'t need to make fields only from binary data; because\n`PacketField.__init__` takes a post parse value, you can also\nconstruct `PacketField`s from scratch with their values and\ntranscribe the resulting binary form.\n\nEach `PacketField` subclass has the following methods:\n* `transcribe`: easily return the binary transcription of this field,\n  either directly as a chunk (or for convenience, also None or\n  an ASCII str) or by yielding successive binary data.\n* `from_buffer`: a factory to parse this field from a\n  `cs.buffer.CornuCopyBuffer`.\n* `from_bytes`: a factory to parse this field from a chunk with\n  an optional starting offset; this is a convenience wrapper for\n  `from_buffer`.\n\nThat may sound a little arcane, but we also supply:\n* `flatten`: a recursive function to take the return from any\n  `transcribe` method and yield chunks, so copying a packet to\n  a file or elsewhere can always be done by iterating over\n  `flatten(field.transcribe())` or via the convenience\n  `field.transcribe_flat()` method which calls `flatten` itself.\n* a `CornuCopyBuffer` is an easy to use wrapper for parsing any\n  iterable of chunks, which may come from almost any source.\n  It has a bunch of convenient factories including:\n  `from_bytes`, make a buffer from a chunk;\n  `from_fd`, make a buffer from a file descriptor;\n  `from_file`, make a buffer from a file-like object;\n  `from_mmap`, make a buffer from a file descriptor using a\n  memory map (the `mmap` module) of the file, so that chunks\n  can use the file itself as backing store instead of allocating\n  and copying memory.\n  See the `cs.buffer` module for further detail.\n\nWhen parsing a complex structure\none must choose between subclassing `PacketField` or `Packet`.\nAn effective guideline is the degree of substructure.\n\nA `Packet` is designed for deeper structures;\nall of its attributes are themselves `PacketField`s\n(or `Packet`s, which are `PacketField` subclasses).\nThe leaves of this hierarchy will be `PacketField`s,\nwhose attributes are ordinary types.\n\nBy contrast, a `PacketField`\'s attributes are "flat" values:\nthe plain post-parse value, such as a `str` or an `int`\nor some other conventional Python type.\n\nThe base case for `PacketField`\nis a single such value, named `.value`,\nand the natural implementation\nis to provide a `.value_from_buffer` method\nwhich returns the basic single value\nand the corresponding `.transcribe_value` method\nto return or yield its binary form\n(directly or in pieces respectively).\n\nHowever,\nyou can handle multiple attributes with this class\nby instead implementing:\n* `__init__`: to compose an instance from post-parse values\n  (and thus from scratch rather than parsed from existing binary data)\n* `from_buffer`: class method to parse the values\n  from a `CornuCopyBuffer` and call the class constructor\n* `transcribe`: to return or yield the binary form of the attributes\n\nCameron Simpson <cs@cskk.id.au> 22jul2018\n\n## Class `BSData(PacketField)`\n\nA run length encoded data chunk, with the length encoded as a BSUInt.\n\n## Class `BSSFloat(PacketField)`\n\nA float transcribed as a BSString of str(float).\n\n## Class `BSString(PacketField)`\n\nA run length encoded string, with the length encoded as a BSUInt.\n\n## Class `BSUInt(PacketField)`\n\nA binary serialsed unsigned int.\n\nThis uses a big endian byte encoding where continuation octets\nhave their high bit set. The bits contributing to the value\nare in the low order 7 bits.\n\n## Class `BytesesField(PacketField)`\n\nA field containing a list of bytes chunks.\n\nThe following attributes are defined:\n* `value`: the gathered data as a list of bytes instances,\n  or None if the field was gathered with `discard_data` true.\n* `offset`: the starting offset of the data.\n* `end_offset`: the ending offset of the data.\n\nThe `offset` and `end_offset` values are recorded during the\nparse, and may become irrelevant if the field\'s contents are\nchanged.\n\n## Class `BytesField(PacketField)`\n\nA field of bytes.\n\n## Class `BytesRunField(PacketField)`\n\nA field containing a continuous run of a single bytes value.\n\nThe following attributes are defined:\n* `length`: the length of the run\n* `bytes_value`: the repeated bytes value\n\nThe property `value` is computed on the fly on every reference\nand returns a value obeying the buffer protocol: a bytes or\nmemoryview object.\n\n## Class `EmptyPacketField(PacketField)`\n\nAn empty data field, used as a placeholder for optional\nfields when they are not present.\n\nThe singleton `EmptyField` is a predefined instance.\n\n## Function `fixed_bytes_field(length, class_name=None)`\n\nFactory for `BytesField` subclasses built from fixed length byte strings.\n\n## Function `flatten(chunks)`\n\nFlatten `chunks` into an iterable of `bytes` instances.\n\nThis exists to allow subclass methods to easily return ASCII\nstrings or bytes or iterables or even `None`, in turn allowing\nthem simply to return their superclass\' chunks iterators\ndirectly instead of having to unpack them.\n\n## Class `Float64BE(PacketField)`\n\nA `PacketField` which parses and transcribes the struct format `\'>d\'`.\n\n## Class `Float64LE(PacketField)`\n\nA `PacketField` which parses and transcribes the struct format `\'<d\'`.\n\n## Class `Int16BE(PacketField)`\n\nA `PacketField` which parses and transcribes the struct format `\'>h\'`.\n\n## Class `Int16LE(PacketField)`\n\nA `PacketField` which parses and transcribes the struct format `\'<h\'`.\n\n## Class `Int32BE(PacketField)`\n\nA `PacketField` which parses and transcribes the struct format `\'>l\'`.\n\n## Class `Int32LE(PacketField)`\n\nA `PacketField` which parses and transcribes the struct format `\'<l\'`.\n\n## Class `ListField(PacketField)`\n\nA field which is a list of other fields.\n\n## Function `multi_struct_field(struct_format, subvalue_names=None, class_name=None)`\n\nFactory for `PacketField` subclasses build around complex struct formats.\n\nParameters:\n* `struct_format`: the struct format string\n* `subvalue_names`: an optional namedtuple field name list;\n  if supplied then the field value will be a namedtuple with\n  these names\n* `class_name`: option name for the generated class\n\n## Class `Packet(PacketField)`\n\nBase class for compound objects derived from binary data.\n\n### Method `Packet.__init__(self, **fields)`\n\nInitialise the `Packet`.\n\nA `Packet` is its own `.value`.\n\nIf any keyword arguments are provided, they are used as a\nmapping of `field_name` to `Field` instance, supporting\ndirect construction of simple `Packet`s.\nFrom Python 3.6 onwards keyword arguments preserve the calling order;\nin Python versions earlier than this the caller should\nadjust the `Packet.field_names` list to the correct order after\ninitialisation.\n\n## Class `PacketField`\n\nA record for an individual packet field.\n\nThis normally holds a single value, such as a int of a particular size\nor a string.\n\nThere are 2 basic ways to implement a `PacketField` subclass.\n\nFor the simple case subclasses should implement two methods:\n* `value_from_buffer`:\n  parse the value from a `CornuCopyBuffer` and returns the parsed value\n* `transcribe_value`:\n  transcribe the value as bytes\n\nSometimes a `PacketField` may be slightly more complex\nwhile still not warranting (or perhaps fitting)\nthe formality of a `Packet` with its multifield structure.\n\nOne example is the `cs.iso14496.UTF8or16Field` class.\nThis supports an ISO14496 UTF8 or UTF16 string field,\nas as such has 2 attributes:\n* `value`: the string itself\n* `bom`: a UTF16 byte order marker or `None`;\n  `None` indicates that the string should be encoded as UTF-8\n  and otherwise the BOM indicates UTF16 big endian or little endian.\n\nTo make this subclass it defines these methods:\n* `from_buffer`:\n  to read the optional BOM and then the following encoded string;\n  it then returns the new `UTF8or16Field`\n  initialised from these values via `cls(text, bom=bom)`.\n* `transcribe`:\n  to transcribe the option BOM and suitably encoded string.\nThe instance method `transcribe` is required because the transcription\nrequires knowledge of the BOM, an attribute of an instance.\n\n### Method `PacketField.__init__(self, value=None)`\n\nInitialise the `PacketField`.\nIf omitted the inial field `value` will be `None`.\n\n## Function `struct_field(struct_format, class_name)`\n\nFactory for `PacketField` subclasses built around a single struct format.\n\nParameters:\n* `struct_format`: the struct format string, specifying a\n  single struct field\n* `class_name`: the class name for the generated class\n\nExample:\n\n    >>> UInt16BE = struct_field(\'>H\', class_name=\'UInt16BE\')\n    >>> UInt16BE.__name__\n    \'UInt16BE\'\n    >>> UInt16BE.format\n    \'>H\'\n    >>> UInt16BE.struct   #doctest: +ELLIPSIS\n    <Struct object at ...>\n    >>> field, offset = UInt16BE.from_bytes(bytes((2,3,4)))\n    >>> field\n    UInt16BE(515)\n    >>> offset\n    2\n    >>> field.value\n    515\n\n## Function `structtuple(class_name, struct_format, subvalue_names)`\n\nConvenience wrapper for multi_struct_field.\n\n## Class `UInt16BE(PacketField)`\n\nA `PacketField` which parses and transcribes the struct format `\'>H\'`.\n\n## Class `UInt16LE(PacketField)`\n\nA `PacketField` which parses and transcribes the struct format `\'<H\'`.\n\n## Class `UInt32BE(PacketField)`\n\nA `PacketField` which parses and transcribes the struct format `\'>L\'`.\n\n## Class `UInt32LE(PacketField)`\n\nA `PacketField` which parses and transcribes the struct format `\'<L\'`.\n\n## Class `UInt64BE(PacketField)`\n\nA `PacketField` which parses and transcribes the struct format `\'>Q\'`.\n\n## Class `UInt64LE(PacketField)`\n\nA `PacketField` which parses and transcribes the struct format `\'<Q\'`.\n\n## Class `UInt8(PacketField)`\n\nA `PacketField` which parses and transcribes the struct format `\'B\'`.\n\n## Class `UTF16NULField(PacketField)`\n\nA NUL terminated UTF-16 string.\n\n### Method `UTF16NULField.__init__(self, value, *, encoding)`\n\nInitialise the `PacketField`.\nIf omitted the inial field `value` will be `None`.\n\n## Class `UTF8NULField(PacketField)`\n\nA NUL terminated UTF-8 string.\n\n## Function `warning(msg, *a, f=None)`\n\nIssue a formatted warning message.\n\n\n\n# Release Log\n\n*Release 20191230.3*:\nDocstring tweak.\n\n*Release 20191230.2*:\nDocumentation updates.\n\n*Release 20191230.1*:\nDocstring updates. Semantic changes were in the previous release.\n\n*Release 20191230*:\nListField: new __iter__ method.\nPacket: __str__: accept optional `skip_fields` parameter to omit some field names.\nPacket: new .add_from_value method to add a named field with a presupplied value.\nPacket: new remove_field(field_name) and pop_field() methods to remove fields.\nBytesesField: __iter__ yields the bytes values, transcribe=__iter__.\nPacketField: propagate keyword arguments through various methods, required for parameterised PacketFields.\nNew UTF16NULField, a NUL terminated UTF16 string.\nPacketField: provide a default `.transcribe_value` method which makes a new instance and calls its `.transcribe` method.\nDocumentation update and several minor changes.\n\n*Release 20190220*:\nPacket.self_check: fields without a sanity check cause a warning, not a ValueError.\nNew Float64BE, Float64LE and BSSFloat classes for IEEE floats and floats-as-strings.\nAdditional module docstringage on subclassing Packet and PacketField.\nBSString: drop redundant from_buffer class method.\nPacketField.__init__: default to value=None if omitted.\n\n*Release 20181231*:\nflatten: do not yield zero length bytelike objects, can be misread as EOF on some streams.\n\n*Release 20181108*:\nNew PacketField.transcribe_value_flat convenience method to return a flat iterable of bytes-like objects.\nNew PacketField.parse_buffer generator method to parse instances of the PacketField from a buffer until end of input.\nNew PacketField.parse_buffer_values generator method to parse instances of the PacketField from a buffer and yield the `.value` attribute until end of input.\n\n*Release 20180823*:\nSome bugfixes.\nDefine PacketField.__eq__.\nBSUInt, BSData and BSString classes implementing the serialisations from cs.serialise.\nNew PacketField.value_from_bytes class method.\nNew PacketField.value_from_buffer method.\n\n*Release 20180810.2*:\nDocumentation improvements.\n\n*Release 20180810.1*:\nImprove module description.\n\n*Release 20180810*:\nBytesesField.from_buffer: make use of the buffer\'s skipto method if discard_data is true.\n\n*Release 20180805*:\nPacket: now an abstract class, new self_check method initially checking the\nPACKET_FIELDS class attribute against the instance, new methods get_field\nand set_field to fetch or replace existing fields, allow keyword arguments\nto initialise the Packet fields and document the dependency on keyword\nargument ordering.\nPacketField: __len__ computed directory from a transcribe, drop other __len__\nmethods.\nEmptyField singleton to use as a placeholder for missing optional fields.\nBytesField: implement value_s and from_buffer.\nmulti_struct_field: implement __len__ for generated class.\nflatten: treat memoryviews like bytes.\nAssorted docstrings and fixes.\n\n*Release 20180801*:\nInitial PyPI release.',
  long_description_content_type = 'text/markdown',
  package_dir = {'': 'lib/python'},
  py_modules = ['cs.binary'],
)
