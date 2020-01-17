#-*- coding: ISO-8859-15 -*-
#===============================================================================
# $Id: _networkfactory.py 4727 2018-03-09 13:16:43Z jeanluc $
#  Module  _networkfactory
#  Projet MonalPy
# 
#  Implementation python de monal, factory
#
#  Author: Jean-Luc PLOIX  -  NETRAL
#  Juillet 2013
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
from .. import monalconst as C
from ..Property import Property, setter, lengetter 
from ..driver import Driver

class NetworkFactory(Driver):
    
    def __init__(self, filename="", modelname="model_0", inputs=0, outputs=0, 
            hidden=0, activfunc="TANH", polytype=0, nosynapse=0):
        super(NetworkFactory, self).__init__(source=filename, modelname=modelname, 
            inputs=inputs, outputs=outputs, hidden=hidden, activfunc=activfunc, 
            polytype=polytype, nosynapse=nosynapse)
        
        self._lastaction = None
        
    def destroyModel(self):
        return self.__del__
    
    def normalizeWeights(self):
        return self.mainModel.normalizeWeights()
    
    @Property
    def action(self):
        return self._lastaction
    
    @setter(action) 
    def _setaction(self, value):  # set the action
        #setting the action.
        raise Exception("Not implemented yet")
#         self._lastaction = None
#         if not self._lastaction:
#             self._lastaction = value
            
    @Property
    def info(self, index):
        param = 0
        if isinstance(index, tuple):
            if len(index) == 2:
                param = index[0]
                index = index[1]
            elif len(index) == 3:
                param = self.getNodeInfo(index[0], index[1]).nodeID
                index = index[2]
        if index == None:
            index = param
            param = 0
        if isinstance(index, str):
            index = C.INFO_D[index]
        if (0 <= index < C.INFO_COUNT):
            res = self.getinfo(index)
            #lib[NC.n_GetInfo](self._handle, c_int(index))
        elif (C.INFO_R_THRESHOLD <= index < C.INFO_R_THRESHOLD + C.INFO_R_COUNT):
            #value = c_double(0)
            index -= C.INFO_R_THRESHOLD
            res = self.getrealvalue(param, index)
            #lib[NC.n_GetRealValue](self._handle, param, byref(value), 
            #                         c_int(index))
            #res = value.value
        elif (C.INFO_I_THRESHOLD <= index < C.INFO_I_THRESHOLD + C.INFO_I_COUNT):
            res = self.getindexinfo(param, index)
            #index -= C.INFO_I_THRESHOLD
            #lib[NC.n_GetIndexInfo](self._handle, c_int(param), c_int(index))
        else:
            raise IndexError("Index Error in getInfo")
        return res
        #raise Exception("info Not implemented yet")
    
    @lengetter(info)  
    def _linfo(self):
        #Total length of info vector property.
        return C.INFO_TOTAL_COUNT
    @setter(info) 
    def _setinfo(self, index, style, value=None):
        #info property setter
        if isinstance(index, tuple): 
        # syntax xx.info[index1, index2, style] = value
            value = style
            style = index[1]
            index = index[0]
        if value == None:   
        # syntax xx.info[style] = value
            value = style
            style = index
            index = 0
        assert style in C.LOADABLE_INFOS, "%s in read only" % C.INFO_DICT[style]
        if (0 <= style < C.INFO_COUNT):
            self.setivalue(style, value)
            #return lib[NC.n_SetIValue](self._handle, value, c_int(style))
                #self.setIValue(value, style)
        elif (C.INFO_R_THRESHOLD <= style < C.INFO_R_THRESHOLD + C.INFO_R_COUNT):
            style -= C.INFO_R_THRESHOLD
            return self.setrealvalue(style, index, value)
            #cvalue = c_double(value)
            #return lib[NC.n_SetRealValue](self._handle, index, cvalue,c_int(style))
        elif (C.INFO_I_THRESHOLD <= style < C.INFO_I_THRESHOLD + C.INFO_I_COUNT):
            style -= C.INFO_I_THRESHOLD
            return self.setindexvalue(style, index, value)
            #cvalue = c_double(value)
            #return lib[NC.n_GetIndexInfo](self._handle, c_int(index), c_int(style))
    
    def modifyModel(self, param, style):
        """
        Model modification.
        
        The effective modification depends upon the style parameter, 
        and the param parameter accordingly :
        
        +-----------------+------+------------+-------------------------------------+
        | style           |value | param      | action                              |
        +=================+======+============+=====================================+
        | FIXMODEL        | 1    | NA         | All synapses are fixed              |
        +-----------------+------+------------+-------------------------------------+
        | MODIFYNODE      | 2    | NodeData   | Node modification                   |
        +-----------------+------+------------+-------------------------------------+
        | ADDLOOP         | 3    | LoopData   | Add a new loop                      |
        +-----------------+------+------------+-------------------------------------+
        | DIFFERENTIALLOOP| 4    | BoucleDiff | Add a differential loop             | 
        +-----------------+------+------------+-------------------------------------+
        | ADDNODE         | 5    | NodeData   | Add a node to the network           |
        +-----------------+------+------------+-------------------------------------+
        | DELETENODE      | 6    | NodeData   | Delete a node from the network      |
        +-----------------+------+------------+-------------------------------------+
        | MOVENODE        | 7    | SynapseData| Move a node inside the network      |
        +-----------------+------+------------+-------------------------------------+
        | MERGENODE       | 8    | SynapseData| Merge two nodes in the network      |
        +-----------------+------+------------+-------------------------------------+
        | ADDLINK         | 9    | SynapseData| Add a link between two nodes        |
        +-----------------+------+------------+-------------------------------------+
        | DELETELINK      | 10   | SynapseData| Delete a link between two nodes     |
        +-----------------+------+------------+-------------------------------------+
        | MODIFYLINK      | 11   | SynapseData| Modifiy a link                      |
        +-----------------+------+------------+-------------------------------------+
        | ADDLAYER        | 12   | LayerData  | Add a layer inside the network      |
        +-----------------+------+------------+-------------------------------------+
        | DELETELAYER     | 13   | LayerData  | Delete a layer from the network     |
        +-----------------+------+------------+-------------------------------------+
        | MERGEMODEL      | 14   | MergeData  | Merge the model with another model  |
        +-----------------+------+------------+-------------------------------------+
        | COMPACTMODEL    | 15   | int        | Compact the network.                |
        |                 |      |            |                                     |
        |                 |      |            | 1: avoid inputs compaction          |
        |                 |      |            |                                     |
        |                 |      |            | 2: avoid layers compaction          |
        |                 |      |            |                                     |
        |                 |      |            | 4: avoid parameters compaction      |
        +-----------------+------+------------+-------------------------------------+

        License level 2 or higher.
        
        """
        #=======================================================================
        # if isinstance(param, int):
        #     par = c_int(param)
        # elif param:
        #     par = byref(param)
        # else:
        #     par = None
        #=======================================================================
        #return lib[NC.n_ModifyModel](self._handle, par, c_int(style))
        if style == C.ADDLAYER:
            return self.mainModel.insertLayer(name=param.name, index=param.index, 
                length=param.length, activfunc=param.activation, 
                nodetype=param.nodeType, stylePos=param.stylePos)
        elif style == C.MODIFYNODE:
            return self.modifnode()
        
        elif style in [C.COMPACTMODEL]:
            return self.normalizeWeights()
            
        raise Exception("modifyModel Not implemented yet for style = %s"% style)

    def mergeModel(self, source=None, ninputmerge=0, nlayershift=0, nnodeshift=0,
        automerge=0, plugin=0, sharedsynapses=0, byname=0, mergedata=None):
        """Merge the network with another network."""
        if mergedata:
            source = mergedata.source
            ninputmerge = mergedata.inMerge
            nlayershift = mergedata.layerShift
            nnodeshift = mergedata.nodeShift
            automerge = mergedata.autoMerge
            plugin = mergedata.plugIn
            sharedsynapses = mergedata.sharedSynapses
            byname = mergedata.byName
        if automerge:
            return self.mergeModel(source=self, ninputmerge=ninputmerge, 
                nlayershift=nlayershift, nnodeshift=nnodeshift, 
                plugin=plugin, sharedsynapses=sharedsynapses, byname=byname)
        if isinstance(source, str):
            nsource = Driver(source)
            return self.mergeModel(source=nsource, ninputmerge=ninputmerge, 
                nlayershift=nlayershift, nnodeshift=nnodeshift, 
                plugin=plugin, sharedsynapses=sharedsynapses, byname=byname)
        while nlayershift < 0:
            self.mainModel.insertLayer(index=1)
            nlayershift += 1
        
        
        totreat = []
        lst = [node for node in self.mainModel.inputNodes]
        inlst = [node for node in source.mainModel.inputNodes]
        if byname:
            for node in lst:
                for innode in inlst:
                    if node.name == innode.name:
                        totreat.append((node, innode))
        elif ninputmerge:
            for index, (node, innode) in enumerate(zip(lst, inlst)):
                if index >= ninputmerge:
                    break
                totreat.append((node, innode))
                
        treated = []
        for node, target in totreat:
            treated.append(target)
            if node == target:
                raise Exception("Errot in model merging")
            node.absorb(target, outputs=True)
        
        self.mainModel.bias.absorb(source.mainModel.bias)
        
        for innode in inlst:
            if not innode in treated:
                self.mainModel.insertNode(innode, (0, -1))
        pass        
        for il in range(1, source.mainModel.layerCount):
            for node in source.mainModel.layers(il):
                self.mainModel.insertNode(node, (il + nlayershift, -1))
            
            #self.mainModel.layerExtend(il + nlayershift, source.mainModel.layers(il))        
        #if not sharedsynapses:
        self.mainModel.organize()
        
        #return lib[NC.n_MergeModel](self._handle, hsource, ssource, byref(mergedata))
        #raise Exception("Not implemented yet")
    
    @Property
    def nodeNames(self, index):
        """
        Indexed property.
        
        get a node name. 
        """
        node = self.mainModel.getNode(index)
        if node:
            return node.name
        return None

    def _lnodeNames(self):
        #reading the nodes number and writing it to the nodeNames vector."""
        return self.inputCount
    #self.getInfo(C.NODE_COUNT) 
    @setter(nodeNames)
    def _setnodeNams(self, index, value): 
        #writing a node name"""          
        node = self.mainModel.getNode(index)
        if node:
            node.name = value
            return node.name
        return ""
    
    def getNodeInfo(self, layerindex=-1, nodeindex=-1, netindex=-1, 
                    nodedata=None, syndata=None, origin=0):
        """
        Information record NodeData on a node.
        
        :param origin: Definr the use of origin or taget node in syndata
        
        :type origin: bool
        
        :param syndata: If exists, target node is defined by origin. Other parameter are ignored.
        
        :type syndata: SynapseData
        
        :param nodedata: if Exists, define the parget node.
        
        :type nodedata: NodeData
        
        :param layerindex: Layer of the target node;
        
        :type layerindex: int
        
        :param nodeindex: Target node index in its layer
        
        :type : int
        
        :param netindex: Index of the model holding the node (for multi model only).
        
        :type : int
        
        """
        if syndata:
            if origin:
                return self.getNodeInfo(syndata.originLayer, 
                                        syndata.originIndex, syndata.netIndex)
            else:
                return self.getNodeInfo(syndata.targetLayer, 
                                        syndata.targetIndex, syndata.netIndex)
        if nodedata:
            return self.getNodeInfo(nodedata.layerindex, nodedata.nodeindex)
        self.lastResult = self.mainModel.nodeinfo(layerindex, nodeindex)
        return self.lastResult

    def getSynapseInfo(self, originlayer=-2, originindex=-1, targetlayer=-2, 
            targetindex=-1, netindex=-1, synindex=-1, style=0, synapsedata=None):
        """
        Information record SynapseData on a synaptic link.
        
        :param synapsedata: If Exists define the target link.
        
        :type synapsedata: SynapseData
        
        :param originlayer: Layer index of the origin node of the target link.
        
        :type originlayer: int
        
        :param originindex: Origin node index in its layer of the target link.
        
        :type originindex: int
        
        :param targetlayer: Layer index of the target node of the target link.
        
        :type targetlayer: int
        
        :param targetindex: Target node index in its layer of the target link.
        
        :type targetindex: int
        
        :param netindex: Index of the model holding the node (for multi model only).
        
        :type netindex: int
        
        :param sinindex: Index of the link with the described origin and target nodes
        
        :type sinindex: int

        """
        if synapsedata:
            originlayer = synapsedata.originlayer
            originindex = synapsedata.originindex
            targetlayer = synapsedata.targetlayer
            targetindex = synapsedata.targetindex
            synindex = synapsedata.synindex
            style = synapsedata.style
        return self.mainModel.synapseinfo(originlayer=originlayer, 
                 originindex=originindex, targetlayer=targetlayer, 
                 targetindex=targetindex, synindex=synindex, style=style)

