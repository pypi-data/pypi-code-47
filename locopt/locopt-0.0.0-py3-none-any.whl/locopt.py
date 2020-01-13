import os
import functools
import json


__all__ = ()


__cause = object()


class Error(Exception):

    __slots__ = ()

    def __iter__(self):

        yield from self.args


def execute(groups, name, *values, cause = __cause):

    """
    Get a formatted string or an exception in accordinance to the values.
    """

    fail = not cause is __cause

    templates = groups[fail]

    template = templates[name]

    content = template.format(*values)

    return Error(content, cause) if fail else content


def load(groups):

    """
    Get an object hosting callables for accessing templates.
    """

    speech = functools.partial(execute, groups)

    access = lambda name: functools.partial(speech, name)

    access = functools.lru_cache(None)(access)

    method = lambda self, name: access(name)

    space = {'__slots__': (), '__getattribute__': method, '__getitem__': method}

    value = type('', (), space)()

    return value
