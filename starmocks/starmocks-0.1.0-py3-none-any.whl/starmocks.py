import functools
from unittest import mock
from attrdict import AttrDict


def starmocks(func):

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        patchings = [arg for arg in args if isinstance(arg, mock.Mock)]
        args = tuple(arg for arg in args if arg not in patchings)

        kwargs["mocks"] = AttrDict({p._mock_name: p for p in patchings})

        return func(*args, **kwargs)

    return _wrapper
