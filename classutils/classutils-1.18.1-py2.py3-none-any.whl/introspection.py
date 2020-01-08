# encoding: utf-8

import inspect


def caller(frame=2):
    """
    Returns the object that called the object that called this function.

    e.g. A calls B. B calls calling_object. calling object returns A.

    :param frame: 0 represents this function
                  1 represents the caller of this function (e.g. B)
                  2 (default) represents the caller of B
    :return: object reference
    """
    stack = inspect.stack()
    try:
        obj = stack[frame][0].f_locals[u'self']
    except KeyError:
        pass  # Not called from an object
    else:
        return obj
