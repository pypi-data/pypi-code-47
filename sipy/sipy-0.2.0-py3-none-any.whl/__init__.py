# -*- coding: utf-8 -*-
"""
`sipy` is a python package for manipulating physical quantities. All quantities in `sipy` are
constructed dynamically from their [SI base units](https://en.wikipedia.org/wiki/SI_base_unit) so
that `sipy` can use [dimensional analysis](https://en.wikipedia.org/wiki/Dimensional_analysis) to
spot errors in your calculations and learn all the valid units for a quantity.
>>> from sipy import meter, second
>>> meter
<Length 1.00E+00m>
>>> try:
...     meter + second
... except TypeError as exception:
...     print(exception)
unsupported operand type(s) for +: 'Length' and 'Time'
>>> distance = 1000 * meter
>>> distance.kilometers
1.0

It is also able to handle non-SI base units. The illustration below demonstrates the various
ways you can create and combine units by calculating the power, in watts, required for a car
to accelerate from 0 mph to 100 mph, in 5 seconds.
>>> from sipy import Length, Time
>>> distance_to_travel = Length()
>>> distance_to_travel.miles = 100
>>> speed_of_car = distance_to_travel / Time(hours=1)
>>> mass_of_car = 1300 * kilogram
>>> power = 0.5 * mass_of_car * speed_of_car ** 2 / Time(seconds=5)
>>> round(power.watts)
259797

As `sipy` dynamically creates all it's quantities it's easy to add new units
todo link to a guide

As well as quantities, it comes packaged with a variety of physical constants
>>> from sipy import constants
>>> constants.avogradro
<InverseAmount 6.02E+23mol^-1>
>>> constants.boltzmann
<InverseTemperatureMassLength2InverseTime2 1.38E-23K^-1kgm^2s^-2>
>>> constants.planck
<MassLength2InverseTime 6.63E-34kgm^2s^-1>

todo
    * headings: Installation, Usage, Features
    * installation
    * mention testing
    * add test tags
    * tune UNITS for perf
    * supported units in config
"""
# SIpy
from sipy.config import quantities
from sipy.quantities import quantity_factory

__version__ = "0.2.0"


def defined_quantities():
    my_quantities = {}
    for quantity in quantities():
        my_quantities[quantity.name] = quantity_factory(quantity.unit_counter)
    return my_quantities


locals().update(defined_quantities())


def defined_units():
    my_units = {}
    for quantity in quantities():
        for unit_name in quantity.unit_names:
            new_quantity = globals()[quantity.name]()
            new_quantity.value = 1
            my_units[unit_name] = new_quantity
    return my_units


locals().update(defined_units())
