import ipyparallel as ipp
import numpy as np

func = None

def run_parallel_legacy(f,data,args,indx):
    args = args[indx]
    model = f(data,args)
    return [model]

def run_parallel(f,model,data,args):
    args = args
    model = f(model,data,args)
    return [model]

class Parallel:
    
    def __init__(self, dview, data):
        
        mydict=dict(data=data)
        dview.push(mydict)
        
        self.grid = []
        self.models = []
        self.names = []
        
        self.dview = dview
        
    def add_model(self,model,grid,name):

        constructors = [model for _ in range(len(grid))]
        
        names = [name for _ in range(len(grid))]
        
        self.grid.extend(grid)
        self.models.extend(constructors)
        self.names.extend(names)
        
    def compute(self,run):
        
        args = self.grid
        
        self.dview['func'] = run
        
        arg_num = len(args)

        iters = np.arange(arg_num)
        
        func_ref, data_ref = map(lambda x:[x for _ in iters],
                              [ipp.Reference('func'),ipp.Reference('data')])
        
        models = self.dview.map_sync(run_parallel,
                                     func_ref,
                                     self.models,
                                     data_ref,
                                     args)
        return models
        
        
    def mapper(self, model, grid):
        
        args = grid
                
        mydict=dict(args=args)
        self.dview.push(mydict)
        
        self.dview['func'] = model
        
        arg_num = len(args)

        iters = np.arange(arg_num)
        
        func_ref, data_ref,args_ref = map(lambda x:[x for _ in iters],
                                      [ipp.Reference('func'), ipp.Reference('data'),ipp.Reference('args')])
    
         
        models = self.dview.map_sync(run_parallel_legacy,func_ref,data_ref,args_ref,iters)

        return models

