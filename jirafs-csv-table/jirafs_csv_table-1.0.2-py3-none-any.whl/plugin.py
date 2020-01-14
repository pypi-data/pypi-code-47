import csv
import io

from jirafs.exceptions import MacroContentError
from jirafs.plugin import AutomaticReversalMacroPlugin


class Plugin(AutomaticReversalMacroPlugin):
    MIN_VERSION = '2.0.0'
    MAX_VERSION = '3.0.0'
    TAG_NAME = 'csv-table'

    def execute_macro(
        self,
        data,
        attrs,
        config,
        **kwargs
    ):
        delimiter = attrs.get('delimiter', ',')
        has_header = attrs.get('has_header', True)

        if len(delimiter) != 1:
            raise MacroContentError(
                "'delimiter' attribute must be a one-character string."
            )

        lines = []

        header_printed = False

        inf = io.StringIO(data)
        reader = csv.reader(inf, delimiter=delimiter)
        for row in reader:
            if not row:
                continue

            # Make sure that each cell has at least a space
            row = [cell or ' ' for cell in row]

            column_separator = "|"

            if has_header and not header_printed:
                column_separator = "||"
                header_printed = True

            lines.append(
                column_separator
                + column_separator.join(row)
                + column_separator
            )

        return '\n'.join(lines)
