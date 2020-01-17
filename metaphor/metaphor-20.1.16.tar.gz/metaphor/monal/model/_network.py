# -*- coding: ISO-8859-15 -*-
#===============================================================================
# $Id: _network.py 4819 2018-11-02 05:32:25Z jeanluc $
#  Module  _network
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
#from __fu ture__ import absolute_import
import os
from itertools import chain
from numpy import newaxis, load, ndarray, ones, zeros, random, zeros_like, \
    asarray
from numpy.lib.npyio import NpzFile
from xml.sax.saxutils import escape, unescape
from xml.etree.cElementTree import fromstring, parse
from collections import defaultdict
from functools import cmp_to_key

from ...nntoolbox.utils import floatEx
from .. import monalconst as C
from ..Property import Property
#from ...monal.util.utils import ChildElementList
from ._model import Model
from ._node import Basenode, Node, newNode
from ._link import Synapse 
from ..util.monaltoolbox import register
from ..util.const_st import st_WEIGHTS, st_REAL
from ..util.monalbase import NodeError#, importPickle #, savePickle, saveJSon

class Basenetwork( Model ):
    """classe de base des reseaux de neurones.
Prend en charge l'usine de construction et modification des reseaux."""
    
    def __init__(self, owner=None, name=""):  # Basenetwork
        # owner peut etre un model ou un driver
        super(Basenetwork, self).__init__(owner, name)
        self._inputDim = 1
        self._inputCount = 0
        self._outputCount = 0
        # creation du biais
        self.bias = Node(self, name="bias", layer=-1, style=C.NS_CONST)
        self.bias.value = 1.0 
        self.bias.nodeid = 0
        # initialisations
        self.nodes = []
        self._weights = zeros(0)
        self._parambackup = ""
        self._lastFix = C.FIX_LIMIT
        self._tagname = 'NETWORK'
        self.GradientInput = None
        self.style = 0
        self._computelevel = 0
        #self.outputWeighting = None
        #return self
        #self._useOriginal = False

    def __del__(self):  # Basenetwork
        #for node in self.nodes:
        #    node.__del__()
        self.nodes = []
        self._weights = None
        super(Basenetwork, self).__del__()
    
    def reprlst(self):  # Basenetwork
        lst = super(Basenetwork, self).reprlst()
#        lst.append("name : {0}".format(self.name))
        if self.inputCount:
            lst.append("inputs : {0}".format(self.inputCount))
        lst.append("outputs : {0}".format(self.outputCount))
        if hasattr(self, 'hidden'):
            lst.append("hidden : {0}".format(self.hidden))
        lst.append("paramCount : {0}".format(self.paramCount))
        longParamCount = len(self.weights)
        if longParamCount != self.paramCount:
            lst.append("longParamCount: {0}".format(longParamCount))
        lst.append("nodes : {0}".format(len(self.nodes)))
        lst.append("layers : {0}".format(self.layerCount))
        return lst
    
    #===========================================================================
    # @Property
    # def nodes(self, index):
    #     return self.nodes[index]
    # @nodes.lengetter
    # def lnodes(self):
    #     return len(self.nodes)
    #===========================================================================
    
    def formula(self, inlist=False, exploded=True):
        if exploded:
            source = self.nodes[self.inputCount:]
        else:
            source = self.nodes[-self.outputCount:]
        lst = ["{0} = {1}".format(node.name, node.formula(exploded)) for node in source]
        if inlist:
            return lst
        return "\n".join(lst)
    
    def getIsLinear(self):
        result = True
        for node in self.nodes:
            result = node.activation in ["", "ident"]
            if not result:
                break
        return result
    
    @Property
    def defaultName(self):
        ni = self.inputCount
        nh = self.hiddenCount
        no = self.outputCount
        return "nn_{0}_{1}_{2}".format(ni, nh, no)
    
    def exportWeights(self):  # Basenetwork
        # copie des poids des synapses dans le vecteur de papametres
        self._weights = zeros(self.longParamCount)
        for syn in self.links:
            if not syn.isFix():
                if self._useOriginal:
                    index = syn.originalid
                else:
                    index = syn.linkid
                self._weights[index] = syn.value
    
    @Property
    def useOriginal(self):  # Basenetwork
        return self._useOriginal
    @useOriginal.setter
    def suseOriginal(self, value):
        self._useOriginal = value
        for node in self.nodes:
            node.useOriginal = value
    
    def singleGradient(self):  # Basenetwork
        return True
    
    def doSaveParameters(self, target, savingformat=C.SF_XML):  # Basenetwork
        return self.doSaveObj(target, self._weights, savingformat)
    
    def compchildren(self, c1, c2):  # Basenetwork
        try:
            if c1.nodeid > c2.nodeid:
                return 1
            if c1.nodeid < c2.nodeid:
                return -1
            return 0
        except:
            return 0
    
    def computedNodes(self, freeOnly=False):  # Basenetwork
        if not freeOnly:
            return (node for node in self.nodes if node.nodeid -1 >= self.inputCount)
        id1 = self.firstFreeNode().nodeid
        return (node for node in self.nodes if node.nodeid >= id1)
    
    def firstFreeNode(self):  # Basenetwork
        for node in self.nodes:
            if not node.IsFixed(True):
                return node
        return None
    
    def inStateNodes(self):  # Basenetwork
        return (node for node in self.nodes if self.inputCount <= node.nodeid -1 < self.inputCount + self.order)
    
    def outStateNodes(self):  # Basenetwork
        return (node.links[0].source for node in self.inStateNodes())
    
    def equivalent(self, target, withException=False):  # Basenetwork
        eq = self.nodeCount == target.nodeCount
        for node1, node2 in zip(self.nodes, target.nodes):
            eq &= node1.equivalent(node2, withException) and (node1.activation == node2.activation)
            if withException and not eq:
                raise AssertionError("Different node activation {0}: {1}, {2}: {3}".format(node1.nodeid, node1.activation, node2.nodeid, node2.activation))                
        return eq
        
    def biasOrigin(self):  # Basenetwork
        res = []
        for syn in self.bias.downLinks:
            val = syn.originalid
            if not val in res and not syn.isFix():  #syn.name.startswith("bias") and (val < int('0x7fff', 16)
                res.append(val)
        return res
    
    def setWeights(self, weights):  # Basenetwork
        if weights is not None:
            # si weights est fourni, il est capturé par le reseau
            self._weights = asarray(weights)
    
    def __setstate__(self, state):  # Basenetwork
        self.__dict__.update(state)
        self.reconnect()
    
    def __getstate__(self):  # Basenetwork
        objdict = self.__dict__.copy()      
        return objdict
    
    def reconnect(self, owner=None):  # Basenetwork
        # - etablissement du proprietaire
        # - branchement des liaisons pendantes
        self.owner = owner
        for node in self.nodes:
            node.reconnect(self)
    
    def getBiasBased(self):
        res = []
        mem = None
        if self._weights is not None:
            mem = self._weights.copy()
        self.organize(self._weights)
        for val in self.biasOrigin():
            if not val in res:
                res.append(val)
        self._weights = mem
        return res
    
    def getOutputLinks(self):
        res = []
        self.organize(self._weights)
        node = self.nodes[-1]
        lst = (syn for syn in node.links if (syn.originalid < C.FIX_LIMIT) and not (syn.originalid in res))
        for syn in lst:
            if syn.name.startswith('bias'):
                res.insert(0, syn.originalid)
            else:
                res.append(syn.originalid)
        return res
    
    def organize(self, weights=None):  # Basenetwork
        # remet tout en place:
        # - numerotation des noeuds
        # - style des noeuds
        # - branchement des liaisons pendantes
        # - tri des composants
        self.setWeights(weights)
        firstlastlayer=True
        if len(self.nodes):
            outlayer = self.nodes[-1].layer
        for index, node in enumerate(self.nodes):
            node.nodeid = index + 1
            node.style &= C.NS_NOPOS
            if not node.layer:
                node.style |= C.NS_INPUT
                #if hasattr(self, "inputCount"):
                if (self._inputCount >= 0) and (node.nodeid-1 > self._inputCount):
                    node.style |= C.NS_STATE
            elif node.layer == outlayer:
                node.style &= not C.NS_INPUT
                if firstlastlayer:
                    firstlastlayer = False
                    lastindex = -1
                lastindex+= 1
                if (self._outputCount >= 0) and (lastindex < self._outputCount):
                    node.style |= C.NS_OUTPUT                       
            else:
                node.style &= not C.NS_INPUT
            node.organize(self) 
        K = cmp_to_key(self.compchildren)
        self.components.sort(key=K)
#        self.components.sort(self.compchildren)
    
    def setSizes(self, inputcount=1, outputcount=1):  # Basenetwork
        if outputcount >= 0:
            self._outputCount = max(0, outputcount)
        if inputcount >= 0:
            self._inputCount = max(0, inputcount)
        self.organize()                
        
    def setInputSpace(self, mat):  # Basenetwork
        """fixation du domaine experimental.
    mat est une numPy.matrix de dimension (n, 2).
    Chaque ligne comprends le minimum et le maximum du noeud correspondant du reseau.
    Une valeur None n'est pas prise en compte."""
        assert(mat.shape[1] == 2)
        for vec, node in zip(mat, self.inputNodes):
            node.setMinMax(list(vec.flat))
    
    def setOutputSpace(self, mat):  # Basenetwork
        """fixation du domaine experimental de sortie.
    mat est une numPy.matrix de dimension (n, 2).
    Chaque ligne comprends le minimum et le maximum du noeud correspondant du reseau.
    Une valeur None n'est pas prise en compte."""
        assert(mat.shape[1] == 2)
        for vec, node in zip(mat, self.outputNodes):
            node.setMinMax(list(vec.flat))
    
    def getNode(self, value):  # Basenetwork
        """Looking for a node in network.
"value' argument may be :
    - a node    -> return this node
    - a name    -> return the node that hold this name, if exists
    - an index  -> return the indexed node
    - a 2-tuple (layer, index) -> return the node indexed 'index' in the layer indexed 'layer'.
return None if no node can be found."""
        if isinstance(value, Basenode):
            return value
        if isinstance(value, str):
            if value.lower() == "bias":
                return self.bias
            for anode in self.nodes:
                if anode.name == value:
                    return anode
            return None
        if isinstance(value, int):
            if not value:
                return self.bias
            for anode in self.nodes:
                if anode.nodeid == value:
                    return anode
            return None
        if isinstance(value, tuple) and (len(value) == 2):
            if value == (-1,0):
                return self.bias
            for index, anode in enumerate((bnode for bnode in self.nodes if bnode.layer == value[0])):
                if index == value[1]:
                    return anode    
        return None           
            
    def getLink(self, source, target, style=0):  # Basenetwork
        source = self.getNode(source)
        target = self.getNode(target)
        for syn in source.downLinks:
            if (syn in target.links):  # and (target.downLinks.index(syn) >= 0):
                if style:
                    if (style and syn.style):
                        return syn
                else:
                    if not syn.sytle:
                        return syn
    
    def _absoluteIndex(self, layer, pos):  # Basenetwork
        if pos == -1:
            try: pos %= self.layerLength(layer)+1
            except: pos = 0
        res = -1
        cumul = 0
        for node in self.nodes:
            if node.layer < layer:
                res += 1
            elif (node.layer == layer):
                if (cumul < pos):
                    cumul += 1
                    res += 1
        return res
    
    def insertLayer(self, name="", index=1, length=0, activfunc='', nodetype=1, stylePos=0, defaultnodevalue=0.0):  # Basenetwork
        if isinstance(name, bytes):
            nam = name.decode()
        else:
            nam = name
        lst = []
        if stylePos == C.PS_END:
            index = self.layerCount - index - 1
        for node in self.nodes:
            if (node.layer >= index):
                node.layer += 1
        self.organize()
        for i in range(length):
            if length > 1:
                lst.append(self.createNode("{0}_{1}".format(nam, i), index, i, activfunc, nodetype, defaultnodevalue)) 
            else:   
                lst.append(self.createNode(nam, index, i, activfunc, nodetype, defaultnodevalue)) 
        self.organize()
        return lst
    
    def deleteLayer(self, index=-2, style= 0):  # Basenetwork
        if (style and C.PS_END):
            index = self.layerCount - index - 1
        tokill = [(node, i) for i, node in enumerate(self.nodes) if node.layer == index]
        for node, ii in tokill[-1::-1]:
            node.isolate(True, True, style=style)
            self.nodes.pop(ii)
            node.__del__()
    
    def deleteNode(self, layer=0, lpos=-1, style=0):  # Basenetwork
        isinput = (layer == 0)
        node = self.getNode((layer, lpos))
        self.isolateNode(node, inputs=True, outputs=True, style=style)
        n = self.nodes.index(node)
        if n >= 0:
            self.nodes.pop(n)
        node.owner = None
        if isinput:
            self._inputCount -= 1
        for index, anode in enumerate(self.nodes):
            if index >= n:
                anode.nodeid -= 1
        node.__del__()
        #self.organize()  
    
    def createNode(self, name="", layer=0, lpos=-1, activ="", style=C.NS_STD, defaultnodevalue=0.0):  # Basenetwork
        anode = newNode(self, name, layer, lpos, activ, style, defaultvalue=defaultnodevalue)
        if anode.layer == -1:
            return 0
        anode.style = style & (C.NS_INPUT | C.NS_OUTPUT)
        #=======================================================================
        # n = self._absoluteIndex(layer, lpos) + 1
        # anode.nodeid = n 
        # self.nodes.insert(n, anode)
        #=======================================================================
        self.insertNode(anode, (layer, lpos))
        self.organize()
        return anode
    
    def insertNode(self, anode, index):  # Basenetwork
        if not anode:
            raise NodeError("Impossible to insert null Node")
        if isinstance(index, tuple):
            anode.layer = index[0]
            index = self._absoluteIndex(index[0], index[1]) + 1
        try:
            oldnode = self.nodes[index]
        except IndexError:
            if len(self.nodes):
                oldnode = self.nodes[-1]
            else:
                oldnode = None
        if oldnode: 
            #layer = oldnode.layer
            oldid = oldnode.nodeid
        else:
            #oldlayer = 0
            oldid = 0
        for node in self.nodes:
            if node.nodeid >= oldid:
                node.nodeid += 1
        anode.nodeid = oldid
        anode.owner = self
        self.nodes.insert(index, anode)
#        self._nodes.insert(index, wr.ref(anode))
        K = cmp_to_key(self.compchildren)
        self.components.sort(key=K)
#        self.components.sort(self.compchildren)
    
    def moveNode(self, target, source, style=0):  # Basenetwork
        sourcenode = self.getNode(source)
        if not sourcenode:
            raise IndexError()
        sourceid = sourcenode.nodeid
        sourcelayer = sourcenode.layer
        sourceindex = self.nodes.index(sourcenode)
        if isinstance(target, tuple):
            targetlayer = target[0]
            #targetpos = target[1]
            targetnode = self.getNode(target)
            if targetnode:
                targetid = targetnode.nodeid
                targetindex = self.nodes.index(targetnode)
            else:
                targetnode = self.getNode((target[0]+1, 0))
                if targetnode:
                    targetid = targetnode.nodeid
                    targetindex = self.nodes.index(targetnode)
                else:
                    targetid = self.nodes[-1].nodeid + 1
                    targetindex = len(self.nodes)
        else:
            targetnode = target
            targetlayer = targetnode.layer
            targetid = targetnode.nodeid
            targetindex = self.nodes.index(targetnode)
        
        if targetid < sourceid:
            for node in self.nodes:
                if node.nodeid < targetid:
                    continue
                elif node.nodeid < sourceid:
                    node.nodeid += 1
                elif node.nodeid == sourceid:
                    node.nodeid = targetid
                    node.layer = targetlayer
                else:
                    break
            
            if sourceindex != targetindex+1:
                node = self.nodes.pop(sourceindex)
                node.layer = targetlayer
                self.nodes.insert(targetindex, node)
        else:
            for node in self.nodes:
                if node.nodeid < sourceid:
                    continue
                elif node.nodeid == sourceid:
                    node.nodeid = targetid
                    node.layer = targetlayer
                elif node.nodeid < targetid:
                    targetid -= 1
                else:
                    break
            if targetindex-1 != sourceindex:
                node = self.nodes.pop(sourceindex)
                node.layer = targetlayer
                #self._nodes.insert(targetindex-1, node)
                self.nodes.insert(targetindex-1, node)
            
        if not sourcelayer and targetlayer:
            self._inputCount -=1
        K = cmp_to_key(self.compchildren)
        self.components.sort(key=K)
#        self.components.sort(self.compchildren) 
           
    def deleteLink(self, target=None, source=None, style=C.LS_STD, linkid=-1, name=None, adjustweights=False, **kwds):  # Basenetwork
        """delete a link 
        kwds is a garbage collector
        """
        
        target = self.getNode(target)
        source = self.getNode(source)
        if target:
            if adjustweights:
                res = target.deleteLink(source, style, linkid, name, self.weights)
                self.adjustLinkid(OkMin=res)
                return res
            else:
                return target.deleteLink(source, style, linkid, name)
        return -2
    
    def adjustLinkid(self, OkMin=1000000):
        self.bias.adjustLinkid(OkMin)
        for node in self.nodes:
            node.adjustLinkid(OkMin) 
        
    
    def createLink(self, target=None, source=None, value=0.0, style=C.LS_STD, linkid=-1, name="", **kwds):  # Basenetwork
        target1 = self.getNode(target)
        source1 = self.getNode(source)
        try:
            syn = target1.createLink(source1, value, style, linkid, name)
            syn.organize()
            return syn
        except:
            return None
    
    def createlinks(self, source=None, targetlayer=None, value=0.0, style=C.LS_STD, **kwds):  # Basenetwork
        source = self.getNode(source)
        #assert(source, "a link must have a source and a target")
        targets = self.layers(targetlayer)
        if targetlayer > source.layer:
            for target in targets:
                syn = target.createLink(source, value, style)
                syn.organize()
        else:
            if targetlayer == source.layer:
                indexes = source.getIndexes()
                targets = targets[:indexes[1]]
            for target in targets:
                syn = source.createLink(target, value, style)
                syn.organize()
    
    def mergeNode(self, target=None, source=Node, inputs=False, outputs=False, **kwds):  # Basenetwork
        target = self.getNode(target)
        if not target: 
            raise IndexError()
        source = self.getNode(source)
        if not source: 
            raise IndexError()
        source.absorb(target, inputs=inputs, outputs=outputs)
    
    def isolateNode(self, layer=0, index=-1, inputs=False, outputs=False, style=C.LS_STD, **kwds):  # Basenetwork
        if isinstance(layer, Basenode):
            node = layer
        else:
            node = self.getNode((layer, index))
            if not node: 
                raise IndexError()
        node.isolate(inputs=inputs, outputs=outputs, weights=self.weights, style=style)                       
    
    def isolateInput(self, index=None, style=C.LS_STD, **kwds):  # Basenetwork
        if isinstance(index, Basenode):
            node = index
        else:
            node = self.getNode((0, index))
            if not node: 
                raise IndexError()
        node.isolate(outputs=True, weights=self._weights, style=style)                       
    
    def layerExtend(self, index=None, source=None, **kwds):  # Basenetwork
        for node in source:
            self.insertNode(node, (index, -1))
            node.owner = self
    
    #===========================================================================
    # def setWeights(self, *args):
    #    if len(args) == 1:
    #        weights = args[0]
    #    else:
    #        weights = args
    #    for i, val in enumerate(weights):
    #        try:
    #            self.weights[i] = val
    #        except: break
    #===========================================================================
    
    @Property
    def synapseCount(self):  # Basenetwork
        lst = self.computingLinks()
        lst2 = []
        for syn in lst:
            n = syn.linkid
            if not n in lst2:
                lst2.append(n)
        return len(lst2) #len(self.weights)  #
    
    @Property
    def links(self):  # Basenetwork
        """liste de tous les liens synaptiques.
    Cette liste comprends les liens fixes et directs aussi bien que les synapses.
    Les liens partagés éventuels sont présentés une fois par occurence"""
        #return list(reduce(chain, (node.links for node in self.nodes))
        lst = list(chain.from_iterable(node.links for node in self.nodes))
        return lst
    
    def computingLinks(self, withfixed=0):  # Basenetwork
        """liste des liens synaptiques qui contribuent au calcul"""
        if withfixed:
            lst = [syn for syn in self.links if isinstance(syn, Synapse)]
        else:
            lst = [syn for syn in self.links if isinstance(syn, Synapse) and not syn.isFix()]
        return lst
    
    def link(self, index):  # Basenetwork
        if isinstance(index, str) or isinstance(index, int):
            for node in self.nodes:
                for syn in node.links:
                    if (syn.linkid == index) or (syn.name == index):
                        return syn 
        elif isinstance(index, tuple):
            if len(index) == 2: 
                return self.nodes[index[0]]._links[index[1]]
            elif len(index) == 3:
                return self.layers(index[0])[index[1]]._links[index[2]]      
        raise IndexError("cannot find link({})".format(index))
    
    def linkOriginalIdList(self, keepint=False):  # Basenetwork
        res = []
        for syn in self.computingLinks():
            ind = syn.originalid
            if not ind in res:
                res.append(ind)
        res.sort()
        if keepint:
            return res
        return [str(val) for val in res]
    
    def linkName(self, index, origin=False):  # Basenetwork
        for link in self.links:
            if origin:
                cond = (link._originalid == index)
            else:
                cond = (link.linkid == index)
            if cond:
                return link.name
        return ""
    
    def layerNodes(self, index):
        return [node for node in self.nodes if node.layer==index]
    
    def layerLength(self, index):  # Basenetwork
        #if index < 0:
        #    index += self.layerCount
        try: 
            index %= self.layerCount
            return len([1 for node in self.nodes if node.layer == index]) 
        except: raise IndexError
    
    def layerlengthlist(self): 
        return [self.layerLength(ind) for ind in range(self.layerCount)]
    
    @Property
    def layerCount(self):  # Basenetwork
        if not len(self.nodes):
            return 0
        return self.nodes[-1].layer +1
    
    def layers(self, index):  # Basenetwork
        try:
            index %= self.layerCount
            #if index < 0:
            #    index += self.layerCount
            return list(node for node in self.nodes if node.layer == index)
        except:
            return None
    
    def iterLayer(self):
        for ind in range(self.layerCount):
            yield self.layerNodes(ind)
#         raise StopIteration
    
    @Property
    def externalNodes(self, index):  # Basenetwork
        ic = len(self.layers(0))
        if index < ic:
            return list(self.layers(0))[index]
        return list(self.layers(-1))[index - ic]
    @externalNodes.lengetter
    def lexternalNodes(self):  # Basenetwork
        return self.inputCount + self.order + self.outputCount
    
    @Property
    def inputNodes(self, index):  # Basenetwork
        return list(self.layers(0))[index]
    @inputNodes.lengetter
    def inputNodes(self):  # Basenetwork
        return self._inputCount
    
    def inputNodeByName(self, nname):
        try:
            test = list(self.inputNames).index(nname)
            res = self.inputNodes[test]
        except ValueError:
            res = None
        return res
            
    @Property
    def inputNames(self, index):  # Basenetwork
        return self.inputNodes[index].name
    @inputNames.lengetter
    def inputNames(self):  # Basenetwork
        return self.inputCount
    @inputNames.setter
    def inputNames(self, index, value):  # Basenetwork
        self.inputNodes[index].name = value
        
    def setInputNames(self, value):
        for val, node in zip(value, self.inputNodes):
            node.name = val
    
    @Property
    def outputNames(self, index):  # Basenetwork
        return self.outputNodes[index].name
    @outputNames.lengetter
    def outputNames(self):  # Basenetwork
        return self._outputCount
    @outputNames.setter
    def outputNames(self, index, value):  # Basenetwork
        self.outputNodes[index].name = value
    
    def setOutputNames(self, value):
        for val, node in zip(value, self.outputNodes):
            node.name = val
    
    @Property
    def inputCount(self):  # Basenetwork
        return self._inputCount
    
    @Property
    def outputCount(self):  # Basenetwork
        return self._outputCount
    
    @Property
    def hiddenCount(self):  # Basenetwork
        return len(self.nodes) - self.inputCount - self.outputCount
    
    @Property
    def outputNodes(self, index):  # Basenetwork
        return list(self.layers(-1))[index]
    @outputNodes.lengetter
    def outputNodes(self):  # Basenetwork
        return self._outputCount
    
    @Property
    def order(self):  # Basenetwork
        return self.layerLength(0) - self.inputCount
    
    @Property
    def stateNodes(self, index):  # Basenetwork
        if self.inputcount < 0:
            raise IndexError
        return self.layers(0)[self.inputcount + index]
    @stateNodes.lengetter
    def stateNodes(self):  # Basenetwork
        return self.order

    @Property
    def nodeCount(self):  # Basenetwork
        return len(self.nodes)# + 1
    
    @Property
    def weights(self):
        return self._weights
    @weights.setter
    def weights(self, value):
        ll = len(value) 
        if ll > self.paramCount:
            self.useOriginal = True
            self.longParamCount = ll
        self._weights = value

#     @Property
#     def weights(self, index):  # Basenetwork
#         return self._weights[index]
#     @weights.setter
#     def sweights(self, index, value):  # Basenetwork
#         self._weights[index] = value
#     @weights.lengetter
#     def lweights(self):  # Basenetwork
#         return len(self._weights)
    
    @Property
    def dimension(self):  # Basenetwork
        #lst = [node.getmaxlinkid() for node in [self.bias] + self.nodes]
        maxb = self.bias.getmaxlinkid()
        lst = [node.getmaxlinkid() for node in self.nodes] + [maxb]
        return max(lst) + 1
        #return 0
    
    def computeDimension(self):  # Basenetwork
        dd = 0
        for syn in self.bias.links:
            if not syn.isFix():
                dd = max(dd, syn.originalid)
        for node in self.nodes:
            for syn in node.links:
                if not syn.isFix():
                    dd = max(dd, syn.originalid)
        return dd+1
    
    def getTrueDimension(self):
        done = []
        res = 0
        for syn in self.links:
            if not syn.isFix() and not syn.linkid in done:
                res += 1
                done.append(syn.linkid)
            
#         for syn in self.bias.downLinks:
#             if not syn.isFix() and not syn.linkid in done:
#                 res += 1
#                 done.append(syn.linkid)
#         for node in self.nodes:
#             for syn in node.downLinks:
#                 if not syn.isFix() and not syn.linkid in done:
#                     res += 1
#                     done.append(syn.linkid)
        return res
    
    def initWeights(self, stddev=0.3, bias0=False, seed=None, **kwds):  # Basenetwork
        if seed is not None:
            random.seed(seed)
        #lst = sorted(self.computingLinks(), cmp=lambda x, y: cmp(x.linkid, y.linkid))
        linkmax = -1
        for syn in self.computingLinks():
            linkmax = max(linkmax, syn.linkid)
            if bias0 and (syn.source == self.bias):
                syn.value = 0
            else:
                syn.init = [0, stddev]
                syn.initWeight()
        if self._weights is not None:
            if len(self._weights) == linkmax+1:
                for syn in self.computingLinks():
                    self._weights[syn.linkid] = syn._value
            self._weights = asarray(self._weights)
    
    def outputnum(self, node):  # Basenetwork
        if not (node.style and C.NS_OUTPUT) or not (node in self.outputNodes):
            return -1
        return list(self.outputNodes).index(node)
    
    def synOfId(self, index):  # Basenetwork
        """generateur de la liste des synapse d'indice designe"""
        lst = (syn for syn in self.computingLinks() if syn.linkid == index)
        return lst
    
    def paramIni(self, index):  # Basenetwork
        try: 
            syn = None
            for synap in self.computingLinks():
                if synap.linkid == index:
                    syn = synap
                    break
            return syn.init
        except: 
            if syn:
                return [0.3, 0]
            return None
    
    def paramList(self):  # Basenetwork
        res = ["" for _ in range(self.synapseCount)]
        for syn in self.computingLinks():
            if syn.linkid < self.synapseCount:
                res[syn.linkid] = syn.name
        return res
    
    def getParamDict(self, reverse=False):  # Basenetwork
        if reverse:
            res = defaultdict(lambda : -1)
            for i in range(self.dimension):
                st = self.registeredParamNames(i, True)
                if st:
                    res[st] = i
            return res
        res = defaultdict(lambda: "")
        for i in range(self.dimension):
            st = self.registeredParamNames(i, True)
            if st:
                res[i] = st
        return res
    
    def registeredParamNames(self, index, original=False):  # Basenetwork
        try: 
            syn = None
            for synap in self.computingLinks():
                if original:
                    test = synap.originalid == index
                else:
                    test = synap.linkid == index
                if test:
                    syn = synap
                    break
            st = syn.name
            return st
        except:
            return ""
    
    @Property
    def iterParamNames(self, index):
        return self.paramNames(index)
    @iterParamNames.lengetter
    def  iterParamNames(self): 
        return self.paramCount      
    
    def paramNames(self, index, original=False):  # Basenetwork
        st = self.registeredParamNames(index, original)
        if not st:
            return "W_{}".format(index)
        return st
        
    def setParamName(self, index, value):  # Basenetwork
        if value is not None:
            lst = [ss for ss in self.computingLinks() if ss.linkid==index]
            for syn in lst:
                syn.name = value
        
    def setParamNames(self, *argv):  # Basenetwork
        if len(argv)==1:
            names = argv[0]
        elif len(argv) > 1:
            names = argv
        for ind, name in enumerate(names):
            if name is not None:
                self.setParamName(ind, name)
                #===============================================================
                # self._parameternames[ind] = name
                # for syn in self.synOfId(ind):
                #     syn.name = name
                #===============================================================
            
    def setParamSpace(self, mat):  # Basenetwork
        assert(mat.shape[1] == 2)
        for ind, vec in enumerate(mat):
            #itersyn = (syn for syn in self.computingLinks() if syn.linkid == ind)
            for syn in self.synOfId(ind):
                syn.setMinMax(list(vec.flat))
            
    @Property
    def paramCount(self):  # Basenetwork
        try:
            return len(self._weights)
        except:
            return 0

    def hasLinkId(self, index):  # Basenetwork
        for syn in self.computingLinks():
            if syn.linkid == index:
                return True
        return False
    
    def normalizeWeights(self):  # Basenetwork
        nd = self.paramCount
        linkids = [syn.linkid for syn in self.computingLinks()]
        tokill = [i for i in range(nd) if not (i in linkids)]   
        tokill = tokill[-1::-1]
        wlst = list(self._weights)
        if len(tokill):
            for i in tokill:
                wlst.pop(i)
                for syn in self.computingLinks():
                    if syn.linkid >= i:
                        syn.linkid -= 1
        self._weights = asarray(wlst)    
            
    
class Network(Basenetwork):
    
    def __init__(self, owner=None, modelname="model_0", inputs=0, 
            outputs=0, hidden=0, activfunc="TANH", polytype=0, 
            nosynapse=0, classif=False):  # Network
        """Neuron network.
    Exemple:
    >>> model = Network(inputs=5, outputs=1, hidden=3)
    >>> print model.paramCount
    22
    >>> print model.layerCount
    3
    >>> print model.layerLength(0)
    5
    >>> print model.layerLength(1)
    3
    >>> print model.layerLength(2)
    1
    >>> w = [0.01 for _ in xrange(model.paramCount)]
    >>> model.loadParameters(w)
    >>> print model.weights[0]
    0.01
    >>> inputs = [-2,-1,0,1,2]
    >>> a = model.propagate(inputs, w)
    >>> print model.outputs[0]
    0.0102999900004
    """
        super(Network, self).__init__(owner, modelname)
        inputnamelist = []
        outputnamelist = []
        if isinstance(inputs, str):
            inputnamelist = [inputs]
            inputs = 1
        elif not isinstance(inputs, int):
            inputnamelist = inputs
            inputs = len(inputs)
        if isinstance(outputs, str):
            outputnamelist = [outputs]
            outputs = 1
        elif not isinstance(outputs, int):
            outputnamelist = outputs
            outputs = len(outputs)
        if inputnamelist == []:
            inputnamelist = ["IN_{}".format(i) for i in range(inputs)]
        if outputnamelist == []:
            outputnamelist = ["OUT_{}".format(i) for i in range(outputs)]
        if polytype:
            # construire ici le polynome integré
            raise Exception("polynom creation not yet implemented")
            #return 
        
        inputnodelist = [self.createNode(lpos=ind, name = inputname, style=C.NS_INPUT) for ind, inputname in enumerate(inputnamelist)]
        for ind in range(hidden):
            nname = "H0_{}".format(ind)
            anode = self.createNode(name=nname, lpos=ind+inputs, layer=1, activ=activfunc)
            if not nosynapse:
                syn = anode.createLink(self.bias)
                syn.organize()
                for innode in inputnodelist:
#                 for i in range(inputs):
#                    syn = anode.createLink(self.nodes[i])
                    syn = anode.createLink(innode)
                    syn.organize()
        curlayer = 2 if hidden else 1
        for outputname in outputnamelist:
        #for _ in xrange(outputs):
            if classif:
                activ = "SIGMOID"
            else:
                activ = ""
            anode = self.createNode(layer=curlayer, name=outputname, 
                                    activ=activ, style=C.NS_OUTPUT)
            if not nosynapse:
                syn = anode.createLink(self.bias)
                syn.organize()
                for i in range(hidden):
                    syn = anode.createLink(self.nodes[inputs + i])
                    syn.organize()
        self.setSizes(inputs, outputs)
        for node in self.nodes:
            if not node._name:
                node.name = node.defaultname()
    
    @classmethod
    def createFromElementXML(cls, owner, element, localversion):  # Network
        name = element.get("name", "")
        name = element.get("networkname", name)
        name = element.get("modelname", name)
        res = cls(owner, name)
        
        style = int(element.get("style", "0"))
        input1 = int(element.get("inputs", "0"))
        output1 = int(element.get("outputs", "0"))
        res.style = style
        lst = list(element)  #.getchildren()) 
        for subelmt in lst:
            if res.includeSubElement(res.nodes, subelmt, localversion, cond = lambda node: node.layer>=0): pass
            elif subelmt.tag == "COMMENT": 
                res.addComment(unescape(subelmt.text))
            elif subelmt.tag == "LAYER":# version 27 a 32
                layer = int(subelmt.get("rank", "0"))
                if layer >= 0:
                    for subsubelmt in list(subelmt):  #list(subelmt.getchildren()):
                        if res.includeSubElement(res.nodes, subsubelmt, localversion):
                            res.nodes[-1].layer = layer
                
        res.setSizes(input1, output1)
        return res
    
    def reprlst(self):  # Network
        lst = super(Network, self).reprlst()
        if self.inputCount:
            st = ", ".join(self.inputNames)
            lst.append("inputnames = [{0}]".format(st))
        if self.outputCount:
            st = ", ".join(self.outputNames)
            lst.append("outputnames = [{0}]".format(st))
        
        return lst
    
    def NoMemSyn(self):  # Network
        for node in self.nodes:
            if not node.TestNoMemSyn:
                return True
        return False
    
    def singleGradient(self):  # Network
        return self.synapseCount == self.paramCount
        
    def getParamsStr(self):  # Network
        res = ["Parameters"]
        res.append("Count = {}".format(self.paramCount))
        for ww in self.weights:
            res.append(str(ww))
        return "\n".join(res)
    
    def loadNpy(self, source):  # Network
        
        try:
            if isinstance(source, NpzFile):  #np .lib.npyio.
                gsource = source
                gsourceO = None
            else:
                gsource = load(source)
                gsourceO = gsource
            if isinstance(gsource, ndarray):
                self.weights = gsource
                #self.weights.assign(gsource)
            else:
                wsource = gsource["params"]
                wnames = gsource["paramnames"]
                for wval, wname in zip(wsource, wnames):
                    for ind in range(self.paramCount):
                        if self.paramNames(ind) == wname:
                            self.weights[ind] = wval
            try:
                if gsourceO:
                    gsourceO.close()
            except:
                pass
            res = True
        except:
            res = False
        return res
    
    def loadASCII(self, source):  # Network
        res = False
        try:
            if os.path.exists(source):
                with open(source) as ff:
                    lst = ff.readlines()
            else:
                lst = source.splitlines(False)
            if lst:
                res = True
                for ind in range(len(lst)):
                    st = lst[ind]
                    st = st.strip().lower()
                    if st in ["weights", "parameters"]:
                        return self.loadFromASCIIStrList(lst, ind+1)
                res = False
        except:
            res = False
        return res

    def loadWeightsXML(self, source):  # Network
        res = False
        try:
            if os.path.exists(source):
                node = parse(source).getroot()
            else:
                node = fromstring(source).getroot()
        except:
            node = None
        if node is not None:
            local = None
#             for local in list(node.getiterator(st_WEIGHTS)):
            for local in list(node.iter(st_WEIGHTS)):
                break
            if (local is not None) and (int(local.attrib["count"]) == self.synapseCount):
                res = True
                vclass = local.attrib.get("class", "")
                if vclass == "RealByteVector":
                    for element in list(local):
                    #list(local.getchildren()):
                        row = int(element.attrib.get("row", 0))
                        valelmt = element.find(st_REAL)
                        if valelmt is not None:
                            value = floatEx(valelmt.text)
                            self.weights[row] = value 
                elif vclass == "RealVector" :
                    for element in list(local):  #.getchildren():
                        row = int(element.attrib.get("row", 0))
                        value = floatEx(element.text)
                        self.weights[row] = value
        return res
    
    def loadParameters(self, source):  # Network
        if source is None: return
        if isinstance(source, (list, ndarray)):
            # chargement d'un vecteur
            #self.weights.assign(source)
            self.weights = source
        #elif isinstance(source, basestring):
        elif isinstance(source, str):
            # chargement XML
            if not self.loadWeightsXML(source):
            # chargement ASCII    
                if not self.loadASCII(source):
                    if not self.loadNpy(source):
                        raise Exception("Cannot load parameters from {0}".format(source))
        elif isinstance(source, NpzFile):  #np .lib.npyio.
            self.loadNpy(source)
        else:#coder les autres sources possibles
            pass    
    
    def xmlChildren(self, indent='\t'):  # Network
        def comline(ind, comment): 
            if not ind: return '{0}<COMMENT>{1}</COMMENT>'.format(indent, escape(comment))
            return '{0}<COMMENT item="{1}">{2}</COMMENT>'.format(indent, ind, escape(comment))
        return [comline(ind, comment) for ind, comment in enumerate(self._comments)]
        
    def xmlAttrList(self):  # Network
        res = ['class="NeuronNetwork"']
        self.appendDefaultedAttribute(res, 'name', self.name, default="")
        self.appendDefaultedAttribute(res, 'style', self.style, default=0)
        self.appendDefaultedAttribute(res, 'inputs', self.inputCount)
        self.appendDefaultedAttribute(res, 'outputs', self.outputCount)
        self.appendDefaultedAttribute(res, 'weights', self.paramCount)
        return res
        
    def connectInputs(self, value):  # Network
        # connecte les valeurs d'entree
        for ind, node in enumerate(self.inputNodes):
            try:
                node.source = value.flat[ind]
            except:
                node.source = value[ind]
    
    def maxParam(self):  # Network
        return self.synapseCount - 1
    
    @Property
    def outputs(self, index):  # Network
        """output values vector"""
        return self.outputNodes[index].value
    @outputs.lengetter
    def outputs(self):  # Network
        return self.outputCount
    @outputs.setter
    def outputs(self, index, value):  # Network
        self.outputNodes[index].value = value
    
    @Property
    def inputs(self, index):  # Network
        """output values vector"""
        return self.inputNodes[index].value
    @inputs.lengetter
    def inputs(self):  # Network
        return self.inputCount
    @inputs.setter
    def inputs(self, index, value):  # Network
        self.inputNodes[index].value = value
    
    @Property
    def inputDim(self):  # Network
        return self._inputDim
    @inputDim.setter
    def sinputDim(self, value):  # Network
        self._inputDim = value
        if self._inputDim == 1:
            self.bias.value = 1
        else:
            self.bias.value = ones((value))
    
    def setInputs(self, inputs):  # Network
        # inputs est un vecteurs d'entrée ou 
        # une collection "inputDim" de vecteurs d'entrée,
        # p. ex. une matrice(inputDim, inputCount)
        if self.inputCount:
            if isinstance(inputs, list):
                self.inputDim = 1
                self.inputs.assign(inputs)
            elif inputs.ndim == 2:
                self.inputDim = inputs.shape[0]
                self.inputs.assign(inputs)
            elif inputs.ndim == 1:
                n = inputs.shape[0]//self.inputCount
                if n > 1:
                    self.inputDim = n
                    self.inputs.assign(inputs.reshape(n, self.inputCount))
                else:
                    self.inputDim = 1# inputs.shape[0]
                    self.inputs.assign(inputs)
    
    def prepareComputeHessian(self):
        for NN in self.nodes:
            NN.prepareComputeHessian(self.paramCount)
    
    def propagate(self, inputs=None, weights=None):  # Network
        """propagation à travers le modèle.
        'inputs' porte des valeurs d'entrée. Si None, les valeurs précédentes sont utilisées
        'weights' est un jeu de paramètres optionnel. Si None, les ^paramètres courants sont utilisés.
        """
        if self.computelevel >= C.ID_DIFF_SEC:
            self.prepareComputeHessian()
        if inputs is not None:
            self.setInputs(inputs)
            for node in self.nodes:
                node.inputDim = self.inputDim
        if weights is not None:
            #self.weights.assign(weights)
            self.weights = weights
        for node in self.computedNodes():
            node.propagate()
        return self
    
    def directInputGradient(self, inputGrad=None, statePartial=None):  # Network
        """Calcul du gradient du modèle par rapport aux entrées par la méthode directe
        """
        for node in self.nodes:
            node.partial = zeros((self.inputCount))
            if node.nodeid-1 < self.inputCount:
                node.partial[node.nodeid-1] = 1
        if inputGrad is None:
            inputGrad = zeros((self.outputCount, self.inputCount))
        if statePartial is not None:
            for stateIndex, node in enumerate(self.outStateNodes()):
                node.partial = statePartial[:, stateIndex]
        for node in self.computedNodes(): 
            node.partialBase()
        for outputIndex, node in enumerate(self.outputNodes):
            inputGrad[outputIndex, :] += node.partial 
        if statePartial is not None:
            for stateIndex, node in enumerate(self.outStateNodes()):
                statePartial[:, stateIndex] = node.partial
        return inputGrad
    
    def directGradient(self, gradient=None, statePartial=None, outputIndex=-1):  # Network
        """Calcul du gradient du modèle par rapport aux paramètres par la méthode directe
        """
        for node in self.nodes:
            node.partial = zeros((self.paramCount))
        if gradient is None:
            gradient = zeros((self.outputCount, self.paramCount))
        if gradient.ndim == 1:
            gradient = gradient[newaxis, :]
        if statePartial is not None:
            for stateIndex, node in enumerate(self.outStateNodes()):
                node.partial = statePartial[:, stateIndex]
        for node in self.computedNodes():
            node.partialBase()
            node.partialExtra()
        if outputIndex >= 0:
            gradient[:] += node.partial
        else:
            for outIndex, node in enumerate(self.outputNodes):
                gradient[outIndex, :] += node.partial
        if statePartial is not None:
            for stateIndex, node in enumerate(self.outStateNodes()):
                statePartial[:, stateIndex] = node.partial
        return gradient    
    
    def propagateAndDirectGradient(self, inputs=None, gradient=None):  # Network
        """Calcul simultané du transfert à travers le modèle normalisé, et du gradient du 
        modèle normalisé par rapport aux paramètres par la méthode directe.
        """
        if self.computelevel < C.ID_DIFF:
            raise Exception("computelevel is too small")
        self.setInputs(inputs)
        if gradient is None:
            gradient = zeros((self.outputCount, self.paramCount))
        for node in self.nodes:
            node.partial = zeros((self.paramCount))
        for node in self.computedNodes():
            node.propagate()
            node.partialBase()
            node.partialExtra()
        for outIndex, node in enumerate(self.outputNodes):
            gradient[outIndex, :] += node.partial
        return self.outputs, gradient    
             
    def backPropagateOld(self, gradient, gradInput=None, gradOutput=None, mode=0):  # Network  
        """Retropropagation dans le modèle.
        
           gradOutput est la matrice directrice de la retropropagation.
           Retourne un tuple constitue de :
               le vecteur gradient par rapport aux parametres
               le vecteur gradient par rapport aux entrées
        """
        if gradient is not None:
            gradDim = gradient.ndim # nombre de dimensions du gradient
        else:
            gradDim = 0
        ind = self.layerLength(-1)
        lc1 = -2 
        for node in self.nodes[::-1]:
            ilayer = node.layer
            if ilayer >= lc1:
                lc1 = ilayer
                ind -= 1 
                if ind < self.outputCount:
                    node.backPropagateOld(gradient, gradOutput[ind], gradDim, mode)
                else:  # modeles dynamiques, noeuds d'etat
                    node.backPropagateOld(gradient, zeros_like(gradOutput)[0], gradDim, mode)
            elif ilayer > 0: 
                node.backPropagateOld(gradient, zeros_like(gradOutput)[0], gradDim, mode)
            elif (ilayer == 0) and (gradInput is not None): 
                res = node.backPropagateOld(None, zeros_like(gradOutput)[0], gradDim, mode)
                if mode & C.GC_MULTI_OUTPUT:
                    for outindex in range(self.outputCount):
                        gradInput[outindex, node.nodeid-1] = res[outindex][0] 
                else:
                    gradInput[node.nodeid-1] = res
        # attention, ici on retourne des références sur des vecteurs qui pourront 
        # être modifiés plus tard 
        return gradient, gradInput
    
    def backPropagateCoreMultiOutput(self, jacobian, gradInput=None, gradOutput=None):  # Network
        """Coeur de la retropropagation
        le jacobien, s'il existe, est de dimensions (no, nd, ns) 
        le gradient aux entrées, s'il existe est de dimensions (no, ni)
        le gradient aux sorties, s'il existe est de dimension (no, no)
        
        jacobian et gradInput, s'ils existent sont les cibles du calcul. Sinon, 
        les mémoires nécessaires sont réservées.
        Si nd est > 1, gradInput n'est pas calculé.
        gradOutput est l'initialisation de la retro-propagation. Pour un gradient 
        aux poids du modèle isolé, c'est ine matrice diagonale
        computelevel doit être au moins égval à id_Diff
        S'il est égal à id_DiffSec, on calculed aussi le hessien (dérivée seconde
        de la sortie du modèle par rapport aux poiods
        
        return jacobian et gradInput
        """
        ind = self.layerLength(-1)
        lc1 = -2 
        for node in self.nodes[::-1]:
            if node.layer >= lc1:
                lc1 = node.layer
                ind -= 1 
                if ind < self.outputCount:
                    node.backPropMultiOut(jacobian, gradOutput[ind])
                else:  # modeles dynamiques, noeuds d'etat
                    node.backPropMultiOut(jacobian)
            elif node.layer > 0: 
                node.backPropMultiOut(jacobian)
            elif (node.layer == 0) and (gradInput is not None): 
                res = node.backPropMultiOut()
                gradInput[Ellipsis, node.nodeid-1] = res
#                gradInput[:, node.nodeid-1] = res[:, 0]
        return jacobian, gradInput
          
    def backPropagateCoreSingleOutput(self, gradient, gradInput=None, gradOutput=1, original=True):  # Network
        """Coeur de la retropropagation
        le jacobien, s'il existe, est de dimensions (nd, ns) 
        le gradient aux entrées, s'il existe est de dimensions (ni)
        le gradient aux sorties est de un scalaire
        
        gradient et gradInput, s'ils existent sont les cibles du calcul. Sinon, 
        les mémoires nécessaires sont réservées.
        Si nd est > 1, gradInput n'est pas calculé.
        gradOutput est l'initialisation de la retro-propagation. Pour un gradient 
        aux poids du modèle isolé, c'est ine matrice diagonale
        computelevel doit être au moins égval à id_Diff
        S'il est égal à id_DiffSec, on calculed aussi le hessien (dérivée seconde 
        de la sortie du modèle par rapport aux poiods
        
        return gradient et gradInput
        """
        ind = self.layerLength(-1)
        lc1 = -2 
        for node in self.nodes[::-1]:
            if node.layer >= lc1:
                lc1 = node.layer
                ind -= 1 
                if ind < self.outputCount:
                    node.backPropSingleOut(gradient, gradOutput, original=original)
                else:  # modeles dynamiques, noeuds d'etat
                    node.backPropSingleOut(gradient, original=original)
            elif node.layer > 0: 
                node.backPropSingleOut(gradient, original=original)
            elif (node.layer == 0) and (gradInput is not None): 
                res = node.backPropSingleOut(None, original=original)
                if gradInput.ndim == 1:
                    gradInput[node.nodeid-1] = res
                else:
                    gradInput[Ellipsis, node.nodeid-1] = res
        return gradient, gradInput
          
    def backPropagate(self, gradient, gradInput=None, gradOutput=None, original=True):   # Network 
        """Retropropagation dans le modèle.
        
        Cette procedure est un wrapper de "backPropagateCore" ou de "backPropagateCoreSingle".
        Elle qui permet de travailler avec des gradient et gradInput qui n'ont pas la bonne dimension
        
        """
        if self.computelevel < C.ID_DIFF:
            raise ValueError("computelevel should higher in Network.backPropagate")
        
        if gradient is not None:
            gradDim = gradient.ndim # nombre de dimensions du gradient
        else: gradDim = 0
        
        if self.outputCount == 1:
            if gradDim == 1:
                gradient = gradient[newaxis, :]                
                
            self.backPropagateCoreSingleOutput(gradient, gradInput, gradOutput, original=original)
            
            if gradDim: 
                gradient.squeeze()
        else:    
            if gradInput is not None:
                gradInputDim = gradInput.ndim
            else: gradInputDim = 0
            
            if gradDim == 1:  #(ns) -> (no, nd, ns)
                gradient =  gradient[newaxis, newaxis, :]
            elif gradDim == 2:  #(no, ns) -> (no, nd, ns)
                gradient = gradient[:, newaxis, :]
                # le cas (nd, ns) n'est pas possible ???
                
            if gradInputDim == 1:  #(ni) -> (nd, ni)
                gradInput = gradInput[newaxis, :]
        
            self.backPropagateCoreMultiOutput(gradient, gradInput, gradOutput)

            if gradDim:  
                gradient.squeeze()
            if gradInputDim:
                gradInput.squeeze()
            
        # attention, ici on retourne des références sur des vecteurs qui pourront 
        # être modifiés plus tard 
        return gradient, gradInput
        
    @Property
    def computelevel(self):
        return self._computelevel
    @computelevel.setter
    def scomputelevel(self, value):
        self._computelevel = value
        for node in self.nodes:
            node.computelevel = value
    
    def walk(self, condIndex=0, reverse=False, layer=None):   # Network 
        """Promenade dans les neurones du réseau
        
Si reverse = False, le parcours va dans le sens ascendant
sinon, le parcours est descendant. Dans ce cas, les couches sont balayées depuis 
leur extrêmité, avec un indice decroissant de lenght-1 à 0
condIndex est l'index une condition que doit remplir le N° de couche:
    id_Nothing (0) -> aucune condition
    id_Input (1)   -> couche = 0
    id_Pos (2)     -> couche > 0
    id_Output (3)  -> couche de sortie
Les couches varient de 0(couche d'entrée) à layerCount -1
    l'indice de la couche d'entrée est '0'
    l'indice la couche de sortie est 'self.children[-1].layer'
La couche des neurones constants (indice -1) n'est pas balayée par cet itérateur.    
"""
        memnl = -2
        if reverse:
            iter1 = self.nodes[::-1]
        else:
            iter1 = self.nodes
        for node in iter1:
            nl = node.layer
            if nl != memnl:
                memnl = nl
                if reverse:
                    i = self.layerLength(nl) 
                else:
                    i = -1
            Cond = ((condIndex == 0) or
                    ((condIndex == 1) and (nl == 0)) or
                    ((condIndex == 2) and (nl > 0)) or
                    ((condIndex == 3) and (nl == self.layercount - 1)) or
                    ((layer is not None) and (layer == nl)))
            if Cond:
                if reverse:
                    i -= 1
                else:
                    i += 1
                yield i, nl, node
        
    def nodeinfo(self, layer=0, index=0):  # Network
        node = self.getNode((layer, index))
        if node:
            return node.todata()    
            
    def synapseinfo(self, originlayer=-2, originindex=-1, targetlayer=-2, 
            targetindex=-1, synindex=-1, style=0):  # Network
        syn = self.getLink((originlayer, originindex), 
            (targetlayer, targetindex), style)
        if syn:
            return syn.todata()
    
    def setOutputParams(self, name="", activ="", index=-1):  # Network
        nlayer = self.layerCount
        output = self.outputCount
        if 0 <= index < output:
            node = self.getNode((nlayer-1, index))
            if node:
                node.activation = C.getActivIndex(activ)
                if name:
                    node.name = name
        else:
            nam = name
            for ind in range(output):
                if name:
                    nam = "{0}_{1}".format(name, ind)
                self.setOutputParams(nam, activ, ind)
                
    def synapseAlign(self):  # Network
        for node in self.nodes:
            for syn in node.links:
                syn.originalid = syn.linkid
                
def isCommonLayer(layer, value=None):
    res = True
    for node in layer:
        res = node.isCommmon(value=value)
        if not res:
            break
    return res
    
                
register(Network)
register(Network, "NETWORK")

if __name__ == "__main__":
    #import pickle  as pcl
    import doctest
    doctest.testmod()
    print("doctest closed")
    #===========================================================================
    # model = Network(inputs=3, outputs=1, hidden=3)
    # pathname = os.path.join(os.path.dirname (__file__), "..", "..", "..", "testFiles")
    # pathname = os.path.normpath(pathname)
    # filename = os.path.join(pathname, "modelpic.net")
    # 
    # model.saveModel(filename, C.SF_BINARY)
    # model2 = importPickle(filename)
    # st0 = model.xml()
    # st1 = model2.xml()
    # if st0 == st1:
    #    print "OK binary saving and retrieving"
    # else:
    #    print st0
    #    print st1
    #===========================================================================