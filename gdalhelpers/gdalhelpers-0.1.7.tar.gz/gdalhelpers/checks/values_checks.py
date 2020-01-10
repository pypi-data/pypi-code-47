from typing import Union
import math
from angles import normalize


def check_number(variable: Union[int, float], variable_name: str) -> None:
    """
    Checks if `variable` is valid is either `int` or `float`. Raises `TypeError` if it is not.

    Parameters
    ----------
    variable : int or float
        Variable to check.

    variable_name : str
        Variable name for error message.

    Returns
    -------
    None

    Raises
    ------
    TypeError
        If `variable` is not `numbers.Number`.
    """

    if not isinstance(variable, (float, int)):
        raise TypeError("`{0}` must be either `int` or `float`. "
                        "The variable is: `{1}`.".format(variable_name, type(variable).__name__))


def check_value_is_zero_or_positive(variable: Union[int, float], variable_name: str) -> None:
    """
    Checks if `variable` is equal or higher than zero. Raises `TypeError` if it is not.

    Parameters
    ----------
    variable : numbers.Number
        Variable to check.

    variable_name : str
        Variable name for error message.

    Returns
    -------
    None

    Raises
    ------
    TypeError
        If `variable` is not number equal or higher than 0.
    """

    check_number(variable, variable_name)

    if variable < 0:
        raise ValueError("`{0}` must be higher than 0. It is `{1}`.".format(variable_name, variable))


def check_return_value_is_angle(theta: Union[int, float], variable_name: str) -> float:
    """
    Checks if `theta` is number and normalizes it into range `[-pi, pi]`.
    Values outside of the range are transformed into the range.

    Parameters
    ----------
    theta : numbers.Number
        Represents angle in radians.

    variable_name : str
        Variable name for error message.

    Returns
    -------
    float
        Value of `theta` normalized into range [-pi, pi].

    """

    check_number(theta, variable_name)

    if not (-math.pi <= theta <= math.pi):
        theta = normalize(theta, -math.pi, math.pi)

    if not (-math.pi <= theta <= math.pi):
        raise ValueError("{0} must be from range `[-pi, pi]`. It is {1}.".format(variable_name, theta))

    return float(theta)


def check_return_value_is_angle_degrees(theta: Union[int, float], variable_name: str) -> float:
    """
    Checks if `theta` is number and normalizes it into range `[0, 360]`.
    Values outside of the range are transformed into the range.

    Parameters
    ----------
    theta : numbers.Number
        Represents angle in degrees.

    variable_name : str
        Variable name for error message.

    Returns
    -------
    float
        Value of `theta` normalized into range [0, 360].

    """

    check_number(theta, variable_name)

    if not (0 <= theta <= 360):
        theta = normalize(theta, 0, 360)

    return float(theta)
