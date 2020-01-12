# -*- coding: utf-8 -*-
# Standard Library
import typing
from collections import Counter

# SI base units
SECONDS = "s"
METERS = "m"
KILOGRAMS = "kg"
AMPERES = "A"
KELVINS = "K"
MOLES = "mol"
CANDELAS = "cd"

# SI base quantities
TIME = "Time"
LENGTH = "Length"
MASS = "Mass"
CURRENT = "Current"
TEMPERATURE = "Temperature"
AMOUNT = "Amount"
LUMINOSITY = "Luminosity"

# Mapping SI base units to SI base qunatities
UNIT_QUANTITY = {
    SECONDS: TIME,
    METERS: LENGTH,
    KILOGRAMS: MASS,
    AMPERES: CURRENT,
    KELVINS: TEMPERATURE,
    MOLES: AMOUNT,
    CANDELAS: LUMINOSITY,
}

# SI base units mapped to their full names
UNIT_NAME = {
    SECONDS: "seconds",
    METERS: "meters",
    KILOGRAMS: "kilograms",
    AMPERES: "amperes",
    KELVINS: "kelvins",
    MOLES: "moles",
    CANDELAS: "candelas",
}

SCALAR = "Scalar"
INVERSE = "Inverse"


def unit_counter(
    seconds: int = 0,
    meters: int = 0,
    kilograms: int = 0,
    amperes: int = 0,
    kelvins: int = 0,
    moles: int = 0,
    candelas: int = 0,
) -> typing.Counter[str]:
    return Counter(
        {
            SECONDS: seconds,
            METERS: meters,
            KILOGRAMS: kilograms,
            AMPERES: amperes,
            KELVINS: kelvins,
            MOLES: moles,
            CANDELAS: candelas,
        }
    )


def unit_string(
    units: typing.Union[typing.Counter[str], typing.Dict[str, float]]
) -> str:
    """Construct a string from a units counter

    :param units: The unit count
    :return: A string representing the units

    >>> unit_string(Counter({"a": 1, "b": 0, "c": 0}))
    'a'
    >>> unit_string(Counter({"a": 0, "b": 1, "c": 0}))
    'b'
    >>> unit_string(Counter({"a": 2, "b": 0, "c": 0}))
    'a^2'
    >>> unit_string(Counter({"a": -1, "b": 0, "c": 0}))
    'a^-1'
    >>> unit_string(Counter({"a": 1, "b": 2, "c": 0}))
    'ab^2'
    """
    string = ""
    for unit, power in sorted(units.items()):
        if power == 1:
            string += unit
        elif power != 0:
            string += f"{unit}^{power}"
    return string


def unit_counter_from_string(unit_string: str):
    """

    Args:
        unit_string:

    Returns:

    >>> unit_counter_from_string("m")
    Counter({'m': 1, 's': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0})
    >>> unit_counter_from_string("m^2")
    Counter({'m': 2, 's': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0})
    >>> unit_counter_from_string("m^-1")
    Counter({'s': 0, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0, 'm': -1})
    >>> unit_counter_from_string("m.s")
    Counter({'s': 1, 'm': 1, 'kg': 0, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0})
    >>> unit_counter_from_string("kg.m^2.s^-2")
    Counter({'m': 2, 'kg': 1, 'A': 0, 'K': 0, 'mol': 0, 'cd': 0, 's': -2})
    """
    units = unit_string.split(".")
    counter_dict = {}
    for unit in sorted(units):
        unit_info = unit.split("^")
        if len(unit_info) == 1:
            count = "1"
            (unit_char,) = unit_info
        else:
            unit_char, count = unit_info
        counter_dict[UNIT_NAME[unit_char]] = int(count)

    return unit_counter(**counter_dict)


def unit_reference(units: typing.Counter[str]) -> str:
    """Construct a name that can be used to reference a unit

    :param units: The unit count
    :return: A string representing the refernce

    >>> unit_reference(unit_counter(seconds=1))
    'seconds'
    >>> unit_reference(unit_counter(meters=2))
    'meters2'
    >>> unit_reference(unit_counter(kilograms=-1))
    'perkilogram'
    >>> unit_reference(unit_counter(meters=1, seconds=-1))
    'meterspersecond'
    >>> unit_reference(unit_counter(meters=-1, seconds=1))
    'secondspermeter'
    >>> unit_reference(unit_counter(seconds=-2, meters=1, kilograms=2))
    'kilograms2meterspersecond2'
    >>> unit_reference(unit_counter(seconds=-2, meters=-1, kilograms=2))
    'kilograms2permeterpersecond2'
    >>> unit_reference(unit_counter())
    Traceback (most recent call last):
    ...
    ValueError: Count cannot be all zeros
    """
    if all(value == 0 for value in units.values()):
        raise ValueError("Count cannot be all zeros")

    start = end = ""
    # Sort based on unit, i.e. A, K, cd, kg, m, mol, s
    for unit, count in sorted(units.items()):
        if count != 0:
            quantity_name = UNIT_NAME[unit]

            if count == 1:
                start += f"{quantity_name}"
            elif count == -1:
                end += f"per{quantity_name[:-1]}"
            elif count > 1:
                start += f"{quantity_name}{count}"
            else:
                end += f"per{quantity_name[:-1]}{-count}"

    return start + end


def quantity_string(units: typing.Counter[str]) -> str:
    """Determine a quantity name from it's units

    :param units: The units of the class
    :return: The name of the class

    >>> quantity_string(unit_counter(seconds=1))
    'Time'
    >>> quantity_string(unit_counter(meters=2))
    'Length2'
    >>> quantity_string(unit_counter(kilograms=-1))
    'InverseMass'
    >>> quantity_string(unit_counter(meters=1, seconds=-1))
    'LengthInverseTime'
    >>> quantity_string(unit_counter(seconds=-2, meters=1, kilograms=2))
    'Mass2LengthInverseTime2'
    """
    name = ""

    # Sort based on unit, i.e. A, K, cd, kg, m, mol, s
    for unit, count in sorted(units.items()):
        if count != 0:
            quantity = UNIT_QUANTITY[unit]
            if count < 0:
                name += INVERSE
                count = -count

            if count == 1:
                name += f"{quantity}"
            else:
                name += f"{quantity}{count}"

    return name if name else SCALAR
