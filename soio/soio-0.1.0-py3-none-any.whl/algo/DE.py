'''
Differential Evolution Algorithm
@author: zzw
@reference: R. Storn, K. Price,
                    Differential Evolution A Simple and Efficient Heuristic for global Optimization over Continuous Spaces,
                    Journal of Global Optimization, 11 (1997) 341-359.

@log: 2020.1.3, create
'''

from soio.core.algorithm import Algorithm
from soio.core.solution import FloatSolution
from soio.core.problem import FloatProblem
import time
import random
import copy

class DifferentialEvolution(Algorithm):

    def __init__(self,
                 problem: FloatProblem,
                 population_size: int,
                 max_nfes: int,
                 CR:float = 0.5, # [0,1] crossover rate
                 F: float = 0.1, #[0,2}
                 ):

        self.problem = problem
        self.population_size = population_size
        self.max_iterations = int(max_nfes/population_size)
        self.F = F
        self.CR = CR

        self.best_solution = FloatSolution(self.problem.number_of_variables)
        self.best_solution.objective = float("inf")

    def create_initial_population(self):
        return [self.problem.create_solution() for _ in range(self.population_size)]

    def run(self):
        """ Execute the algorithm. """
        start_computing_time = time.time()

        self.population = self.create_initial_population()
        for ind in self.population:
            self.problem.evaluate(ind)
            if ind.objective < self.best_solution.objective:
                self.best_solution = ind
        self.records = []

        for iter in range(self.max_iterations):
            for i in range(self.population_size):
                a = int(random.random()*self.population_size)
                while i==a:
                    a = int(random.random() * self.population_size)
                b = int(random.random() * self.population_size)
                while i==b or a==b:
                    b = int(random.random() * self.population_size)
                c = int(random.random() * self.population_size)
                while i==c or a==c or b==c:
                    c = int(random.random() * self.population_size)
                new_solution = FloatSolution(self.problem.number_of_variables)
                for j in range(self.problem.number_of_variables):
                    if random.random() < self.CR:
                        v = self.population[a].variables[j] + self.F * (self.population[b].variables[j] - self.population[c].variables[j])
                        new_solution.variables[j] = min(max(v, self.problem.lower_bound[j]), self.problem.upper_bound[j])
                    else:
                        new_solution.variables[j] = self.population[i].variables[j]
                rj = int(random.random()*self.problem.number_of_variables)
                new_solution.variables[rj] = self.population[a].variables[rj] + self.F * (self.population[b].variables[rj] - self.population[c].variables[rj])
                self.problem.evaluate(new_solution)

                if new_solution.objective < self.population[i].objective:
                    self.population[i] = new_solution
                    if new_solution.objective < self.best_solution.objective:
                        self.best_solution = new_solution

            self.records.append(self.best_solution.objective)

        self.total_computing_time = time.time() - start_computing_time

    def get_result(self):
        return self.best_solution

    def get_name(self) -> str:
        return 'Differential Evolution Algorithm'