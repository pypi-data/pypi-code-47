#-*- coding: ISO-8859-15 -*-
#===============================================================================
# $Id: _modellib.py 4738 2018-03-26 05:30:12Z jeanluc $
#  Module _modellib.py
#  Projet MonalPy
#
#  modeles fondes sur les libraries partagees
#
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

#from __fu ture__ import absolute_import
import os
import numpy as np
from ctypes import create_string_buffer, byref, c_int, c_double, c_void_p
import math
#from nntoolbox._2and3 import isstr
from six import string_types
try:
    from scipy.stats.t import interval
except:
    from ..util.monaltoolbox import interval
from ..model import ModelBase
from ..Property import Property, Properties
from ..lcode import codeconst as CC
from ..library.libmanager import LibManager, LibraryManagerError


class ModelLibError (Exception): 
    """ModelLib Exception.
    """
    pass

@Properties(("confidencelevel", "extraweights", "extradispersions", 
             "LOOweights", "BSweights", "LOOweightsMulti"), False)
class ModelLib(ModelBase, LibManager): 
    """class ModelLib
    Gestionnaire des modeles provenant de librairies dynamiques (dll, so, dylib)
    """
    
    def __init__(self, libfilename, owner=None, name="", source=None, paramfile=None):
        ModelBase.__init__(self, owner, name)
        LibManager.__init__(self, libfilename)
        self.weights = None
        self._LOOweightsMulti = None
        self._LOOweights = None
        self._BSweights = None
        if source:
            if isinstance(source, string_types):
                with np.load(source, allow_pickle=True) as sourceloc:
                    if "propertyname" in sourceloc.files:
                        self.propertyName = str(sourceloc["propertyname"])
            else:
                if "propertyname" in list(source.keys()):
                    self.propertyName = str(source["propertyname"])
        self.loadParameters(paramfile if paramfile else source)
            
    def __del__(self):
        LibManager.__del__(self)
        ModelBase.__del__(self)

    def __enter__(self):
        return self
    
    def __exit__(self, etype, value, traceback):
        self.__del__()
    
    def __repr__(self):
        return self.getDescription()
    
    def getDescription(self, keeplist=False):  #, extended=False
        lst = [("From module %s"% self.moduleName)]
        lst.append("module type %s"% self.moduleType)
        lst.append("code version/current %s/%s"% (self.codeVersion, CC.__useversion__))
        lst.append("created %s"% self.created)
        if self.mark: #getStrPropertyFromLib("mark"):
            lst.append("mark %s"% self.getStrPropertyFromLib("mark"))
        lst.append("Molecule %s"% self.modelName)
        #lst.append("Module %s"% self.moduleName)#getStrPropertyFromLib("moduleName"))
        lst.append("Smiles %s"% self.smiles)#getStrPropertyFromLib("smiles"))
        lst.append("Train base %s"% self.trainBase)#getStrPropertyFromLib("trainbase"))
        lst.append("Configuration %s"% self.configuration)
        if self.propertyName:
            lst.append("propertyName %s"%self.propertyName)
        lst.append("paramcount %d"%self.paramCount)
        lst.append("dimension %d"%self.dimension)
        lst.append("hidden %s"%self.hidden)
        if self.BSCount:
            lst.append("BSCount %s"%self.BSCount)
        if self.LOOCount:
            lst.append("LOOCount %s"%self.LOOCount)
        if self.trainingStddev:
            lst.append("trainingStddev %s"%self.trainingStddev)
        if self.baselen:
            lst.append("baselen %s"%self.baselen)
#         if extended and self.configuration:
#             connect, central, classif, hidden = ReverseConfigString(self.configuration)
        if keeplist:
            return lst
        return "\n\t".join(lst)
    
    @property
    def modelName(self):
        return self.getStrPropertyFromLib("modelName").decode("ISO-8859-15")
    
    @Property
    def dimension(self): # LibManager
        return self.lib.dimension()
    
    @property
    def configuration(self):
        return self.getStrPropertyFromLib("configuration")
    
    @property
    def smiles(self):
        return self.getStrPropertyFromLib("smiles")
    
    @property
    def trainBase(self):
        return self.getStrPropertyFromLib("trainbase")
    
    @property
    def BSCount(self):
        if not hasattr(self, "_BSweights") or self._BSweights is None:
            return 0
        return self.BSweights.shape[0]
    
    @property
    def LOOCount(self):
        if not hasattr(self, "_LOOweights") or self._LOOweights is None:
            return 0
        return self.LOOweights.shape[0]
    
    def extraList(self):
        lst = []
        if hasattr(self, "_BSweights"):
            lst.append("BS")
        if hasattr(self, "_LOOweights") or hasattr(self, "_LOOweightsMulti"):
            lst.append("LOO")
        return lst
    
    def transferExtra(self, extratype=""):  #, axis=0):
        lst = []
        if (extratype == "LOO") and hasattr(self, "_LOOweightsMulti") and (self.LOOweightsMulti is not None):
            res = np.asarray([[self.transfer(weights) for weights in target] for target in self.LOOweightsMulti])
            return res
            #return np.mean(res, axis=axis)
            
        target = None
        if (extratype in ("", "BS")) and hasattr(self, "_BSweights"):
            target = self.BSweights
        elif (extratype == "LOO") and hasattr(self, "_LOOweights"):
            target = self.LOOweights
        if target is not None:
            lst = [self.transfer(weights) for weights in target]
        return np.asarray(lst)
    
#     def transferBS(self):  # DriverLib
#         return self.transferExtra("BS")
        
#     def transferLOO(self):  # DriverLib
#         return self.transferExtra("LOO")
        
    @Property
    def trainingStddev(self): # ModelLib
        no = self.lib.outputCount()
        target = np.zeros((no,), dtype=np.double)
        target_p = c_void_p(target.ctypes.data)
        self.lib.getstddev(target_p)
        if no == 1:
            return target[0]
        else:
            return target
    @trainingStddev.setter
    def trainingStddev(self, value): # ModelLib
        #no = self.lib.outputCount()
        source = c_double(value)
        return self.lib.setstddev(source)

    @Property
    def baselen(self): # ModelLib
        return self.lib.getbaselen()
    @baselen.setter
    def baselen(self, value): # ModelLib
        self.lib.setbaselen(int(value))
    
    @Property
    def params(self): # ModelLib
        nw = self.lib.getparams(None)
        target = np.zeros((nw,), dtype=np.double)
        target_p = c_void_p(target.ctypes.data)
        res = self.lib.getparams(target_p)
        if res:
            return None
        return target
    @params.setter
    def params(self, value): # ModelLib
        source = np.asarray(value)
        try:
            ll = source.shape[0]
        except IndexError:
            print("Error in params setter: source : %s"%source)
            raise
            
        source_p = c_void_p(source.ctypes.data)
        res = self.lib.setparams(source_p, c_int(ll)) 
        if res == -1:
            dim = self.lib.lasterror(None) 
            rtyp = create_string_buffer(dim + 1) 
            res = self.lib.lasterror(byref(rtyp))
            if not res: 
                raise ModelLibError(rtyp.value)
            raise ModelLibError("Unknown error")
    
    @Property
    def halfdispersion(self): # ModelLib
        nd = self.lib.dimension()
        nw = self.lib.paramCount(None)
        target = np.zeros((nd*nw,), dtype=np.double)
        target_p = c_void_p(target.ctypes.data)
        res = self.lib.gethalfdispersion(target_p)
        if res:
            return None
        target = np.reshape(target, (nw, nd))
        return target
    @halfdispersion.setter
    def halfdispersion(self, value): # ModelLib
        nd = self.lib.dimension()
        nw = self.lib.paramCount(None)
        source = np.asarray(value)
        if source.ndim == 1:
            ll2 = len(source)
            ll = int(math.sqrt(ll2))
            if (ll2 != ll*ll) or not (ll in [nw, nd]):
                raise ModelLibError("Bad dimension in dispersion setter")
        elif source.ndim == 2:
            ll, ld = source.shape
            if (ll != ld) or not (ll in [nw, nd]):
                raise ModelLibError("Bad dimension in dispersion setter")
            source = source.reshape(ll*ld,)
        source_p = c_void_p(source.ctypes.data)
        self.lib.sethalfdispersion(source_p, c_int(ll))
    
    @Property
    def dispersion(self): # ModelLib
        nw = self.lib.paramCount(None)
        #nw = self.lib.dimension()
        target = np.zeros((nw*nw,), dtype=np.double)
        target_p = c_void_p(target.ctypes.data)
        res = self.lib.getdispersion(target_p)
        if res:
            return None
        target = np.reshape(target, (nw, nw))
        return target
    
    @dispersion.setter
    def dispersion(self, value): # ModelLib
        nw = self.lib.paramCount(None)
        nd = self.lib.dimension()
        source = np.asarray(value)
        if source.ndim == 1:
            ll2 = len(source)
            ll = int(math.sqrt(ll2))
            if (ll2 != ll*ll) or not (ll in [nw, nd]):
                raise ModelLibError("Bad dimension in dispersion setter")
        elif source.ndim == 2:
            ll, ld = source.shape
            if (ll != ld) or not (ll in [nw, nd]):
                raise ModelLibError("Bad dimension in dispersion setter")
            source = source.reshape(ll*ld,)
        source_p = c_void_p(source.ctypes.data)
        self.lib.setdispersion(source_p, c_int(ll))
    
    def loadParameters(self, source): # ModelLib
        if source is None: return
        if isinstance(source, string_types):
            #chargement binaire
            try:
                with np.load(source) as source1:
                    res = self.loadFromDict(source1) or self.loadWeightsASCII(source, self) or self.loadWeightsXML(source, self)
#                     if not self.l oadFromDict(source1):
#                         # chargement ASCII    
#                         if not self.loadWeightsASCII(source, self):
#                             # chargement XML
#                             self.loadWeightsXML(source, self)
                return res
            except:
                return False
        elif isinstance(source, (list, np.ndarray)):
            if self.weights is None:
                self.weights = np.asarray(source)
            # chargement d'un vecteur
            else:
                self.weights = source
        else:  #if isinstance(source, dict):
            return self.loadFromDict(source)

    def adaptParams(self, params):
        params = np.asarray(params)
        ddim = params.shape[0]
        if ddim == self.paramCount:
            return params
        try:
            return np.asarray([params[ind] for ind in self.wused])
        except:
            return None
        
    def adaptDispersion(self, dispersion):
        dispersion = np.asarray(dispersion)
        ddim = dispersion.shape[0]
        if ddim == self.paramCount:
            return dispersion 
        try:            
            return np.asarray([[dispersion[ii][jj] for jj in self.wused] for ii in self.wused])
        except:
            return None
        
    def adaptHalfDispersion(self, halfdispersion):
        return halfdispersion

    def loadFromDict(self, source): # ModelLib
        try:
            paramnames = None
            dispersionMatrix = None
            
            #halfDispersionMatrix = None
            for key, value in source.items():
                try:
                    if key == "propertyname":
                        self.propertyname = str(value)
                    elif key == "paramnames":
                        paramnames = list(value)
                    elif key == "params":
                        params = np.asarray(value)
                    elif key in ("outnorm", "outputnorm"):
                        self.outputnorm = value
                    elif key == "baselen":
                        self._baselen = int(value)
                    elif key == "stddev":
                        self.trainingStddev = float(value)
                    elif key == "dispersion":
                        dispersionMatrix = np.asarray(value)
                    #elif key == "halfdispersion":
                    #    halfDispersionMatrix = np.asarray(value)
                    elif key == "extraweights":
                        extraweights = value
                        nbmulti = extraweights.shape[0]
                        self._extraweights = np.zeros((nbmulti, self.paramCount))
                        for ind, ww in enumerate(extraweights):
                            self._extraweights[ind] = self.adaptParams(ww)
                            #self._extraweights[ind] = self.adaptParams(extraweights[ind])
                    elif key == "LOOweights":
                        ndim = value.ndim
                        shape = value.shape
                        if ndim == 2:
                            nbmulti = shape[0]
                            LOOweights = value
                        elif ndim == 3:
                            nbmulti = shape[1]
                            LOOweights = value[0]
                            LOOweightsMulti = value
                            self._LOOweightsMulti = np.zeros((shape[0], nbmulti, self.paramCount))
                            for matloc, mat in zip(self._LOOweightsMulti, LOOweightsMulti):
                                for ind, ww in enumerate(mat):
                                    matloc[ind] = self.adaptParams(ww)
                        self._LOOweights = np.zeros((nbmulti, self.paramCount))
                        for ind, ww in enumerate(LOOweights):
                            self._LOOweights[ind] = self.adaptParams(ww)
                            
                    elif key == "BSweights":
                        BSweights = value
                        nbmulti = BSweights.shape[0]
                        self._BSweights = np.zeros((nbmulti, self.paramCount))
                        for ind, ww in enumerate(BSweights):
                            self._BSweights[ind] = self.adaptParams(ww)
                    elif key == "extradispersion":
                        extradispersion = value
                        #nbmuti = extradispersion.shape[0]
                        self._extradispersions = np.asarray([self.adaptDispersion(mat) for mat in extradispersion])
                except: pass    
            if (paramnames is None):
                self.params = params
                self.dispersion = dispersionMatrix
                #self.halfdispersion = halfDispersionMatrix
            else:
                self.params = self.adaptParams(params)
                try:
                    source = self.adaptDispersion(dispersionMatrix)
                    self.dispersion = source
                except Exception as err:
                    pass
                #self.halfdispersion = self.adaptHalfDispersion(halfDispersionMatrix)
            return True
        except (IOError, ModelLibError) as err:
            return False
    
    @Property
    def wused(self): # ModelLib
        ls = self.paramCount
        target = np.zeros((ls,), dtype=np.int)
        target_p = c_void_p(target.ctypes.data)
        #res = 
        self.lib.getwused(target_p)
        return target
    
    @Property
    def freedom(self):
        return self.lib.getfreedom(0)
    
    def transfer(self, weights=None, inputs=None, norm=None): # ModelLib
        no = self.outputCount
        ni = self.inputCount
        if ni:
            if inputs is None:
                source_p = None
            else:
                source = np.asarray(inputs, np.double)
                source_p = c_void_p(source.ctypes.data)
        target = np.zeros((no,), dtype=np.double)
        target_p = c_void_p(target.ctypes.data)
        if weights is None:
            weights_p = None
        else:
            weights_s = np.asarray(weights, np.double)
            weights_p = c_void_p(weights_s.ctypes.data)
        if norm is None:
            norm_p = None
        else:
            norm_s = np.asarray(norm, np.double)
            norm_p = c_void_p(norm_s.ctypes.data)
        if ni:
            #res = 
            self.lib.transfer(weights_p, source_p, target_p, norm_p)            
        else:
            #res = 
            self.lib.transfer(weights_p, target_p, norm_p)
       
        if no == 1:
            target = target[0]
        return target
    
    def transferprime(self, weights=None, norm=None): # ModelLib
        no = self.outputCount
        nw = self.paramCount
        target = np.zeros((no,), dtype=np.double)
        target_p = c_void_p(target.ctypes.data)
        gradient = np.zeros((nw,), dtype=np.double)
        gradient_p = c_void_p(gradient.ctypes.data)
        if weights is None:
            weights_p = None
        else:
            weights_s = np.asarray(weights, np.double)
            weights_p = c_void_p(weights_s.ctypes.data)
        if norm is None:
            norm_p = None
        else:
            norm_s = np.asarray(norm, np.double)
            norm_p = c_void_p(norm_s.ctypes.data)
        #res = 
        self.lib.transferprime(weights_p, target_p, gradient_p, norm_p)
       
        if no == 1:
            target = target[0]
        return target, gradient
    
    def transferleverage(self, weights=None, disp=None, norm=None, style=0): # ModelLib  # default par disp
        mem = None
        externdisp = disp is not None
        if externdisp:
            mem = self.dispersion
            self.dispersion = disp
        no = self.outputCount
        target = np.zeros((no,), dtype=np.double)
        target_p = c_void_p(target.ctypes.data)
        leverage = np.zeros((no,), dtype=np.double)
        leverage_p = c_void_p(leverage.ctypes.data)
        if weights is None:
            weights_p = None
        else:
            weights_s = np.asarray(weights, np.double)
            weights_p = c_void_p(weights_s.ctypes.data)
        if norm is None:
            norm_p = None
        else:
            norm_s = np.asarray(norm, np.double)
            norm_p = c_void_p(norm_s.ctypes.data)
        if style == 1:
            # use of halfdispersion
            self.lib.transferleverage2(weights_p, target_p, leverage_p, norm_p)
        else:
            # direct use of dispersion
            self.lib.transferleverage(weights_p, target_p, leverage_p, norm_p)
       
        if no == 1:
            target = target[0]
            leverage = leverage[0]
            try:
                self.dispersion = mem
            except Exception as err:
                pass
        return target, leverage

    def transferIC(self, weights=None, inputs=None, acc=0.95, style=0, withlev=0, withhalf=0): # ModelLib
        out, leverage = self.transferleverage(weights, style=withhalf) # ici style = 1 -> methode halfdispersion
        stddev = self.trainingStddev
        df = self.freedom
        inter = interval(acc, df)
        if leverage >= 0:
            coeff = stddev * math.sqrt(leverage)
        else:
            coeff = 0
        if not style:
            if withlev == 2:
                return tuple([out] + [out + val * coeff for val in inter] + [leverage])
            elif withlev:
                return tuple([out + val * coeff for val in inter] + [leverage])
            else:
                return tuple(out + val * coeff for val in inter)
        else:
            IC =  interval(acc)[1] * coeff
            if withlev:
                return out[0], IC, leverage
            return out[0], IC

    def transferEx(self, inputs=None): # ModelLib
        try:
            outs = []
            levs = []
            for lweight, ldisp in zip(self.extraweights, self.extradispersions):     #self.dispersion = ldisp
                out, lev = self.transferleverage(lweight, disp=ldisp ,style=0)
                outs.append(out)
                levs.append(lev)
            return outs, levs            
        except AttributeError:
            return None, None
    
    def long2short(self, source):
        wused = self.wused
        ls = len(wused)
        if ls == source.shape[0]:
            return source
        sh = list(source.shape)
        dims = tuple([ls] + sh[1:])
        res = np.zeros(dims)
        for i, ind in enumerate(wused):
            res[i] = source[ind]
        return res
    
    def short2long(self, source): # ModelLib
        ls = self.paramCount
        ll = self.dimension
        if ll <= ls:
            return source
        if len(source) != ls:
            return source
        result = np.zeros((ll,))
        wused = self.wused
        for index, ind in enumerate(wused):
            result[ind] = source[index]
        return result
        
def VerifyModule(filename, datarange, modelcount):
    if not os.path.exists(filename):
        return False
    try:
        with LibManager(filename) as mgr:
            ret = mgr.codeVersionOK()
            try:
                ret = ret and hasattr(mgr, "datarange") and mgr.datarange == datarange
            except:
                ret = False
            try:
                ret = ret and hasattr(mgr, "modelCount") and mgr.modelCount == int(modelcount)
            except:
                ret = False
#            hasattr(mgr, "modelCount") and mgr.modelCount == modelcount
    except LibraryManagerError:
        ret = False
    return ret        

def codeVersionOK(filename): 
    if not os.path.exists(filename):
        return False
    try:
        with LibManager(filename) as mgr:
            ret = mgr.codeVersionOK()
    except LibraryManagerError:
        ret = False
    return ret
        
def useCodeVersionOK(filename): 
    if not os.path.exists(filename):
        return False
    #ret = False
    try:
        with LibManager(filename) as mgr:
            ret = mgr.usecodeVersionOK()
    except LibraryManagerError:
        ret = False
    return ret
    
def expectedPpty(filename, ppty, value):
    if not os.path.exists(filename):
        return False
    ret = False
    try:
        with LibManager(filename) as mgr:
            if isinstance(ppty, string_types):
                ret = mgr.getStrPropertyFromLib(ppty) == value
            else:
                for ind, (ppty1, value1) in enumerate(zip(ppty, value)):
                    if not ind:
                        ret = True
                    ret = ret and mgr.getStrPropertyFromLib(ppty1) == value1
    except LibraryManagerError:
        ret = False
    return ret

        
# if __name__ == "__main__":
#     path = "C:\Projets\GM\TestAD_2\BaseA109"
#     module = "basea109_chi00n.d ll"
#     module = os.path.join(path, module)
#     moduleold = "basea109_chi04n.dl l"
#     moduleold = os.path.join(path, moduleold)
#     
#     
#     print CC.__version__
#     print codeVersionOK(module)
#     print codeVersionOK(moduleold)
    
#------------------------------------------------------------------------------    
# if __name__ == "__main__":
#     print student.interval(0.99, 5)
#     print interval(0.99, 5)
    
#     testFileDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',  '..', "testFiles"))
#     libfile = os.path.join(testFileDir, "libpropane_.so")
#     gmxfile =  os.path.join(testFileDir, "LogP_base321_dgrs3_3n.gmx")
#     
#     model = ModelLib(libfile, gmxfile=gmxfile)
#     print(model)
