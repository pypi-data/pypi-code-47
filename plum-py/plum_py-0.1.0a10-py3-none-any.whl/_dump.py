# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2020 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Pack/unpack bytes summary."""

TAB = '  '


class Dump:  # pylint: disable=too-many-instance-attributes

    """Pack/unpack bytes summary.

    :param int indent: access description indentation
    :param str access: access description
    :param str value: representation of value associated with bytes
    :param bits: start, end bit offset (None -> not a bit field)
    :type bits: tuple of (int, int)
    :param bytes memory: bytes
    :param str cls: plumtype name
    :param list rows: summary rows
    :param int offset: master byte offset

    """

    def __init__(self, indent=0, access='', value='', bits=None, memory=b'', cls='',
                 rows=None, offset=0):
        # pylint: disable=too-many-arguments
        if rows is None:
            rows = []

        self.indent = indent
        self.access = access
        self.value = value
        self.bits = bits
        self.memory = memory
        self.cls = cls
        self.rows = rows
        self.offset = offset
        self.last = False

    def __call__(self):
        print(self)

    def add_level(self, access='', value='', bits=None, memory=b'', cls=''):
        """Add row with access column value indented further.

        :param str access: access description
        :param str value: value representation associated with bytes
        :param bits: start, end bit offset (None -> not a bit field)
        :type bits: tuple of (int, int)
        :param bytes memory: bytes
        :param str cls: plumtype name

        """
        dump = Dump(self.indent + 1, access, value, bits, memory, cls, self.rows, self.offset)
        self.rows.append(dump)
        return dump

    def add_row(self, access='', value='', bits=None, memory=b'', cls='', indent=None):
        """Add row with access column value indention at same level.

        :param str access: access description
        :param str value: representation of value associated with bytes
        :param bits: start, end bit offset (None -> not a bit field)
        :type bits: tuple of (int, int)
        :param bytes memory: bytes
        :param cls: plumtype (or name of plumtype)
        :param int indent: access description indentation
        :type cls: type or str

        """
        # pylint: disable=too-many-arguments
        if indent is None:
            indent = self.indent
        dump = Dump(indent, access, value, bits, memory, cls, self.rows, self.offset)
        self.rows.append(dump)
        return dump

    def add_extra_bytes(self, access, memory):
        """Add rows listing bytes without access/value descriptions.

        :param str access: access description
        :param bytes memory: extra bytes

        """
        for i in range(0, len(memory), 16):
            self.add_level(access=access, memory=memory[i:i + 16])
            access = ''

    HEADERS = ['Offset', 'Access', 'Value', 'Bytes', 'Type']

    @property
    def cells(self):
        """Table row column values.

        :returns: column name/values
        :rtype: dict

        """
        try:
            pos, size = self.bits
        except TypeError:
            # bits is None
            bits = ''
        else:
            end = pos + size - 1
            if end == pos:
                bits = f'[{pos}]'
            else:
                bits = f'[{pos}:{pos + size - 1}]'

        return {
            'Offset': bits,  # byte offset prepended later
            'Access': TAB * self.indent + self.access,
            'Value': str(self.value),
            'Bytes': ' '.join('{:02x}'.format(c) for c in self.memory),
            # pylint: disable=no-member
            'Type': self.cls.__name__ if isinstance(self.cls, type) else str(self.cls),
        }

    def _get_lines(self):
        # pylint: disable=too-many-locals

        rows = list(row.cells for row in self.rows)
        last_flags = list(row.last for row in self.rows)
        last_flags[-1] = True

        # make bit offset information uniform in length
        if any(cells['Offset'] for cells in rows):
            fmt = '{:%ds}' % max(len(cells['Offset']) for cells in rows)
            for cells in rows:
                cells['Offset'] = fmt.format(cells['Offset'])

        # prepend byte offset
        nbytes = sum(len(row.memory) for row in self.rows)
        offset_template = '{:%dd}' % len(str(nbytes + self.offset))
        filler = ' ' * len(str(nbytes))
        consumed = 0
        for cells, row in zip(rows, self.rows):
            if row.memory:
                byte_offset = offset_template.format(self.offset + consumed)
                consumed += len(row.memory)
            else:
                byte_offset = filler
            cells['Offset'] = byte_offset + cells['Offset']

        headers = list(self.HEADERS)

        if not any(row.access for row in self.rows):
            headers.remove('Access')
            for row in rows:
                del row['Access']

        cell_sizes = [
            max([len(name)] + [len(cells[name]) for cells in rows])
            for name in headers]

        border = '+{}+'.format('+'.join('-' * (n + 2) for n in cell_sizes))
        row_template = '|{}|'.format('|'.join(' {:%ds} ' % n for n in cell_sizes))

        yield border
        yield row_template.format(*headers)
        yield border
        for row, cells, last in zip(self.rows, rows, last_flags):
            yield row_template.format(*cells.values())
            if last:
                yield border

    def __str__(self):
        return '\n'.join(self._get_lines())

    def __eq__(self, other):
        return (other is self) or (other == str(self))

    def __ne__(self, other):
        return not self.__eq__(other)
