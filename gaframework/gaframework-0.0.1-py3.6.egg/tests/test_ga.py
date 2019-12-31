from unittest import TestCase
from GaPy.ga import *

generations = 0
evaluations = 0


def display_event_details(args: GaEventArgs):
    global generations
    generations = args.generation_count

    global evaluations
    evaluations = args.evaluation_count

    best_chromosome = args.population.best_chromosome()
    # print("Generation: {0}, Evaluations: {1}, Max Fitness: {2}".format(args.generation_count,
    #                                                               args.evaluation_count,
    #                                                                   best_chromosome.fitness))


def terminate(population: Population, generation_count: int, evaluation_count: int):
    if generation_count == 100:
        return True


def fitness(chromosome: Chromosome):
    try:
        return 0.1

    except Exception as ex:
        raise FitnessError("An error has occurred within the fitness function: {0}".format(ex))


class TestGa(TestCase):

    def test_run(self):
        chromosomes = Chromosome.create(40, 100)
        population = Population(chromosomes)

        # crossover = SinglePointCrossover()

        ga = Ga(population)

        # ga.append_operator(crossover)
        ga.initial_evaluation_complete_event += display_event_details
        self.assertEqual(generations, 0)

        ga.generation_complete_event += display_event_details

        ga.run(fitness, terminate)

        self.assertEqual(100, generations)

    def test_get_range_constant(self):
        rc = Ga.get_range_constant(0, 100, 16)

        # try with max value
        val = 65535 * rc  # max val for 16 bits should be ranged to approximately 100
        self.assertTrue(val > 99.99 and val <= 100.0)

        # try with middle value
        val = 32767 * rc  # max val for 16 bits should be ranged to approximately 100
        self.assertTrue(val > 49.99 and val <= 50.01)

        # try with negative value
        rc = Ga.get_range_constant(-50, 50, 16)
        self.assertTrue(val > 49.99 and val <= 50.01)

    def test_normalise_binary(self):
        bval = "1111111111111111"  # 65535 in binary, max value for 16 bits

        # max value should equate to 100 with range set at 0 to 100
        val = Ga.normalise_binary(bval, 0.0, 100.0)
        self.assertTrue(val > 99.99 and val <= 100.0)

        # max value should equate to 50 with range set at -50 to +50
        val = Ga.normalise_binary(bval, -50.0, 50.0)
        self.assertTrue(val > 49.99 and val <= 50.01)

        bval = "0111111111111111"  # 32767 in binary, middle value for 16 bits

        # middle value should equate to 50 with range set at 0 to 100
        val = Ga.normalise_binary(bval, 0.0, 100.0)
        self.assertTrue(val > 49.99 and val <= 50.0)

        # middle value should equate to 0 with range set at -50 to +50
        val = Ga.normalise_binary(bval, -50.0, 50.0)
        self.assertTrue(val > -0.99 and val <= 0.01)

        # middle value should equate to 100 with range set at 50 to 150
        val = Ga.normalise_binary(bval, 50.0, 150.0)
        self.assertTrue(val > 99.99 and val <= 100.01)

    def test_schaffer_f6_function(self):

        file = open("f6.csv", "w")

        for x in range(-100,100):
            #for y in range(-100,100):
            y = 0
            z= Ga.schaffer_f6_function(x,y)
            file.write("{0},{1},{2}\r\n".format(x,y,z))

        file.close()

        x = 0.0
        y = 0.0

        r = Ga.schaffer_f6_function(x, y)

        self.assertEqual(1.0, r)

