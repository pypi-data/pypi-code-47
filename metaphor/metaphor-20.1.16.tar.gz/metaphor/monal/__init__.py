#-*- coding: ISO-8859-15 -*-
#===============================================================================
#  Module  monal
#  Projet MonalPy
#
#  Implementation python de monal
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
"""monal module version 3.3
non-linear process modelling.
Sub modules :
    - monalconst   -> common constants
    - monalrecords -> data structures for ctype communicatioon with NDK DLL
    - specialmath  -> special numbers: INF, -INF, NAN
    - util         -> utilities
    - Property     -> special property module, adding formal vector properties feature
    - version      -> module version management
Sub modules for full Python version :
    - model        -> linear and non-linear python models;
    - driver       -> python model driver.
    - lcode        -> C code model
    - include      -> include files for C models
    - library      -> computed libraries management
"""

import os, sys
try:
    __path__
except:
    __path__ = [os.path.dirname(__file__)]
if not __path__[0] in sys.path:
    sys.path.append(__path__[0])

from metaphor.version import __version__
from metaphor.nntoolbox.utils import  getancestor, addpathlist, null
from datetime import datetime

#print("checking 'monal' rights")
CHECK_TOKEN = 1
if CHECK_TOKEN:
    from metaphor.nntoolbox.toktoolbox.tokens import checkToken
#     tokens = __import__("metaphor.nntoolbox.toktoolbox.tokens")
#     checkToken = tokens.checkToken
else:
    checkToken = null
#     from metaphor.nntoolbox.toktoolbox.tokens import checkToken

def version():
    """return the version of the module monal
    """
    return __version__

def installFileName(ppath="dist", ext=".tar.gz"):
    """
    """
    cur = "monal-%s%s" % (__version__, ext)
    if len(ppath):
        return os.path.join(ppath, cur)
    return cur


# try:
#     __path__
# except:
#     __path__ = os.path.dirname(__file__)

try:
    # initialisation de la variable __paths__
    from metaphor.nntoolbox.utils import  addpathlist
    __paths__ = addpathlist(__path__[0], "monal", [])
except:
    __paths__ = __path__

__prefix__ = ""

def prefix():
    global __prefix__
    if not __prefix__:
        __prefix__ = getancestor(__path__[0], 'lib', True, True)
    if not __prefix__:
        __prefix__ = getancestor(__path__[0], 'src', True, True)
    return __prefix__
 
__modulepath__ = ""

def path():
    global __modulepath__
    if not __modulepath__:
        __modulepath__ = __path__[0]
    return __modulepath__
 
applibdir = os.path.join(path(), "lcode")
includedir = os.path.join(path(), "include")
parentdir = os.path.dirname(path())

def tokenPath():
    res = os.path.expanduser("~/.tok")
    if not os.path.exists(res):
        os.makedirs(res)
    return res
tokenfile =  os.path.join(tokenPath(), ".tok.tk")   

def getLocalToken():
    if os.path.exists(tokenfile):
        with open(tokenfile, "r") as ff:
            res = ff.read() 
    else:
        res = ""
    return res

def doCheckToken():
    tok = getLocalToken()
    result = tok
    if not tok:
        tok = input("Please enter a valid user token : ")  #.encode('utf_8')
        result = checkToken(tok, "Monal")
        if not result:
            raise Exception("invalid usertoken")
        tokfile = os.path.join(tokenPath(), ".tok.tk")
        with open(tokfile, "w") as ff:
            ff.write(tok)
    else:
        result = checkToken(tok, "Monal")
    return result

# try:
#     res = doCheckToken()
#     expires = res["expires"]
#     expdate = datetime.fromtimestamp(expires).strftime("%A, %B %d, %Y %I:%M:%S")
#     print("\ntoken expires", expdate)
# except Exception as err:
#     print (err)

