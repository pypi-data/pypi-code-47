p#-*- coding: ISO-8859-15 -*-
#-------------------------------------------------------------------------------
#
# $Id: version.py 4819 2018-11-02 05:32:25Z jeanluc $ 
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
Created on 20 nov. 2013

@author: jeanluc
'''
VERSION_MAJOR = 19
VERSION_MINOR = 12
VERSION_MAINTENANCE = 30
VERSION_BUILD = 1
TAG = "a"

# history # 

# 19.1.0a1  creation of metaphor_nntoolbox project
# 18.6.13.3  update of cython to 0.28.5
# 18.6.13.2  update of cython to 0.25
# 18.6.13.1  return to targz build format
# 18.6.13.0  return to cython use
# 18.6.12.1  add tokenlib in required
# 18.6.11.0  repeat to get dev and std versions simultaneously
# 18.6.8.2   modify version display
# 18.6.8.1   add rstrip in file reading in manageApiOptionsResult
# 18.6.8.0   add rstrip in file reading in manageApiOptionsResult
# 18.6.7.1   result axis format to "'#,##0.00'"
# 18.6.7.0   adjust docker
# 18.6.6.4   fix bug in multiusage
# 18.6.6.3   fix bug in multiusage
# 18.6.6.2   fix bug in multiusage
# 18.6.6.1   fix bug in multiusage
# 18.6.6.0   compile docker
# 18.5.28.0  new get_results_from_smiles in api.run
# 18.5.26.0  remise en ordre des sauvega    rdes wush
# 18.5.25.3  idem
# 18.5.25.2  fix bug in usage NN without id and target
# 18.5.25.0  usage decimal piloted by target string
# 18.5.24.3  back to cython
# 18.5.24.2  back to cython
# 18.5.24.1  no cython
# 18.5.24.0  use wheel everywhere
# 18.5.23.2  version beck to cython
# 18.5.23.1  version no_cython
# 18.5.22.0  remove versions in install requires
# 18.5.19.0  full installrequire
# 18.5.18.1  change modeltemplate to start with 'zzz'
# 18.5.18.0  fix bug in indexing files in GM create model
# 18.5.17.1  fix bug in default init with @ argfile calling
# 18.5.17.0  fix bug in finishExcel

# 18.5.16.1  fix bug in finishExcel
# 18.5.16.0  fix dockerfiles nn1_base
# 18.5.15.8  still working on dependencies
# 18.5.15.4 remove dependencylinks from setup
# 18.5.15.1  remove import futures from nntoolbox.setup.py
# 18.5.15.0  remove import futures
# 18.5.12.1  fix bug SF_CODE -> SF_CCODE in _driver
# 18.5.12.0  OK nn1 api interface and demo jupyter
# 18.4.21.4  OK test argfile creation
# 18.4.21.3  fix nntoolbox.utils.getListFromStr to accept None input
# 18.4.21.0  display LOO inspected
# 18.4.20.0  clarify init options
# 18.4.19.0  random init for trainjob back to the old method
# 18.4.18.7  cosmetic
# 18.4.18.6  cosmetic
# 18.4.18.2  send to sys.stderr error messages that stop
# 18.4.18.1  cosmetic display
# 18.4.18.0  fixing display with berbose and verbosexls
# 18.4.17.9  modif utils.callerView to remove /home/ from displayed filenames
# 18.4.17.8  modif utils.callerView to remove /home/ from displayed filenames
# 18.4.17.3  fix bug DEMO_DEBUG_FOLDER
# 18.4.17.2  fix bug results display internal folder
# 18.4.17.1  fix bug "/docker" in nntoolbox/utils
# 18.4.17.0  change internal excvhange folder from /docker to /home
# 18.4.16.3  full version display for VERSION fixed
# 18.4.16.0  full version display for VERSION fixed
# 18.4.15.3  ful version display for VERSION
# 18.4.15.2  modernize monalrecords
# 18.4.15.1  init xml=None in getModelDict
# 18.4.15.0  supp modeldata from nnx
# 18.4.14.0  check modelCount in existing training models
# 18.4.12.0  extend search input files on all children of shared folder
# 18.4.11.3  reading hostpath from docker in host.pth ...
# 18.4.11.0  reading hostpath from docker in host.pth
# 18.4.10.3  OK fullH
# 18.4.10.2  check csv data foermat
# 18.4.10.1  change static lib file names more specific
# 18.4.10.0  fix bug erase tempdir before compiling
# 18.4.9.4   supp '-D_FILE_OFFSET_BITS=64' in compile dll
# 18.4.9.3   declarations extern en C 3
# 18.4.9.2   declarations extern en C 2
# 18.4.8.1   declarations extern en C
# 18.4.8.0   track bug testH
# 18.4.6.3   main tra    in back to parallel
# 18.4.6.2   init seed in LOO indexed on init and no longer on training example
# 18.4.6.1   train with H atoms
# 18.4.6.0   accept H atoms froim smiles
# 18.4.5.2   fix loo save
# 18.4.5.0   fix usage multi display
# 18.4.4.14 reprise usage gm

# 18.4.4.5  OK usage with few parameters
# 18.4.4.0   sqlfilename and sqlLOOfilename in excel file
# 18.4.3.6   fix resultFrame call and recall
# 18.4.3.4   fix loo decor and resultFrame recall
# 18.4.3.3   fix decor empty
# 18.4.3.2   fix decorfile
# 18.4.3.1   fix bug in getSaveDictMulti
# 18.4.3.0   fix bug loo only
# 18.3.29.0  set usage mode - 1
# 18.3.26.0  debug tootest + modif random initia    lization in parallel jobs
# 18.3.24.0  debug indexation des lootrain sur excel
# 18.3.23.0  debug test results indexings
# 18.3.22.5  debug normalisation des modËles en test (nn1 et gm)
# 18.3.22.2  debug gm test
# 18.3.22.2  debig lootest for gm projects - dont work for nn projects
# 18.3.21.1  ajout de '-D_FILE_OFFSET_BITS=64' dans les azrguments de compilation du module dynamique
# 18.3.21.0  fix bug in seed init in parallel jobs (std anf LOO-BS)
# 18.3.20.3  fix bug on setidentifier in C code
# 18.3.20.0  bug on gm molecules display - use #define _FILE_OFFSET_BITS  64 in dll C code - nn1 OK (dev) on train, test, loo for nn and gm
# 18.3.16.0  intro of chem_gm in nn1 require˘ents
# 18.3.15.3  fix library compile, including monal lib
# 18.3.15.0  fix sql selection results, multi compile
# 18.3.14.0 blocksize variable in multimodel compile - display local seed in training 
# 18.3.5.1 no input type checking
# 18.3.5.0 optimisation C code
# 18.3.2.1 fix bug in compile multimodels aftder modif of compile_lib
# 18.3.2.0 fix LOO bug in loo models selection
# 18.3.1.0  modif code C for memory blocking
# 18.2.9.0 rewrite inputs selection
# 18.2.8.1 
# 18.2.8.0  revisit input selection wth gramm-schmidt
# 18.2.2.1  follow nntoolbox 18.2.2.1  relax openpyxl version requirement
# 18.1.31.0
# 7.0.2.25 extract _driverlib from cython
# 7.0.2.22 extract monal/datareader/fileInspect from cython
# 7.0.2.21 preceeding without monal/model
# 7.0.2.19 preceeding + monal/model except _network, _node, _link, _modelfunc
# 7.0.2.18 preceeding + monal/model except _network, _node, _link
# 7.0.2.17 preceeding + monal/model except _network
# 7.0.2.16 preceeding + monal/model
# 7.0.2.15 preceeding + monal/library
# 7.0.2.14 preceeding + monam/driver in cythonlist except networkfactory, drivermultidyn, parallelJobs
# 7.0.2.13 preceeding + monam/driver in cythonlist except networkfactory, drivermultidyn
# 7.0.2.12 preceeding + monam/driver in cythonlist except networkfactory
# 7.0.2.11 preceeding + monam/driver in cythonlist
# 7.0.2.10 add all monal/datareader monal/lcode monal/util*.py to cythonlist except monal/util/utils.py
# 7.0.2.8  add all monal/datareader monal/lcode monal/model*.py to cythonlist
# 7.0.2.7  add all monal/datareader monal/lcode *.py to cythonlist
# 7.0.2.6  add all monal/datareader *.py to cythonlist
# 7.0.2.5  add all monal *.py to cythonlist
# 7.0.2.4  follow nntoolbox 1.0.2.4  full cython on nntoolbox
# 7.0.2.3  follow nntoolbox 1.0.2.2 cython on nntoolbox ote filetoolbox 
# 7.0.2.2  follow nntoolbox 1.0.2.2  cython on nntoolbox
# 7.0.2.1  follow nntoolbox 1.0.2.1   pandas > 0.21.0 => set_value, get_value depreecated
# 7.0.2.0  basic woth no cython proptection
# 7.0.1.55 test of C extension in monal
# 7.0.1.54 test of C extension in monal

#  ...25  test setup & install
# 7.0.1.18 follow nntoolbox 1.0.1.15 test cleaner
# 7.0.1.17 follow nntoolbox 1.0.1.14 test cleaner
# 7.0.1.16 follow nntoolbox 1.0.1.13 test cleaner
# 7.0.1.15 follow nntoolbox 1.0.1.12 fix bug in cleanup
# 7.0.1.14 follow nntoolbox 1.0.1.11 fix bug in setup
# 7.0.1.13 follow nntoolbox 1.0.1.10 new setup
# 7.0.1.12 follow nntoolbox 1.0.1.9  fix bug in configparsertoolbox
# 7.0.1.11 follow nntoolbox 1.0.1.8  return to setup process
# 7.0.1.10 follow nntoolbox 1.0.1.7  no arguments at all 2
# 7.0.1.9  follow nntoolbox 1.0.1.6  no arguments at all
# 7.0.1.6  follow nntoolbox 1.0.1.5  fix bug test only
# 7.0.1.4  follow nntoolbox 1.0.1.4  bug excelutil color lev thresh
# 7.0.1.1  follow nntoolbox 1.0.1.1
# 7.0.1.0  follow nntoolbox 1.0.1.0  first OK of nn1 in docker
#  35 fix bug in monaltoolbox choicequestion
# 7.0.0.19 frix bug in util/utils
# 7.0.0.17 follow nntoolbox 1.0.0.23
# 7.0.0.16 follow nntoolbox 1.0.0.22 exception on clean files
# 7.0.0.14 follow nntoolbox 1.0.0.20
# 7.0.0.10 add 'magic' in required in setup
# 7.0.0.9  follow nntoolbox 1.0.0.20 clean filetoolbox
# 7.0.0.6  follow nntoolbox 1.0.0.19 fix install with test
# 7.0.0.3  follow nntoolbox 1.0.0.3 modify utils
# 7.0.0.2  follow nntoolbox 1.0.0.2 add average data on test chart
# 7.0.0.1  follow nntoolbox 1.0.0.1 fix bug in excelutils (index in test chart)
# 7.0.0.0  follow nntoolbox 1.0.0.0  OK first NN1
# 6.1.1.15 follow nntoolbox 0.0.0.6
# 6.1.1.14 follow nntoolbox 0.0.0.5
# 6.1.1.12 fix setup bug
# 6.1.1.11 follow nntoolbox 0.0.0.4
# 6.1.1.10 follow nntoolbox 0.0.0.4
# 6.1.1.0  test expand cythonlist 
# 6.1.0.49 OK setup with cythonlist -> remove py files 
# 6.1.0.33 test setup with cythonlist -> remove py files 
# 6.1.0.32 test setup 
# 6.1.0.31 test setup 
# 6.1.0.30 test setup 
# 6.1.0.29 test setup 
# 6.1.0.28 test setup 
# 6.1.0.27 test setup with getCythonList
# 6.1.0.26 publi 25 October 2017
# 6.1.0.25 publi October 2017
# 6.1.0.24 automate copy pyx
# 6.1.0.23 OK cythonize 5 files
# 6.1.0.21 OK cythonize 7 files
# 6.1.0.14 OK cythonize 3 files
# 6.1.0.13 OK cythonize 3 files
# 6.1.0.3..12  test x on cythonize
# 6.1.0.2  test 3 on cythonize
# 6.1.0.1  test 2 on cythonize
# 6.1.0.0  test 1 on cythonize

# 6.0.1.3  work on debug encoding files monaltoolbox debugOutput
# 6.0.1.2  for docker demo 6.1
# 6.0.1.1  change numpy version to 1.13.3
# 6.0.1.0  fix bug in configstr, central, decor
# 6.0.0.42 fix bug in sqlite_copy_db
# 6.0.0.41 new gm with env
# 6.0.0.40 fix bug in toolbox.yesnoquestion : raw_input
# 6.0.0.39 fix bug in toolbox.isint
# 6.0.0.38 fix bug in toolbox.isint
# 6.0.0.37 fix bug in util.utils.CCharOnlys with u nicode
# 6.0.0.36 OK py36
# 6.0.0.35 fix install setup: no lib compile ins install.
# 6.0.0.34 modif openpyxl requirement >=...
# 6.0.0.33 put back afterinstall in setup
# 6.0.0.31 debug
# 6.0.0.30 eliminate makdtemp in util.utils
# 6.0.0.29 add mkdirs after mkdtemp in util.utils
# 6.0.0.27 fix bug on compilemonallib in utils
# 6.0.0.26 fix bug on compilemonallib in utils
# 6.0.0.25 fix bug on compilemonallib in utils
# 6.0.0.24 fix bug on compilemonallib in utils
# 6.0.0.23 fix bug on xfile in toolbox
# 6.0.0.22 introduce crypt fonctionamity in utils for comple monal lib
# 6.0.0.21 Fix bug in data files to install
# 6.0.0.20 fix setup without compile monal lib
# 6.0.0.19 re-add compilemonallib in compile module, from crypted files
# 6.0.0.18 fix haspackage in setuptoolbox
# 6.0.0.17 fix haspackage in setuptoolbox
# 6.0.0.16 fix haspackage in setuptoolbox
# 6.0.0.15 test install docker
# 6.0.0.14 eliminate 'pip-build' content monalpath
# 6.0.0.13 fix install bug in python 3
# 6.0.0.11 add wirites in installmonal.txt
# 6.0.0.10 fix install bug bad location & erase failing
# 6.0.0.8  fix install bug bad location & erase failing
# 6.0.0.8  fix print bug in lineartoolbox
# 6.0.0.7  remove fu ture from install requirement in setup
# 6.0.0.6  bug in setuptoolbox.compilemonallib test
# 6.0.0.5  fix utf-8 errors in C codes crypt
# 6.0.0.4  fix install bug in C code crypt
# 6.0.0.3  fix install bug on environ
# 6.0.0.2  test dist PyPi
# 6.0.0.1  test dist PyPi
# 6.0.0.0  Python 3.6 
# 5.0.0.2  modif fut ures in fu ture in setup required
# 5.0.0.1  fix bug in _driver.TransferEx.mappingtransferleverages
# 5.0.0.0  Code Python 3.1
# 4.5.0.2  fix bug in setup.py templatelist ->->->->->->->->->->->->Publi
# 4.5.0.1  modif MANIFEST.in to eliminate uncrypted files
# 4.5.0.0  set crypted template sources
# 4.4.1.4  demo avec bootstrap OK
# 4.4.1.3  adjust CORRECTED _FIELD & create dbField in monalconst
# 4.4.1.2  intro onSpecialResult in driver
# 4.4.1.1  intro loo in api demo
# 4.4.1.0  reorg gmx for eliminate config

# 4.4.0.2  ???
# 4.4.0.1  add loadFrom in monal.util.toolbox
# 4.4.0.0  last before loo and bootstrap development
# 4.3.2.37 modify monal.excelsource.getcustomproperty
# 4.3.2.36 add SUBSTITUTE_FIELD in monalconst
# 4.3.2.35 modify to CORRECTED_ FIELD in monalconst
# 4.3.2.34 add CORRECTEDFIELD in monalconst
# 4.3.2.33 test sql_numpy
# 4.3.2.32 cosmetic in util.utils
# 4.3.2.31 heu ?
# 4.3.2.30 fix bug in driver.transferex 
# 4.3.2.28 add getcustomproperty in datareader.excelsource
# 4.3.2.27 add hasOneOf in util.toolbox
# 4.3.2.26 add enrichFilename in util.utils
# 4.3.2.25 ??
# 4.3.2.24 modif repr
# 4.3.2.23 ??
# 4.3.2.22 modif .__repr__
# 4.3.2.21 add chmod to compilemonallib
# 4.3.2.20 ecclude *.a in setup
# 4.3.2.19 
# 4.3.2.18 fix bug monaltoolbox
# 4.3.2.17 display of seconds
# 4.3.2.16 supp space before ":" in display
# 4.3.2.15 code version 46
# 4.3.2.14 ???
# 4.3.2.13 monal/util/utils.backupfile modify to return true if file do not exists
# 4.3.2.12 cosmetic
# 4.3.2.11 cosmetic
# 4.3.2.10 upgrade codeversion to recompile models eliminating default connect values
# 4.3.2.9  cosmetic
# 4.3.2.8 fix bug in _modellib
# 4.3.2.7  fix bug in _modellib
# 4.3.2.6  add substitute of scipy
# 4.3.2.5  add tabledisplatdict in monalconst
# 4.3.2.4  bug fix in modellib import
# 4.3.2.3  contournement de scipoy dans _modellib. rest a faire dans mplUtils
# 4.3.2.2  _drivermultidyn optimize check presence of scipy
# 4.3.2.1  suppr scipy requirement in setup. _driver IC computation and train from optimize
# 4.3.2.0  suppr scipy requirement in setup. IC computation to set as independant of scipi.stats.t

# 4.3.1.92 cosmetic changes
# 4.3.1.91 modify DriverMultiDyn.repr to introduce veryshort level
# 4.3.1.90 cosmetic changes
# 4.3.1.89 utils.backupfile revisited -> xxx_backup_.ext
# 4.3.1.88 pretty setup +modif codeconst.__version__ 42 + utils.backupfile revisited
# 4.3.1.87 add setuptoolbox in monal.util to separate frol toolbox
# 4.3.1.86 bug fix in train.c (=! -> !=) and move install utilities from setup.py to toolbox.py
# 4.3.1.85 codeversion update
# 4.3.1.84 bug fix in tain.c earlyHii
# 4.3.1.83 monal.util.utils backupfile modif
# 4.3.1.82 gmapidemo manage OKcodeversion
# 4.3.1.81 modif calcul de deltash in train.c par diff des sommes de hii => modif codeconst.__version__ 39
# 4.3.1.80 modif calcul de deltash in train.c => modif codeconst.__version__ 38
# 4.3.1.79 enrichment of toolvox/IndexFilename -> add "last" param
# 4.3.1.78 Ok for api use existing models
# 4.3.1.77 modif gmapidemo -> useexisting added param
# 4.3.1.76 fix bug in LibManager.codeversionOK 
# 4.3.1.75 
# 4.3.1.74 stabilisation
# 4.3.1.73 stabilisation
# 4.3.1.72 modif monal/util/IndexFilename
# 4.3.1.71 modif monal/util/IndexFilename
# 4.3.1.70 isnan bug fixed
# 4.3.1.69 create monal/api
# 4.3.1.68 add xlsm as accepted filetype in excelsource
# 4.3.1.67 add gettitles in datareader/excelsource
# 4.3.1.66 change read_sql with read_sql_query in sqlite_numpy.getDataFrame
# 4.3.1.65 minor cosmetic bugs fixed
# 4.3.1.64 minor cosmetic bugs fixed
# 4.3.1.63 work on datafields and testfields
# 4.3.1.62 put datafields in datareader/excelsource
# 4.3.1.61 optimize speed
# 4.3.1.60 add IndexFilename in monal/util/toolbox
# 4.3.1.59 modif setup install_requires to be coherent with chem_gm
# 4.3.1.58 adjust grad and accessories length with longParamCount
# 4.3.1.57 supp adptParams and adaptDispersion in _Driver 
# 4.3.1.55 bug fix in toolbox
# 4.3.1.54 speed up usage
# 4.3.1.53 impose epoches as integer in -paralleljobs.onTreturnResult
# 4.3.1.52 adjust train, transferOld
# 4.3.1.51 mod C code add superOut in trainbase
# 4.3.1.50 mod multidyn for moduleType
# 4.3.1.49 improve _linkstr in util/toolbox
# 4.3.1.48 add _linkstr in util/toolbox
# 4.3.1.47 add dict attribute in _drivermultidyn
# 4.3.1.46 add xlwt in install required
# 4.3.1.45 use no lib in gm usage demo
# 4.3.1.44 rewrite raw_input environment
# 4.3.1.43 load readline in monaltoolbox for raw_input
# 4.3.1.42 short repr for multimodel
# 4.3.1.41 update valuequestion to understand "y" as default
# 4.3.1.40 update yesnoquestion for "hit any key to quit"
# 4.3.1.39 add forceyes in monaltoolbox.yesnoquestion and forcedefault in monaltoolbox.valueQuestion
# 4.3.1.38 OK dll model 
# 4.3.1.36 fix bug in 
# 4.3.1.35 move datasource.py from GM//************///
# 4.3.1.34 fix bug de getConfiguration dans les codes C 
# 4.3.1.33 fix bug de moduletype dans les codes C (;)
# 4.3.1.32 introduction de moduletype dans les codes C
# 4.3.1.31 transfert de getFrame dans excelsource
# 4.3.1.30 utilisation de ctypes.create_string_buffer avec dim+1 tjs
# 4.3.1.29 remise libmonal.a
# 4.3.1.28 debug install
# 4.3.1.26 add extra_preargs in monal/util/utils.compile_lib
# 4.3.1.25 debug install
#   .
#   .
#   .
# 4.3.1.13 debug install
# 4.3.1.12 suppress libmonal.a de l'install
# 4.3.1.11 -fPIC option suppressed for monal.a lib
# 4.3.1.10 library prefix 'lib' in linux
# 4.3.1.9  fix -fPIC option in lib compile for installation
# 4.3.1.8  fix -fPIC option in module compile (necessary for ubuntu)
# 4.3.1.7  sprintf "" fixed in interfacetrainingdll.c
# 4.3.1.6  mise au pt creation modele serie pour ubuntu
# 4.3.1.5  'jurgb.txt''jurfr.txt''licgb.txt''licfr.txt'
# 4.3.1.3  GetJurComment lower in codewriter. 'jurgb.txt''jurfr.txt''licgb.txt''licfr.txt'
# 4.3.1.2  fix monaltoolbox bug
# 4.3.1.1  adapt to gm api demo + install requires
# 4.3.1.0  adapt to gm api demo
# 4.3.0.1  create test libmanager
# 4.3.0.0  retour calcul delta sh separe de delta rank
# 4.2.0.6
# 4.2.0.5  OK with GM
# 4.2.0.4  separatikon des tests
# 4.2.0.1  fix bug configfile getappliconfig getapplidatabase 
# 4.2.0.0  OK auto upgrade
# 4.1.1.57 add "--user" if is User in install
# 4.1.1.56 remove --user option when virtual
# 4.1.1.55 fix bug in util.utils.getancestor
# 4.1.1.53 test new upgrademgr

# 4.1.1.52 test new upgrademgr
# 4.1.1.51  upgrade isVirtual and GetFile for iMac
# 4.1.1.49  cosmetic in debug file
# 4.1.1.48  cosmetic in debug file
# 4.1.1.46  cosmetic in debug file
# 4.1.1.44  introduce date and version in debug file
# 4.1.1.43  introduce date and version in debug file
# 4.1.1.41  modif to "--debug" setup option
# 4.1.1.40  modif to "debug" setup option
# 4.1.1.39  ajout de --debug option
# 4.1.1.36  mise au point setup - debug=0

# 4.1.1.19  extend graphmachineconstant.getfile

#  4.1.1.0  suppress call to exports sybol in dll compiling
#  4.1.0.3  move monal.a creation from gra^hmachine install to monal install
#  4.1.0.2  move monal.a location to monal.lcode and create it during installation
#  4.1.0.1  move sqlite_numpy.py from graphmachine.component to monal.util
#  4.1.0.0  OK version release 16/06/2016
#  4.0.0.33 random seed again
#  4.0.0.32 randaom seed in parallel jobs while computing LOO
#  4.0.0.31 OK multitrain, localtrain
#  4.0.0.30 OK multitrain
#  4.0.0.29 OK multitrain
#  4.0.0.28 le 07/06/2016
#  4.0.0.27 le 06/06/2016
#  4.0.0.26 05/06/2016
#  4.0.0.25 pb de Pypi
#  4.0.0.24 fix delta sh avec early hii sum
#  4.0.0.23  fix C code training
#  4.0.0.22  after register version de reference
#  4.0.4.21 fix CChar in module names
#  4.0.4.20 test upgrade
#  4.0.4.19 test upgrade
#  4.0.4.18 fix small bugs
#  4.0.4.17 getapplibase extended in util.utils
#  4.0.4.15 add specifiers in setup.py
#  4.0.4.13 change download_urls in setup.py
#  4.0.4.12 test PyPI upload
#  4.0.4.9  new console interface for gm  
#  4.0.4.8  create CRITERION_TYPE_STR in monalconst
#  4.0.4.7
#  4.0.4.6  
#  4.0.4.4  work on event management
#  4.0.4.3  cleaning dialogs
#  4.0.4.2  multitrain management of training failure
#  4.0.4.1  multitrain proptect from writer None
#  4.0.4.0  cosmetic
#  4.0.3.7  reorganize modelcontainer
#  4.0.3.6  OK El Capitan + XCode 7.3
#  4.0.3.5  fix CCharsOnly bug
#  4.0.3.4  adapt to GM 3.0.0.3 & 4
#  4.0.3.3  adapt to GM 3.0.0.2
#  4.0.3.2  adapt to GM 3.0.0.1
#  4.0.3.1  introducing P-Train
#  4.0.2.43 
#  4,0,2,42 fix LOO bugs
#  4.0.2.41 fix network display with alternate columns
#  4.0.2.40 
#  4.0.2.39 
#  4.0.2.38 intro py 2app
#  4.0.2.37 fix install
#  4.0.2.36 Separation __init__.py et version.py
#  4.0.2.35 NoSectionError  
#  4.0.2.34 add FileConfifParser
#  4.0.2.33 version commune P2/P3
#  4.0.2.31 en cours
#  4.0.2.30 setup epure
#  4.0.2.29 maxworkers 0
#  4.0.2.28 modif import concurrent.fu tures
#  4.0.2.27 maxworkers programmable
#  4.0.2.25 trainBS selection upgrade
#  4.0.2.24 fix memory leak with np.load
#  4.0.2.23 fix memory leak with np.load
#  4.0.2.22 fix multiLOO sort bug
#  4.0.2.21 en cours super train
#  4.0.2.20 multiLOO
#  4.0.2.19 track on node.deleteLink consequences
#  4.0.2.18 track on node.deleteLink consequences
#  4.0.2.17 node.deleteLink fixed
#  4.O.2.16 fix training display 
#  4.0.2.15 modif DISPFIELDNAMES
#  4.0.2.14 toolbox raw(str)
#  4.0.2.13 noms accentues
#  4.0.2.11 iso multiple
#  4.0.2.10 fix non ASCII char in model names in C code
#  4.0.2.9 fix iso bug
#  4.0.2.8 annotation folles
#  4.0.2.7 
#  4.0.2.6 formula
#  4.0.2.5 fix LOO inittype
#  4.0.2.4 fix charge vs grade et garde vs ring
#  4.0.2.3 bugs
#  4.0.2.2 fix iso bug
#  4.0.2.0 ajout gestion des modeles dans GM
#  4.0.1.9 integration getPRESS
#  4.0.1.8 process interrupt, OK Bootstrap
#  4.0.1.7 large database with smiles beginning with "(" 
#  4.0.1.6 Bug init random LOO OK
#  4.0.1.5 Test sur les sommes des hii pour la selection de modele
#  4.0.1.4 Multiinit LOO with PRESS selection
#  4.0.1.3 multinit for LOO
#  4.0.1.2 creating modules shorten
#  4.0.1.1 loading single modules too long fixed
#  4.0.1   LOO bug fixed
#  4.0.0a3 LOO bug fixed almost
#  4.0.0a2 
#  4.0.0a1 small bugs
#  4.0.0a0 OK first parallel
#  3.3.2.x dans la branche referenceGM
#  3.3.2.0 OK avant parallel
#  3.3.1a14 fix bug memWeight for trainBS-LOO
#  3.3.1a13 fix bug on interfacetraindll.c getCost
#  3.3.1a12 calcul des LOOleverages
#  3.3.1a11 apprentissages special avec poids de depart specifie
#  3.3.1a10 fix auto update
#  3.3.1a9 fix bug test set
#  3.3.1a8 supp les install_requires dans le setup.py
#  3.3.1a7 mise a jour auto
#  3.3.1a6 inclusion directe des *.c dans les modules d'apprentissage
#  3.3.1a5 securisation de "mathplus.c" et "nttoolbox.c"
#  3.3.1a4 amemioration de "restart" dans monal.util.utils.py : impression des params
#  3.3.1a3 affinement apres update
#  3.3.1a2 ajout de "restart" dans monal.util.utils.py
#  3.3.1a1 alignement sur la sous version de graphmachine (premiere sous version avec le chaeck for update complet)
#  3.3.1a0 deplacement des info codeversion vers les procedures d'initialisation
#  3.3.0a8 ajout codeversion
#  3.3.0a7 corr bug usage multi  -> non pour leverage
#  3.3.0a6 corr bug usage multi
#  3.3.0a5 en usage, leverage par methode monari
#  3.3.0a4 config auto
#  3.3.0a3 fusion de la cr√©ation de modele et de l'enregistrement du code C; destruction rapide des modeles en memoire et remplacement par des leurres
#  3.3.0a2 accompagne GM 1.3.0a2
#  3.3.0a1 dans utyil/utils/getapplicfg, recopie du fichier cfg s'il est plus vieux que la candidat model
#  3.3.0a0 Utilisation des modules dll aussi pour mod√®les simples
#  3.2a05  Sauvegarde modules container en dll
#  3.2a04  Use train.c in library
#  3.2  Use abstract compilers for saving in python module format
#  3.1  OK pout GM 1.0
#  3.0

__version__ = "%d.%d.%d.%d" % (VERSION_MAJOR, VERSION_MINOR, VERSION_MAINTENANCE, VERSION_BUILD)  
VERSION3 = "%d.%d.%d" % (VERSION_MAJOR, VERSION_MINOR, VERSION_MAINTENANCE)
VERSION2 = "%d.%d" % (VERSION_MAJOR, VERSION_MINOR)
try:
    if TAG:
        __version__ = "{0}.{1}{2}".format(VERSION3, TAG, VERSION_BUILD)
except: pass
version = lambda : __version__

def distname(path="", ext=".tar.gz"):   
    import os
    st = "monal-%s%s"% (__version__, ext)
    if len(path):
        st = os.path.join(path, st)
    return st

if __name__ == "__main__":
    print(__version__)
