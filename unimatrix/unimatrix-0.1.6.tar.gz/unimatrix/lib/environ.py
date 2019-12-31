"""Declares primitives to parse data from the operating
system environment.
"""


def parselist(environ, key, sep=':', cls=tuple):
    """Parses the environment variable into an iterable,
    using `sep` as a separator.
    """
    values = environ.get(key) or ''
    return cls(filter(bool, str.split(values, sep)))
