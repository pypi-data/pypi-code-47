#! /usr/bin/python

import random


class Chromosome:

    def __init__(self, genes = []):

        self.genes = genes
        self.fitness = 0
        self.elite = False

    @staticmethod
    def create(chromosome_length: int, population_size: int = 1):

        #TODO: Is this the best way to seed the random object.
        random.seed()

        result = []

        for c in range(population_size):

            genes = []

            for i in range(chromosome_length):

                genes.append(bool(random.getrandbits(1)))

            result.append(Chromosome(genes))

        return result

    def evaluate(self, fitness_function):
        # note that a call to this method will evaluate irrespective of
        # the self.elite state this is by design
        self.fitness = fitness_function(self)

    def __str__(self):

        s = ''
        for gene in self.genes:
            if gene:
                s += '1'
            else:
                s += '0'

        # TODO: consider different gene types


        return s

    def __repr__(self):

        return self.__str__()

    def __len__(self):

        return len(self.genes)