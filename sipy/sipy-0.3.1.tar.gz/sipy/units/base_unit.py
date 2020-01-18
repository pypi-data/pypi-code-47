# -*- coding: utf-8 -*-
"""The base class for an SI Unit

The `sipy.units.si.SIBaseUnit` implements the descriptor protocol.
When combined with a `sipy.quantities.quantity.Quantity` it is used
as an abstraction to a specific unit of that quantity. Every
`sipy.quantities.quantity.Quantity` has a `value` attribute that
stores the underlying value and the `sipy.units.si.SIBaseUnit` acts
as a wrapper around that.
>>> from sipy.quantities.base_quantity import Quantity
>>> q = Quantity
>>> q.unit = SIBaseUnit()
>>> quantity = q()
>>> quantity.unit = 1
>>> quantity.value
1
"""
# Standard Library
from typing import Type


class SIBaseUnit:
    def __get__(self, instance, _) -> float:
        """Implement the descriptor protocol"""
        return self._from(instance.value)

    def __set__(self, instance, value: float):
        """Implement the descriptor protocol"""
        instance.value = self._to(value)

    def _to(self, value: float) -> float:  # pylint: disable=R0201
        """Method that converts to the base value

        Expect this method to be overwritten by the base classes children
        """
        return value

    def _from(self, value: float) -> float:  # pylint: disable=R0201
        """Method that converts from the base value

        Expect this method to be overwritten by the base classes children
        """
        return value

    @classmethod
    def name(cls, unit_name: str = "") -> str:
        """The name of the unit

        It's expected that the name will be used as an attribute to access
        the unit on the `sipy.quantities.quantity.Quantity`

        Args:
            unit_name: The name of the fundamental unit, provided so that child
                classes can generate a modified name e.g. meter -> kilometer

        Returns: The modified name of the unit
        """
        return unit_name.lower()

    @classmethod
    def factory(cls, name: str, *args) -> Type["SIBaseUnit"]:
        """A factory method for generating new types of `sipy.units.si.SIBaseUnit`

        Args:
            name: The name of new `sipy.units.si.SIBaseUnit`
            *args: additional args used by child classes

        Returns:

        """
        raise NotImplementedError()


class DerivedSIUnit(SIBaseUnit):
    """A concrete implementation of the `sipy.units.si.SIBaseUnit` for SIUnits"""

    @classmethod
    def factory(cls, name: str, *args):
        return cls
