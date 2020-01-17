#-*- coding: ISO-8859-15 -*-
#===============================================================================
# $Id: monalrecords.py 4789 2018-06-08 11:40:08Z jeanluc $
#  Module _ndkWorkshop.py
#  Projet MonalDLL
#  MonaEx70 DLL interface avancé (Neuro Developer Kit)
#
#  Author: Jean-Luc PLOIX  -  NETRAL
#  July 2008
# 
#===============================================================================
"""Module defining useful 'Structure's for Neural developper kit (NDK).
"""
from ctypes import Structure, sizeof, c_short, c_ushort, c_byte, c_int, byref, \
    c_long, c_double, create_string_buffer, memset, memmove, addressof, string_at  #, c_char
from functools import partial

from .Property import Property, setter
from .util.utils import Class_doc
from . import monalconst as C

# __all__ = ["LoopData", "SynapseData", "NodeData", "LayerData", "MergeData", 
#            "ModelData", "DataDrivenModel", "DataDrivenModelTrain", "baseData"]

#-----------------------------------------------
class baseData(Structure):
    __doc__ = Class_doc("""Abstract base class for data-structures.""")
    def _setstr_at(self, field, value, lenmax=256):
        start = addressof(self) + field.offset
        val = value.encode()
        st = create_string_buffer(val)           
        memmove(start, byref(st), min(len(st), lenmax))
            
    def _getstr_at(self, field):
        start = addressof(self) + field.offset
        return string_at(start).decode()
#---------------------------------------
class LoopData (baseData):  # commun avec Delphi (TLoopDataEx)
    """
    Model loop creation data.
    
    Used for ModifyNetwork, with style: AddLoop.
    
    Fields :
        
    :layer: layer index
    :node: Node index in layer
    :state: State index
    :redondancy: Take care of redondancy while building a loop
    :notCreateSynapses: Dont create synapses
    :existingnode: Existing origin node
    """    
    #===========================================================================
    # __doc__ = Class_doc("""Donnees de bouclage reseau.
    # Utilisé pour ModifyNetwork, avec le style: AddLoop.""")
    #===========================================================================
    _fields_ = [
        ("layer", c_short),
        ("node", c_short),
        ("state", c_short),
        ("redondancy", c_ushort),
        ("notCreateSynapses", c_ushort),
        ("existingnode", c_ushort)]
    
    def __repr__(self):
        st = super(LoopData, self).__repr__()
        st2 = '(%s, %s, %s, %s, %s, %s)'% (self.layer, self.node, self.state, 
            self.redondancy, self.notCreateSynapses, self.existingnode)
        return st + st2

    def __init__(self, layer=0, node=0, order=1, nosynapse=0, existingnode=0):
        super(LoopData, self).__init__()
        memset(byref(self), 0, sizeof(self))
        self.layer = layer
        self.node = node
        self.state = order
        self.redondancy = 1
        self.notCreateSynapses = nosynapse
        self.existingnode = existingnode

#---------------------------------------
class SynapseData (baseData):  #  commun avec Delphi
            # Pour Movenode, si <> 0, l'entrée de rang
            # RangOrigine est déplacé dans la couche constante
            # avec la valeur "Valeur"
            # Pour MERGENODE si <> 0, absorbtion des synapses parents
    """
    Node link data.
    
    Used for ModifyNetwork with styles :
    
        - Movenode
        - MergeNeuron
        - NouvelleSynapse
        - DetruireSynapse
        - ModifierSynapse
        
    Fields:
    
    :size: Current record size
    :originLayer: Layer index of origin node
    :originIndex: Index of origin node in its layer
    :targetLayer: Layer index of target node
    :targetIndex: Index of target node in its layer
    :style: Link style
    :inputBool: Include input in action
    :outputBool: Include output in action
    :value: Parameter value
    :_name: Parameter name
    :netIndex: Model Index in multi model
    :index: Link index in model
    
    """
    #===========================================================================
    # __doc__ = Class_doc("""Données de lien entre noeuds.
    # Utilisé pour ModifyNetwork avec les styles :
    #    Movenode
    #    MergeNeuron
    #    NouvelleSynapse
    #    DetruireSynapse
    #    ModifierSynapse""")
    #===========================================================================
    _fields_ = [
        ("size", c_int ),
        ("originLayer", c_short),
        ("originIndex", c_short),
        ("targetLayer", c_short),
        ("targetIndex", c_short),
        ("style", c_ushort), # style de lien synaptique. Constantes ls...
        ("inputBool", c_ushort), 
        ("outputBool", c_ushort), # Pour AbsorberNeurone si <> 0, absorbtion des synapses enfants
        ("value", c_double),
        ("_name", c_byte* 256),
        ("netIndex", c_int),
        ("index", c_int)]
    
    def __repr__(self):
        st = super(SynapseData, self).__repr__()
        st2 = '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'% (self.originLayer, 
            self.originIndex, self.targetLayer, self.targetIndex, self.style, 
            self.inputBool, self.outputBool, self.value, self.sname, self.netIndex, 
            self.index)
        return st + st2

    def __init__(self, name='', originlayer=-2, originindex=-1, targetlayer=-2, 
                 targetindex=-1, style=0, inputbool=0, outputbool=0, 
                 netindex=-1, synindex=-1, value=0.0):
        super(SynapseData, self).__init__()
        memset(byref(self), 0, sizeof(self))
        self.size = sizeof(self)
        self.originLayer = originlayer
        self.originIndex = originindex
        self.targetLayer = targetlayer
        self.targetIndex = targetindex
        self.style = style
        self.inputBool = inputbool
        self.outputBool = outputbool
        self.value = value
        self.sname = name
        self.netIndex = netindex
        self.index = synindex
    
    @Property
    def sname(self):
        """
        Property.
        
        Link sname. 
        """
        return self._getstr_at(self.__class__._name)
    @setter(sname)
    def _setname(self, value):
        self._setstr_at(self.__class__._name, value)

#---------------------------------------
class NodeData (baseData):  #  commun avec Delphi
    # !!! ATTENTION !!! Correspond au TNeuronDataEx du code Delphi
    """
    Network node data.
    
    Used for GetNeuroneInfo, or ModifyNetwork, with styles:
    
        - ModifierNeurone
        - AjoutNeurone
        - SupprimerNeurone
    
    Fields :
    
    :size: Current record size
    :_name: Node name
    :modelName: Model name
    :layerIndex: Node layer index
    :nodeIndex: Node index in its layer
    :activation: activation function
    :nodeID: Node ID
    :nodeType: Type of node
    :stylePos: Type of positioning
    :nodePos: Node position
    :activationPlus: Second activation function
    :indexNet: Model Index in multi model
    :value: Node value
    """
    #===========================================================================
    # __doc__ = Class_doc("""Données de noeud de modèle neuronal. Utilisé pour :
    # GetNeuroneInfo, ou ModifyNetwork, avec les styles:
    #    ModifierNeurone
    #    AjoutNeurone
    #    SupprimerNeurone
    # et pour les modifications de nom de modèle.""")
    #===========================================================================
    _fields_ = [
        ("size", c_int ),        
        ("_name", c_byte*256),
        ("modelName", c_int),
        ("layerIndex", c_int),
        ("nodeIndex", c_int),
        ("activation", c_int),
        ("nodeID", c_int),
        ("nodeType", c_int),     # TNeuronType : (ntNone, ntSigma, ntSigma2, ntPi, ntSigmaPlus)
        ("stylePos", c_int),       # TPositionStyle : (psBegin, psEnd)
        ("nodePos", c_int), # TAddNeuronType : (anDontCare, anConstant, anInput, anOutPut, anOutState)
        ("activationPlus", c_int),
        ("indexNet", c_int),
        ("value", c_double)]

    def __repr__(self):
        st = super(NodeData, self).__repr__()
        st2 = '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'% (self.name, 
            self.modelName, self.layerIndex, self.nodeIndex, C.ACTIV_NAME[self.activation], self.nodeID, 
            self.nodeType, self.stylePos, self.nodePos, self.value, 
            C.ACTIV_NAME[self.activationPlus], self.indexNet)
        return st + st2
    
    def __init__(self, name='', isnetname=0, layerindex=-2, nodeindex=-1, 
                 activation='TANH', nodeID=-1, nodetype=1, style=0, 
                 nodeposition=0, value=0.0, netindex=-1, Model=None):
        super(NodeData, self).__init__()
        memset(byref(self), 0, sizeof(self))
        self.size = sizeof(self)
        if Model:
            self.name = Model.Name 
            self.modelName = Model.NetWorkName
            self.layerIndex = Model.LayerIndex
            self.nodeIndex = Model.NeuronIndex 
            self.activation = Model.Activation
            self.nodeID = Model.NeuronID
            self.nodeType = Model.NeuronType
            self.stylePos = Model.StylePos
            self.nodePos = Model.NeuronPosition
            self.value = Model.value
            self.activationPlus = Model.ActivationPlus
            self.indexNet = Model.IndexNet
        else:
            self.name = name 
            self.modelName = isnetname
            self.layerIndex = layerindex
            self.nodeIndex = nodeindex 
            self.activation = C.getActivIndex(activation)
            self.nodeID = nodeID
            self.nodeType = nodetype
            self.stylePos = style
            self.nodePos = nodeposition
            self.value = value
            self.activationPlus = 0
            self.indexNet = netindex
        
    @Property
    def name(self):
        """
        Property.
        
        Node name. 
        """
        return self._getstr_at(self.__class__._name)
    @setter(name)
    def _setname(self, value):
        self._setstr_at(self.__class__._name, value)

#---------------------------------------
class LayerData (baseData):  #  commun avec Delphi
    """
    Layer data.
    
    Used for ModifyNetwork with styles :
    
    - NouvelleCouche
    - DetruireCouche
    
    Fields :
    
    :size: Current record size
    :index: Layer index in the model
    :length: Layer length
    :activation: Common node activation
    :nodeType: Common type of nodes
    :stylePos: Positionning style
    :activationPlus: Secundary activation
    :_name: Base name for nodes
    :netIndex: Index of model in multi models
    :defaultnodevalue: Default nodes value
    """
#    __doc__ = Class_doc("""Données de couche. 
#    Utimisée pour  ModifyNetwork avec les styles :
#        NouvelleCouche
#        DetruireCouche.""")
    _fields_ = [    
        ("size", c_int ),
        ("index", c_short),
        ("length", c_short),
        ("activation", c_short),
        ("nodeType", c_ushort),
        ("stylePos", c_ushort),
        ("activationPlus", c_short),
        ("_name", c_byte*256),
        ("netIndex", c_int),
        ("defaultnodevalue", c_double),]

    # !!! attention changement de valeur par defaut  index=0 -> 1
    def __init__(self, name='', index=1, length=0, activfunc='TANH', ntype=1, style=0, defaultnodevalue=0.0):
        super(LayerData, self).__init__()
        memset(byref(self), 0, sizeof(self))
        self.size = sizeof(self)
        self.index = index
        self.length = length
        self.activation = C.getActivIndex(activfunc)
        self.nodeType = ntype
        self.stylePos = style
        self.activationPlus = 0
        self.name = name
        self.netIndex = 0
        self.defaultnodevalue = defaultnodevalue

    def __repr__(self):
        st = super(LayerData, self).__repr__()
        st2 = '(%s, %s, %s, %s, %s, %s, %s, %s, %s)'% (self.index, self.length, 
            C.ACTIV_NAME[self.activation], self.nodeType, self.stylePos, 
            C.ACTIV_NAME[self.activationPlus], self.name, self.netIndex,
            self.defaultnodevalue)
        return st + st2

    @Property
    def name(self):
        """
        Property.
        
        layer nodes name
        """
        return self._getstr_at(self.__class__._name)
    @setter(name)
    def _setname(self, value): 
        self._setstr_at(self.__class__._name, value)

#---------------------------------------
class MergeData( baseData ):  #  commun avec Delphi
    """
    Model merging data.
    
    Fields :
    
    :size: Current record size
    :_source: File name for the model to merge
    :inMerge: Merging of inputs
    :layerShift: Shift in layer index
    :nodeShift: Shift in node index
    :autoMerge: Merge of current model with itself
    :plugIn: Plugin the merged model if possible
    :sharedSynapses: Share the links between models
    :byName: Merge choice by node names 
    """
#    __doc__ = Class_doc("""Donnees de fusion.
#    Utilise par modifyModel avec le style 
#        MERGEMODEL.""")
    _fields_ = [("size", c_int ),
                ("_source", c_byte*256),
                ("inMerge", c_short),
                ("layerShift", c_short),
                ("nodeShift", c_short),
                ("autoMerge", c_ushort),
                ("plugIn", c_ushort),
                ("sharedSynapses", c_ushort),
                ("byName", c_ushort)]
    
    def __init__(self, source="", ninputmerge=0, nlayershift=0, nnodeshift=0,
        automerge=0, plugin=0, sharedsynapses=0, byname=0):
        super(MergeData, self).__init__()
        memset(byref(self), 0, sizeof(self))
        self.size = sizeof(self)
        self.source = source
        self.inMerge = ninputmerge
        self.layerShift = nlayershift
        self.nodeShift = nnodeshift
        self.autoMerge = automerge
        self.plugIn = plugin
        self.sharedSynapses = sharedsynapses
        self.byName = byname

    def __repr__(self):
        st = super(MergeData, self).__repr__()
        st2 = '(%s, %s, %s, %s, %s, %s, %s, %s)'% (self.source, self.inMerge, 
            self.layerShift, self.nodeShift, self.autoMerge, self.plugIn, 
            self.sharedSynapses, self.byName)
        return st + st2

    @Property
    def source(self):
        """
        Propertry.
        
        merging model source.
        """
        return self._getstr_at(self.__class__._source)
    @setter(source)
    def _setsource(self, value): 
        self._setstr_at(self.__class__._source, value)

#---------------------------------------
class ModelData( baseData ):  #  commun avec Delphi
    """
    Model data.
    
    Used by ndkInterface, createNewModel, recreateModel
    
    Fields :
    
    :size: Current record size
    :input: Number of inputs
    :output: Number of outputs
    :hidden: Number of hidden nodes
    :activation: activation function of hidden nodes
    :layer: layer of loop origin node
    :node: index in its layer if loop origin node
    :state: number of loops
    :redondancy: Take care of redundancy while creating loops
    :notCreateSynapses: Dont create synapses
    :existingNode: Origin node is an exissting node
    :polyType: Polynom type
    :_name: Model name
    """
#    __doc__ = Class_doc("""Donnees de modele - 
#    Utilise par
#        ndkInterface 
#        createNewModel
#        recreateModel.""")
    _fields_ = [( "size", c_int ),
                ( "input", c_int ),
                ( "output", c_int ),
                ( "hidden", c_int ),
                ( "activation", c_short ),
                ( "layer", c_short ),
                ( "node", c_short ),
                ( "state", c_short ),
                ( "redondancy", c_byte ),
                ( "notCreateSynapses", c_byte ),
                ( "existingNode", c_byte ),     # pour les bouclages
                ( "polyType", c_short),
                ( "_name", c_byte*256)]

    def __init__(self, input=1, output=1, hidden=2, activfunc="TANH", 
            statelayer=-1, statenodeindex=-1, order=0, nosynapse=0, 
            existingnode=0, polytype=0, name=""):
        super(ModelData, self).__init__()
        memset(byref(self), 0, sizeof(self))
        self.size = sizeof(self)
        self.input = input
        self.output = output
        self.hidden = hidden
        self.activation = C.getActivIndex(activfunc)
        self.layer = statelayer
        self.node = statenodeindex
        self.state = order
        self.redondancy = 1
        self.notCreateSynapses = nosynapse
        self.existingNode = existingnode
        self.polyType = polytype
        #if isinstance(name, str):
        self.name = str(name)            
        
    def __repr__(self):
        st = super(ModelData, self).__repr__()
        st2 = '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'% (self.input, 
            self.output, self.hidden, self.activation, self.layer, self.node, 
            self.state, self.redondancy, self.notCreateSynapses, 
            self.existingNode, self.polyType, self.name)
        return st + st2

    @Property
    def name(self):
        """
        Property
        
        Model name.
        """
        return self._getstr_at(self.__class__._name)
    @setter(name)
    def _setname(self, value): 
        self._setstr_at(self.__class__._name, value)

#TModelData = ModelData # compatibilité
#---------------------------------------
class DataDrivenModel (baseData): # commun avec delphi TDataDrivenModel
    """
    Data for data driven model creation.
    
    Fields :
    
    :size: Current record size
    :input: Number of inputs
    :output: Number of outputs
    :hidden0: Minimum number of hidden nodes
    :hiddenM: Maximum number of hidden nodes
    :order: Order of model
    :polyType: Type of polynom
    :normalize: normalisation action
    :_savedir: saving folder
    :_tempdir: temporary folder
    :dataFormat: format of data 
    """
#    __doc__ = Class_doc("""Donnees de creation d'un modele pilote par les donnees""")
    _fields_ = [
        ("size", c_long),
        ("input", c_long),
        ("output", c_long),
        ("hidden0", c_long),
        ("hiddenM", c_long),
        ("order", c_long),
        ("polyType", c_long),
        ("_reserve1", c_long),
        ("normalize", c_long),
        ("_reserve2", c_long),
        ("_savedir", c_byte*256),
        ("_tempdir", c_byte*256),
        ("dataFormat", c_long*256)]
    
    def __init__(self, inputs=-1, outputs=-1, hidden0=-2, hiddenm=5, order=0, 
                 polyt=0, normalize=1, savedir="", tempdir="", dataformat=[]):
        super(DataDrivenModel, self).__init__()
        memset(byref(self), 0, sizeof(self))
        self.size = sizeof(self)
        self.input = inputs
        self.output = outputs
        self.hidden0 = hidden0
        self.hiddenM = hiddenm
        self.order = order
        self.polyType = polyt
        self.normalize = normalize
        self.savedir = savedir
        self.tempdir = tempdir
        for ind in range(256):
            self.dataFormat[ind] = -1
        for ind, item in enumerate(dataformat):
            self.dataFormat[ind] = int(item)

    def __repr__(self):
        st = super(DataDrivenModel, self).__repr__()
        st2 = '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'% (self.input, self.output, 
            self.hidden0, self.hiddenM, self.order, self.polyType, self.normalize,
            self.saveDir, self.tempDir, self.dataFormat)
        return st + st2
    
    @Property
    def savedir(self):
        """
        Property.
        
        Saving folder.
        """
        return self._getstr_at(self.__class__._savedir)
    @setter(savedir)
    def _setsavedir(self, value):
        self._setstr_at(self.__class__._savedir, value)

    @Property
    def tempdir(self):
        """
        Property.
        
        Temporary folder.
        """
        return self._getstr_at(self.__class__._tempdir)
    @setter(tempdir)
    def _settempdir(self, value): 
        self._setstr_at(self.__class__._tempdir, value)

#-------------------------------------------------------------------------------
class DataDrivenModelTrain (baseData):
    """
    Training data for data driven model.
    
    Fields :
    
    :size: Current record size
    :inits: Number of parameters initialisation per model
    :style: Training style
    :criterion: Choice criterion
    :algorithm: Training algorithm
    :epochs: Number of epochs for each parameters initialisation
    :_subdir: Saving sub-folder
    :_target: Target file name
    :onFlightCriterion: On flight selection criterion
    """
    #__doc__ = Class_doc("""donnees d'apprentissage d'un model pilote par les donnees""")
    _fields_ = [
        ("size", c_long),
        ("inits", c_long),
        ("style", c_long),
        ("criterion", c_long),
        ("algorithm", c_long),
        ("epochs", c_long),
        ("_subdir", c_byte*256),
        ("_target", c_byte*256),
        ("onFlightCriterion", c_long)]
    
    def __init__(self, inits=10, style=C.TR_S_INIT_PARAM_LEVERAGE, 
                 onFlightCriterion=C.TCR_STD_DEV_BIAS_LESS, 
                 criterion=C.TCR_STD_DEV_BIAS_LESS,
                 algorithm=C.TA_LM, epochs=50, subdir="", target=""):
        super(DataDrivenModelTrain, self).__init__()
        memset(byref(self), 0, sizeof(self))
        self.size = sizeof(self)
        self.inits = inits
        self.style = style
        self.criterion = criterion
        self.algorithm = algorithm
        self.epochs = epochs
        self.subDir = subdir
        self.target = target
        self.onFlightCriterion = onFlightCriterion 

    def __repr__(self):
        st = super(DataDrivenModelTrain, self).__repr__()
        st2 = '(%s, %s, %s, %s, %s, %s, %s, %s)'% (self.inits, self.style, 
            self.criterion, self.algorithm, self.epochs, self.subDir, self.target, 
            self.onFlightCriterion)
        return st + st2
    
    @Property
    def subdir(self):
        """
        Property.
        
        Saving subdir.
        """
        return self._getstr_at(self.__class__._subdir)
    @setter(subdir)
    def _setsubdir(self, value): 
        self._setstr_at(self.__class__._subdir, value)

    @Property
    def target(self):
        """
        Property.
        
        Target folder
        """
        return self._getstr_at(self.__class__._target)
    @setter(target)
    def _settarget(self, value):
        self._setstr_at(self.__class__._target, value)

#-------------------------------------------------------------------------------
if __name__ == "__main__":
    print(baseData.__doc__)
    print()
    print(LoopData.__doc__)
    print()
    print(SynapseData.__doc__)
    print()
    print(NodeData.__doc__)
    print()
    print(LayerData.__doc__)
    print()
    print(MergeData.__doc__)
    print()
    print(ModelData.__doc__)
    print()
    print(DataDrivenModel.__doc__)
    print()
    print(DataDrivenModelTrain.__doc__)
    