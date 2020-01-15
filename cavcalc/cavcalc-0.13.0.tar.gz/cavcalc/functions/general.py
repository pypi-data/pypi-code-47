import numpy as np

from .. import constants
from ..parameter import Parameter
from ..utilities import form_args
from ..utilities.misc import physical_return_dispatcher


### Generic cavity properties


@physical_return_dispatcher()
def fsr(L):
    return 0.5 * constants.SPEED_OF_LIGHT / L


@physical_return_dispatcher()
def finesse(R1, R2):
    values = form_args(("R1", R1), ("R2", R2))
    R1 = values["R1"]
    R2 = values["R2"]

    return (
        0.5 * np.pi / np.arcsin(0.5 * (1 - np.sqrt(R1 * R2)) / np.power(R1 * R2, 0.25))
    )


@physical_return_dispatcher()
def fwhm(L, R1, R2):
    values = form_args(("L", L), ("R1", R1), ("R2", R2))
    L = values["L"]
    R1 = values["R1"]
    R2 = values["R2"]

    return fsr(L) / finesse(R1, R2)


@physical_return_dispatcher()
def pole(L, R1, R2):
    return 0.5 * fwhm(L, R1, R2)


FUNC_DEPENDENCIES_MAP = {
    fsr: ((Parameter.CAV_LENGTH,), Parameter.FSR,),
    finesse: (
        (Parameter.REFLECTIVITY_ITM, Parameter.REFLECTIVITY_ETM),
        Parameter.FINESSE,
    ),
    fwhm: (
        (Parameter.CAV_LENGTH, Parameter.REFLECTIVITY_ITM, Parameter.REFLECTIVITY_ETM),
        Parameter.FWHM,
    ),
    pole: (
        (Parameter.CAV_LENGTH, Parameter.REFLECTIVITY_ITM, Parameter.REFLECTIVITY_ETM),
        Parameter.POLE,
    ),
}
