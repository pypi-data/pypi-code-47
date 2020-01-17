#-*- coding: ISO-8859-15 -*-
#===============================================================================
#  Module  driver
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
"""module __init__.
A developper
"""
from metaphor.nntoolbox.dataset import DataManager
from ._driver import DriverBase, Driver, saveModel, setCallback, \
        setSavingFormat
from ._optimizer import optim_bfgs, optim_leastsq
from ._workshop import Workshop
from ._networkfactory import NetworkFactory
from ._drivermultidyn import DriverMultiDyn #, doBootstrap, multitrain
from ._parallelJobs import trainJobBS, trainJob, onEndIter, onReturnResult, \
        onSpecialResult
from ._driverlib import DriverLib, DriverLibError

__all__ = ["DataManager", "Driver", "saveModel", "Workshop",
           "optim_bfgs", "optim_leastsq", "NetworkFactory",
           "setCallback", "setSavingFormat", "DriverMultiDyn",
           "DriverBase", "DriverMultiDyn", "trainJob", "trainJobBS",
           "onEndIter", "onReturnResult", "onSpecialResult", "DriverLib",
           "DriverLibError"]  #, "setUnicode"