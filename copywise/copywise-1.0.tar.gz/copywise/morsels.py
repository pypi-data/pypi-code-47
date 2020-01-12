from collections.abc import Iterable


def deep_flatten(i):
    for i in i:
        if isinstance(i, str):
            yield i
        elif isinstance(i, Iterable):
            yield from deep_flatten(i)
        else:
            yield i
