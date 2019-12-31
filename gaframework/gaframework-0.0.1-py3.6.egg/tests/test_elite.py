from unittest import TestCase
from GaPy.chromosome import *
from GaPy.population import *
from GaPy.elite import *

class TestElite(TestCase):

    def test_invoke(self):

        chromosomes = []

        # create a popultation with chromosome fitness values = 0 to 100 all set to elite
        for f in range(100):
            c = Chromosome()
            c.fitness = f
            chromosomes.append(c)

        population = Population(chromosomes)

        elites = population.get_elites()

        self.assertEqual(0, len(elites))

        elite = Elite(10)
        elite.invoke(population, None)

        elites = population.get_elites()

        self.assertEqual(10, len(elites))
        self.assertEqual(99, elites[9].fitness)