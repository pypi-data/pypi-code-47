# An LP wrapper over scipy's linprog
# to convert an LP to scipy's LP cononical form
import numpy as np
from scipy.optimize import linprog

class LpModel:
   # record the parameters, convert to format for numpy.linprog
   def __init__(self, objdir, c, A, sense, b,
                method='simplex', bounds=(0, None)):
      # record the constructor arguments
      self.objdir = objdir
      self.c = c
      self.A = A
      self.sense = sense
      self.b = b
      self.method = method
      self.bounds = bounds

      self.check() # check parameters

      # generate inputs for the scipy call
      self._isMax = self.gen_isMax()
      self._c = self.gen_c()
      self._Aeq = self.gen_Aeq()
      self._beq = self.gen_beq()
      self._Aub = self.gen_Aub()
      self._bub = self.gen_bub()

   # solve the LP using scipy, return the scipy result
   def solve(self):
      if len(self._beq) > 0 and len(self._bub) > 0:
         result = linprog(self._c, method=self.method,
                       bounds=self.bounds,
                       A_eq=self._Aeq, b_eq=self._beq, 
                       A_ub=self._Aub, b_ub=self._bub)
      elif len(self._beq) > 0:
         result = linprog(self._c, method=self.method,
                       bounds=self.bounds,
                       A_eq=self._Aeq, b_eq=self._beq)
      elif len(self._bub) > 0:
         result = linprog(self._c, method=self.method,
                       bounds=self.bounds,
                       A_ub=self._Aub, b_ub=self._bub)
      else:
         raise ValueError("no constraints specified")
      # if needed adjust result for sign flips
      if self._isMax: result.fun *= -1
      return result

   # TODO - solveDual()

   # set boolean for isMax
   def gen_isMax(self):
      return self.objdir == 'max'

   # convert obj function to bp array, flip sign if needed
   def gen_c(self):
      result = np.array(self.c)
      if self._isMax:
         result *= -1
      return result

   # get and return equalty constraint coefficients
   def gen_Aeq(self):
      result = []
      A = self.A
      s = self.sense
      for j in range(len(A)):
         if s[j] == '=':
            result.append(np.array(A[j]))
      #print(result)
      return result

   # get and return inequality constraints
   def gen_Aub(self):
      result = []
      A = self.A
      s = self.sense
      for j in range(len(A)):
         if s[j] == '<=':
            result.append(np.array(A[j]))
         elif s[j] == '>=':
            result.append(np.array(A[j]) * -1)
      return result

   # get and return equality constraint rhs
   def gen_beq(self):
      result = []
      for i in range(len(self.b)):
         if self.sense[i] == '=':
            result.append(self.b[i])
      #print('beq', result)
      return np.array(result)

   # get and return inequality rhs
   def gen_bub(self):
      result = []
      for i in range(len(self.b)):
         if self.sense[i] == '<=':
            result.append(self.b[i])
         elif self.sense[i] == '>=':
            result.append(-self.b[i])
      return np.array(result)

   # check arguments are valid and consistent
   # some checks will be covered by scipy.linprog
   def check(self):
      if self.objdir not in ["min", "max"]:
         raise ValueError("objdir must be either min or max")
      try:
         len(self.b)
      except TypeError:
         raise TypeError("b must be a list of numbers")
      try:
         len(self.sense)
      except TypeError:
         raise TypeError("sense must be a list of strings")
      if len(self.b) != len(self.sense):
         raise ValueError("b and sense must be same length")
      #try:
      #   for s in self.sense:
      #      if s not in ["<=", ">=", "="]:
      #         raise ValueError('sense elements must be <=, >=, or =')
      #except:
      #   raise TypeError("sense must be a list of strings")

# test driver
if __name__ == "__main__":
   p_c = [3, 5]
   p_A = [[1,0],[0,2], [3,2], [1, 0]]
   p_sense = ['<=', '<=', '<=', '']
   p_b = [4, 12, 18, 3]
   lpm = LpModel("max", p_c, p_A, p_sense, p_b,
                 method='simplex', bounds=(0, None))
   #print(lpm._isMax, lpm._c, lpm._bub)
   #print(lpm._Aub)
   result = lpm.solve()
   print(result)
