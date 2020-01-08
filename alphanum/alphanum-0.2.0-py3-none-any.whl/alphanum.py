try:
    import secrets as random
except ImportError:
    import random
import string

POP = string.ascii_letters + string.digits


def generate(length: int = 1) -> str:
    """Generates a random string of alphanumeric characters of the given length.
    If no length is specified, a single character is returned.

    On Python 3.5, this string is pseudo-randomly generated using
    :py:mod:`random`. With 3.6 and later, the randomness is generated with
    :py:mod:`secrets`, making the randomization cryptographically strong.

    Args:
        length (:obj:`int`, optional): Desired string length. Defaults to 1.

    Returns:
        str: A pseudo-random alphanumeric string.

    Examples:
        >>> print(alphanum.generate())
        'G'
        >>> print(alphanum.generate(10))
        'a93jfDjdA0'

    """
    return ''.join(random.SystemRandom().choice(POP) for i in range(length))
