"""
Module for checking variables. Most of the functions just checks if the variable passes logical tests.

There are several types of functions based on their names:

- check_* - These functions do not return anything just raise `Error` if the necessary conditions are not fulfilled.

- warn_* - These functions just print `Warning` based on condition.

- does/is_* - These functions return `True/False` if the conditions are met.

- check_return_* - These functions raise `Error` if the  necessary conditions are not fulfilled and `return` the value,
possibly modified or adjusted, back.
"""