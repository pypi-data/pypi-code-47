import csv

from jirafs.exceptions import MacroContentError
from jirafs.plugin import (
    VoidElementMacroPlugin,
)


class Plugin(VoidElementMacroPlugin):
    MIN_VERSION = '2.0.0'
    MAX_VERSION = '3.0.0'
    COMPONENT_NAME = 'csv-table'

    def execute_macro(
        self,
        data,
        filename="",
        delimiter=",",
        has_header=True,
        **kwargs
    ):
        if not filename:
            raise MacroContentError(
                "'filename' attribute is required."
            )
        if len(delimiter) != 1:
            raise MacroContentError(
                "'delimiter' attribute must be a one-character string."
            )

        lines = []

        header_printed = False
        with open(filename, 'r') as inf:
            reader = csv.reader(inf, delimiter=delimiter)
            for row in reader:
                if not row:
                    continue

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
