# -*- coding: utf-8 -*-
"""This module contains everything that is related to types.
"""

import typing


class PineappleType:
    """This class represents a type with custom checks.
    When defining a custom type you can either herit from this class and
    reimplement PineappleType or use the <decorate> static method to transform a
    function into a PineappleType.
    """

    Types = {}

    def __init__(self):
        """Default PineappleType constructor
        """

    def check(self, value: typing.Any) -> bool:
        """Default PineappleType check method
        Unimplemented
        """
        raise NotImplementedError()

    def __call__(self, value: typing.Any) -> bool:
        return self.check(value)

    @staticmethod
    def decorate(function: typing.Callable) -> "PineappleType":
        """decorate static method.
        This static method is used when you want to transform a function into a Pineapple type.
        The function should take a
        <self: PineappleType> and
        <value: Any> parameter and return a boolean.
        Using @Pineapple.decorate on this function will dynamically
        create a new class that herits from
        PineappleType and use the function to replace the <check>
        method of PineappleType.

        Parameters
        ==========
        function: Callable
            Function you want to use as the <check> method for the new PineappleType

        Returns
        =======
        PineappleType:
            New class that herits from PineappleType
        """

        def new_type_repr(self):
            return function.__name__

        new_type = type(
            function.__name__,
            (PineappleType,),
            {"check": function, "__repr__": new_type_repr},
        )
        PineappleType.Types[function.__name__] = new_type
        return new_type


@PineappleType.decorate
def Any(self, value: typing.Any) -> bool:
    """This type will always work and does not depends on the value it has to check

    Returns
    =======
    bool:
        True, always
    """
    return True


class SumType(PineappleType):
    """This class represents a type that accepts multiple types
    """

    def __init__(self, *args: type):
        """SumType constructor

        Parameters
        ==========
        *args: type
            List of types that the SumType should accept
        """
        super().__init__()
        self.accepted_types = args

    def check(self, value: Any) -> bool:
        """Checks whether value's type is one of the
        accepted types

        Parameters
        ==========
        value: Any
            Value you want to check the type of

        Returns
        =======
        bool:
            True if the value's type is one of the accepted types, False otherwise
        """
        for accepted_type in self.accepted_types:
            if isinstance(value, accepted_type):
                return True
        return False

    def __repr__(self) -> str:
        return f"SumType({self.accepted_types})"


Numeric = SumType(int, float, complex)


class Nullable(PineappleType):
    def __init__(self, accepted_type: type):
        super().__init__()
        self.accepted_type = accepted_type

    def check(self, value: Any) -> bool:
        if isinstance(value, self.accepted_type) or value is None:
            return True
        return False

    def __repr__(self) -> str:
        return f"Nullable({self.accepted_type})"
