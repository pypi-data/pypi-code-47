#! /usr/bin/python

from enum import Enum

# Determines how the population is updated
class ReplacementMethod(Enum):
        # New solutions (Children) are created from existing solutions
        # and a new population is created."""
        generational_replacement = 0,
        # Children created are used to replace the the weakest solutions
        # in the current population.
        delete_last = 1
