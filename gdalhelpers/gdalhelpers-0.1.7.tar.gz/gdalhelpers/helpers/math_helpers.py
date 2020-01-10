import math


# https://www.quora.com/How-does-one-correctly-compare-two-floats-in-Python-to-test-if-they-are-equal
def is_almost_equal(x: float, y: float, epsilon: float = 1 * 10 ** (-8)) -> bool:
    """
    Return True if two values are close in numeric value. By default close is withing 1*10^-8 of each other
    i.e. 0.00000001.

    Parameters
    ----------
    x, y : float
        Values to compare.

    epsilon : float, optional
        Value of closeness, small number. Default value is 1 * 10e-8.

    Returns
    -------
    bool
        `True` if the absolute difference between `x` and `y` is smaller then `epsilon`.

    """

    """Return True if two values are close in numeric value
    By default close is withing 1*10^-8 of each other
    i.e. 0.00000001"""

    return abs(x - y) <= epsilon


def distance(x1: float, y1: float,
             x2: float, y2: float) -> float:
    """
    Calculate distance from coordinates of two points.

    Parameters
    ----------
    x1, y1 : float
    x2, y2 : float

    Returns
    -------
    float
        Distance of points.
    """

    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))


def horizontal_angle(x1: float, y1: float,
                     x2: float, y2: float) -> float:
    """
    Calculate angle (direction) from coordinates of two points.

    Parameters
    ----------
    x1, y1 : float
    x2, y2 : float

    Returns
    -------
    float
        Angle orientation.

    """

    return math.atan2(y1 - y2, x1 - x2)
