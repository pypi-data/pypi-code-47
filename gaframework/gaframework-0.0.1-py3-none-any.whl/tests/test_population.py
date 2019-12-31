from unittest import TestCase
from GaPy.population import *
from GaPy.exceptions import *


class TestPopulation(TestCase):

    def test__fps_selection(self):

        # create population
        chromosomes = Chromosome.create(16, 100)

        for chromosome in chromosomes:
            chromosome.fitness = random.random()

        population = Population(chromosomes)
        parents = population._fps_selection()

        self.assertEqual(2, len(parents))

    def test__fps_select(self):

        chromosomes = []

        # create a popultation with chromosome fitness values = 0 to 16
        for f in range(16):
            c = Chromosome()
            c.fitness = f
            chromosomes.append(c)

        population = Population(chromosomes)

        # test with 4.5 being the random number
        parent = population._fps_select(4.5)

        # the 4th chromosome should be selected as the first
        # three total 0 + 1 + 2 = 3 which is less than 4.5
        # the fitness of the fourth added to the previous is
        # greater than rand num, therefore this is selected
        self.assertEqual(3, parent.fitness)

    def test__sus_selection(self):

        # create population
        chromosomes = Chromosome.create(16, 100)

        for chromosome in chromosomes:
            chromosome.fitness = random.random()

        population = Population(chromosomes)
        parents = population._sus_selection()

        self.assertEqual(2, len(parents))

        parents = population._sus_selection(16)

        self.assertEqual(16, len(parents))

    def test__tour_selection(self):

        # create population
        chromosomes = Chromosome.create(16, 100)

        for chromosome in chromosomes:
            chromosome.fitness = random.random()

        population = Population(chromosomes)
        parents = population._tour_selection()

        self.assertEqual(2, len(parents))

    def test__random_selection(self):

        # create population
        chromosomes = Chromosome.create(16, 100)

        for chromosome in chromosomes:
            chromosome.fitness = random.random()

        population = Population(chromosomes)
        parents = population._random_selection()

        self.assertEqual(2, len(parents))

    def test_total_fitness(self):

        # create population
        chromosomes = Chromosome.create(16, 100)

        for chromosome in chromosomes:
            chromosome.fitness = 0.5

        population = Population(chromosomes)
        total_fitness = population.total_fitness()

        self.assertEqual(50.0, total_fitness)

    def test_get_elites(self):

        chromosomes = Chromosome.create(16,100)

        for i in range(5):
            elite = random.choice(chromosomes)
            elite.elite = True

        population = Population(chromosomes)
        elites = population.get_elites()

        self.assertEqual(5, len(elites))


    def test_worst_chromosome(self):

        chromosomes = []

        # create a popultation with chromosome fitness values = 0 to 16
        for f in range(16):
            c = Chromosome()
            c.fitness = f
            chromosomes.append(c)

        population = Population(chromosomes)
        best = population.worst_chromosome()

        self.assertEqual(0, best.fitness)


    def test_best_chromosome(self):

        chromosomes = []

        # create a popultation with chromosome fitness values = 0 to 16
        for f in range(16):
            c = Chromosome()
            c.fitness = f
            chromosomes.append(c)

        population = Population(chromosomes)
        best = population.best_chromosome()

        self.assertEqual(15, best.fitness)

    def test_test_top(self):

        chromosomes = []

        # create a popultation with chromosome fitness values = 0 to 16
        for f in range(16):
            c = Chromosome()
            c.fitness = f
            chromosomes.append(c)

        population = Population(chromosomes)
        top = population.top(4)

        self.assertEqual(15, top[0].fitness)
        self.assertEqual(14, top[1].fitness)
        self.assertEqual(13, top[2].fitness)
        self.assertEqual(12, top[3].fitness)
