# Quadratic programming wrapper over scipy SLSQP optimizer
from scipy.optimize import minimize
import numpy as np

class QpModel:
    # constructor
    #  objdir is either min or max
    #  c is vector of linear objective function coef
    #  cqm is a vector of vectors of quadratic objective function coefs (lower diag)
    #  A is the constraint matrix (vector of vectors)
    #  sense is a vector of strings, each of =, <=, or >=
    #  b is the rhs vector
    #  x0 is an initial solution guess vector
    #  bounds is the upper and lower bounds of each variable, or None
    def __init__(self, objdir, c, cqm, A, sense, b, x0, bounds=None):
       #print("in QpModel")
       self.objdir = objdir
       self.c = c
       self.cqm = cqm
       self.A = A
       self.sense = sense
       self.b = b
       self.x0 = x0
       self.bounds = bounds
       self.check()

    # check a few values for validity
    def check(self):
        if self.objdir not in ('min', 'max'):
            raise ValueError("objdir must be either 'min' or 'max'")
        for sens in self.sense:
            if sens not in ['=', '<=', '>=']:
                raise ValueError("Each sense value must be =, <=, or >=")

    # build constraint data dynamically (for scipy)
    def buildConstraints(self):
        result = []
        for i in range(len(self.sense)):
            type = 'eq' if self.sense[i] == '=' else 'ineq' 
            con = {'type': type,
                    'fun': self.constraints,
                    'args': (i,)
                    }
            result.append(con)
        return result

    # return bounds from c'tor, or build (0,inf) bounds for each variable
    def buildBounds(self):
        if self.bounds != None: return self.bounds
        result = []
        for i in range(len(self.c)):
            result.append((0, np.inf))
        return result

    # set up problem and call scipy minimize to solve
    def solve(self):
        x0 = self.x0
        # build constraint data structure dynamically
        cons = self.buildConstraints()
        # build bounds dynamically
        bounds = self.buildBounds()
        result = minimize(self.objective, x0, constraints=cons, bounds=bounds, method='SLSQP')
        if self.objdir == 'max': result.fun *= -1.0
        return result

    # callback for objective
    def objective(self, x):
        #print("objective", x)
        result = 0.0
        # cumulate the linear terms
        for i in range(len(x)):
            result += self.c[i] * x[i]
        # calculate and add in the quadratic terms
        q = self.qobjective(x)
        result += q 
        if self.objdir == 'max': result *= -1 # flip sign for maximization
        return result

    # calculate the quadratic part of the objective
    def qobjective(self, x):
        result = 0.0
        c = self.cqm
        for j in range(len(c)):
            for i in range(j+1):
                #print(c[j][i], x[i], x[j])
                result += c[j][i] * x[i] * x[j]
        #print("q", result)
        return result

    # callback for constraints
    def constraints(self, x, *args):
        j = args[0]
        #print('constraint', j)
        a = self.A[j]
        result = 0.0
        for i in range(len(x)):
            result += a[i] * x[i]
        if self.sense[j] == '<=': #scipy constraints are >= by convention, flip sign for <= constraints
             result = self.b[j] - result
        else:
             result -= self.b[j]
        #print(result)
        return result

# TEST example
# TODO - consider soft-coded test driver
if __name__ == "__main__":
    c = [3, 2]
    cqm = [[1,0], [2,3]]
    A = [[1,1],[1,0],[0,1]]
    sense = ['=', '>=', '<=']
    b = [1, 0.2, 0.7]
    x0 = [.5, .5]
    qp = QpModel('max', c, cqm, A, sense, b, x0)
    result = qp.solve()
    print(result)
