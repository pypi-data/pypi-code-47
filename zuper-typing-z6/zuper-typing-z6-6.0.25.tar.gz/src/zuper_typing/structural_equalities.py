from dataclasses import Field, fields, is_dataclass
from typing import Dict, List, Type, TypeVar

from zuper_commons.types import ZValueError
from zuper_typing.get_patches_ import is_dataclass_instance
from . import dataclass


@dataclass
class EqualityResult:
    result: bool
    why: "Dict[str, EqualityResult]"
    a: object
    b: object

    def __post_init__(self):
        if not self.result:
            assert self.why, self

    def __bool__(self) -> bool:
        return self.result


X = TypeVar("X")


def eq(T: Type[X], a: X, b: X) -> EqualityResult:
    if not (is_dataclass(T) and is_dataclass_instance(a) and is_dataclass_instance(b)):
        raise ZValueError(T=T, a=a, b=b)

    _fields: List[Field] = fields(T)
    why = {}
    for f in _fields:
        va = getattr(a, f.name)
        vb = getattr(b, f.name)
        if is_dataclass(f.type):
            res = eq(f.type, va, vb)
            if not res.result:
                why[f.name] = res
        else:
            if not (va == vb):
                res = EqualityResult(result=False, a=va, b=vb, why={})
                why[f.name] = res

    result = len(why) == 0
    return EqualityResult(result=result, why=dict(why), a=a, b=b)
