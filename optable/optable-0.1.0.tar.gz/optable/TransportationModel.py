# Specify and solve a Transportation Model using a Pandas DataFrame

import pandas as pd
import LpModel

class TransportationModel:
   def __init__(self, df):
      self.df = df

   # convenience method to use pandas read_csv w/ good defaults
   @staticmethod
   def read_csv(filename):
      df = pd.read_csv(filename,
       sep=' ', skipinitialspace=True, index_col='name', comment='#')
      return df
   
   def solve(self):
      objdir = "min"
      c = self.getC()
      #print(c)
      A = self.getA()
      #print(A)
      sense = self.getSense()
      #print(sense)
      b = self.getRhs()
      #print(b)

      lpm = LpModel.LpModel(objdir, c, A, sense, b)
      result = lpm.solve()
      xmatrix = self.xToMatrix(result.x)
      #TODO - construct and return result as a DataFrame
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
      print(dfr)
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
   print(df.fillna(""))
   tranmodel = TransportationModel(df)
   result = tranmodel.solve()
   print(result.status)
   print(result.fun)
   print(result.x)
   print(result.xmatrix)
