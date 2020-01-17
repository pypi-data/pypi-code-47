#-*- coding: ISO-8859-15 -*-
#===============================================================================
# $Id: _node.py 4819 2018-11-02 05:32:25Z jeanluc $
#  Module  _node
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

import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)

from operator  import mul as opmul
from numpy import array, asarray, ndarray, zeros, zeros_like, dtype, NaN, \
    delete as npdelete
from functools import reduce

from ._monalfunc import identityactiv, getIndexFromActivClass, getActivClass
from ..Property import Property
from ..util.monalbase import Component, MonalError, DimensionError, LinkError
from ..util.utils import CCharOnlys  #, ChildElementList
from ._link import Synapse
from ..util.monaltoolbox import register
from ..util import const_st as CS
from ..monalconst import NS_STATE, NS_PI, LS_STD, LS_FIXE, LS_TELQUEL, \
    FIX_LIMIT, ID_COMPUTE, ID_DIFF, GC_MULTI_DATA, GC_MULTI_OUTPUT #, NS_INPUT
from ..monalrecords import NodeData
from ..specialmath import INF

__all__ = ["Basenode", "Node", "Nodepi", "newNode"]

candidateattr = ("atom", "mass")
# noms des attributs facultatifs qui peuvent être attribués lors de la
    #construction d'un "Node". Ces attributs sont conservés lors de la sauvvegarde XML
    
XMLRELATIVE_01 = 1  # 1 -> intervalle [0, 1]
                    # 0 -> intervalle [-1, 1]

class Basenode(Component):

    def __init__(self, owner, name="", layer=0, pos=-1, activ="", defaultvalue=0.0, style=0):
        # owner doit etre un Network
        super(Basenode, self).__init__(owner, name)
        self.style = style
        self.links = []
        self.downLinks = []
        self.layer = layer
        self.nodeid = None
        self.activation = activ
        self.value = defaultvalue
        self._tagname = 'NODE'
        self.derive = array([1.])
        self.partial = array([0.])
        self.TestNoMemSyn = True
        self._useOriginal = False
        self.computelevel = 1
        self.DLambdaZ = None
        self.DLambdaW = None
        self._mini = None
        self._maxi = None

    def __del__(self):  # Basenode
        try:
            del self._activfunc
        except: pass
        self.downLinks = []
        self.links = []
        super(Basenode, self).__del__()

    def reprlst(self):  # Basenode
        lst = super(Basenode, self).reprlst()
        lst.append("nodeid : {}".format(self.nodeid))
        lst.append("layer : {}".format(self.layer))
        lst.append("activation : {}".format(self.activation))
        lst.append("value : {}".format(self.value))
        return lst

    @Property
    def linksCount(self):  # Basenode
        return len([val for val in self.components if isinstance(val, Synapse)])

    @classmethod
    def createFromElementXML(cls, owner, element, localversion):  # Basenode
        name = element.get("neuronname", "") or element.get("name", "")
        style = int(element.get("style", "0"))
        layer = int(element.get("layer", "0"))
        funct = element.get("function", "") or element.get("func", "")
        nodeid = int(element.get("nodeid", "0"))
        res = cls(owner, name, layer, activ=funct)
        for attr in candidateattr:
            try:
                st = element.get(attr, "")
            except:
                st = ""
            if st:
                setattr(res, attr, st)
        res.style = style
        res.nodeid = nodeid
        lst = list(element)# list(element.getchildren())
        haspot = not len(lst)  #list(element.getchildren()))
        for subelmt in lst:
            if res.includeSubElement(res.links, subelmt, localversion): pass  #, weak=True
            elif subelmt.text != 'None':
                if subelmt.tag == "MINIMUM": res._mini = float(subelmt.text)
                elif subelmt.tag == "MAXIMUM": res._maxi = float(subelmt.text)
                elif subelmt.tag == "VALUE": res.value = float(subelmt.text)
                elif subelmt.tag == "POTENTIAL":
                    res.potential = float(subelmt.text)
                    haspot = True
                elif subelmt.tag == "INTERFACE":  # version 27 a 32
                    mini = subelmt.get("minimum", 0.0)
                    if (mini != "NAN") and mini is not None:
                        res._mini = float(mini)
                    maxi = subelmt.get("maximum", 1.0)
                    if (maxi != "NAN") and maxi is not None:
                        res._maxi = float(maxi)
                    try:
                        relinput = float(subelmt.get("relinput", "0"))
                        if XMLRELATIVE_01:
                            delta = (res._maxi - res._mini) * relinput
                        else:
                            delta = (res._mini * (1 - relinput) + res._maxi * (1 + relinput)) / 2
                        res.value = res._mini + delta
                    except: pass
        if not haspot:
            res.potential = res.value
        return res

    def getmaxlinkid(self, origin=True):  # Basenode
        if origin:
            lst = [syn.originalid for syn in self.links if syn.linkid < FIX_LIMIT]
        else:
            lst = [syn.linkid for syn in self.links if syn.linkid < FIX_LIMIT]
        if len(lst):
            return max(lst)
        return 0

    @Property
    def useOriginal(self):  # Basenode
        return self._useOriginal
    @useOriginal.setter
    def suseOriginal(self, value):  # Basenode
        self._useOriginal = value
        for syn in self.links:
            syn.useOriginal = value

    def IsFixed(self, fromInput):  # Basenode
    #=============================================================================
    # Result := true;
    # i := 0;
    # while Result and (i < CompteParent) do
    # begin
    #   SS := Synapses[i];
    #   Result := SS.Fixed;
    #   if Result and FromInput then
    #     Result := SS.NParent.GetIsFixed(true);
    #   inc(i);
    # end;
    #=============================================================================
        res = True
        for syn in self.links:
            res = syn.isFix()
            if res and fromInput:
                res = syn.source.IsFixed(True)
            if not res:
                break
        return res

    def outputnum(self):  # Basenode
        return self.owner.outputnum(self)

    def isPi(self):  # Basenode
        return False

    def equivalent(self, target, withException=False):  # Basenode
        eq = True
        for syn1, syn2 in zip(self.orderedLinks, target.orderedLinks):
            eq &= syn1.equivalent(syn2, withException) and (syn1.source.nodeid == syn2.source.nodeid)
            if withException and not eq:
                raise AssertionError("Different link sources %s: %s, %s: %s"%(syn1.linkid, syn1.source.nodeid, syn2.linkid, syn2.source.nodeid))
        return eq
    
    def xmlAttrList(self):  # Basenode
        res = []
        self.appendDefaultedAttribute(res, 'nodeid', self.nodeid)
        self.appendDefaultedAttribute(res, 'name', self.name)
        for attr in candidateattr:
            if hasattr(self, attr):
                self.appendDefaultedAttribute(res, attr, getattr(self, attr))
        self.appendDefaultedAttribute(res, 'style', self.style, default='0')
        self.appendDefaultedAttribute(res, 'layer', self.layer)
        self.appendDefaultedAttribute(res, 'function', self.activation, default="ident")
        return res
    
    def isLin(self):  # Basenode
        act = self._activfunc
        return (act is None) or isinstance(act, identityactiv)
    
    def xmlChildren(self, ident='\t'):  # Basenode
        res = []
        if hasattr(self, "potential") and (self.value != self.potential):
            res = ['%s<POTENTIAL>%s</POTENTIAL>'% (ident, self.potential)]
        if self.value:
            res.append('%s<VALUE>%s</VALUE>'% (ident, self.value))
        return res
            
    def getSynapse(self, source, style=LS_STD, linkid=-1, name=None):  # Basenode
        #for link in self.downLinks:
        for link in self.links:
            if ((link.source == source) and  
            ((linkid < 0) or (link._linkid == linkid)) and
            ((not name) or (link.name == name))):
                return link
        return None            
    
    def absorb(self, source, inputs=False, outputs=False):  # Basenode
        if inputs:
            while source.linksCount:
                syn = source.links[0]
                syn.owner = self
                self.links.append(syn)
        if outputs:
            while len(source.downLinks):
                syn = source.downLinks.pop(0)
                syn.source = self
    
    def isolate(self, inputs=False, outputs=False, weights=None, style=LS_STD):  # Basenode
        if inputs:
            for syn in list(self.links)[-1::-1]:
                self.deleteLink(syn, weights=weights, style=style)
        if outputs:
            while len(self.downLinks):
                syn = self.downLinks.pop()
                if not (style & LS_TELQUEL|LS_FIXE) and weights and (syn.linkid < len(weights)):
                    weights.pop(syn.linkid)     
                syn.target.links.remove(syn)
                syn.owner = None
            
#             lst = self.downLinks[-1::-1]
#             for syn in lst:
#                 
#                 syn.target.deleteLink(syn, style=style)
    
    def deleteLink(self, source, style=LS_STD, linkid=-1, name=None, weights=None):  # Basenode
        res = -1
        if isinstance(source, Synapse):
            syn = source
        else:
            syn = self.getSynapse(source, style, linkid, name)
        if syn:
            res = syn._linkid
            syn.owner.links.remove(syn)
            if not(style & (LS_TELQUEL|LS_FIXE)):
                if weights is not None:
                    if isinstance(weights, list):
                        weights.pop(syn.linkid)
                    else:
                        weights = npdelete(weights, [syn.linkid])
            try:
                syn.source.downLinks.remove(syn)
                # this remove is done at the end to keep a reference to syn 
                # until there
            except Exception:
                pass
            syn.owner = None
        return res
    
    def createLink(self, source, value=0.0, style=LS_STD, linkid=-1, name=""):  # Basenode
        """Create a new link from source toward target"""
        cursyn = Synapse(owner=self, source=source, value=value, style=style, name=name)
        self.links.append(cursyn)

        # accepter le lien et calculer son numero d'ordre, ...
        if not (LS_FIXE & cursyn.style) and (linkid <= FIX_LIMIT):
            wlst = list(self.network._weights)
            if linkid < 0:
                wlst.append(cursyn.value)
                linkid = len(wlst) - 1
            elif len(wlst) > linkid:
                for synloc in self.network.links:
                    if (synloc.linkid >= linkid) and not synloc.isFix():
                        synloc.linkid += 1
                wlst.insert(linkid, cursyn.value)
            else:
                while len(wlst) <= linkid:
                    wlst.append(NaN)
                wlst[linkid] = cursyn.value
#                 while len(self.network._weights) <= cursyn.linkid:
#                     self.network._weights.append(NaN)
#                 self.network._weights[linkid] = cursyn.value
#                 self.network._weights = asarray(wlst)
#             cursyn.linkid = linkid
            self.network._weights = asarray(wlst)
        elif linkid > FIX_LIMIT:
            self.network._lastFix = max(linkid, self.network._lastFix)
        else:
            linkid = self.network._lastFix
            self.network._lastFix += 1
        # OK, le lien est accepte        
        #self._parameternames[linkid] = syn.name
        cursyn.linkid = linkid
        return cursyn
    
    def reconnect(self, owner):  # Basenode
        # - etablissement du proprietaire
        # - branchement des liaisons pendantes
        self._owner = owner
        for syn in self.links:
            syn.reconnect(self)
    
    #def __setstate__(self, state):  # Basenode
    #    self.__dict__.update(state)
    
    def __getstate__(self):  # Basenode
        # preparation du pickling
        objdict = self.__dict__.copy()
        objdict["downLinks"] = []
        #objdict["components"] = [] 
        objdict["_owner"] = None
        return objdict
    
    def organize(self, network):  # Basenode
        assert(network)
        for syn in self.links:
            syn.organize()  #self, network
        for syn in list(self.downLinks):
            tg = syn.target
            if tg is None:
                raise LinkError("Ownerless Synapse #%d  on node #%d"% (syn.linkid, self.nodeid))
            if (tg.nodeid < self.nodeid) and (tg.style & NS_STATE):
            # syn.target est situee avant dans le reseau, et est un noeud d'etat
            # donc self est une sortie d'etat
                self.style &= NS_STATE
            
    def setMinMax(self, mini=None, maxi=None):  # Basenode
        if maxi is None:
            try: 
                maxi = mini[1]
                mini = mini[0]
            except: pass
        self._mini = mini
        self._maxi = maxi
        
    @Property
    def interval(self): # Basenode
        try:
            return (self._mini, self._maxi)
        except:
            return(-INF, INF)
    
    @Property
    def minimum(self):  # Basenode
        try: 
            val = self._mini
            if val is None:
                return -INF
            return val
        except: return -INF
            
    @Property
    def maximum(self):  # Basenode
        try: 
            val = self._maxi
            if val is None:
                return INF
            return val
        except: return INF
        
    @Property
    def mean(self): # Basenode
        min = self.minimum
        max = self.maximum
        try:
            return (min + max)/2
        except:
            return None
            
    def nameC(self):  # Basenode
        return CCharOnlys(self.name)
    
    def activationIndex(self):  # Basenode
        return getIndexFromActivClass(self.activation)
    
    def todata(self, nodedata=None):  # Basenode
        if nodedata is None:
            nodedata = NodeData()
        nodedata.name = self.name
        nodedata.layerIndex, nodedata.nodeindex = self.getIndexes()
        nodedata.activation = getIndexFromActivClass(self.activation)
        nodedata.nodeID = self.nodeid
        nodedata.style = self.style
        #nodedata.nodeType = self.nodetype
        nodedata.value = self.value    
        return nodedata
    
    def getIndexes(self):  # Basenode
        ll = self.layer
        nn = -1
        for anode in self.owner.layers(ll):
            nn += 1
            if anode == self:
                return ll, nn
        return ll, -1
    
    def defaultname(self):  # Basenode
        ll, nn = self.getIndexes()
        if nn < 0:
            return "badly inserted in network"
        if not ll:
            return CS.st_INdefault % nn
        lc = self.owner.layerCount
        if ll == lc-1:
            return CS.st_OUTdefault % nn
        ln = self.owner.layerLength(ll)
        if ln == 2:
            return "H%d"% (ll-1)
        return CS.st_HIDdefault % (ll-1, nn)
    
    def isCommmon(self, value=None):  # Basenode      
        return (len(self.links) == 1) and len(self.downLinks) \
            and self.links[0].isCommon(value=value)
    
    @Property
    def activation(self):  # Basenode
        if self._activfunc:
            return str(self._activfunc)
        return ""
    @activation.setter
    def setactivation(self, value):  # Basenode
        self._activclass = getActivClass(value)
        self._activfunc = self._activclass()

    @Property
    def source(self):  # Basenode
        ll = self.linksCount
        if not ll or (ll > 1):
            raise DimensionError("Error in source assignment")
        try: return self.links[0].source
        except: raise MonalError("Error in source assignment")
    @source.setter
    def ssource(self, value):  # Basenode
        if isinstance(value, (int, float, dtype)):#
            self.links[0].source = value
        else:
            self.links[0].source = value.flat
    
    @Property
    def orderedLinks(self):  # Basenode
        lst = (syn for syn in self.links if isinstance(syn, Synapse))
        return sorted(lst, key=lambda syn: syn.linkid)
    
    def activFormula(self, expr):  # Basenode
        return self._activfunc.formula(expr)
    
    @Property
    def network(self):  # Basenode
        return self.owner
    
    @Property
    def freeLinks(self):  # Basenode
        return (syn for syn in self.links if not syn.isFix())
        
    def adjustLinkid(self, OkMin=1000000):
        for syn in self.links:
            if syn.linkid > OkMin:
                syn.linkid -= 1
    
    def partialBase(self):
        #res = sum(syn.deltaPartial() for syn in self.links)
        res = zeros_like(self.partial)
        for syn in self.links:
            res += syn.deltaPartial()
        self.partial = res * self.derive #* syn.sousproduit
    
    def partialExtra(self):  # Basenode
        for syn in self.links:
            if syn.linkid < FIX_LIMIT:
                self.partial[syn.linkid] += self.derive * syn.source.value #* syn.sousproduit
        
    def calculDirectLocal(self, index=-1):  # Basenode
        cumul = 0
        for syn in self.links:
            if syn.linkid == index:
                cumul += syn.source.value #* syn.sousproduit
            cumul += syn.deltaPartial() 
        self.partial = cumul * self.derive   
    
    def computepotential(self):  # Basenode
        #return sum(map(lambda link: link.output(), self.links))
        return sum(link.output() for link in self.links)

    def formula(self, light=True):  # Basenode
        expr = self.potentialformula(light)
        return self.activFormula(expr)
    
    def potentialformulaList(self, light=True):  # Basenode
        lst = []
        for link in self.links:
            source = link.source
            if link.isFix():
                valstr = str(link.value)
            else:
                valstr = "{%s}" % link.name
            if source.name == "bias":
                lst.append(valstr)
            elif light:
                if valstr == "1.0":
                    lst.append(source.name)
                else:
                    lst.append("%s*(%s)" %(valstr, source.name))
            else:
                if valstr == "1.0":
                    lst.append(source.formula(light))
                else:
                    lst.append("%s*(%s)" %(valstr, source.formula(light)))
        return lst
    
    def prepareComputeHessian(self, paramCount):  # Basenode
        localnodeCount = self.linksCount
        self.DLambdaZ = zeros(self.nodeCount)
        self.DLambdaW = zeros(paramCount)
        for SS in self.links:
            SS.prepareComputeHessian(localnodeCount, paramCount)
        
    
    def propagate(self):  # Basenode
        self.potential = self.computepotential()
        self.value = self._activfunc(self.potential)
        if self.computelevel > ID_COMPUTE:
            self.derive = array(self._activfunc.derive(self.potential))
            if self.computelevel > ID_DIFF:
                self.derive2 = self._activfunc.derive2(self.potential)
        return self.value
    
    def backPropagateOld(self, gradient=None, local = None, gradDim=0, mode=0):  # Basenode
        # Calcul de la dérivée par retropropagation 
        self._lambda = local
        for syn in self.downLinks:  # balayage des enfants
            delta = syn.owner._lambda * syn.owner.derive * syn.value
            self._lambda += delta

        lambdaDerive = array([0.])
        if self.layer or (gradient is None):
            if (gradient is None):
                if mode & GC_MULTI_OUTPUT:
                    no = no = local.shape[0]
                else:
                    no = 1
                nd = 1
            elif (gradDim <= 1):
                no = 1
                nd = 1
            elif gradDim ==2:
                if mode & GC_MULTI_DATA:
                    no = 1
                    nd = gradient.shape[0]
                else:
                    if isinstance(local, ndarray) and (local is not None):
                        no = local.shape[0]
                    else:
                        no = gradient.shape[0]
                    nd = 1
            else:  # ici, gradDim = 3
                no = gradient.shape[0]
                nd = gradient.shape[1]
            if isinstance(self._lambda, (int, float, dtype)):#
                lambdaDerive = self.derive * self._lambda
            else: 
                lambdaDerive = zeros((no, nd))
                for outindex in range(no):
                    lambdaDerive[outindex, :] = self.derive * self._lambda[outindex]
            
        if (self.layer > 0) and (gradient is not None):
#            iterr = ((syn.linkidid, syn.source.value) for syn in self.freeLinks)
            iterr = ((syn.originalid, syn.source.value) for syn in self.freeLinks)
            if gradDim == 1:
                for synid, val in iterr:
                    gradient[synid] += lambdaDerive * val  
            elif gradDim == 2:
                for synid, val in iterr:
                    value = lambdaDerive * val
                    if mode & GC_MULTI_DATA:
                        try:
                            gradient[:, synid] += value
                        except:
                            gradient[:, synid] += value[0]
                    else:
                        for outindex in range(no):
                            gradient[outindex, synid] += value[outindex][0]
                          
            elif gradDim == 3: 
                for synid, val in iterr:
                    gradient[:, :, synid] += lambdaDerive * val 

        if self.computelevel > ID_DIFF:
        #  if (ComputeLevel >= 2) then
        #  begin
        #    DLambdaZ.AssignAll(0);
        #    DLambdaW.AssignAll(0);
        #    // Calcul des vecteurs DLambdas.
        #    CalculDLambda;
        #  end;
            pass  # a developper
        
        return lambdaDerive
            
    def backPropMultiOut(self, gradient=None, local = None):  # Basenode
        # Calcul de la dérivée par retropropagation 
        # la forme du gradient est (no, nd, ns) 
        self._lambda = local
        for syn in self.downLinks:  # balayage des enfants
            delta = syn.owner._lambda * syn.owner.derive * syn.value
            if self._lambda is None:
                self._lambda = delta
            else:
                self._lambda += delta

        lambdaDerive = None
        if self.layer or (gradient is None):
            if isinstance(self._lambda, ndarray):
                no = self.owner.outputCount
                nd = self.inputDim
                lambdaDerive = zeros((no, nd))
                for outindex in range(no):
                    lambdaDerive[outindex] = self.derive * self._lambda[outindex]
            else:
                lambdaDerive = self.derive * self._lambda
        
        if self.computelevel > ID_DIFF:
        #    DLambdaZ.AssignAll(0);
        #    DLambdaW.AssignAll(0);
        #    // Calcul des vecteurs DLambdas.
        #    CalculDLambda;
            pass  # a developper
        
        if not self.layer:
            return lambdaDerive.squeeze()
        
        if (gradient is not None):
            iterr = ((syn.originalid, syn.source.value) for syn in self.freeLinks)
#            iterr = ((syn.linkidid, syn.source.value) for syn in self.freeLinks)
            for synid, val in iterr: 
                if len(gradient.shape) == 2:
                    gradient[:, synid] += lambdaDerive * val
                else:
                    gradient[synid] += lambdaDerive * val 
#                gradient[:, :, synid] += lambdaDerive * val
                 
        return None

    def backPropSingleOut(self, gradient=None, local=None, original=True): # Basenode
        # Calcul de la dérivée par retropropagation pour une seule sortie 
        # la forme du gradient est (ns) 
        self._lambda = local
        for syn in self.downLinks:  # balayage des enfants
            if self._lambda is None:
                self._lambda = syn.owner._lambda * syn.owner.derive * syn.value
            else:
                self._lambda += syn.owner._lambda * syn.owner.derive * syn.value

        lambdaDerive = None
        if self.layer or (gradient is None):
            lambdaDerive = self.derive * self._lambda
        
        if (self.layer > 0) and (gradient is not None):
#            iterr = ((syn.linkid, syn.source.value) for syn in self.freeLinks)
            if original:
                iterr = ((syn.originalid, syn.source.value) for syn in self.freeLinks)
            else:
                iterr = ((syn.linkid, syn.source.value) for syn in self.freeLinks)
            for synid, val in iterr:
                if gradient.ndim == 2:
                    gradient[:, synid] += lambdaDerive * val 
                else:
                    gradient[synid] += lambdaDerive * val 

        if self.computelevel > ID_DIFF:
        #    DLambdaZ.AssignAll(0);
        #    DLambdaW.AssignAll(0);
        #    // Calcul des vecteurs DLambdas.
        #    CalculDLambda;
            pass  # a developper
        
#        if len(lambdaDerive.shape) == 2:
#            return lambdaDerive[0]
#        else:
        return lambdaDerive
                        
class Node(Basenode):
    """additive node (neuron)"""

    def potentialformula(self, light=True):  # Node
        lst = self.potentialformulaList(light)
        return " + ".join(lst)
    
    def xmlAttrList(self):  # Node
        return ['class="NeuronSigma"'] + super(Node, self).xmlAttrList()
    
class Nodepi(Basenode):
    """multiplicative node (pi neuron)"""
            
    def __init__(self, owner, name="", layer=0, pos=-1, activ=""):  # Nodepi
        # owner doit etre un Network
        super(Nodepi, self).__init__(owner, name, layer, pos, activ)
        self.TestNoMemSyn = False
        
    def potentialformula(self, light=True):  # Nodepi
        lst = self.potentialformulaList(light)
        lst = ["(%s)"% val for val in lst]
        return " * ".join(lst)
    
    def xmlAttrList(self):  # Nodepi
        return ['class="NeuronPi"'] + super(Nodepi, self).xmlAttrList()

    def computepotential(self):  # Nodepi
        return reduce(opmul, (link.output() for link in self.links))
    
    def isPi(self):  # Nodepi
        return True
    
def newNode(owner, name="", layer=0, pos=-1, activ="", style=0, defaultvalue=0.0):
    if style & NS_PI:
        return Nodepi(owner, name, layer, pos, activ, defaultvalue=defaultvalue)
    return Node(owner, name, layer, pos, activ)

register(Node)
register(Node, "Neuron")
register(Node, "NeuronSigma")
register(Nodepi)
register(Nodepi, "NeuronPi")
