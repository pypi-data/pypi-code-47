from enum import Enum


class OrderProjection(Enum):
    # EXECUTABLE and EXECUTION_COMPLETE orders
    ALL = 'NO_ROLLUP'

    # An order that has a remaining unmatched portion.
    # This is either a fully unmatched or partially matched bet (order)
    EXECUTABLE = 'EXECUTABLE'

    # An order that does not have any remaining unmatched portion.
    # This is a fully matched bet (order).
    EXECUTION_COMPLETE = 'EXECUTION_COMPLETE'
