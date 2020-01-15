import random
import string

# Individual Constants
BINARIES_ENCODING = 'binaries'
DIGITS_ENCODING = 'digits'
BOOLEANS_ENCODING = 'booleans'
LETTERS_ENCODING = 'letters'
CUSTOM_ENCODING = 'custom'

# Population Constants
ASCENDING_ORDER = False
DESCENDING_ORDER = True

def create_binary_individual(long):
    genes = []
    i = 0
    while i < long:
        genes.append(str(random.randint(0, 1)))
        i += 1
    return genes


def create_individual_from_values(long, encoding):
    if encoding == BOOLEANS_ENCODING:
        values = ['True', 'False']

    if encoding == DIGITS_ENCODING:
        values = list(string.digits)

    if encoding == LETTERS_ENCODING:
        values = list(string.ascii_uppercase)

    genes = []
    i = 0
    while i < long:
        genes.append(random.choice(values))
        i += 1
    return genes


def create_individual_from_list(long, mylist):
    genes = []
    i = 0
    while i < long:
        genes.append(str(random.choice(mylist)))
        i += 1
    return genes


class Individual(object):
    def __init__(self, long=0, encoding=BINARIES_ENCODING, extra=[]):
        self.genes = []
        self.fitness = 0
        if long > 0:
            if encoding not in [BINARIES_ENCODING, DIGITS_ENCODING, BOOLEANS_ENCODING, LETTERS_ENCODING,
                                CUSTOM_ENCODING]:
                encoding = BINARIES_ENCODING

            if encoding == CUSTOM_ENCODING and len(extra) == 0:
                encoding = BINARIES_ENCODING

            if encoding == BINARIES_ENCODING:
                self.genes = create_binary_individual(long)

            if encoding in [BOOLEANS_ENCODING, DIGITS_ENCODING, LETTERS_ENCODING]:
                self.genes = create_individual_from_values(long, encoding)

            if encoding == CUSTOM_ENCODING:
                self.genes = create_individual_from_list(long, extra)

    def create_chromosome(self, long=0, encoding=BINARIES_ENCODING, extra=[]):
        genes = []
        if long > 0:
            if encoding not in [BINARIES_ENCODING, DIGITS_ENCODING, BOOLEANS_ENCODING, LETTERS_ENCODING,
                                CUSTOM_ENCODING]:
                encoding = BINARIES_ENCODING

            if encoding == CUSTOM_ENCODING and len(extra) == 0:
                encoding = BINARIES_ENCODING

            if encoding == BINARIES_ENCODING:
                self.genes = create_binary_individual(long)

            if encoding in [BOOLEANS_ENCODING, DIGITS_ENCODING, LETTERS_ENCODING]:
                self.genes = create_individual_from_values(long, encoding)

            if encoding == CUSTOM_ENCODING:
                self.genes = create_individual_from_list(long, extra)

        return genes

    def get_fitness(self):
        return self.fitness

    def get_genes(self):
        return self.genes

    def get_size(self):
        return self.genes.__len__()

    def __repr__(self):
        return repr(
            {
                'Individual': self.genes,
                'Fitness': self.fitness
            }
        )





class Population:
    def __init__(self, size=0, long=0, encoding=BINARIES_ENCODING, extra=[]):
        self.individuals = []
        self.populationSortOrder = DESCENDING_ORDER

        i = 0
        while i < size :
            self.individuals.append( Individual(long, encoding, extra) )
            i += 1

        self.individuals.sort(key=lambda x: x.get_fitness(), reverse=self.populationSortOrder)

    def get_all_individuals(self):
        return self.individuals

    def add_individual(self, individual):
        self.individuals.append(individual)
        self.individuals.sort(key=lambda x: x.get_fitness(), reverse=self.populationSortOrder)

    def display_population(self):
        print("--------------------------------------------------------------------")
        i = 0
        for x in self.get_all_individuals():
            print("Individual #",i," : ",x.get_genes()," | Fitness", x.get_fitness())
            i += 1
        print("--------------------------------------------------------------------")