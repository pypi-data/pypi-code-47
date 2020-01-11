import pandas as pd

class Result:
   def __init__(self):
      #print("in Result()")
      self.status = None
      self.objective = None
      self.x = None
      self.xmatrix = None
      self.slack = None

   def __str__(self):
      result = \
         "   status: " + str(self.status) + "\n" + \
         "objective: " + str(self.objective) + "\n"
      if isinstance(self.x, pd.DataFrame):
         result += "x:" + "\n" + \
         self.x.to_string()
      elif isinstance(self.xmatrix, pd.DataFrame):
         result += "xmatrix:" + "\n" + \
         self.xmatrix.to_string()
      return result

   __repl__ = __str__
