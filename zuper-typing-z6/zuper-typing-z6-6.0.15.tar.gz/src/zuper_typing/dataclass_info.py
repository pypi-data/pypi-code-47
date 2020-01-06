from dataclasses import dataclass
from typing import Dict, Tuple, Type

from zuper_commons.text import pretty_dict
from zuper_commons.types import ZValueError
from zuper_typing.aliases import TypeLike

MULTI_ATT = "__dataclass_info__"

from . import logger

__all__ = ["get_dataclass_info", "set_dataclass_info", "DataclassInfo"]


class DataclassInfo:
    name: str  # only for keeping track
    # These are the open ones
    # generic_att_XXX: Tuple[TypeLike, ...]
    # These are the bound ones
    bindings: Dict[TypeLike, TypeLike]
    # These are the original ones
    orig: Tuple[TypeLike, ...]
    # Plus the ones we collected
    extra: Tuple[TypeLike, ...]

    def __init__(self, name, bindings, orig, extra):
        self.name = name
        self.bindings = bindings
        self.orig = orig
        self.extra = extra

    def get_open(self) -> Tuple[TypeLike, ...]:
        res = []
        for x in self.orig:
            if x not in self.bindings:
                res.append(x)
        for x in self.extra:
            if x not in self.bindings:
                res.append(x)

        return tuple(res)

    def __post_init__(self):
        for k in self.bindings:
            if k not in (self.orig + self.extra):
                msg = f"There is a bound variable {k} which is not an original one or child. "
                raise ZValueError(msg, di=self)

    def __repr__(self):
        # from .debug_print_ import debug_print
        debug_print = str
        return pretty_dict(
            "DataclassInfo",
            dict(
                name=self.name,
                orig=debug_print(self.orig),
                extra=debug_print(self.extra),
                bindings=debug_print(self.bindings),
            ),
        )


def set_dataclass_info(T, di: DataclassInfo):
    if not hasattr(T, MULTI_ATT):
        setattr(T, MULTI_ATT, {})
    ma = getattr(T, MULTI_ATT)

    ma[id(T)] = di


def get_dataclass_info(T: Type[dataclass]) -> DataclassInfo:
    default = DataclassInfo(T.__name__, {}, (), ())
    if not hasattr(T, MULTI_ATT):
        return default
    ma = getattr(T, MULTI_ATT)
    if not id(T) in ma:
        msg = f"Cannot find type info for {T} ({id(T)}"
        logger.info(msg, ma=ma)
        return default
    return ma[id(T)]
