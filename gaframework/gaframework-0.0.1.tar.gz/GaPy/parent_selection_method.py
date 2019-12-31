#! /usr/bin/python

from enum import Enum

# Parent Selection Method Enumerator
class ParentSelectionMethod(Enum):

    # This method is often referred to as Roulette Wheel selection The analogy to a roulette
    # wheel can be envisaged by imagining a roulette wheel in which each candidate solution
    # represents a section of the wheel. The size of the sections are proportionate to the
    # probability of selection of the solution. This means that fitter solutions are more
    # likely to be selected but all solutions have a chance.
    fitness_proportionate_selection = 0

    # Stochastic Universal Sampling is a development of fitness proportionate selection.
    # Where FPS chooses several solutions from the population by repeated random sampling,
    # Stochastic Universal Sampling uses a single random value to sample all of the solutions
    # by choosing them at evenly spaced intervals. This gives weaker members of the population
    # a better chance of being chosen.
    stochastic_universal_sampling = 1

    # Tournament selection involves executing several "tournaments" using individuals chosen
    # at random from the population. The winner of each tournament is selected.
    tournament_selection = 2
    random_selection = 3