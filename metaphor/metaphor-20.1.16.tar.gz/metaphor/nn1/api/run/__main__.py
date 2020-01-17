# -*- coding: ISO-8859-1 -*-
#-------------------------------------------------------------------------------
# $Id$
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
#-------------------------------------------------------------------------------
'''
Created on 14 december 2018

@author: jeanluc
'''
# import sys
# from . import  nn_run
# 
# nn_run.run(sys.argv)
#from metaphor.monal.util.monaltoolbox import yesNoQuestion
#from metaphor import chem_gm
from metaphor.nn1.api.run import nn_run
import sys, os

# res = 
nn_run.supervisor()

# from argparse import Namespace
# if isinstance(res, Namespace):
#     print("results in :", res.metaphorResult[0])
print("All Done")