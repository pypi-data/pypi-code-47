from soio.core.problem import FloatProblem
from soio.core.solution import FloatSolution
import matplotlib.pyplot as plt

class FuncProblem(FloatProblem):
    def __init__(self, func, n_varaibles, lower_bound, upper_bound):
        self.number_of_variables = n_varaibles
        self.nfes = 0
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.func = func

    def evaluate(self, solution: FloatSolution):
        solution.objective = self.func(solution.variables)
        self.nfes += 1
        return solution

def imp(func, Optimizer, opt_params, n_variables, lower_bound, upper_bound, plot= False):
    optimizer = Optimizer(
        problem=FuncProblem(func, n_variables, lower_bound, upper_bound),
        **opt_params
    )
    optimizer.run()
    optimal_solution = optimizer.get_result()
    if plot:
        plt.plot(optimizer.records)
        plt.show()
    return optimal_solution.variables, optimal_solution.objective