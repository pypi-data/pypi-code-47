#*- coding: ISO-8859-15 -*-
#-------------------------------------------------------------------------------
#
# $Id: utils.py 4778 2018-05-26 05:20:33Z jeanluc $
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
'''Module monal.util.utils
Utilities for monal
Created on 26 mars 2010

@author: Jean-Luc PLOIX

This file must NOT be cythonize !
'''
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)

import os, sys, shutil, errno, re
import site
from six import PY3, PY2
#from site import USER_BASE, addsitedir #, getuserbase
import warnings
import threading
import distutils.sysconfig as sc
import distutils.ccompiler as dc
import distutils.errors as de
import tempfile
import time
import gc
import platform as pt
from string import ascii_letters, digits
from collections import defaultdict
import concurrent.futures as cf

from metaphor.nntoolbox.constants import USE_PARALLEL_COMPILE
from metaphor.monal import includedir, applibdir
from metaphor.monal import path as mpath
from metaphor.nntoolbox.utils import xfile, maxWorkers
from metaphor.nntoolbox.filetoolbox import backupfile
monalpath = mpath()

proprietaryname = 'LartenNetral_JLP_04_05_47'

PREFIXES = [sys.prefix, sys.exec_prefix]
USER_SITE = None
USER_BASE = None

DEBUG_COMPILE_LIB = 0

def getheaderFile(filename):
    res = ""
    if filename.endswith('.c'):
        res = filename[:-2] + ".h"
    return res

def convertFile2Windows(filename, target=""):
    if not os.path.exists(filename):
        return
    if not target:
        target = filename
    if PY3:
        with open(filename, "r") as f:
            data = f.read()
        with open(target, "w", newline="\r\n") as ff:
            ff.write(data)
    else:
        with open(filename, "rb") as f:
            data = f.read()
        newdata1 = data.replace("\r", "")
        newdata = newdata1.replace("\n", "\r\n")
        if (newdata != data) or (target != filename):
            with open(target, "wb") as f:
                f.write(newdata)

def translateList(source, dico):
    return [dico[val] if val in dico.keys() else val for val in source]

def getChildPath(parent, folder="site-packages"):
    """Look for a 'folder' directory in the children tree of 'parent'.
    return empty string if not found.
    """
    res = ""
    for path, dirs, _ in os.walk(parent):
        if folder in dirs:
            return os.path.join(path, folder)
        else:
            for direc in dirs:
                res = getChildPath(direc, folder)
                if res: break  #return res
    return res

def getappliconfig(appli, origindir=""):
    res = os.path.join(getapplidatabase(appli, origindir), "config.ini")
    return res

def getapplidatabase(appli="", origindir=""):
    if origindir:
        pth = origindir
    else:
        pth = os.path.abspath(sys.prefix)
    if appli:
        pth = os.path.join(pth, appli)
        if not os.path.exists(pth):
            pth = os.path.join(getuserbase(), appli)
        if not os.path.exists(pth):
            ppth, base = os.path.split(__file__)
            while (base.lower() != "lib") and base:
                ppth, base = os.path.split(ppth)
            if base:
                pth = os.path.join(ppth, appli)
    elif not os.path.exists(pth):
        pth = getuserbase()
    return pth

def isVirtual():
    """detect if python run in a virtual environment.
    """
    #import pip
    from sysconfig import get_config_var
    prefix = get_config_var('prefix')
    platbase = get_config_var('platbase')
    #pipfile = pip.__file__
    return (prefix != platbase) or not hasattr(site, 'getuserbase') #or pipfile.startswith(platbase)

def getcurrentsitepackages():
    res = ""
    lst = os.environ['PYTHONPATH'].split(os.pathsep)
    for val in lst:
        if val.endswith('site-packages'):
            res = val
            break
    return res

def getsitebase(targetuser=False):
    pth = getbase(targetuser)
    return getChildPath(pth, "site-packages")

def getbase(targetuser=False):
    if isVirtual() or not targetuser:
        import sys
        return sys.prefix
    if targetuser:
        try:
            return getuserbase()
        except:
            return USER_BASE

def getuserbase():
    """Returns the `user base` directory path.

    The `user base` directory can be used to store data. If the global
    variable ``USER_BASE`` is not initialized yet, this function will also set
    it.
    """
    global USER_BASE
    if USER_BASE is not None:
        return USER_BASE
    if isVirtual():
        USER_BASE = sys.prefix
    else:
        from sysconfig import get_config_var
        USER_BASE = get_config_var('userbase')
    return USER_BASE

def getusersitepackages():
    import os
    """Returns the user-specific site-packages directory path.

    If the global variable ``USER_SITE`` is not initialized yet, this
    function will also set it.
    """
    global USER_SITE
    user_base = getuserbase() # this will also set USER_BASE

    temp = getsitebase(True)
    #os.path.join(os.path.abspath(sys.prefix), 'lib', 'python2.7', 'site-packages')
    #os.path.join(getm onalpath(), 'lib', 'site_packages')
    if os.path.exists(temp):
        USER_SITE = temp
        return temp

    if USER_SITE is not None:
        return USER_SITE

    from sysconfig import get_path
    import os

    if sys.platform == 'darwin':
        from sysconfig import get_config_var
        if get_config_var('PYTHONFRAMEWORK'):
            USER_SITE = get_path('purelib', 'osx_framework_user')
            return USER_SITE

    USER_SITE = get_path('purelib', '%s_user' % os.name)
    return USER_SITE

def getsitepackages():
    """Returns a list containing all global site-packages directories
    (and possibly site-python).

    For each directory present in the global ``PREFIXES``, this function
    will find its `site-packages` subdirectory depending on the system
    environment, and will return a list of full paths.
    """

    sitepackages = []
    seen = set()

    for prefix in PREFIXES:
        if not prefix or prefix in seen:
            continue
        seen.add(prefix)

        if sys.platform in ('os2emx', 'riscos'):
            sitepackages.append(os.path.join(prefix, "Lib", "site-packages"))
        elif os.sep == '/':
            sitepackages.append(os.path.join(prefix, "lib",
                "python" + sys.version[:3 ],"site-packages"))
            sitepackages.append(os.path.join(prefix, "lib", "site-python"))
        else:
            sitepackages.append(prefix)
            sitepackages.append(os.path.join(prefix, "lib", "site-packages"))
        if sys.platform == "darwin":
            # for framework builds *only* we add the standard Apple
            # locations.
            from sysconfig import get_config_var
            framework = get_config_var("PYTHONFRAMEWORK")
            if framework:
                sitepackages.append(
                        os.path.join("/Library", framework,
                            sys.version[:3], "site-packages"))
    return sitepackages

#     try:
#         return getuserbase()
#     except:
#         return USER_BASE
# 
# def getusersitepackages(debugfile=None):
#     import site
#     try:
#         return site.getusersitepackages()
#     except:
#         prefix = site.PREFIXES[0]
#         user_site = site.USER_SITE
#         try:
#             pos = user_site.index('/lib/')
#             suffix = user_site[:pos]
#             res = os.path.join(prefix, suffix)
#             if debugfile:
#                 with open(debugfile, 'a') as ff:
#                     ff.write( "usersitepackages %s\n"% res)
#         except:
#             raise
#     return res
#             
# class ntdefaultDict(dict
#     def __init__(self, default):
#         dict.__init__(self)
#         self._default = default

permittedchar = ascii_letters + digits + "_"
firstchar = ascii_letters #+ "_"

IS_WIN32 = 'win32' in str(sys.platform).lower()
IS_WINDOWS = 'windows' == str(pt.system()).lower()

def dllExtension():
    if is_mac():
        return ".so"
    elif is_linux():
        return ".so"    # ?? dylib  ??
    else:
        return ".dll"  #.dll"

def is_windows():
    return IS_WINDOWS  #pt.system() == "Windows"

def is_mac():
    return pt.system() == "Darwin"

def is_linux():
    return pt.system() == "Linux"
    
def fullSplit(filenamer):
    base, filen = os.path.split(filenamer)
    body, ext = os.path.splitext(filen)
    return base, body, ext

def fileDate(filename):
    filetime = os.path.getmtime(filename)
    return filetime
    
def safemakedirs(path):
    if os.path.exists(path):
        return False
    try: 
        os.makedirs(path)
        res = True
    except:  # FileExistsError: 
        res = False
        return res

def getancestor(mainDir, target, father=False, casesensitive=True):
    """Recherche d'un repertoire ancetre.
    mainDir -> repertoire de départ
    target -> repertoire cible
    father -> si True, retourne le repertoire parent de target
    casesensitive -> si True, la recherche de target est sensible a la casse.
    """
    folder, base = os.path.split(mainDir)
    if not casesensitive:
        target = target.lower()
        base = base.lower()
    if target == base:
        if not father:
            return mainDir
        return folder
    if base:
        return getancestor(folder, target, father, casesensitive)
    return ""

# def getancestor(mainDir, target, father=False):
#     folder, base = os.path.split(mainDir)
#     if (target == base):  #(mainDir == "") or 
#         if not father:
#             return mainDir
#         return folder
#     if base:
#         return getancestor(folder, target, father)
#     return ""

def homedir():
    return os.path.expanduser(chr(126))

def getFile(mainDir, filename="", applis=[]):  #graphmachine.cfg
    if mainDir:
        for path, _, files in os.walk(mainDir):
            if filename in files:
                return os.path.join(path, filename)
    for appli in applis:
        fname = os.path.join(applidata(appli), filename)
        if os.path.exists(fname):
            return fname
        test = os.path.join(getapplibase(appli), filename)
        if os.path.exists(test):
            return test
        st = getancestor(mainDir, "lib")
        if st:
            test = os.path.join(os.path.dirname(st), appli, filename)
            if os.path.exists(test):
                return test
    for valDir in sys.path:
        test = os.path.join(valDir, filename)
        if os.path.exists(test):
            return test
    return ""

def applidata(appliname=""):
    st = os.path.abspath(sys.prefix)
    if appliname:
        return os.path.join(st, appliname)
    else:
        return st

def getapplibase(appli, docreate=False):  #, setinpypath=False):
    """get the application owned directory.
    """
    testdir = os.path.dirname(__file__)
    if testdir:
        st = os.path.join(testdir, '..', '..', '..')
        st = os.path.abspath(st)
    else:
        try:
            #st = getuserbase()
            st = getcurrentsitepackages()
        except:  # Attention MacOs UNIX only
            if is_windows():
                st = os.path.join(os.environ['APPDATA'], appli)
            else:
                st = os.path.join(homedir(), "Applications")
                #"~/.local"
    if os.path.basename(st).lower() == "python":
        st = os.path.dirname(st)
    st = os.path.join(st, appli)
    if docreate and not os.path.exists(st):
        safemakedirs(st)
        #if not os.path.exists(st):
        #    os.m akedirs(st)
#     if setinpypath and not st in sys.path:
#         sys.path.insert(0, st)
    return st

def getapplicfg(appli, model="", ext=".cfg", path="", docreate=True, module=""):
    confdir = getapplibase(appli, docreate)
    target = appli
    if module:
        target = os.path.join(target, module)
    #conffile = lookForFile("%s%s"% (appli, ext), None, target)
    conffile = os.path.join(confdir, "%s%s"% (appli, ext))
    docopy = not os.path.exists(conffile)
    if not model:
        model = "%s%s"%(appli, ext)
    if path:
        model = os.path.join(path, model)
    if (not docopy) and os.path.exists(model):
        t1 = fileDate(model)
        t2 = fileDate(conffile)
        docopy = t2 < t1
    if docopy:
        try:
            shutil.copyfile(model, conffile)
        except: pass
        return conffile    
    if docreate and not os.path.exists(conffile):
        with open(conffile, "rb"):
            pass
    return conffile

def getmodulepath(mod):
    try: 
        return os.path.dirname(sys.modules[mod].__file__)
    except:
        try: return os.path.dirname(__import__(mod).__file__)
        except: return ""
    
configdict = sc.get_config_vars()
#'prefix': 'C:\\Python27', 'Users/jeanluc/anaconda'
#'exec_prefix': 'C:\\Python27', 'Users/jeanluc/anaconda'
#'EXE': '.exe', ['']
#'LIBDEST': 'C:\\Python27\\Lib', ['/Users/jeanluc/anaconda/lib/python2.7']
#'VERSION': '27', ['.so']
#'SO': '.pyd', 
#'BINLIBDEST': 'C:\\Python27\\Lib', ['/Users/jeanluc/anaconda/lib/python2.7']
#'INCLUDEPY': 'C:\\Python27\\include', 
#'BINDIR': 'C:\\Python27'  ['/Users/jeanluc/anaconda/bin']

PREFIX = sc.PREFIX

def get_desktop_path():

    D_paths = list()

    try:

        fs = open(os.sep.join((homedir(), ".config", "user-dirs.dirs")),'r')
        data = fs.read()
        fs.close()
    except:
        data = ""

    D_paths = re.findall(r'XDG_DESKTOP_DIR=\"([^\"]*)', data)

    if len(D_paths) == 1:
        D_path = D_paths[0]
        D_path = re.sub(r'\$HOME', homedir(), D_path)

    else:
        D_path = os.sep.join((homedir(), 'Desktop'))

    if os.path.isdir(D_path):
        return D_path
    else:
        return None
    
def appdatadir(followup="", APPNAME="graphmachine", docreate=False): 
    if is_windows():
        appdata = os.path.join(os.environ['APPDATA'], APPNAME)
    else:
        #app data = (os.path.join(homedir(), "app data", APPNAME)
        appdata = os.path.join(homedir(), "Applications", APPNAME)
    if followup:
        appdata = os.path.join(appdata, followup)
    if docreate and not os.path.exists(appdata):
        safemakedirs(appdata)
    return appdata
        
try:
    pythonlibsdir = os.path.join(configdict['BINDIR'], "libs")
except KeyError:
    pythonlibsdir = configdict['LIBDIR']
appmodeldir = appdatadir("models")
try:
    includepy = configdict['INCLUDEPY']
except KeyError:
    includepy = os.path.abspath(os.path.join(pythonlibsdir, '..', 'include'))
defaultIncludelist = [os.path.join(getmodulepath("numpy"), "core", "include"),
                      includedir, includepy]
#===============================================================================
# MSVCBIN = r"C:\Program Files\Microsoft Visual Studio 10.0\VC\bin"
# MSVCCOMPILER = "cl.exe"
# MINGW32BIN = r"C:\MinGW32-xy\bin"
# MINGW32LIB = r"C:\MinGW32-xy\lib"
# MINGW32COMPILER = "gcc.exe"
# MINGW32ARCHIVER = "ar.exe"
# TCC32BIN = r"C:\tcc32"
# TCC32COMPILER = "tcc.exe"
# CLANGBIN = r"C:\Program Files\LLVM\bin"
# CLANGCOMPILER = "clang-cl.exe"
# CLANGARCHIVER = "clang-ar.exe"
#===============================================================================
compilerdict = {
    "msvc": r"C:\Progra~1\Microsoft Visual Studio 10.0\VC\bin\cl.exe",
    "mingw": r"C:\MinGW\bin\gcc.exe",
    "mingw32": r"C:\MinGW\bin\gcc.exe",
    "tcc": r"C:\tcc32\tcc.exe",
    "tcc64": r"C:\tcc64\tcc.exe",
    "llvm": r"C:\Program Files\LLVM\bin\clang.exe",
    "clang": r"C:\Program Files\LLVM\bin\clang.exe",
    "clang-cl": "C:\Program Files\LLVM\bin\clang-cl.exe"}

compilers = {
    "msvc": r"C:\Progra~1\Microsoft Visual Studio 10.0\VC\bin\cl.exe",
    "mingw": "gcc",
    "mingw32": "gcc",
    "tcc": r"C:\tcc32\tcc.exe",
    "tcc64": r"C:\tcc64\tcc.exe",
    "llvm": "clang",
    "clang": "clang",
    "clang-cl": "clang-cl"}

archiverdict = {
    "msvc": r"C:\MinGW\bin\ar.exe",
    "mingw": r"C:\MinGW\bin\ar.exe",
    "mingw32": r"C:\MinGW\bin\ar.exe",
    "clang": r"C:\Program Files\LLVM\bin\llvm-ar.exe",
    "clang-cl": r"C:\Program Files\LLVM\bin\llvm-ar.exe",
    "llvm": r"C:\Program Files\LLVM\bin\llvm-ar.exe"}

archivers = {
    "msvc": "ar",
    "mingw": "ar",
    "mingw32": "ar",
    "clang": "llvm-ar",
    "clang-cl": "llvm-ar",
    "llvm": "llvm-ar"}

archiverfromcompiler = {
    "msvc": "msvc",
    "mingw": "mingw",
    "mingw32": "mingw",
    "tcc": "mingw",
    "llvm": "llvm",
    "clang": "llvm",
    "clang-cl": "llvm"
    }

archivetemplate = {
    "msvc": "%s.lib",
    "mingw": "lib%s.a",
    "mingw32": "lib%s.a",
    "tcc": "lib%s.a",
    "llvm": "lib%s.a",
    "clang": "lib%s.a",
    "clang-cl": "lib%s.a",
    }

#MINGW32LIB = os.path.dirname(compilerdict["mingw"])
minGw32Compiler = compilerdict["mingw"]  #os.path.join(MINGW32BIN, MINGW32COMPILER)
minGW32Archiver = archiverdict["mingw"]  #os.path.join(MINGW32BIN, MINGW32ARCHIVER)
tcc32Compiler = compilerdict["tcc"]  #os.path.join(TCC32BIN, TCC32COMPILER)
msvcCompiler = compilerdict["msvc"]  #os.path.join(MSVCBIN, MSVCCOMPILER)
llvmCompiler = compilerdict["llvm"]
llvmArchiver = archiverdict["llvm"]

def getLibExt():
    cc = dc.new_compiler(compiler=dc.get_default_compiler())
    return cc.shared_object_filename("")
libext = getLibExt()

monallibs = []

def monallibdate():
    lname = getLibname(output_dir=applibdir)[0]
    if not os.path.exists(lname):
        return 0
    result = fileDate(lname)
    return result

# def monalLibName():
#     return "monal{0}".format(libExtension())

def getLibname(compiler="", output_dir=""):
    compiler = compiler if compiler else dc.get_default_compiler()  #compilerName()
#     if compiler == "msvc":
#         compiler = "mingw32"
    cc = dc.new_compiler(compiler=compiler)
    libname = cc.library_filename("monal", output_dir = output_dir)#applibdir)
    return libname, compiler
    
def getlibinitialized(compiler="", alibname=""):
    global monallibs
    compiler = compiler if compiler else dc.get_default_compiler()  #compilerName()
    if not compiler in monallibs:
        if alibname:
            libname = alibname
        else:
            cc = dc.new_compiler(compiler=compiler)
            libname = cc.library_filename("monal", output_dir = applibdir)
        if os.path.exists(libname):
            monallibs.append(compiler)
    return compiler in monallibs
    
def getsitepython():
    return sys.prefix

def getsitepackage():
    return sc.get_python_lib()

def addpackage(packagename, base="", addtopath=False, nosetup=False):
    base = base if base else getsitepackage()
    lst = packagename.split(".")
    for addin in lst:
        base = os.path.join(base, addin)
        #if not os.path.exists(base):
            #os.ma kedirs(base)
        if safemakedirs(base):
            setupfile = os.path.join(base, "__init__.py") 
            if not nosetup and not os.path.exists(setupfile):
                with open(setupfile, "wb"): pass
        if addtopath:
            from site import addsitedir
            addsitedir(base)
    return base        

def libpathfromcompiler(compiler):
    cmpi = compilerdict[compiler]
    return os.path.join(os.path.dirname( os.path.dirname(cmpi)), "bin)")

def includedirsfromcompiler(compiler):
    if compiler == "msvc":
        folder = configdict['LIBDEST']
        res = [os.path.join(folder, "site-packages", "numpy", "core", "include")]
        if PY2:
            toaddpath = "C:\\Program Files (x86)\\Windows Kits\\10\\Include\\10.0.17134.0\\um"
            res.append(toaddpath)
            toaddpath = "C:\\Program Files (x86)\\Windows Kits\\10\\Include\\10.0.17134.0\\\shared"
            res.append(toaddpath)
        elif PY3:
            pass
            toaddpath = "C:\\Program Files (x86)\\Windows Kits\\10\\Include\\10.0.17134.0\\ucrt"
            res.append(toaddpath)
#             toaddpath = "C:\\Program Files (x86)\\Windows Kits\\10\\Include\\shared"
#             res.append(toaddpath)
        return res
    if compiler in ("mingw", "mingw32"):
        return [os.path.join(configdict['LIBDEST'], "site-packages", "numpy", "core", "include")]
    if compiler in ["llvm", "clang", "clang-cl"]:
        mingwinclude = os.path.join(os.path.dirname(os.path.dirname(minGw32Compiler)), "include")
        return [os.path.join(configdict['LIBDEST'], "site-packages", "numpy", "core", "include"), configdict['INCLUDEPY'], mingwinclude]
    return [os.path.join(configdict['LIBDEST'], "site-packages", "numpy", "core", "include")]

def getIsUptodatelib(libname, sources):
    dateMax = os.path.getmtime(libname) 
    for source in sources:
        if os.path.getmtime(source) > dateMax:
            return False
    return True
                            
def compilemonallib(compiler="", force=True, outputdir="", doprint=False, 
                    freesource=False, debug=0, logfile=None):
    
    #from tempfile import mkdtemp
    rr = None
    source_dir = os.path.join(monalpath, 'lcode', 'code_templates', 'common')
    if not os.path.exists(source_dir):
        return rr
    _, _, files = next(os.walk(source_dir))
    if not len(files):
        return rr
    filescrypt = [fil for fil in files if fil.endswith('.cc')]
    files = [fil for fil in files if fil.endswith('.c')]
    dotempdir = not len(files)
    if dotempdir:
        tempdir = tempfile.mkdtemp() 
        #os.path.join(homedir(), "temp")
        if not os.path.exists(tempdir):
            os.makedirs(tempdir)
        for fil in filescrypt:
            source = os.path.join(source_dir, fil)
            target = os.path.join(tempdir, fil)[:-1]            
            files.append(xfile(source, target, proprietaryname, 0))
        source_dir = tempdir
    outputdir = outputdir if outputdir else applibdir
    libname, compiler = getLibname(compiler, outputdir)
    res = not force and getlibinitialized(compiler=compiler, alibname=libname)
    include_dirs_monal = [sc.get_config_vars()['INCLUDEPY'], os.path.join(monalpath, 'include')]
    excluded = ['readfile', 'dlmdriver']
    if compiler == "msvc":
        extra_preargs = [] 
    else:
        extra_preargs = ['-fPIC']
    if res:
        root, _, files = next(os.walk(include_dirs_monal[1]))
        sources = [os.path.join(root, val) for val in files if val.endswith(".h") and not val[:-2] in excluded]
        root, _, files = next(os.walk(source_dir))
        sources +=[os.path.join(root, val) for val in files if (val.endswith(".c") or val.endswith(".h")) and not val[:-2] in excluded]
        res = getIsUptodatelib(libname, sources)
        res = res and not force
        if not res:
            os.remove(libname)
            if doprint:
                print("{0} removed".format(libname))
    if not res:
        if force and os.path.exists(libname):
            backupfile(libname, backmark="back", replace=True, keepold=True)
            if doprint:
                print("remove -> {0}".format(libname))
        try:
            rr = compile_lib(compiler, libname="monal", source_dir=source_dir, 
                include_dirs=include_dirs_monal, target_dir=outputdir, 
                excluded=excluded, extra_preargs=extra_preargs, doprint=doprint,
                freesource=freesource, debug=debug)
        except Exception as err:
            print("Error in compiling monal lib: %s\n"% (err))
    if logfile:
        with open(logfile, "a") as ff:
            ff.write("Compiled {0}".format(libname))
    if dotempdir:
        shutil.rmtree(tempdir)
    return rr

def compileAsExtension(mainfile, filelist, savedir="", destdir="build", libname="mylib", 
        includedirs=[], package="", compiler="", linker="", archiver="", progress=None, verbose=0):
    """Utilisation des compilateurs abstraits de distutils.ccompiler
    """
     
    if mainfile:
        mainmodule = os.path.splitext(mainfile)[0]
    else:
        mainmodule = os.path.splitext(filelist[-1])[0]
    modulename = mainmodule.lower()
    safemakedirs(destdir)
    #if not os.path.exists(destdir):
    #    os.ma kedirs(destdir)
 
    savedir = savedir if savedir else os.getcwd()
    compiler = compiler if compiler else dc.get_default_compiler()  #compilerName()
    comp = dc.new_compiler(compiler=compiler)
    if verbose >= 3:
        print(("compile with %s"%compiler))
    if not len(includedirs):
        includedirs = defaultIncludelist
    addlist = [val for val in includedirsfromcompiler(compiler) if not val in includedirs]
    includedirs.extend(addlist)
    comp.set_include_dirs(includedirs)
    if not mainfile in filelist:
        filelist = [mainfile] + filelist
    macros = [("_CRT_SECURE_NO_WARNINGS", 1)]
    objlist = comp.compile(filelist, output_dir=destdir, macros=macros) 
    libs = ['python27', 'monal']
    libdirs = ['.', 'build', applibdir, pythonlibsdir]
    # attention dans la liste, monal.applibdir apparait avant pythonlibsdir
    comp.shared_lib_extension = configdict['SO']
    targetfile = modulename + comp.shared_lib_extension
    if compiler == "msvc":
        extra_preargs = []
    else:
        extra_preargs = ['-fPIC']
     
    comp.link_shared_lib(objlist, modulename, libraries=libs, 
        library_dirs=libdirs, export_symbols=None, extra_preargs=extra_preargs)
 
    if package:
        dest = addpackage(package, addtopath=False, nosetup=False)
        destfile = os.path.join(dest, targetfile)
        if os.path.exists(destfile):
            try:
                os.remove(destfile)
            except:
                modulename = os.path.splitext(targetfile)[0]
                if package:
                    modulename = "%s.%s" %(package, modulename)
                for mod in list(sys.modules.keys()):
                    if mod == modulename:
                        lib = sys.modules.pop(mod)
                        del lib
                        gc.collect()
                        break
                os.remove(destfile)
        try:
            comp.move_file(targetfile, destfile)
            if verbose:
                print(("Installation of %s.%s succeded"%(package, targetfile)))
        except OSError:  #WindowsError:
            print(("Installation of %s.%s failed"% (package, targetfile)))
            #raise
                            
def runCompileMonalLib(doprint=False, freesource=False, force=False, 
        logfile=None, debug=0, libpath=""):
    libpath = libpath if libpath else os.path.join(monalpath, 'lcode')
    return compilemonallib(force=force, outputdir=libpath, doprint=doprint, 
            freesource=freesource, logfile=logfile, debug=debug)

def compileAsDll(mainfile, filelist, exports=None, savedir="", 
        destdir="build", includedirs=[], package="", compiler="", 
        linker="", archiver="", progress=None, verbose=0, 
        writer=sys.stdout, forcelib=False, additionallibs=[],
        forcecreate=False): 
    """Utilisation des compilateurs abstraits de distutils.ccompiler
    """ 
    libdir = os.path.join(monalpath, 'lcode')
    libpath, compiler = getLibname(compiler, libdir)
    if forcelib or not os.path.exists(libpath):
        if verbose:
            writer.write("compile monallib in %s\n"% libdir)
        assert compilemonallib(force=True, outputdir=libdir, 
                               doprint=False)
    if mainfile:
        mainmodule = os.path.splitext(mainfile)[0]
    else:
        mainmodule = os.path.splitext(filelist[-1])[0]
    modulename = mainmodule.lower()
    safemakedirs(destdir)
 
    dosavedir = bool(savedir)
    savedir = savedir if savedir else os.getcwd()
    compiler = compiler if compiler else dc.get_default_compiler()  
    comp = dc.new_compiler(compiler=compiler)
    if verbose >= 3:
        if not len(includedirs):
            writer.write("compile with %s\n"%compiler)
            includedirs = defaultIncludelist
    addlist = [val for val in includedirsfromcompiler(compiler) if not val in includedirs]
    includedirs.extend(addlist)
    comp.set_include_dirs(includedirs)
    if not mainfile in filelist:
        filelist.append(mainfile)
    macros = [("_CRT_SECURE_NO_WARNINGS", 1)]
    if is_windows():
        for fil in filelist:
            convertFile2Windows(fil)            
            convertFile2Windows(getheaderFile(fil))
        macros.append(("WIN", 1))
    if compiler == "msvc":
        extra_preargs = []
    else:
        extra_preargs = ['-fPIC']
#     extra_preargs = ['-fPIC', '-D_FILE_OFFSET_BITS=64']
#     comp.shared_lib_extension = configdict['SO']
     
    memout = sys.stdout
    sys.stdout = writer
    myincludedirs = comp.include_dirs
    for val in includedirs:
        if not val in myincludedirs:
            myincludedirs.append(val)
#     print("")
#     for val in filelist:
#         print("to compile", val)
    objlist = comp.compile(filelist, output_dir=destdir, macros=macros, 
        extra_preargs=extra_preargs, include_dirs=myincludedirs) 
    if verbose >= 1:
        for val in objlist:
            print("compile -> {0}".format(val))
    sys.stdout = memout
#     print("applibdir", applibdir) 
    libs = ['monal'] + additionallibs  #+ ['Kernel32']
    if is_windows():
        if PY3:
            libs.append('msvcrt')
            libs.append('msvcmrt')
#            libs.append('msvcrtd')
#            libs.append('python37')
    libdirs = ['.', 'build', applibdir]
#     if PY3:
#         libdirs.append("C:\\ProgramData\\Anaconda3\\pkgs\\python-3.7.0-hea74fb7_0\\libs")
    if modulename.lower().endswith("dll"):
        modulename = modulename[:-3]
    elif modulename.lower().endswith("so"):
        modulename = modulename[:-2]
    elif modulename.lower().endswith("dylib"):
        modulename = modulename[:-5]
    targetfile = modulename + comp.shared_lib_extension 
    initfct = "init%s"% modulename
    if exports is not None:
        exports += [initfct] 
        if not initfct in exports:
            exports.append(initfct)
    extra_preargs = []
    if is_windows():
        extra_preargs.append("/ENTRY:{0}".format("entrypoint"))
        extra_preargs.append("/SUBSYSTEM:WINDOWS")
#         extra_preargs.append("/NODEFAULTLIB:msvcrt.lib") # surtout pas en en python 2.7 
    comp.link_shared_lib(objlist, modulename, libraries=libs, 
                         extra_preargs=extra_preargs,
                         library_dirs=libdirs, export_symbols=exports)
    if is_mac():  
        targetfile = "lib" + targetfile
    elif is_linux():
        targetfile = "lib" + targetfile
    if verbose >= 1:
        print("link -> {0}".format(targetfile))
    if package: 
        dest = package  
        if not os.path.exists(dest):
            comp.mkpath(dest)
        destfile = os.path.join(dest, targetfile)
        if os.path.exists(destfile):
            backupfile(destfile, backmark="back")
        try:
            comp.move_file(targetfile, destfile)
            if verbose:
                writer.write("Installation of %s.%s succeded\n"%(package, 
                                                            targetfile))
        except OSError:  
            writer.write("Installation of %s.%s failed\n"% (package, 
                                                            targetfile))
    elif dosavedir and (savedir != os.getcwd()) and ("/private" + savedir != os.getcwd()):
        destfile = os.path.join(savedir, targetfile)
        backupfile(destfile, backmark="back", replace=True, keepold=True)
        try:
            comp.move_file(targetfile, destfile)
        except Exception as err:  #distutils.errors.DistutilsFileError:
            print(err)
         
    return targetfile
# def compileAsDll(mainfile, filelist, exports=None, savedir="", 
#         destdir="", #"build", 
#         destlibdir="", includedirs=[], package="", compiler="", 
#         linker="", archiver="", progress=None, verbose=0, 
#         writer=sys.stdout, forcelib=False, additionallibs=[],
#         forcecreate=False): 
#     """Utilisation des compilateurs abstraits de distutils.ccompiler
#     """ 
#     libdir = os.path.join(monalpath, 'lcode')
#     libpath, compiler = getLibname(compiler, libdir)
#     if forcelib or not os.path.exists(libpath):
#         if verbose:
#             writer.write("compile monallib in %s\n"% libdir)
#         assert compilemonallib(force=True, outputdir=libdir, 
#                                doprint=False)
#     if mainfile:
#         mainmodule = os.path.splitext(mainfile)[0]
#     else:
#         mainmodule = os.path.splitext(filelist[-1])[0]
#     modulename = mainmodule.lower()
#     safemakedirs(destdir)
# 
#     dosavedir = bool(savedir)
#     savedir = savedir if savedir else os.getcwd()
#     compiler = compiler if compiler else dc.get_default_compiler()  
#     try:
#         comp = dc.new_compiler(compiler=compiler)
#     except:
#         comp = dc.new_compiler(compiler=None)
#     if verbose >= 3:
#         if not len(includedirs):
#             writer.write("compile with %s\n"%compiler)
#             includedirs = defaultIncludelist
#     addlist = [val for val in includedirsfromcompiler(compiler) if not val in includedirs]
#     includedirs.extend(addlist)
#     comp.set_include_dirs(includedirs)
#     if not mainfile in filelist:
#         filelist.append(mainfile)
#     macros = [("_CRT_SECURE_NO_WARNINGS", 1)]
#     if is_windows():
#         for fil in filelist:
#             convertFile2Windows(fil)            
#             convertFile2Windows(getheaderFile(fil))
#         macros.append(("WIN", 1))
#     if compiler == "msvc":
#         extra_preargs = []
#     else:
#         extra_preargs = ['-fPIC']
# #     extra_preargs = ['-fPIC', '-D_FILE_OFFSET_BITS=64']
# #     comp.shared_lib_extension = configdict['SO']
#     
#     memout = sys.stdout
#     sys.stdout = writer
#     myincludedirs = comp.include_dirs
#     for val in includedirs:
#         if not val in myincludedirs:
#             myincludedirs.append(val)
#     objlist = comp.compile(filelist, output_dir=destdir, macros=macros, 
#         extra_preargs=extra_preargs, include_dirs=myincludedirs) 
#     if verbose >= 1:
#         for val in objlist:
#             print("compile -> {0}".format(val))
#     sys.stdout = memout
#     libs = ['monal'] + additionallibs  #+ ['Kernel32']
#     if is_windows():
# #         if PY3:
#         libs.append('msvcrt')
#         libs.append('msvcmrt')
#     libdirs = ['.', applibdir]
# #     libdirs = ['.', 'build', applibdir]
#     if modulename.lower().endswith("dll"):
#         modulename = modulename[:-3]
#     elif modulename.lower().endswith("so"):
#         modulename = modulename[:-2]
#     elif modulename.lower().endswith("dylib"):
#         modulename = modulename[:-5]
#     targetfile = modulename + comp.shared_lib_extension 
#     initfct = "init%s"% modulename
#     if exports is not None:
#         exports += [initfct] 
#         if not initfct in exports:
#             exports.append(initfct)
#     extra_preargs = []
#     if is_windows():
#         extra_preargs.append("/ENTRY:{0}".format("entrypoint"))
#         extra_preargs.append("/SUBSYSTEM:WINDOWS")
# #         extra_preargs.append("/NODEFAULTLIB:msvcrt.lib") # surtout pas en en python 2.7 
#     comp.link_shared_lib(objlist, modulename, libraries=libs, 
#                          extra_preargs=extra_preargs,
#                          library_dirs=libdirs, export_symbols=exports)
#     if is_mac():  
#         targetfile = "lib" + targetfile
#     elif is_linux():
#         targetfile = "lib" + targetfile
#     if verbose >= 1:
#         print("link -> {0}".format(targetfile))
#     if package: 
#         dest = package  
#         if not os.path.exists(dest):
#             comp.mkpath(dest)
#         destfile = os.path.join(dest, targetfile)
#         if os.path.exists(destfile):
#             backupfile(destfile, backmark="back")
# #             destfileback = destfile + "~"
# #             if os.path.exists(destfileback):
# #                 try:
# #                     os.remove(destfileback)
# #                 except: pass
# #             try:
# #                 comp.move_file(destfile, destfileback)
# #             except:
# #                 modulename = os.path.splitext(targetfile)[0]
# #                 if package:
# #                     modulename = "%s.%s" %(package, modulename)
# #                 for mod in list(sys.modules.keys()):
# #                     if mod == modulename:
# #                         lib = sys.modules.pop(mod)
# #                         del lib
# #                         gc.collect()
# #                         break
# #                 os.remove(destfile)
#         try:
#             comp.move_file(targetfile, destfile)
#             if verbose:
#                 writer.write("Installation of %s.%s succeded\n"%(package, 
#                                                             targetfile))
#         except OSError:  
#             writer.write("Installation of %s.%s failed\n"% (package, 
#                                                             targetfile))
#     elif dosavedir and (savedir != os.getcwd()) and ("/private" + savedir != os.getcwd()):
#         destfile = os.path.join(savedir, targetfile)
#         backupfile(destfile, backmark="back", replace=True, keepold=True)
#         try:
#             comp.move_file(targetfile, destfile)
#         except Exception as err:  #distutils.errors.DistutilsFileError:
#             print()
#             print(err)
#         try:
#             for val in additionallibs:
#                 if val.startswith("_shared"):
#                     dllfile = "lib{}.so".format(val)
#                     sublibfile = os.path.join(destdir, dllfile)
#                     destfile = os.path.join(savedir, dllfile)
#                     backupfile(destfile, backmark="back", replace=True, keepold=False) #
# #                     shutil.move(sublibfile, destfile)
#                     comp.move_file(sublibfile, destfile)
#         except Exception as err:  #distutils.errors.DistutilsFileError:
#             print()
#             print(err)
#         
#     return targetfile
                            
def prefixstrlist(pathlist, prefix="", quoted=False):
    #if not prefix:
    #    return pathlist
    if quoted:
        tmp = prefix + '"%s"'
    else:
        tmp = prefix + '%s'
    return [tmp % val for val in pathlist]

def objCompileList(filen, destdir="", includedirs=[], compiler="msvc", warning=True):
    corefile = os.path.splitext(os.path.basename(filen))[0]
    if compiler == "msvc":
        otarget = os.path.join(destdir, "%s.obj"%corefile)
    else:
        otarget = os.path.join(destdir, "%s.o"%corefile)
    st = sc.get_config_vars()['INCLUDEPY']
    if not (st in includedirs):
        includedirs = [st] + includedirs
    inclist = prefixstrlist(includedirs, "-I")
    #if compiler == "msvc":
    #    lst = ["-mdll", "-O", "-Wall"] + inclist + ["-c", "%s.c"%corefile, "-o", otarget]  #
    #else:
    #    lst =          ["-O", "-Wall"] + inclist + ["-c", "%s.c"%corefile, "-o", otarget] 

    lst = []
    if compiler == "msvc":
        lst = ["-mdll"]
    lst.append("-O")
    lst.append("-g")
    if warning:
        lst.append("-Wall")
    lst.extend(inclist)
    lst.extend(("-c", "%s.c"%corefile, "-o", otarget))
    
    return lst

def objCompileCommand(filen, compiler=minGw32Compiler, destdir="", includedirs=[]):
    return " ".join(objCompileList(filen, compiler, destdir, includedirs))
    
# monkey-patch for parallel compilation
# def parallelCCompile(self, sources, output_dir=None, macros=None, include_dirs=None, debug=0, extra_preargs=None, extra_postargs=None, depends=None):
#     # those lines are copied from distutils.ccompiler.CCompiler directly
#     macros, objects, extra_postargs, pp_opts, build = self._setup_compile(output_dir, macros, include_dirs, sources, depends, extra_postargs)
#     cc_args = self._get_cc_args(pp_opts, debug, extra_preargs)
#     # parallel code
#     N=2 # number of parallel compilations
#     import multiprocessing.pool
#     def _single_compile(obj):
#         try: src, ext = build[obj]
#         except KeyError: return
#         self._compile(obj, src, ext, cc_args, extra_postargs, pp_opts)
#     # convert to list, imap is evaluated on-demand
#     list(multiprocessing.pool.ThreadPool(N).imap(_single_compile,objects))
#     return objects
# # to use:
# #import distutils.ccompiler
# #distutils.ccompiler.CCompiler.compile=parallelCCompile

def compile_lib(compiler="default", libname="", source_dir=".", 
        include_dirs=[], target_dir="", excluded=[], extra_preargs=[], 
        doprint=False, freesource=False, debug=0):
    """Compile common C files in library
    parameters:
        default -> if True, only the default compiler is used.
            else all available compiler will be tried.
        libname -> name of the library, not a filename.
        source_dir -> directory of the C files. All C files in this directory 
            will be compiled and included in the static library.
        include_dirs -> list of directories for satic libs gathering
        target_dir -> directoty to place the output lib. If empty, lib will be placed in python libs directory
        excluded -> list of c files (extension less) to to excluded out of the computed library 
        doprint -> print the result.
    """
    default = compiler == "default"
    if default:
        complist = [dc.get_default_compiler()]
    elif not compiler:
        complist = list(dc.compiler_class.keys())
    else:
        complist = [compiler]
    if len(complist)==1:
        res = create_lib(complist[0], libname, source_dir=source_dir, 
            target_dir=target_dir, include_dirs=include_dirs, excluded=excluded, 
            extra_preargs=extra_preargs, doprint=doprint, freesource=freesource, 
            debug=debug)       
    else:
        res = True
        for comp in complist:
            blocksize = 0
            res = res and create_lib(comp, libname, source_dir=source_dir, 
                target_dir=target_dir, include_dirs=include_dirs, 
                excluded=excluded, blocksize=blocksize,
                doprint=doprint, freesource=freesource, debug=debug)
    return res


# def sub_create_lib(index, cc, temp, step, originsources, libname, target_dir,
#                    macros, include_dirs, extra_preargs):
# #     cc = dc.new_compiler(compiler=comp)
# #     cc.mkpath(target_dir)
#     start = step * index
#     sources = originsources[start: start+step]
# #    temp = tempfile.mkdtemp(prefix="$%s"% libname)  # temp is obj file dir
#     if PY3:
#         os.makedirs(temp, exist_ok=True)  # ici
#     else:
#         if os.path.exists(temp):
#             shutil.rmtree(temp)
#         os.makedirs(temp)  # ici
#     #if cutbool:
#     curlibname = '{0}_{1}'.format(libname, index)
#     #else:
#     #    curlibname = libname
#     libfilename = os.path.join(target_dir, '{0}.a'.format(curlibname))
# #    result.append(curlibname)
#     if os.path.exists(libfilename):
#         os.remove(libfilename)
#     objlist = cc.compile(sources, output_dir=temp, macros=macros, 
#         include_dirs=include_dirs, extra_preargs=extra_preargs)
#     cc.create_static_lib(objlist, curlibname, target_dir)
# #     if pr ogress is not None:
# #         prog ress(start + len(sources))
#     res = os.path.exists(libfilename)
# #    shutil.rmtree(temp) 
#     return index, res, curlibname, len(sources)

# def cr eate_lib(compiler, libname, source_dir="", target_dir="", include_dirs=[], 
#                excluded=[], extra_preargs=[], doprint=False, freesource=False,
#                blocksize=0, prog ress=None, maxworkers=-2, 
#                doparallel = False):
#     """Creation of a static library.
#     parameters:
#         compiler -> compiler name. Must be in the list of available compilers.
#         libname -> name of the library. Not file name.
#         source_dir -> directory of C sources files.
#         target_dir-> directory of resulted library file. 
#             If empty, library will be installed in Python libs folder. 
#         excluded -> list of excluded files. '.c' extension will be added if necessary.
#         doprint -> print results.
#     """
#     res = False 
#     result = []
#     cur = os.getcwd()
#     for i, val in enumerate(excluded):
#         if not val.lower().endswith(".c"):
#             excluded[i] = val + ".c"
#     if not target_dir:
#         target_dir = os.path.join(sys.prefix, "libs")
#     os.chdir(source_dir)
#     if not len(include_dirs):
#         incpy = sc.get_config_vars()['INCLUDEPY']
#         include_dirs = [incpy, os.path.join(source_dir, 'include')]
#     comp = compiler if compiler else dc.get_default_compiler()  #compilerName()
# #     cc = dc.new_compiler(compiler=comp)
# #     cc.mkpath(target_dir)
#     macros = [("_CRT_SECURE_NO_WARNINGS", 1)]
#     if is_windows():
#         macros.append(("WIN", 1))
#     
#     
#     root, _, files = next(os.walk(source_dir))
#     originsources = [val for val in files if val.endswith(".c") and not val in excluded]
#     cutbool = 0 < blocksize < len(originsources)
#     do_parallel = cutbool
#     if not cutbool:
#         blocksize = len(originsources)
#     res = True
#     if not blocksize:
#         nboucle = 1
#     else:
#         nboucle = len(originsources) // blocksize
#         rel = len(originsources) % blocksize
#         if not rel:
#             nboucle += 1
#     doparallel = doparallel and (nboucle > 1)
#     
#     cc = dc.new_compiler(compiler=comp)
#     cc.mkpath(target_dir)
#     if pro gress is not None:
#         pro gress(0)
#     if doparallel:
#         max_workers = maxWorkers(maxworkers) 
#         cumul = 0
#         count = 0
#         with cf.ProcessPoolExecutor(max_workers=max_workers) as executor:
#             try:
#                 temp = tempfile.mkdtemp(prefix="$%s"% libname)  # temp is obj file dir
#                 futures = [executor.submit(sub_create_lib, index, cc, 
#                     blocksize, originsources, libname, target_dir, macros, 
#                     include_dirs, extra_preargs) for index in range(nboucle)]
#                 for future in cf.as_completed(futures):
#                     index, resl, curlibname, lensource = future.result()
#                     res = res and resl
#                     count = cumul*blocksize + lensource
#                     if pro gress is not None:
#                         pro gress(count)
#                     cumul += 1
#                     
#             except Exception as err:
# #                 writer.write(err.message)
# #                 writer.write("\n")
#                 if pr ogress:
#                     pr ogress(count)
#                 for future in cf.as_completed(futures):
#                     future.cancel()
#             
#         
#         
# #         for ind in range(nboucle):
# #             start
#     else:
#         start = 0
#         index = 0
#         sources = originsources[start: start+blocksize]
#         #while len(sources):
#         for index in range(nboucle):
#             
#             try:
#                 temp = tempfile.mkdtemp(prefix="$%s"% libname)  # temp is obj file dir
#                 start = index * blocksize
#                 indexl, resl, curlibname, lensource = sub_create_lib(index, cc, 
#                         temp, blocksize, originsources, libname, target_dir, macros, 
#                         include_dirs, extra_preargs )
#                 res = res and resl
#                 result.append(curlibname)
# #                 temp = tempfile.mkdtemp(prefix="$%s"% libname)  # temp is obj file dir
# #                 if PY3:
# #                     os.makedirs(temp, exist_ok=True)  # ici
# #                 else:
# #                     if os.path.exists(temp):
# #                         shutil.rmtree(temp)
# #                     os.makedirs(temp)  # ici
# #                 if cutbool:
# #                     curlibname = '{0}_{1}'.format(libname, index)
# #                 else:
# #                     curlibname = libname
# #                 libfilename = os.path.join(target_dir, '{0}.a'.format(curlibname))
# #                 result.append(curlibname)
# #                 if os.path.exists(libfilename):
# #                     os.remove(libfilename)
# #                 objlist = cc.compile(sources, output_dir=temp, macros=macros, 
# #                     include_dirs=include_dirs, extra_preargs=extra_preargs)
# #                 cc.create_static_lib(objlist, curlibname, target_dir)
#                 if pro gress is not None:
#                     progr ess(start + lensource)
# #                 res = res and os.path.exists(libfilename)
# #                 index +=1
# #                 start += blocksize
# #                 sources = originsources[start: start+blocksize]
#     #             if doprint:
#     #                 print(("compiler %s succeded"% comp))
#             except de.CompileError as err:
#                 print(("compiler %s failed"% comp))
#                 print(err)
#             finally:
#                 try:
#                     shutil.rmtree(temp)  # delete directory
#                 except OSError as exc:
#                     if exc.errno != errno.ENOENT:  # ENOENT - no such file or directory
#                         raise  # re-raise exception
#     if freesource:
#         try:
#             for source in originsources:
#                 os.remove(source)
#         except:
#             if doprint:
#                 print("erase %s failed"% source)
#     os.chdir(cur)
#     return result

# def create _lib_loc(index, cc, libname, sources, target_dir, sub_lib_dir,
#         include_dirs, macros, extra_preargs, no0=False, doprint=False): #temp, 
#     try:  
#         temp = tempfile.mkdtemp(prefix="$%s"% libname)  # temp is obj file dir          
#         curlibname = ""
#         lensources = len(sources)
#         if (index > 0) or not(index or no0):
#             curlibname = '{0}_{1:003}'.format(libname, index)
#         else:
#             curlibname = libname        
#         # libfilename = os.path.join(target_dir, 'lib{0}.a'.format(curlibname))
#         libfilename = cc.library_filename(curlibname, output_dir=target_dir)
#         if os.path.exists(libfilename):
#             os.remove(libfilename)
#         objlist = cc.compile(sources, output_dir=temp, macros=macros, 
#             include_dirs=include_dirs, extra_preargs=extra_preargs)
#         if doprint:
#             for obj in objlist:
#                 ofile = os.path.basename(obj)
#                 print("compile -> {0}".format(ofile))
#         cc.create_static_lib(objlist, curlibname, target_dir)
#         if doprint:
#             print("link -> {0}".format(os.path.basename(libfilename)))
#     except de.CompileError as err:
#         print("compilation failed")
#         print(err)
#     finally:
#         shutil.rmtree(temp) 
#     res = os.path.exists(libfilename)
#     ll = lensources
#     return res, curlibname, ll

def create_lib_loc(index, cc, libname, sources, target_dir, sub_lib_dir, 
        include_dirs, macros, extra_preargs, no0=False, doprint=False): 
    try:            
        temp = tempfile.mkdtemp(prefix="${0}".format(libname))
#         temp = tempfile.mkdtemp(prefix="${0}{1}".format(index, libname))
        curlibname = ""
        lensources = len(sources)
        if (index > 0) or not(index or no0):
            curlibname = '{0}_{1:003}'.format(libname, index)
        else:
            curlibname = libname        
#         if sub_lib_dir: 
#             libfilename = cc.library_filename(curlibname, lib_type='shared',
#                 output_dir=sub_lib_dir)
#         else:
        objlist = cc.compile(sources, output_dir=temp, macros=macros, 
            include_dirs=include_dirs, extra_preargs=extra_preargs)
        if doprint:
            for obj in objlist:
                ofile = os.path.basename(obj)
                print("compile -> {0}".format(ofile))
#         if sub_lib_dir: 
#             output_libname = cc.library_filename(curlibname, lib_type='shared', 
#                 output_dir=sub_lib_dir)
#             if os.path.exists(output_libname):
#                 os.remove(output_libname)        
#             cc.link_shared_lib(objlist, curlibname, output_dir=sub_lib_dir)  #, libraries=None, library_dirs=None, runtime_library_dirs=None, export_symbols=None, debug=0, extra_preargs=None, extra_postargs=None, build_temp=None, target_lang=None])
#         else:
        libfilename = cc.library_filename(curlibname, lib_type='static',
            output_dir=target_dir)
        if os.path.exists(libfilename):
            os.remove(libfilename)
        cc.create_static_lib(objlist, curlibname, target_dir)
        
        if doprint:
            print("link -> {0}".format(os.path.basename(libfilename)))
    except de.CompileError as err:
        print("compilation failed")
        print(err)
    finally:
        shutil.rmtree(temp)
#     if sub_lib_dir:
#         res = os.path.exists(output_libname)        
#     else:
    res = os.path.exists(libfilename)
    return res, curlibname, lensources

def create_lib(compiler, libname, source_dir="", target_dir="", sub_lib_dir="",
            include_dirs=[], excluded=[], extra_preargs=[], doprint=False, 
            freesource=False, blocksize=0, progress=None, maxworkers=-2, 
            debug=0):
    """Creation of a static library.
    parameters:
        compiler -> compiler name. Must be in the list of available compilers.
        libname -> name of the library. Not file name.
        source_dir -> directory of C sources files.
        target_dir-> directory of resulted library file. 
            If empty, library will be installed in Python libs folder. 
        sub_lib_dir -> directory of sub libraries
        excluded -> list of excluded files. '.c' extension will be added if necessary.
        doprint -> print results.
    """
    result = []
    cur = os.getcwd()
    for i, val in enumerate(excluded):
        if not val.lower().endswith(".c"):
            excluded[i] = val + ".c"
    if not target_dir:
        target_dir = os.path.join(sys.prefix, "libs")
    os.chdir(source_dir)
    if not len(include_dirs):
        incpy = sc.get_config_vars()['INCLUDEPY']
        include_dirs = [incpy, os.path.join(source_dir, 'include')]
    macros = [("_CRT_SECURE_NO_WARNINGS", 1)]
    if is_windows():
        macros.append(("WIN", 1)) 
    root, _, files = next(os.walk(source_dir))
    originsources = [val for val in files if val.endswith(".c") and not val in excluded]
    originsources.sort()
    cutbool = 0 < blocksize < len(originsources)
    if not cutbool:
        blocksize = len(originsources)
        nboucle = 1
    else:
        if not blocksize:
            nboucle = 1
        else:
            nboucle = len(originsources) // blocksize + int(bool(len(originsources) % blocksize))
    doparallel = USE_PARALLEL_COMPILE and (nboucle > 1)
    res = True
    if progress is not None:
        progress(0)
    comp = compiler if compiler else None  #dc.get_default_compiler()  #compilerName()
    try:
        cc = dc.new_compiler(compiler=comp)
    except  de.DistutilsPlatformError:
        cc = dc.new_compiler(compiler=None)
    cc.mkpath(target_dir)
    
    sourcelst = [originsources[istart:istart + blocksize] \
                 for istart in range(0, len(originsources), blocksize)]
    # sourcelst est la liste des blocs de source a compiler
    cumul = 0
    no0 = len(sourcelst) == 1
    if doparallel:
        max_workers = maxWorkers(maxworkers) 
        with cf.ProcessPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(create_lib_loc, index, cc, 
                libname, originloc, target_dir, sub_lib_dir, include_dirs, 
                macros, extra_preargs, no0, doprint) 
                for index, originloc in enumerate(sourcelst)]
            for future in cf.as_completed(futures):
                resloc, curlibname, lensources = future.result()
                cumul += lensources
                res = res and resloc
                result.append(curlibname)
#                 if DEBUG_COMPILE_LIB or debug:    
#                     print("library", curlibname)
#                     for val in originloc:
#                         print("\t{0}".format(val))
                if progress:  # is not None:
                    progress(cumul)
    else:
        for index, originloc in enumerate(sourcelst):
            resloc, curlibname, lensources = create_lib_loc(index, cc, 
                libname, originloc, target_dir, sub_lib_dir, include_dirs, 
                macros, extra_preargs, no0, doprint)
            cumul += lensources
            res = res and resloc
            result.append(curlibname)
#             if DEBUG_COMPILE_LIB or debug:    
#                 print("library", curlibname)
#                 for val in originloc:
#                     print("\t{0}".format(val))
            if progress:
                progress(cumul)
    if progress:
        progress.ends()
        
    if freesource:
        for source in originsources:
            try:
                os.remove(source)
                if doprint:
                    print("erasing {0}".format(source))
            except:
                if doprint:
                    print("erase failed {0}".format(source))
    os.chdir(cur)
    return result

# def create_lib(compiler, libname, source_dir="", target_dir="", include_dirs=[], 
#                excluded=[], extra_preargs=[], doprint=False, freesource=False,
#                blocksize=0, progress=None, maxworkers=-2, debug=0):
#     """Creation of a static library.
#     parameters:
#         compiler -> compiler name. Must be in the list of available compilers.
#         libname -> name of the library. Not file name.
#         source_dir -> directory of C sources files.
#         target_dir-> directory of resulted library file. 
#             If empty, library will be installed in Python libs folder. 
#         excluded -> list of excluded files. '.c' extension will be added if necessary.
#         doprint -> print results.
#     """
# 
# 
#     doparallel = USE_PARALLEL_COMPILE
# #     print()
# #     print("doparallel", doparallel)
#     result = []
#     cur = os.getcwd()
#     for i, val in enumerate(excluded):
#         if not val.lower().endswith(".c"):
#             excluded[i] = val + ".c"
#     if not target_dir:
#         target_dir = os.path.join(sys.prefix, "libs")
#     os.chdir(source_dir)
#     if not len(include_dirs):
#         incpy = sc.get_config_vars()['INCLUDEPY']
#         include_dirs = [incpy, os.path.join(source_dir, 'include')]
#     comp = compiler if compiler else dc.get_default_compiler()  #compilerName()
#     macros = [("_CRT_SECURE_NO_WARNINGS", 1)]
#     if is_windows():
#         macros.append(("WIN", 1)) 
#     root, _, files = next(os.walk(source_dir))
#     originsources = [val for val in files if val.endswith(".c") and not val in excluded]
#     originsources.sort()
#     cutbool = 0 < blocksize < len(originsources)
#     if not cutbool:
#         blocksize = len(originsources)
#         nboucle = 1
#     else:
#         if not blocksize:
#             nboucle = 1
#         else:
#             nboucle = len(originsources) // blocksize + int(bool(len(originsources) % blocksize))
#     doparallel = doparallel and (nboucle > 1)
#     res = True
# #    temp = tempfile.mkdtemp(prefix="$%s"% libname)  # temp is obj file dir
#     if progress is not None:
#         progress(0)
#     cc = dc.new_compiler(compiler=comp)
#     cc.mkpath(target_dir)
#     
#     cumul = 0
# #     sourcelst = []
# #     start = 0
# #     while 1:
# #         start1 = start + blocksize
# #         loclst = originsources[start: start1]
# #         if not len(loclst):
# #             break
# #         sourcelst.append(loclst)
# #         start = start1
#     sourcelst = [originsources[istart:istart + blocksize] \
#                  for istart in range(0, len(originsources), blocksize)]
#     no0 = len(sourcelst) == 1
#     cumul = 0
#     if doparallel:
#         max_workers = maxWorkers(maxworkers) 
# #         cumul = 0
#         with cf.ProcessPoolExecutor(max_workers=max_workers) as executor:
#             futures = [executor.submit(create _lib_loc, index, cc, 
#                 libname, originloc, target_dir, None, include_dirs, macros, 
#                 extra_preargs, no0, doprint) 
#                 for index, originloc in enumerate(sourcelst)]
#             for future in cf.as_completed(futures):
#                 resloc, curlibname, lensources = future.result()
#                 res = res and resloc
#                 cumul += lensources
#                 res = res and resloc
#                 if progress is not None:
#                     progress(cumul)
#  
#     else:
#         for index, originloc in enumerate(sourcelst):
#             resloc, curlibname, lensources = create _lib_loc(index, cc, 
#                 libname, originloc, target_dir, None, include_dirs, macros, 
#                 extra_preargs, no0, doprint)
#             cumul += lensources
#             if progress:
#                 progress(cumul)
#             res = res and resloc
#             result.append(curlibname)
#             if DEBUG_COMPILE_LIB or debug:    
#                 print("library", curlibname)
#                 for val in originloc:
#                     print("\t{0}".format(val))
#     if progress:
#         progress.ends()
#         
# #    shutil.rmtree(temp)  # delete directory
#     if freesource:
#         try:
#             for source in originsources:
#                 if doprint:
#                     print("erasing {0}".firmat(source))
#                 os.remove(source)
#         except:
#             if doprint:
#                 print("erase %s failed {0}".format(source))
#     os.chdir(cur)
#     return result

def getmodulename(modulecore, ext="", doshort=False):
    if doshort:
        if modulecore.startswith("lib"):
            modulecore = modulecore[3:]
    if ext == "":
        if is_mac() and not doshort and not modulecore.startswith("lib"):
            return "lib%s"% modulecore
        return modulecore
    if is_mac() and not doshort and not modulecore.startswith("lib"):
        return "lib%s.%s"% (modulecore, ext)
    return "%s.%s"% (modulecore, ext)

# def removemodule(modname, modpath="", backup=True):
#     """Efface un module python du repertoire designe
#     """
#     if not modpath:
#         modpath, modname = os.path.split(modname)
#     fullmod = os.path.join(modpath, modname)
#     modname = os.path.splitext(modname)[0]
#     initpy = os.path.join(modpath, "__init__.py")
#     if os.path.exists(initpy):
#         lst = []
#         OK = False
#         with open(initpy, "rb") as ff:
#             lst = ff.readlines()
#         for i, line in enumerate(lst):
#             if line.strip() == "import %s"%modname:
#                 lst.pop(i)
#                 OK = True
#                 break
#         if OK:
#             with open(initpy, "wb") as ff:
#                 for line in lst:
#                     ff.write(line)
#     if os.path.exists(fullmod):
#         backup, _ = os.path.splitext(fullmod)
#         backup += ".bak"
#         backup = backup.lower()
#         if os.path.exists(backup):
#             os.remove(backup)
#         os.rename(fullmod, backup)

def nonASCIICharsConvert(Chaine):
    lst = []
    for c in Chaine:
        nn = ord(c)
        if 0 < nn < 128:
            lst.append(c)
        else:
            st = hex(nn)
            lst.append('\\%s'%st[1:])
    return "".join(lst)

AccentDict = defaultdict(lambda:u'', {
        u'é': u'e', 
        u'è': u'e', 
        u'ê': u'e', 
        u'ë': u'e',
        u'à': u'a', 
        u'â': u'a', 
        u'ä': u'a',
        u'î': u'i', 
        u'ï': u'i',
        u'ù': u'u', 
        u'û': u'u', 
        u'ç': u'c',})        

StrAccentDict = defaultdict(lambda:'', {
        'é': 'e', 
        'è': 'e', 
        'ê': 'e', 
        'ë': 'e',
        'à': 'a', 
        'â': 'a', 
        'ä': 'a',
        'ç': 'c',
        'î': 'i', 
        'ï': 'i',
        'û': 'u',
        'ù': 'u', 
})


def unicodeRemoveAccent(inp, accept=permittedchar, replaceDict={}):
    if inp in accept:
        return inp
    if inp in replaceDict:
        return replaceDict[inp]
    return u''
    
def removeAccent(inp, accept=permittedchar):  #uni=False, 
    '''inp is a string or unicode char 
    '''
    if inp in accept:
        return inp

    if PY3:
        if inp in ['é', 'è', 'ê', 'ë']:
            return 'e'
        elif inp in ['à', 'â', 'ä']:
            return 'a'
        elif inp == 'ç':
            return 'c'
        elif inp in ['î', 'ï']:
            return 'i'
        elif inp in ['ù', 'û']:
            return 'u'
    if inp in [u'é', u'è', u'ê', u'ë']:
        return u'e'
    elif inp in [u'à', u'â', u'ä']:
        return u'a'
    elif inp == u'ç':
        return u'c'
    elif inp in [u'î', u'ï']:
        return u'i'
    elif inp in [u'ù', u'û']:
        return u'u'
    else:
        return '_'
#     else:
#         if inp in [u'é', u'è', u'ê', u'ë']:
#             return u'e'
#         elif inp in [u'à', u'â', u'ä']:
#             return u'a'
#         elif inp == u'ç':
#             return u'c'
#         elif inp in [u'î', u'ï']:
#             return u'i'
#         elif inp in [u'ù', u'û']:
#             return u'u'
#         elif category(inp)[0] not in [u"L", u"N", u"S"]:
#             return u'_'
#         else:
#             return u''

def CCharOnlys(Chaine, nostartint=False, Fortran=False, extended=False, hyphen=False):
    global permittedchar
    if not len(Chaine):
        return ""
    #uni = (sys.version_info < (3,)) and isinstance(Chaine, str)
#     accept = permittedchar
    if hyphen:
        permittedchar += '-'
    lst = [removeAccent(c, accept=permittedchar) for c in Chaine]
    if lst[0].isdigit():
        if extended:
#             if uni:
#                 lst.insert(0, u'_')
#             else:
            lst.insert(0, '_')
        elif nostartint:
            lst[0] = '_'
    if Fortran:
        for i, c in enumerate(lst):
            if c == u'_':
                lst[i] = u'$'
            elif c == '_':
                lst[i] = '$'
    res = "".join(lst)
    return res

def CPrefix(Name, Substitute="", Maj=False):
    Result = CCharOnlys(Name).strip().lower()
    if not Result:
        Result = Substitute.lower()
    if Maj:
        Result = Result.upper()
    return Result

##--- NML Converter -------------------------------------------------------
# def ChildElementList(elmt):
# #     try:
# #         return list(elmt.iter())
# #     except:
#     return elmt.getchildren()

def cleanXML(source, nodeToClean=[]):
    """Remove all Text nodes between Element nodes.
    owner is the elements parent
    source must be an Element
    """
    from xml.dom.minidom import Element, Text
    toremove = []
    for child in source.childNodes:
        if isinstance(child, Text):
            toremove.append(child)
        elif isinstance(child, Element):
            if child.tagName in nodeToClean:
                cleanXML(child, nodeToClean)
    for child in toremove:
        source.removeChild(child)


##--- Doc generator -------------------------------------------------------
def Module_doc( package, alls ):
    """Module documentation generator.
    """
    lst = [package.__name__]
    for val in alls:
        if not val.startswith("_"):
            attr = getattr(package, val)
            if hasattr(attr, "__name__"):
                lst.append("\n" + attr.__name__ + ":")
                if attr.__doc__:
                    lst.append("    " + attr.__doc__)
    st = "\n".join(lst)
    return st

class Class_doc( object ):
    """Class documentation generator.
    Class_doc is initiated with a class doc header as parameter, 
    and must be affected to the __doc__ address. It then works as a 
    descriptor.
    When the <class>.__doc__ is called, it return the addition of the original 
    __doc__ and all the public attribute docstrings."""
    def __init__(self, initdoc):
        self.initdoc = initdoc
        
    def _get_values(self, obj):
        def _print_value(key):
            if key.startswith('_'):
                return ''
            value = getattr(obj, key)
            if hasattr(value, "__doc__") and not isinstance(value, (int, float, bool, str)):
                doc = value.__doc__
            elif not hasattr(value, 'im_func'):
                doc = type(value).__name__
            elif value.__doc__ is None:
                doc = 'no docstring'
            else:
                doc = value.__doc__
            return '    %s: %s'% (key, doc)
        res = [_print_value(el) for el in dir(obj)]
        return [el for el in res if el]
    
    def __get__(self, instance, klass=None):
        target = instance or klass
        if not target:
            return ""
        lst = self.initdoc.splitlines()
        lst.extend(self._get_values(target))
        if klass is not None:    
            lst.insert(0, "Class: %s"% klass.__name__)
        return '\n'.join(lst)            
                
#--- Decorators ----------------------------------------------------------------
# def timeit(method):
# 
#     def timed(*args, **kw):
#         ts = time.time()
#         result = method(*args, **kw)
#         te = time.time()
# 
#         print '%r (%r, %r) %2.2f sec' % \
#               (method.__name__, args, kw, te-ts)
#         return result
# 
#     return timed

def setInterval(interval):
    """Decorator that launch a function every 'interval' seconds.
    launch with:
        actor = function()
    stop with:
        acrtor.set()
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop(): # executed in another thread
                while not stopped.wait(interval): # until stopped
                    function(*args, **kwargs)

            t = threading.Thread(target=loop)
            t.daemon = True # stop if the program exits
            t.start()
            return stopped
        return wrapper
    return decorator


class memoized(object):
    """Decorator that caches a function's return value each time it is called.
If called later with the same arguments, the cached value is returned, and
not re-evaluated."""
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            self.cache[args] = value = self.func(*args)
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)
    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__
      
def deprecated(substitute=""):
    '''This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used. If a substitute is furnished
    it will be proposed'''
    def wrap(func):
#        @functools.wraps(func)  supprimé pour utiliser Sphinx
        def new_func(*args, **kwargs):
            if substitute:
                st = "Call to deprecated function %s. Please use %s" %(func.__name__, substitute)
            else:
                st = "Call to deprecated function %s." %(func.__name__)
            warnings.warn_explicit(st,
                category=DeprecationWarning,
                filename=func.__code__.co_filename,
                lineno=func.__code__.co_firstlineno + 1)
            return func(*args, **kwargs) 
        new_func.__doc__ = func.__doc__
        new_func.__name__ = func.__name__
        return new_func        
    return wrap

def timeit(method):
    """Decorator that print the execution time of a mathod
    """
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print(('%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)))
        return result

    return timed

class Counter(object):
    """Decorator that keeps track of the number of times a function is called."""

    __instances = {}

    def __init__(self, f):
        self.__f = f
        self.__numcalls = 0
        Counter.__instances[f] = self
        self.__name__ = f.__name__

    def __call__(self, *args, **kwargs):
        self.__numcalls += 1
        return self.__f(*args, **kwargs)

    def reinit(self):
        """Clear the track memory"""
        self.__numcalls = 0
        
    def count(self):
        "Return the number of times the function f was called."
        return Counter.__instances[self.__f].__numcalls
  
    def name(self):
        return self.__name__#Counter.__instances[self.__f].__name__

    @staticmethod
    def counts():
        "Return a dict of {function: # of calls} for all registered functions."
        return dict([(f.__name__, Counter.__instances[f].__numcalls) for f in Counter.__instances])

#--- Divers --------------------------------------------------------------------

def Activ2Name(activ):
    if isinstance(activ, str): 
        return activ
    return ""
    #activName[activ]

def modelName(modeldata):
    if modeldata["name"] == "%AUTO%": return "Model-{0}-{1}-{2}".format(modeldata["input"], modeldata["hidden"], modeldata["output"])
    return modeldata["name"]

def IndexInActivList(activlist, activindex):
    for i, val in enumerate(activlist):
        if val == activindex: return i
    return -1

#--- Traitement des DOM (XML) --------------------------------------------------

def removePI(dom, target, datastart):
    """Suppression d'une commande Processing Instruction dans un QDomDocument"""
    child = dom.firstChild()
    while not child.isNull():
        nextt = child.nextSibling()
        if child.isProcessingInstruction():
            pi = child.toProcessingInstruction()
            if ((pi.target() == target) and 
                (str(pi.data()).startswith(datastart))):
                dom.removeChild(child)
        child = nextt 

def getFirstNodeOfTag(root, tag):
    if isinstance(tag, str):
        return getFirstNodeOfTag(root, [tag])
    node = root.firstChild()
    while not node.isNull():
        if node.toElement().tagName() in tag:
            return node
        res = getFirstNodeOfTag(node, tag)
        if not res is None: return res 
        node = node.nextSibling()

def ClearComments(root):
    node = root.firstChild() 
    while not node.isNull():
        nextt = node.nextSibling()
        if node.toElement().tagName() == "COMMENT":
            root.removeChild(node)
        node = nextt
        
#def addCommentLine(root, st):
#    node = QtCore.QDomDocument.createElement("COMMENT")
#    root.appendChild(node)
#    textnode = node.appendChild(self.dom.createTextNode(st))
    #textnode.appendChild(node)
    
#def addComments(root, lst):
#    for st in lst:
#        addCommentLine(root, st)

def DomToV7(dom):
    """Modification de l'arbre DOM d'un modele.
    Suppression des noeuds 'LAYER' de la version 6"""
    def ToV7(node):
        nextt = node.nextSibling()
        if node.toElement().tagName() == "LAYER":
            # pour un noeud "LAYER", les enfants sont marqués 
            parent = node.parentNode() 
            # d'un attribut "layer" et déplacés vers le parent
            layernum = node.toElement().attribute("rank", "0")
            child = node.firstChild()
            while not child.isNull():
                child.toElement().setAttribute("layer", layernum)
                parent.insertBefore(child, node)
                child = node.firstChild()
            parent.removeChild(node)
        else:
            child = node.firstChild()
            while not child.isNull():
                child = ToV7(child)
        return nextt
        
    # suppression de l'instruction xsl (svg)
    removePI(dom, "xml-stylesheet", 'type="text/xsl"')
    root = dom.documentElement()
    node = root.firstChild() 
    while not node.isNull():
        node = ToV7(node)
    
def NMLComment(indent=0, comments="", uindent="\t"):
    if isinstance(indent, int):
        indent = uindent * indent
    if isinstance(comments, str):
        comments = comments.split('\n')
    for i, st in enumerate(comments):
        if i == 0:
            lst = ['{0}<COMMENT>{1}</COMMENT>'.format(indent, st)]
        else:
            lst.append('{0}<COMMENT item="{1}">{2}</COMMENT>'.format(indent, i, st)) 
    return "\n".join(lst)

def NMLLink(indent=0, linkid=0, parentid=0, value=0.0, name=None, minimum=None, maximum=None, init=None, uindent="\t"):
    if isinstance(indent, int):
        indent = uindent * indent
    st = '{0}<LINK class="Synapse" linkid="{1}" parentid="{2}"'.format(indent, linkid, parentid)
    if name: st = '{0} name="{1}'.format(st, name)
#    if not value and  (minimum is None) and (maximum is None) and (init is None): 
#        return st + "/>"
    lst = [st + ">"]
    indentloc = indent + uindent
    #if value:
    lst.append('{0}<VALUE>{1}</VALUE>'.format(indentloc, value))
    if minimum is not None:
        lst.append('{0}<MINIMUM>{1}</MINIMUM>'.format(indentloc, minimum))
    if maximum is not None:
        lst.append('{0}<MAXIMUM>{1}</MAXIMUM>'.format(indentloc, maximum))
    if init is not None:
        if isinstance(init, str):
            st = init
        else:
            st = ";".join([str(item) for item in init])
        lst.append('{0}<INIT>{1}</INIT>'.format(indentloc, st))        
    lst.append('{0}</LINK>'.format(indent))
    return "\n".join(lst)
        
def NMLNode(indent=0, classname="NeuronSigma", name="", layer="0", nodeid=0, activ="", parents=[], linkid=0, uindent="\t"):
    if isinstance(indent, int):
        indent = uindent * indent
    st = '{0}<NODE class="{1}" nodeid="{2}"'.format(indent, classname, nodeid)
    if name: st = '{0} name="{1}"'.format(st, name)
    if activ: st = '{0} function="{1}"'.format(st, Activ2Name(activ))
    st = '{0} layer="{1}"'.format(st, layer)
    if len(parents) == 0:
        return st + "/>"
    lst = [st + ">"]
    for i, parent in enumerate(parents):
        lst.append(NMLLink(indent + uindent, linkid + i, parent, uindent=uindent))
    lst.append('{0}</NODE>'.format(indent))
    return "\n".join(lst)


#cdef = 'b!mkjq  q'

def newNML(modeldata=None, nin=1, nhid=3, nout=1, activ=2, name="%AUTO%", comment=None, monalver=33, uindent="\t"):
    outactiv = 0
    if modeldata:
        nin = modeldata["input"]
        nhid = modeldata["hidden"]
        nout = modeldata["output"]
        name = modelName(modeldata)
        activ = modeldata["activation"]
        outactiv = modeldata["outputactivation"]
    if comment == None:
        comment = "Created by Neuro One on Python"
    if name == "%AUTO%":
        name = "Model-{0}-{1}-{2}".format(nin, nhid, nout)
    nweight = (1 + nin)*nhid + (1 + nhid)*nout
    res = ['<?xml version="1.0" encoding="ISO-8859-1"?>']
    st = '<MODEL xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="{0}">'.format(monalver)
    res.append(st)
    st = '{0}<NETWORK class="NeuronNetwork" name="{1}" inputs="{2}" outputs="{3}" weights="{4}">'.format(uindent, name, nin, nout, nweight)
    res.append(st)
    res.append(NMLComment(2, comment, uindent))
    # neuron biais
    res.append(NMLNode(2, "Neuron", "bias", -1, uindent=uindent))
    cumulnode = 1
    for i in range(nin):
        # neurone d'entree
        nname = "IN_{0}".format(i)
        nodeid = "{0}".format(cumulnode)
        res.append(NMLNode(2, nodeid=nodeid, name=nname, layer=0, uindent=uindent))
        cumulnode += 1
    cumullink = 0
    parents = list(range(nin + 1))
    for i in range(nhid):
        # neurones caches
        nname = "H0_{0}".format(i)
        nodeid = "{0}".format(cumulnode)
        res.append(NMLNode(2, nodeid=nodeid, name=nname, layer=1, activ=activ, parents=parents, linkid=cumullink, uindent=uindent))
        cumullink += len(parents)
        cumulnode += 1 
    parents = [0] + list(range(nin+1, nin+1+nhid))
    for i in range(nout):
        # neurone de sortie
        nname = "OUT_{0}".format(i)
        nodeid = "{0}".format(cumulnode)
        res.append(NMLNode(2, nodeid=nodeid, name=nname, layer=2, activ=outactiv, parents=parents, linkid=cumullink, uindent=uindent))
        cumullink += len(parents)
        cumulnode += 1 
    res.append('{0}</NETWORK>'.format(uindent))
    res.append('</MODEL>')
    return "\n".join(res)

def getparamfilename(root, ppty, suffix): 
    #base = self.rootname
    if suffix:
        return "%s_%s_%s.npy" %(ppty, root, suffix)
    return "%s_%s.npz" %(ppty, root)
    
def restart(target="", params=[]):
    #import subprocess
    #import platform
    if not target:
        st = sys.argv[0]
        base = os.path.splitext(st)[0]
        if base.lower().endswith("python") and (len(sys.argv) > 1):
            target = sys.argv[1]
        else:
            target = st
    target = [target]
    if is_windows():
        cmd = '%s "%s"' % (sys.executable, target)
        main = sys.executable
    else:
        cmd = '%s %s' % ("pythonw", target)
        main = "pythonw"
    paramsst = ""
    if len(params):
        params = [str(val) for val in params]
        paramsst = " ".join(params)
        cmd = "%s %s"%(cmd, paramsst)
    try:
        os.execv(main, sys.argv)
#         os.execv("", sys.argv)
        #cmd = ["exec", "pythonw"]
        #cmd.extend(sys.argv)
        #os.system(" ".join(cmd))
        #exit()
        #subprocess.Popen(cmd)
    except Exception as e: 
        print(e)

    #exit("exit to restart with parameters: %s"% paramsst)
def defaultModuleExt():
    if is_mac():
        return "dylib"
    if is_windows():
        return "dll"
    #if is_linux():
    #    return "so"
    return "so"
    
def str2tuple(source, typ=None):
    # conversion d'un str(tuple) en tuple. Tous les éléments doivent avoir le même type
    if not (source.startswith('(') and source.endswith(')')):
        raise TypeError("%s should starts and ends with parenthesis"% source)
    source = source[1:-1]
    lst = source.split(',')
    res = []
    for val in lst:
        if val.strip():
            if typ is None:
                res.append(val.strip())
            else:
                res.append(typ(val.strip()))
    return tuple(res)

#===============================================================================
def run(argv=[]):
    if not len(argv):
        argv = sys.argv[1:]
    import argparse
    defaulttarget = os.path.join(monalpath, 'lcode')
    #os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lcode'))
    parser = argparse.ArgumentParser(description='monal.util.utils.') 
    parser.add_argument('-dd', '--dest_dir', dest='folder', 
        default=defaulttarget, help="Set working folder")
    parser.add_argument('-e', '--empty', action='store_true', 
        help="Force empty file creation")
    parser.add_argument('-d', '--delete', nargs="?", const=1, type=int,
        default=1, help="delete source files after compilation")
    parser.add_argument('-f', '--force', action='store_true',
        default=0, help="force compilation")
    parser.add_argument('--debug', nargs="?", const=1, type=int,
        default=0, help="debug state")
    parser.add_argument('-p', '--doprint', action='store_true',
        default=0, help="print compilation")
#     parser.add_argument('-y', '--yes', nargs="?", const=1, type=int,
#         default=defaultvalue("YES"),         
#         help="Answer yes to all questions and accept default values")
     
    options = parser.parse_args(argv)
     
    if options.empty:
        rr = 0
        if is_windows():
            target = os.path.join(options.folder, 'monal.lib')            
        else:
            target = os.path.join(options.folder, 'libmonal.a')
        with open(target, "w") as ff:
            ff.write("")
    else:# cette alternative est utilisee lors de l'installation
        rr = compilemonallib(force=options.force, 
                             outputdir=options.folder, 
                             doprint=options.doprint,
                             freesource=options.delete,
                             debug=options.debug)
 
    return rr

def docompilelib():
    run(['--doprint'])

#-------------------------------------------------------------------------------

if __name__ == "__main__":
#     runCompileMonalLib(True, freesource=True, debug=False)
    run()
    print("done")
#     print("done")

#     arg = sys.argv
#     freesource = '-free' in arg or '--free' in arg
#     #len(arg) >= 2 and arg[1] == 'free'
#     debug = '-d' in arg or '--debug' in arg
#     runCompileMonalLib(True, freesource=freesource, debug=debug)
#     argv = sys.argv[1:]
#     
#     st = "1,2,5:7,10:16:2,25"
#     st=5
#     
#     #opts = run(argv)
#     #print opts.folder
#     #print 'empty', opts.empty
#     print (getListFromStr(st))
#     print ('done')
    
    
#     rr = compilemonallib(force=True)
#     print "compile monal lib:", rr
#     print "Done"
#     pth = getuserbase()
#     print pth
#     tg = getChildPath(pth)
#     print tg
#     print getancestor(tg, 'lib', False)
#     print getancestor(tg, 'lib', True)
#     print "done"
    
#     print "desktop_path", get_desktop_path()
#     #print "Using compiler " + '"' + compilerName() + '"'
#     #dc.show_compilers()
#     print((monallibdate()))
#     #import os
#     
#     print AccentDict['ç']
#     
#     if is_windows():
#         print("Windows")
#         sourcedir = "C:\\Users\jeanluc\workspace\MonalPy\src"
#     if is_linux():
#         print("Linux")
#         sourcedir = "/Users/Shared/workspace"
#     if is_mac():
#         print("Mac")
#         sourcedir = "/Users/Shared/workspace"
#     print((getLibExt()))
#     
#     source_dir = os.path.join(sourcedir, "MonalPy/src/monal/code/code_templates/common")
#     include_dirs = [os.path.join(sourcedir, "MonalPy/src/monal/include")]
#     target_dir = os.path.join(sourcedir, "MonalPy/src/monal/llib")
#     excluded = ['readfile', 'dlmdriver', 'train']
#     print((fileDate(os.path.join(source_dir, "train.c"))))
#     print((fileDate(os.path.join(source_dir, "mathplus.c"))))
#     
#     
#     complist = list(dc.compiler_class.keys())
#     print(complist)
#     compilemonallib(force=True)
#     print((getlibinitialized()))
#     #com pile_lib(default=False, 
#     #            libname="monal", 
#     #            source_dir=source_dir, 
#     #            include_dirs=include_dirs, 
#     #            excluded=excluded, 
#     #            doprint=True)
#     #create_ monal_lib(complist, source_dir=source_dir, target_dir=target_dir, include_dirs=include_dirs, excluded=excluded, doprint=True)
#     print("done")
#     #sys.stderr = olderr
#     #print objCompileCommand("toto.c", destdir=r"build\temp.win32-2.7\Release", includedirs=[r"C:\toto\bin"])
        