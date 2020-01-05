import numpy as np
import math
from soio.core.problem import FloatProblem
from soio.core.solution import FloatSolution

class Ackley(FloatProblem):
    '''
    https://www.sfu.ca/~ssurjano/ackley.html
    Global minimum: f(X) = 0 at X = [0]D
    '''
    def __init__(self, D, a=20, b=0.2, c=2*math.pi):
        self.number_of_variables = D
        self.lower_bound = np.ones(D)*(-32.768)
        self.upper_bound = np.ones(D)*32.768
        self.a = a
        self.b = b
        self.c = c
        self.nfes = 0

    def get_name(self):
        return 'Ackley Function'

    def evaluate(self, solution: FloatSolution):
        self.nfes += 1
        solution.objective = self.compute(solution.variables)

    def compute(self, X: np.ndarray):
        return -self.a * math.exp(-self.b * math.sqrt(np.mean(np.square(X)))) \
               - math.exp(np.mean(np.cos(self.c * X))) + self.a + math.e

    def create_solution(self) -> FloatSolution:
        new_solution = FloatSolution(self.number_of_variables)
        new_solution.variables = np.random.uniform(self.lower_bound, self.upper_bound)
        return new_solution

