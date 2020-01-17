#-*- coding: ISO-8859-15 -*-
#===============================================================================
#  Module  model
#  Projet MonalDLL
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
"""model module.
Modelling classes :
    - model      -> base class of all modelling classes;
    - modelcontainer -> 
    - normalizer -> normalizing class;
    - network    -> neuron network class;
    - node       -> additive node class;
    - nodepi     -> multiplicative node lcass
    - directLink -> direct node link class;
    - synapse    -> synaptic node link class.
"""

from ._link import *
from ._linmodel import *
from ._network import *
from ._node import *
from ._model import Leurre, ModelBase, Model
from ._modelcontainer import *
from ._modellib import *
from ._pseudomatrix import *
#from . import _monalfunc as monalfunc
#from _networkfactory import NetworkFactory
__all__ = ["DirectLink", "Synapse", "Normalizer", "Polynom", "Model", 
           "ModelBase", "Leurre", "ModelLib", "PseudoMatrix", "ModelLibError"
           "monalError", "dimensionError", "Network", "Node", "Nodepi", 
           "newNode", "monalfunc", "Multimodel", "ms_parallel", "ms_serie",
           "codeVersionOK", "pseudoMatrix"]

