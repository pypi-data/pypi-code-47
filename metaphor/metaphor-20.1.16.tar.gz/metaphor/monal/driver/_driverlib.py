#-*- coding: ISO-8859-15 -*-
#===============================================================================
# $Id: _driverlib.py 4565 2017-08-25 10:44:17Z jeanluc $
#  Module  _DriverLib
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
from six import PY3, text_type

from ctypes import CFUNCTYPE, byref, c_int, c_long, c_double, c_void_p, c_char_p
from weakref import proxy
import random
#from functools import reduce
from numpy import asarray, ndarray, zeros, ones, load, NaN, reshape, sqrt, \
    isnan, squeeze
from numpy import int as npint, long as nplong
from numpy import double as npdouble
from numpy import float as npsum
from numpy import sum as npflaot
from numpy import dot as npdot

from metaphor.nntoolbox.utils import floatEx, isNum, floatEx, decodequote, \
    RE_NONE, RE_LOO, RE_SUPER, BSGROUP, seedList, insertInList

from metaphor.nntoolbox.datareader.datasource import DataSource
from metaphor.nntoolbox.constants import USE_PARALLEL_MAIN, USE_PARALLEL_BS, \
    USE_SUPER_TRAIN
from metaphor.nntoolbox.utils import concatenateList
from metaphor.monal.Property import Property #, Properties, delegate
from metaphor.monal.library.libmanager import LibManager, LibraryManagerError
from metaphor.monal import monalconst as C, specialmath as sp
from metaphor.monal.lcode import codeconst as CC
from metaphor.nntoolbox.utils import maxWorkers
from metaphor.monal.driver import DriverBase
from metaphor.monal.driver._parallelJobs import trainJobBS, trainJob, no_parallel_seed
from metaphor.monal.driver import optim_bfgs, optim_leastsq

import math
#from api.api import inpts
try:
    from scipy.stats.t import interval
    from scipy import optimize
    OKScipy = True
except ImportError:
    OKScipy = False
    from metaphor.monal.util.monaltoolbox import interval
try:
    import concurrent.futures as cf
except: pass

# moved to metaphor.nntoolbox.constants
# USE_PARALLEL_MAIN = 0 # ici a remettre a 1
# USE_PARALLEL_BS = 1  # ici a remettre a 1
# USE_SUPER_TRAIN = 1
DEBUG_LOO = 0
DEBUG_LOO_FILE = 0
DEBUG_LOCAL_TRAIN = 0

def callbackminprint(cost, count):
    print("cost({0}): {1}".format(count, cost))
    # le return = 0 pour continuer. Une valeur True arrete l'operation
    return 0

def callbackmin(cost, count):
    return 0

# def callbackwrite(cost, count):
#     print("cost({0}) = {1}".format(count, cost))
#     return 0

class DriverLibError (Exception): 
    """DriverLib Exception.
    """
    pass

class DriverLib(DriverBase, LibManager):
    """class DriverLib
    Gestionnaire des drivers d'apprentissage multimodeles provenant de librairies dynamiques (dll, so, dylib)
    """
    
    def __init__(self, libfilename, verbose=0):  #, callback=None): # DriverLib
        DriverBase.__init__(self, verbose)  #, callback)
        LibManager.__init__(self, libfilename)
        try:
            self._modelType = self.moduleType
        except:
            self._modelType = 3
        self.savedir = ""
        self._targetfile = ""
        self._lastweights = None
        self._weights = None
        self.cumulEpoch = 0
        self.stoptrain = 0   
        self.resultMatrix = None   
        self.presses = None
        self._callbacklib = None 
        self._callbacktype = None
        
        if self.propertyName == 'unknown':
            self.lib.setproperty(None)
#         if self._callback and self.lib:
#             self.setcallback(self._callback)      
    
    def __del__(self):
        LibManager.__del__(self)
        DriverBase.__del__(self)
    
    def reprlist(self, mode='long', prefix="module"):
        lst = ["{0} {1}:".format(prefix, self.moduleName)]
        if mode == 'long':
            lst.append("code module/program %s/%s"% (self.codeVersion, CC.__version__))
            lst.append("type %s"% self.moduleTypeStr)
            if self.mark:
                lst.append("mark: %s" % self.mark)
        if self.created and not self.mark:
            lst.append("created %s" % self.created)
        if self.base:
            lst.append("base: %s" % self.base)
        if self.propertyName:
            lst.append("property: %s" % self.propertyName)
        if self.inputCount:
            lst.append("inputs: {0}".format(self.inputCount))
        lst.append("hidden: %s"% self.hidden)
        lst.append("outputs: {0}".format(self.outputCount))
        lst.append("parameter count: %s" % self.paramCount)
        if mode == 'long':
            if self.biasbased is not None:
                lst.append("biasbased: %s"%  self.biasbased)
            if self.outlinks is not None:
                lst.append("outlinks: %s"%  self.outlinks)
            if self.targets is not None and len(self.targets):
                lst.append("outputnorm: %s"% self.outputnorm)
                if len(self.targets) <= 10:
                    tg = "targets %s"% self.targets
                else:
                    l1 = [str(val) for val in self.targets[:5]]
                    l2 = [str(val) for val in self.targets[-5:]]
                    tg = "targets [%s]"% " ".join(l1 + ["..."] + l2)
                lst.append(tg)
        return lst
    
    def repr(self, mode='long', tab="\t", prefix="module"):
        lst = self.reprlist(mode=mode, prefix=prefix)
        fulltab = "\n%s" % tab
        return fulltab.join(lst) 
    
    def __repr__(self):
        return self.repr('long')
    
    def xml(self): # LibManager
        st = self.getStrPropertyFromLib("xml")
        st = decodequote(st)
        return st
    
    def dict(self):
        return {
            'name': self.moduleName,
            'type': self.moduleType,
            'codeversion': self.codeVersion,
            'created': self.created,
            'mark': self.mark,
#            'config': self.configuration,
            'base': self.base,
            'property': self.propertyName,
            'paramCount': self.paramCount,
            'dataCount': self.dataCount,
            'hidden': self.hidden,
            }

    @Property
    def moduleTypeStr(self):
        if self.moduleType == 1:
            return 'usage, single'
        elif self.moduleType == 2:
            return 'training, multiple'
        elif self.moduleType == 3:
            return 'training, single'
        else:
            return 'unknown'
    
    @Property
    def paramCount(self):  # DriverLib
        return self.lib.paramCount()
        
    @Property
    def weights(self): # DriverLib
        return self._weights
    @weights.setter
    def weights(self, value):
        if isinstance(value, (list, ndarray)):
            self._weights = value.copy()
        else:
            self._weights = asarray(value, npdouble)
    
    def setWeights(self, weights):  # DriverLib
        self.weights = weights.copy()
    
    def getWeights(self):  # DriverLib
        return self._weights
    
    @Property
    def inputRanges(self):
        target = zeros((self.inputCount * 2), dtype=npdouble)
        target_p = c_void_p(target.ctypes.data)
        res = self.lib.getinputranges(target_p)
        if res < 0: 
            raise LibraryManagerError(self.lasterror)
        target = target.reshape(self.inputCount, 2)
        return target
    
    @Property
    def outputRanges(self):
        target = zeros((self.outputCount * 2), dtype=npdouble)
        target_p = c_void_p(target.ctypes.data)
        res = self.lib.getoutputranges(target_p)
        if res < 0: 
            raise LibraryManagerError(self.lasterror)
        target = target.reshape(self.outputCount, 2)
        return target
    
    @Property
    def biasbased(self):  # LibManager
        try:
            dim = self.lib.getbiasbased(None)
            target = zeros((dim,), dtype=npint)
            target_p = c_void_p(target.ctypes.data)
            res = self.lib.getbiasbased(target_p)
            if res < 0: 
                raise LibraryManagerError(self.lasterror)
        except AttributeError:
            target = None
        return target
    
    @Property
    def outlinks(self):  # LibManager
        try:
            dim = self.lib.getoutlinks(None)
            target = zeros((dim,), dtype=npint)
            target_p = c_void_p(target.ctypes.data)
            res = self.lib.getoutlinks(target_p)
            if res < 0: 
                raise LibraryManagerError(self.lasterror)
        except AttributeError:
            target = None
        return target
    
    @Property
    def inputNorm(self):
        target = zeros((self.inputCount * 2), dtype=npdouble)
        target_p = c_void_p(target.ctypes.data)
        res = self.lib.getinputnorm(target_p)
        if res < 0: 
            raise LibraryManagerError(self.lasterror)
        
        target = target.reshape(self.inputCount, 2)
        return target
    
    @Property
    def outputNorm(self):
        target = zeros((self.outputCount * 2), dtype=npdouble)
        target_p = c_void_p(target.ctypes.data)
        res = self.lib.getnorm(target_p)
        if res < 0: 
            raise LibraryManagerError(self.lasterror)
        target = target.reshape(self.outputCount, 2)
        return target
    
    def __getstate__(self):
        objdict = self.__dict__.copy()
        objdict["lib"] = None
        objdict["libname"] = ""
        objdict["_lastweights"] = None
        objdict["_callback"] = None
        objdict["targets"] = self.targets
        objdict["propertyName"] = self.propertyName
        objdict["datacount"] = self.lib.dataCount()
        objdict["inputcount"] = self.lib.inputCount()
        objdict["inputs"] = self.fullData
        return objdict
    
    def __setstate__(self, state):
        targets = state.pop("targets", None)
        propertyName = state.pop("propertyName", None)
        datas = state.pop("inputs", None)
        datacount = state.pop("datacount", 0)
        inputcount = state.pop("inputcount", 0)
        self.__dict__.update(state)
        self._setlib(self.libfilename)
        if datas is not None:
            source_p = c_void_p(datas.ctypes.data)
            self.lib.loaddatabase(source_p, datacount, inputcount)      

        if targets is not None:
            self.targets = targets
        if propertyName is not None:
            self.propertyName = propertyName
        
    def Jacobian2long(self, weights=None):    # DriverLib  #, inputs=None, model=None
        """Mise en forme pour les routines d'optimisation.
        Calcule et retourne les sorties et le jacobien du modèle.
        Si le modele est un multimodel parallel, inputs est None, et model est le multimodel.
        Sinon, inputs est la matrice des entrées proposées sur chaque ligne, et model est le modele.
        """
        if weights is None:
            weights = self.weights
        return self.getjacobian(weights, style=2)
    
    def setIdentifiers(self, idlist, datacount=-1): # DriverLib
        res = 0
        if not hasattr(self.lib, "setidentifier"):
            return -1
        if not len(idlist) and datacount > 0:
            idlist = ["data_{0}".format(ind) for ind in range(datacount)]
        for index, val in enumerate(idlist):
            if PY3:
                try:
                    value = val.encode("utf-8")
                except AttributeError:
                    value = str(val).encode("utf-8")
            else:
                value = str(val)
            rtyp = c_char_p(value)
            resloc = self.lib.setidentifier(index, rtyp)
            res |= resloc
        return res
#         if res: 
#             raise LibraryManagerError("getNames error : %s"% res)

    def loadTrainingDataFromArray(self, source, baselen=-1, linelen=-1): # DriverLib
#         def extendList(a, b):
#             a.extend(b)
#             return a
        
        if isinstance(source, ndarray):
            ss = asarray(source.flatten(), npdouble)
            if baselen < 0:
                baselen = source.shape[0]
            if linelen < 0:
                linelen = source.shap[1]
        else:
            if isinstance(source, list) and isinstance(source[0], list):
                if baselen < 0:
                    baselen = len(source)
                if linelen < 0:
                    linelen = len(source[0])
                source = concatenateList(source)
                #reduce(extendList, source)
                
#                 for ind, vlist in enumerate(source):
#                     if not ind:
#                         lst = vlist.copy()
#                     else:
#                         lst.extend(vlist)
#                 source = lst
            try:
                ss = asarray(source, npdouble)
            except:
                ss = asarray(asarray(source).flatten(), npdouble)
#         if isinstance(source, list):
#             if len(source) == 2:
#                 fullsource = source[0].append(source[1])
#                 source = fullsource
#             base = len(source[0])
#             size  = len(source[0][0])
#         else:
#             base, size = source.shape
#         if baselen < 0:
#             baselen = base
#         if linelen < 0:
#             linelen = size
        source_p = c_void_p(ss.ctypes.data)
        return self.lib.loaddatabase(source_p, baselen, linelen)
    
    def loadTrainingDataFromFrame(self, dataFrame, inputCount=-1, outputCount=-1):
        noindex = False
        idname = dataFrame.index.name
        if idname is None:
            noindex = True
            idname = 'index'
        cols = [val.lower() for val in dataFrame.columns]
        coltypes = dataFrame.dtypes
        datacount, colcount = dataFrame.shape
        decal = 0
        lin = 0
        lout = 0
        smilesindex = -1
        if 'smiles' in cols:
            smilesfields = dataFrame.fieldsOf('smiles') 
            decal = len(smilesfields)
            smilesindex = cols.index('smiles')
        if 'inputs' in cols or 'outputs' in cols:
            if 'inputs' in cols:
                infields = dataFrame.fieldsOf('inputs')
                inindexes = dataFrame.indexesOf('inputs')
                lin = len(infields)
            if 'outputs' in cols:
                outfields = dataFrame.fieldsOf('outputs')
                outindexes = dataFrame.indexesOf('outputs')
                lout = len(outfields)
            datas = dataFrame._frame.iloc[:, inindexes+outindexes]
            source = asarray(datas, npdouble).flatten()
            #source = asarray(asarray(dataFrame._frame).iloc[:, inindexes+outindexes].flatten(), npdouble)
            pptyname = outfields[0]
            linelen = lin+lout
        elif outputCount >= 0 and inputCount >= 0 and colcount > inputCount+outputCount:
            pptyname = cols[-1]
            datas = dataFrame._frame.iloc[:, :inputCount + outputCount]
            source = asarray(datas, npdouble).flatten()
            linelen = datas.shape[1]  #inputCount
        else:
            pptyname = cols[-1]
            usecol = [ind for ind, _ in enumerate(dataFrame.columns) if ind != smilesindex]
            datas = dataFrame._frame.iloc[:,usecol]
            source = asarray(datas, npdouble).flatten()
            linelen = datas.shape[1]
        source_p = c_void_p(source.ctypes.data)
        self.lib.loaddatabase(source_p, datacount, linelen)
        # ajouter le chargement des identificateurs 
        self.propertyName = pptyname
        if not noindex:
            self.setIdentifiers(list(dataFrame.index), datacount)
        return datacount, colcount - decal
                 
        
    def loadTrainingData(self, options=None, filename="", filetype="", datarange="", datafields=[], grouplist=[]):
        if (options is None) and not filename: return
        if options is not None:
            filename = options.source
            filetype = options.filetype
            datarange = options.datarange
            datafields = options.datafields
            grouplist = options.grouplist
        datafmt = []
        #for datades in ['inputs', 'outputs']:
        for datades in grouplist:
            datafmt.extend(datafields[grouplist.index(datades)])
        datasource = DataSource(filename, filetype=filetype, datarange=datarange,
            datafmt=datafmt, titles=True)
        values = []
        smiles = []
        ids = []
        datacount = 0
        lid = len(datafields[grouplist.index('identifiers')]) if 'identifiers' in grouplist else 0
        lsmi = len(datafields[grouplist.index('smiles')]) if 'smiles' in grouplist else 0
        lin = len(datafields[grouplist.index('inputs')]) if 'inputs' in grouplist else 0
        lout = len(datafields[grouplist.index('outputs')]) if 'outputs' in grouplist else 0
        for ind, row in enumerate(datasource.source.iterData(datarange=datarange, datafmt=datafmt)):
            if not ind and not isNum(row[-1]):
                continue
            ids.extend(row[:lid])
            smiles.extend(row[lid:lid+lsmi])
            values.extend(row[lid+lsmi:])
            datacount += 1
        datasize = lin + lout
        values = [floatEx(val) for val in values]
        source = asarray(values, npdouble)
        source_p = c_void_p(source.ctypes.data)
        self.lib.loaddatabase(source_p, datacount, datasize)
        if options is not None:
            options.datacount = datacount
            options.datasize = datasize
        # ajouter le chargement des identificateurs 
        self.setIdentifiers(ids, datacount)
        pass        
        
    def loadParameters(self, source):  # DriverLib
        if source is None: return
        if isinstance(source, dict):
            return self.loadFromDict(source)
        elif isinstance(source, str):
            #chargement binaire
            res = False
            with load(source) as sourceopen:
                res = self.loadFromDict(sourceopen)
            if not res:  #self.loadFromDict(load(source)):  #loadWeightsBinary(source):
                # chargement ASCII    
                if not self.loadWeightsASCII(source, self):
                    # chargement XML
                    self.loadWeightsXML(source, self)
        else:
            self.weights = source
#         elif isinstance(source, (list, ndarray)):
#             source = source.copy()
#             if self.weights is None:
#                 self.weights = asarray(source)
#             # chargement d'un vecteur
#             else:
#                 self.weights = source
                    
    def setcallback(self, cbFunc):  # DriverLib 
        """setcallback(cbFunc)
        Installation and uninstallation of the callback function.
        params:
            cbFunc -> Callback function to install. 
                C parameters: (double, long)
                return long
            For uninstallation, this parameter will be "None" 
        """
        self._callback = cbFunc
        if cbFunc:
            curcallback = proxy(cbFunc)
        # definition du type de fonction de callback, conforme a l'attente de la DLL
        # les fonctions de callback sont toujours de type "cdecl"
            self._callbacktype = CFUNCTYPE (c_int, c_double, c_int)#
        # L'enregistrement de la reference "_callback" permet de garder la
        # fonction de callback vivante malgre le garbage collector.
            self._callbacklib = self._callbacktype(curcallback)
        else:
            self._callbacklib = None
        return self.lib.setcallback(self._callbacklib)
    
# #     
# #     @property
# #     def SVDCount(self):
# #         try:
# #             return self.lib.getsvdcount()
# #         except Exception:
# #             return 0
# #     

    @Property
    def trainingResults(self):
        try:
            return self._trainingResults
        except:
            return None
        
#     @property
#     def bestList(self):
#         return self._bestList
    
#     @Property
#     def baseLen(self): # DriverLib
#         try:
#             return self.lib.baselen()
#         except:
#             return 0
#     
#     @Property
#     def dataCount(self): # DriverLib
#         try:
#             return self.lib.dataCount()
#         except:
#             return 0
#     modelCount = dataCount
#     
    @Property
    def modelCount(self):
        return 1
    
    @Property
    def paramNames(self, index): # DriverLib
        return self.getNames(2, index)
    @paramNames.lengetter
    def paramNames(self): # DriverLib
        return self.paramCount
    
    @Property
    def modelNames(self, index): # DriverLib
        return self.getNames(0, index)
    @modelNames.lengetter
    def modelNames(self): # DriverLib
        return self.dataCount
    
    @Property
    def smiles(self, index): # DriverLib
        return self.getNames(1, index) 
    @smiles.lengetter
    def smiles(self): # DriverLib
        return self.modelCount
    
    @Property
    def trainingData(self, index):  # DriverLib
        return self.traindatas()[index]
    @trainingData.lengetter
    def ltrainingData(self):  # Driver
        return self.dataCount
    
    def getTrainingData(self):
        return self.traindatas()
        
    def traindatas(self): # DriverLib
        result = self.fullData
        result.shape = (self.lib.baselen(), self.lib.inputCount())
        return result
    
    @Property
    def fullData(self):
        length = self.lib.getdata(-1, None)
        target = zeros((length,))
        target_p = c_void_p(target.ctypes.data)
        self.lib.getdata(-1, target_p)
        return target
    
#     @Property
#     def trainingData(self, index):
#         length = self.lib.getdata(index, None)
#         target = zeros((length,))
#         target_p = c_void_p(target.ctypes.data)
#         self.lib.getdata(index, target_p)
#         return target
#      
#     @trainingData.lengetter
#     def trainingData(self):
#         return self.lib.baselen()
    
#     @Property
#     def inputs(self, index):
#         length = self.lib.inputCount()
#         target = zeros((length,))
#         target_p = c_void_p(target.ctypes.data)
#         self.lib.getdata(index, target_p)
#         return target
#     
#     @inputs.lengetter
#     def inputs(self):
#         return self.lib.inputCount()
#     
    def gettargets(self):#pour compatibilite
        return self.targets
    
    def settargets(self, values, nonorm=0): # DriverLib
        try:
            source = asarray(values, npdouble)
            source_p = c_void_p(source.ctypes.data)
            res = self.lib.settargets(source_p, int(nonorm))
        except:
            res = 0
        if res < 0: 
            raise DriverLibError(self.lasterror)
    
    @Property
    def targetsmem(self): # DriverLib
        try:
            dim = self.lib.gettargets(0, None)
            target = zeros((dim,), dtype=npdouble)
            target_p = c_void_p(target.ctypes.data)
            res = self.lib.gettargets(-2, target_p)
            if res < 0: 
                raise DriverLibError(self.lasterror)
        except:
            target = None
        return target
            
    @Property
    def targets(self): # DriverLib
        try:
            dim = self.lib.gettargets(-1, None)
            target = zeros((dim,), dtype=npdouble)
            target_p = c_void_p(target.ctypes.data)
            res = self.lib.gettargets(-1, target_p)
            if res < 0: 
                raise DriverLibError(self.lasterror)
        except:
            target = None
        return target
            
    @targets.setter
    def stargets(self, value): # DriverLib
        self._targetfile = ""
        source = None
        if isinstance(value, str) and os.path.exists(value):
            self._targetfile = value
            with open(value, "r") as ff:
                lines = ff.readlines()
                lst0 = [val for val in lines]
                val0 = lst0[0]
                lst = [floatEx(val) for val in lst0]
                if isnan(lst[0]):
                    lst = lst[1:]
                    pptyname = val0
                else:
                    pptyname = os.path.basename(value)
                source = asarray(lst, npdouble)
                self.propertyName = pptyname 
        else:  
            try:
                source = asarray(value, npdouble)
            except: 
                res = -1
#              ValueError:
#             source = None
#             if os.path.exists(value):
#                 self._targetfile = value
#                 with open(value, "r") as ff:
#                     lines = ff.readlines()
#                     lst = [floatEx(val) for val in lines]
#                     source = asarray(lst, npdouble)
#                     self.propertyName = os.path.basename(value)
        if source is not None:
            source_p = c_void_p(source.ctypes.data)
            res = self.lib.settargets(source_p, 0)
        if res < 0: 
            raise DriverLibError(self.lasterror)
        
    def getlastresiduals(self, curw=None, outputs=None):  # DriverLib
        outputs = outputs if outputs is not None else self._outputs
        val = self.targets - outputs
        return val
    
    def getresiduals(self, params=None, style=0): # DriverLib
        if params is not None:
            params = asarray(params)
        else:
            if self.weights is not None:
                params = self.weights
        if params is not None:
            self._lastweights = params.copy
        else:
            raise DriverLibError("params sould not be null in getresiduals")
        try:
            dim = self.lib.getresiduals(None, 0, None)
            source = asarray(params, npdouble)
            source_p = c_void_p(source.ctypes.data)
            target = zeros((dim,), dtype=npdouble)
            target_p = c_void_p(target.ctypes.data)
            res = self.lib.getresiduals(source_p, style, target_p)
            if res < 0: 
                raise DriverLibError(self.lasterror)
        except:
            target = None
        return -target
    
    def freedom(self, index=0):  # DriverLib
        return self.lib.getfreedomindex(index)
    
    def transferICindex(self, params=None, index=-1, trainingStdDev=None, disp=None, acc=0.95):  # DriverLib
        out, leverage = self.transferleverageindex(params, index, False, disp)
        stddev = trainingStdDev if trainingStdDev is not None else self.trainingStddev
        df = self.freedom(index)
        #inter = interval(acc, df)
        if leverage >= 0:
            coeff = stddev * math.sqrt(leverage)
        else:
            coeff = 0
        IC =  interval(acc, df)[1] * coeff
        return out, IC
    
    def transferleverageindex(self, params=None, index=-1, removeindex=False, disp=None):
        if disp is None:
            disp = self._dispersionMatrix
        out, gradient = self.transfergradientindex(params, index=index)
        lev = npdot(npdot(gradient.T, disp), gradient)
        return out, lev
    
    def transferindex(self, params=None, index=-1):
        if isinstance(params, text_type) and (params == 'extra'):
            return [self.transferindex(param, index) for param in self._extraweights]
        if params is not None:
            params = asarray(params, npdouble)
        else:
            if self.weights is not None:
                params = self.weights
        if params is None:
            if self.weights is not None:
                params = self.weights
        if params is not None:
            self._lastweights = params.copy
            params = asarray(params, npdouble)
        else:
            raise DriverLibError("params sould not be null in transferindex")
         
        out = None
        try:
            source = params.copy()
            source_p = c_void_p(source.ctypes.data)
            out = zeros((1,), dtype=npdouble)
            out_p = c_void_p(out.ctypes.data)
            res = self.lib.transferindex(index, source_p, out_p)
            if res < 0: 
                raise DriverLibError(self.lasterror)
             
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
        if params is None:
            if self.weights is not None:
                params = self.weights
        if params is not None:
            self._lastweights = params.copy
            params = asarray(params, npdouble)
        else:
            raise DriverLibError("params sould not be null in transfergradientindex")
         
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
                raise DriverLibError(self.lasterror)
             
        except: pass
        if self.outputCount ==1:
            out = out[0]
        return out, gradient
    
#     def transfer(self, inputs=None, params=None): # DriverLib
#         # inputs must be an np.array, type np.double
#         if isinstance(params, str) and (params == 'extra'):
#             return [self.transfer(inputs, param) for param in self.extraweights]
#         if params is not None:
#             params = asarray(params, npdouble)
#         else:  # not isinstance(params, str):
#                 params = self.weights
#             if self.weights is not None:
    
    def transfer(self, inputs=None, style=C.TFR_STD, params=None, **kwds):
        # inputs must be an np.array, type np.double
        indexmove = kwds.get('indexmove', -1)
        indexlist = kwds.get('indexlist', None)
        if (inputs is not None) and (indexmove >= 0) and (indexlist is not None):
            res = [self.transfer(insertInList(inputs, value, indexmove), style, params) for value in indexlist]
#             res = [0] * len(indexlist)
#             for ind, value in enumerate(indexlist):
#                 #inputs[indexmove] = value
#                 res[ind] = self.transfer(insertInList(inputs, value, indexmove), style, params)
            
            return res
        
        if style == C.TFR_GRADIENT:
            return self.transfergradient(inputs, params, **kwds)
        if style == C.TFR_LEVERAGE:
            disp = kwds.get('dispersion', None)
            return self.transferleverage(inputs, params, disp, **kwds)
        if style != C.TFR_STD:
            raise NotImplementedError
        index = kwds.get('index', -1)
        if index >= 0:
            return self.transferindex(params, index)
        
        if isinstance(params, str) and (params == 'extra'):
            return [self.transfergradient(inputs, param) for param in self.extraweights]
        if params is None:
            if self.weights is not None:
                params = self.weights
        if params is not None:
            self._lastweights = params.copy
            params = asarray(params, npdouble)
        if inputs is not None:
            inputs = asarray(inputs)
        try:
            param_p = None if params is None else c_void_p(params.ctypes.data)  #.copy()
#             if params is None:
#                 param_p = None
#             else:
#                 param = params.copy()
#                 param_p = c_void_p(param.ctypes.data)
            inp_p = c_void_p(inputs.ctypes.data)
            out = zeros((self.outputCount,), dtype=npdouble)
            out_p = c_void_p(out.ctypes.data)
            res = self.lib.transfer(inp_p, param_p, out_p)
            if not res:
                if self.outputCount ==1:
                    out = out[0]
            else:
                out = None
        except Exception as err:
            out = None
        return out
    
    def transferEx(self, inputs=None, withCI=0, modelindex=-1):
#         if (self.weights is not None) and (len(self.weights) > self.paramCount):
#             self.mainModel.weights = self.weights
        outs = []
        levs = []
        stds = []
        CIp = []
        CIm = []
        if (self._extraweights is None) or (self._extradispersions is None):
#             out, lev = self.transferLeverages(inputs=inputs)  #original=original
#             out, grad = self.transfergradient(inputs=inputs)
            out, lev = self.transferleverage(inputs=inputs)  #original=original
            outs.append(squeeze(out))
            levs.append(squeeze(lev))
        else:
            if self._extrastddev is None:
                extrastddev = [0 for _ in range(len(self._extraweights))]
            else:
                extrastddev = self._extrastddev
            if 0 <= modelindex < self.extraCount:
                try:
                    weight = self._extraweights[modelindex] 
                    disp = self._extradispersions[modelindex]
                    std = extrastddev[modelindex]
                    out, lev = self.transferLeverages(inputs, weight, disp) 
                    outs.append(out.squeeze())
                    levs.append(lev.squeeze())
                    stds.append(std.squeeze())
                except AttributeError:
                    raise
            else:     
                try:
                    for weight, disp, std in zip(self._extraweights, self._extradispersions, extrastddev):
                        out, lev = self.transferLeverages(inputs, weight, disp)  
                        outs.append(out.squeeze())
                        levs.append(lev.squeeze())
                        try:
                            stds.append(std.squeeze())
                        except AttributeError:
                            stds.append(std)           
                except AttributeError as err:
                    raise
        if not withCI:
            return outs, levs
        students = [self._studentvariable for _ in range(len(outs))] 
        if withCI == 1:
            return outs, levs, stds, students
        for out, lev, std in zip(outs, levs, stds):
            ic = sqrt(lev)*self._studentvariable*std
            CIp.append(out + ic)
            CIm.append(out - ic)
        return outs, CIp, CIm, levs
    
    def transfergradient(self, inputs=None, params=None, **kwds):
        if isinstance(params, str) and (params == 'extra'):
            return [self.transfergradient(inputs, param) for param in self.extraweights]
        if params is not None:
        # inputs must be an np.array, type np.double
            params = asarray(params, npdouble)
        elif self.weights is not None:
                params = self.weights
#         if params is not None:
#             self._lastweights = params.copy
        try:
            param = None if params is None else params.copy()
            self._lastweights = param
            param_p = None if param is None else c_void_p(param.ctypes.data)
            inp_p = c_void_p(inputs.copy().ctypes.data)
            out = zeros((self.outputCount,), dtype=npdouble)
            out_p = c_void_p(out.ctypes.data)
            grad = zeros((self.paramCount,), dtype=npdouble)
            grad_p = c_void_p(grad.ctypes.data)
            res = self.lib.transfergradient(inp_p, param_p, out_p, grad_p)
            if self.outputCount ==1:
                out = out[0]
        except:
            out = grad = None
        return out, grad
    
    def transferleverage(self, inputs=None, params=None, disp=None, **kwds):
        if isinstance(params, text_type) and (params == 'extra'):  #
            return [self.transferleverage(inputs, param, disper) for param, disper in zip(self.extraweights, self.extradispersions)]
        if params is not None:
            params = asarray(params, npdouble)
        else:
            if self.weights is not None:
                params = self.weights
        if params is not None:
            self._lastweights = params.copy
#         else:
#             raise DriverLibError("params sould not be null in transfergradientindex")
        lev = NaN
        try:
            param = None if params is None else params.copy()
            param_p = None if param is None else c_void_p(param.ctypes.data)
            inputs = inputs.copy()
            inp_p = c_void_p(inputs.ctypes.data)
            disper = None if disp is None else disp.copy()
            disper_p = None if disp is None else c_void_p(disper.ctypes.data)
            out = zeros((self.outputCount,), dtype=npdouble)
            out_p = c_void_p(out.ctypes.data)
            lev_p = c_double(lev)
            res = self.lib.transferleverage(inp_p, param_p, disper_p, out_p, byref(lev_p))
            lev = lev_p.value
            if self.outputCount ==1:
                out = out[0]
        except Exception as err: 
            out = lev = NaN
        return out, lev
            
    def getjacobian(self, params=None, style=0): # DriverLib
        if params is not None:
            params = asarray(params)
        else:
            if self.weights is not None:
                params = self.weights
        if params is not None:
            self._lastweights = params.copy
        else:
            raise DriverLibError("params sould not be null in getjacobian")
        #dim = self.lib.get residuals(None, 0, None, None)
        try:
            modelCount = self.lib.dataCount()
            paramCount = self.lib.paramCount()
            source = asarray(params, npdouble)
            source_p = c_void_p(source.ctypes.data)
            target = zeros((modelCount*paramCount,), dtype=npdouble)
            target_p = c_void_p(target.ctypes.data)
            out = zeros((modelCount,), dtype=npdouble)
            out_p = c_void_p(out.ctypes.data)
            
            res = self.lib.getjacobian(source_p, style, target_p, out_p) 
            
            if res < 0: 
                raise DriverLibError(self.lasterror)
            target2 = reshape(target, (modelCount, paramCount))
            target2 = target2[:self.baseLen]
#             ll = self.get dirlen()
#             if 0 < ll < self.modelCount:
#                 target2 = target2[:ll]
        except:
            out = None
            target2 = None
        if style:
            return out, target2
        return target2

    def getTrainType(self):
        return self.lib.gettraintype()
    
    def getStdDev(self, params=None, trainstyle=0, **kwds):
        return self.getCost(params, True, True, trainstyle)
    
    def getCost(self, params=None, donorm=False, root=False, trainstyle=-1, **kwds): # DriverLib  
        """Cost computation.
        params -> model parameters to be used. If None, current weights are used
        donorm -> result normalisation with the data count
        root -> extract the resjult square root (return stdDev)
        trainstyle -> style of cost computation. -1 keep the current trainstyle.
            see CS_xxx constants in monalconst module.
        """
        iparams = None
        if params is not None:
            iparams = asarray(params, npdouble)
        else:
            if self.weights is not None:
                iparams = asarray(self.weights, npdouble)
        if iparams is not None:
            self._lastweights = iparams.copy
        else:
            raise DriverLibError("params sould not be null in getCost")
        try:
            if trainstyle >= 0:
                trainstylemem = self.setTrainStyle(trainstyle)
            dim = self.lib.getcost(None, None)
            source_p = c_void_p(iparams.ctypes.data)
            target = zeros((dim,), dtype=npdouble)
            target_p = c_void_p(target.ctypes.data)
            res = self.lib.getcost(source_p, target_p)
            if res < 0: 
                raise DriverLibError(self.lasterror)
            if donorm:
                target /= self.lib.dataCount()
            if root:
                target = sqrt(target);
        except Exception as err:
            target = None
        finally:
            if trainstyle >= 0:
                self.setTrainStyle(trainstylemem)
        if dim == 1:
            target = target[0]
        return target
        
    def setTrainStyle(self, style):
        return self.lib.settrainstyle(c_int(style))
        
    def getTrainStyle(self):
        return self.lib.gettrainstyle()
    
    def getPRESS(self, params=None, donorm=False, root=False, full=False, 
                 trainstyle=0):
        iparams = None
        if params is not None:
            iparams = asarray(params)
        else:
            if self.weights is not None:
                iparams = self.weights
        if iparams is not None:
            self._lastweights = iparams.copy
        else:
            raise DriverLibError("params sould not be null in getPRESS")
        try:
            svdlen = 0
            if trainstyle >= 0:
                stylemem = self.setTrainStyle(trainstyle)
            else:
                trainstyle = self.getTrainStyle()
            #trainstyle = 0 #C.CS_MODERATE #| C.CS_LIMITED_LEVERAGE
            deltash = 0.0
            if full:
                ZMat = zeros((self.paramCount*self.paramCount,), dtype=npdouble)
                ZMat_p = c_void_p(ZMat.ctypes.data) 
                leverages = zeros((self.lib.baselen(),), dtype=npdouble)
                leverages_p = c_void_p(leverages.ctypes.data)
                residuals = zeros((self.lib.baselen(),), dtype=npdouble)
                residuals_p = c_void_p(residuals.ctypes.data)
                singular = zeros((self.paramCount,), dtype=npdouble)
                singular_p = c_void_p(singular.ctypes.data)
            else:
                ZMat_p = None
                leverages_p = None
                residuals_p = None
                singular_p = None
            svdlen_p = c_long(svdlen)
            deltash_p = c_double(deltash)
            dim = self.lib.outputCount()
            source = iparams  #asarray(iparams, npdouble)
            source_p = c_void_p(source.ctypes.data)
            press = zeros((dim,), dtype=npdouble)
            press_p = c_void_p(press.ctypes.data)
            
            if CC.__version__ >= 21:
                res = self.lib.getpress(source_p, press_p, residuals_p,
                singular_p, leverages_p, ZMat_p, byref(deltash_p), 
                c_int(trainstyle), byref(svdlen_p))  # getpress
            else:
                res = self.lib.getpress(source_p, press_p, residuals_p,
                singular_p, leverages_p, ZMat_p, byref(svdlen_p))  # getpress
            if res < 0: 
                raise DriverLibError(self.lasterror)
            if donorm:
                press /= self.lib.baselen()
            if root:
                press = sqrt(press)
            residuals = -residuals
        except Exception as err:
            print(err)
            press = None
        finally:
            if trainstyle >= 0:
                self.setTrainStyle(stylemem)
        if dim == 1:
            press = press[0]
        if full:
            disp = ZMat.reshape(self.paramCount, self.paramCount)
            return press, residuals, singular, leverages, disp, svdlen_p.value, deltash_p.value
                
        return press

    def getprime(self, params=None, style=0):  # DriverLib
        if params is not None:
            params = asarray(params)
        else:
            if self.weights is not None:
                params = self.weights
        if params is not None:
            self._lastweights = params.copy
        else:
            raise DriverLibError("params sould not be null in getprime")
        dim = self.lib.prime(None, style, None)
        source = asarray(params, npdouble)
        source_p = c_void_p(source.ctypes.data)
        target = zeros((dim,), dtype=npdouble)
        target_p = c_void_p(target.ctypes.data)
        res = self.lib.prime(source_p, style, target_p)
        if res < 0: 
            raise DriverLibError(self.lasterror)
        return target
                    
    @Property
    def director(self):  # DriverLib
        dim = self.lib.getdirector(0)  #None
        target = zeros((dim,), dtype=npint)
        target_p = c_void_p(target.ctypes.data)
        res = self.lib.getdirector(target_p)
        if res < 0: 
            raise DriverLibError(self.lasterror)
        return target
    @director.setter
    def director(self, values):  # DriverLib
        values = list(values)
        if len(values) < self.modelCount:
            values.append(-1)  # modif 14/12/17 'values =' supp
        source = asarray(values, npint)
        source_p = c_void_p(source.ctypes.data)
        res = self.lib.setdirector(source_p)
        if res < 0: 
            raise DriverLibError(self.lasterror)
    
    def initWeights(self, stddev=0.3, bias0=True, seed=None, **kwds):
        if seed is not None:
            self.setRandSeed(seed)
        weights = self.newWeights(stddev=stddev, bias0=bias0)
        self.weights = weights
    
    def newWeights(self, stddev=0.3, bias0=True, doinit=True):  # DriverLibMulti
        if not doinit:
            return self.weights
        if bias0:
            lst = self.biasbased
        else:
            lst = []
        return asarray(self.getNewWeights(stddev, lst))
    
    def settrainingset(self, style=0, index=0, residuals=None):  # DriverLib
        if (residuals is None) or (style == 2):
            source_p = None
        else:
            source = asarray(residuals, float)
            source_p = c_void_p(source.ctypes.data)
        res = self.lib.settrainingset(style, index, source_p)
        if res < 0: 
            raise DriverLibError(self.lasterror)
        return res
                
    def multitrain(self, # DriverLib
            initcount=1, 
            epochs=100, 
            initweights=None, 
            weightsstddev=0.3, 
            seed=None, 
            style=C.TR_S_STD, # 0
            substyle=0, 
            writer=sys.stdout,
            onEndIter=None, 
            onReturnResult=None, 
            trainstyle=0, 
            maxworkers=-2, 
            parallel=True,
            callback=callbackmin,
            **kwds): 
        
        parallel = True  # !!! ATTENTION  mettre a True!!!
        """multitrain(initcount=1, epochs=0, algo="LM_INTEGRATED", initweights=None,
                   seed=-1, callback=None, criterion=C.TCR_COST)  debugfile=None, 
        
        Lancement de plusieurs séquences d'apprentissage
        """
        max_workers = maxWorkers(maxworkers)
        do_DEBUG_TRAIN = (trainstyle & C.CS_DEBUG)  
        if do_DEBUG_TRAIN:
            print("startweights", initweights)
        do_parallel = (parallel and 
                    USE_PARALLEL_MAIN and 
                    (initcount > 1) and 
                    (max_workers > 0) and 
                    not do_DEBUG_TRAIN)
        if not do_parallel:
            # ProcessPoolExecutor ne sait pas gerer ce callback
            self.setcallback(callback)
        self.leverages = None
        self.stoptrain = 0 
        self.cumulEpoch = 0
        if epochs <= 0:
            epochs = 100*(1 + self.paramCount)
        self.setRandSeed(seed)
        if writer is not None and self.isLinear:
            writer.write("Current model is linear.\n")
        if initweights is not None:
            self.loadParameters(initweights)
        else:
            self.weights = self.newWeights(weightsstddev, 
                doinit=(self.weights is None) or (style & C.TR_S_INIT_PARAM))        
        self.memWeights = self.weights.copy()
            
        #self._trainingResults = zeros((initcount, C.TCR_COUNT))
        self._dispersionMatrix = None
        self._conditionning = None
        self._stdtrain = 0
        muststop = 0
        
        # ici on sépare la boucle d'apprentissage en deux boucles.
        # la boucle 1 procede a l'apprentiisage proprement dit, et met en mémoire les résultats
        # la boucle 2 enregistre les resultats        
        #winit = [self.weights.copy()] + [self.newWeights(weightsstddev) for _ in xrange(initcount-1)]
        stylemem = self.setTrainStyle(trainstyle)
        if no_parallel_seed:
            sel = seedList(seed, initcount)
        else:
            sel = [seed for _ in range(initcount)]
            
        fullresults = []
        if do_parallel:
        # traitement en parallele
            with cf.ProcessPoolExecutor(max_workers=max_workers) as executor:  # multitrainNew
                futures = [executor.submit(trainJob, self, 
                                    weightsstddev, 
                                    epochs, 
                                    True,
                                    ind, 
                                    sed) for ind, sed in enumerate(sel)] 
#                                     seed) for ind in range(initcount)] 
 
                for indloc, future in enumerate(cf.as_completed(futures)):
                    res0, res1, res2 = future.result()
                    ind, cur, locepochs, stddev, startweights, trainend, history, locseed, _ = res0
                    resvec = res2
                    self.stoptrain = (onEndIter and onEndIter(history, trainend, ind, indloc, locepochs))
                    if (cur is not None) and not self.stoptrain:
                        self._lastweights = cur.copy()
                    fullresults.append((indloc, res0, res1, res2))
                    if self.stoptrain:
                        break
                if self.stoptrain:
                    for future2 in futures:
                        future2.cancel()
        else:  # traitement en serie
            for indloc in range(initcount):
                res0, res1, res2 = trainJob(self, 
                        weightsstddev, 
                        epochs, 
                        True, 
                        indloc, 
                        seed)        
                ind, cur, locepochs, stddev, startweights, trainend, history, locseed, _ = res0
                self.stoptrain = (onEndIter and onEndIter(history, trainend, ind, indloc, locepochs))
                if (cur is not None) and not self.stoptrain:
                    self._lastweights = cur.copy()
                fullresults.append((indloc, res0, res1, res2))
                if self.stoptrain:
                    break 
        self.setTrainStyle(stylemem)
        nfail = 0
        for res in fullresults:
            indloc = res[0]
            ind, cur, locepochs, stddev, startweights, trainend, \
                history, locseed, code = res[1]  
            if res[2] is None:
                r2 = (None, None, None, None, None, None, None, None, None)
            else:
                r2 = res[2]
            press, residuals, singular, leverages, disp, svdlen, deltash, \
                outputs, jacobians = r2  #
            resvec = res[3]
            if cur is None:
                nfail += 1
                print ("fail", indloc)
                # que faire ici ???
            else: 
                self._lastweights = cur.copy()
                self._outputs = outputs
                self._jacobians = jacobians
                self._stdtrain = stddev #math.sqrt(stddev/self.modelCount)
                self._dispersionMatrix = disp
                self.actualepochs = locepochs
                self.cumulEpoch += locepochs
                
                if onReturnResult:
                    # dbConnect, tablename, indcur, resultvector, startweights, endweights, leverages, dispersion, history
                    restrain = onReturnResult(ind, resvec, startweights, cur, leverages, disp, history, locseed)
            
        if do_DEBUG_TRAIN:
            print("EndWeights", self.weights)
        return nfail
    
    def kerneltrainintegratedmain(self, weights, maxiter, withhistory=False, index=-1):
        assert weights is not None
        assert maxiter 
        code = 0
        mem = weights.copy()
        try:
            res = self.train_integrated(weights, epochs=maxiter, withhistory=withhistory)[0]
            cur, N, stddev, trainend, hist, code = res  
            if withhistory:
                history = sqrt(hist / self.dataCount)
            else:
                history = None  
        except Exception as exres:
            N = -1
            stddev = 0.0
            cur = None
            print("DriverLib.train", exres)
            if not code:
                code = -1
            return cur, N, stddev, None, None, None, None, None, code
        #self.setdebugfile("")
        resvec = None
        disp = None
        if code:
            cur = None
            stddev = 0.0
        else:
            self.actualepochs = N
            if C.USE_INTEGRATED_LEVERAGE:
                resvec = self.computeTrainingResultsIntegrated(curw=cur) 
            else:
                resvec = self.computeTrainingResultsOld(curw=cur) 
#             resvec = self.computeTrainingResults(curw=cur) 
            disp = self._dispersionMatrix.copy() 
             
        return cur, N, stddev, mem, trainend, resvec, disp, history, code
        
    def core_train2(self, weights, maxiter, withhistory=False, index=-1):
        assert weights is not None
        assert maxiter 
        #resvec = disp = None
        code = 0
        mem = weights.copy()
        try:
            res = self.train_integrated(weights, epochs=maxiter, withhistory=withhistory)[0]
            cur, N, stddev, trainend, hist, code = res  
            if withhistory:
                history = sqrt(hist / self.dataCount)
            else:
                history = None  
        except Exception as exres:
            N = -1
            stddev = 0.0
            cur = None
            print("DriverLib.train", exres)
            if not code:
                code = -1
            return index, cur, N, stddev, None, None, None, code
        if code:
            cur = None
            stddev = 0.0
        return index, cur, N, stddev, mem, trainend, history, code
        
    def core_train(self, weights, maxiter, withhistory=False, index=-1):
        assert weights is not None
        assert maxiter 
        #resvec = disp = None
        code = 0
        memweights = weights.copy()
        try:
            res = self.train_integrated(weights, epochs=maxiter, withhistory=withhistory, computeDispersion=True)
            cur, N, stddev, trainend, hist, code = res[0] 
            if withhistory:
                history = sqrt(hist / self.dataCount)
            else:
                history = None  
        except Exception as exres:
            N = -1
            stddev = 0.0
            cur = None
            print("DriverLib.train", exres)
            if not code:
                code = -1
            return index, cur, N, stddev, None, None, None, code
        if code:
            cur = None
            stddev = 0.0
            
        res0 = (index, cur, N, stddev, memweights, trainend,  history, code)
        #target, residuals, singular, leverages, disp, svdlen, deltash, outputs, jacobians = res[1]  #
        #resvec = res[2] 
        return res0, res[1], res[2]
        
    def kerneltrainintegratedmain3(self, weights, maxiter, withhistory=False, index=-1):
        assert weights is not None
        assert maxiter 
        code = 0
        memweights = weights.copy()
        try:
            res = self.train_integratedex(weights, epochs=maxiter, withhistory=withhistory)
            cur, N, stddev, press, residuals, leverages, disp, jacob, trainend, deltash, svdlen, singular, hist, code = res
            NN = self.dataCount
            qq = self.paramCount
            disp = reshape(disp, (qq, qq))
            jacob = reshape(jacob, (NN, qq))
            #print "dispersion", disp.shape
            #print "jacob", jacob.shape
            if withhistory:
                history = sqrt(hist / self.dataCount)
            else:
                history = None  
        except Exception as exres:
            N = -1
            stddev = 0.0
            cur = None
            print("DriverLib.trainex", exres)
            if not code:
                code = -1
            return index, cur, N, stddev, None, None, None, None, None, None, None, None, None, None, None, code
        if code:
            cur = None
            stddev = 0.0
        return index, cur, N, stddev, press, memweights, residuals, leverages, disp, jacob, trainend, deltash, svdlen, singular, history, code
        
#     def aftertrain2(self, onEndIter, indloc, ind, cur, locepochs, 
#                    stddev, startweights, trainend, history, code):  #resvec, disp, history, code):
#         """Action apres apprentissage, a l'interieur de la boucle d'exploitation des jobs paralleles
#         """
#         muststop = (cur is None) or (onEndIter and onEndIter(history, trainend, ind, locepochs))
#         if not muststop:
#             if cur is None:
#                 outputs = None 
#                 jacobians = None
#             else:
#                 self._lastweights = cur.copy()
#                 outputs, jacobians = self.getjacobian(cur, style=2)
#                 self._stdtrain = math.sqrt(stddev/self.modelCount)
#         return muststop, indloc, ind, cur, locepochs, stddev, startweights, trainend, history, outputs, jacobians, code
        
    def aftertrain(self, indloc, ind, cur, locepochs, 
                   stddev, startweights, trainend, history, code): 
        """Action apres apprentissage, a l'interieur de la boucle d'exploitation des jobs paralleles
        """
        #self.stoptrain = (onEndIter and onEndIter(history, trainend, ind, locepochs))
        muststop = (cur is None) or self.stoptrain
        if not muststop: # and (cur is not None):
            self._lastweights = cur.copy()
        return muststop, indloc, ind, cur, locepochs, stddev, startweights, trainend, history, code 
        
    def train_integrated(self, params, epochs=-1, withhistory=False, 
            computeDispersion=False, trainstyle=-1):
        hist = None
        hist_p = None
        trainEnd = 0
        
        params = asarray(params, npdouble)
        params_p = c_void_p(params.ctypes.data)
        epoch_t = c_long(epochs)
        trainEnd_t = c_long(trainEnd)
        if withhistory:
            hist = zeros((epochs+1,))
            hist.fill(NaN)  # modif du 9/02/15
            hist_p = c_void_p(hist.ctypes.data)
        if trainstyle >= 0:
            trainstylemem = self.setTrainStyle(trainstyle)
        code = self.lib.train(params_p, byref(epoch_t), byref(trainEnd_t), hist_p)
        if trainstyle >= 0:
            self.setTrainStyle(trainstylemem)
        self.setWeights(params)
        if computeDispersion:
            resvec = self.computeTrainingResults(curw=params, actualepochs=epoch_t.value)
            respress = self.getPRESS(params, donorm=True, root=True, full=True)
            residuals = respress[1]
            stddev = sqrt((residuals**2).sum()/self.dataCount)
            outputs, jacobians = self.getjacobian(params, style=2)
            press, residuals, singular, leverages, disp, svdlen, deltash = respress
            resfull = (press, residuals, singular, leverages, disp, svdlen, deltash, outputs, jacobians)
        else:
            resfull = resvec = outputs = jacobians = None
            stddev = self.getStdDev(params)         
        trainEnd = trainEnd_t.value
        return (params, epoch_t.value, stddev, trainEnd, hist, code), resfull, resvec
        
#     def train_integratedOld(self, params, epochs=-1, withhistory=False, 
#             computeDispersion=False):
#         hist = None
#         hist_p = None
#         trainEnd = 0
#         
#         source = asarray(params, npdouble)
#         source_p = c_void_p(source.ctypes.data)
#         epoch_t = c_long(epochs)
#         trainEnd_t = c_long(trainEnd)
#         if withhistory:
#             hist = zeros((epochs+1,))
#             hist.fill(NaN)  # modif du 9/02/15
#             hist_p = c_void_p(hist.ctypes.data)
#         if self.codeVersion >= 28:
#             code = self.lib.train(source_p, byref(epoch_t), byref(trainEnd_t), hist_p)
#         elif self.codeVersion >= 16:
#             code = self.lib.train(source_p, byref(epoch_t), byref(trainEnd_t), hist_p, -1)
#         elif self.codeVersion >= 6:
#             code = self.lib.train(source_p, byref(epoch_t), byref(trainEnd_t), hist_p)
#         elif self.codeVersion >= 5:
#             code = self.lib.train(source_p, byref(epoch_t), hist_p)
#         else:         
#             code = self.lib.train(source_p, byref(epoch_t))
#         self.setWeights(params)
#         if computeDispersion:
#             resvec = self.computeTrainingResults(curw=params, actualepochs=epoch_t.value)
#             respress = self.getPRESS(params, donorm=True, root=True, full=True)
#             residuals = respress[1]
#             stddev = sqrt((residuals**2).sum()/self.dataCount)
#             outputs, jacobians = self.getjacobian(params, style=2)
#             press, residuals, singular, leverages, disp, svdlen, deltash = respress
#             resfull = (press, residuals, singular, leverages, disp, svdlen, deltash, outputs, jacobians)
#         else:
#             resfull = resvec = outputs = jacobians = None
#             stddev = self.getStdDev(source)         
#         trainEnd = trainEnd_t.value
#         return (source, epoch_t.value, stddev, trainEnd, hist, code), resfull, resvec

    def train_integratedex(self, params, epochs=-1, withhistory=False, 
            style=-1):
        hist = None
        trainEnd = 0
        svdlen = 0
        deltash = 0.0
        source = asarray(params, npdouble)
        source_p = c_void_p(source.ctypes.data)
        epoch_t = c_long(epochs)
        trainEnd_t = c_long(trainEnd)
        ZMat = zeros((self.paramCount*self.paramCount,), dtype=npdouble)
        ZMat_p = c_void_p(ZMat.ctypes.data) 
        Jacob = zeros((self.paramCount*self.dataCount,), dtype=npdouble)
        Jacob_p = c_void_p(Jacob.ctypes.data) 
        leverages = zeros((self.lib.baselen(),), dtype=npdouble)
        leverages_p = c_void_p(leverages.ctypes.data)
        residuals = zeros((self.lib.baselen(),), dtype=npdouble)
        residuals_p = c_void_p(residuals.ctypes.data)
        singular = zeros((self.paramCount,), dtype=npdouble)
        singular_p = c_void_p(singular.ctypes.data)
        svdlen_p = c_long(svdlen)
        deltash_p = c_double(deltash)
        dim = self.lib.outputCount()
        target = zeros((dim,), dtype=npdouble)
        target_p = c_void_p(target.ctypes.data)
        cost = zeros((dim,), dtype=npdouble)
        cost_p = c_void_p(target.ctypes.data)
        
        if withhistory:
            hist = zeros((epochs+1,))
            hist.fill(NaN)  # modif du 9/02/15
            hist_p = c_void_p(hist.ctypes.data)
        else:
            hist = None
            hist_p = None
            
        if self.codeVersion < 33:
            code = 0xFFF
        else:
            code = self.lib.trainex(source_p, byref(epoch_t), byref(trainEnd_t),
                hist_p, cost_p, target_p, residuals_p, singular_p, leverages_p, 
                ZMat_p, Jacob_p, byref(deltash_p), byref(svdlen_p))
            if code < 0: 
                raise DriverLibError(self.lasterror)
            self.setWeights(source)
            nlen = self.lib.baselen()
            press = sqrt(target / nlen)
            stddev = sqrt(cost / nlen)

        return source, epoch_t.value, stddev, press, residuals, leverages, \
            ZMat, Jacob, trainEnd_t.value, deltash, svdlen, singular, hist, \
            code

    def train(self, 
              startWeights=None, 
              epochs=0, 
              index=-1, 
              callback=callbackmin, 
              **kwds):                                    # DriverLib
        #algo="LM_INTEGRATED", disp=0, weightsstddev=0.3,
        """Lancement d'un apprentissage.
        Utilise les algorithmes d'optimisation integres.
        callback est une fonction  de callback prototype C: typedef long (*cbk)(real, long);
        """
        if callback == "debug":
            callback = callbackminprint
        trainstyle = kwds.get('trainstyle', 0)
        # setcallback assure la conversion de type de la fonction python 
        # callback vers le type C
        self.setcallback(callback)
        epochs = kwds.get('maxiter', epochs)
#         epochs = epochs if not 'maxiter' in kwds else kwds['maxiter']
        Nt = -1 
#         if 'style' in  kwds:
#             style = kwds["style"]
#         else:
#             style = algo
        #trainend = 0         
        vecPrime = self.getjacobian  # a revoir pour LOO et BS
        residuals = self.getresiduals  # a revoir pour LOO et BS
        fcost = self.getCost
        prime = self.getprime
        
        if startWeights is None:
            startWeights = self.weights
#         startWeights = self.newWeights(weightsstddev, 
#                 doinit=(startWeights is None) or (style & C.TR_S_INIT_PARAM))
        if epochs:
            self._dispersionMatrix = None
            self._conditionning = None
            self._stdtrain = 0
#         if disp:
#             sys.stderr.write("\nInformation: training %s, max iterations %d\n" % ("LM_INTRGRATED", epochs))
        fopt = 0.0
        popt = None
        try:
#             if style == "LM_INTEGRATED":
            res = self.train_integrated(startWeights, epochs=epochs, 
                trainstyle=trainstyle)[0]
            popt, Nt, fopt, _, _, code = res  #trainend
#             elif style == "LM_NT":  # LM by JLP
#                 res = optim_leastsq(func=residuals, x0=startWeights, 
#                   maxiter=maxiter, Dfun=vecPrime, 
#                 full_output=1, disp=disp, call back=call back)#
#                 popt, code, Nt, _, _, fopt = res  #Nf, Ng, 
#             elif style == "BFGS_NT":  # BFGS by JLP
#                 res = optim_bfgs(fcost, startWeights,
#                     maxiter=maxiter, Dfun=prime, 
#                     full_output=1, disp=disp, call back=call back)#
#             elif not OKScipy:
#                 raise Exception("Not implemented yet without Scipy")
#             else:
#                 if style == "LM":  # LM by SciPy
#                     res = optimize.leastsq(func=residuals, x0=startWeights, 
#                          maxfev=maxiter,  Dfun=vecPrime, factor=97, full_output=1)  #
#                     popt, _, infodict, _, _ = res #cov, mesg, ier
#                     Nt = infodict["nfev"]
#                     fopt = npsum(infodict['fvec']**2)/2
#                 elif style == "CG":  # CG by SciPy
#                     res = optimize.fmin_cg(f=fcost, x0=startWeights,
#                         fprime=prime, maxiter=maxiter, 
#                         full_output=1, disp=disp, call back=call back)
#                     popt, fopt, Nt, _, _ = res #Ng, warnflag
#                 elif style == "BFGS":  # BFGS by SciPy
#                     res  = optimize.fmin_bfgs(fcost, startWeights, fprime=prime, 
#                         maxiter=maxiter, full_output=1, disp=disp, call back=call back)
#                     popt, fopt, _, _, Nt, _, _ = res  #gopt, Bopt, Ng, warnflag
#                     popt, code, Nt, _, _, fopt = res #Nf, Ng, 
#                 elif style == "SPX":  # SPX by SciPy
#                     res = optimize.fmin(fcost, startWeights,
#                         maxiter=maxiter, full_output=1, disp=disp, 
#                         call back=cal lback)
#                     popt, fopt, Nt, _, _, _  = res #funcalls, warnflag, allvecs
#             else:
#                 popt = None
        except Exception as exres:
            print("DriverLib.train", exres)
        self._lastweights = popt.copy()
        N = self.modelCount
        self._stdtrain = math.sqrt(fopt/N)
        if code:
            return None, code, 0.0
        return popt, Nt, fopt  

    def reverse_train(self, outputtarget, inputs=None, freeinputs=None, 
        epochs=None, withhistory=False, debug=0, **kwds):
        # kwds est une poubelle
        innames = None
        if isinstance(inputs, dict):
            innames = list(inputs.keys())
            inputs = list(inputs.values())
        inputs = asarray(inputs, npdouble)
        assert inputs.shape[0] == self.inputCount
        inputs_p = c_void_p(inputs.ctypes.data)
        
        if freeinputs is None or freeinputs == 'all':
            freeinputs = ones((self.inputCount,), dtype=nplong)
        elif isinstance(freeinputs, dict):
            newfreeinputs = zeros((self.inputCount,), dtype=nplong)
            for index, name in enumerate(self.inputNames):
                if name in freeinputs:
                    newfreeinputs[index] = freeinputs[name]
            freeinputs = newfreeinputs
        elif isinstance(freeinputs, list) and len(freeinputs):
            newfreeinputs = zeros((self.inputCount,), dtype=nplong)
            for value in freeinputs:
                if isinstance(value, str):
                    index = self.inputNames.index(value)
                elif isinstance(value, int):
                    index = value
                if index >= 0:
                    newfreeinputs[index] = 1
            freeinputs = newfreeinputs
        else:
            freeinputs = asarray(freeinputs, nplong)
            
        freeinputs_p = c_void_p(freeinputs.ctypes.data)
        outputtarget_p = c_double(outputtarget)
        if epochs is None:
            epochs = 100
        epochs_p = c_long(epochs)
        ender = 0
        ender_p = c_long(ender)
        if withhistory:
            history = zeros((epochs+1,), dtype=npdouble)
            for ind in range(history.shape[0]):
                history[ind] = float('nan')
            history_p = c_void_p(history.ctypes.data)
        else:
            history_p = None 
        self.lib.settrainstyle(debug)
        self.lib.reversetrain(inputs_p, freeinputs_p, byref(outputtarget_p), 
            byref(epochs_p), byref(ender_p), history_p)
        epochs = epochs_p.value  
        ender = ender_p.value  
        if innames is not None:
            inputs = {name: val for name, val in zip(innames, inputs)}
        if withhistory:
            return inputs, epochs, ender, history[:epochs+1]
        else:
            return inputs, ender
    
    def hasDebug(self, trainstyle):
        return 1 if (trainstyle & C.CS_DEBUG) else 0
    
    def trainLOO(self, initlist=None, inittype=C.INIT_START_PARAM, 
        callback2=None, onReturnResult=None, selected_LOO=None, 
        initcount=1, weightsstddev=0.1, epochs=0, callback=None, 
        LOOcriterion=None, LOOThreshold=0, trainstyle=-1, maxworkers=-2, 
        parallel=True, seed=None):
        
        return self.trainBS(initlist=initlist, inittype=inittype, 
            weightsstddev=weightsstddev, initcount=initcount, epochs=epochs, 
            BStype=RE_LOO, callback=callback, callback2=callback2, 
            onReturnResult=onReturnResult, selected_LOO=selected_LOO, 
            LOOcriterion=LOOcriterion, LOOThreshold=LOOThreshold, 
            trainstyle=trainstyle, maxworkers=maxworkers, 
            parallel=parallel, seed=seed) 
        
    def trainSuper(self, initlist=None, inittype=C.INIT_START_PARAM, 
        weightsstddev=0.3, initcount=1, BScount=100, epochs=0, 
        callback=None, callback2=None, onReturnResult=None, trainstyle=-1, 
        maxworkers=-2, parallel=True, seed=None): 
        
        return self.trainBS(initlist=initlist, inittype=inittype, 
            weightsstddev=weightsstddev, initcount=initcount, BScount=BScount, 
            epochs=epochs, BStype=RE_SUPER, callback=callback, 
                callback2=callback2, onReturnResult=onReturnResult, 
                trainstyle=trainstyle, maxworkers=maxworkers, parallel=parallel)
        
    def trainBS(self, initlist=None, inittype=C.INIT_START_PARAM, weightsstddev=0.1,  #startParams=None, 
        initcount=1, BScount=100, epochs=0, BStype=RE_NONE, callback=None, 
        callback2=None, onReturnResult=None, selected_LOO=None, 
        LOOcriterion=None, LOOThreshold=0, trainstyle=-1, maxworkers=-2, 
        parallel=True, seed=None): 
        # callback est utilise dans le train de base
        # callback2 est utilise dans les boucles externes
        # selected_LOO sert a limiter le nb de run pour debug
        
        computeDispersion = True 
        resultMatrix = None
        # computeDispersion est mis a Vrai pour permettre le calcul du LOO_leverage
        max_workers = maxWorkers(maxworkers)
        do_selected_LOO = (selected_LOO is not None) and len(selected_LOO)
        do_parallel = (parallel and 
                    # USE_PARALLEL and 
                    USE_PARALLEL_BS and 
                    not do_selected_LOO and 
                    (max_workers > 0) and 
                    not self.hasDebug(trainstyle))# and (BStype < RE_SUPER) 
        
        if self.weights is None:
            originalParams = None
        else:
            originalParams = self.weights.copy()
        muststop = False
        self.resultMatrix = None
        settrainindex = 0
        stylemem = 0
        extraweights = None
        extraweightslist = []
        leverageslist = []
        try:
            if BStype == RE_LOO:  # LOO
                BScount = self.dataCount
                settrainindex = 2
            elif BStype in BSGROUP:
                settrainindex = 1 
            elif BStype == RE_SUPER:
                initcount = len(initlist)
                settrainindex = 0
                LOOcriterion = None
            if not USE_SUPER_TRAIN:
                trainstyle = trainstyle & (~ C.CS_SUPER_TRAIN)
            stylemem = self.setTrainStyle(trainstyle)
            extraweights = zeros((BScount, self.paramCount))
            extraweightslist = zeros((initcount, BScount, self.paramCount))
            leverages = zeros((BScount,)) if computeDispersion else None
            leverageslist = zeros((initcount, BScount))
            outs = zeros((BScount,)) if computeDispersion else None
            presses = zeros((BScount, )) if computeDispersion else None
            if (BStype >= RE_LOO) and do_selected_LOO:
                BScount = len(selected_LOO)
            if epochs <= 0:
                epochs = 10*(1 + self.paramCount)
            
            if BStype == RE_SUPER:
                residuals = self.getresiduals(style=C.CS_SUPER_TRAIN).copy()
            elif not self.weights is None:
                residuals = self.getresiduals()  # ici le 15/12/18
            else:
                residuals = None
            targets = self.targets.copy()
            
            loccount = 0
            reslist = []
            if not onReturnResult:
                resultMatrix = zeros((BScount, initcount), dtype=object)
                
            if no_parallel_seed:
                seedlistlist = []
                for _ in range(BScount):
                    seedloc = random.randint(0x10, 0xFFFFFFFF)
                    seedlist = seedList(seedloc, initcount)
                    seedlistlist.append(seedlist)
                
            else:
                seedlistlist = [[seed for _ in range(initcount)] for _ in range(BScount)]
            
            
            if do_parallel:  
                # debut boucle parallele
                with cf.ProcessPoolExecutor(max_workers=max_workers) as executor:                    
                    futures = [executor.submit(trainJobBS, self, initlist, 
                        inittype, initindex, residuals, BStype, settrainindex, 
                        epochs, molindex, computeDispersion, weightsstddev, 
                        targets, locseed)
                        for molindex, seedlist in enumerate(seedlistlist) 
                        for initindex, locseed in enumerate(seedlist)]  
#                         for molindex in range(BScount) 
#                         for initindex in range(initcount)]  
                    
                    cumul0 = 0
                    cumul1 = 0
                    for future in cf.as_completed(futures):
                        res = future.result()
                        molindex, initindex = res[4:6]
                        reslist.append(res)
                        if onReturnResult:
                            onReturnResult(*res)
                        if resultMatrix is not None:
                            resultMatrix[molindex, initindex] = res
                        if callback and (not cumul0 % initcount):
                            cumul1 += 1
                            cont = callback(cumul1)
                            if isinstance(cont, tuple):
                                cont = cont[0]
                            muststop = not cont
                        cumul0 += 1
                        if muststop:
                            break
                    if muststop:
                        for future in futures:
                            future.cancel()
                # fin boucle parallele                            
                if not muststop and (resultMatrix is not None):
                    for molindex in range(BScount):
                        resvec = list(resultMatrix[molindex])
                        resvec = sorted(resvec, key=lambda x:x[4])
                        resultMatrix[molindex] = resvec
                     
                
            else:  # traitement en serie
                # self.setcallback(None)
#                 if do_selected_LOO:
#                     itercount = selected_LOO
#                 else:
#                     itercount = range(BScount)
                for molindex, sedlist in enumerate(seedlistlist):  #itercount:
                    for initindex, locseed in enumerate(sedlist):  #range(initcount):
                        res = trainJobBS(self, initlist, inittype, initindex, 
                            residuals, BStype, settrainindex, epochs, molindex, 
                            computeDispersion, weightsstddev, targets, locseed)  #, trainstyle
                        reslist.append(res)
                        if resultMatrix is not None:
                            resultMatrix[molindex, initindex] = res[:-1]
                        if onReturnResult:
                            onReturnResult(*res)
                                                
                    if callback:
                        cont = callback(molindex+1)
                        if isinstance(cont, tuple):
                            cont = cont[0]
                        muststop = not cont
                    if muststop:
                        break
                    if muststop:
                        break
                            
            if not muststop and (resultMatrix is not None):
                # Ici on traite les résultats enregistrés dans resultMatrix
                for index in range(BScount):
                # pour chaque molecule
                    indloc = index if BStype == 3 else BStype
                    self.settrainingset()
                    if initcount <= 1:
                        loccount = 1
                        val = resultMatrix[index, 0] 
                        code, epochs, ini_params, paramMem, molindex, \
                            initindex, indexReturn, cost, press, out, lev, \
                            resvec, disp, _, _ = val
                        if computeDispersion:
                            leverages[index] = lev
                            outs[index] = out
                            presses[index] = press 
                    else:
                        self.settrainingset(settrainindex, indloc, residuals)
                        # on cree la liste verticale des resultats de la molecule definie par index
                        lst = list(resultMatrix[index])
                        # on trie si necessaire la liste locresult sur la valeur du premier element
                        try:
                            # on trie la liste a trier en fonction du critere 
                            sortindex = C.criterindex[LOOcriterion]
                            locresult = sorted(lst, key = lambda x: abs(x[sortindex]))
                        except:
                            locresult = lst
                        self.settrainingset()
                        for ind1, res in enumerate(locresult):
                            # renseignement de la liste des poids par ordre de tri
                            extraweightslist[ind1][index] = res[C.TRR_PARAMS].copy()
                            leverageslist[ind1][index] = res[C.TRR_LEV]
                            resultMatrix[index, ind1] = res
                            
                        if len(locresult):
                            code, epochs, ini_params, paramMem, molindex, initindex, _, cost, press, out, lev, resvec, disp, _, _ = locresult[0]  #[1] returnindex, , inittype
                            if computeDispersion:
                                leverages[index] = lev
                                outs[index] = out
                                presses[index] = press
                        else:
                            # cas ou tous les apprentissages ont echoue
                            code, epochs, paramMem, molindex, initindex = (-1, -1, None, index, -1)
                        assert(index == molindex)
                    
                    if epochs and not code:
                        extraweights[index] = paramMem.copy()
                        loccount += 1
                    if callback2:
                        cont = callback2(index + 1)
                        if isinstance(cont, tuple):
                            cont = cont[0]
                            
#             else:
#                 for res in reslist:
#                     code, epochs, ini_params, params, index, initindex, indexReturn, stddev, press, out, lev, resvec, disp, inittype , target, locseed = res
                
            self.settrainingset()
        except Exception as err:
            print(err)
            raise
        finally:
            self.setTrainStyle(stylemem)
            self.weights = originalParams
            self._extraweights = extraweights
            self._extraweightslist = extraweightslist
            self.leverages = leverageslist #leverages
#            self.outputs = outs
            self.presses = presses
            self.resultMatrix = resultMatrix
        self.settrainingset()
        return loccount, resultMatrix   

#    setweights = setweights         
    #DriverLib.trainingdata = DriverLib.trainingData         
    
def onGetNewWeights(model, weightsstddev):
    return model.newWeights(weightsstddev)
    
def kerneltrainintegratedmain(model, weights, maxiter, withhistory, index=-1):
    res = model.kerneltrainintegratedmain(weights, maxiter, withhistory, index)
    if index < 0:
        return res
    return (index,) + res

def core_train2(model, weights, maxiter, withhistory, index=-1):
    return model.core_train2(weights, maxiter, withhistory, index)

# def core_train(model, weights, maxiter, withhistory, index=-1):
#     return model.core_train(weights, maxiter, withhistory, index)

def kerneltrainintegratedmain3(model, weights, maxiter, withhistory, index=-1):
    return model.kerneltrainintegratedmain3(weights, maxiter, withhistory, index)
#     if index < 0:
#         return res
#     return (index,) + res

# def kerneltraining(model, weights, maxiter, withhistory, index=-1):
#     res = model.kerneltraining(weights, maxiter, withhistory)
#     if index < 0:
#         return res
#     return (index,) + res
def checklib(libfilename):
    model = DriverLib(libfilename)
    print(repr(model))
    
def checkpicklelib(libfilename, filename, filetype, datarange, datafields, grouplist):
    from io import BytesIO
    import pickle as pickle
    
    model = DriverLib(libfilename)
    model.loadTrainingData(None, filename, filetype, datarange, datafields, grouplist)
    print(repr(model))
    print(model.traindatas())
    stream = BytesIO()
    pickle.dump(model, stream)
    stream.flush()
    stream.seek(0)
    model2 = pickle.load(stream)
    stream.close()
    print(repr(model2))
    print(model2.traindatas())
#     return model
    
    #for i in range(model.baselen):

#==============================================================================
if __name__ == "__main__":
    
#     source = "/Users/jeanluc/dockerold/workdir/libbjma244t25_si3_5n.so"
#     checklib(source)
    
#     loadTrainingData(self, options=None, filename="", filetype="", datarange="", datafields):
    source = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_Test/src/metaphor/test_monal/testFiles/libnn_5_5_1.so"
    # "/Users/jeanluc/nn1/workdir/libnn_5_5_1.so"
    filename = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_Test/src/metaphor/test_monal/testFiles/L_153.csv"
    #"/Users/Shared/workspace/Monal_Test/src/testFiles/L_153.xlsx"
    filetype ="csv"
    datarange = "DATA"
    datafields = [[0, 1, 2, 3, 4], [5]]
    grouplist = ['inputs', 'outputs']
    #             (libfilename, filename, filetype, datarange, datafields, grouplist)
    checkpicklelib(source, filename, filetype, datarange, datafields, grouplist)
    
    model = DriverLib(source)

    model.setRandSeed(194999)
    ww = model.newWeights(0.3)
    #residu = model.getresiduals(ww)
    #print "residu", residu
    costini = model.getCost(ww)
    #ww2, epochs, cost, code
    #bests, saveres = model.multitrain(initcount=5, initweights=ww, maxiter=100)
    #bestmem = bests[0][0]
    #print "bests"
    #for val in bests:
    #    print "", val
    
#     from io import StringIO
#     import pickle as pickle
#     single = 1
# #     source = "C:\\Projets\\GM\\TestAD\\Base115new\\base115new_chi0iso00n.dll"
# #     source = "/Users/Shared/GMWorkspace/BaseA109/libbasea109_chi03n.so"
#     source = "/Users/jeanluc/nn1/workdir/libnn_9_5_1.so"
#     datafile = "/Users/Shared/workspace/Monal_Test/src/testFiles/B321_19d_JLPloix.xlsx"
# 
# #codeversion
#     
#     model = DriverLib(source)
#     #model.settrainingset()
#     model.setRandSeed(1947)
#     #model.targets = targetfile
#     
# #     stream = StringIO()
# #     pickle.dump(model, stream)
# #     stream.flush()
# #     stream.seek(0)
# #     #stream2 = StringIO(stream.getvalue())
# #     model2 = pickle.load(stream)
# #     stream.close()
#     #model2 = DriverLib(source)
#     #model.settrainingset()
#     #model.setRandSeed(1947)
#     #model2.targets = targetfile
#     
#     print("property:", model.propertyName)
#     print()
#     print("moduleName", model.moduleName)
#     print("monalVersion", model.monalVersion)
#     print("created", model.created)
#     print("mark", model.mark)
#     print("base", model.base)
#     print("linear", model.isLinear)
#     print("paramlCount", model.paramCount)
#     print("modelCount", model.modelCount)
#     print("inputCount", model.inputCount)
#     print("outputCount", model.outputCount)
#     print("hidden", model.hidden)
#     print("biasBased", model.biasbased)
#     print("outlinks", model.outlinks)
#     #model2.targets = [0 for _ in range(model.modelCount)]
#     #print "target 1", model.targets
#     #print "target 2", model2.targets
#     print("outputnorm", model.outputnorm)
#     print("input norm", model.inputnorm)
# 
# 
# 
# #     print("norm 2", model2.outputnorm)
#     print(model.lib)
# #     print(model2.lib)
#     
#     #if single:
#     model.setRandSeed(194999)
#     ww = model.newWeights(0.3)
#     #residu = model.getresiduals(ww)
#     #print "residu", residu
#     costini = model.getCost(ww)
#     #ww2, epochs, cost, code
#     #bests, saveres = model.multitrain(initcount=5, initweights=ww, maxiter=100)
#     #bestmem = bests[0][0]
#     #print "bests"
#     #for val in bests:
#     #    print "", val
#     
#     
#     
#     
#     cur, epochs, cost, trainend, code = model.kerneltrainintegratedmain(ww, 150)
#     #cost2 = model.getcost(cur)
#     #press_old = model.getPRESS_(cur, None, True, True)
#     press = model.getPRESS(cur, 1, 1)
#     print("cost ini  ", costini)
#     print("cost final", cost)
#     print("PRESS", press)
#     #print "PRESS old", press_old
#     print("epochs", epochs)
#     #else:
#         #os.system("ipcluster start")
#         #lst = multitrainintegrated(model, targetfile, None, 8, 100)
#         #for val in lst:
#         #    print val
#         #for ind, (cur, N, fopt, mem, code) in enumerate(lst):
#         #    print ind, N, fopt
#         
#         #os.system("ipcluster stop")
#     
#     #model = None
#     
    print("done")