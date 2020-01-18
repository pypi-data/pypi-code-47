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

It is also able to handle non-SI base units. The example below demonstrates the various
ways you can create and combine units by calculating the power, in watts, required for a car
to accelerate from 0 mph to 100 mph, in 5 seconds we use

>>> from sipy import Length, Time
>>> distance_to_travel = Length()
>>> distance_to_travel.miles = 100
>>> speed_of_car = distance_to_travel / Time(hours=1)
>>> mass_of_car = 1300 * kilogram
>>> power = 0.5 * mass_of_car * speed_of_car ** 2 / Time(seconds=5)
>>> round(power.watts)
259797

.. NOTE::
    To calculate the power required we determine the change in kinetic energy and divide
    it by the time taken, giving us this equation:
    .. math::
        \\displaystyle \\frac{ \\frac{1}{2} \\times mass \\times {velocity}^2} {time}


As `sipy` dynamically creates all it's quantities it's easy to add new units
todo link to a guide

As well as quantities, it comes packaged with a variety of physical constants
>>> from sipy import avogradro, boltzmann, planck
>>> avogradro
<InverseAmount 6.02E+23mol^-1>
>>> boltzmann
<InverseTemperatureMassLength2InverseTime2 1.38E-23K^-1kgm^2s^-2>
>>> planck
<MassLength2InverseTime 6.63E-34kgm^2s^-1>

todo
    * tune UNITS for perf
"""
# SIpy
from sipy.quantities import defined_quantities, generate_constants
from sipy.units import generate_units_from_quantities

__version__ = "0.3.1"


# Update project namespace to include all quantities, units and constants
_QUANTITIES = defined_quantities()
locals().update(_QUANTITIES)
locals().update(generate_units_from_quantities(_QUANTITIES))
locals().update(generate_constants())
