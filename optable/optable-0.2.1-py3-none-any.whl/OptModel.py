# Specify and solve an LP using a Pandas DataFrame

import pandas as pd
if __name__ != "__main__":
   from . import LpModel
   from . import Result
else:
   from LpModel import LpModel
   from Result import Result

class OptModel:
   def __init__(self, df):
      #print("in OptModel()")
      self.df = df
      self.ismax = False

   def __str__(self):
      return self.df.fillna("").to_string()

   __repl__ = __str__

   # convenience method to use pandas read_csv w/ good defaults
   @staticmethod
   def read_csv(filename):
      df = pd.read_csv(filename,
            sep=' ', skipinitialspace=True, 
            index_col='name',
            comment='#')
      return df

   # convenience method to use pandas read_csv w/ string & good defaults
   @staticmethod
   def read_str(s):
      from io import StringIO
      df = pd.read_csv(StringIO(s),
       sep=' ', skipinitialspace=True, index_col='name', comment='#')
      return df

   # Add checks other than those in set up methods
   def check(self):
      #TODO - check for missing values
      #TODO - check for non-numeric values for c, A, b
      if not isinstance(self.df, pd.DataFrame):
         raise ValueError("Argument for OptModel must be a DataFrame")
      if 'sense' not in self.df.columns:
         raise AttributeError("DataFrame must have a 'sense' column")
      if 'rhs' not in self.df.columns:
         raise AttributeError("DataFrame must have a 'rhs' column")
      return
   
   def solve(self):
      self.check()

      objdir = self.getObjdir()
      #print(objdir)
      c = self.getC()
      #print(c)
      A = self.getA()
      #print(A)
      sense = self.getSense()
      #print(sense)
      b = self.getRhs()
      #print(b)

      lpm = LpModel(objdir, c, A, sense, b)
      res = lpm.solve()
      #print(res.slack)

      result = Result()
      result.status = res.status
      result.objective = res.fun
      if res.status == 0:
         result.x = pd.Series(res.x, self.getVarnames())
         result.slack = pd.Series(res.slack, self.getIneqNames())
      return result

   # determine if max or min
   def getObjdir(self):
      df = self.df
      row = df[(df.sense == 'min') | (df.sense == 'max')]
      if len(row) == 0: raise ValueError("min or max not specified for a row")
      if len(row) > 1: raise ValueError("multiple min or max found, only 1 may be specified")
      result = row.iloc[0].sense
      return result

   # get the A constraint matrix
   def getA(self):
      result = []
      df = self.df
      df2 = df[(df.sense == '<=') | (df.sense == '>=') | (df.sense == '=')]
      for index, row in df2.iterrows():
         rowvals = []
         for name, value in row.items():
            if name not in ['sense', 'rhs']:
               rowvals.append(value)
         result.append(rowvals)
      return result

   # extract the sense for all constraint rows
   def getSense(self):
      result = []
      for index, row in self.df.iterrows():
         if row.sense in ['<=', '>=', '=']:
            result.append(row.sense)
      return result

   # extract the rhs for all constraints
   def getRhs(self):
      result = []
      for index, row in self.df.iterrows():
         if row.sense in ['<=', '>=', '=']:
            result.append(row.rhs)
      return result

   # extract the objective function coefficients
   # TODO: err detect  0 or 2+ min/max rows found
   def getC(self):
      result = []
      df = self.df
      row = df[(df.sense == 'min') | (df.sense == 'max')]
      for name, values in row.iteritems():
         value = values[0]
         if name not in ['sense', 'rhs']:
            result.append(value)
      return result

   def getVarnames(self):
      result = []
      df = self.df
      for name in df.columns:
         if name not in ['sense', 'rhs']:
            result.append(name)
      return result

   def getIneqNames(self):
      df = self.df
      df2 = df[(df.sense == '<=') | (df.sense == '>=')]
      values = df2.index.values
      return list(values)

if __name__ == "__main__":
   df = OptModel.read_csv("lpmodel.txt")
   #print(df.fillna(""))
   lpmodel = OptModel(df)
   print(lpmodel)
   result = lpmodel.solve()
   #print(result.status)
   #print("x:\n" , result.x, sep='')
   print(result)
   print("slack:\n" , result.slack, sep='')

   df2 = OptModel.read_str(
"""
name   x1 x2  sense rhs
# objective:
obj     3  5    max
# subject to:
#x1lower 1  0    = 2
plant1  1  0    <=   4
plant2  0  2    <=  12
plant3  3  2    <=  18
""")
   lpmodel2 = OptModel(df2)
   print(lpmodel)
   result2 = lpmodel2.solve()
   print(result2)
