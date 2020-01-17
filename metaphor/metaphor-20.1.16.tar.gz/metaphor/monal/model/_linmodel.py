#-*- coding: ISO-8859-15 -*-
#===============================================================================
# $Id: _linmodel.py 4819 2018-11-02 05:32:25Z jeanluc $
#  Module  _linmodel
#  Projet MonalPy
# 
#  Implementation python de monal
#
#  Author: Jean-Luc PLOIX  -  NETRAL
#  Decembre 2009
#
# Copyright 2016 Jean-Luc PLOIX
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================
'''
'''

from numpy import matrix, copy, zeros
from ..Property import Property
from ._model import Model
from ..monalconst import ID_COMPUTE
from ..util.monaltoolbox import register

class LinearModel(Model):
    
    def __init__(self, owner=None, name=""):
        super(Model, self).__init__(owner, name)
        self._inputs = None
        self._outputs = None

    def _setNames(self, inNames=None, outNames=None):
        if inNames: 
            self._inputnames = [name for name in inNames]
        else:
            self._inputnames = ["IN_%d"% i for i in range(self.inputCount)]
        if outNames: 
            self._outputnames = [name for name in outNames]
        else:
            self._outputnames = ["OUT_%d"% i for i in range(self.outputCount)]            
    
    def container(self):
        return self.owner
    
    @Property
    def inputs(self, index):
        return self._inputs[index]
    @inputs.setter
    def inputs(self, index, value):
        self._inputs[index] = value
    @inputs.lengetter
    def inputs(self):
        return self.inputCount
    
    @Property
    def outputs(self, index):
        return self._outputs[index]
    @outputs.setter
    def outputs(self, index, value):
        self._outputs[index] = value
    @outputs.lengetter
    def outputs(self):
        return self.inputCount
    
    @Property
    def inputNames(self, index):
        return self._inputnames[index]
    @inputNames.lengetter
    def linputNames(self):
        return self.inputCount
    @inputNames.setter
    def sinputNames(self, index, value):
        self._inputnames[index] = value
    
    @Property
    def outputNames(self, index):
        return self._outputnames[index]
    @outputNames.lengetter
    def loutputNames(self):
        return self.outputCount
    @outputNames.setter
    def soutputNames(self, index, value):
        self._outputnames[index] = value
        

class Normalizer(LinearModel):
    '''
    Normalizing model.
    Data are in a numpy.matrix of sizes (N, 2)
    '''

    def __init__(self, owner=None, data=None, inNames=None, outNames=None, 
                 style=0, name="", reverse=False): 
        super(Normalizer, self).__init__(owner, name)
        self.style = style 
        if (data is None) or isinstance(data, int):
            try: count = int(data)
            except: count = 1
#            data = matrix([[1, 0] for _ in range(count)])  modif le 03/04/2019
            data = zeros((count, 2))
            for ind in range(count):
                data[ind, 0] = 1
        self.setData(data, reverse)
        self._setNames(inNames, outNames)
                        
    def setData(self, data, reverse=False):
        self.data = copy(data)
        if reverse:
            self.data[:, 0] = 1/self.data[:, 0]
            self.data[:, 1] = - self.data[:, 1] * self.data[:, 0]
        self._inputs = [0.0 for _ in range(self.inputCount)]
        self._outputs = [0.0 for _ in range(self.inputCount)]
                
    def isNorm(self):
        return True
        
    @Property
    def inputCount(self):
        try:
            return self.data.shape[0]
        except:
            return 0
    
    @Property
    def outputCount(self):
        try:
            return self.data.shape[0]
        except:
            return 0
    
    def propagate(self, inputs=None):
        if inputs is not None:
            self._outputs = inputs * self.data[:, 0] + self.data[:, 1]            
        else:
            self._outputs = self._inputs * self.data[:, 0] + self.data[:, 1]
        return self
    
    def backPropagate(self, gradient=None, gradOutput=0, computelevel=ID_COMPUTE):
        """Retropropagation dans le modèle.
        
           gradOutput est le vecteur directeur de la retropropagation.
           Retourne un tuple constitue de :
               le vecteur gradient par rapport aux poids = None
               le vecteur gradient par rapport aux entrées
        """  
        return gradient, gradOutput * self.data[:, 0]

#    def inputNormalization(self, index):
#        return self.data[index, :]
#
#    def outputNormalization(self, index):
#        return self.data[index, :]

class Polynom(LinearModel):
    '''
    # under development
    '''
    
    def __init__(self, owner=None, inputs=0, output=0, order=1, inNames=None, outNames=None, name="model_0"):
        super(Polynom, self).__init__(owner, inNames, outNames, name)
        # under development
          
    def propagate(self, inputs=None, weights=None):
        # under development
        return self

    def backPropagate(self, gradient, gradInput=None, gradOutput=None, computelevel=ID_COMPUTE): 
        # under development 
        return None, None

register(Normalizer)       
register(Normalizer, "NORMALIZER") 
register(Polynom)       
register(Polynom, "POLYNOM") 
