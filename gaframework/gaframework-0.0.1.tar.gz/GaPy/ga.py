#! /usr/bin/python

# TODO: Check the __str__ and __repr__ methods as well as __len__ and so on.
# TODO: Do we need to pass the fitness function to each Genetic Operator when it can be made available within the population
# TODO:   in the same way as parent selection is

from GaPy.single_point_crossover import *
from GaPy.binary_mutate import *
from GaPy.elite import *
from GaPy.event import *
from GaPy.event_args import *
from GaPy.exceptions import *


class Ga:

    def __init__(self, population: Population):

        self.population = population
        self._operators = []
        self.generation_complete_event = Event()
        self.initial_evaluation_complete_event = Event()
        self.operator_complete_event = Event()

    def append_operator(self, operator: GeneticOperator):

        # if type(operator) is not GeneticOperator:
        if not isinstance(operator, GeneticOperator):
            raise TypeError("Operators should be derived from the abstract base class GeneticOperator.")

        self._operators.append(operator)

    def run(self, fitness_function, terminate_function):

        # perform an initial evaluation
        evaluation_count = self._evaluate(fitness_function)

        #evaluation_count = len(self.population)  # account for the initial evaluation
        generation_count = 0

        # initial evaluation complete
        args = GaEventArgs(self.population, generation_count, evaluation_count)
        self.initial_evaluation_complete_event(args)

        # terminate funtion will be called with generation = 0, i.e before any operators have been applied
        while not terminate_function(self.population, generation_count, evaluation_count):

            # start a new generation
            generation_count += 1
            for operator in self._operators:

                operator.invoke(self.population, fitness_function)
                evaluation_count += operator.evaluation_count

                # operator complete event
                args = GaEventArgs(self.population, generation_count, evaluation_count)
                self.operator_complete_event(args)

            # evaluate what is now the next generation
            evaluation_count += self._evaluate(fitness_function)

            # generation complete event
            args = GaEventArgs(self.population, generation_count, evaluation_count)
            self.generation_complete_event(args)

    def _evaluate(self, fitness_function):

        """Evaluates the whole population."""
        evaluation_count = 0
        try:
            for chromosome in self.population.chromosomes:
                if not chromosome.elite:
                    chromosome.evaluate(fitness_function)
                    evaluation_count += 1

            return evaluation_count

        except TypeError as ex:
            raise TypeError(
                "Ensure the supplied fitness function accepts a single argument representing the chromosome to be evaluated.")

    # TODO: Check that these methods are appropriate and in the correct place
    @staticmethod
    def normalise_fitness(value: float, value_a: float, min_value=0):

        # normalises a value between 0.0 and 1.0
        #		public static double GetRangeConstant (double range, int numberOfBits)
        # {
        #	return range / (System.Math.Pow (2, numberOfBits) - 1);
        # }
        # return  (value - min_value) / (max_value - min_value);
        pass

    @staticmethod
    def get_range_constant(range_min: float, range_max: float, bits: int):

        if range_min >= range_max:
            raise BadRangeException("The value of 'range_value_high' must be greater than 'range_value_low'.")

        range = range_max - range_min
        return range / (pow(2, bits) - 1)

    @staticmethod
    def normalise_binary(binary_string_value: str, range_min: float = 1e-10, range_max: float = 1.0):

        # convert the bianry string to an integer, this is now in the range based on the number of bits
        value = int(binary_string_value, 2)

        # work out what the constant is to move the range to that specified in the 'range' argument
        range_constant = Ga.get_range_constant(range_min, range_max, len(binary_string_value))
        value *= range_constant

        # add any offset
        return value + range_min

    @staticmethod
    def clamp(n: float):
        """Clamps a value between 0.0. and 1.0"""
        return float(max(min(0, n), 1.0))

    @staticmethod
    def schaffer_f6_function(x, y):

        xsqrdysqrd = x*x + y*y

        # This is the Shaffer version taken from Johannes, M., Dieterich, Bernd Hartke (2012)
        #  which minimises to 0.0 with x and y = 0, this does return negative numbers sometimes
        #return 0.5 + (math.sin(math.sqrt(xsqrdysqrd))-0.5) / (1+0.001*xsqrdysqrd)**2

        # matlab f6plot1=0.5-((sin(sqrt(X.^2+Y.^2))).^2-0.5)./((1+0.001.*(X.^2+Y.^2)).^2);
        return 0.5 - ((math.sin(math.sqrt(xsqrdysqrd)))**2 - 0.5) / ((1.0 + 0.001*xsqrdysqrd)**2)

#        return 0.5 - (math.sin(math.sqrt(xsqrdysqrd))**2 / (1+0.001*(xsqrdysqrd)**2)

