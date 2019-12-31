#! /usr/bin/python

from typing import List, Set, Dict, Tuple, Optional
from GaPy.chromosome import *
from GaPy.population import *
from enum import Enum
from operator import attrgetter
from GaPy.parent_selection_method import *
from GaPy.replacement_method import *


class Population:

    def __init__(self, chromosomes: List[Chromosome]):

        self.chromosomes = chromosomes

    def select_parents(self, parent_selection_method: ParentSelectionMethod = ParentSelectionMethod.stochastic_universal_sampling, n: int = 2):

        if parent_selection_method == ParentSelectionMethod.fitness_proportionate_selection:
            return self._fps_selection(n)

        elif parent_selection_method == ParentSelectionMethod.stochastic_universal_sampling:
            return self._sus_selection(n)

        elif parent_selection_method == ParentSelectionMethod.tournament_selection:
            return self._tour_selection(n)

        elif parent_selection_method == ParentSelectionMethod.random_selection:
            return self._random_selection(n)

    def get_elites(self):

        return [c for c in self.chromosomes if c.elite]

    def clear_elites(self):

        for c in self.chromosomes:
            c.elite = False

    def _fps_selection(self, n: int = 2):

        # Roulette Wheel
        # (Davis, 1992, P.14-15
        #
        # sum the fitness of all the population (TotalFitness)
        # generate n (random between 0 and total fitness
        # return the first population member whose fitness
        # added to the fitness of the precedeing population
        # members is greater or equal to n.

        # TODO: Consider Normlised Fitness...
        total_fitness = sum([o.fitness for o in self.chromosomes])
        parents = []

        i = 0

        while i < n:
            parents.append(self._fps_select(random.uniform(0.0, total_fitness)))
            i += 1

        return parents

    def _fps_select(self, rand_num: float):

        # Separated from above in order to unit test
        running_total = 0.0

        for chromosome in self.chromosomes:

            running_total += chromosome.fitness
            if running_total >= rand_num:
                return chromosome

        return None


    def _sus_selection(self, n: int  = 2):

        raise NotImplementedError("This functionality has not been implemented yet.")

        # TODO: Consider Normlised Fitness...
        total_fitness = self.total_fitness()
        parents = []

        # get the distance between pointers
        point_distance = total_fitness / n;
        starting_point = random.random() * point_distance;

        pointers = []

        for i in range(n):
            pointers.append(starting_point + (i * point_distance))

        # now the roulette part
        index = 0
        fitness = 0.0
        for point in pointers:

            selected = False

            while not selected:
                fitness += self.chromosomes[index].fitness
                if fitness < point:
                    index += 1
                else:
                    parents.append(self.chromosomes[index])
                    break

        return parents

    def _tour_selection(self, n: int = 2):

        raise NotImplementedError("This functionality has not been implemented yet.")

        parents = []
        max_iterations = 16
        tour = []

        # TODO: consider returning all parents in one call to this method otherwise
        # evaluating pop size here could be expensive.
        population_size = len(self.chromosomes)

        for i in range(n):

            tour_size = random.randint(1, population_size)
            tour = self._sus_selection(tour_size + 1)

            # add the best of the tour to the parents list
            parents.append(max(tour, key=attrgetter('fitness')))

        return parents

    def _random_selection(self):

        return random.choices,(self.chromosomes, None, None)

    def total_fitness(self):
        """
        Reurns the sum of the fitness value of each chromosome in the population.
        :return:
        """
        #TODO: Consider Normlised Fitness...
        return sum([o.fitness for o in self.chromosomes])

    def worst_chromosome(self):
        """
        Returns the chromosome with the lowest fitness value.
        """
        return min(self.chromosomes, key=attrgetter('fitness'))

    def best_chromosome(self):
        """
        Returns the chromosome with the highest fitness value.
        """
        return max(self.chromosomes, key=attrgetter('fitness'))

    def top(self, n: int):
        """
        Returns the top n chromosomes sorted in reverse order
        :param n:
        :return:
        """
        return sorted(self.chromosomes, key=lambda x: x.fitness, reverse=True)[:n]

    def __str__(self):

        s = ""
        for chromosome in self.chromosomes:
            s += str(chromosome) + "\r\n"
        return s

    def __repr__(self):

        return self.__str__()

    def __len__(self):

        return len(self.chromosomes)