from collections import namedtuple
from functools import wraps
from itertools import combinations

import numpy as np

from .. import CONFIG

PhysicalReturn = namedtuple("PhysicalReturn", "v dual")


class CavCalcError(Exception):
    pass


def physical_return_dispatcher(dual=False):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            values = function(*args, **kwargs)
            return PhysicalReturn(values, dual)

        return wrapper

    return decorator


def form_args(*args):
    combs = list(combinations(args, 2))

    values = {}
    for (k1, v1), (k2, v2) in combs:
        if both_arraylike(v1, v2):
            v1, v2 = np.meshgrid(v1, v2)
            values[k1] = v1
            values[k2] = v2
        else:
            if k1 not in values:
                values[k1] = v1
            if k2 not in values:
                values[k2] = v2

    return values


def dummy_return(value):
    return value


def both_arraylike(x, y):
    return isinstance(x, np.ndarray) and isinstance(y, np.ndarray)


def save_result(result, filename):
    """Save an array of data to either a .npy file or txt file,
    depending upon `filename`."""
    if filename is None:
        return
    if filename.endswith(".npy"):
        np.save(filename, result)
    else:
        np.savetxt(filename, result)


def quit_print(msg, from_command_line=True):
    if from_command_line:
        print(msg)
        exit(-1)
    else:
        raise CavCalcError(msg)


def bug(msg, from_command_line):
    if "bug_reporting" in CONFIG and CONFIG["bug_reporting"].getboolean("report"):
        # TODO send an email with contents = msg
        pass

    quit_print(msg, from_command_line)
