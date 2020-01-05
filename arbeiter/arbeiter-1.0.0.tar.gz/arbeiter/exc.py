

class DuplicateLinesError(Exception):
    """At least two lines are identical in a text file

    This is used to prevent duplicated words/stories/names in
    memorization sheets.
    """
    def __init__(self, line, line_nr_first, line_nr_second):
        self.line = line
        self.line_nr_first = line_nr_first
        self.line_nr_second = line_nr_second

    def __str__(self):
        return f'Duplicated line {self.line!r} ' \
               f'at line nr {self.line_nr_first} and {self.line_nr_second}'
