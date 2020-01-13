from jirafs.exceptions import MacroContentError
from jirafs.plugin import AutomaticReversalMacroPlugin


class Plugin(AutomaticReversalMacroPlugin):
    MIN_VERSION = '2.0.0'
    MAX_VERSION = '3.0.0'
    TAG_NAME = 'list-table'

    def get_row_by_number(self, columns, row):
        content = []

        for column in columns:
            content.append(column[row])

        return content

    def get_row_count(self, columns):
        return len(columns[0])

    def execute_macro(self, data, attrs, config, **kwargs):
        data = data.strip()
        columns = []
        current_column = []
        for line in data.strip().split('\n'):
            if line.startswith('* ') or line == '*':
                if current_column:
                    columns.append(current_column)
                    current_column = []
                line_content = line[1:].strip()
                current_column.append(line_content if line_content else ' ')
            elif line.startswith('** '):
                line_content = line[2:].strip()
                current_column.append(line_content if line_content else ' ')
            else:
                raise MacroContentError("Unexpected content: %s" % line)

        if current_column:
            columns.append(current_column)

        if not all([len(column) == len(columns[0]) for column in columns]):
            raise MacroContentError(
                "Specified table does not have columns of equal lengths!"
            )

        output_lines = []
        for idx in range(self.get_row_count(columns)):
            separator = '|'
            if idx == 0:
                separator = '||'

            row = self.get_row_by_number(columns, idx)
            output_lines.append(
                separator + separator.join(row) + separator
            )

        return '\n'.join(output_lines)
