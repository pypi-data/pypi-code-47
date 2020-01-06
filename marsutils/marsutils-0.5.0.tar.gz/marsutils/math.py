import math


def signed_square(value):
    """ A tiny function that returns the square of ``value`` but with the
        same sign.

        >>> signed_square(-2)
        -4

        >>> signed_square(2)
        2
    """
    return math.copysign(value * value, value)


def two_way_clamp(lower, upper, value):
    # This function ensures the lower bound is less than the upper bound,
    # preventing easy to miss bugs
    """ A function that accepts a lower and upper bound and a value
        and will return the value if it is between the bounds, or it
        will return the clamped value.

        >>> two_way_clamp(100, 500, 250)
        250

        >>> two_way_clamp(100, 500, -40)
        100

        >>> two_way_clamp(-100, -500, 0)
        -100
    """
    if lower > upper:
        upper, lower = lower, upper
    return max(lower, min(upper, value))
