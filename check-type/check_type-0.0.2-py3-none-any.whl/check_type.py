# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 12:14:40 2020
"""
import sys
import typeguard

from typing import Callable, get_type_hints

def check_input_type(func: Callable):
    """
    Runtime checking of types of the input arguments of ``func``.

    Parameters
    ----------
    func : Callable
        The function that you would like to have type checked.

    Examples
    --------
    1. Inside a class method

    .. code-block:: python

        import check_type
        class MyType:
            def __init__(self, data: int):
                check_type.check_input_type(self.__init__)
                self.data = data

        mt = MyType(3)

    2. Inside a funciton

    .. code-block:: python

        import check_type
        def func1(var: float):
            check_type.check_input_type(func1)
            print(var)
    """
    assert isinstance(func, Callable), "`func` must be a function."
    local_vars = sys._getframe(1).f_locals
    type_hints = get_type_hints(func)
    for var_name, expected_type in type_hints.items():
        if var_name == 'return':
            continue  # skip return type checking
        # END IF
        typeguard.check_type(var_name, local_vars[var_name], expected_type)
    # END FOR
