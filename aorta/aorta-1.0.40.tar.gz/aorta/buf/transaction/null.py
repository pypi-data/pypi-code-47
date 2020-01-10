from .base import BaseTransaction


class NullTransaction(BaseTransaction):
    """A :class:`BaseTransaction` implementation that does
    nothing.
    """

    def flush(self):
        pass
