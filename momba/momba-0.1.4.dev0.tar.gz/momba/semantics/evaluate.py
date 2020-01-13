# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

import typing as t

import functools

from .. import model
from ..kit import dbm
from ..model import expressions, operators

from . import values

import dataclasses


@dataclasses.dataclass
class Result:
    """
    A result is a tuple comprising a value and an optional DBM. If the value
    is a `BooleanValue.MAYBE` the DBM, if present, describes for which clock
    valuations the expression is true. A DBM may not always be present if the
    result is MAYBE because DBMs are not closed under union and negation. We
    may want to use a mightier representation in the future.
    """

    value: values.Value

    clock_valuation: t.Optional[dbm.DBM] = None


class Environment:
    pass


@functools.singledispatch
def evaluate_expression(expr: model.Expression, env: Environment) -> Result:
    raise NotImplementedError(
        f"evaluation function for `{expr}` has not been implemented"
    )


@evaluate_expression.register
def _evaluate_boolean_constant(
    expr: expressions.BooleanConstant, env: Environment
) -> Result:
    return Result(values.BooleanValue(expr.boolean))


@evaluate_expression.register
def _evaluate_integer_constant(
    expr: expressions.IntegerConstant, env: Environment
) -> Result:
    return Result(values.IntegerValue(expr.integer))


@evaluate_expression.register
def _evaluate_real_constant(expr: expressions.RealConstant, env: Environment) -> Result:
    return Result(values.RealValue(expr.as_float))


def _combine_binary_and(left: Result, right: Result) -> Result:
    assert isinstance(left.value, values.BooleanValue) and isinstance(
        right.value, values.BooleanValue
    ), "the type system should ensure that both operands are booleans"
    if left.value.is_false:
        boolean_value = values.BooleanValue.FALSE
    elif left.value.is_maybe:
        if right.value.is_false:
            boolean_value = values.BooleanValue.FALSE
        boolean_value = values.BooleanValue.MAYBE
    else:
        assert left.value.is_true
        if right.value.is_false:
            boolean_value = values.BooleanValue.FALSE
        elif right.value.is_maybe:
            boolean_value = values.BooleanValue.MAYBE
        else:
            assert right.value.is_true
            boolean_value = values.BooleanValue.TRUE
    clock_valuation: t.Optional[dbm.DBM] = None
    if left.clock_valuation is not None and right.clock_valuation is not None:
        clock_valuation = dbm.intersect(left.clock_valuation, right.clock_valuation)
    return Result(boolean_value, clock_valuation=clock_valuation)


def _combine_binary_or(left: Result, right: Result) -> Result:
    assert isinstance(left.value, values.BooleanValue) and isinstance(
        right.value, values.BooleanValue
    ), "the type system should ensure that both operands are booleans"
    if left.value.is_true:
        boolean_value = values.BooleanValue.TRUE
    elif left.value.is_maybe:
        if right.value.is_true:
            boolean_value = values.BooleanValue.TRUE
        boolean_value = values.BooleanValue.MAYBE
    else:
        assert left.value.is_false
        if right.value.is_true:
            boolean_value = values.BooleanValue.TRUE
        elif right.value.is_maybe:
            boolean_value = values.BooleanValue.MAYBE
        else:
            assert right.value.is_false
            boolean_value = values.BooleanValue.FALSE
    # DBMs are not closed under union, hence, we omit the DBM information here
    return Result(boolean_value, clock_valuation=None)


Combinator = t.Callable[[Result, Result], Result]

_COMBINATORS: t.Mapping[operators.BinaryOperator, Combinator] = {
    operators.BooleanOperator.AND: _combine_binary_and,
    operators.BooleanOperator.OR: _combine_binary_or,
}


@evaluate_expression.register
def _evaluate_binary_expression(
    expr: expressions.BinaryExpression, env: Environment
) -> Result:
    left_result = evaluate_expression(expr.left)
    right_result = evaluate_expression(expr.right)
    return _COMBINATORS[expr.operator](left_result, right_result)
