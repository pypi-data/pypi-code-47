#! /usr/bin/python3

import math

from GaPy.genetic_operator import *
from GaPy.population import *
from GaPy.event import *
from GaPy.event_args import *
from GaPy.exceptions import *


class SinglePointCrossover(GeneticOperator):

    def __init__(self, probability: float = 0.85):

        super().__init__(probability)
        self.evaluations = 0
        self.parent_selection_method = ParentSelectionMethod.stochastic_universal_sampling
        self.replacement_method = ReplacementMethod.generational_replacement
        self.crossover_complete_event = Event()

    def invoke(self, population, fitness_function):

        p = random.random()

        if self.enabled and p <= self._p:

            # reset the number of evaluations
            self.evaluations = 0
            p_size = len(population)

            # the approach taken is to build a new list of chromosomes and
            # then attach these to the current population, start by taking any
            # existing elites
            # new_chromosomes = [c for c in population.chromosomes if c.elite]
            new_chromosomes = population.get_elites()

            # TODO: we could get all of the parents in one go and refactor the loop below
            # for two children we need 2 parents so parents required == children required
            # children_required = math.ceil((p_size - len(new_chromosomes)) / 2.0)
            # parents = population.select_parents(self.parent_selection_method, children_required)

            # create the correct number of children (population size - elites)
            for child_count in range(math.ceil((p_size - len(new_chromosomes)) / 2.0)):

                parents = population.select_parents(self.parent_selection_method)

                # can't assume that each chromosome is the same length
                parent_len_0 = len(parents[0])
                if parent_len_0 != len(parents[1]):
                    raise ParentMismatchError

                point = random.randint(0, parent_len_0 -1)
                children = self._crossover(parents, point)

                # crossover complete event
                args = CrossoverEventArgs(parents, children, [point])
                self.crossover_complete_event(args)

                # add them to the new chromosome list
                new_chromosomes.extend(children)

            if self.replacement_method == ReplacementMethod.generational_replacement:
                # Note that we are trimming the length as this is simpler than
                # testing for the population being full before adding each child in
                # the above loop. This could occur if we had an odd number of children
                # to create (e.g. 1 elite, 99 children needed)
                population.chromosomes = new_chromosomes[:p_size]

            elif self.replacement_method == ReplacementMethod.delete_last:

                raise NotImplementedError("This functionality has not been implemented yet.")

                # NOTE: that at this point the new population has not been evaluated

                # evaluate the children
                #self._evaluate(children, fitness_function)

                # get the minimum fitness of the current population
                #min_fitness = population.worst_chromosome().fitness

                # only add if they are better than the worst of the existing population
                #population.chromosomes += [c for c in new_chromosomes if c.fitness > min_fitness]

                # sort the chromosomes by fitness with highest first and trim to population size
                #population.chromosomes = sorted(population.chromosomes, key=lambda x: x.fitness, reverse=True)[:p_size]



    def _crossover(self, parents: List[Chromosome], point: int):

        # return a list with the children
        # TODO: use first, last type approach rather than indexing see Multiple Assignments
        return [Chromosome(parents[0].genes[:point] + parents[1].genes[point:]),
                Chromosome(parents[1].genes[:point] + parents[0].genes[point:])]

