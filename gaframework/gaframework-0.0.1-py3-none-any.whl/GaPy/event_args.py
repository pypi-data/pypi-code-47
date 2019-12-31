from GaPy.population import *
from typing import List, Set, Dict, Tuple, Optional


class GaEventArgs:

    def __init__(self, population: Population, generation_count: int, evaluation_count: int):

        self.population = population
        self.generation_count = generation_count
        self.evaluation_count = evaluation_count


class CrossoverEventArgs:

    def __init__(self, parents: List[Chromosome], children: List[Chromosome], points: List[int]):

        self.parents = parents
        self.children = children
        self.points = points
