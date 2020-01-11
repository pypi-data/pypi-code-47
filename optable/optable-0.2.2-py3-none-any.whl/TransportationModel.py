# Specify and solve a Transportation Model using a Pandas DataFrame

import pandas as pd
if __name__ != "__main__":
   from . import LpModel
   from . import Result
else:
   from LpModel import LpModel
   from Result import Result

class TransportationModel:
   def __init__(self, df, objdir="min"):
      #print("in TransportationModel()")
      self.df = df
      self.objdir = objdir

   def __str__(self):
      return self.df.fillna("").to_string()

   __repl__ = __str__

   # convenience method to use pandas read_csv w/ good defaults
   @staticmethod
   def read_csv(filename):
      df = pd.read_csv(filename,
       sep=' ', skipinitialspace=True, index_col='name', comment='#')
      return df

   # convenience method to use pandas read_csv w/ string & good defaults
   @staticmethod
   def read_str(s):
      from io import StringIO
      df = pd.read_csv(StringIO(s),
       sep=' ', skipinitialspace=True, index_col='name', comment='#')
      return df
   
   def solve(self):
      c = self.getC()
      #print(c)
      A = self.getA()
      #print(A)
      sense = self.getSense()
      #print(sense)
      b = self.getRhs()
      #print(b)

      lpm = LpModel(self.objdir, c, A, sense, b)
      res = lpm.solve()

      # if non-optimal, return terse result
      if res.status != 0:
         result = Result()
         result.status = res.status
         return result
      # construct and return result as a DataFrame
      xmatrix = self.xToMatrix(res.x)
      dfr = pd.DataFrame(columns=self.df.columns)
      dfr.drop('supply', axis=1, inplace=True)
      for row in xmatrix:
         dfr.loc[len(dfr)] = row
      # TODO - more efficient/concise way to get index w/o 'demand'
      rownames = []
      for i in self.df.index:
         if i != 'demand':
            rownames.append(i)
      dfr.index = rownames
      # print(dfr)
      # construct Result
      result = Result()
      result.status = res.status
      result.objective = res.fun
      result.xmatrix = dfr
      return result

   # get the A constraint matrix
   def getA(self):
      result = []
      nrows, ncolumns = self.shape()
      # supply constraints
      for j in range(nrows):
         row = []
         for i in range(nrows):
            coef = 0
            if i == j: coef = 1
            block = [coef] * ncolumns
            row.extend(block)
         result.append(row)
      # TODO - demand constraints
      for j in range(ncolumns):
         row = []
         for i in range(nrows*ncolumns):
            coef = 0
            if (i % ncolumns) == j:
               coef = 1
            row.append(coef)
         result.append(row)

      return result

   # extract the sense for all constraint rows
   def getSense(self):
      result = []
      nrows, ncolumns = self.shape()
      s1 = nrows * ["<="] # supply
      s2 = ncolumns * ["="] # demand
      result.extend(s1)
      result.extend(s2)
      return result

   # extract the rhs for all constraints
   def getRhs(self):
      result = []
      df = self.df
      df2 = df.drop("demand", axis="rows")
      supply = df2.supply
      #print(supply.tolist())
      df3 = df.drop("supply", axis="columns")
      demand = df3.loc["demand"]
      #print(demandrow.tolist())
      result.extend(supply.tolist())
      result.extend(demand.tolist())
      return result

   # extract the objective function coefficients
   def getC(self):
      result = []
      df = self.df
      df2 = df.drop("supply", axis='columns')
      df3 = df2.drop("demand", axis='rows')
      for index, row in df3.iterrows():
         for value in row:
            result.append(value)
      return result

   def xToMatrix(self, x):
      result = []
      nrows, ncolumns = self.shape()
      k = 0
      for j in range(nrows):
         row = []
         for i in range(ncolumns):
            row.append(x[k])
            k += 1
         result.append(row)
      return result

   def shape(self):
      nrows, ncolumns = self.df.shape
      nrows -= 1
      ncolumns -= 1
      return (nrows, ncolumns)

if __name__ == "__main__":
   df = TransportationModel.read_csv("tranmodel.txt")
   #print(df.fillna(""))
   tranmodel = TransportationModel(df)
   print(tranmodel)
   result = tranmodel.solve()
   print(result)

   df2 = TransportationModel.read_str(
"""
   name  D1  D2  D3  D4  supply
   S1    464 513 654 867  75
   S2    352 416 690 791 125
   S3    995 682 388 685 100
   demand 80  65  70  85
""")
   print(df2)
   tranmodel2 = TransportationModel(df2, objdir="min")
   result2 = tranmodel2.solve()
   print(result2)