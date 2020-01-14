# -*- coding: utf-8 -*-
"""This module contains everything that is related to InputFlags.
This module contains the InputFlag class and several flags such as Hidden and Optional.
"""

from typing import Any


class InputFlag:
    """This class represents a Flag that you can test.
    This is attached to a NodeInput and can allow a Node to detect special
    behaviour to apply on a given NodeInput.
    """

    def __init__(self, *flags: int):
        """NodeInput constructor

        Parameters
        ==========
        *flags: int
            Array of integers used to define an unique flag
        """
        self.flags = 0
        for flag in flags:
            self.flags = self.flags | flag
        self.underlying_type = None

    def __call__(self, underlying_type: Any) -> "InputFlag":
        """Special method __call__.
        Used to store a type inside the InputFlag.

        Parameters
        ==========
        underlying_type: Any
            Type you want to store in the InputFlag

        Returns
        =======
        InputFlag:
            Returns itself
        """
        self.underlying_type = underlying_type
        return self

    def __contains__(self, flag: "InputFlag") -> bool:
        """Checks whether an InputFlag contains one of the defined flags or not.
        You can you it like this :
        >>> SpecificFlag in my_flag

        Parameters
        ==========
        flag: InputFlag
            Flag you want to check if it is inside the current InputFlag

        Returns
        =======
        bool:
            True if the InputFlag contains the given flag, False otherwise
        """
        return (self.flags & flag.flags) != 0

    def __and__(self, flag: "InputFlag") -> "InputFlag":
        """Combines multiple InputFlags.
        After the combination of multiple InputFlags, the __contains__ method will
        return True for both flags

        Parameters
        ==========
        flag: InputFlag
            Flag you want to combine the current InputFlag with
        """
        return InputFlag(self.flags | flag.flags)


def create_input_flag() -> InputFlag:
    """Creates a new InputFlag and returns it.

    Returns
    =======
    InputFlag:
        The newly created InputFlag,
        the internal counter is multiplied by 2 everytime this function is called.
    """
    create_input_flag.counter *= 2
    return InputFlag(create_input_flag.counter)


create_input_flag.counter = 1
Hidden = create_input_flag()
Optional = create_input_flag()


def contains_flag(base: InputFlag, flag: InputFlag):
    return (
        isinstance(flag, InputFlag) and isinstance(base, InputFlag) and (flag in base)
    )
