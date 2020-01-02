import builtins
from functools import reduce
import forbiddenfruit


def _map(self, fun, *iterables, **kwargs):
    return self.__class__(map(fun, self, *iterables, **kwargs))


def _filter(self, fun, *iterables, **kwargs):
    return self.__class__(filter(fun, self, *iterables, **kwargs))


def _zip(self, *others):
    return self.__class__(zip(*tuple(self, *others)))


def _enumerate(self):
    return self.__class__(enumerate(self))


def _reduce(self, fun, initial=None):
    return reduce(fun, self, initial) if initial else reduce(fun, self)


def _sum(self, start=0):
    return sum(self, start=start)


def _apply(self, fun, *args, **kwargs):
    return fun(self, *args, **kwargs)




def curse(classes=[list, tuple, set, dict]):
    """Add functional methods to list, tuple, set, and dict in-place."""
    cursed_methods = {
        "map": _map,
        "filter": _filter,
        "reduce": _reduce,
        "apply": _apply,
        "zip": _zip,
        "enumerate": _enumerate,
    }
    for klass in classes:
        for name, fun in cursed_methods.items():
            forbiddenfruit.curse(klass, name, fun)


def reverse(classes=[list, tuple, set, dict]):
    """Add functional methods to list, tuple, set, and dict in-place."""
    cursed_methods = {
        "map": _map,
        "filter": _filter,
        "reduce": _reduce,
        "apply": _apply,
        "zip": _zip,
        "enumerate": _enumerate,
    }
    for klass in classes:
        for name, fun in cursed_methods.items():
            forbiddenfruit.reverse(klass, name)
