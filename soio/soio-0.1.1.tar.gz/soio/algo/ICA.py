'''
Imperialist Competitive Algorithm
@author: zzw
@reference: Atashpaz-Gargari, E., & Lucas, C. (2007).
                    Imperialist competitive algorithm: An algorithm for optimization inspired by imperialistic competition.
                    2007 IEEE Congress on Evolutionary Computation.
                    doi:https://doi.org/10.1109/CEC.2007.4425083

@log: 2019.11.30, creation
'''
from soio.core.algorithm import Algorithm
from soio.core.solution import FloatSolution
from soio.core.problem import FloatProblem
import time
import numpy as np
import random
import math

class ImperialistCompetitiveAlgorithm(Algorithm):

    def __init__(self,
                 problem: FloatProblem,
                 population_size: int,
                 imperialists_size: int,
                 max_nfes: int):

        self.problem = problem
        self.population_size = population_size
        self.imperialists_size = imperialists_size
        self.colonies_size = population_size - imperialists_size
        self.max_infes = max_nfes

        self.beta = 2
        self.gamma = math.pi / 4
        self.epsilon = 0.1


        self.best_solution = FloatSolution(self.problem.number_of_variables)
        self.best_solution.objective = float("inf")

    def create_initial_countries(self):
        """ Creates the initial list of solutions of a metaheuristic. """
        return [self.problem.create_solution() for _ in range(self.population_size)]

    def evaluate(self, countries):
        """ Evaluates the countries. """
        for i in range(self.population_size):
            self.problem.evaluate(countries[i])
        return countries

    def run(self):
        """ Execute the algorithm. """
        start_computing_time = time.time()

        # create initial countries
        self.countries = self.create_initial_countries()
        self.evaluate(self.countries)

        # create initial empires
        self.countries.sort(key=lambda x: x.objective)
        self.best_solution = self.countries[0]
        self.records = []
        imperialists = self.countries[:self.imperialists_size]
        colonies = self.countries[self.imperialists_size:]
        max_imp_cost = imperialists[-1].objective
        normalized_imp_costs = np.array([max_imp_cost-s.objective for s in imperialists])
        imp_powers = normalized_imp_costs / np.sum(normalized_imp_costs)
        imp_colonies_size = [int(round(ip*self.colonies_size)) for ip in imp_powers]
        imp_colonies_size[0] += self.colonies_size - sum(imp_colonies_size)
        assert self.colonies_size == sum(imp_colonies_size), [self.colonies_size,sum(imp_colonies_size) ]
        random.shuffle(colonies)
        imp_colonies  = []
        counter = 0
        for  i in range(self.imperialists_size):
            imp_colonies.append(colonies[counter: counter + imp_colonies_size[i]])
            counter += imp_colonies_size[i]

        while True:
            if self.problem.nfes >= self.max_infes:
                break

            # assimilating: move the colonies toward their relevant imperialist
            for i in range(self.imperialists_size):
                for j in range(imp_colonies_size[i]):
                    colony = imp_colonies[i][j]
                    for k in range(self.problem.number_of_variables):
                        colony.variables[k] = colony.variables[k] + random.random() * self.beta * (imperialists[i].variables[k] - colony.variables[k])
                        colony.variables[k] = max(min(colony.variables[k], self.problem.upper_bound[k]), self.problem.lower_bound[k])
                    self.problem.evaluate(colony)
                    if colony.objective < imperialists[i].objective:
                        # swap colony and imperialist
                        imp_colonies[i][j] = imperialists[i]
                        imperialists[i] = colony

            for imp in imperialists:
                if imp.objective < self.best_solution.objective:
                    self.best_solution = imp

            self.records.append(self.best_solution.objective)

            if self.imperialists_size > 1:
                # imperialistic competition, eliminate the powerless empire
                imp_total_costs = [imperialists[i].objective + self.epsilon *
                                   sum([imp_colonies[i][j].objective for j in range(imp_colonies_size[i])])
                                   for i in range(self.imperialists_size)]
                weakest_imp = np.argmin(imp_total_costs)
                imp_total_costs.pop(weakest_imp)
                imp_colonies_size.pop(weakest_imp)
                new_colonies = imp_colonies.pop(weakest_imp) + [imperialists.pop(weakest_imp),]
                self.imperialists_size -= 1
                norm_imp_total_costs = np.array(imp_total_costs) - max(imp_total_costs)
                imp_powers = norm_imp_total_costs / (np.sum(norm_imp_total_costs) + 1e-9)
                total_power = np.sum(imp_powers)
                for colony in new_colonies:
                    # roulette wheel selection
                    r = random.random() * total_power
                    select_imp = -1
                    while r >0:
                        select_imp += 1
                        r -= imp_powers[select_imp]
                    imp_colonies[select_imp].append(colony)
                    imp_colonies_size[select_imp] += 1

        self.total_computing_time = time.time() - start_computing_time

    def get_result(self):
        return self.best_solution

    def get_name(self) -> str:
        return 'Imperialist Competitive Algorithm'

