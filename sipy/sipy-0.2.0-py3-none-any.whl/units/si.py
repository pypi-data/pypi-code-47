# -*- coding: utf-8 -*-


class SIBaseUnit:
    def __get__(self, instance, _) -> float:
        return self._from(instance.value)

    def __set__(self, instance, value: float):
        instance.value = self._to(value)

    def _to(self, value: float) -> float:
        return value

    def _from(self, value: float) -> float:
        return value

    @classmethod
    def name(cls, unit_name: str = "") -> str:
        return unit_name.lower()

    @classmethod
    def factory(cls, name: str, *args):
        raise NotImplementedError()


class DerivedSIUnit(SIBaseUnit):
    @classmethod
    def factory(cls, name: str, *args):
        return cls
