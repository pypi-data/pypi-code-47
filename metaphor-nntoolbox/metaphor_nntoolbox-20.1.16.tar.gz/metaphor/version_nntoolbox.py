#-*- coding: ISO-8859-15 -*-
#-------------------------------------------------------------------------------
# Metaphor
#
# $Id: $ 
#
# Copyright 2018 Jean-Luc PLOIX
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
Created on 24 jan 2019

@author: jeanluc
'''
#include_start
VERSION_MAJOR = 20         # YEAR
VERSION_MINOR = 1          # MONTH    
VERSION_MAINTENANCE = 16   # DAYq
VERSION_BUILD = 0          # release
TAG = "a"

# history # 

# 20.1.16    OK verif publi results
# 20.1.16.1  OK usage call with get
# 20.1.15.1  OK test calls
# 20.1.14.4  current work on test with files
# 20.1.12.2  fix bug look for 'xlsx' and 'xlsm' in candidate Excel files. Source file nntoolbox.datareader.excelsource.py l.54 
# 20.1.12.1  fix destdir in _modelcontainer.py l.761
# 20.1.11.2  fix recap token "'tuple' object has no attribute 'book'"
# 20.1.10.4  fix token.symbol and token ._symbol for 2H
# 20.1.10.3  increment __version__ in codeconst.py
# 20.1.10.2  traitement des isotopes
# 20.1.10.1  add atoms (Pb, ..) in atoms available list atoms.cfg
# 20.1.9.1   add trainingDate table in dbResults + analyse central atoms
# 20.1.7.1   branch scandium-ghost. fix it by complying to SMILES spec
# 20.1.1.1   modify configstr for contener programmation
# 19.12.29.1 move version control to GitHib
# 19.11.28.2 cosmetic fix output usage mode
# 19.11.28.1 fix decimal in usage (defaulted to 2, with verbose="3,0")
# 19.11.26.1 fix bug on testSheet
# 19.11.20.4 format axis in new_line_chart
# 19.11.20.3 format default 0.000
# 19.11.20.1 add numerical formats in options: 'excelnumformat' & 'terminalnumformat'
# 19.11.19.2 publi ? excel testsheet, lootrainsheeet corrected
# 19.11.12.2 publi ?!?
# 19.11.9.2  cosmetic change in Excel result files: test result Chart select event show molecule and smiles and propose return to data sheet 
# 19.11.9.1  return to gcc compiler
# 19.11.1.1  fix chart series names
# 19.10.31.6 test codeVersionOK for different C compiler
# 19.10.31.1 repair index field in training result sheet (titles[0]  #[0]) nn1.api_api_service l.2157
# 19.10.30.3 multi hidden -> multi db
# 19.10.30.2 OK parallel compile
# 19.10.28.6 add delete sources in monal lib compile during install
# 19.10.28.5 back to no parallel compile 
# 19.10.28.2 back to parallel compile with order change in create_lib
# 19.10.28.2 no parallel compile
# 19.10.28.1 add compile parallelism in main stream metaphor
# 19.10.17.1 & 2 
# 19.10.4.2 _api_service.py l.608 -> fix mode if unknown
# 19.10.4.1 tentative link 64 bit in interfacetraindll.h
# 19.7.1.2  cosmetic in docker metaphor
# 19.7.1.1  input prime in C code  
# 19.6.26.6 Ok display and fix server init bug
# 19.6.26.5 Ok display and fix server init bug
# 19.6.26.2 Ok display
# 19.6.23.2 OK setup with cython
# 19.6.17.1 cosmetic changes
# 19.6.13.1 fix allow_pickle=True in numpy.load. Necessary since numpy 1.16.4 wher the default value has been changed
# 19.6.12.3 bug fixing
# 19.6.2.2  bug fixing
# 19.6.1.6  parallel introduced in preprocaction. best result removed from test result chart
# 19.5.21.2 weights moderation in file decoration
# 19.5.21.1 revisited weights moderation
# 19.5.17.4 activation of weights moderation name weightsmoderation also for LOO and BS
# 19.5.17.1 activation of weights moderation name weightsmoderation
# 19.5.17.1 activation of weights moderation
# 19.5.6.1  set server interface + modify monal.model._model.transfer with kwds + extra
# 19.5.1.1  protect 'dialogdefaults.ini' reading in _api_service against corruption
# 19.4.26.4 fix bug "server" as command
# 19.4.26.2 include "server" as command
# 19.4.26.1 include metaphor api
# 19.4.25.1 fix address bug in LOO training results sheet
# 19.4.24.2 objects destruction checked for modules with ".so"
# 19.4.24.1 message 'loo' mis en majuscule 'LOO'
# 19.4.23.3 Ok for filltest LOO et BS
# 19.4.23.1 Suppress the call to float('inf') for compatibility with excel
# 19.4.18.5 add workbook.close in _api_service 3224
# 19.4.18.4 add workbook.close in _api_service 3224
# 19.4.18.1 coherence test betweeen  source and test
# 19.4.17.3 install debug 'usage'
# 19.4.15.5 bug fixed in demo argsfile location
# 19.4.15.3 bug fixed in demo argsfile location
# 19.4.15.2 modif debug
# 19.4.15.1 add rundemo
# 19.4.14.6 add "Property naame" in utilities dsheet
# 19.4.14.5 OK version docker + version scipy in version display
# 19.4.14.4 OK version docker + init in dockerfile revisited
# 19.4.14.3 OK version docker
# 19.4.12.2 fix seed bug in loo & bootstrap weights initialization
# 19.4.11 fix many bugs = loo training, threshold -1, docker cmd line, ...
# 19.2.21a7 test of entrypoint usage
# 19.2.19a5  fix bug in hour:min:sec display
# 19.2.19a4 fix bug fuffH (from YesyNoQuestion)+ bug new compiled code version (backing ol so)
# 19.2.9a5  fix bug in load existing nn model
# 19.2.9a3  completion of 09/02/2019 -> docker 1.2
# 19.2.8a2  completion of 08/02/2019 -> docker 1.2
# 19.2.1a1  fix errors in gm mode demo 
# 19.1.24a2 fix the test errors 
# 19.1.1a4 remove nntoolbox from metaphor project (it moved to metaphor-nntoolbox)
# 19.1.0a3 en cours uploader
# 19.1.0a2  en cours uploader
# 19.1.0a1  creation of metaphor_nntoolbox project
# 18.11.23a2 fix cython file erasing after install
# 18.11.22a12 fix ccrypt.py after erasing common folder in install
# 18.11.22a11 OK for erasing common folder in install
# 18.11.22a3 OK install
# 18.11.6a10 remove tests with *.so
# 18.11.6a9 modif testfiles extension from TXT to txt
# 18.11.6a2 map setup 
# 18.11.6a1 create metaphor project 
#include_end

VERSION3 = "%d.%d.%d" % (VERSION_MAJOR, VERSION_MINOR, VERSION_MAINTENANCE)
VERSION2 = "%d.%d" % (VERSION_MAJOR, VERSION_MINOR)
if not VERSION_BUILD:
    candidate__version__ = VERSION3
elif TAG:
    candidate__version__ = "{0}{1}{2}".format(VERSION3, TAG, VERSION_BUILD)
else:
    candidate__version__ = "%d.%d.%d.%d" % (VERSION_MAJOR, VERSION_MINOR, VERSION_MAINTENANCE, VERSION_BUILD)  
__version__ = candidate__version__

version = lambda: __version__

def distname(dname="", path="", ext=".tar.gz"):   
    import os
    if not dname:
        dname = 'metaphor'
    st = "%s-%s%s"% (dname, __version__, ext)
    if len(path):
        st = os.path.join(path, st)
    return st

if __name__ == "__main__":
    print("metaphor version :", __version__)