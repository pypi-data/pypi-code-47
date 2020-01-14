from pineapple_core.core.node import node
from pineapple_core.core.types import Numeric

import math


@node(module="Math", name="Add", autotrigger=True)
def add_node(a: Numeric, b: Numeric) -> Numeric:
    return a + b


@node(module="Math", name="Subtract", autotrigger=True)
def subtract_node(a: Numeric, b: Numeric) -> Numeric:
    return a - b


@node(module="Math", name="Mutiply", autotrigger=True)
def multiply_node(a: Numeric, b: Numeric) -> Numeric:
    return a * b


@node(module="Math", name="Divide", autotrigger=True)
def divide_node(a: Numeric, b: Numeric) -> Numeric:
    return a / b


@node(module="Math", name="Cosinus", autotrigger=True)
def cosinus_node(a: Numeric) -> Numeric:
    return math.cos(a)


@node(module="Math", name="Sinus", autotrigger=True)
def sinus_node(a: Numeric) -> Numeric:
    return math.sin(a)


@node(module="Math", name="Tangent", autotrigger=True)
def tangent_node(a: Numeric) -> Numeric:
    return math.tan(a)


@node(module="Math", name="Ceil", autotrigger=True)
def ceil_node(a: Numeric) -> Numeric:
    return math.ceil(a)


@node(module="Math", name="Floor", autotrigger=True)
def floor_node(a: Numeric) -> Numeric:
    return math.floor(a)


@node(module="Math", name="CopySign", autotrigger=True)
def copysign_node(a: Numeric, b: Numeric) -> Numeric:
    return math.copysign(a, b)


@node(module="Math", name="Abs", autotrigger=True)
def abs_node(a: Numeric) -> Numeric:
    return abs(a)


@node(module="Math", name="Factorial", autotrigger=True)
def factorial_node(a: Numeric) -> Numeric:
    return math.factorial(a)


@node(module="Math", name="Modulo", autotrigger=True)
def modulo_node(a: Numeric, b: Numeric) -> Numeric:
    if isinstance(a, Numeric) and isinstance(b, Numeric):
        return a % b
    else:
        return math.fmod(a, b)


@node(module="Math", name="IsInfinite", autotrigger=True)
def is_infinite_node(a: Numeric) -> bool:
    return math.isinf(a)


@node(module="Math", name="Sum", autotrigger=True)
def sum_node(*numbers: Numeric) -> Numeric:
    result = math.fsum(numbers)
    if result == int(result):
        return int(result)
    else:
        return result


@node(module="Math", name="GCD", autotrigger=True)
def gcd_node(a: Numeric, b: Numeric) -> Numeric:
    return math.gcd(a, b)


@node(module="Math", name="Exp", autotrigger=True)
def exp_node(a: Numeric) -> Numeric:
    return math.exp(a)


@node(module="Math", name="Log", autotrigger=True)
def log_node(a: Numeric, base: Numeric) -> Numeric:
    return math.log(a, base)


@node(module="Math", name="Pow", autotrigger=True)
def pow_node(a: Numeric, b: Numeric) -> Numeric:
    return math.pow(a, b)


@node(module="Math", name="Sqrt", autotrigger=True)
def sqrt_node(a: Numeric) -> Numeric:
    return math.sqrt(a)
