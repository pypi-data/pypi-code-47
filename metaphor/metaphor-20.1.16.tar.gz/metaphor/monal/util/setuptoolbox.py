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
Created on 2 mars 2017

@author: jeanluc
'''

import os, sys, re, stat
from site import getuserbase, USER_BASE
from distutils.dir_util import mkpath
from distutils import sysconfig as sc
import distutils.ccompiler as dc
from distutils import errors as de
import shutil, errno
from tempfile import mkdtemp

# Fonctions utilitaires pur le setup.py
#----------------------------------------------------------------------------

def hasPackage(pth, package="monal", pythonver="3.6", version=""):  #, versionmin=""):
    content = os.listdir(pth)
    res = package in content
    if not res:
        return False
    if not len(version):
        return True
#     if len(pythonver) and ('.' in pythonver):
#         egg_info = "%s-%s-py%s.egg-info" % (package, version, pythonver)
#         if len(version):
#             if (package in content) and (egg_info in content):
#                 return True
#     else:
#     egg_info = "%s-%s-py%s" % (package, version, pythonver)
    egg_info = "%s-%s" % (package, version)
    for val in content:
        if val.startswith(egg_info):
            return True
    return False

# def compile monal lib(erasesources=True, userTarget=False, outfile="", monalpath="", isVirtual=False, isWin=False):
#     #import distutils.ccompiler as dc
#     #import distutils.sysconfig as sc
#     
#     libname = 'monal'
#     modulename = 'monal'
#     #version = __import__('monal').__version__
#     #applidir = getApplicationsDir(libname)
#     sitebasepath = getsitebase(userTarget, isVirtual)
#     #egg_info_path = os.path.join(sitebasepath, "%s-%s.egg-info"% (modulename, version))
#     #egg_info_sourcepath = os.path.join(egg_info_path, "SOURCES.txt")
#     if not len(monalpath):
#         monalpath = os.path.join(sitebasepath, modulename)
#         if not os.path.exists(monalpath):
#             monalpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), modulename)
#     comp = dc.get_default_compiler()
#     source_dir = os.path.join(monalpath, 'lcode', 'code_templates', 'common')
#     target_dir = os.path.join(monalpath, 'lcode')
#     try:
#         curmode = os.stat(target_dir).st_mode
#         os.chmod(target_dir, curmode | stat.S_IWOTH | stat.S_IROTH) 
#         OKmode = True
#     except:
#         OKmode = False
#     include_dirs = [sc.get_config_vars()['INCLUDEPY'], os.path.join(monalpath, 'include')]
#     excluded = ['readfile', 'dlmdriver']
#     extra_args = ['-fPIC']  
#     if outfile:
#         outfile.write( "libname : %s\n"% libname)
#         #outfile.write( "applidir : %s\n"% applidir)
#         outfile.write( "monalpath : %s\n"% monalpath)
#         outfile.write( "source_dir : %s\n"% source_dir)
#         outfile.write( "target_dir : %s\n"% target_dir)
#         outfile.write( "include_dirs :\n") 
#         for val in include_dirs:
#             outfile.write("\t%s\n"% val)
# 
#     try:
#         rr = create_lib(comp, libname, source_dir=source_dir, 
#             target_dir=target_dir, include_dirs=include_dirs, excluded=excluded,
#             extra_preargs=extra_args, isWin=isWin) 
#         if erasesources:
#             eraseCommon(userTarget, outfile, monalpath, isVirtual)
#     except Exception as err:
#         rr = -1
#         if outfile:
#             outfile.write( "Error in compiling monal lib\n")
#             outfile.write(str(err))
#             outfile.write("\n")
#         else:
#             print("Error in compiling monal lib\n")
#     if OKmode:
#         os.chmod(target_dir, curmode)
#     return rr

# def eraseCommon(userTarget=False, outfile="", monalpath="", isVirtual=False):
#     from distutils.dir_util import  remove_tree
#     if not len(monalpath):
#         libname = 'monal'
#         monalpath = os.path.join(getsitebase(userTarget, isVirtual), libname)
#     source_dir = os.path.join(monalpath, 'lcode', 'code_templates', 'common')
#     remove_tree(source_dir, verbose=True)
# #     if outfile:
# #         outfile.write( "removing %s\n"% source_dir)

def getChildPath(parent, folder="site-packages"):
    """Look for a 'folder' directory in the children tree of 'parent'.
    return empty string if not found.
    """
    res = ""
    for path, dirs, _ in os.walk(parent):
        if folder in dirs:
            return os.path.join (path, folder)
        else:
            for direc in dirs:
                res = getChildPath(direc, folder)
                if res: break  #return res
    return res
 
def getbase(userTarget=False, isVirtual=False):
    if isVirtual or not userTarget:
        return os.path.abspath(sys.prefix)
    if userTarget:
        try:
            return getuserbase()
        except:
            return USER_BASE
    
def getsitebase(targetuser=False, isVirtual=False):
    pth = getbase(targetuser, isVirtual)
    return getChildPath(pth, "site-packages")

def getApplicationsDir(appli="", docreate=False):
    base = os.path.join(os.path.expanduser("~"), "Applications")
    if appli:
        base = os.path.join(base, appli)
    if docreate:
        mkpath(base)
    return base
    
def compilerName():
    comp = dc.get_default_compiler()
    getnext = False

    for a in sys.argv[2:]:
        if getnext:
            comp = a
            getnext = False
            continue
    #separated by space
        if a == '--compiler'  or  re.search('^-[a-z]*c$', a):
            getnext = True
        continue
    #without space
        m = re.search('^--compiler=(.+)', a)
        if m == None:
            m = re.search('^-[a-z]*c(.+)', a)
        if m:
            comp = m.group(1)

    return comp

def create_lib(comp, libname, source_dir="", target_dir="", include_dirs=[], 
               excluded=[], extra_preargs=[], doprint=False, isWin=False):
    """Creation of a static library.
    parameters :
        comp -> compiler name. Must be in the list of available compilers.
        libname -> name of the library. Not file name.
        source_dir -> directory of C sources files.
        target_dir-> directory of resulted library file. 
            If empty, library will be installed in Python libs folder. 
        excluded -> list of excluded files. '.c' extension will be added if necessary.
        doprint -> print results.
    """
    res = 0 
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
    comp = comp if comp else compilerName()
    cc = dc.new_compiler(compiler=comp)
    cc.mkpath(target_dir)
    _, _, files = next(os.walk(source_dir))
    #sources = [os.path.join(root, val) for val in files if val.endswith(".c") and not val in excluded]
    sources = [val for val in files if val.endswith(".c") and not val in excluded]
    macros = [("_CRT_SECURE_NO_WARNINGS", 1)]
    #plat = sys.platform
    #if (plat=='nt') or plat.startswith('win'):
    if isWin:  #IS_WIN32 or IS_WINDOWS:
        macros.append(("WIN", 1))
    try:
        temp = mkdtemp(prefix="$%s"% libname)  
        fulllibname = os.path.join(target_dir, 'lib%s.a'% libname)
        if os.path.exists(fulllibname):
            os.remove(fulllibname)
        objlist = cc.compile(sources, output_dir=temp, macros=macros, 
            include_dirs=include_dirs, extra_preargs=extra_preargs)
        cc.create_static_lib(objlist, libname, target_dir)
        res = 1
        if doprint:
            print(("compiler %s succeded"% comp))
    except de.CompileError:
        print(("compiler %s failed"% comp))
    finally:
        try:
            shutil.rmtree(temp)  # delete directory
        except OSError as exc:
            if exc.errno != errno.ENOENT:  # ENOENT - no such file or directory
                raise  # re-raise exception
    os.chdir(cur)
    return res
#----------------------------------------------------------------------------

if __name__ == '__main__':
    """Recreation of the monal module
    """
    monalpath = os.path.dirname(__file__)
    monalpath = os.path.dirname(monalpath)
#    compile monallib(erasesources=False, userTarget=False, outfile="", monalpath=monalpath)
    print('Done')
