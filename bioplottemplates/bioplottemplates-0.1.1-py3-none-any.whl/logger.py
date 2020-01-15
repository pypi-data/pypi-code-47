"""Manages operations with logging."""


class TitleLog:
    """Format string to title."""

    def __init__(self, msg, *args):
        self.msg = msg.title()
        self.args = args

    def __str__(self):  # noqa: D105
        return '\n* {} ...'.format(self.msg.format(*self.args))


class SubLog:
    """
    Format string to bullet point like structure.
    
    This format performs nicely under the `TitleLog` formatting.
    """
    
    def __init__(self, msg, *args):
        self.msg = msg
        self.args = args
    
    def __str__(self):  # noqa: D105
        return '    {}'.format(self.msg.format(*self.args))


T = TitleLog
S = SubLog
