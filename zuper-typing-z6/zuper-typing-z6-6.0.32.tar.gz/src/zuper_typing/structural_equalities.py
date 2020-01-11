from dataclasses import Field, fields, is_dataclass
from typing import Dict, List, Type, TypeVar, Optional

from zuper_commons.types import ZValueError
from zuper_typing.get_patches_ import is_dataclass_instance
from . import dataclass
from .my_dict import get_DictLike_args, get_ListLike_arg, is_DictLike, is_ListLike


@dataclass
class EqualityResult:
    result: bool
    why: "Dict[str, EqualityResult]"
    a: object
    b: object
    msg: Optional[str] = None

    def __bool__(self) -> bool:
        return self.result


X = TypeVar("X")


def eq(T: Type[X], a: X, b: X) -> EqualityResult:
    # todo: tuples
    if is_dataclass(T):
        return eq_dataclass(T, a, b)
    elif is_ListLike(T):
        return eq_listlike(T, a, b)
    elif is_DictLike(T):
        return eq_dictlike(T, a, b)
    else:
        if not (a == b):
            return EqualityResult(result=False, a=a, b=b, why={}, msg="by equality")
        else:
            return EqualityResult(result=True, a=a, b=b, why={})


K = TypeVar("K")
V = TypeVar("V")


def eq_dictlike(T: Type[Dict[K, V]], a: Dict[K, V], b: Dict[K, V]) -> EqualityResult:
    k1 = set(a)
    k2 = set(b)
    if k1 != k2:
        return EqualityResult(result=False, a=a, b=b, why={}, msg="different keys")
    _, V = get_DictLike_args(T)

    why = {}
    for k in k1:
        va = a[k]
        vb = a[k]
        r = eq(V, va, vb)
        if not r.result:
            r[k] = r

    result = len(why) == 0
    return EqualityResult(result=result, why=(why), a=a, b=b)


def eq_listlike(T: Type[List[V]], a: List[V], b: List[V]) -> EqualityResult:
    k1 = len(a)
    k2 = len(b)
    if k1 != k2:
        return EqualityResult(result=False, a=a, b=b, msg="different length")
    V = get_ListLike_arg(T)

    why = {}
    for i in range(k1):
        va = a[i]
        vb = a[i]
        r = eq(V, va, vb)
        if not r.result:
            r[str(i)] = r

    result = len(why) == 0
    return EqualityResult(result=result, why=(why), a=a, b=b)


def eq_dataclass(T, a, b):
    if not (is_dataclass(T) and is_dataclass_instance(a) and is_dataclass_instance(b)):
        raise ZValueError(T=T, a=a, b=b)

    _fields: List[Field] = fields(T)
    why = {}
    for f in _fields:
        va = getattr(a, f.name)
        vb = getattr(b, f.name)

        res = eq(f.type, va, vb)
        if not res.result:
            why[f.name] = res

    result = len(why) == 0
    return EqualityResult(result=result, why=dict(why), a=a, b=b)
