#-*- coding: ISO-8859-15 -*-
#===============================================================================
# $Id: _model.py 4819 2018-11-02 05:32:25Z jeanluc $
#  Module  _model
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
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================

from numpy import zeros, identity, array, asarray
from numpy.random import randn
try:
    import cPickle  as pickle
except ImportError:
    import pickle
import os, sys
import json
from datetime import datetime
from ...nntoolbox.utils import floatEx
#from nntoolbox._2and3 import isstr
from six import string_types, print_, text_type
from ..Property import Property, Properties, IndexedProperty, makefct
from ..util.monalbase import Component, MonalError 
from ..util.monaltoolbox import isStrNum
from ..util.utils import safemakedirs
from .. import monalconst as C
from ..util import leverage
from ..driver._optimizer import optim_bfgs #optim_leastsq, 

class ModelBase(Component):
    def __init__(self, owner=None, name=""):
        super(ModelBase, self).__init__(owner, name)
        dt = datetime.now()
        self._modelType = 0

    @Property
    def modelCount(self):
        return 1
    
    @Property
    def modelType(self):
        return self._modelType
    @modelType.setter
    def modelType(self, value):
        self._modelType = value
        
    @Property    
    def defaultName(self):
        return ""
    
    @Property
    def richName(self):
        defaultname = self.defaultName
        if defaultname:
            if self.name:
                return "{0}_{1}".format(self.name,defaultname)
            return defaultname
        return self.name

class Leurre(ModelBase):
    def __init__(self, owner=None, model=None):
        # initialisation d'un leurre en copie d'un modele
        super(Leurre, self).__init__(owner, model.name)
        self.trueName = model.trueName
        self.hidden = model.hidden
        self.biasBased = model.getBiasBased()
        self.outputLinks = model.getOutputLinks()
        self.paramCount = model.paramCount
        self.dimension = model.dimension
        self.inputCount = model.inputCount
        self.outputCount = model.outputCount
        self.inputNames = [model.inputNodes[ind].nameC() for ind in range(self.inputCount)]
        self.outputNames = [model.outputNodes[ind].nameC() for ind in range(self.outputCount)]
        try:
            self.isLinear = model.isLinear
        except AttributeError:
            try:
                self.isLinear = model.owner.isLinear
            except:
                self.isLinear = not bool(self.hidden)
        self.smiles = model.smiles
        try:
            self.doubt = model.doubt
        except AttributeError:
            self.doubt = False

@Properties(("originallink", 'useOriginal', 'longParamCount',), False)
class _Model (ModelBase):
    source = None
    def __init__(self, owner=None, name=""):  # Model
        super(Model, self).__init__(owner, name)
        self._comments = []
        self.style = 0
        self._isLinear = None
        self.curinputs = None
        self._truename = ""
        self._paramdict = None
        self._originallink = True
        self._useOriginal = False
        self._longParamCount = 0
        self._modelType = 1
        self._extraInputCount = 0
    
    @Property
    def trueName(self):  # Model
        return self._truename if self._truename else self.name 
    @trueName.setter
    def strueName(self, value):  # Model
        self._truename = value 
    
    def propagate(self, inputs=None, weights=None):  # Model
        return self
        
    def __call__(self, inputs=None, computelevel=C.ID_COMPUTE, gradient=None, 
                 gradInput=None, hessian=None, original=True):  # Model
        inputs = None if inputs is None else asarray(inputs)
        if (inputs is not None) and (isinstance(inputs, IndexedProperty) or (inputs.ndim==2)):
            res = [self.__call__(locinput, computelevel, gradient, gradInput, 
                                 hessian, original) for locinput in inputs]
            return asarray(res)    
        self.computelevel = computelevel 
        self.propagate(inputs)
        if self.computelevel <= C.ID_COMPUTE:
            # pas de demnde de calcul des gradients
            return self.getOutputvalues()
        
        # ici on va calculer les gradients par rapport aux poids et par rapport aux entrées.
        # le supplément pour calcul du 2eme gradient est très faible
        ndata = self.inputDim
        internalgrad = gradient is None
        internalgradIn = (gradInput is None) and (ndata == 1) and self.layerLength(0)
        no = self.outputCount
        if self.useOriginal:
            ns = self.longParamCount
        else:
            ns = self.synapseCount
        
        if no == 1:
            if internalgrad:
                if ns <= 1:
                    gradient = zeros((ndata,))
                else:
                    gradient = zeros((ndata, ns)).squeeze()
            if internalgradIn:
                gradInput = zeros((self.layerLength(0),))
            outGrad = 1
                
            self.backPropagateCoreSingleOutput(gradient, gradInput, outGrad, original=original)
                
            if internalgrad:
                gradient = gradient.squeeze()
            
        else:
            if internalgrad:
                gradient = zeros((no, ndata, ns))
            if internalgradIn:
                gradInput = zeros((no, self.layerLength(0)))
            outGrad = identity(no)
                
            self.backPropagateCoreMultiOutput(gradient, gradInput, outGrad)
                
            if internalgrad:
                gradient = gradient.squeeze()
            if internalgradIn:
                gradInput = gradInput.squeeze()
        
        #if not self.computeLevel:
        #    return self.outputs
        if (gradInput is None) or not len(gradInput): # or not gradInput:
            return self.getOutputvalues(), gradient
        return self.getOutputvalues(), gradient, gradInput
        
    # = transferOld
    
    def getOutputvalues(self):  # Model
        if self.outputCount == 1:
            return self.outputs[0]
        return array([val for val in self.outputs])
    
    @property
    def isLinear(self):
        return self.getIsLinear()
    
    def getIsLinear(self):  # Model
        if self._isLinear is not None:
            return self._isLinear
        hasw = self._weights is not None
        if self._isLinear is None:
            result = True
            if hasw:
                memweight = self._weights.copy()
            #ww = randn(dim,)
            #self.setWeights(ww)
            self.initWeights()
            inputs = randn(self.inputCount,)
            res1 = self(inputs, computelevel=C.ID_DIFF, original=False)
            #ww = randn(dim,)
            #self.setWeights(ww)
            self.initWeights()
            res2 = self(inputs, computelevel=C.ID_DIFF, original=False)
            
            for r1, r2 in zip(res1[1], res2[1]):
#                 for val1, val2 in zip(r1, r2):
                if abs(r1 - r2) > 1E-10:
                    result = False
                    break
#                 if not result:
#                     break
            if hasw:
                self.setWeights(memweight)
            else:
                self._weights = None
            self._isLinear = result
        return self._isLinear
    @isLinear.setter
    def sisLinear(self, value):  # Model
        self._isLinear = value
        
    def signature(self):  # Model
        memweights = self._weights.copy()
        self._weights = [0.1 for _ in range(self.paramCount)]
        inputs = [0.1 for _ in range(self.inputCount)]
        res = self(inputs)
        self._weights = memweights
        return res
        
    def _expandvec(self, vec, inivec, fixed): # copie depuis _driver
        index = 0
        target = []
        for inivalue, fix in zip(inivec, fixed):
            if fix:
                val = inivalue
            else:
                val = vec[index]
                index += 1
            target.append(val)
        return asarray(target)
    
    def _reducevec(self, vec, fixed): # copie depuis _driver
        return asarray([val for test, val in zip(fixed, vec) if not test])

    def reverse_train(self, outputtarget, inputs=None, fixedinputs=None, 
        epochs=None, modelindex=-1, callback=None, debug=0, verbose=0):  # Model
        """Obtain the result of model reverse transfer.
        
        Parameters:
        
         - outputtarget -> output value target.
         - inputs -> initial input values. It may be a vector-like, a dictionary or None:
             - vector-like : vector of the initial input values, in the order of the inputs.
             - dictionary: initial input value for each input name.
             - None : no new initial input values (default).
         - fixedinputs -> fixed input values.  It may be a vector-like, a dictionary or None:
             - vector-like : vector of boolean values, in the order of the inputs.
             - dictionary : each input may be fixed (or not) by its name. A missing input is considered as free.
             - None : all input values are free
         - acc -> accuracy of targetting. Optimizing computation is stopped as soon as this accuracy is obtained, no matter the epochs value.
         - epochs -> maximum number of optimizing computation epochs.
         - callback -> callback function. It takes a current index as parameter.
         - modelindex -> if -1, the computation take into account all the extra weights. Otherwise, if positive, give the index of the model used.
        """
        if not self.inputCount:
            raise MonalError("Model must have at least 1 input to be reverse-trained")
        acc=1.49012e-08
        if fixedinputs is None:
            fixedinputs = [0 for _ in range(self.inputCount)]
        if isinstance(fixedinputs, dict):
            lst = []
            for inname in self.inputNames:
                if inname in fixedinputs:
                    lst.append(fixedinputs[inname])
                else:
                    lst.append(0)
            fixedinputs = lst
        if inputs is None:
            inputs = asarray(self.inputs)
        #inputs = self.normalizeInputs(inputs)
        inputini = [val for val in inputs]
        #outputtarget = self.unnormalizeOutputs(outputtarget, reverse=True)
        args=(inputini, fixedinputs, outputtarget, modelindex)
        factor = self.inputCount    
        reducedinputs = self._reducevec(inputs, fixedinputs)

        newreducedinputs, code = optim_bfgs(self.inputTrainCost, reducedinputs, args, 
            self.inputTrainGrad, maxiter=epochs, disp=verbose >= 3, factor=factor, 
            callback=callback)
        
        if debug:
            if code & 1:
                print_('Information: no acceptable point found', file=sys.stderr)
            if code & 2: 
                print_('Information: accuracy reached', file=sys.stderr)
            if code & 4: 
                print_('Information: stop for maxiter', file=sys.stderr)
        newinputs = self._expandvec(newreducedinputs, inputini, fixedinputs)
        #newinputs = self.normalizeInputs(newinputs, reverse=True)
        return newinputs, code

    def transfer(self, inputs=None, style=C.TFR_STD, original=True, **kwds):  # Model
        # ici transfer sur un modele , pas sur un driver.kwds['index'] n'est pas 
        # pris en compte
        newWeights = kwds.pop('weights', None)
        if newWeights is not None:
            memweights = self._weights
            self._weights = newWeights
        indexmove = kwds.pop('indexmove', -1)
        if (inputs is not None) and (0 <= indexmove < self.inputCount):
            indexinputs = kwds.pop('indexinputs', [])
            result = []
            inival = inputs[indexmove] 
            for value in indexinputs:
                inputs[indexmove] = value
                res = self.transfer(inputs, style=style, original=original)
                result.append(res)
            inputs[indexmove] = inival
        
        elif style == C.TFR_STD:  # 0
            result = self(inputs)  #.transferOld
        elif style == C.TFR_GRADIENT:  # 1
            result = self(inputs, C.ID_DIFF, original=original)  #.transferOld
        elif style == C.TFR_LEVERAGE:  # 2
            res = self(inputs, C.ID_DIFF, original=original)  #.transferOld
            result = res  # a revoir
        elif style == C.TFR_GRADIENTLEVERAGE:  # 3
            res = self(inputs, C.ID_DIFF, original=original)# a revoir  #.transferOld
            pass
            result = res  # a revoir
        elif style == C.TFR_GRADIENTCONFIDENCE:  # 4
            res = self(inputs, C.ID_DIFF, original=original)# a revoir  #.transferOld
            pass
            result = res  # a revoir
        elif style == C.TFR_GRADIENTINPUTS:  # 5
            res = self(inputs, C.ID_DIFF, original=original)  #.transferOld
            result = res[0], res[2]
        elif style == C.TFR_GRADIENTHESSIAN:  # 6
            res = self(inputs, C.ID_DIFF_SEC, original=original)  #.transferOld
        if newWeights is not None:
            self._weights = memweights
        return result  # a revoir
    
    def initWeights(self, stddev=0.3, bias0=False, seed=None): 
        raise Exception('initWeights must be implemented in children classes of Model')
        
    def loadWeightsXML(self, source):  # Model
        return None
        
    def maxParam(self):  # Model
        return -1
    
    def isModel(self):  # Model
        return True
    
    def isNorm(self):  # Model
        return False
    
    def addComment(self, value=""):  # Model
        self._comments.append(value)
        
    def getComment(self, index=0):  # Model
        try: return self._comments[index]
        except: return ""
        
    def getComments(self):  # Model
        return '\n'.join(self._comments)
    
    @Property
    def comments(self, index):  # Model
        return self._comments[index]
    @comments.lengetter
    def lcomments(self):  # Model
        return len(self._comments)
    
    @Property
    def inputs(self, index):  # Model
        raise IndexError
    @inputs.setter
    def inputs(self, index, value):  # Model
        raise IndexError
    @inputs.lengetter
    def inputs(self):  # Model
        return self.inputCount
    
    @Property
    def outputs(self, index):  # Model
        raise IndexError
    @outputs.setter
    def outputs(self, index, value):  # Model
        raise IndexError
    @outputs.lengetter
    def outputs(self):  # Model
        return self.inputCount
    
    @Property
    def commentCount(self):  # Model
        return len(self._comments)
    
    @Property 
    def extendedInputCount(self):
        return self.inputCount + self._extraInputCount        
    
    @Property
    def inputCount(self):  # Model
        return 0
    
    @Property
    def outputCount(self):
        return 0#self._outputcount
    
    @Property
    def order(self):  # Model
        return 0

    @Property
    def hiddenCount(self):  # Model
        return 0
    
    @Property
    def synapseCount(self):  # Model
        return 0
    
#     @Property
#     def weights(self, index):  # Model
#         return []
#     @weights.lengetter
#     def lweights(self):  # Model
#         return 0
#     @weights.setter
#     def sweights(self, index, value):  # Model
#         pass
    
    @Property
    def paramCount(self):  # Model
        return 0
    
    def hasMinMax(self):  # Model
        return False
    
    def saveModel(self, filename, savingformat=C.SF_XML, 
        modeltemplate="", callback=None, compiler=""):  # Model
        if savingformat in [C.SF_XML, C.SF_BINARY, C.SF_JSON]:
            return self.saveObj(self, filename, savingformat)
        else:
            raise Exception('saveModel not implemented yet with format = {}'.format(savingformat))
    
    def saveParameters(self, filename, savingformat=C.SF_XML, count=0, appending=False):  # Model
        if savingformat in [C.SF_XML, C.SF_BINARY, C.SF_JSON]:
            return self.saveObj(self._weights, filename, savingformat, appending)
        else:
            raise Exception('saveModel not implemented yet with format = {}'.format(savingformat))
    
    def saveObj(self, obj, target, savingformat=C.SF_XML, appending=False):  # Model
#        if isinstance(target, basestring):
        if isinstance(target, string_types):
            basedir = os.path.dirname(target)
            safemakedirs(basedir)
            #if not os.path.exists(basedir):
            #    os.ma kedirs(basedir)
            if appending:
                mode = "ab"
            else:
                mode = "wb"
            with open(target, mode) as ff:
                res = self.saveObj(obj, ff, savingformat)
            return res
        if savingformat == C.SF_XML:
            try:
                return target.write(obj.xml().encode())
            except:
                return target.write(obj.xml())
        if savingformat == C.SF_BINARY:
            return pickle.dump(obj, target, pickle.HIGHEST_PROTOCOL)
        if savingformat == C.SF_JSON:
            return json.dump(self)

    @Property 
    def paramdict(self):  # Model
        if self._paramdict is None:
            self._paramdict = self.getParamDict(True)
        return self._paramdict
    
    def getIndexWeightOfName(self, wname):  # Model
        """Retourne l'indice d'un poids de nom défini
        """
        return self.paramdict[wname]
    
    def loadFromASCIIStrList(self, lst, index):  # Model
        res = bool(lst)
        if not res:
            return 0
        dim = self.paramCount
        #i0 = 0
        wformat = []
        #delta = 0
        st= lst[index]
        llst = st.split('=')
        if llst[0].strip().lower() == "count":
            #index += 1
            dim = int(llst[1].strip())
            index += 1
            #st = lst[index]
        for row in range(dim):
            st = lst[index + row]
            locallst = st.split(";")
            if isStrNum(locallst[0]):
                self.weights[row] = floatEx(locallst[0])
                wformat.append(row)
            elif (len(locallst) >= 2) and isStrNum(locallst[1]):
                wname = locallst[0]
                if isinstance(wname, string_types):
                    wname = self.getIndexWeightOfName(wname)
                if wname >= 0:
                    self.weights[wname] = floatEx(locallst[1])
                    wformat.append(wname)
        return dim

# def _decorator(cls, prop_names, readonly):
#     for name in prop_names:
#         hname = '_' + name
#         if not hasattr(cls, hname):
#             setattr(cls, hname, None) 
#         getter = makefct(hname, False)
#         setter = None if readonly else makefct(hname)
#         setattr(cls, name, Property(getter, setter))    
#     return cls        
# 
#         
# Model =  _decorator(_Model, ("originallink", 'useOriginal', 'longParamCount',), False) 
Model = _Model

if __name__ == "__main__":
    pass
#     inidir = "/Users/jeanluc/Desktop/Reserve/Tests SAP Samir MEDROUK"
#     source = os.path.join(inidir, "Modeles fusionnes", "Modele_Final.NML")
#     inifile = os.path.basename(source)
# 
#     with open(source, "r") as ff:
#         sourcecontent = ff.read()
     