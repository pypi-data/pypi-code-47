import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

class ObjectPypi(object):
    database = 'data/Novo.csv'
    model = None
    methods = {}
    def __init__(self, variaveis, model, target=None):
        self.variaveis = variaveis
        self.model = model
        self.target = target

    def __getstate__(self):
        return vars(self)

  
    def __setstate__(self, state):
        self.__dict__.update(state)


    def __getattr__(self, key):
        if key.startswith('__') and not key.endswith('__'):
            if key not in self.methods:
                raise NotImplementedError('Function {} not implemented'.format(key))
            return self.methods.get(key)
        return self.__dict__[key]
    

    def dump(self):
        with open('serasa_object.pickle', 'wb') as obj:
            pickle.dump(self, obj)

    def calc(self, dataframe):
        return self.model.predict(dataframe)

    def submit(self):
        if 'calc' not in self.methods:
            raise Exception('Por favor implemente o metodo calc')

    def colecao(self):
        dataframe = pd.read_csv(self.database)
        if self.target:
            return dataframe[self.target], dataframe[self.variaveis]
        return dataframe[self.variaveis]

    def transforma(self, dataframe):
        return dataframe

    def run(self):
        dataframe = self.colecao()
        dataframe = self.transforma(dataframe)
        return self.calc(dataframe)
 
    def register(self, func):
        func_name = func.__name__
      
        def start(*args, **kwargs):
            args = list(args)
            args.insert(0, self)
            return func(*args, **kwargs)
        self.methods[func_name] = start
        return start   

    def funcionaPypi():
        return 'Funciona com PyPi!!!'    

