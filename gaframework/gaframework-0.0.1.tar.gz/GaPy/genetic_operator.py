#! /usr/bin/python

from abc import ABC, abstractmethod
from typing import List, Set, Dict, Tuple, Optional
from GaPy.chromosome import Chromosome


class GeneticOperator(ABC):

    @abstractmethod
    def __init__(self, p: float = 1.0):

        self._p = p # probability, percentage etc
        self.enabled = True
        self.evaluation_count = 0

    @abstractmethod
    def invoke(self, population, fitness_function):
        pass

    def _evaluate(self, chromosomes:List[Chromosome], fitness_function):

        try:
            for chromosome in chromosomes:
                chromosome.fitness = fitness_function(chromosome)
                self.evaluation_count += 1

        except TypeError as ex:
            raise TypeError("Ensure the supplied fitness function accepts a single argument representing the chromosome to be evaluated.")
