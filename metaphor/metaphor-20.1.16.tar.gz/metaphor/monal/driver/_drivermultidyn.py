#-*- coding: ISO-8859-15 -*-
#===============================================================================
# $Id: _drivermultidyn.py 4787 2018-05-27 20:46:03Z jeanluc $
#  Module  _drivermultidyn
#  Projet MonalPy
# 
#  Implementation python de monal
# interface pour Dll
#
#  Author: Jean-Luc PLOIX  -  NETRAL
#  Mai 2014
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

import os, sys
from ctypes import CFUNCTYPE, byref, c_int, c_long, c_double, c_void_p
from weakref import proxy
from numpy import asarray, ndarray, zeros, load, NaN, reshape, sqrt
from numpy import int as npint
from numpy import double as npdouble
from numpy import float as npsum
from numpy import sum as npflaot
from numpy import dot as npdot

from metaphor.nntoolbox.utils import floatEx, setRandSeed
from metaphor.monal.Property import Property #, Properties, delegate
from metaphor.monal import monalconst as C, specialmath as sp
from metaphor.monal.lcode import codeconst as CC
from metaphor.nntoolbox.utils import maxWorkers
from metaphor.monal.driver import DriverBase  #, getRandState, setRandState
from metaphor.monal.driver._driverlib import DriverLibError, DriverLib
from metaphor.monal.driver import optim_bfgs, optim_leastsq

import math
# try:
#     from sc ipy.stats.t import interval
#     from sc ipy import optimize
#     OKSc ipy = True
# except ImportError:
#     OKSc ipy = False
#     from monal.util.monaltoolbox import interval
#import numpy.ran dom as rnd
# import concurrent.fut ures as cf

# U SE_PARALLEL_MAIN = 1
# U SE_SUPER_TRAIN = 1
# D EBUG_LOO = 0
# D EBUG_LOO_FILE = 0
# D  EBUG_LOCAL_TRAIN = 0


class DriverMultiDynError (DriverLibError): 
    """DriverMultiDyn Exception.
    """
    pass

class DriverMultiDyn(DriverLib):
    """class DriverMultiDyn
    Gestionnaire des drivers d'apprentissage multimodeles provenant de 
    librairies dynamiques (dll, so, dylib);
    """
    def __init__(self, libfilename, verbose=0, callback=None): # DriverMultiDyn
        super(DriverMultiDyn, self).__init__(libfilename, verbose)  #, callback
        #self._modelType = 2
        #self.model Count = self.dataCount
        if callback:
            self.setcallback(callback)
        
    def __repr__(self):
        return self.repr('long')
    
    @property
    def modelCount(self):
        return self.dataCount
    
    @Property
    def configuration(self): # DriverMultiDyn
        return self.getStrPropertyFromLib("configuration")
    
    @Property
    def configurationLong(self): # DriverMultiDyn
        return self.getStrPropertyFromLib("configuration")
#         return self.getStrPropertyFromLib("configurationlong")
    
    def reprlist(self, mode='long', prefix="module"):
        lst = super(DriverMultiDyn, self).reprlist(mode, prefix)
        lst.append("model count: %s"%  self.modelCount)
        if mode in ['long']:  #, 'short'
            lst.append("configuration: %s"% self.configuration)
            lst.append("signature: {0}".format(self.signature()))
        return lst    
    
    def dict(self):
        return {
            'name': self.moduleName,
            'type': self.moduleType,
            'codeversion': self.codeVersion,
            'created': self.created,
            'mark': self.mark,
            'base': self.base,
            'config': self.configuration,
            'property': self.propertyName,
            'paramCount': self.paramCount,
            'modelCount': self.modelCount,
            'hidden': self.hidden,
            }
    
    def __getstate__(self):
        objdict = self.__dict__.copy()
        objdict["lib"] = None
        objdict["libname"] = ""
        objdict["_lastweights"] = None
        objdict["_callback"] = None
        objdict["targets"] = self.targets
        objdict["propertyName"] = self.propertyName
        return objdict
     
    def __setstate__(self, state):
        targets = state.pop("targets", None)
        propertyName = state.pop("propertyName", None)
        self.__dict__.update(state)
        self._setlib(self.libfilename)
        if targets is not None:
            self.targets = targets
        if propertyName is not None:
            self.propertyName = propertyName
         
    def signature(self):
        weights = [0.01 for _ in range(self.paramCount)]
        inputs = [0.01 for _ in range(self.inputCount)]
        res = 0
        for ind in range(self.modelCount):
            if self.inputCount:
                res += self.transferindex(weights, inputs, ind)
            else:
                res += self.transferindex(weights, ind)
        return res / self.paramCount
    
    def transferindex(self, params=None, index=-1):
        if isinstance(params, str) and params == 'extra':
            return [self.transferindex(param, index) for param in self._extraweights]
        if params is not None:
            params = asarray(params, npdouble)
        else:
            if self.weights is not None:
                params = self.weights
        if params is not None:
            self._lastweights = params.copy
        else:
            raise DriverMultiDynError("params sould not be null in transferindex")
         
        out = None
        try:
            source = params.copy()
            source_p = c_void_p(source.ctypes.data)
            out = zeros((1,), dtype=npdouble)
            out_p = c_void_p(out.ctypes.data)
            res = self.lib.transferindex(index, source_p, out_p)
            if res < 0: 
                raise DriverMultiDynError(self.lasterror)
             
        except: pass
        if self.outputCount ==1:
            out = out[0]
        return out
 
    def transfergradientindex(self, params=None, index=-1):
        if params is not None:
            params = asarray(params, npdouble)
        else:
            if self.weights is not None:
                params = self.weights
        if params is not None:
            self._lastweights = params.copy
        else:
            raise DriverMultiDynError("params sould not be null in transfergradientindex")
         
        out = None
        #target = None
        try:
            paramCount = self.lib.paramCount()
            source = params.copy()  #asarray(params, npdouble)
            source_p = c_void_p(source.ctypes.data)
            gradient = zeros((paramCount,), dtype=npdouble)
            gradient_p = c_void_p(gradient.ctypes.data)
            out = zeros((1,), dtype=npdouble)
            out_p = c_void_p(out.ctypes.data)
            res = self.lib.transfergradientindex(index, source_p, out_p, gradient_p)
            if res < 0: 
                raise DriverMultiDynError(self.lasterror)
             
        except: pass
        if self.outputCount ==1:
            out = out[0]
        return out, gradient
         
def onGetNewWeights(model, weightsstddev):
    return model.newWeights(weightsstddev)
    
def kerneltrainintegratedmain(model, weights, maxiter, withhistory, index=-1):
    res = model.kerneltrainintegratedmain(weights, maxiter, withhistory, index)
    if index < 0:
        return res
    return (index,) + res

def core_train2(model, weights, maxiter, withhistory, index=-1):
    return model.core_train2(weights, maxiter, withhistory, index)

def kerneltrainintegratedmain3(model, weights, maxiter, withhistory, index=-1):
    return model.kerneltrainintegratedmain3(weights, maxiter, withhistory, index)

#==============================================================================
if __name__ == "__main__":
    from io import StringIO, BytesIO
    import pickle as pickle
    single = 1
#     source = "C:\\Projets\\GM\\TestAD\\Base115new\\base115new_chi0iso00n.dll"
#     source = "/Users/Shared/GMWorkspace/BaseA109/libbasea109_chi03n.so"
    source = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_Test/src/metaphor/test_monal/testFiles/libnn_5_5_1.so"
    #"/Users/Shared/workspace/GraphMachine/test/testfiles/libbase321_27_dgrs5_5n.so"
    targetfile = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_Test/src/metaphor/test_monal/testFiles/L_153_target.csv" 
    #"/Users/Shared/workspace/GraphMachine/test/testfiles/LogP_Base321"

#code version
    
    model = DriverMultiDyn(source)
    #model.settrainingset()
    model.setRandSeed(1947)
    model.targets = targetfile
    
#    st = pickle.dumps(model)
    stream = BytesIO()
    pickle.dump(model, stream)
    stream.flush()
    stream.seek(0)
    #stream2 = StringIO(stream.getvalue())
    model2 = pickle.load(stream, allow_pickle=True)
    stream.close()
    #model2 = DriverMultiDyn(source)
    #model.settrainingset()
    #model.set RandSeed(1947)
    #model2.targets = targetfile
    
    print("property:", model.propertyName)
    print()
    print("moduleName", model.moduleName)
    print("monalVersion", model.monalVersion)
    print("created", model.created)
    print("mark", model.mark)
    print("base", model.base)
    print("linear", model.isLinear)
    print("paramlCount", model.paramCount)
    print("modelCount", model.modelCount)
    print("inputCount", model.inputCount)
    print("outputCount", model.outputCount)
    print("hidden", model.hidden)
    print("biasBased", model.biasbased)
    print("outlinks", model.outlinks)
    #model2.targets = [0 for _ in range(model.modelCount)]
    #print "target 1", model.targets
    #print "target 2", model2.targets
    print("norm 1", model.outputnorm)
    print("norm 2", model2.outputnorm)
    print(model.lib)
    print(model2.lib)
    
    #if single:
    model.setRandSeed(194999)
    ww = model.newWeights(0.3)
    #residu = model.getres iduals(ww)
    #print "residu", residu
    costini = model.getCost(ww)
    #ww2, epochs, cost, code
    #bests, saveres = model.mult itrain(initcount=5, initweights=ww, maxiter=100)
    #bestmem = bests[0][0]
    #print "bests"
    #for val in bests:
    #    print "", val
    
    
    
    
 #    cur, epochs, cost, trai nend, code = model.kerneltrainintegratedmain(ww, 150)
    #cost2 = model.getcost(cur)
    #press_old = model.getPRESS_(cur, None, True, True)
#     press = model.getPRESS(cur, 1, 1)
#     print("cost ini  ", costini)
#     print("cost final", cost)
#     print("PRESS", press)
#     #print "PRESS old", press_old
#     print("epochs", epochs)
#     #else:
        #os.system("ipcluster start")
        #lst = multitrainintegrated(model, targetfile, None, 8, 100)
        #for val in lst:
        #    print val
        #for ind, (cur, N, fopt, mem, code) in enumerate(lst):
        #    print ind, N, fopt
        
        #os.system("ipcluster stop")
    
    #model = None
    
    print("done")