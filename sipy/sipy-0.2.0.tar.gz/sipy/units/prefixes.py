# -*- coding: utf-8 -*-
# Standard Library
from typing import Type

# SIpy
from sipy.config import prefixes
from sipy.units.si import SIBaseUnit

# todo tests for this module


class UnitMultiple(SIBaseUnit):
    MULTIPLIER: float = 0

    def _to(self, value: float) -> float:
        return value * self.MULTIPLIER

    def _from(self, value: float) -> float:
        return value / self.MULTIPLIER

    @classmethod
    def factory(cls, name: str, *args):
        new_prefix: Type[UnitMultiple] = type(name, (cls,), {})
        new_prefix.MULTIPLIER = float(args[0])
        return new_prefix


class Prefix(UnitMultiple):
    @classmethod
    def name(cls, unit_name: str = "") -> str:
        return f"{cls.__name__}{unit_name}".lower()


PREFIXES = [Prefix.factory(name, multiplier) for name, multiplier in prefixes().items()]


# Kilograms are problematic for prefixes and need a few tweaks
class MassPrefix(Prefix):
    ADJUSTMENT = 1e-3

    def _to(self, value: float) -> float:
        return value * self.MULTIPLIER * self.ADJUSTMENT

    def _from(self, value: float) -> float:
        return value / self.MULTIPLIER / self.ADJUSTMENT

    @classmethod
    def name(cls, _="") -> str:
        return f"{cls.__name__}grams".lower()


MASS_PREFIXES = [
    MassPrefix.factory(name, multiplier)
    for name, multiplier in prefixes().items()
    if name != "kilo"
]


PUBLIC_PREFIXES = {"Prefix": PREFIXES, "MassPrefix": MASS_PREFIXES, "NoPrefix": []}
