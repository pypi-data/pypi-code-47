from unittest import TestCase
from GaPy.population import *
from GaPy.single_point_crossover import *


def fitness(chromosome):
    return 0.5


def create_parents():
    # create the standard parents
    parents = Chromosome.create(16, 2)

    parents[0].genes = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    parents[1].genes = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]

    return parents


class TestSinglePointCrossover(TestCase):

    def test__crossover(self):
        parents = create_parents()

        # test crossover at point 2
        crossover = SinglePointCrossover()
        children = crossover._crossover(parents, 2)

        self.assertEqual("1100000011111111", str(children[0]))
        self.assertEqual("0011111100000000", str(children[1]))

        # test crossover at point 0
        crossover = SinglePointCrossover()
        children = crossover._crossover(parents, 0)

        self.assertEqual(str(parents[1]), str(children[0]))
        self.assertEqual(str(parents[0]), str(children[1]))

        # test crossover at point 16
        crossover = SinglePointCrossover()
        children = crossover._crossover(parents, 16)

        self.assertEqual(str(parents[0]), str(children[0]))
        self.assertEqual(str(parents[1]), str(children[1]))


