"""Modifying an object."""


import functools
import typing as t

import attr
import dataclasses


@functools.singledispatch
def modify(x: object, data: t.Mapping):
    """Modify object with data, returning a shallow new object.
    """
    if attr.has(type(x)):
        return attr.evolve(x, **data)
    if dataclasses.is_dataclass(type(x)):
        return dataclasses.replace(x, **data)
    raise NotImplementedError(type(x))


@modify.register(list)
@modify.register(dict)
@modify.register(bytearray)
def _(x, data: t.Mapping):
    x = x.copy()
    for k, v in data.items():
        x[k] = v
    return x


@modify.register(str)
@modify.register(bytes)
@modify.register(tuple)
def _(x, data: t.Mapping):
    return type(x)(modify(list(x), data))
