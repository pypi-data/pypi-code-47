# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import abc
import dataclasses
import enum


class Value:
    pass


class BooleanValue(Value, enum.Enum):
    """ We use a three valued logic to evaluate clock constraints given a DBM. """

    TRUE = True
    FALSE = False
    MAYBE = None

    @property
    def is_true(self) -> bool:
        return self is BooleanValue.TRUE

    @property
    def is_false(self) -> bool:
        return self is BooleanValue.FALSE

    @property
    def is_maybe(self) -> bool:
        return self is BooleanValue.MAYBE

    @property
    def is_maybe_true(self) -> bool:
        return self in {BooleanValue.TRUE, BooleanValue.MAYBE}

    @property
    def is_maybe_false(self) -> bool:
        return self in {BooleanValue.FALSE, BooleanValue.MAYBE}


class NumericValue(Value, abc.ABC):
    @property
    @abc.abstractmethod
    def as_real(self) -> RealValue:
        raise NotImplementedError()


@dataclasses.dataclass(frozen=True)
class IntegerValue(NumericValue):
    integer: int

    @property
    def as_real(self) -> RealValue:
        # TODO: emit some warning to keep track of imprecisions
        return RealValue(float(self.integer))


@dataclasses.dataclass(frozen=True)
class RealValue(NumericValue):
    real: float

    @property
    def as_real(self) -> RealValue:
        return self


@dataclasses.dataclass(frozen=True)
class ClockDifference(Value):
    pass
