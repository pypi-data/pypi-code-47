from dataclasses import dataclass, fields
from typing import Tuple, Type, Dict, Optional

from zuper_commons.text import pretty_dict
from zuper_commons.types import ZValueError
from zuper_typing.aliases import TypeLike
from .annotations_tricks import is_TypeLike
from .get_patches_ import is_dataclass_instance

MULTI_ATT = "__dataclass_info__"

from . import logger

__all__ = ["get_dataclass_info", "set_dataclass_info", "DataclassInfo"]


class DataclassInfo:
    name: str  # only for keeping track
    # These are the open ones
    # generic_att_XXX: Tuple[TypeLike, ...]
    # These are the bound ones
    # bindings: Dict[TypeLike, TypeLike]
    # These are the original ones
    orig: Tuple[TypeLike, ...]

    # Plus the ones we collected
    # extra: Tuple[TypeLike, ...]
    specializations: Dict[Tuple, type]
    _open: Optional[Tuple[TypeLike, ...]]

    def __init__(self, *, name: str, orig: Tuple[TypeLike, ...]):
        self.name = name
        # self.bindings = bindings
        self.orig = orig
        if not isinstance(orig, tuple):
            raise ZValueError(sself=self)
        for _ in orig:
            if not is_TypeLike(_):
                raise ZValueError(sself=self)
        # self.extra = extra
        # if bindings: raise ZException(self=self)
        self.specializations = {}
        self._open = None

    def get_open(self) -> Tuple[TypeLike, ...]:
        from zuper_typing.recursive_tricks import find_typevars_inside

        if self._open is None:
            res = []
            for x in self.orig:
                for y in find_typevars_inside(x):
                    if y not in res:
                        res.append(y)
            self._open = tuple(res)

        return self._open

    #
    # def get_open_old(self) -> Tuple[TypeLike, ...]:
    #     res = []
    #     for x in self.orig:
    #           if x not in self.bindings:
    #             res.append(x)
    #     for x in self.extra:
    #         if x not in self.bindings:
    #             res.append(x)
    #
    #     return tuple(res)

    # def __post_init__(self):
    #     for k in self.bindings:
    #         if k not in (self.orig + self.extra):
    #             msg = f"There is a bound variable {k} which is not an original one or child. "
    #             raise ZValueError(msg, di=self)

    def __repr__(self):
        # from .debug_print_ import debug_print
        debug_print = str
        return pretty_dict(
            "DataclassInfo",
            dict(
                name=self.name,
                orig=debug_print(self.orig),
                # extra=debug_print(self.extra),
                # bindings=debug_print(self.bindings)
                open=self.get_open(),
            ),
        )


def set_dataclass_info(T, di: DataclassInfo):
    assert is_TypeLike(T), T
    if not hasattr(T, MULTI_ATT):
        setattr(T, MULTI_ATT, {})
    ma = getattr(T, MULTI_ATT)

    ma[id(T)] = di


def get_dataclass_info(T: Type[dataclass]) -> DataclassInfo:
    assert is_TypeLike(T), T
    default = DataclassInfo(name=T.__name__, orig=())
    if not hasattr(T, MULTI_ATT):
        return default
    ma = getattr(T, MULTI_ATT)
    if not id(T) in ma:
        msg = f"Cannot find type info for {T} ({id(T)}"
        logger.info(msg, ma=ma)
        return default
    return ma[id(T)]


def get_fields_values(x: dataclass) -> Dict[str, object]:
    assert is_dataclass_instance(x), x
    res = {}
    T = type(x)
    try:
        fields_ = fields(T)
    except Exception as e:
        raise ZValueError(T=T) from e
    for f in fields_:
        k = f.name
        v0 = getattr(x, k)
        res[k] = v0
    return res
