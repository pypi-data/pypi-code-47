#-*- coding: ISO-8859-15 -*-
#===============================================================================
# $Id: _modelcontainer.py 4744 2018-04-11 12:00:13Z jeanluc $
#  Module  _modelcontainer
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
Created on 30 dï¿œc. 2009

@author: Jean-Luc PLOIX
'''
import shutil as sh
import sys
import numpy as np
import numpy.random as rnd
import os, csv
import pickle as pcl
import json
import tempfile as tf
from xml.sax.saxutils import escape, unescape
from math import sqrt, floor

from ..Property import Property, Properties
from ..util.monalbase import internalversion ,importXML, importPickle  #savePickle, saveJSon, 
from ..model import Model
from ..util.monaltoolbox import register
from ..util.utils import configdict, getsitepackage, compileAsDll, \
    safemakedirs, CCharOnlys, create_lib, defaultIncludelist  
# compileAsExtension, \    
from ..util import toolbox as tb
# from ...nntoolbox.constants import USE_PARALLEL_COMPILE
from .. import monalconst as C
from ..lcode import codeconst as CC
from ..lcode.codewriterC import CodeWriterC, createCodeWriter

(ms_serie, ms_parallel) = list(range(2))

@Properties(("targets", "targetname", "codeWriter", "verbose"), False)
class Multimodel(Model):
    
    _models = []
    def __init__(self, owner=None, model=None, name="", filename="", verbose=0, 
                 progress=None):
        self.style = ms_serie
        self.biasBaseId = []
        self.outputLinkId = []
        self._weights = None
        self._targets = []
        self._targetname = ""
        self._codeWriter = None
        self._verbose = verbose
        self.targetfile = ""
        #self._models = []
        #self.propertyname = ""
        if isinstance(model, str):
            name = model
            model = None
        if model and not name:
            name = model.name
            model.name = model.name + "_inside"
        super(Multimodel, self).__init__(owner, name)
        if model:
            self._models = [model]
        elif filename and os.path.exists(filename):
            self.targets, (modelname, self._targetname) = \
                self.loadMultiModelFromFile(filename, progress)
            self.name = modelname if modelname else self.name
        else:
            self._models = []
        self._paramDict = {}
        self._modelType = 2

    def __del__(self):
        # les modeles sont propriï¿œtï¿œ du composant self.
        # Ils sont donc dï¿œtruits automatiquement
        for reseau in self.models:
            reseau.__del__()
        self._models = []
        super(Multimodel, self).__del__()
    
    @property
    def isParallel(self):
        return self.style == ms_parallel
    
    @property
    def isLinear(self):
        res = True
        for model in self.models:
            res = model.isLinear
            if not res:
                break;
        return res
    
    def setWeights(self, weights):
        if weights is not None:
            # si weights est fourni, il est capturï¿œ par le reseau
            #if isinstance(weights, tuple):
            #    self._weights = np.array(weights)
            #else:
            self._weights = np.asarray(weights).copy()
            for model in self.models:
                model.setWeights(self._weights)
    
    def getoutputLinks(self):
        self.outputLinkId = []
        for model in self._models:
            if hasattr(model, "outputLinks"):
                for val in model.outputLinks:
                    if not val in self.outputLinkId:
                        self.outputLinkId.append(val)
            else:
                try:
                    model.organize(self._weights)
                    source = model
                except:
                    model.mainModel.organize(self._weights)
                    source = model.mainModel
                node = source.nodes[-1]
                lst = (syn for syn in node.links if (syn.originalid < C.FIX_LIMIT) and not (syn.originalid in self.outputLinkId))
                for syn in lst:
                    if syn.name.startswith('bias'):
                        self.outputLinkId.insert(0, syn.originalid)
                    else:
                        self.outputLinkId.append(syn.originalid)
        return self.outputLinkId;            
    
    def getBiasBased(self):
        self.biasBaseId = []
        for model in self._models:
            if hasattr(model, "biasBased"):
                for val in model.biasBased:
                    if not val in self.biasBaseId:
                        self.biasBaseId.append(val)
            else:
                try:
                    model.organize(self._weights)
                    source = model
                except:
                    model.mainModel.organize(self._weights)
                    source = model.mainModel
                for val in source.biasOrigin():
                    if not val in self.biasBaseId:
                        self.biasBaseId.append(val)
        return self.biasBaseId
    
    def loadMultiModelFromFile(self, filename, progress=None):
        self._models = []
        targetlist = []
        commonpath = os.path.dirname(filename)        
        with open(filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=";", quotechar='"')
            for i, row in enumerate(reader):
                if not i:
                    row0 = tuple(row)
                    continue
                modelfile = os.path.join(commonpath, row[0])
                model = importXML(self, modelfile, quiet=True)
                if model is None:
                    model = importPickle(self, modelfile)
                model.useOriginal = True
                self._models.append(model)
                targetlist.append(tb.floatEx(row[1]))
                if progress:
                    progress(i-1)
        targetlist = np.array(targetlist)
        #self._models = modellist
        self.style = ms_parallel
        dim = max((model.computeDimension() for model in self._models))
        self._weights = np.zeros((dim,))
        for model in self._models:
            model._weights = self._weights
        # mettre ici les poids des modeles dans le container si possible
        # sinon
        self.biasBaseId = self.getBiasBased()
        self.outputLinkId = self.getoutputLinks()
        #=======================================================================
        # for model in self._models:
        #     model.organize(self._weights)
        #     for val in model.biasOrigin():
        #         if not val in self.biasBaseId:
        #             self.biasBaseId.append(val) 
        #=======================================================================
        self.initWeights(bias0=True)
        return targetlist, row0
        
    @Property
    def paramCount(self):
        if self.style == ms_serie:
            return sum([model.paramCount for model in self._models])
        if self._weights is None:
            return max(model.paramCount for model in self._models)
        return len(self._weights)
    
    @Property
    def inputCount(self):
        if len(self._models):
            return self._models[0].inputCount
        return 0
    
    @Property
    def outputCount(self):
        if len(self._models):
            return self._models[-1].outputCount
        return 0
    
    @Property
    def hiddenCount(self):
        return sum([model.hiddenCount for model in self._models])
    
    @Property
    def iputNodes(self, index):
        if len(self._models):
            try:
                return self._models[0].inputNodes[index]
            except AttributeError:
                return self._models[0].mainModel.inputNodes[index]
        return None
    
    @iputNodes.lengetter
    def linputNodes(self):
        return self.inputCount

    @Property
    def outputNodes(self, index):
        if len(self._models):
            try:
                return self._models[-1].outputNodes[index]
            except AttributeError:
                return self._models[-1].mainModel.outputNodes[index]
        return None
    
    @outputNodes.lengetter
    def loutputNodes(self):
        return self.outputCount

    def doSaveParameters(self, target, savingformat=C.SF_XML):
        #if savingformat == C.SF_XML:
        #    return target.write(self.xml())
        res = -1
        if savingformat == C.SF_BINARY:
            res = pcl.dump(self._weights, target, pcl.HIGHEST_PROTOCOL)
        elif savingformat == C.SF_JSON:
            return json.dump(self.weights, target)
        elif savingformat == C.SF_ASCII:
            res = 0
            dct = self.getParamDict()
            if self.targetname:
                target.write("# %s"% self.targetname)
            target.write("parameters\n")
            target.write("count=%d\n"% self.dimension)
            for i, val in enumerate(self.weights):
                name = dct[i]
                target.write("%s;%18.15g\n"%(name, val)) 
            return res
        
    def paramNames(self, index, original=False):
        if original and hasattr(self, "originalWeightNames"):
            try:
                return self.originalWeightNames[index]
            except IndexError:
                print("index = %d"% index)
                raise
        dct = self.getParamDict()
        if index in list(dct.keys()):
            return dct[index]
        if str(index) in list(dct.keys()):
            return dct[str(index)]
        return "W_%d"% index
    
    def linkName(self, index): 
        return self.paramNames(index, True)   
        
    def saveParameters(self, filename, savingformat=C.SF_XML):
        if savingformat in [C.SF_ASCII, C.SF_BINARY, C.SF_JSON]:
            with open(filename, "w") as ff:
                return self.doSaveParameters(ff, savingformat)
        return -1
                    
    def getParamDict(self):
        if self._paramDict:
            return self._paramDict
        self._paramDict = {}
        for model in self.models:
            try:
                newd = model.getParamDict()
            except AttributeError:
                newd = model.mainModel.getParamDict()
            for key, value in list(newd.items()):
                if not (key in self._paramDict):
                    self._paramDict[key] = value
            if len(self._paramDict) == self.dimension:
                break
        return self._paramDict           
    
    def saveToFile(self, target, roottag=C.ROOT_TAG):
        indent = '\t'
        with open(target, 'w') as ff:
            ff.write('<?xml version="1.0" encoding="ISO-8859-1"?>\n')
            ff.write('<%s version="%s"%s'% (roottag, internalversion, '>\n'))
            for item in self.xmllst(indent):
                ff.write(indent + item + '\n')
            ff.write('</%s>'% roottag)
            
    def maxParam(self):
        return max([model.maxParam() for model in self._models])
    
    def connectInputs(self, value):
        self._models[0].connectInputs(value)
    
    def __call__(self, inputs=None, computelevel=C.ID_COMPUTE, jacobian=None):
        if computelevel == C.ID_COMPUTE:
            lst = [mod(inputs) for mod in self._models] 
            return np.array(lst).squeeze()
        if computelevel == C.ID_DIFF:
            if jacobian is not None:
                lst = [mod(inputs, computelevel, jacobian[ind]) for ind, mod in enumerate(self._models)]                
            else:
                lst = [mod(inputs, computelevel) for mod in self._models]
            outs = np.array([res[0] for res in lst]).squeeze()
            if jacobian is not None:
                jacob = jacobian
            else:
                jacob = np.array([res[1] for res in lst]).squeeze()
            return outs, jacob
        
    def transfer(self, inputs=None, style=0):
        self.curinputs = inputs
        return self.transferil(style=style)
    
    def transferil(self, style=0):
        if self.style == ms_serie:
            # reprendre ici en fonction de style
            clevel = C.ID_COMPUTE
            return self.propagate(self.curinputs, computelevel=clevel)
        
        # self.style == ms_parallel
        if not style:  # transfer simple
            res = np.zeros((self.modelCount, ))
            for ind, model in enumerate(self._models):
                res[ind] = model.transfer(self.curinputs)[0]
            return res
        if style == 1:
            outputs = np.zeros((self.modelCount, ))
            jacobian = np.zeros((self.modelCount, self.dimension))
            for ind, model in enumerate(self._models):
                res = model(self.curinputs, C.ID_DIFF, gradient=jacobian[ind])
                outputs[ind] = res[0]
                #jacobian[ind] = res[1]
            return outputs, jacobian
    
    @Property
    def dimension(self):
        if self._weights is not None:
            return len(self._weights)
        lst = [model.dimension for model in self._models]
        if len(lst):
            return max(lst)
        return 0
    
    def propagate(self, inputs=None, computelevel=C.ID_COMPUTE):#, innormalized=False, outnormalized=False
        for ind, model in enumerate(self._models):
            if ind or (inputs is None):
                model.propagate(None, computelevel)
#            elif innormalized:
#                model.outputs.assign(inputs)
            else:
                model.inputs.assign(inputs)
                model.propagate(None, computelevel)
        return self     
    
    def backPropagate(self, gradient=None, gradOutput=None, computelevel=C.ID_COMPUTE):
        gradOut = gradOutput
        for model in self._models[::-1]:
            gradIn = np.copy(gradOut)
            gradient, gradOut = model.backPropagate(gradient, gradIn, computelevel)
        # attention en dessous: le copy est obligatoire    
        return gradient, np.copy(gradOut)
        
    def xmlChildren(self, indent='\t'):
        def comline(ind, comment): 
            if not ind: return '%s<COMMENT>%s</COMMENT>'% (indent, escape(comment))
            return '%s<COMMENT item="%d">%s</COMMENT>'% (indent, ind, escape(comment))
        return [comline(ind, comment) for ind, comment in enumerate(self._comments)]
        
    @classmethod
    def createFromElementXML(cls, owner, element, localversion):
        name = element.get("name", "")
        name = element.get("modelname", name)
        res = cls(owner, name)
        res._tagname = element.tag
        res._inputcount = int(element.get("inputs", "0"))
        res._outputcount = int(element.get("outputs", "0"))
        for subelmt in element.getchildren():
            if subelmt.tag == "COMMENT": 
                res.addComment(unescape(subelmt.text))
            else:
                res.includeSubElement(res._models, subelmt, localversion, cond = None)
        return res

    @Property
    def modelCount(self):
        return len(self._models)
    
    @Property
    def weights(self, index):
        if self.style==ms_parallel:
            return self._weights[index]
        cum = 0
        for model in self._models:
            old = cum
            cum += model.synapseCount
            if index < cum:
                return model.weights[index - old]
    @weights.lengetter
    def weights(self):
        if self.style==ms_serie:
            return sum([len(model.weights) for model in self._models])
        return len(self._weights)
    @weights.setter
    def weights(self, index, value):
        if self.style==ms_parallel:
            self._weights[index] = value
        else:
            cumul = 0
            old = 0
            for model in self._models:
                old = cumul
                cumul += len(model.weights)
                if index < cumul:
                    model.weights[index - old] = value
                    break
        
    @Property
    def synapseCount(self):
        if self.style == ms_serie:
            return sum([model.synapseCount for model in self._models])
        return self.dimension
        
    @Property
    def models(self, index):
        return self._models[index]
    @models.setter
    def models(self, index, value):
        self._models[index] = value
    @models.lengetter
    def lmodels(self):
        return len(self._models)
    
    def appendModel(self, target, forcenames=False):
        target.owner = self
        return self.insertModel(len(self._models), target, forcenames=forcenames)
    
    def insertModel(self, index, target, forceplace=False, forcenames=False):
        if not target:
            return
        try:
            target.trainable = self.trainable
        except: pass
        target.owner = self
        if not forceplace:
            self._models.insert(index, target)
        else:
            while (len(self._models) < index):
                self._models.append(None)
            if len(self._models) > index:
                self._models[index] = target
            else:
                self._models.insert(index, target)
        index = self._models.index(target)
        if forcenames:
            if index < len(self._models)-1:
                nextmodel = self._models[index + 1]
                for ind in range(target.outputCount):
                    nextmodel.inputNames[ind] = target.outputNames[ind]
            if index > 0:
                prevmodel = self._models[index - 1]
                for ind in range(target.inputCount):
                    prevmodel.outputNames[ind] = target.inputNames[ind]
                
    def removeModel(self, target):
        if isinstance(target, int):
            target = self._models[target]
        if target is None:
            raise IndexError
        self._models.remove(target)  
        self.chainModels()
        return target
    
    def modelIndex(self, target):
        for ind, model in enumerate(self._models):
            if model == target:
                return ind
        return -1
        
    @Property
    def inputs(self):
        return self._models[0].inputs
    
    @Property
    def outputs(self):
        return self._models[-1].outputs
    
    @Property
    def inputNames(self, index):
        return self._models[0].inputNames[index]
    @inputNames.lengetter
    def linputNames(self):
        if self._models:
            return self._models[0].inputCount
        return 0
    @inputNames.setter
    def sinputNames(self, index, value):
        self._models.inputNames[index] = value
    
    @Property
    def outputNames(self, index):
        return self._models[-1].outputNames[index]
    @outputNames.lengetter
    def loutputNames(self):
        if self._models:
            return self._models[-1].outputCount
        return 0
    @outputNames.setter
    def soutputNames(self, index, value):
        self._models[-1].outputNames[index] = value
        
    def initWeights(self, stddev=0.3, bias0=True):
        if self.style == ms_parallel:
            dim = self.dimension
            #dim = len(self._weights)
            self._weights = rnd.randn(dim)*stddev
            if bias0:
                for i in self.biasBaseId:
                    self._weights[i] = 0.0            
            for model in self.models:
                model.setWeights(self._weights)
        else:
            for model in self.models:
                model.initWeights(stddev, bias0)
                
    def readUnitFile(self):
        if hasattr(self, "unitfilename") and self.unitfilename:
            unitnet = importXML(self, self.unitfilename, quiet=True)
            self.inputParameters = list(unitnet.inputNames)
            self.originalWeightNames = [unitnet.paramNames(i) for i in range(unitnet.paramCount)]
        
    def saveModel(self, modelfolder, savingformat=C.SF_XML, modeltemplate="m%03d_", 
            package="models", progress=None, keeptemp=False, callback=None, compiler="",
            moduletype="dll", tempdir="", writer=sys.stdout, forcelib=False):  # Multimodel
        res = 0
        muststop = 0
        if self.biasBaseId == []:
            self.biasBaseId = self.getBiasBased()
        if self.outputLinkId == []:    
            self.outputLinkId = self.getoutputLinks()
        if savingformat == C.SF_CPYTHON:
            res = self.saveModelPython(modelfolder, modeltemplate, "", progress, 
                keeptemp, callback, compiler=compiler, moduletype=moduletype, 
                tempdir=tempdir, writer=writer, forcelib=forcelib)
        elif not savingformat in [C.SF_BINARY, C.SF_XML, C.SF_ASCII, C.SF_DLM, 
                                  C.SF_JSON, C.SF_CCODE]:
            res = self.saveObj(self, filename, savingformat)
        else:
            res = 0
            for index, model in enumerate(self._models):
                model.noname = True
                modname = (modeltemplate + "%s")% (index+1, C.extfmt[savingformat])
                targetfilename=os.path.join(modelfolder, modname) 
                res = model.saveModel(targetfilename, savingformat, index+1)
                model.noname = False
                if progress:
                    progress(index+1)
            if progress:
                progress.flush()
        return res or muststop
    
#     def saveModelPython(self, modelfolder, modeltemplate="m%03d_", 
#                 package="models", progress=None, keeptemp=False, 
#                 callback=None, compiler="", moduletype="dll",
#                 tempdir="", writer=sys.stdout, forcelib=False):
#         if progress:
#             progress(0)  # -10
#         res = 0
#         self.targetfile = ""
#         muststop = 0
#         if not tempdir:
#             if keeptemp and (keeptemp != 1):
#                 savedir = os.path.join(tf.gettempdir(), str(keeptemp))
#                 tb.cleanDir(savedir, doprint=True, stoponerror=False, writer=writer)
#             else:
#                 savedir = tf.mkdtemp(prefix="$PyExt") 
#             if keeptemp:
#                 message = 'folder "%s" will be kept\n' % savedir
#                 writer.write(message)
#             elif (self.verbose >= 3):
#                 print(savedir)
#             for index, model in enumerate(self._models):
#                 # boucle de creœation des codes C des modœles œlœmentaires
#                 model.noname = True
#                 if progress:
#                     progress(index+1)
#                 targetfilename=os.path.join(savedir, modeltemplate% (index+1)) 
#                 res = model.saveModel(targetfilename, C.SF_CCODEMULTI, index+1)
#                 model.noname = False
#             if progress:
#                 progress.flush()
#         else:
#             savedir = tempdir
#         
#         if callback:
#             muststop = callback(2)
#         packname = package
#         destdir="build"
#         
#         codeWriter = createCodeWriter(self, savedir=savedir, 
#             trainable=True, verbose=self.verbose)
#         codeWriter.moduleName = packname
#         
#         namel = CCharOnlys(self.name.lower(), nostartint=True)
#        
#         for code in CC.PyCodeMulti:
#             codeWriter.CodeFichier(code, included=1, dosave=True)
#             codeWriter.CodeFichier(code, dosave=True)
#             
#         excluded = ["{}dll.c".format(namel), "{}trainbase.c".format(namel)] 
# #         excluded = ["%sdll.c"% namel] 
#         blocksize = max(10, int(floor(sqrt(self.modelCount + 1))))
# #         libname = "stat_{0}".format(namel)
#         libname = namel
#         # creation des codes O communs a la base
#         # et groupement par 'blocksize' dans des libraries statiques
# # def create_lib(compiler, libname, source_dir="", target_dir="", sub_lib_dir="",
# #             include_dirs=[], excluded=[], extra_preargs=[], doprint=False, 
# #             freesource=False, blocksize=0, progress=None, maxworkers=-2, 
# #             debug=0):
#         liblist = create_lib(compiler, libname=libname, source_dir=savedir, 
#             include_dirs=defaultIncludelist, target_dir=destdir, 
#             excluded=excluded, extra_preargs=['-fPIC'],
#             blocksize=blocksize, progress=progress)
#         
#         sourcedir = codeWriter.SaveDir
#         
#         pathmem = os.getcwd()
#         os.chdir(savedir)
#         filelist = []
#         includedirs = defaultIncludelist  #[]         
#         
#         if moduletype in ["so", "dll", "dylib"]:
#             mainfile = "%sdll.c"% namel
#             savedirloc = os.path.dirname(modelfolder)
#             self.targetfile = compileAsDll(mainfile, filelist, savedir=savedirloc, 
#                 destdir=destdir, includedirs=includedirs, compiler=compiler, 
#                 progress=progress, verbose=self.verbose, writer=writer, 
#                 forcelib=forcelib, additionallibs=liblist) 
# 
#         os.chdir(pathmem) 
#         
#         originpackname = packname
#         if not modelfolder:
#             # si on ne demande pas de repertoire d'installation, alors l'installation 
#             modelfolder = getsitepackage()
#             packname = os.path.join(packname, self.name[:self.name.index("_")]) 
#             
#         if modelfolder:
#             sourcepack = os.path.join(sourcedir, originpackname)
#             if modelfolder.endswith((".pyd", ".dll", ".so", ".dylib")):
#                 savepack = os.path.dirname(modelfolder)
#             else:
#                 savepack = os.path.join(modelfolder, packname)
#             if packname != originpackname:
#                 fatherpack = os.path.join(modelfolder, originpackname)
#                 tb.make_dir(fatherpack, self.verbose, writer)
#             tb.make_dir(savepack, self.verbose, writer) # 
#             for root, _, files in os.walk(sourcepack):
#                 for ffile in files:
#                     base, ext = os.path.splitext(ffile)
#                     base = os.path.basename(base)
#                     if ext in [configdict['SO'], ".dll", ".so", "dylib"]: 
#                         try:
#                             filename = os.path.join(root, ffile)
#                             sh.copy(filename, os.path.join(savepack, ffile))
#                             if ext == "pyd":  
#                                 tb.adduniqueline("import %s"% base, os.path.join(savepack, "__init__.py"))
#                         except: pass              
#             
#         if not (bool(keeptemp) & CC.KT_AFTER):
#             tb.cleanDir(sourcedir, remove=True, doprint=self.verbose, writer=writer)           
# #         codeWriter.__del__()
#         codeWriter = None
#         if progress:
#             progress(-11)
# 
#         return res or muststop
#          
# #     def createCodeWriter(self, targetLang="C", savedir="", original=True):  # Driver 
# #         if targetLang == "C":
# #             #self._codeWriter
# #             CW = CodeWriterC(None, self)
# #         CW.SaveDir = savedir
# #         CW.originallink = original
# #         if not CW.SaveDir:
# #             CW.SaveDir = tb.tempDir("model")
# #         tb.make_dir(CW.SaveDir, self.verbose)
# #         return CW
    def saveModelPython(self, modelfolder, modeltemplate="m%03d_", 
                package="models", progress=None, keeptemp=False, 
                callback=None, compiler="", moduletype="dll",
                dynamiclinking=False, tempdir="", writer=sys.stdout, 
                forcelib=False):
        if progress:
            progress(0)  # -10
        res = 0
        self.targetfile = ""
        muststop = 0
        if not tempdir:
            if keeptemp and (keeptemp != 1):
                savedir = os.path.join(tf.gettempdir(), str(keeptemp))
                tb.cleanDir(savedir, doprint=True, stoponerror=False, writer=writer)
            else:
                savedir = tf.mkdtemp(prefix="$PyExt") 
            if keeptemp:
                message = 'folder "%s" will be kept\n' % savedir
                writer.write(message)
            elif (self.verbose >= 3):
                print(savedir)
            for index, model in enumerate(self._models):
                # boucle de creœation des codes C des modœles elementaires
                model.noname = True
                if progress:
                    progress(index+1)
                targetfilename=os.path.join(savedir, modeltemplate% (index+1)) 
                res = model.saveModel(targetfilename, C.SF_CCODEMULTI, index+1)
                model.noname = False
            if progress:
                progress.flush()
        else:
            savedir = tempdir
        
        if callback:
            muststop = callback(2)
        packname = package
        destdir="build"
#        destdir="."   !!!!!!!!!!!!!!!  ici  !!!!!!!!!!!!!!!!! 12/01/20
        
        codeWriter = createCodeWriter(self, savedir=savedir, 
            trainable=True, verbose=self.verbose)
        codeWriter.moduleName = packname
        
        namel = CCharOnlys(self.name.lower(), nostartint=True)
       
        for code in CC.PyCodeMulti:
            codeWriter.CodeFichier(code, included=1, dosave=True)
            codeWriter.CodeFichier(code, dosave=True)
            
        excluded = ["{}dll.c".format(namel), "{}trainbase.c".format(namel)] 
#         excluded = ["%sdll.c"% namel] 
        blocksize = max(10, int(floor(sqrt(self.modelCount + 1))))
        # creation des codes O communs a la base
        # et groupement par 'blocksize' dans des libraries statiques
#         liblist = create_stat_lib(compiler, libname=libname, source_dir=savedir, 
#             include_dirs=defaultIncludelist, target_dir=destdir, 
#             excluded=excluded, extra_preargs=['-fPIC'],
#             blocksize=blocksize, progress=progress, doparallel=USE_PARALLEL_COMPILE)
        libdir = os.path.dirname(modelfolder)
        # libdir is destination path of library        
        # sub_lib_dir is destination path of sub dynamic libraries
        if dynamiclinking:
            sub_lib_dir = destdir  #libdir
            libname = "_shared_{0}".format(namel)            
        else:
            sub_lib_dir = ""
            libname = "_stat_{0}".format(namel)
        
        liblist = create_lib(compiler, libname=libname, source_dir=savedir, 
            include_dirs=defaultIncludelist, target_dir=destdir, 
            sub_lib_dir=sub_lib_dir, excluded=excluded, extra_preargs=['-fPIC'],
            blocksize=blocksize, progress=progress)
        
        sourcedir = codeWriter.SaveDir
        
        pathmem = os.getcwd()
#        additionallibs = liblist
        destlibdir = libdir if dynamiclinking else ""
        os.chdir(savedir)

        includedirs = defaultIncludelist  #[] 
        mainfile = "{}dll.c".format(namel)
        filelist = [val for val in excluded if val != mainfile]        
        
        if moduletype in ["so", "dll", "dylib"]:
            self.targetfile = compileAsDll(mainfile, filelist, savedir=libdir, 
                destdir=destdir, includedirs=includedirs, 
                compiler=compiler, progress=progress, verbose=self.verbose, 
                writer=writer, forcelib=forcelib, additionallibs=liblist) # destlibdir=destlibdir, 

        os.chdir(pathmem) 
        
        originpackname = packname
        if not modelfolder:
            # si on ne demande pas de repertoire d'installation, alors l'installation 
            modelfolder = getsitepackage()
            packname = os.path.join(packname, self.name[:self.name.index("_")]) 
            
        if modelfolder:
            sourcepack = os.path.join(sourcedir, originpackname)
            if modelfolder.endswith((".pyd", ".dll", ".so", ".dylib")):
                savepack = os.path.dirname(modelfolder)
            else:
                savepack = os.path.join(modelfolder, packname)
            if packname != originpackname:
                fatherpack = os.path.join(modelfolder, originpackname)
                tb.make_dir(fatherpack, self.verbose, writer)
            tb.make_dir(savepack, self.verbose, writer) # 
            for root, _, files in os.walk(sourcepack):
                for ffile in files:
                    base, ext = os.path.splitext(ffile)
                    base = os.path.basename(base)
                    if ext in [configdict['SO'], ".dll", ".so", "dylib"]: 
                        try:
                            filename = os.path.join(root, ffile)
                            sh.copy(filename, os.path.join(savepack, ffile))
                            if ext == "pyd":  
                                tb.adduniqueline("import %s"% base, os.path.join(savepack, "__init__.py"))
                        except: pass              
            
        if not (bool(keeptemp) & CC.KT_AFTER):
            tb.cleanDir(sourcedir, remove=True, doprint=self.verbose, writer=writer)           
#         codeWriter.__del__()
        codeWriter = None
        if progress:
            progress(-11)

        return res or muststop


register(Multimodel)
register(Multimodel, "MULTIMODEL")

if __name__ == "__main__":
    import time
    testpath = os.path.join (os.path.dirname (__file__), "..", "..", "..", "testFiles", "Models_2N")
    testpath = os.path.normpath(testpath)
    testfile = os.path.join(testpath, "data.csv")
    commonpath = testpath  
    
    #driver = Multimodel(filename=testfile)
    #pr int "linear :", driver.isLinear
    #driver.initWeights()
    #p rint driver._weights
    #pr int driver.transfer()
    lst = []
    before = time.time()
    with open(testfile, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=";", quotechar='"')
        for i, row in enumerate(reader):
            if not i:
                lst.append(row)
                continue
            modelfile = os.path.join(commonpath, row[0])
            model = importXML(None, modelfile)
            model.useOriginal = True
            lst.append((model, row[1]))
    after = time.time()
    loadxmltime = after - before
    print("loading XML time :", loadxmltime)
    
    
    targetpath = os.path.join (os.path.dirname (__file__), "..", "..", "..", "testFiles", "Models_2N_pcl") 
    targetpath = os.path.normpath(targetpath)
    targetfile = os.path.join(targetpath, "data.csv")
    modelpath = targetpath
    safemakedirs(modelpath)
    safemakedirs(targetpath)
    #if not os.path.exists(modelpath):  
        #os.m akedirs(modelpath) 
    #if not os.path.exists(targetpath):
    #    os.m akedirs(targetpath) 
    
    before = time.time()
    with open(targetfile, 'wb') as csvfile:
        for ind, (model, value) in enumerate(lst):
            if not ind:
                csvfile.write("%s;%s\n" %(model, value))
                continue
            filename = os.path.join(modelpath, "model_%d"% (ind))
            model.saveModel(filename, C.SF_BINARY)
            csvfile.write("%s;%s\n"%(os.path.basename(filename), value))
    after = time.time()
    savejsontime = after - before
    print("saving Pickle time :", savejsontime)
    
    lst2 = []
    before = time.time()
    with open(targetfile, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=";", quotechar='"')
        for i, row in enumerate(reader):
            if not i:
                lst2.append(row)
                continue
            modelfile = os.path.join(modelpath, row[0])
            model = importPickle(None, modelfile)
            model.useOriginal = True
            lst2.append((model, row[1]))
    after = time.time()
    loadjsontime = after - before
    print("loading Pickle time :", loadjsontime)
    
__all__ = ["Multimodel", "ms_serie", "ms_parallel"]    
    
        
