#-*- coding: ISO-8859-15 -*-
#===============================================================================
# $Id: _link.py 4819 2018-11-02 05:32:25Z jeanluc $
#  Module  _link
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

from numpy.random import normal
from numpy import zeros, asarray
import warnings

from ...nntoolbox.utils import floatEx
from ..Property import Property, Properties
from ..util.monalbase import Component, LinkError
from ..util.monaltoolbox import register
#from ..util.utils import ChildElementList
from ..monalconst import FIX_LIMIT, LS_FIXE, LS_STD, LS_INVERSE
from ..monalrecords import SynapseData 
from ..specialmath import INF, NAN  
from ._model import Model

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)


__all__ = ["Link", "DirectLink", "Synapse"]

@Properties(("multi",), False)
class Link(Component):
    """Link de base"""
    def __init__(self, owner, name="", linkid=-1, source=None):  # Link
        # owner deviendra la cible. Doit etre un Node
        super(Link, self).__init__(owner, name)
        self._linkid = linkid
        self._originalid = -1
        self._useOriginal = False
        self._multi = False
        self._source = source
        self.SSProd = None
        self.FSPDU = None
        
    def __del__(self):  # Link
        try:
            if self._source: 
                n = self._source.downLinks.index(self)  
                if n >= 0:  
                    self._source.downLinks.pop(n)
        except: pass
        self._source = None
        super(Link, self).__del__()
    
    def reprlst(self):  # Link
        lst = super(Link, self).reprlst()
        lst.append("linkid : {}".format(self._linkid))
        lst.append("source : {}".format(self._source.name))
        return lst
        
    @Property
    def useOriginal(self):  # Link
        return self._useOriginal
    @useOriginal.setter
    def suseOriginal(self, value):  # Link
        self._useOriginal = value
        
    def equivalent(self, target):  # Link
        return isinstance(target, Link)
    
    def isFix(self):  # Link
        return True
    
    def defaultname(self):  # Link
        if self._linkid >= 0:
            return "W_%d"% self._linkid
        return "D_X"

    def _connectstate(self, state, key):  # Link
        pass
#         ind = state[key]
#         if ind:
#             state[key] = self.network.nodes[ind - 1]
#         else:
#             state[key] = self.network.bias
    
    def reconnect(self, owner):  # Link
        # - etablissement du proprietaire
        # - branchement des liaisons pendantes
        self._owner = owner
        self._connectstate(self.__dict__, "_source")
        if hasattr(self._source, "downLinks") and not (self in self._source.downLinks):
            #self._source.downLinks.append(self)
            self._source.downLinks.append(self)  #wr.proxy(
        
    #def __setstate__(self, state):  # Link
    #    self.__dict__.update(state)
    
    def __getstate__(self):  # Link
        #correction des enregistrements du pickling
        objdict = self.__dict__.copy()
        objdict["_source"] = self._source.nodeid
        objdict["_owner"] = None  #self._owner.nodeid
        return objdict
        
    def organize(self):  # Link
        node = self.owner
        network = node.owner
        if hasattr(self, "_parentID"): 
            # cas particulier ou la source est encore definie par un indice absolu
            value = getattr(self, "_parentID")
            if value > 0:  #self._parentID > 0:
                self._source = network.nodes[value - 1]
            elif not value:
                self._source = network.bias
            else:
                raise LinkError("Bad source ID : %s"% value)
            delattr(self, "_parentID")
        if hasattr(self._source, "downLinks"):
#              and not (self in self._source.downLinks):
            lst = getattr(self._source, "downLinks")
            if not self in lst:
                lst.append(self) 
                setattr(self._source, "downLinks", lst)
                # self._source.downLinks.append(self)
                # self._source.downLinks.append(self)  #wr.proxy(
        
#    def dzu(self):  # Link
#        return self.owner.derive
    
    def LambdaDZUDZ(self, inputval):  # Link
        return self.owner._lambda #* self.DZUDZ(inputval)  # child
    
    def prepareComputeHessian(self, localnodeCount, paramCount):  # Link
        self.SSProd = zeros(localnodeCount)
        self.FSPDU = zeros(paramCount)
        
    def deltaPartial(self):  # Link
        return 0  #self._value * self._source.partial # * self.sousProduit
    
    @Property
    def target(self):  # Link
        return self.owner        
    
    @Property
    def source(self):  # Link
        return self._source
    @source.setter
    def ssource(self, value):  # Link
        if self._source == value:
            return
        try:
            n = self._source.downLinks.index(self)
            if n >= 0:
                self._source.downLinks.pop(n)
            self._source = None
        except: pass
        # value est le noeud source
        self._source = value
        if hasattr(self._source, "downLinks") and not (self in self._source.downLinks):
            #self._source.downLinks.append(self)
            self._source.downLinks.append(self)  #wr.proxy
        
    @Property
    def NumeroTouteSynapse(self):  # Link
        res = self._linkid
        if res > FIX_LIMIT:
            res -= FIX_LIMIT
            res += self._source.owner.paramCount
        return res
    
    def initweight(self): pass  # Link

class DirectLink(Link):
    """lien direct.
le parametre de ce lien est toujours 1"""

    def equivalent(self, target):  # DirectLink
        return isinstance(target, DirectLink)
    
    def output(self):  # DirectLink
        if isinstance(self._source, Model):
            return self._source._outputs[self._linkid]
        if isinstance(self._source, (int, float)):
            return self._source
        if self._linkid >= 0:
            try: return self._source[self._linkid]
            except: return self._source(self._linkid)
        try: return self._source.value
        except:
            try: return float(self._source)  
            except: return list(self._source)

    @Property
    def value(self):  # DirectLink
        return 1
    
    @Property
    def style(self):  # DirectLink
        return LS_FIXE

class Synapse(Link):
    
    def __init__(self, owner, source=None, value=0.0, style=LS_STD, name=""):  # Synapse
        super(Synapse, self).__init__(owner, name, source=source)
        self.style = style
        self._value = value
        self._weightlist = None
        self._linkid = 2**32
        self._tagname = 'LINK'
        self._init = (0.0, 0.3)
            
    def reprlst(self):  # Synapse
        lst = super(Synapse, self).reprlst()
        lst.append("value : {}".format(self._value))
        return lst

    def _connectstate(self, state, key):  # Synapse
        ind = state[key]
        if ind:
            state[key] = self.owner.owner.nodes[ind - 1]  # network
        else:
            state[key] = self.owner.owner.bias
    
    @classmethod
    def createFromElementXML(cls, owner, element, localversion): # Synapse 
        name = element.get("name", "")
        style = int(element.get("style", "0"))
        
        res = cls(owner, None, 0.0, style, name)
        res._parentID = int(element.get("parentid", "0"))
        res._linkid = int(element.get("linkid", "0"))
        res._originalid = int(element.get("originalid", res._linkid))
        res.style = style
        lst = list(element)
        #list(element.getchildren())
        for subelmt in lst:
            if subelmt.tag == "VALUE": 
                val = floatEx(subelmt.text)
                res._value = val
#                if res._linkid < FIX_LIMIT: res._valuetemp = val
#                else: res._weightlist = [val]
            elif subelmt.tag == "MINIMUM": 
                try: res.setMinMax(floatEx(subelmt.text), None)
                except: pass
            elif subelmt.tag == "MAXIMUM": 
                try: res.setMinMax(None, floatEx(subelmt.text))
                except: pass
            elif subelmt.tag == "INIT":
                try:
                    center, dev = tuple(list(subelmt.text.split(";")))
                except:
                    center, dev = tuple(list(subelmt.text.split(",")))
                if (center != "NAN"):
                    res._init = (float(center), res._init[1]) 
                else: pass
                if (dev != "NAN"):
                    res._init = (res._init[0], float(dev))
                else: pass         
        return res

    def todata(self, syndata=None): # Synapse
        if syndata is None:
            syndata = SynapseData()
        syndata.sname = self.name
        syndata.originlayer, syndata.originindex = self._source.getIndexes()
        syndata.targetlayer, syndata.targetindex = self.owner.getIndexes()
        syndata.style = self.style
        syndata.value = self._value
        syndata.index = self._linkid 
        return syndata       
    
    def organize(self): # Synapse
        super(Synapse, self).organize()
        node = self.owner
        network = node.owner
        if self._source is None:
            raise LinkError("Link %s has no source"% self)
        if (self._source.nodeid >= node.nodeid):
            mess = "source node must be before target node : source=%d, target=%d"
            raise LinkError(mess%(self._source.nodeid, node.nodeid))                
        
        if self._linkid < FIX_LIMIT:
            self._weightlist = list(network._weights)
            if len(self._weightlist) < self._linkid + 1:
                #weightlist = self._weightlist.tolist()
                while len(self._weightlist) < self._linkid + 1:
                    self._weightlist.append(NAN)
            if hasattr(self, '_value') and (self._value is not None):
                self._weightlist[self._linkid] = self._value
                self._value = None
            network._weights = asarray(self._weightlist)
                #delattr(self, '_value') 
        #self.clearmem()

    def equivalent(self, target, withException=False): # Synapse
        eq = (self.value == target.value)
        eq |= abs((self.value - target.value)/(self.value + target.value)) < 1E-10
        if withException and not eq:
            raise AssertionError("Different link values %s: %s, %s: %s"%(self.linkid, self.value, target.linkid, target.value))
        return eq
    
    def deltaPartial(self):  # Synapse
        return self._value * self._source.partial # * self.sousProduit

    def initWeight(self): # Synapse
        self._value = normal(loc=self._init[0], scale=self._init[1])
        
    def isCommon(self, value=None):
        return (self._source.nodeid == 0) and (self.isFix()) and \
            ((value is None) or (self.value==value))
    
    def output(self): # Synapse
        return self._source.value * self.value
    
    def xmlChildren(self, indent='\t'): # Synapse
        res = []
        if self.value: 
            res.append('%s<VALUE>%s</VALUE>'% (indent, self.value))
        if self._init[0] or (self._init[1]!= 0.3):
            res.append("%s<INIT>%s;%s</INIT>"% (indent, self._init[0], self._init[1]))
        return res
    
    def xmlAttrList(self): # Synapse
        res = ['class="Synapse"']
        self.appendDefaultedAttribute(res, 'name', self.name, default=self.defaultname())
        self.appendDefaultedAttribute(res, 'style', self.style, default=0)
        self.appendDefaultedAttribute(res, 'linkid', self.linkid)
        if (self.originalid != self.linkid) and (self.originalid >= 0):
            self.appendDefaultedAttribute(res, 'originalid', self.originalid)
        self.appendDefaultedAttribute(res, 'parentid', self._source.nodeid)
        return res
    
    @Property
    def init(self): # Synapse
        return self._init
    @init.setter
    def sinit(self, *argv): # Synapse
        if len(argv) == 1:
            self._init = argv[0]
        else:
            self._init = tuple(argv[:2])
    
    def setMinMax(self, mini=None, maxi=None): # Synapse
        if maxi is None:
            try: 
                maxi = mini[1]
                mini = mini[0]
            except: pass
        if mini is not None:
            self._minimum = mini
        if maxi is not None:
            self._maximum = maxi
    @Property
    def minimum(self): # Synapse
        try: return self._minimum
        except: return -INF
    @minimum.setter
    def sminimum(self, value): # Synapse
        self._minimum = value
    
    @Property
    def maximum(self): # Synapse
        try: return self._maximum
        except: return INF
    @maximum.setter
    def smaximum(self, value): # Synapse
        self._maximum = value
    
    @Property
    def originalid(self): # Synapse
        if self._originalid < 0:
            return self._linkid
        else:
            return self._originalid
    @originalid.setter
    def soriginalid(self, value): # Synapse
        self._originalid = value
    
    @Property
    def linkid(self): # Synapse
        return self._linkid
    @linkid.setter
    def slinkid(self, value): # Synapse
        self._linkid = value
        if not self.isFix():
            self.style &= LS_FIXE
            self._weightlist = None
            
    @Property
    def activid(self): # Synapse
        if self._useOriginal:
            return self._originalid
        return self._linkid
    
    #@Property
    def isFix(self): # Synapse
        return bool(self._linkid >= FIX_LIMIT)
        
    @Property
    def value(self): # Synapse
        if self.isFix():
            val = self._value
        else:
            try:
                val = self._owner._owner._weights[self.activid]
            except:
                val = self._value
        #=======================================================================
        # try:
        #    val = self._weightlist[self.activid]
        # except:
        #    val = self._value
        #=======================================================================
        if LS_INVERSE & self.style: return 1/val
        return val        
    @value.setter
    def value(self, val): # Synapse
        try:
            self._owner._owner._weights[self.activid] = val
        except:
            self._value = val
    
    @Property
    def network(self): # Synapse
        try:
            return self.owner.owner
        except:
            raise LinkError("Cannot find synapse's network for %s"% self)
        
register(Synapse)
register(Synapse, "Synapse")
register(Synapse, "LINK")

if __name__ == "__main__":
    pass
                    