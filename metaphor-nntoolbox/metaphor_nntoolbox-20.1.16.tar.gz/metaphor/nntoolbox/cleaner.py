# -*- coding: ISO-8859-1 -*-
#-------------------------------------------------------------------------------
# $Id$
#
# Copyright 2017 Jean-Luc PLOIX
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

import os, sys

def isstr(value):
    if (1 if sys.version_info.major==3 else 0):
        return isinstance(value, str)    
    if (1 if sys.version_info.major==2 else 0):
        return isinstance(value, basestring)
    return False

def modulepath(module):
    if hasattr(module, "__file__"):
        return os.path.dirname(module.__file__)
    if module in sys.modules:
        return modulepath(sys.modules[module])
    try:
        if isstr(module):
            mod = __import__(module)
            return modulepath(mod)
    except: pass
    return ""

def cleanlist(module, filelist, ext="", modpath="", outfile=None):
    if isinstance(module, (tuple, list)):
        return [cleanlist(mod, filelist, ext, modpath, outfile) for mod in module]           
    if isinstance(ext, (list, tuple)):
        return [cleanlist(module, filelist, extval, modpath, outfile) for extval in ext]
    if not modpath:
        modpath = modulepath(module)
    if not os.path.exists(filelist):
        filelist = os.path.join(modpath, filelist)
    if not os.path.exists(filelist):
        return 1
    ppath = os.path.dirname(modpath)
    for val in open(filelist, 'r'):
        if not val.startswith('#'):
            fullval = os.path.join(ppath, val.strip())
            filename = "{0}{1}".format(fullval, ext)
            if os.path.exists(filename):
                os.remove(filename)
                if outfile:
                    outfile.write("removed {0}\n".format(filename))
            elif outfile:
                outfile.write("cannot find {0}\n".format(filename))
    return 0

if __name__ == "__main__":
    argv = sys.argv[1:]
    if not len(argv):
        cleanlist("nntoolbox", "cythonlist.txt", ".c", "", sys.stdout)
    modulename = "nntoolbox" if len(argv) == 0 else argv[0]
    listname = "cythonlist.txt" if len(argv) < 2 else argv[1]
    if len(argv) < 3:
        ext = [".c", "pyx"]
    else:
        ext = argv[2:]
    
    #elif len(argv) >= 3:
    cleanlist(modulename, listname, ext, "", sys.stdout)
        