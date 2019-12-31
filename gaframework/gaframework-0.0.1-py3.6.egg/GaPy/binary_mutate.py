#! /usr/bin/python

from GaPy.genetic_operator import *
from GaPy.chromosome import *


class BinaryMutate(GeneticOperator):

    def __init__(self, probability: float = 0.01):

        super().__init__(probability)

    def invoke(self, population, fitness_function):

        # TODO: consider an option (property) where the probability refers to a single
        #       randomly selected being mutated this should improve performance and
        #       could be the default option. Default probability value would need to be
        #       selected depending upon which option was selected

        if self.enabled:

            for c in population.chromosomes:
                self._mutate_chromosome(c)

    def _mutate_chromosome(self, chromosome):

        for i in range(len(chromosome)):
#        for g in chromosome.genes:
            p = random.random()
            if p < self._p:
                chromosome.genes[i] = self._mutate_gene(chromosome.genes[i])

    def _mutate_gene(self, gene):

        if isinstance(gene, bool):
            return not gene
        elif isinstance(gene, int) or isinstance(gene, float):
            return gene * -1
        else:
            # TODO: could check for a char of '1' or '0' so that binary (str) strings could be used
            raise TypeError("The gene is of the incorrect type. The type should be bool, float, int.")

