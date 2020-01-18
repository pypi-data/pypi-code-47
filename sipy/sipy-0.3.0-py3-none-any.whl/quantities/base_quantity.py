# -*- coding: utf-8 -*-
# pylint: disable=R0401
"""The base class for physical quantities and associated factory.

This module implements `sipy.quantities.quantity.Quantity`, the base class
for all physical quantities implemented by SIpy. The
`sipy.quantities.quantity.quantity_factory` provides a method of generating
new quantity classes based on their SI units.

Example:
    The `Length` class could be generated with the following function call:

    >>> Length = quantity_factory(Counter(m=1))
    >>> print(Length())
    0.00E+00m
"""
# Standard Library
import operator
import typing
from collections import Counter
from copy import copy
from numbers import Number

# SIpy
from sipy.automap import UNIT_MAP
from sipy.definitions import quantity_string, unit_string


class Quantity:
    """Base class for all physical quantities.

    All new SIpy physical quantities should inherit from
    `sipy.quantities.quantity.Quantity`. Children should override the `UNITS`
    class attribute with a `collections.Counter` indicating the SI units of
    the quantity. The keys for `UNITS` are those defined in `sipy.definitions`.

    `sipy.quantities.quantity.Quantity` implements support for the standard
    mathematical operations that should work between physical quantities. It
    uses dimensional analysis to identify (and police) the operations
    allowed between different quantities as well as calculating the resulting
    quantities.

    Dimensional Analysis Rules:
        * Addition and subtraction is only allowed between quantities that have
        the same physical type. The result of the operation also has that type.
        * Multiplication and division works between quantities of different
        types and may produce a quantity of a different type.
        * Power operations are allowed if they result in a valid physical
        quantity.
        * Two quantities are equal if they have the same value ans are of the
        same type.
        * Quantities can be compared if they are of the same type.

    Attributes:
        UNITS: the SI units of the quantity, overridden by child classes.
        value: the value of the quantity expressed in SI units.
    """

    UNITS: typing.Counter[str] = Counter({})

    def __init__(self, **kwargs: str):
        """Create a quantity with a value of zero

        Args:
            **kwargs: an optional kwarg used to initialise the quantity with
                a non-zero value. The name of kwarg should correspond to
                a unit of measurement supported by the quantity. For instance

                >>> from sipy import Length
                >>> Length(kilometers=2.5)
                <Length 2.50E+03m>
        """
        self.value: float = 0
        if len(kwargs) > 1:
            raise TypeError(
                f"{self.__class__.__name__}.__init__() takes at most 1 keyword argument"
            )
        for unit, value in kwargs.items():
            if not hasattr(self, unit):
                raise AttributeError(
                    f"'{self.__class__.__name__}' has no attribute '{unit}'"
                )
            setattr(self, unit, value)

    def __add__(self, other: "Quantity") -> "Quantity":
        if not self._isinstance(other):
            raise TypeError(
                f"unsupported operand type(s) for +: "
                f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
            )
        val = self.__class__()
        val.value = self.value + other.value
        return val

    def __sub__(self, other: "Quantity") -> "Quantity":
        if not self._isinstance(other):
            raise TypeError(
                f"unsupported operand type(s) for -: "
                f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
            )
        val = self.__class__()
        val.value = self.value - other.value
        return val

    def __mul__(self, other: typing.Union["Quantity", float]) -> "Quantity":
        if not isinstance(other, Quantity):
            if not isinstance(other, Number):
                raise TypeError(
                    f"unsupported operand type(s) for *: "
                    f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
                )
            return self._number_mul(other)

        quantity = quantity_factory(add_counters(self.UNITS, other.UNITS))()
        quantity.value = self.value * other.value
        return quantity

    def __rmul__(self, other: float) -> "Quantity":
        if not isinstance(other, Number):
            raise TypeError(
                f"unsupported operand type(s) for *: "
                f"'{other.__class__.__name__}' and '{self.__class__.__name__}'"
            )

        return self._number_mul(other)

    def __truediv__(self, other: typing.Union["Quantity", float]) -> "Quantity":
        if not isinstance(other, Quantity):
            if not isinstance(other, Number):
                raise TypeError(
                    f"unsupported operand type(s) for /: "
                    f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
                )
            return self._number_truediv(other)

        quantity = quantity_factory(subtract_counters(self.UNITS, other.UNITS))()
        quantity.value = self.value / other.value
        return quantity

    def __rtruediv__(self, other: float) -> "Quantity":
        if not isinstance(other, Number):
            raise TypeError(
                f"unsupported operand type(s) for /: "
                f"'{other.__class__.__name__}' and '{self.__class__.__name__}'"
            )

        inverted_units = Counter({unit: -power for unit, power in self.UNITS.items()})
        quantity = quantity_factory(inverted_units)()
        quantity.value = other / self.value
        return quantity

    def __pow__(self, power: float) -> "Quantity":
        new_units = multiply_counter(self.UNITS, power)
        quantity = quantity_factory(new_units)()
        quantity.value = self.value ** power
        return quantity

    def __str__(self) -> str:
        return f"{self.value:.2E}{self.unit_string}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.value:.2E}{self.unit_string}>"

    def __eq__(self, other: object) -> bool:
        if not self._isinstance(other):
            return False
        return self.value == other.value  # type: ignore

    def __lt__(self, other: object) -> bool:
        if not self._isinstance(other):
            raise TypeError(
                f"'<' not supported between instances of "
                f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
            )
        return self.value < other.value  # type: ignore

    def _isinstance(self, other):
        """Determine if 2 Quantities are of the same type

        >>> from sipy import meters, seconds
        >>> seconds._isinstance(meters)
        False
        >>> seconds._isinstance(seconds)
        True
        """
        return self.__class__.__name__ == other.__class__.__name__

    @property
    def unit_string(self) -> str:
        """The human readable form of this quantities units, e.g. m^2.

        Returns: The qunatities units as a string.
        """
        return unit_string(self.UNITS)

    def _number_mul(self, number: float) -> "Quantity":
        """Scalar multiplication for the quantity."""
        val = self.__class__()
        val.value = self.value * number
        return val

    def _number_truediv(self, number: float) -> "Quantity":
        """Scalar division for the quantity."""
        val = self.__class__()
        val.value = self.value / number
        return val


def quantity_factory(units: Counter) -> typing.Type[Quantity]:
    """Construct a Quantity class based on the provided units

    >>> Q = quantity_factory(Counter({"m": 1}))
    >>> Q.__name__, Q.UNITS
    ('Length', Counter({'m': 1}))
    >>> d = Q()
    >>> d.kilometers = 1
    >>> d.meters, d.kilometers
    (1000.0, 1.0)

    Args:
        units: The dimensions of the quantity

    Returns:
        The corresponding quantity class
    """
    unit_combo = unit_string(units)
    name = quantity_string(units)
    quantity: typing.Type[Quantity] = type(name, (Quantity,), {})
    quantity.UNITS = units

    if unit_combo == "":
        return quantity

    for unit_name, unit in UNIT_MAP[unit_combo]:
        setattr(quantity, unit.name(unit_name), unit())

    return quantity


def add_counters(
    first: typing.Counter[str], second: typing.Counter[str]
) -> typing.Counter[str]:
    """Add together two `collection.Counter`.

    >>> add_counters(Counter(a=-2, b=3, c=4), Counter(a=5, d=1))
    Counter({'c': 4, 'a': 3, 'b': 3, 'd': 1})

    Args:
        first: The initial counter.
        second: The counter to add to the initial counter.

    Returns:
        The `collection.Counter` resulting from the addition
    """
    return _combine_counters(first, second, operator.add)


def subtract_counters(
    first: typing.Counter[str], second: typing.Counter[str]
) -> typing.Counter[str]:
    """Subtract two `collection.Counter`.

    >>> subtract_counters(Counter(a=-2, b=3, c=4), Counter(a=5, d=1))
    Counter({'c': 4, 'b': 3, 'd': -1, 'a': -7})

    Args:
        first: The initial counter.
        b: The counter to subtract from the initial counter.

    Returns:
        The `collection.Counter` resulting from the subtraction
    """
    return _combine_counters(first, second, operator.sub)


def _combine_counters(
    first: typing.Counter[str], second: typing.Counter[str], combiner: typing.Callable
) -> typing.Counter[str]:
    """Combine two counters using the specified operator"""
    tmp = copy(first)
    for item, value in second.items():
        tmp[item] = combiner(tmp[item], value)

    return tmp


def multiply_counter(
    counter: typing.Counter[str], factor: float
) -> typing.Counter[str]:
    """Scale a `collection.Counter` by a factor.

    >>> multiply_counter(Counter(a=-2, b=3), 2)
    Counter({'b': 6, 'a': -4})

    Args:
        counter: The initial counter.
        factor: The factor to scale counter by.

    Returns:
        The scaled `collection.Counter`

    Raises:
        ValueError: The values of the resulting counter
            are not whole numbers.
    """
    tmp_counter: typing.Dict[str, float] = {}
    for unit in counter:
        tmp_counter[unit] = counter[unit] * factor

    if any(v % 1 for v in tmp_counter.values()):
        raise ValueError(
            f"Quantity must have integer units: {unit_string(tmp_counter)}"
        )

    return Counter(tmp_counter)
