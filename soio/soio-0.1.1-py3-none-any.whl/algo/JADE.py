'''
Differential Evolution Algorithm
@author: zzw
@reference: J. Zhang, A.C. Sanderson,
                    JADE: Adaptive Differential Evolution With Optional External Archive,
                    IEEE Transactions on Evolutionary Computation, 13 (2009) 945-958.


@log: 2020.1.3, create
'''

from soio.core.algorithm import Algorithm
from soio.core.solution import FloatSolution
from soio.core.problem import FloatProblem
import time
import random
from scipy.stats import cauchy
import numpy as np

class JADE(Algorithm):

    def __init__(self,
                 problem: FloatProblem,
                 max_nfes: int,
                 population_size: int = 30,
                 archive_size = 0,
                 p = 0.05, # [5%, 20%]
                 c = 0.1 #[1/20, 1/5]
                 ):

        self.problem = problem
        self.population_size = population_size
        self.max_iterations = int(max_nfes/population_size)
        self.archive_size = archive_size
        self.p = p
        self.c = c

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

        top_population = sorted(self.population, key=lambda x: x.objective)[:int(self.population_size*self.p)]
        archive = []
        mu_CR = 0.5
        mu_F = 0.5

        self.best_solution = top_population[0]
        self.records = []

        for iter in range(self.max_iterations):
            SCR = [] # successful crossover probabilities
            SF =[] # successful mutation factors
            for i in range(self.population_size):
                CR_i = random.normalvariate(mu_F, 0.1)
                F_i = cauchy.rvs(loc=mu_F, scale=0.1, size=1)[0]
                Xp_best = top_population[int(random.random()*len(top_population))]

                a = int(random.random()*self.population_size)
                while i==a:
                    a = int(random.random() * self.population_size)
                b = int(random.random() * (self.population_size+len(archive)))
                while i==b or a==b:
                    b = int(random.random() * self.population_size+len(archive))
                Xi = self.population[i]
                Xa = self.population[a]
                Xb = self.population[b] if b < self.population_size else archive[b-self.population_size]

                new_solution = FloatSolution(self.problem.number_of_variables)
                for j in range(self.problem.number_of_variables):
                    if random.random() < CR_i:
                        v = Xi.variables[j] + F_i * (Xp_best.variables[j] - Xi.variables[j]) + F_i*(Xa.variables[j] - Xb.variables[j])
                        #new_solution.variables[j] = min(max(v, self.problem.lower_bound[j]), self.problem.upper_bound[j])
                        if v < self.problem.lower_bound[j]:
                            v = (self.problem.lower_bound[j] + Xi.variables[j]) / 2
                        if v > self.problem.upper_bound[j]:
                            v = (self.problem.upper_bound[j] + Xi.variables[j]) / 2
                        new_solution.variables[j] = v
                    else:
                        new_solution.variables[j] = Xi.variables[j]
                rj = int(random.random()*self.problem.number_of_variables)
                v =Xi.variables[rj] + F_i * (Xp_best.variables[rj] - Xi.variables[rj]) + F_i*(Xa.variables[rj] - Xb.variables[rj])
                if v < self.problem.lower_bound[rj]:
                    v = (self.problem.lower_bound[rj] + Xi.variables[rj]) / 2
                if v > self.problem.upper_bound[rj]:
                    v = (self.problem.upper_bound[rj] + Xi.variables[rj]) / 2
                new_solution.variables[rj] = v
                self.problem.evaluate(new_solution)

                if new_solution.objective < self.population[i].objective:
                    if self.archive_size > 0:
                        if len(archive)<self.archive_size:
                            archive.append(self.population[i])
                        else:
                            archive[int(random.random()*self.archive_size)] = self.population[i]
                    self.population[i] = new_solution
                    SCR.append(CR_i)
                    SF.append(F_i)

            if len(SCR) > 0:
                mu_CR = (1-self.c)*mu_CR + self.c * np.mean(SCR)
                mu_F = (1-self.c) * mu_F + self.c * np.sum(np.power(SF,2)) / (np.sum(SF)+1E-10)

            top_population = sorted(self.population, key=lambda x: x.objective)[:int(self.population_size * self.p)]
            self.best_solution = top_population[0]
            self.records.append(self.best_solution.objective)

        self.total_computing_time = time.time() - start_computing_time

    def get_result(self):
        return self.best_solution

    def get_name(self) -> str:
        return 'JA Differential Evolution Algorithm'