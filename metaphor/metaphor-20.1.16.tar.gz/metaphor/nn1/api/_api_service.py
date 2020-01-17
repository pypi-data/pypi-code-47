
'''Created on 13 déc. 2018

@author: jeanluc
metaphor.nn1.api._api_service
'''
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import os, sys, stat, time
from importlib import import_module
import json
from configparser import ConfigParser
import functools as ft
from random import choice
from string import ascii_uppercase
from six import text_type
from collections import defaultdict, OrderedDict
# import shutil
from argparse import ArgumentParser, FileType
import platform
import numpy as np
from scipy import __version__ as scipyversion
from pandas import DataFrame, ExcelWriter, __version__ as pandasversion
from openpyxl import __version__ as openpyxlversion
from xlrd import __VERSION__ as xlrdversion
from sqlite3 import connect as sqlconnect, Connection as sqlConnection, \
    PARSE_DECLTYPES as sqlPARSE_DECLTYPES, \
    OperationalError as sqlOperationalError
# from concurrent.futures import as_completed, \
#     ProcessPool Executor as Pool Exec

import metaphor as mp
# from ...version_nntoolbox import __version__ as nntoolboxversion
from ...nntoolbox import hookable
from ...nntoolbox.constants import nobarverb, USE_LIB_FOR_TEST 
import metaphor.nntoolbox.utils
from ...nntoolbox.utils import doNothing, getListFromStr, isIntList,\
    IDformat, roundoff_format, defaultvalue, float_format, \
    isIntBase, isInt, unquote, make_extern, make_intern, \
    get_decimal_size, getSqlFileNameFromConf, strintlist, isFloat, \
    tableTemplate, estimatedstr, leveragestr, set2Float, testresidualstr, \
    trainresidualstr, targetstr, meanstr,  moleculestr, deepenlist, \
    updateDict, make_neutral, intersection, coherencetraintest, rindex 
from ...nntoolbox.utils import debugDict, RE_NONE, RE_LOO, BSGROUP, \
    RE_SUPER, DEMO_DEBUG_ANALYSIS, DEMO_DEBUG_PROGRESS, DEMO_DEBUG_MODEL, \
    DEMO_DEBUG_DISPLAY_1, DEMO_USAGE_NO_LIB, DEMO_DEBUG_USAGE, \
    DEMO_USE_EXISTING, DEMO_DEBUG_TRANSFER, DEMO_DEBUG_COST, \
    DEMO_DEBUG_PRESS, DEMO_DEBUG_JACOBIAN, DEMO_DEBUG_PARALLEL, \
    DEMO_DEBUG_FOLDER, DEMO_DEBUG_OPTIONS, DEMO_DEBUG_ALL, \
    OPTION_WARN_AND_STOP, OPTION_NO_ERROR, OPTION_STOP, \
    OPTION_DISPLAY_FILE_AND_STOP, OPTION_WARN_AND_ASK, DEMO_DEBUG_DEMO
from ...monal.util.sqlite_copy_db import copy_table
from ...nntoolbox.sqlite_numpy import createTableDb, cleanTableDb, getDataFrame, \
    getTableCountFromDb, getTableListFromDb, insertDataToDb
from ...nntoolbox.filetoolbox import getReducedSelectedGmx, \
    decorfile, arg_file_parse, option2Arguments, IndexFilename, \
    getDictFromGmx, removemodule, getGmxFileName, setEnvironFromFile
from ...nntoolbox.modelutils import TransferModel, getModelDictFromConfig, \
    getGmxFileAndSave, stdTable, roundOffTestStr, \
    paramStartStr, paramEndStr, dispStr, epochsStr, getModelDict
import metaphor.nntoolbox.excelutils as exu
from ...nntoolbox.excelutils import multiRangesType, simpleRangeType,\
    initiateExcelWriter, enrichRecapExcelFile, enrichSimpleSheet, getSheet, \
    getVbaProjectBin
from ...nntoolbox.configparsertoolbox import defaultedConfigParser, \
    getDefaultedConfigParser
from ...nntoolbox.progress import FanWait, Progress_tqdm
from ...nntoolbox.cmd_line_dialogs import choiceQuestion, \
    valueQuestion, yesNoQuestion, chooseFields
import metaphor.nntoolbox.utils as utils
from ...nntoolbox.utils import toPrint, orderedIndexes, getModuleVersionList
#from ...nntoolbox.lineartoolbox import randomProbe  
from ...nntoolbox.datareader.fileInspect import inspectFile
from ...nntoolbox.datareader.modeldataframe import get_modelDataframe
from ...nntoolbox.datareader.datasource import DataSource
from ...nntoolbox.datareader.excelsource import getFrame, gettitles, \
    getcustomproperty, getcustomproperties, getFrameFromExcel

from ...monal import __version__ as monalversion, monalconst as C
from ...monal.util.utils import CCharOnlys, getapplidatabase, \
    getLibExt as libExtension, appdatadir
from ...monal.util.toolbox import _linkstr, make_dir, setTrainingActionParams
from ...monal.util.monaltoolbox import debugOutput
from ...monal.modelutils import loadModule
from ...monal.monalrecords import ModelData
from ...monal.driver import Driver, DriverLib, DriverMultiDyn, \
    onSpecialResult, onEndIter, onReturnResult
from ...monal.library.libmanager import moduleType
from ...monal.model import Network, ModelLib
from ...monal.lcode.codeconst import __version__ as codeversion

from ...version import __version__ as metaphorversion
##from ...nntoolbox.filetoolbox import setEnvironFromFile
# from filetoolbox import setEnvironFromFile

ADDPATH = os.environ.get("ADDPATH", "")
ADDPATHLIST = ADDPATH.split(':')
sys.path.extend(ADDPATHLIST)

dialogdefaults = {
    'action': {
        'save_argfile': 1,
        'run_new_project': 1,
        'continue': 1,
        'continue_anyway': 1,
        'run_test': 1,
        'check_bootstrap': 1,
        'check_LOO': 1,
        'hidden': {},
        },
    'data': {
        'add_test': 1,
        'same_file': 1,
        'same_struct': 1,
        'identifiers': 0,
        'inputs': 'from0',  #0, from0, toLast, last, -1
        'outputs': 'last',  # 0, last
        'switch2gm': 1,
        'add_group': 'n',   #default = 'n'  # ou "y" ????
        'check_data': 'n',
        'hidden': {},
        },
    'model': {
        'classif': 0,
        'hidden': {
            'classif': 1,
            }
        },
    'train': {
        'check': 1,
        'hidden': {},
        },
    }

unuseddebuglist = ['run']    
modulesticker = "NN"
availablemode = ['nn']
modeconfigdict = {'nn': {}}
groupavailables = {
    'unknown': {
        'identifiers': 0,
        'inputs': 1,
        'outputs': 2,},
    'nn': {
        'identifiers': 0,
        'inputs': 1,
        'outputs': 2,},
    }
grouptypes = {
    'identifiers': 'any',
    'inputs': 'numerical',
    'outputs': 'numerical',
    }
groupdefault = ['inputs', 'outputs']
add_arg_list = []

class nn1Error(Exception):
    pass

class nn1ReadError(Exception):
    pass

debug = 0

debugdemo = 0
debugoptions = 0
debugfolder = 0
debugAnalyse = 0
debugprogress = 0
debugModel = 0
debugDisplay = 0
debugTransfer = 0
debugJacobian = 0
debugCost = 0
debugPRESS = 0
debugParallel = 0
skipCreateModel = 0
debugUsage = 1

demodebug = 0
if debug:
    if debugAnalyse:
        demodebug |= DEMO_DEBUG_ANALYSIS
    if debugoptions:
        demodebug |= DEMO_DEBUG_OPTIONS
    if debugdemo:
        demodebug |= DEMO_DEBUG_DEMO
    if debugfolder:
        demodebug |= DEMO_DEBUG_FOLDER
    if debugprogress:
        demodebug |= DEMO_DEBUG_PROGRESS
    if debugModel:
        demodebug |= DEMO_DEBUG_MODEL
    if skipCreateModel:
        demodebug |= DEMO_USE_EXISTING
    if debugDisplay:
        demodebug |= DEMO_DEBUG_DISPLAY_1
    if debugTransfer:
        demodebug |= DEMO_DEBUG_TRANSFER
    if debugJacobian:
        demodebug |= DEMO_DEBUG_JACOBIAN
    if debugCost:
        demodebug |= DEMO_DEBUG_COST
    if debugPRESS:
        demodebug |= DEMO_DEBUG_PRESS
    if debugParallel:
        demodebug |= DEMO_DEBUG_PARALLEL
    if debugUsage:
        demodebug |= DEMO_DEBUG_USAGE


applidatapath = getapplidatabase("nn1")

dicoversion = OrderedDict()
dicoversion['platform'] = platform.platform()
dicoversion['python'] = platform.python_version()
for key, module in getModuleVersionList():
    module = __import__(module)
    dicoversion['chem_gm' if key == 'gm' else key] = module.__version__
dicoversion['C code'] = str(codeversion)
dicoversion['numpy'] = np.__version__
dicoversion['scipy'] = scipyversion
dicoversion['pandas'] = pandasversion
dicoversion['openpyxl'] = openpyxlversion
dicoversion['xlrd'] = xlrdversion
  
argumentsdefaultdict = {
    "HELP": 0,
    "VERSION": 0,
    "LICENSE": 0,
    "YES": 1,
    "YESYES": 0,
    "ACTION": 'analyse,preproc',
    "GROUPLIST": "",  #"id,in,out",
    "GROUPCOUNT": "0",
    "SHAREDFOLDER": os.path.expanduser("~/docker"),
    "SORTBY": 'PRESS',
    "LOOSORTBY": 'ID',
    "BSSORTBY": 'PRESS',
    "RESULTTYPE": 'xlsx',
    "MAXREC": "10",
#    "FULLH": 0,
    "HIDDEN": 5,
    'CONFIGSTR': '',
#    'CENTRAL': '',
    'ORIGIN': '',
    'SAVEFOLDER': '',
    'CLASSIF': 0,
    "EPOCHS": 150,
    "INIT": 150,
    "PROBECOUNT": 1000,
    "SEED": -1,
    "DECOR": "t,i,e,s,se,lt,wm",
    "LOOINITTYPE": 2,
    "LOOINITCOUNT": 100,
    "LOOEPOCHS": 150,
    "LOOMAXREC": 1,
    "LOOLEVTHRES": 0.0,
    "LEVTHRES": 0.0,
    "BSINITTYPE": 2,
    "BSCOUNT": 250,
    "BSINITCOUNT": 2,
    "BSEPOCHS": 150,
    "PREPROCTYPE": "",
    "PERTTHRES": 0.5,
    "RDMINIT": 0.1,
    "RNDTHRES": 1E-4,
    "FORCEMODEL": 0,
    "VERB": 3,
    "CALLER": 0,
    'LIBUSE': 0,
    'TIMER': 0,
    'MODERATE': 0,
    'EXCELNUMFORMAT': "0.000",  #FORMATNUM
    'TERMINALNUMFORMAT': "6.3f"
#    "DEBUG": 0,
    }

groupdict = {
    'inputs':'inputs',
    'in': 'inputs',
    'outputs': 'outputs',
    'out': 'outputs',
    'identifiers':'identifiers',
    'id':'identifiers',
#    'smiles': 'smiles',
    }

reverseDecorDict = {
    'mode': 'm',
    'inputs': 'i',
    'i': 'i',
    'traincount':'t',
    't': 't',
    'seed': 'se',
    'se': 'se',
    'selectedcount': 's',
    's': 's',
    'hidden': 'n',
    'n': 'n',
    'levthresh': 'lt',
    'loo': 'l',
    'l': 'l',
    'hash': 'h',
    'h': 'h',
    epochsStr: 'e',
    'e': 'e',
    'confstr': 'c',
    'c': 'c',
    'bootstrap': 'b',
    'b': 'b',
    'moderation': 'wm',
    'wm': 'wm',
    }

basicDecorDict = {
        'B': 'bootstrap',
        'b': 'bootstrap',
        'C': 'confstr',
        'c': 'confstr',
        'E': epochsStr,
        'e': epochsStr,
        'H': 'hash',
        'h': 'hash',
        'L': 'loo',
        'l': 'loo',
        'LT': 'levthresh',
        'lt': 'levthresh',
        'M': 'selectedcount', # pour compatibilite ascendante
        'm': 'selectedcount', # pour compatibilite ascendante 
        'N': 'hidden', 
        'n': 'hidden', 
        'S': 'selectedcount', 
        's': 'selectedcount', 
        'SE': 'seed',
        'se': 'seed',
        'SS': 'selectedcountex', 
        'ss': 'selectedcountex', 
        'T': 'traincount', 
        't': 'traincount', 
        'i': 'inputs',
        'm': 'mode',
        'wm': 'moderation',
        }


def addTest(options, defaultindex, searchdir, candidates=[], ranges=[], commonFieldExclude=True, doprint=None):
    dotestanalysis = 'analyse' in options.actionlist and (options.testfields != options.datafields)        
    optionstest = options.test
    forcedefault=options.yesyes
    verbose = options.verbose
    usesamefile = False
    valdef = int(dialogdefaults['data']['add_test'])
    notest = not yesNoQuestion("Will you add a test ?", valdef, printMessage="Test", forcedefault=forcedefault, doprint=doprint)
    if not notest:
        valdef = int(dialogdefaults['data']['same_file'])
        usesamefile = yesNoQuestion("Use the same file for test ?", valdef, forcedefault=forcedefault, doprint=doprint) 

    if not notest:
        if usesamefile:
            options.test = ""                    
        else:
            options.test, indextest = _getDockerDataFile(optionstest, 
                searchdir=searchdir, candidates=candidates, datakind='testfile',
                defaultindex=defaultindex, forcedefault=forcedefault, doprint=doprint)
    
    options.notest = notest
    #options.testfield = 
    testChecking(options, dotestanalysis, ranges, commonFieldExclude, forcedefault, doprint, verbose)
#    return optionstest, notest#, usesamefile

# def getModuleVersionList():
#     filelist = []
#     apppath = os.path.dirname(mp.__file__)
#     if not apppath in sys.path:
#         sys.path.insert(0, apppath)
#     if not "" in sys.path:
#         sys.path.insert(0, "")
#     for val in sys.path:
#         if val.endswith('metaphor'):
#             for (dirpath, _, filenames) in os.walk(val):
#                 filelist.extend([os.path.join(dirpath, val) for val in filenames if val.startswith('version') and val.endswith(".py")])
#                 break
#     lst = []
#     for filename in filelist:
#         name = os.path.splitext(os.path.basename(filename))[0]
#         namelst = name.split('_')
#         if len(namelst) > 1:
#             key = namelst[-1]
#         else:
#             key = 'metaphor'
#         lst.append((key, name))
#     return lst

def getServicesList():
    filelist = []
    apppath = os.path.dirname(mp.__file__)
    if not apppath in sys.path:
        sys.path.insert(0, apppath)
    if not "" in sys.path:
        sys.path.insert(0, "")
    for val in sys.path:
        if val.endswith('metaphor'):
            for (dirpath, _, filenames) in os.walk(val):
                filelist.extend([os.path.join(dirpath, val) for val in filenames if val.startswith('services')])
                break
    return filelist

@hookable.onlyonce
def linkToServices(file=sys.stdout, nn1serv=None):
    def doprint(*args, **kwds):
        if not file is None:
            print(*args, **kwds, file=file)
    
    doprint("\n{}".format(time.strftime("%c")))
    serviceslist = getServicesList()
    for service in serviceslist:
        doprint(service)
        config = ConfigParser()
        config.optionxform = str
        with open(service) as ff:
            config.read_file(ff)
        pth = config.get('module', 'path')
        mname = config.get('module', 'name')
        
        #sticker = config.get('module', 'sticker')
        fullname = "{}.{}".format(pth, mname)
 #       if 
        try:
            newmodule = import_module(fullname)  #, fromlist=[None])
        except Exception as err:
            print(err)
            continue
        sticker = newmodule.modulesticker.lower()
        doprint("sticker: {}".format(sticker))
        doprint("imported module: {}".format(newmodule))
        availablemode.append(sticker)
        section = 'addkeytodict'
        if section in config.sections():
            doprint(section)
            for option in config.options(section):
                lst = config.get(section, option).split(',')
                for ind0 in range(0, len(lst), 2):
#                     key, source = config.get(section, option).split(',')
                    key = lst[ind0].strip()
                    source = lst[ind0+1].strip()
                    target = getattr(sys.modules[__name__], option)
                    sourceObj = getattr(newmodule, source)
                    if key in target and isinstance(sourceObj, dict):
                        target[key].update(sourceObj)
                    else:
                        target[key] = sourceObj
                    doprint("\t", option, source, target)
        section = 'updatedict'
        if section in config.sections():
            doprint(section)
            for option in config.options(section):
                target = getattr(sys.modules[__name__], option)
                source = config.get(section, option)
                target.update(getattr(newmodule, source))
                doprint("\t", option, source, target)
        section = 'inserttolist'
        if section in config.sections():
            doprint(section)
            for option in config.options(section):
                lst = getattr(sys.modules[__name__], option)
                insertlist = config.get(section, option).split(',')
                for tpl in insertlist:
                    value, index = tpl.split(':')         
                    index = int(index.strip())
                    lst.insert(index, value.strip())
                doprint("\t", option, lst, insertlist)
        section = 'delfromlist'
        if section in config.sections():
            doprint(section)
            for option in config.options(section):
                lst = getattr(sys.modules[__name__], option)
                todel = config.get(section, option)
                index = lst.index(todel)
                lst.pop(index)
                doprint("\t", option, lst, todel)
        section = 'extendlist'
        if section in config.sections():
            doprint(section)
            for option in config.options(section):
                targetlst = getattr(sys.modules[__name__], option)
                toappend = config.get(section, option)
                targetlst.extend(getattr(newmodule, toappend))
                doprint("\t", option, targetlst, toappend)
        section = 'appendtolist'
        if section in config.sections():
            doprint(section)
            for option in config.options(section):
                targetlst = getattr(sys.modules[__name__], option)
                toappend = config.get(section, option)
                targetlst.append(getattr(newmodule, toappend))
                doprint("\t", option, targetlst, toappend)
        section = 'hooks'
        if section in config.sections():
            doprint(section)
            for option in config.options(section):
                source = getattr(sys.modules[__name__], option)
                sourcename = config.get(section, option)
                target = getattr(newmodule, sourcename)
                doprint("\t", source, option, target)
                source.addhook(sticker, target)
        section = 'replaces'  
        if section in config.sections():
            doprint(section)
            for option in config.options(section):
                source = getattr(sys.modules[__name__], option)
                sourcename = config.get(section, option)
                target = getattr(newmodule, sourcename)
                doprint("\t", source, option, target)
                setattr(sys.modules[__name__], option, target)
          
#createSpecialModel = None
# # decorator for initiate sqlconnect
def connectMgr(func):
    """Decorator for sql connected functions.
    If function first parameter is a sql connection, then return the original function.
    Otherwise, if first parameter is a filename of a db registry, the connection 
    to this registry is open, then the original function is called with this connection as first parameter, and then the connection is closed.
    """
    #from functools import wraps
    @ft.wraps(func)
    def inside_func(*args, **kwargs):
        if not isinstance(args[0], str):
            return func(*args, **kwargs)
        with sqlconnect(args[0], detect_types=sqlPARSE_DECLTYPES) as dbConnect:
            res = func(dbConnect , *args[1:], **kwargs)
        return res
    return inside_func
     
class monalError(Exception):
    pass

def defaultCfg(mode="nn", addtrain=True):   
    """Creation of the default configuration parser.
    
    Parameters:
     - excluded -> sections to exclude
     - mode -> 'nn' or 'gm'
    """
    config = defaultedConfigParser() 
    try:
        modedico = modeconfigdict[mode]
    except KeyError:
        lst = list(modeconfigdict.keys())
        lst = ['"{0}"'.format(val) for val in lst]
        mark = ", ".join(lst)
        mess = "Error in mode. Mode should be in [{0}]".format(mark)
        raise nn1ReadError(mess)
    sectionlist = ["general", "model", "private"]
    if addtrain:
        sectionlist.insert(2, "training")
    if 'add_section' in modedico:
        res = modedico['add_section']
        if isinstance(res[0], tuple):
            for val in res:
                sectionlist.insert(val[0], val[1])
        else:
            sectionlist.insert(*res)
    for section in sectionlist:
        config.add_section(section)
        
    if 'add_set' in modedico:
        res = modedico['add_set']
        if isinstance(res[0], tuple):
            for val in res:
                config.set(*val) 
        else:
            config.set(*res)        
    config.set("general", "simpledispersion", "False")
    config.set("general", "verbose", "0")
    config.set("model", "compiler", "")
    config.set("model", "hidden", "0")
    config.set("private", "keeptemp", "")
    config.set("private", "moduletype", "dll")
    return config 

def checkSingleInputField(modeldataframe, typeDict, inputsindex, ind, inputname, mode, forcedefault, doprint, debug):
    if typeDict[inputname] == str:
        
        if (not mode == 'unknown') and (mode == 'nn' or not 'smiles' in groupavailables.get(mode)):
            return False, mode
        mess = "Input field '{0}' has string type.\n\tWill you switch to Graphmachine engine ?".format(inputname)
        valdef = dialogdefaults['data']['switch2gm']
        accept = (mode == 'gm') or yesNoQuestion(mess, valdef, forcedefault=forcedefault, doprint=doprint)
        if accept:
            smilesfield = modeldataframe.dataFields[inputsindex].pop(ind)
            if not 'smiles' in modeldataframe.dataGroups:
                modeldataframe.dataGroups.insert(0, 'smiles')
                modeldataframe.dataFields.insert(0, [])
            modeldataframe.dataFields[0].append(smilesfield)
            mode = 'gm'
#         first = False

    if [] in modeldataframe.dataFields:
        emptyindex = modeldataframe.dataFields.index([])
        modeldataframe.dataFields.pop(emptyindex)
        modeldataframe.dataGroups.pop(emptyindex)
    return True, mode

def CheckInputTypes(filename, datarange, datafields, datagroups, 
        filetype='', mode='unknown', forcedefault=False, doprint=doNothing, debug=0):
    #print("groupavailables", groupavailables)
    drop = ('identifiers' in datagroups) and not datagroups.index('identifiers') and (len(datafields[0]) == 1)
    modeldataframe, titlelist, indexdict = get_modelDataframe(filename, datarange, datafields, 
        datagroups, filetype=filetype, drop=drop, withindexdict=True)  #, sheetname=None, indexfield=-1, drop=False)
    typeDict = modeldataframe.dtypes
    outlist = list(modeldataframe.fieldsOf('outputs'))
    for outputname in outlist:
        if typeDict[outputname] == str:
            raise nn1Error("Outputs must be numeric")
    badfields = []
#     if mode == 'unknown':
#         if 'smiles' in modeldataframe.dataGroups:
#             mode = 'gm'
#         else:            
#             mode = 'nn'
    if 'inputs' in modeldataframe.dataGroups:
        inlist = list(modeldataframe.fieldsOf('inputs'))
        inputsindex = modeldataframe.dataGroups.index('inputs')
#         first = True
        for ind, inputname in enumerate(inlist):
            OK, mode = checkSingleInputField(modeldataframe, typeDict, 
                inputsindex, ind, inputname, mode, forcedefault, 
                doprint, debug)
            if not OK:
                badfields.append(inputname)
        if mode == 'unknown':
            mode = 'nn'
        modeldataframe._datacounts = [len(val) for val in modeldataframe.dataFields]
        if drop:
            datafields = [datafields[datagroups.index('identifiers')]] + [[indexdict[val] for val in lst] for lst in modeldataframe.dataFields]
            datagroups = ['identifiers'] + modeldataframe.dataGroups
        else:
            datagroups = modeldataframe.dataGroups
            datafields = [[indexdict[val] for val in lst] for lst in modeldataframe.dataFields]

    if mode == 'unknown':
        if 'smiles' in modeldataframe.dataGroups:
            mode = 'gm'
        else:            
            mode = 'nn'
    return modeldataframe, datafields, datagroups, mode, badfields, titlelist

def _checkGroupList(mode, grlist=[], groups=[],  doprint=None, forcedefault=False, verbose=1):
    if len(groups):
        if not len(grlist):
            return groups
    else:
#        groupavail = groupavailables.get(mode)
        default = groupavailables['unknown']
        groups = groupavailables.get(mode, default)  #groupavailables
    extralist = [val for val in groups if val not in grlist]
#     if len(extralist):
#         st = "group list is ({0}). you may add new items".format(",".join(grlist))
#         doprint(st, verbose=verbose)
    change = False
    for val in extralist:
        mess = "Will you have '{0}' data ?".format(val)
#         mess = "add '{0}' to the field group list?".format(val)
        printMessage = "adding '{0}'".format(val)
        # mettre ici une recherche de la reponse par defaut la plus pertinente
        valdef = dialogdefaults['data']['add_group']
        accept = yesNoQuestion(mess, default=valdef, printMessage=printMessage, doprint=doprint, 
                outfile=None, forcedefault=forcedefault, verbose=verbose)
        if accept:
            change = True
            grlist.append(val)
    #grlist.sort(key=lambda x:groups[x])
    if change:
        st = "group list is now ({0})".format(",".join(grlist))
        doprint(st, verbose=verbose)
     
    return grlist
 
def _checkFile(filename, excluded=[], datafor='train', datarange="", indexdefault=0, forcedefault=False, 
        doprint=doNothing, verbose=1):
    res = inspectFile(filename, forceTitles=True)
    dialect = None
    ftype = res[0]
    if ftype in multiRangesType:
        rangeRichList = [val for val in res[1:] if not val[0].startswith('_')]
        ranges = ["_" if val[0] in excluded else val[0] for val in rangeRichList]
        if datarange in ranges:
            indexdefault = ranges.index(datarange)
        sizes = [val[1] for val in rangeRichList]
        titleslist = [val[3] for val in rangeRichList]
        promptlst = ['Availables ranges for {0}:'.format(datafor)]
        for ind, (value, size, titles) in enumerate(zip(ranges, sizes, titleslist)):
            if not value.startswith("_"):
                lst = ['\t', text_type(ind), str(value), '\tfields:', text_type(titles), '\t', text_type(size), 'lines']
                promptlst.append(" ".join(lst))
        promptlst.append("Please choose {0} source range by its index [{1}] ?".format(datafor, indexdefault))
        mess = "\n".join(promptlst)
        printMessage = "Chosen {0} range:".format(datafor)
        datarange = choiceQuestion(mess, ranges, indexdefault, printMessage, 
            returnType=str, doprint=doprint, forcedefault=forcedefault,
            verbose=verbose)
        if datarange is None:
            return ftype, None, None, None, None 
        titles = titleslist[ranges.index(datarange)]
    else:
        ranges = []
        ftype, size, titleFirst, titles, dialect = res  
        promptlst = []
        promptlst.append('Availables for {0}:'.format(datafor))
        lst = ['\tfields:', str(titles), '\t', str(size), 'lines']
        promptlst.append(" ".join(lst))
        promptlst.append("Accept these data for {0} [y] ?".format(datafor))
        mess = "\n".join(promptlst)
        accept = yesNoQuestion(mess, default='y', printMessage="", 
            doprint=doprint, forcedefault=forcedefault, verbose=verbose)
        if not accept:
            return ftype, None, None, None, None
    return ftype, datarange, titles, ranges, dialect

def _CheckTrainingParameters(options, doprint=None, verbose=1, forceyes=False, prefix=""):
    if isinstance(options.multihidden, list) and len(options.multihidden) > 1:
        hiddendefault = ",".join([str(val) for val in options.multihidden])
    else:
        hiddendefault = str(options.hidden)
    options.hidden = valueQuestion("Enter number of hidden neurons", 
        hiddendefault, "Hidden neurons", doprint=doprint, returnType=str,
        verbose=verbose, forcedefault=forceyes, prefix=prefix)
    options.multihidden = getListFromStr(options.hidden)
    if not isIntList(options.multihidden, True):
        raise ValueError("'{0}' is not a correct hidden value".format(options.hidden))        
    options.initcount = valueQuestion("Enter the number of training run", 
        options.initcount, "Training count", forcedefault=forceyes, 
        prefix=prefix, doprint=doprint,
        verbose=verbose)  
    options.epochs = valueQuestion("Enter the number epochs per run", 
        options.epochs, "Epochs", forcedefault=forceyes, prefix=prefix, 
        doprint=doprint, verbose=verbose) 
    defaultmaxrec = ",".join([str(val) for val in sorted(options.multimaxrec)])
    options.maxrec = valueQuestion("Enter the training use count(s)",
        defaultmaxrec, "Training use count", forcedefault=forceyes, prefix=prefix, 
        returnType=str, doprint=doprint, verbose=verbose)
    options.multimaxrec = getListFromStr(options.maxrec)
    if not isIntList(options.multimaxrec, True):
        raise ValueError("'{0}' is not a correct training use value".format(options.maxrec))        
    options.seed = valueQuestion("Enter a random seed (-1 for no seed)", 
        options.seed, "Seed", forcedefault=forceyes, prefix=prefix, 
        doprint=doprint, verbose=verbose, returnType=int)
    options.initstddev = valueQuestion("Enter random weights initialization standard deviation", 
        options.initstddev, "Envelope", forcedefault=forceyes, prefix=prefix, 
        doprint=doprint, verbose=verbose, returnType=float)
    options.roundthreshold = valueQuestion("Enter computing error threshold", 
        options.roundthreshold, "Computing error threshold", forcedefault=forceyes, prefix=prefix, 
        doprint=doprint, verbose=verbose, returnType=float)
    options.leveragethreshold = valueQuestion("Enter leverage selection threshold", 
        options.leveragethreshold, "Leverage threshold", forcedefault=forceyes, prefix=prefix, 
        doprint=doprint, verbose=verbose, returnType=float)
    if isinstance(options.decor, text_type):
        defaultdecor = options.decor
    else:
        defaultdecor = ",".join([str(reverseDecorDict[val]) for val in options.decor])
    lst = ["Enter the file decoration choice list (comma separated)."]
    lst.append("Available decorators:")
    lst.append("\tt (traincount)")
    lst.append("\ti (inputcount)")
    lst.append("\te (epochs)")
    lst.append("\ts (selectedcount)")
    lst.append("\tse (seed)")
    lst.append("\tlt (leverage threshold)")
    lst.append("\twm (weights moderation)")
    lst.append("\tb (bootstrap)")
    lst.append("\tl (LOO)")
#     lst.append("\tc (confstr)")
#     lst.append("\th (hash)")
#     lst.append("\tn (hidden)")
#     lst.append("\tss (selectedcountex)")
    lst.append("")
    mess = "\n".join(lst)
    options.decor = valueQuestion(mess, defaultdecor, "File decoration", 
        forcedefault=forceyes, prefix=prefix, returnType=str, 
        doprint=doprint, verbose=verbose)
    if isinstance(options.decor, str):
        options.decor = options.decor.split(",")
    options.decor = [val.strip() for val in options.decor]
    if options.debug & DEMO_DEBUG_OPTIONS:
        print("in _CheckTrainingParameters")
        print("\tdecor", options.decor)

def _CheckLOOParameters(options, doprint=None, verbose=1, forceyes=False, prefix=""):
    initlist = ["start weight", "end weight", "random"]
    options.looinittype = choiceQuestion("Enter the LOO weight initialization type", 
        initlist, options.looinittype, printMessage="LOO weight initialization ", 
        returnType=int, doprint=doprint, forcedefault=forceyes, 
        extradisplay=True, listindexed=True, verbose=verbose)
    options.looinitcount = valueQuestion("Enter the number of LOO initializations",
        options.looinitcount, "LOO initializations", forcedefault=forceyes, prefix=prefix, 
        doprint=doprint, verbose=verbose)
    options.looepochs = valueQuestion("Enter the number of LOO epochs",
        options.looepochs, "LOO epochs", forcedefault=forceyes, prefix=prefix, 
        doprint=doprint, verbose=verbose)
    options.loomaxrec = valueQuestion("Enter the LOO CV use count",
        options.loomaxrec, "LOO CV use count", forcedefault=forceyes, prefix=prefix, 
        doprint=doprint, verbose=verbose)  
    options.loolevthres = valueQuestion("Enter the LOO leverage threshold",
        options.loolevthres, "LOO leverage threshold", forcedefault=forceyes, prefix=prefix, 
        doprint=doprint, verbose=verbose)  

def _CheckBSParameters(options, doprint=None, verbose=1, forceyes=False, prefix=""):
    initlist = ["none", "standard", "residus"]
    options.bootstraptype = choiceQuestion("Enter the bootstrap type", 
        initlist, options.bootstraptype, printMessage="BS type ", 
        returnType=int, doprint=doprint, forcedefault=forceyes, 
        extradisplay=True, listindexed=True, verbose=verbose)
    initlist = ["start weight", "end weight", "random"]
    options.bootstrapinittype = choiceQuestion("Enter the bootstrap weight initialization type", 
        initlist, options.bootstrapinittype, printMessage="bootstrap weight initialization ", 
        returnType=int, doprint=doprint, forcedefault=forceyes, 
        extradisplay=True, listindexed=True, verbose=verbose)
    options.bootstrapinitcount = valueQuestion("Enter the number of bootstrap initializations",
        options.bootstrapinitcount, "Bootstrap initializations", forcedefault=forceyes, prefix=prefix, 
        doprint=doprint, verbose=verbose)
    options.bootstrapepochs = valueQuestion("Enter the number of bootstrap epochs",
        options.bootstrapepochs, "Bootstrap epochs", forcedefault=forceyes, prefix=prefix, 
        doprint=doprint, verbose=verbose)

def _initiate_options(argv=[], proposedOptions=None, hlp=False, debug=0):
    if debug:
        print("sys.path")
        for val in sys.path:
            print("\t", val)
    if hlp:
        argv.append("--help")
    dico = None
    diction, argumentfile, argvv = arg_file_parse(argv, ("@", "--arg_file"), debug=debug) 
    if demodebug & DEMO_DEBUG_DEMO:
        print("retrieve argumentfile", argumentfile)
  
    if isinstance(diction, text_type):
        sys.stderr.write(diction)
    elif diction is not None:
        diction['priority'] = 1
        dico = defaultdict(lambda: None)
        dico.update(diction)
    if argumentfile and not os.path.exists(argumentfile):
        for basepath in os.environ["PATH"].split(":"):
            test = os.path.join(basepath, argumentfile)
            if os.path.exists(test):
                argumentfile = test
                break
    if demodebug & DEMO_DEBUG_DEMO:
        print("located argumentfile", argumentfile)
    if argumentfile and os.path.exists(argumentfile):
        if demodebug & DEMO_DEBUG_DEMO:
            print("call setEnvironFromFile with file", argumentfile)
        setEnvironFromFile(argumentfile)
    if debug:
        print("remaining arguments:", argvv)
        if os.path.exists(argumentfile):
            print("argumentfile: {} do exists".format(argumentfile))
        elif argumentfile:
            print("argumentfile: {} do NOT exists".format(argumentfile))

    if proposedOptions:
        options = proposedOptions
    else:
        options = _getCmdLineOptions(argvv, dico, debug=debug)
    options.arg_file = argumentfile
    if not options.caller and options.sharedfolder == '/host':
        options.sharedfolder = ""
    if debug:
        print("after _getCmdLineOptions")
        for key, val in options.__dict__.items():
            print("\toptions.{0} = {1}".format(key, val))
    if int(options.yes) & 2:
        options.yesyes = True
        options.yes = options.yesyes % 2
    else:
        options.yesyes = False
    if options.weightsmoderation:
        options.trainstyle = C.CS_MODERATE
    else:
        options.trainstyle = 0    
    options.curaction = ""
    options.lastaction = ""
    options.lastactions = []
    return options

def decor2long(decor):
    if decor:
        if decor == "[]":
            decor = []
        else:
            decordic = defaultdict((lambda: ""), basicDecorDict)     
            lst = []
            if not isinstance(decor, (list, tuple)):
                decor = decor.split(',')
            for val in decor:
                dval = decordic[val]
                val = dval if dval else val
                if val:
                    lst.append(val)
            if not "mode" in lst:
                lst.append("mode")
            decor = lst
    else:
        decor = []
    return decor

def _initiate_folders(options, caller): 
    res = True           
    if not caller:  # call by native code
        if hasattr(options, 'sharedfolder') and options.sharedfolder:
            shared = options.sharedfolder
        else:
            shared = '~/docker'
        options.sharedfolder = os.path.expanduser(shared)
        options.targetfolder = os.path.join(options.sharedfolder, 'result')
        options.workfolder = os.path.join(options.sharedfolder, 'workdir')
        options.datafolder = os.path.join(options.sharedfolder, 'data')
        options.argsfolder = os.path.join(options.sharedfolder, 'argsdir')
        
    elif caller == 1 : # call within docker run
        options.sharedfolder = '/host'
        options.targetfolder = os.path.join(options.sharedfolder, 'result')
        options.workfolder = os.path.join(options.sharedfolder, 'workdir')
        options.datafolder = os.path.join(options.sharedfolder, 'data')
        options.argsfolder = os.path.join(options.sharedfolder, 'argsdir')
        
    elif caller == 2 : # call within docker demo
        options.sharedfolder = '/host'
        options.targetfolder = os.path.join(options.sharedfolder, 'result')
        options.workfolder = os.path.join(options.sharedfolder, 'workdir')
        localshared =  os.path.expanduser('~')
        options.datafolder = os.path.join(localshared, 'data')
        options.argsfolder = os.path.join(localshared, 'argsdir')
        
    elif caller == 3 : # call within docker server
        options.sharedfolder = '/host'
        if not os.path.exists(options.sharedfolder):
            options.sharedfolder = '/home/docker'
        options.targetfolder = os.path.join(options.sharedfolder, 'result')
        options.workfolder = os.path.join(options.sharedfolder, 'workdir')
        options.datafolder = os.path.join(options.sharedfolder, 'data')
        options.argsfolder = os.path.join(options.sharedfolder, 'argsdir')
    else:
        res = False
    if not options.datafolder in sys.path:
        sys.path.append(options.datafolder)
    if not options.argsfolder in sys.path:
        sys.path.append(options.argsfolder)
    
    return res

def _initiate_debug(options):
    toprint = ""
    errorcode = OPTION_NO_ERROR
    debugbase = isIntBase(options.debug) # return 0, 8, 10 ou 16
    if debugbase:
        # ici le debug est appele par son code en entier, octal ou hexadecimal
        options.debug = int(options.debug, debugbase)
    elif options.debug and isinstance(options.debug, str):
        # ici le debug est appele par une liste de 
        lst = options.debug.lower().split(',')
        value = 0
        for test in lst:
            if test in debugDict:
                value |= debugDict[test]            
            elif not test.lower() in unuseddebuglist:
                toprint = 'unknown debug option: "%s"\n'% test 
                errorcode |= OPTION_WARN_AND_STOP
                break
        options.debug = value
    return options, toprint, errorcode

def initiate_verbose(options):
    verb = [int(val) for val in str(options.verbose).split(',')]
    if not hasattr(options, "dotimer") or options.dotimer == "0":
        options.dotimer = 0
    if len(verb) == 1:
        options.verbose = int(verb[0]) % 16
        options.verbosexls = int(verb[0]) + 1 // 16
    else:
        options.verbose = int(verb[0])
        options.verbosexls = int(verb[1])
        if len(verb) > 2:
            options.dotimer = int(verb[2])
    return options

def initiate_dialog_defaults(options):
    local = dialogdefaults.copy()
    registered = None
    if os.path.exists(options.sharedfolder):
        diadeffile = os.path.join(options.sharedfolder, 'dialogdefaults.ini')
        if os.path.exists(diadeffile):
            with open(diadeffile, 'r') as read_file:
                try:
                    registered = json.load(read_file)
                    local = updateDict(local, registered)
                except json.decoder.JSONDecodeError:
                    pass
        with open(diadeffile, "w") as write_file:
            json.dump(local, write_file, indent=4)
    return local

def initiate_externpath(options, doprint=None, withdialog=True):
    searchbase = options.sharedfolder
    if not os.path.exists(searchbase):
        return None
    options.externpath = ""
    pthfile = os.path.join(searchbase, 'host.pth')
#     if options.caller == 3:
#         options.externpath = <host>
    if os.path.exists(pthfile):
        with open(pthfile, "r") as ff:
            options.externpath = ff.read().strip()
    elif withdialog:
        forcedefault = options.caller == 3
        mess = """Please give the absolute path of the shared folder in the host?
        (for labelling output files only)"""
        result = valueQuestion(mess, "<host>", "host path", str, doprint=doprint, 
                forcedefault=forcedefault ,verbose=options.verbose)  
        if result:
            options.externpath = result
            try:
                with open(pthfile, 'w') as ff:
                    ff.write(result)
            except: 
                return None
    return options

def _setFileFolders(filename, sharebaselist=[], externbase=""):    
    filename = unquote(filename)
    if not filename:
        return ""
    filename = os.path.expanduser(filename)
    if externbase and filename.startswith(externbase):
        # le nom du fichier est en reference externe: on 
        filename = filename[len(externbase):]
        if filename.startswith('/') or filename.startswith('\\'):
            filename = filename[1:]
    for basedir in sharebaselist:
        test = os.path.join(basedir, filename)
        if os.path.exists(test):
            return test
        for root, dirs, _ in os.walk(basedir):           
            test = os.path.join(root, filename)
            if os.path.exists(test):
                return test
    return filename

def _isSourceFile(filename, exts=[]):
    _, ext = os.path.splitext(filename)
    if len(exts):
        OK = ext in exts
    else:
        OK = ext in [".txt", ".csv"] or (ext.startswith(".xls"))
    return OK
    
def _getDataFileCandidates(searchdir="", exts=[], searchbase=[]):
    candidates = []
    for sdir in searchbase:
        try:
            _, _, files = next(os.walk(sdir))
            candidates = [fil for fil in files if _isSourceFile(fil, exts)] 
        except: pass
        if len(candidates):
            searchdir = sdir
            break
    if not len(candidates) and searchdir and os.path.isdir(searchdir): 
        try:
            _, _, files = next(os.walk(searchdir))
            candidates = [fil for fil in files if _isSourceFile(fil, exts)] 
        except: pass
    return candidates, searchdir

def _getDockerDataFile(filename, searchdir="", candidates=[], 
        datakind="datafile", defaultindex=None, forcedefault=False, 
        doprint=doNothing):  # ca ller=0
    index = None
    if not searchdir:
        pass
#        searchdir = options.folder  #use sharedfolder
        #os.path.join(currentshare(cal ler), "data")
    if not filename:
        try:
            if not len(candidates):
                candidates, searchdir = _getDataFileCandidates(searchdir=searchdir)
            if len(candidates):
                mess = "Search candidates in folder: {0}\n".format(searchdir)
                if datakind:
                    mess += "Will you choose the {0} in the candidate list ?".format(datakind)                    
                    printMessage = "chosen {0} ".format(datakind) 
                else:
                    mess += "Will you choose the datafile in the candidate list ?"
                    printMessage = "chosen datafile "
                res, index = choiceQuestion(mess, candidates,
                    printMessage=printMessage, 
                    returnType=str, listindexed=True, extradisplay=True,
                    defaultindex=defaultindex, fulloutput=True, 
                    forcedefault=forcedefault, doprint=doprint)
                if res:
                    candidate = os.path.join(searchdir, res)
                    if os.path.exists(candidate):
                        filename = candidate
        except: pass
    if not filename:
        return "", -1
    if os.path.exists(filename):
        return filename, index
    test = os.path.join(searchdir, filename)    
    if os.path.exists(test):  
        return test
    ppath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pathlst = ["/data",
               os.path.join(ppath, "api", "demofiles"),
               os.path.join(applidatapath, "demofiles"),
               ]
    for curpath in pathlst:
        test = os.path.join(curpath, filename)    
        if os.path.exists(test):  
            return test, index
    return "", -1  
    
def updateOptionsFromGmx(options, sourcefile):
    if not os.path.exists(sourcefile):
        return
    dico = None
    try:
        dico = getDictFromGmx(sourcefile)
    except nn1ReadError as err:
        try:
            dicoxl = getcustomproperties(sourcefile, "Utilities")
            if "Model file" in dicoxl.keys():
                nnxfile = dicoxl["Model file"]
                nnxfile = make_intern(nnxfile, options)
                dico = getDictFromGmx(nnxfile)
            else:
                pass  # mettre ici la recherche de donnees interessantes dans le dicoxl lui-meme
        except:
            dico = None
    if dico is None:
        return -1
    if epochsStr in dico:
#    if epochsStr in dico.keys():
        options.epochs = int(dico[epochsStr])
    if 'propertyname' in dico:
        options.propertyname = dico['propertyname']
    if 'model' in dico.keys():
        modeldict = dico['model']
        if 'hidden' in modeldict.keys():
            options.hidden = int(modeldict['hidden'])
    if 'training' in dico.keys():
        traindict = dico['training']
        if epochsStr in traindict.keys():
            options.epochs = int(traindict[epochsStr])
        if 'initcount' in traindict.keys():
            options.initcount = int(traindict['initcount'])
        if 'initstddev' in traindict.keys():
            options.initstddev = float(traindict['initstddev'])
        if 'seed' in traindict.keys():
            options.seed = int(traindict['seed'])

def getVersionList(header=[]):
    lst = ["{0}: {1}".format(key, value) for key, value in dicoversion.items() if value]
    if len(header):
        header.extend(lst)
        lst = header
    return lst

# def getContainerVersion(caller=0):
#     basedir = os.path.expanduser(chr(126))
#     if not caller:
#         basedir = os.path.join(basedir, "docker")
#     with open(os.path.join(basedir, "version.txt"), "r") as ff:
#         result = ff.read().strip()
#     return result

def api_options(argv=[], proposedOptions=None, nofile=False, hlp=False, debug=0):  #cal lermodule="nn1", 

    """Options namespace creating or reading from command line,
    
    parameters:
     - argv            -> comand line argument list. Defaulted to empty list.
     - proposedOptions -> suggested option namespace. Defaulted to empty list.
     - searchdir       -> directory where data files are looked for when proposedOptions has no datafile. Defaulted to internal datadir
     - nofile          -> if set to True, the datafile searching is forbidden. Defaulted to False.
     - hlp            -> return a help text for the command line arguments. Defaulted to False.
     
    return: 
     - options         -> options namespace.
     - toprint         -> error message to print or text file to read and print when needed.
     - errorcode       -> error code. 
    Error codes are defined in 'nntoolbox.utils' 
     - OPTION_NO_ERROR = 0
     - OPTION_DISPLAY_FILE_AND_STOP = 1
     - OPTION_WARN_AND_STOP = 2
     - OPTION_WARN_AND_ASK = 4
     - OPTION_STOP = 5
    """
    #debugdemo = demodebug & DEMO_DEBUG_DEMO
    toprint = ""
    errorcode = OPTION_NO_ERROR

    if debug:
        print("argument list:", argv)
# ici on recherche les options telles que lues dans la ligne de 
# commande ou les variables d'environnement
    if demodebug & DEMO_DEBUG_DEMO:
        print("call _initiate_options")
    options = _initiate_options(argv, proposedOptions, hlp, debug=debug)
#     if debug:
#         print("after _initiate_options")
#         for key, val in options.__dict__.items():
#             print("\toptions.{0} = {1}".format(key, val))

# initialisation du debug 
    options, toprint, errorcode = _initiate_debug(options) 
    if  errorcode == OPTION_WARN_AND_STOP:
        return options, toprint, errorcode  
# adaptation des verboses
    options = initiate_verbose(options)

# initialisations des repertoires 
    options.dockercallable = options.caller in [1, 2]
    isdocker = options.caller in [1, 2, 3]
    if not _initiate_folders(options, options.caller):
        toprint = "options error\t unknown caller {}".format(options.caller)
        errorcode = OPTION_STOP
        return options, toprint, errorcode
        
    options.libfolder = os.path.join(options.workfolder, 'lib')
    
    if options.source and not os.path.exists(options.source):
        base = os.path.basename(options.source)
        candidate = os.path.join(options.datafolder, base)
        if os.path.exists(candidate):
            options.source = candidate
    
    if options.test and not os.path.exists(options.test):
        base = os.path.basename(options.test)
        candidate = os.path.join(options.datafolder, base)
        if os.path.exists(candidate):
            options.test = candidate
    
    if options.origin and not os.path.exists(options.origin):
        if hasattr(options, 'resultfolder'):
            resultfolder = options.resultfolder
        else:
            pth = os.path.dirname(options.datafolder)
            resultfolder = os.path.join(pth, 'result')
        base = os.path.basename(options.origin)
        candidate = os.path.join(resultfolder, base)
        if os.path.exists(candidate):
            options.origin = candidate
    
    if not os.path.exists(options.sharedfolder):
        try:
            os.makedirs(options.sharedfolder, 0o777)
            mode = os.stat(options.sharedfolder)[0]
            os.chmod(options.sharedfolder, mode | stat.S_IWOTH | stat.S_IWGRP)  
        except PermissionError: pass  
    if not os.path.exists(options.libfolder):
        try:
            os.makedirs(options.libfolder, 0o777)
        except PermissionError: pass  
#         mode = os.stat(options.libfolder)[0]
#         os.chmod(options.libfolder, mode | stat.S_IWOTH | stat.S_IWGRP)    
# initialisation du printer
    doprint = toPrint(options.outfile)
    
# recherche d'information sur le chemin externe (dans la machine hote)
    options = initiate_externpath(options, doprint)
    if options is None:
        errorcode = OPTION_STOP
        toprint = "Metaphor needs a host folder to be connected to."
        return None, toprint, errorcode
    dialogdefaults = initiate_dialog_defaults(options)
    searchbases = [options.datafolder]

    options.savedir = ""
    options.notest = False
    
    options.dockername = "<docker image name>"
    pth = os.path.expanduser("~/version.txt")
    if os.path.exists(pth):
        with open(pth, "r") as ff:
            options.dockername = ff.read()
    
    if options.debug & DEMO_DEBUG_OPTIONS:
        for val in dir(options):
            if not val.startswith('_'):
                doprint("options.{0} -> {1}".format(val, getattr(options, val)), file=sys.stderr)
# adaptations des chemeins des fichiers externes et internes           
#     sharebase = [searchbase]
#     if options.use sharedfolder and not options.caller:
#         sharebase.append(options.use sharedfolder)

    #options.origin = _setFileFolders(options.origin, searchbases, options.externpath)
    #options.sour ce = _setFileFolders(options.sou rce, searchbases, options.externpath)
    #options.test = _setFileFolders(options.test, searchbases, options.externpath)
        doprint("extern path", options.externpath)
    if options.verbose > 4:    
        doprint("origin", options.origin)
        doprint("source", options.source)
        doprint("test", options.test)
    if not options.source and options.origin:
        options.actionstr = 'usage'

    if (options.debug & DEMO_DEBUG_ANALYSIS) and not (options.debug & DEMO_DEBUG_OPTIONS):
        doprint('options.sharedfolder -> {}'.format(options.sharedfolder), file=sys.stderr)  # change usesharedfolder for sharedfolder 27/03/2019
        doprint('options.externpath -> {}'.format(options.externpath), file=sys.stderr)
        doprint('options.targetfolder -> {}'.format( options.targetfolder), file=sys.stderr)
            
#  adaptation de actionstr en fonction de origin 
    if os.path.exists(options.origin):
        if options.actionstr == "analyse,preproc":
            options.actionstr = 'usage'
        updateOptionsFromGmx(options, options.origin)

# adaptation du type de fichier de sortie            
    options.copytype = options.copytype.lower()
    options.copyexcel = options.copytype.startswith('xls') #in ['xls', 'xlsx', 'xlsm']
    options.copytxtcsv = options.copytype[:3] in ['csv', 'txt']
    if options.copytxtcsv:
        if len(options.copytype) > 3:
            options.copytype = options.copytype[:3]
            options.decimal = options.copytype[3:]
        if options.copytype == 'csv':
            options.sep = ";"
        elif options.copytype == 'txt':
            options.sep = "\t"

# detection des demandes simplifiées de  "LICENSE", "VERSION", "HELP"         
    if  options.outfile is None:
        options.outfile = debugOutput(sys.stdout)
    if options.version:
        licfile = os.path.expanduser("~/2")
        header = ["nn1 docker container modules versions:"]
        if os.path.exists(licfile):
            with open(licfile, 'r') as ff:
                ver = ff.read().rstrip()
            header.append("container: {0}".format(ver))
        lst = getVersionList(header)
        toprint = "\n\t".join(lst)
        errorcode |= OPTION_STOP
        return options, toprint, errorcode
    if options.license:
        licfile = os.path.expanduser("~/LICENSE")
        errorcode |= OPTION_DISPLAY_FILE_AND_STOP
        return options, licfile, errorcode
    if options.dhelp:
        if options.caller == 2:
            helpfile = os.path.expanduser("~/help/helplight.txt")
        else:
            helpfile = os.path.expanduser("~/help/help.txt")
        errorcode |= OPTION_DISPLAY_FILE_AND_STOP
        return options, helpfile, errorcode
# levee des incompatibilites
    options.loomaxrec = min(options.loomaxrec, options.looinitcount)    
# initialisation de actionlist, notrain
    if options.actionstr:
        options.actionlist = [val.strip() for val in options.actionstr.split(',')]
#     options.action = [val.lower() for val in options.actionlist]
    options.actionlist = [val.lower() for val in options.actionlist]
    options.actionlist = _actionListMgmt(options.actionlist)
    options.action = options.actionlist
#   actions = options.action
    options.notrain = not 'train' in options.actionlist
    options.nolootrain = not 'loo' in options.actionlist
    options.nobstrain = not 'bootstrap' in options.actionlist
    options.notest = not 'test' in options.actionlist

# checking de 'usage'
    if 'usage' in options.action:
        options.action = ['usage']
        if not options.origin:
            toprint = "options error\n\tUsage mode needs a model file (ORIGIN)!"
            errorcode = OPTION_STOP
            return options, toprint, errorcode
        if not os.path.exists(options.origin):
            toprint = "options error\n\tmodel file '{0}' cannot be found!".format(options.origin)
            errorcode = OPTION_STOP
            return options, toprint, errorcode
        
# adaptation des test implicites
    if 'test' in options.actionlist:
        if not options.test:
            options.test = options.source
            if options.testfields == "":
                options.testfields = options.datafields
            if not options.testrange and options.datarange:
                options.testrange = "TEST"
        if not coherencetraintest(options):
            toprint = "options.test is not coherent with options.train"
            errorcode = OPTION_STOP
            return options, toprint, errorcode
# ==============================
    if options.debug & DEMO_DEBUG_OPTIONS:
        print("sharedfolder", options.sharedfolder)
        print("targetfolder", options.targetfolder)
    
    if options.compiler.lower() == "default":
        options.compiler = ""

    options.decor = decor2long(options.decor)
    if options.debug & DEMO_DEBUG_OPTIONS:
        print("in api_options")
        print("\tdecor", options.decor)
    
    test = options.orderfield.strip()
    try:
        options.orderfield = C.CORRECTED_FIELD[test]
    except KeyError:
        options.orderfield = test

    index = None
    if not options.source and ('analyse' in options.actionlist) and not ('usage' in options.actionlist):            
        if nofile:
            options.source, index = "", -1
        else:
            #forcedefault = options.yesyes
            searchbases = [options.datafolder]
            candidates, searchdir = _getDataFileCandidates(searchbase=searchbases)
            if not searchdir:
                searchdir = options.sharedfolder  # change usesharedfolder for sharedfolder 27/03/2019
            options.source, index = _getDockerDataFile(options.source, 
                searchdir=searchdir, candidates=candidates, datakind='datafile', 
                defaultindex=0, doprint=doprint, forcedefault=options.yesyes )
        options.index = index
        if (index is None or index < 0) and not nofile:
            errorcode  |= OPTION_STOP
            if options.debug & DEMO_DEBUG_ANALYSIS:
                toprint = """searchdir -> {0}
                candidates -> {3}
                nofile -> {1}
                index -> {2}
                no datafile: action stopped
                """.format(searchdir, nofile, index, candidates)
                
            else:
                toprint = "no datafile: action stopped"
            return options, toprint, errorcode
#         indextest = None
#    
#         
#         if (index is not None and (index >= 0)) and not nofile:
#             options.test, options.notest = add Test(options.test, index, 
#                 searchdir, candidates, forcedefault=options.yesyes, 
#                 doprint=doprint)
#         if not options.notest and (indextest is not None) and (indextest == index):
#             options.test = ""

    updateOptionsFromGmx(options, options.origin)
    
    options.root = CCharOnlys(os.path.splitext(os.path.basename(options.source))[0], extended=True) 
    if not options.root:
        options.root = CCharOnlys(os.path.splitext(os.path.basename(options.test))[0], extended=True)
    if not options.filetype:
        options.filetype = os.path.splitext(options.source)[1][1:]
    if not options.filetype:
        options.filetype = os.path.splitext(options.test)[1][1:]

    lst = options.source.split('|') 
    if len(lst) == 3:
        options.datafields = lst.pop(2)
    if len(lst) == 2:
        options.source = lst[0]
        if options.datarange:
            toprint = "{0}conflict of datarange. {1} will overwrite {2}\n".format(toprint, options.datarange, lst[1])
            errorcode |= OPTION_WARN_AND_ASK
        else:
            options.datarange = lst[1]
    
    if not options.datarange and options.filetype in multiRangesType:
        options.datarange = 'DATA'
    if not isinstance(options.datafields, list):
        options.datafields = getListFromStr(options.datafields)
        options.datafields = deepenlist(options.datafields)
    if not isinstance(options.testfields, list):
        options.testfields = getListFromStr(options.testfields)
        options.testfields = deepenlist(options.testfields)
        
    if not isinstance(options.grouplist, list):
        if options.grouplist:
            try:
                options.grouplist = [val.strip() for val in options.grouplist.split(',')]
            except ValueError:
                options.grouplist = [val.strip() for val in options.grouplist.split(';')]
#             for val in options.grouplist:
#                 val = val.lower()
#                 newval = groupdict.get() 
            
            options.grouplist = [groupdict.get(val.lower(), val.lower()) for val in options.grouplist]
        else:
            options.grouplist = []
    if options.debug & DEMO_DEBUG_USAGE:
        print('initial grouplist:', options.grouplist)
    if options.groupcount and not isinstance(options.groupcount, list):
        try:
            options.groupcount = [int(val.strip()) for val in options.groupcount.split(',')]
        except ValueError:
            options.groupcount = [int(val.strip()) for val in options.groupcount.split(';')]
    if not options.testfields and not options.test and not options.testrange:
        options.notest = True

    cond = not hasattr(options, 'notest') or not options.notest
    if cond and not options.test and options.filetype in multiRangesType:
        options.test = options.source
    lst = options.test.split('|')  
    if len(lst) == 3:
        options.testfields = lst.pop(2)
    if len(lst) == 2:
        options.test = lst[0]
        if options.testrange:
            toprint = "{0}conflict of testrange. {1} will overwrite {2}\n".format(toprint, options.testrange, lst[1])
            errorcode |= OPTION_WARN_AND_ASK
        else:
            options.testrange = lst[1]
    if cond and not options.testrange and options.filetype in multiRangesType:
        options.testrange = 'TEST'
        
# on n'affiche pas le verbose < 5
    if (options.verbose >= 5) and (options.outfile is not None): # ic i
        toprint = "{0}verbose: {1}\n".format(toprint, options.verbose)
        toprint = "{0}verbosexls: {1}\n".format(toprint, options.verbosexls)
#     if (options.verbose >= 5) and (outfile is not None):
#         toprint = "{0}monal version: {1}\n".format(toprint, monalversion)
        toprint = "{0}metaphor version: {1}\n".format(toprint, metaphorversion)


    if options.copytype: 
        try:
            targetfolder = options.targetfolder  
#             if not targetfolder:
#                 targetfolder = options.usesharedresult
            if not os.path.exists(targetfolder):
                os.makedirs(targetfolder, 0o777)
                mode = os.stat(targetfolder)[0]
                os.chmod(targetfolder, mode | stat.S_IWOTH | stat.S_IWGRP)
        except OSError:
            targetfolder = os.path.join(options.folder, 'result')
            if not os.path.exists(targetfolder):
                os.makedirs(targetfolder, 0o777)
                mode = os.stat(targetfolder)[0]
                os.chmod(targetfolder, mode | stat.S_IWOTH | stat.S_IWGRP)
        options.targetfolder = targetfolder
    if isInt(options.modelcreation):
        options.modelcreation = int(options.modelcreation)
    if not options.modelcreation:
        options.debug |= DEMO_USE_EXISTING
    
    if options.roundthreshold > 0:
        options.extraselect = "((DeltaRank = 0) AND (abs(RoundoffTest)< {0:g}))".format(options.roundthreshold)
        options.extraselectrelaxed = '(abs(RoundoffTest)<{0:g})'.format(options.roundthreshold)
    else:
        options.extraselect = "(DeltaRank = 0)"
        options.extraselectrelaxed = ''
    
    if options.savefolder and not os.path.isdir(options.savefolder):
        folder = make_intern(getcustomproperty(options.savefolder, 'Utilities', 'Working folder'), options)
        options.origin = options.savefolder
        options.savefolder = folder

#     if options.savefolder and not os.path.exists(options.savefolder):
#         toprint = "bad savefolder option: %s\n"% options.savefolder
#         errorcode |= OPTION_WARN_AND_STOP
#         return options, toprint, errorcode
    
#     if options.leveragethreshold <= 0:
#         options.leveragethreshold = 0xFFFFFFFF     #float('i nf') 
        
    try:
        options.configstrMem = options.configstr
    except: pass
    
    options.multiseed = getListFromStr(options.seed)
    options.seed = options.multiseed[0]
    
    options.multihidden = getListFromStr(options.hidden)
    options.hidden = options.multihidden[0]   
    options.multihidden.sort()
    if len(options.multiseed) > 1:
        dirname = "{0}-multiseed".format(options.root)
        options.targetfolder = os.path.join(options.targetfolder, dirname)
        options.targetfolder = IndexFilename(options.targetfolder)
        if not os.path.exists(options.targetfolder):
            os.makedirs(options.targetfolder)

    options.multimaxrec = getListFromStr(options.maxrec)
    options.multimaxrec.sort(reverse=True)
    # traitement des valeurqs superieures a options.initcount
    excessvalues = [value for value in options.multimaxrec if value > options.initcount]
    while len(excessvalues):
        val = excessvalues.pop(0)        
        if len(excessvalues):
            options.multimaxrec.pop(0)
            toprint = "%sselected results %d is too high: ccanceled\n" % (toprint, val)
        else:
            options.multimaxrec[0] = options.initcount
            st = ','.join([str(val) for val in options.multimaxrec])
            errorcode |= OPTION_WARN_AND_ASK 
            toprint = "%sproposed selected results list: [%s]\n"%(toprint, st)
    options.maxrec = options.multimaxrec[0]    

#     if not options.verbosexls:
#     # si options.verbosexls est 0, on n'affiche que le premier maxrec 
#         if (len(options.multimaxrec) > 1) and (options.verbose >= 3):
#             toprint = "%sselected results limited to %d only (only one value permitted)\n" % (toprint, options.multimaxrec[0])
#             errorcode |= OPTION_WARN_AND_ASK
#         options.multimaxrec = options.multimaxrec[:1]
    
    if options.debug & DEMO_DEBUG_OPTIONS:
        lst = ["options"]
        for val in dir(options):
            if not val.startswith("_"):
                value = options.__getattribute__(val)
                typ = type(value)
                name = typ.__name__
                lst.append("%s\t%s (%s)" % (val, value, name))
        toprint = "%s%s\ndone\n"%(toprint, "    \n".join(lst))
        errorcode |= OPTION_WARN_AND_STOP

    return options, toprint, errorcode
# end api_options

def saveOptionsToFile(options, forceAction="train,test", doprint=doNothing, 
        forceYes=False, forceModel=False, rootTargetName="arguments"):
    """Write options namespace to a text file.
    
    Parameters:
     - options -> namespace to write down. 
         - The saving folder is read in options.savedir
     - doprint -> print function.
     - forceYes -> if set to False, the actual saving is submitted to accept question.
     - rootTargetName -> root of the written argument filename, without extension. The argument filename will be "options.root_rootfilename<_'x'>.txt", where 'x' is an index.
     
    Return:
     - options namespace eventually modified.
     - full name of the written argument file.
    """
# preparation de l'enregistrement du fichier d'arguments
    argdir = options.argsfolder
    if not os.path.exists(argdir):
        os.makedirs(argdir, 0o777)
    argfilename = os.path.join(argdir, "{0}_{1}.txt".format(options.root, rootTargetName))
    argfilename = IndexFilename(argfilename, "_{0}")
    options.actionstr = forceAction
    options.yes = True
    lst = option2Arguments(options)
    if options.verbose >= 4:
        for st in lst:
            print(st)
    locargfilename = make_extern(argfilename, options)   
    mess = "Will you save the argument list in file '{0}'?".format(locargfilename) 
    valdef = dialogdefaults['action']['save_argfile']
    if yesNoQuestion(mess, valdef, "", doprint=doprint, forcedefault=forceYes):
        with open(argfilename, "wb") as ff:
            for val in lst:
                ff.write("{0}\n".format(val).encode())
        doprint("saved argument file: {0}".format(locargfilename))
        if options.dockercallable: 
#             st = "cammand line:\n\tdocker run -it --rm -v {2}:{0} --env-file {1} {3}"
            st = "cammand line:\n\tdocker run -it --rm -v {2}:{0} {3} @{1}"
            target = make_neutral(locargfilename, options, addpath="argsdir")
            message = st.format(options.sharedfolder, target, options.externpath, options.dockername)
            doprint(message)
        if forceModel:
            options.modelcreation = True
            
        options.yes = True
#      options.actionstr = "train,test"
        options.actionlist = options.actionstr.split(',')
        return options, argfilename
    return options, ""

def _getCmdLineOptions(args, defaultdico=None, add_argumentlist=add_arg_list, debug=0):
    """Read the argument list, usually coming from command line.
    defaultdico is the dictionary of default values.
    
    Return the 'options' namespace.
    """
    #if defaultdico is None:
    origindico = defaultdict(lambda: None)
    origindico.update(argumentsdefaultdict)
    if defaultdico is not None:
        envlist = [(key, val) for key, val in origindico.items() if not key in defaultdico]
        origindico.update(defaultdico) 
        for key, val in envlist:
            origindico[key] = os.environ.get(key, val)
    defaultdico = origindico
    actionlist = ['all', 'analyse', 'preproc', 'train', 'test', 'loo', 'lootest', 'bootstrap', 'bootstraptest', 'usage']
    actionlist.extend([val.upper() for val in actionlist])

    if debug:
        print("_getCmdLineOptions 1")
        for key, val in defaultdico.items():
            print("\tdefaultdico[{0}] = {1}".format(key, val))

    parser = ArgumentParser(description='Metaphor.', fromfile_prefix_chars='@') 

    # string arguments
    parser.add_argument('--arg_file', nargs="?", type=str, default="",
        help="name of arguments file")
    valdef = defaultvalue("DATAFILE", "", "", defaultdico=defaultdico)
    parser.add_argument('-df', '--source', nargs="?", type=str,
        default=valdef,
        help="Initial data source filename (xls,xlsx,xlsm,csv,txt format)")
    
    valdef = defaultvalue("DATA", "", "", defaultdico=defaultdico)
    parser.add_argument('-ud', '--usagedata', nargs="?", type=str,
        default=valdef, help="data for single usage")
    
    valdef = defaultvalue("TESTFILE", "", "", defaultdico=defaultdico)
    parser.add_argument('-tf', '--test', nargs="?", type=str,
        default=valdef, 
        help="Data test filename (xls,xlsx,csv,txt format)")
    
    parser.add_argument('-typ', '--filetype', default="",
        choices=["txt", "csv", "xls", "xlsx"], nargs='?',
        help="Source and test file type")
    
    valdef = defaultvalue("MODE", "unknown", "unknown", defaultdico=defaultdico)
    parser.add_argument('-mo', '--mode', dest='mode', default=valdef, 
        nargs='?', help="Neural engine mode (nn, gm or unknown)")
    
    parser.add_argument('-cc', '--compiler', dest='compiler', 
        default="", help="Compiler for model libraries")

    valdef = defaultvalue("SAVEFOLDER", "", "", defaultdico=defaultdico)
    parser.add_argument('-sf', '--savefolder', nargs='?', 
        default=valdef,
        help="training results saving folder")
    
    valdef = defaultvalue("SHAREDFOLDER", "", "", defaultdico=defaultdico)
    parser.add_argument('-sh', '--sharedfolder', nargs='?', default=valdef,
        help="shared folder only for native call")
    
    valdef = defaultvalue("ORIGIN", "", "", defaultdico=defaultdico)
    parser.add_argument('-or', '--origin', nargs='?', 
        default=valdef,
        help="training results saving folder")
    
    valdef = defaultvalue("DATARANGE", "DATA", "", defaultdico=defaultdico)
    parser.add_argument('-sd', '--datarange', 
        default=valdef,
        help="Range for training data (Excel-like files)")
    
    valdef = defaultvalue("TESTRANGE", "TEST", "", defaultdico=defaultdico)
    parser.add_argument('-st', '--testrange', 
        default=valdef,
        help="Range for test data (Excel-like files)")
    
    valdef = defaultvalue("DATAFIELDS", "", "", defaultdico=defaultdico)
    parser.add_argument('-fd', '--datafields',
        default=valdef,            
        help="Fields for training data (Excel-like files)")
    
    valdef = defaultvalue("TESTFIELDS", "", "", defaultdico=defaultdico)
    parser.add_argument('-ft', '--testfields',
        default=valdef,            
        help="Fields for test data (Excel-like files)")
    
    parser.add_argument('-dt', '--datatable', default=stdTable, 
        help="SQL table name")
    
    valdef = defaultvalue("GROUPLIST", "", "", defaultdico=defaultdico)
    parser.add_argument('-gl', '--grouplist', 
        default=valdef, help='field groups')
    
    valdef = defaultvalue("GROUPCOUNT", "0", "0", defaultdico=defaultdico)
    parser.add_argument('-gc', '--groupcount', 
        default=valdef, help='field counts in groups')
    
    valdef = defaultvalue("RESINDEX", "0", "0", defaultdico=defaultdico)
    parser.add_argument('-r', '--resultindex', type=int, 
        default=valdef, help="Best result index. Default 0")
    
    valdef = defaultvalue("TEMPDIR", "", "", defaultdico=defaultdico)
    parser.add_argument('-k', '--keeptemp', dest='keeptemp', 
        default=valdef, help="Keeping temporary folder")
    
    valdef = defaultvalue("SORTBY", default="", const="VLOO score", 
                          defaultdico=defaultdico)
    parser.add_argument('-o', '--orderfield', const="VLOO score", nargs="?", 
        default=valdef, help="Data field used for result sorting")
    
    valdef = defaultvalue("LOOSORTBY", default="", const="ID", 
                          defaultdico=defaultdico)
    parser.add_argument('-lo', '--looorderfield', const="ID", nargs="?", 
        default=valdef, help="Data field used for loo result sorting")
    
    valdef = defaultvalue("BSSORTBY", default="", const="VLOO score", 
                          defaultdico=defaultdico)
    parser.add_argument('-bo', '--bootstraporderfield', const="VLOO score", nargs="?", 
        default=valdef, help="Data field used for bootstrap result sorting")
    
    valdef = defaultvalue("DECOR", '', '', defaultdico=defaultdico)
    parser.add_argument('-d', '--decor', nargs='?', default=valdef, 
        help="decorator rules for result files. Default ''")
    
    valdef = defaultvalue("PROPERTYUNIT", "", "", defaultdico=defaultdico)
    parser.add_argument('-pu', '--propertyunit', 
        default=valdef, help="unit of the targeted property")
    
    valdef = defaultvalue("EXCELNUMFORMAT", "", "", defaultdico=defaultdico)
    parser.add_argument('-en', '--excelnumformat',
        default=valdef, help="numerical display format")
    
    valdef = defaultvalue("TERMINALNUMFORMAT", "", "", defaultdico=defaultdico)
    parser.add_argument('-tn', '--terminalnumformat',
        default=valdef, help="numerical display format")
    
    # integer arguments
    valdef = defaultvalue("LICENSE", 0, 1, defaultdico=defaultdico)
    parser.add_argument('--license', nargs="?", const=1, type=int, 
        default=valdef, help="Display license")
    
    valdef = defaultvalue("VERSION", 0, 1, defaultdico=defaultdico)
    parser.add_argument('--version', nargs="?", const=1, type=int, 
        default=valdef,
        help="Display graphmachine docker container version")
    
    valdef = defaultvalue("HELP", 0, 1, defaultdico=defaultdico)
    parser.add_argument('--dhelp', nargs="?", const=1, type=int, 
        default=valdef, help="Display docker container help")
    
    valdef = defaultvalue("YES", defaultdico=defaultdico)
    parser.add_argument('-y', '--yes', nargs="?", const=1, type=int,
        default=valdef,
        help="Answer yes to all questions and accept default values")
    
    valdef = defaultvalue("VERB", "1", "1", defaultdico=defaultdico)
    parser.add_argument('-v', '--verbose', default=valdef, type=str, 
        help="Verbose level")
    
    valdef = defaultvalue("RESULTTYPE", "xlsx", "xlsx", defaultdico=defaultdico)
    parser.add_argument('-R', '--copytype', default=valdef,
        help="result copy file type")
    
    valdef = defaultvalue("MAXREC", 10, 0, defaultdico=defaultdico)
    parser.add_argument('-M', '--maxrec', default=valdef,
        help="Number max of registered records (list of); default 10")
    
    valdef = defaultvalue("SEED", -1, -1, defaultdico=defaultdico)
    parser.add_argument('-s', '--seed', default=valdef, 
        help="Random generator seed. Default -1")
    
    valdef = defaultvalue("HIDDEN", 5, 0, defaultdico=defaultdico)
    parser.add_argument('-H', '--hidden', default=valdef,
        help="Number of hidden neurons (list of). Default 5")
    
    valdef = defaultvalue("EPOCHS", 150, 0, outtype=int, 
        defaultdico=defaultdico)
    parser.add_argument('-e', '--epochs', type=int, default=valdef, 
        help="Number of training epochs. Default 150")

    valdef = defaultvalue("INIT", 250, 0, outtype=int, 
        defaultdico=defaultdico)
    parser.add_argument('-I', '--initcount', type=int, default=valdef, 
        help="Number of training initialization. Default 250")

#     valdef = defaultvalue("PREPROCTYPE", "", "", 
#                              defaultdico=defaultdico)
#     parser.add_argument('-pp', '--preproctype', type=str, default=valdef,
#         help='Preprocessing type: ""-> choice by user, "linear", "crossproduct", "full2ndorder"')

#     valdef = defaultvalue("PROBECOUNT", 1000, 0, defaultdico=defaultdico)
#     parser.add_argument('-pc', '--probecount', type=int, default=valdef, 
#         help="Number of random probe initialization. Default 1000")

    valdef = defaultvalue("PERTTHRES", 0.5, 0, outtype=float, 
                             defaultdico=defaultdico)
    parser.add_argument('-pt', '--pertinencethreshold', type=float,
        default=valdef, help="Pertinence threshold for input selection")

    valdef = defaultvalue("CALLER", 0, 0, defaultdico=defaultdico)
    parser.add_argument('--caller', type=int, default=valdef,
        help="Caller type (0: direct, 1: docker). Default 0")

    parser.add_argument('-rd', '--resultdisplay', type=int, default=-1, 
        help="Number of best result displayed. Default -1 (=all)")
    
    valdef = defaultvalue("LOOINITTYPE", 2, 0, defaultdico=defaultdico)
    parser.add_argument('-lt', '--looinittype', type=int, default=valdef, 
        help="special init 0: start weight, 1: end weight, 2 random). Default 0")

    valdef = defaultvalue("LOOINITCOUNT", 100, 0, defaultdico=defaultdico)
    parser.add_argument('-li', '--looinitcount', type=int, default=valdef, 
        help="LOO: number of train per base. Default 100")
    
    valdef = defaultvalue("LOOEPOCHS", 150, 0, defaultdico=defaultdico)
    parser.add_argument('-le', '--looepochs', type=int, default=valdef, 
        help="number of epochs in trainings for LOO CV. Default 150")

    valdef = defaultvalue("LOOMAXREC", 1, 0, defaultdico=defaultdico)
    parser.add_argument('-lm', '--loomaxrec', type=int, default=valdef, 
        help="number of training selected after trainings for LOO CV. Default 1")
    
    valdef = defaultvalue("BSTYPE", 2, 0, defaultdico=defaultdico)
    parser.add_argument('-bs', '--bootstraptype', type=int, 
        default=valdef, 
        help="bootstraptype 0: none, 1: standard, 2: residus. Default 2")
    
    valdef = defaultvalue("BSINITTYPE", 2, 0, defaultdico=defaultdico)
    parser.add_argument('-bt', '--bootstrapinittype', type=int, 
        default=valdef, 
        help="special init 0: start weight, 1: end weight, 2 random). Default 2")

    valdef = defaultvalue("BSCOUNT", 250, 0, defaultdico=defaultdico)
    parser.add_argument('-bc', '--bootstrapcount', type=int, 
        default=valdef, 
        help="boostrap: number of train per base. Default 100")

    valdef = defaultvalue("BSINITCOUNT", 100, 0, defaultdico=defaultdico)
    parser.add_argument('-bi', '--bootstrapinitcount', type=int, 
        default=valdef,
        help="boostrap: number of train initialisation per base. Default 100")
    
    valdef = defaultvalue("BSEPOCHS", 150, 0, defaultdico=defaultdico)
    parser.add_argument('-be', '--bootstrapepochs', type=int, 
        default=valdef, 
        help="number of epochs in bootstrap trainings. Default 150")
    
    # choices arguments
    valdef = defaultvalue("ACTION", "", "", defaultdico=defaultdico)
    parser.add_argument('-a', '--actionstr', dest='actionstr', 
        default=valdef,
        help="action option in character string version with comma separator")
    
    # float arguments
    valdef = defaultvalue("RDMINIT", 0.1, 0, outtype=float, 
                             defaultdico=defaultdico)
    parser.add_argument('-D', '--initstddev', type=float,
        default=valdef,
        help="Standard deviation for param initialization. Default 0.1")  
    valdef = defaultvalue("RNDTHRES", 1E-4, 0, outtype=float, 
                             defaultdico=defaultdico)
    parser.add_argument('-T', '--roundoffthreshold', type=float, 
        default=valdef,
        dest="roundthreshold", help="Roundoff selection threshold. Default 1E-4")
    valdef = defaultvalue("LEVTHRES", 0.0, 0, outtype=float, 
                             defaultdico=defaultdico)
    parser.add_argument('-L', '--leveragethreshold', type=float, 
        default=valdef,
        help="leverage selection threshold. Default 5.0")
    valdef = defaultvalue("LOOLEVTHRES", 0.0, 0, outtype=float, 
                             defaultdico=defaultdico)
    parser.add_argument('-LL', '--looleveragethreshold', type=float, 
        default=valdef, 
        help="loo leverage selection threshold for LOO. Default 0.0")  
    
    # boolean arguments 
    valdef = defaultvalue('MODERATE', "0", "0", defaultdico=defaultdico)
    parser.add_argument('-wm', '--weightsmoderation', action='store_true',
        default=valdef, help="Add weight moderation during training")
    
    valdef = defaultvalue("CLASSIF", "", "0", defaultdico=defaultdico) 
    parser.add_argument('-cl', '--classif', action='store_true',# nargs="?", const=1,
        default=valdef, help="Create a classification model")

    valdef = defaultvalue("FORCEMODEL", "", "0", defaultdico=defaultdico)
    parser.add_argument('-m', '--modelcreation', action='store_true', #nargs="?", const=1,
        default=valdef, help="No model creation if already exists")
    
    valdef = defaultvalue("TIMER", 0, 0, defaultdico=defaultdico)
    parser.add_argument('--timer', action='store_true', dest="dotimer", 
        default=valdef, help="Set timer mode. Default 0")
    
    valdef = defaultvalue("DEBUG", 0, 0, defaultdico=defaultdico)
    parser.add_argument('-dd', '--debug', #action='store_true', 
        default=valdef, help="Debug state. Default 0")
    
    valdef = defaultvalue("LIBUSE", 0, 0, defaultdico=defaultdico)
    parser.add_argument('-lu', '--libuse', action='store_true', 
        default=valdef, help="Debug state. Default 0")
    # file arguments
    parser.add_argument('--infile', type=FileType('r'), 
        default=sys.stdin, help='Input file. Default stdin')
    
    parser.add_argument('--outfile', type=FileType('w'),
        default=sys.stdout, help='Output file. Default stdout')
    
    if debug:
        print("add arguments")
        for val in add_argumentlist:
            print("\t", val)
    for val in add_argumentlist:  
        # ajouter les arguments supplementaires 
        if val[-2] == 'dico':
            key = val[1][2:].upper()
            valdef = defaultvalue(key, val[3], val[3], defaultdico=defaultdico)
        else:
            valdef = val[-3]
        if len(val) == 7: 
            parser.add_argument(val[0], val[1], type=val[2], choices=val[4], default=valdef, help=val[5])
        elif len(val) == 6: 
            parser.add_argument(val[0], val[1], type=val[2], default=valdef, help=val[5])
        elif len(val) == 5:
            parser.add_argument(val[0], val[1], default=valdef, help=val[4])
     
    res = parser.parse_args(args)
    exu.NUM_FORMAT = res.excelnumformat
    utils.TERM_NUM_FORMAT = res.terminalnumformat
    return res

def _computeTrainingResult(dbConnect, tablename, model, resultdisplay=-1,
        specialresultdisplay=-1, IDlist=[0], maxrec=10, targets=None, 
        pptyname="", extraselect="", orderfield="PRESS", indexname=None, 
        extratype="", verbosexls=1): 
    """Calcul des résultats d'apprentissage.
    Les resultats d'apprentissage sont dans la base de donnees connectee par 
    dbConnect. 
    Creation de la table DataFrame.
    """
    targetfield = _linkstr(targetstr, pptyname)
    assert isinstance(model, DriverLib)
    fieldlist = ["ID", paramEndStr]  #, "disp ersion"]
    resindex = IDlist[0]
    indlist = IDlist[:maxrec]
    if resultdisplay < 0:
        resultdisplay = len(indlist)
    else:
        resultdisplay = max(1, min(resultdisplay, len(indlist)))
    reverse = orderfield in C.TCR_MAXIMIZE   
    paramdisp = getDataFrame(dbConnect, table=tablename, fieldlist=fieldlist, 
        comp=0, maxrec=maxrec, orderfield=orderfield, reverse=reverse, 
        extraselect=extraselect)  #index=resindex, 
    
    ww = paramdisp[paramEndStr]
    weights = np.ndarray((ww.shape[0], ww[0].shape[0]))
    for ind, w in enumerate(ww):
        weights[ind] = w
    ll = min(resultdisplay, ww.shape[0])
    if extratype in ['loo', 'bootstrap']:
        resultarray = np.ndarray((model.baseLen, 1 + ll))
    else:
        resultarray = np.ndarray((model.baseLen, 1 + 4 * ll))
    
    multires = TransferModel(model, weights=weights, style=2, debug=1)
    columns = [targetfield]
    for ind, besttrainindex, (_, residuals, _, leverages, _, _, _) in \
            zip(range(resultdisplay), paramdisp["ID"], multires):
        start = len(columns)
        if extratype in ['loo', 'bootstrap']:
            columns.append(_linkstr("VLOO", pptyname, besttrainindex))
        else:
            columns.extend([_linkstr(estimatedstr, pptyname, besttrainindex), 
                _linkstr(trainresidualstr, pptyname, besttrainindex), 
                _linkstr(leveragestr, pptyname, besttrainindex), 
                _linkstr("VLOO", pptyname, besttrainindex)])
        
        for ind, (target, residual, lev) in enumerate(zip(model.targets, 
                residuals, leverages)):  #, model.modelNames
            #if start == 1:
            if extratype in ['loo', 'bootstrap']:
                resultarray[ind, 0] = target
                resultarray[ind, start] = target + residual/(1 - lev)
            else:    
                resultarray[ind, 0] = target
                resultarray[ind, start] = target + residual
                resultarray[ind, start + 1] = - residual  # 3
                resultarray[ind, start + 2] = lev  # 2
                resultarray[ind, start + 3] = target + residual/(1 - lev)  # 1
    try:
        model.modelNames[0]
        index = model.modelNames
    except (AttributeError, IndexError):
        index = range(model.dataCount)
    df = DataFrame(resultarray, columns=columns, index=index)
    if indexname is not None:
        df.index.name = indexname

    return df

def LoadModuleFromCfg(cfgfile, modulename=""):
    """charge un module d'apprentissage depuis les informations de config
    Passe par l'intermediaire du fichier gmx.
    Charge egalement les cibles d'apprentissage.
    Le nom du module est facultatif. S'il est absent, il est recherche dans le 
    fichier cfg.
    Retourne le modele ainsi cree.
    """
    if isinstance(cfgfile, str):
        confResult = defaultedConfigParser(cfgfile)
        root = confResult.get("projects", "0")
        config = getDefaultedConfigParser(confResult.get(root, "cfgfile"))
    else:
        config = cfgfile
        root = config.get("projects", "0")
    if not modulename:
        modulename = config.get(root, "module")
    gmxfile = config.get(root, "gmxfile")
    dico = getDictFromGmx(gmxfile)
    model = loadmoduleloc(modulename)   #loadTrainingModule(modulename)
    model.loadParameters(dico)
    #model.targets = targetlist
    return model

def loadmoduleloc(modulename, workingdir=""):
    if not modulename.endswith((".dll", ".so", ".dylib")):
        return None
    if workingdir:
        modulename = os.path.join(workingdir, modulename)
    mtype = moduleType(modulename)
    if mtype == 3:
        return DriverLib(modulename)
    if mtype == 2:
        return DriverMultiDyn(modulename)
    if mtype == 1:
        return ModelLib(modulename)

def apiTrainResults(options=None, resfile="", titles=[], targets=None, 
        maxrec=10, resultdisplay=-1, extraselect="", extraselectrelaxed="",
        outfile=sys.stdout, extratype="", gmxfile="", debug=0, verbose=1, 
        verbosexls=0, trainDataFrame=None, mynames=None):
    #orderfield="PRESS", 
    
    looTrainFrame = None
    bsTrainFrame = None
    IDlist = []
    orderfield = getOrderField(options, "PRESS")
    if not options is None:
        titles = options.datatitles
        maxrec = options.maxrec 
        resultdisplay = options.resultdisplay 
        extraselect = options.extraselect 
        extraselectrelaxed = options.extraselectrelaxed
        outfile = options.outfile 
        debug=options.debug 
        verbose = options.verbose 
        verbosexls = options.verbosexls
#        orderfield = options.orderfield
        resfile = options.cfgfile
        mode = options.mode
    doprint = toPrint(outfile)
    specialresultdisplay = -1 
#     if (extratype in ['loo', 'bootstrap']):
    if (extratype == 'loo'):
        specialresultdisplay = options.loomaxrec
            
    if resfile and isinstance(resfile, str):
        confResult = defaultedConfigParser(resfile)
        confResult.read(resfile)
        if confResult.has_section("projects"):
            root = confResult.get("projects", "0")
        else:
            root = options.root
        if confResult.has_section(root) and confResult.has_option(root, "cfgfile"):
            cfgfile = confResult.get(root, "cfgfile")
            confResult = defaultedConfigParser(cfgfile)
        if hasattr(options, "sqlFileName") and options.sqlFileName:
            sqlFileName = options.sqlFileName
        else:
            sqlFileName = confResult.get(root, "sqlfilename")
        options.sqlFileName = sqlFileName
        tablename = confResult.get(root, "tablename")
        options.tablename= tablename
        pptyname = confResult.get(root, "propertyname")
        options.pptyname = pptyname
        pptyunit = confResult.get(root, "propertyunit")
        options.pptyunit = pptyunit
        module = confResult.get(root, "module")
        options.modulename = module
        gmxfile = confResult.get(root, "gmxfile")
#         if targets is None:
#             targetsstr = confResult.get(root, "targetlist")
#             targets = [float(val) for val in targetsstr.split(",")]
    else:
        root = options.root
        sqlFileName = options.sqlFileName
        tablename = options.tableName
        pptyname = options.propertyName
        pptyunit = options.propertyunit
        module = options.modulename
        fol = os.path.dirname(module) 
        if not fol:
            module = os.path.join(options.savedir, module)
    with sqlconnect(sqlFileName, detect_types=sqlPARSE_DECLTYPES) as dbConnect:
        reverse = orderfield in C.TCR_MAXIMIZE  
        curselect = extraselect 
        IDlist = getDataFrame(dbConnect, table=tablename, index=None, 
            fieldlist=["ID"], comp=0, orderfield=orderfield, reverse=reverse,
            maxrec=maxrec, extraselect=curselect)["ID"]
        if not IDlist.shape[0]:
            curselect = extraselectrelaxed
            IDlist = getDataFrame(dbConnect, table=tablename, index=None, 
                fieldlist=["ID"], comp=0, orderfield=orderfield, reverse=reverse,
                maxrec=maxrec, extraselect=curselect)["ID"]
        if options.notrain:
            sname = 'training results' if mynames is None else mynames.trainsheetname 
            dataframe = getFrameFromExcel(options.origin, sname, reduce=True)
            if options.nolootrain and ('lootest' in options.action):
                sname = 'LOO CV results' if mynames is None else mynames.lootrainsheetname 
                looTrainFrame = getFrameFromExcel(options.origin, sname, reduce=True)
            if options.nobstrain and ('bootstraptest' in options.action):
                sname = 'Bootstrap training results' if mynames is None else mynames.bstrainsheetname 
                bsTrainFrame = getFrameFromExcel(options.origin, sname, reduce=True)
        else:
            with loadModule(module, pptyname=pptyname, targets=targets) as model:
                model.loadTrainingData(options)
                if len(titles) and model.modelCount and 'identifiers' in options.grouplist:
                    indexname = titles[0]  #[0]
                else:
                    indexname = None
                dataframe = _computeTrainingResult(dbConnect, 
                    tablename, 
                    model, 
                    resultdisplay=resultdisplay, 
                    specialresultdisplay=specialresultdisplay,
                    IDlist=IDlist, 
                    maxrec=maxrec, 
                    targets=targets, 
                    pptyname=pptyname, 
                    extraselect=curselect,
                    orderfield=orderfield, 
                    indexname=indexname, 
                    extratype=extratype, 
                    verbosexls=verbosexls)
                if not dataframe.index.name:
                    dataframe.index.name = trainDataFrame.index.name
    if (verbose >= 6) and (outfile is not None):
        doprint("training data:")
        doprint(dataframe.to_string(float_format=float_format()))
    trainresultColumn = 1
    return dataframe, looTrainFrame, bsTrainFrame, IDlist, root, trainresultColumn, gmxfile
    
def fillLOOTestFrame(options, source, savedir, testFrame, smilestitle="",
    keyresult="", keyLev="", keyError="", keyLOOresult="", LOOkeys = [], 
    writer=None, verbose=1, mode="gm", debug=0): #, max Workers
    
    leveragethreshold = options.looleveragethreshold

    def ApplyResults(outputlevs, ID):
        idloc = testFrame.index[ID]
        if leveragethreshold > 0:
            outOkLev = [out for out, lev in outputlevs if lev < leveragethreshold]
        else:
            outOkLev = outOkLev = [outs[0] for outs in outputlevs]
        count = len(outOkLev)
        mean = float('nan') if not count else sum(outOkLev)/count
#        testFrame.at[molecule, keyresult] = float(output[0])
#        testFrame.at[molecule, keyLev] = float(output[1])
        testFrame.at[idloc, keyLOOresult] = mean
        testFrame.at[idloc, "SCount"] = count
        for ind, output in enumerate(outOkLev):
            st = "{0}-{1}".format(keyresult, ind)
            testFrame.at[idloc, st] = output

#     drivermodel, _, _, _ = getTrainingModule(options) 
#     drivermodel = getTrainingModule(options) 
    with getTrainingModule(options) as drivermodel:
        drivermodel = drivermodel[0]
        ni = drivermodel.inputCount
        if ni:
            try:
                inputnorm = source["inputnorm"]
            except KeyError:
                inputnorm = source['root']["inputnorm"]
            if isinstance(inputnorm, text_type):
                inputnorm_a = inputnorm.split(';')
                inputnorm = []
                for val in inputnorm_a:
                    normloc = []
                    if isinstance(val, text_type) and (val.startswith('[') and (val.endswith(']'))):
                        val2 = val[1:-1].split(' ')
                    else:
                        val2 = val
                    normloc = [val3 for val3 in val2 if val3 != ""]
                    inputnorm.append(normloc)                            
            drivermodel.inputnorm = np.asarray(inputnorm)
        try:
            outputnorm = source["outputnorm"]
        except KeyError:
            outputnorm = source['root']["outputnorm"]
        if isinstance(outputnorm, text_type):
            outputnorm_a = outputnorm.split(';')
            outputnorm = []
            if len(outputnorm_a) > 1 and not isFloat(outputnorm_a[0]):
                for val in outputnorm_a:
                    normloc = []
                    if isinstance(val, text_type) and (val.startswith('[') and (val.endswith(']'))):
                        val2 = val[1:-1].split(' ')
                    else:
                        val2 = val
                    normloc = [val3 for val3 in val2 if val3 != ""]
                    outputnorm.append(normloc)  
            else:
                val = outputnorm_a
                if isinstance(val, list) and len(val) == 2:
                    outputnorm = [float(vala) for vala in val]
                elif isinstance(val, text_type) and (val.startswith('[') and (val.endswith(']'))):
                    val2 = val[1:-1].split(' ')
                    outputnorm = [val3 for val3 in val2 if val3 != ""]
                else:
                    val2 = val[1:-1].split(' ')
                    outputnorm = [float(vala) for vala in val2]
        drivermodel.outputnorm = np.asarray(outputnorm)
        
        options.paramCount = drivermodel.paramCount
        weights = source['extraweights']
        dispersions = source['extradispersion']
        indexex = source['indexes']
        modeldict = source['model']
        try:
            pptyname = source['propertyname']
        except KeyError:
            pptyname = source['root']['propertyname']
        drivermodel.extraweights = weights
        drivermodel.extradispersions = [np.asarray(disp.flat, np.double) for disp in dispersions]   
    
        inputcount = drivermodel.inputCount
        mess = "\tLOO test"
        with Progress_tqdm(len(testFrame.index), desc=mess, nobar=verbose<nobarverb) as update:
            for ind, (frameindex, row) in enumerate(testFrame.iterrows()):
                try:
                    inputs = np.asarray(row[0: inputcount], np.double)
                except ValueError:  # python 2.x
                    inputs = np.asarray(row[1: ni+1], np.double)
                outlevlist = drivermodel.transferleverage(inputs, 'extra')
                ApplyResults(outlevlist, ind)
                update(ind+1)

    return testFrame  #, testFrameBaseCol, inputcount


@hookable.indirect('mode')
def computeLOOTest(options, modeltestframe, source, savedir="", verbose=1, debug=0):   
    """Calcul du resultat des tests avec LOO.
    """
    maintitles = modeltestframe.gettitles()
    pptyname = maintitles[-1]
    testFrameBaseCol = modeltestframe.shape[1]
    testFrame = modeltestframe._frame.copy()
    richestimated = []
    keyresult = _linkstr(estimatedstr, pptyname)
    keyLev = _linkstr(leveragestr, pptyname)
    keyError = _linkstr(testresidualstr, "LOO_{}".format(pptyname))
    keyLOOresult = "{0}_{1}".format("LOO", _linkstr(estimatedstr, pptyname))
    
    testFrame = fillLOOTestFrame(options, source, savedir, testFrame, 
        smilestitle="", keyresult=keyresult, keyError=keyError, keyLOOresult=keyLOOresult,
        keyLev=keyLev, LOOkeys= richestimated, verbose=verbose, 
        mode=options.mode, debug=debug)
    
    return testFrame
    
@hookable.indirect('mode')        
def computeBSTest(options, modeltestframe, source, savedir="", extratype="LOO", verbose=1, debug=0):  

    maintitles = modeltestframe.gettitles()
    pptyname = maintitles[-1]
    testFrameBaseCol = modeltestframe.shape[1]
    testFrame = modeltestframe._frame.copy()
    leveragethreshold = options.looleveragethreshold

    keyresult = _linkstr(estimatedstr, pptyname)
    keyLOOresult = "{0}_{1}".format("LOO", _linkstr(estimatedstr, pptyname))
    def ApplyResults(outputlevs, ID):
        idloc = testFrame.index[ID]
        if leveragethreshold > 0:
            outOkLev = [out for out, lev in outputlevs if lev < leveragethreshold]
        else:
            outOkLev = [outs[0] for outs in outputlevs]
        count = len(outOkLev)
        mean = float('nan') if not count else sum(outOkLev)/count
        testFrame.at[idloc, keyLOOresult] = mean
        testFrame.at[idloc, "SCount"] = count
        for ind, output in enumerate(outOkLev):
            st = "{0}-{1}".format(keyresult, ind)
            testFrame.at[idloc, st] = output
    
    
    with getTrainingModule(options) as drivermodel:
        drivermodel = drivermodel[0]
        ni = drivermodel.inputCount
        if ni:
            try:
                inputnorm = source["inputnorm"]
            except KeyError:
                inputnorm = source['root']["inputnorm"]
            if isinstance(inputnorm, text_type):
                inputnorm_a = inputnorm.split(';')
                inputnorm = []
                for val in inputnorm_a:
                    normloc = []
                    if isinstance(val, text_type) and (val.startswith('[') and (val.endswith(']'))):
                        val2 = val[1:-1].split(' ')
                    else:
                        val2 = val
                    normloc = [val3 for val3 in val2 if val3 != ""]
                    inputnorm.append(normloc)                            
            drivermodel.inputnorm = np.asarray(inputnorm)
        try:
            outputnorm = source["outputnorm"]
        except KeyError:
            outputnorm = source['root']["outputnorm"]
        if isinstance(outputnorm, text_type):
            outputnorm_a = outputnorm.split(';')
            outputnorm = []
            if len(outputnorm_a) > 1 and not isFloat(outputnorm_a[0]):
                for val in outputnorm_a:
                    normloc = []
                    if isinstance(val, text_type) and (val.startswith('[') and (val.endswith(']'))):
                        val2 = val[1:-1].split(' ')
                    else:
                        val2 = val
                    normloc = [val3 for val3 in val2 if val3 != ""]
                    outputnorm.append(normloc)  
            else:
                val = outputnorm_a
                if isinstance(val, list) and len(val) == 2:
                    outputnorm = [float(vala) for vala in val]
                elif isinstance(val, text_type) and (val.startswith('[') and (val.endswith(']'))):
                    val2 = val[1:-1].split(' ')
                    outputnorm = [val3 for val3 in val2 if val3 != ""]
                else:
                    val2 = val[1:-1].split(' ')
                    outputnorm = [float(vala) for vala in val2]
        drivermodel.outputnorm = np.asarray(outputnorm)
        
        options.paramCount = drivermodel.paramCount
        weights = source['extraweights']
        dispersions = source['extradispersion']
#         indexex = source['indexes']
#         modeldict = source['model']
        try:
            pptyname = source['propertyname']
        except KeyError:
            pptyname = source['root']['propertyname']
        drivermodel.extraweights = weights
        drivermodel.extradispersions = \
            [np.asarray(disp.flat, np.double) for disp in dispersions]   
    
        ni = drivermodel.inputCount
        if extratype.lower() == 'loo':
            mess = "LOO test"
        else:
            mess = "\tBootstrap test"
        with Progress_tqdm(len(testFrame.index), desc=mess, nobar=verbose<nobarverb) as update:
            for ind, (_, row) in enumerate(testFrame.iterrows()):
                try:
                    inputs = np.asarray(row[0: ni], np.double)
                except ValueError:  # python 2.x
                    inputs = np.asarray(row[1: ni+1], np.double)
                outlevlist = drivermodel.transferleverage(inputs, 'extra')
                ApplyResults(outlevlist, ind)
                update(ind+1)
            update.flush()

    return testFrame  #, patternlist, testFrameBaseCol  #, inputcount

def getExtraFields(maxreclist, pptyname, cols=[], richestimated=[], richtestresidual=[], verbose=3):
    countfield = []
    withresidual = True  #len(richtestresidual)
    for maxrecloc in maxreclist:
        if len(maxreclist):
            countfieldstr = "SCount({})".format(maxrecloc) 
            richestimatedstr = "{}({})".format(_linkstr(estimatedstr, pptyname), maxrecloc)
        else:
            countfieldstr = "SCount"
            richestimatedstr = _linkstr(estimatedstr, pptyname)
        if withresidual:
            if len(maxreclist):
                richtestresidualstr = "{}({})".format(_linkstr(testresidualstr, pptyname), maxrecloc)
            else:
                richtestresidualstr = _linkstr(testresidualstr, pptyname)
            extracol = [richestimatedstr, richtestresidualstr, countfieldstr]
        else:
            richtestresidualstr = ""
            extracol = [richestimatedstr, countfieldstr]
        cols.extend(extracol)
        richestimated.append(richestimatedstr)
        richtestresidual.append(richtestresidualstr)
        countfield.append(countfieldstr)
    return countfield, cols, richestimated, richtestresidual

#======================================================================#
@hookable.indirect('mode')
def fillTestFrame(options, source, savedir, testFrame, maintitles=[], 
    modeluse=USE_LIB_FOR_TEST, writer=None, keyTitleList=[], levTitleList=[], 
    verbose=1, debug=0, desc="test"):  #firstcolcount=0, 
    
    with getTrainingModule(options) as drivermodel:
        drivermodel = drivermodel[0]
        drivermodel.loadFromDict(source)
        options.paramCount = drivermodel.paramCount
    
        ni = drivermodel.inputCount
        mess = desc
        with Progress_tqdm(len(testFrame.index), desc="\t"+mess, nobar=verbose<nobarverb) as update:
            for ind, (frameindex, row) in enumerate(testFrame.iterrows()):
                try:
                    inputs = np.asarray(row[0: ni], np.double)
                except ValueError:  # python 2.x
                    inputs = np.asarray(row[1: ni+1], np.double)
                outlevlist = drivermodel.transferleverage(inputs, 'extra')
                for (out, lev), outstr, levstr in zip(outlevlist, keyTitleList, levTitleList):
                    testFrame.at[frameindex, outstr] = out
                    testFrame.at[frameindex, levstr] = lev
                if update:
                    update(ind+1)
            update.flush()
    return testFrame  #, ni

def FinishTestWithGlobalResults(testFrame, targetfieldstr, keyList, levList, 
    maxreclist, richestimated, richtestresidual, countfield, 
    leveragethreshold=1, verbose=1):
    computeFieldList = [testFrame[key] for key in keyList] 
    leveragesFieldList = [testFrame[key] for key in levList] 
    
    testlist = list(zip(maxreclist, richestimated, richtestresidual, countfield))  #[-1::-1]
    testthres = leveragethreshold > 0
    locpattern = []
    for maxrecloc, richestimatedstr, richtestresidualstr, countfieldstr in testlist:
        patternlist = []
        for index in testFrame.index:
            locpattern = []
            scount = 0
            cumul = 0     
            vals = [serie[index] for serie in computeFieldList[:maxrecloc]] 
            levs =  [serie[index] for serie in leveragesFieldList[:maxrecloc]] 
            for val, lev in zip(vals, levs):
                try:
                    index = val.index[0]
                    val = val.at[index][0]
                    lev = lev.at[index][0]
                except: pass
                ok = not testthres or (lev <= leveragethreshold)
                if ok and not np.isnan(val):
                    locpattern.append(0)
                    scount += 1
                    cumul += val
                else:
                    locpattern.append(1)
            if scount:
                valoc = cumul / scount
            else:
                valoc = float('nan')
            testFrame.at[index, richestimatedstr] =  valoc
            testFrame.at[index, richtestresidualstr] = testFrame.at[index, targetfieldstr] - valoc      
#             testFrame.at[index, richtestresidualstr] = valoc - testFrame.at[index, targetfieldstr]   #testFrame.ix[index][1]       
            testFrame.at[index, countfieldstr] = int(scount)
        patternlist.append(locpattern)
    if verbose > 1:
        testFrame[countfieldstr] = testFrame[countfieldstr].astype(np.int)
    return patternlist

def computeTest(options, modeltestframe, IDlist, maxreclist, source, savedir,
        finishTest=None, getExtra=None, verbose=1, verbosexls=1, debug=0):  
    """Calcul du resultat des tests.
    """
    leveragethreshold = options.leveragethreshold
    maintitles = modeltestframe.gettitles()
    maxreccount = len(maxreclist)
    maxrec = maxreclist[0]
    nametitle = maintitles[0]
    pptyname = maintitles[-1]
    inputtitles = maintitles[1:-1]
    testFrameBaseCol = modeltestframe.shape[1]
    testFrame = modeltestframe._frame.copy()
    propertyfield = testFrame.columns[-1]
    countfield, cols, richestimated, richtestresidual = getExtra(
        maxreclist, pptyname, cols=[], richestimated=[], 
        richtestresidual=[])
    targetfieldstr = testFrame.columns[-1]
    
    keyList = [_linkstr(estimatedstr, pptyname, ID) for ID in IDlist]
    levList = [_linkstr(leveragestr, pptyname, ID) for ID in IDlist]
    for key, lev in zip(keyList, levList):
        cols.append(key)
        cols.append(lev)
    fullcol = list(testFrame.columns) + cols
    newcol = OrderedDict({val: float('nan') for val in cols})
    testFrame = testFrame.assign(**newcol)
    testFrame = testFrame[fullcol]  # remise en ordre de testFrame
    inputcount = options.inputcount
    # fill TestFrame is hooked for the mode nn or gm
    testFrame = fillTestFrame(options, source, savedir, testFrame,
        maintitles=maintitles, keyTitleList=keyList, levTitleList=levList, 
        verbose=verbose, debug=debug, desc="\ttest")
# FinishTestWithGlobalResults
    patternlist = finishTest(testFrame, targetfieldstr, keyList, levList, 
        maxreclist, richestimated, richtestresidual, countfield, 
        leveragethreshold, verbosexls)
    
    return testFrame, patternlist, testFrameBaseCol+1, inputcount  #  ici 18/11/2019 le + vient de la collonne de residus
      
def getOrigin(options):
    cond = not hasattr(options, 'origin') or not options.origin
    if cond and options.savefolder and os.path.isdir(options.savefolder):
        options.origin = options.savefolder
    if options.origin:
        if os.path.isdir(options.origin):
            origin = None
            root, _, files = next(os.walk(options.origin))
            cfgfiles = [val for val in files if val.endswith(".cfg")]
            for val in cfgfiles:
                filename = os.path.join(root, val)
                config = defaultedConfigParser(filename)
                if config.has_option('training', 'excelresult'):
                    origin = config.get('training', 'excelresult')
                    break
            if origin:
                options.origin = origin
        elif not os.path.exists(options.origin) and os.path.exists(options.targetfolder):
            options.origin = os.path.join(options.targetfolder, options.origin)
    return options.origin
      
def apiTestResults(resfile, datacount=0, modeltestframe=None, 
        IDlist=[], options = None, testfile="", filetype="", testrange="", 
        testformat=None, maxreclist=[], basedir="", leveragethreshold=5, 
        resindex=0, extraselect="", orderfield="PRESS", outfile=sys.stdout,
        traintype="", gmxfile="", verbose=1, verbosexls=0, todoprint=True, debug=0):
    patternlist = []
    testfile=options.test
    if not options is None:
        filetype=options.filetype 
        testrange=options.testrange 
        testformat=options.testfields
        maxreclist = options.multimaxrec
        basedir=options.workfolder 
        leveragethreshold=options.leveragethreshold 
        extraselect=options.extraselect 
        outfile=options.outfile 
        verbose=options.verbose 
        verbosexls=options.verbosexls
        debug=options.debug
        orderfield = options.orderfield
    doprint = toPrint(outfile)
    testinputColumns = []
    useexistingmodels = (debug & DEMO_USE_EXISTING)
    confResult = None
    if not resfile or not isinstance(resfile, str):
        raise monalError("configuration data file is not correct")
    confResult = defaultedConfigParser(resfile)
    try:
        root = confResult.get("projects", "0")
    except Exception:  #NoSectionError
        root = options.root
        cfgfile = confResult.get(root, 'cfgfile')
        confResult = defaultedConfigParser(cfgfile)
    tablename = confResult.get(root, "tablename")
    pptyname = confResult.get(root, "propertyname")
    pptyunit = confResult.get(root, "propertyunit")
    if not gmxfile:
        if options.lastaction in ['bootstrap', 'bootstraptest'] and \
                hasattr(options, "modelbsfile") and options.modelbsfile:
            gmxfile = options.modelbsfile
        elif options.lastaction in ['loo', 'lootest'] and \
                hasattr(options, "modelloofile") and options.modelloofile:
            gmxfile = options.modelloofile
        elif hasattr(options, "modelfile") and options.modelfile:
            gmxfile = options.modelfile
        else:
            gmxfile = confResult.get(root, "gmxfile")
    sqlFileName = getSqlFileNameFromConf(confResult, root, traintype)
    source = gmxfile
    
    if isinstance(source, text_type):
    
        source = getDictFromGmx(source)
    savedir = os.path.join(basedir, root)
    modulesource = confResult.get(root, "module")
    modulename = os.path.splitext(os.path.basename(modulesource))[0]
    
    if not len(IDlist): 
        with sqlconnect(sqlFileName, detect_types=sqlPARSE_DECLTYPES) as dbConnect:
            reverse = orderfield in C.TCR_MAXIMIZE
            IDlist = getDataFrame(dbConnect, table=tablename, index=None, 
                fieldlist=["ID"], comp=0, orderfield=orderfield, reverse=reverse,
                maxrec=maxreclist[0], extraselect=extraselect)["ID"]
    if not traintype:
            res = computeTest(options, modeltestframe, IDlist,
            maxreclist, source, savedir, 
            finishTest=FinishTestWithGlobalResults,
            getExtra=getExtraFields,
            verbose=verbose, 
            verbosexls=verbosexls, 
            debug=debug) 
            testframe, patternlist, testFrameBaseCol, _ = res
    elif traintype in ['loo', 'lootest']:
        testFrameBaseCol = modeltestframe.shape[1]
        testframe = computeLOOTest(options, modeltestframe, source, 
            savedir=savedir, verbose=verbose, debug=debug) 
    elif traintype in ['bs', 'bootstrap']:
        testFrameBaseCol = modeltestframe.shape[1]
        testframe = computeBSTest(options, modeltestframe, source,
            savedir=savedir, verbose=verbose, debug=debug)
    resultColumn = testFrameBaseCol + 2 
    inputcount = options.inputcount
    if inputcount:
        delta = testFrameBaseCol - inputcount
        testinputColumns = list(range(delta, testFrameBaseCol))

    if verbosexls <= 1:  
    # reduction de dimension de la table pour affichage restreint
        for val in testframe.columns[resultColumn-1:]:
            testframe.drop(val, 1, inplace=True)
    # remplacement du nom de propriete par targetstr dans les champs de testFrame
    if isinstance(testframe, tuple):
        testframe = testframe[0]
    lst = list(testframe.columns)
    for ind, val in enumerate(testframe.columns):
        if val == pptyname or (val.startswith(pptyname) and val[len(pptyname)]=='('):
            lst[ind] = _linkstr(targetstr, pptyname)
            break
    testframe.columns = lst
    if (verbose >= 4) and (testframe is not None):  #and (out file is not None) 
        doprint("test data (leverage threshold = %s):" % leveragethreshold)
        doprint(testframe.to_string(float_format=float_format()))
#     elif (verbose >= 3) and todoprint:
#         doprint("leverage threshold = %s" % leveragethreshold)      
        
    # lire et afficher - le tableau des resultats, le digramme de dispersion du meilleur
#     if not blind:
#         figure = _d rawResult(modulename, pptyname, dataframe, datarange, testframe, testrange, IDlist[resindex], pptyname)
    return testframe, patternlist, pptyname, testFrameBaseCol, gmxfile  #testinputColumns

@connectMgr
def getExtraWeightsFromTable(dbConnect, template, criterion, extraselect, 
        weightfiels='param_end'):
    tableList = getTableListFromDb(dbConnect, template)   
    fieldlist = [weightfiels]
    res = []
    for table in tableList:
        frameloc = getDataFrame(dbConnect, table, fieldlist=fieldlist, 
            orderfield=criterion, extraselect=extraselect)
        try:
            params = frameloc[weightfiels][0]
        except Exception as err:
            params = None
        res.append(params)
    return res
#         model._extraweights[bsindex] = params

@connectMgr
def getBSFrame(dbConnect, options, model):    
    fieldlist = ['param_end', 'StdDev', 'dispersion']  #, "StdDev", "PRESS", "leverages"]
    table = 'trainingResult'
    orderfield = getOrderField(options)
    framelocbase = getDataFrame(dbConnect, table, fieldlist=fieldlist, 
        orderfield=orderfield, extraselect=options.extraselect) #, maxrec=maxrec)
    paramsbase = framelocbase['param_end'][0]
    StdDevbase = framelocbase['StdDev'][0] 
    dispbase = framelocbase['dispersion'][0]
    pptyname = model.propertyName
    targetfield = _linkstr(targetstr, pptyname)
    estimatedfield = _linkstr(estimatedstr, pptyname)
    estimatedfieldM = _linkstr(estimatedfield, "CI95", linker="-")
    estimatedfieldP = _linkstr(estimatedfield, "CI95", linker="+")
    meanBS = _linkstr("BS", meanstr, pptyname)
    meanBSmin = _linkstr(meanBS, "min95")
    meanBSmax = _linkstr(meanBS, "max95")
    columns = [moleculestr,
        targetfield, 
        estimatedfield, 
        estimatedfieldM,
        estimatedfieldP, 
        meanBS, 
        meanBSmin,
        meanBSmax]
    extracol = ["BS_%d"% index for index in range(options.bootstrapcount)]
    columns.extend(extracol)
    outlist = []
    template = tableTemplate['bs']
    targets = model.targets
    molecules = model.modelNames
    for index, (target, molecule) in enumerate(zip(targets, molecules)):
        outbase, IC = model.transferICindex(paramsbase, index, StdDevbase, dispbase)
        reslist = model.transferindex('extra', index)
        outmean = np.mean(reslist)
        outmin, outmax = np.percentile(reslist, (2.5, 97.5))
        loclist = [molecule, target, outbase, outbase-IC, outbase+IC, outmean, outmin, outmax]
        loclist.extend(reslist)
        outlist.append(loclist)
    bsFrame = DataFrame(outlist, columns=columns)
    bsFrame.set_index(moleculestr, inplace=True)
    return bsFrame

def _apiDemoBS(config, options, sourceFrame, resultFrame, model, resfile, mynames=None):  #
    sqlFileName = options.sqlFileName
    base, ext = os.path.splitext(sqlFileName)
    sqlBSFileName = "%s_BS%d_%dT_%dE_%dI%s"% (base, options.bootstraptype, 
        options.bootstrapcount, options.bootstrapepochs, 
        options.bootstrapinittype, ext)
    sqlBSFileName = IndexFilename(sqlBSFileName)
    root = options.root
    config.set(root, 'sqlbootstrapfilename', sqlBSFileName)
    options.sqlBSFileName = sqlBSFileName
    pptyname = config.get(root, "propertyname")
    config.save(options.cfgfile)
    
    if sourceFrame:
        trainFrame = sourceFrame._frame.copy()
        trainresultColumn = sourceFrame.shape[1]
        IDlist = resultFrame.index
    else:
        apiTrainRes = apiReadTrainFrame(options, extratype='bootstrap', mynames=mynames)  #module
        trainFrame, _, _, IDlist, root, trainresultColumn, gmxfile = apiTrainRes

    if trainFrame is None:
        nametitle, smilestitle, pptyname = "", "", "" #maintitles0 
             
    copy_table(sqlFileName, sqlBSFileName, stdTable)    
    with sqlconnect(sqlBSFileName, detect_types=sqlPARSE_DECLTYPES) as dbConnect:
        for ind in range(options.bootstrapcount):
            template = tableTemplate['bs']
            diction = C.EXTRA_TRAIN_DATA.copy()
            createTableDb(dbConnect, template % ind, diction) 
        initlist = getInitList(sqlFileName, options)
        onBSResultLoc = ft.partial(onSpecialResult, dbConnect, tableTemplate['bs'])
        with Progress_tqdm(options.bootstrapcount, desc='\tBootstrap training', 
            nobar=options.verbose<nobarverb) as update:
            resamplingTrainModule(model,     
                inittype=options.bootstrapinittype, 
                initlist=initlist, 
                initcount=options.bootstrapinitcount, 
                epochs=options.bootstrapepochs, 
                BStype=options.bootstraptype, 
                count=options.bootstrapcount,
                weightsstddev=options.initstddev, 
                selected_LOO=None, 
                onReturnResult = onBSResultLoc,
                callBack=update,  #printTo(outfile), 
                LOOcriterion=-C.CRITER_PRESS,
                trainstyle=options.trainstyle,
                seed=options.seed)
            update.flush()
        gm0 = getModelDictFromConfig(config)
        indexlist = IDlist
        extrasize = options.bootstrapcount
        neurotype = 'nn1'
        gmxfileBS = getGmxFileAndSave(dbConnect, gm0, config, indexlist, options, 
            neurotype, extrasize=extrasize, dosave=True)  # ici gmx
        config.set(root, "gmxfilebs", gmxfileBS)
        config.save()
    
        trainresultColumn = trainFrame.shape[1]
        model.extraweights = getExtraWeightsFromTable(dbConnect, 
                                tableTemplate['bs'], 
                                options.orderfield, 
                                options.extraselect)
        bsFrame = getBSFrame(dbConnect, options, model)  
        
#         model, bsTrainFrame, gmxfileBS, sqlBSFileName, IDlist, \
#             BSResultTrainColumn = res
        
    return model, bsFrame, gmxfileBS, sqlBSFileName, IDlist, trainresultColumn

def _apiDemoLOO(config, options, sourceFrame, resultFrame, model, seed=None, mynames=None):
    sqlFileName = options.sqlFileName
    base, ext = os.path.splitext(sqlFileName)
    sqlLOOFileName = "%s_LOO_%dT_%dE_%dI%s"% (base, options.looinitcount, options.looepochs, options.looinittype, ext)
    sqlLOOFileName = IndexFilename(sqlLOOFileName)
    root = options.root
    config.set(root, 'sqlloofilename', sqlLOOFileName)
    options.sqlLOOFileName = sqlLOOFileName
    pptyname = config.get(root, "propertyname")
    config.save(options.cfgfile)
        
    if sourceFrame:
        trainFrame = sourceFrame._frame.copy()
        trainresultColumn = sourceFrame.shape[1]
        IDlist = resultFrame.index
    else:
        apiTrainRes = apiReadTrainFrame(options, extratype='loo', mynames=mynames)  #module
        trainFrame, IDlist, root, trainresultColumn, gmxfile = apiTrainRes
        
    if trainFrame is None:
        nametitle, smilestitle, pptyname = "", "", "" #maintitles0   
    copy_table(sqlFileName, sqlLOOFileName, stdTable)    
    
    with sqlconnect(sqlLOOFileName, detect_types=sqlPARSE_DECLTYPES) as dbConnect:
        for ind in range(model.dataCount):  # vérifier ici si baselen ne doit pas etre lu depuis config
            diction = C.EXTRA_TRAIN_DATA.copy()
            template = tableTemplate['loo']
            createTableDb(dbConnect, template% ind, diction) 
        
        initlist = getInitList(sqlFileName, options)
        onBSResultLoc = ft.partial(onSpecialResult, dbConnect, tableTemplate['loo'])
        with Progress_tqdm(model.dataCount, desc='\tLOO CV', 
            nobar=options.verbose<nobarverb) as update:
            loccount, resultMatrix = resamplingTrainModule(model,     
                inittype=options.looinittype, 
                initlist=initlist, 
                initcount=options.looinitcount, 
                epochs=options.looepochs, 
                BStype=RE_LOO, 
                weightsstddev=options.initstddev, 
                selected_LOO=None, 
                onReturnResult = onBSResultLoc,
                callBack=update,
                LOOcriterion=-C.CRITER_PRESS,
                trainstyle=options.trainstyle,
                seed=seed)
            update.flush()
        gm0 = getModelDictFromConfig(config)
        indexlist = list(IDlist)
        extrasize = model.dataCount 
        neurotype = 'nn1'
        gmxfileLOO = getGmxFileAndSave(dbConnect, gm0, config, None, options,  #indexlist, 
            neurotype, extrasize=extrasize, dosave=True)  # ici gmx
        config.set(root, "gmxfileloo", gmxfileLOO)
        config.save()
        datacount = max(model.modelCount, model.dataCount)
        if not datacount and not sourceFrame is None:
            datacount = sourceFrame.shape[0]
        trainresultColumn = trainFrame.shape[1]
        trainFrame, _ = getLOOFrame(dbConnect, options, trainFrame) 
    # end of dbConnect context 
    return model, trainFrame, gmxfileLOO, sqlLOOFileName, IDlist, trainresultColumn

def apiReadTrainFrame(options, extratype='', mynames=None):
    """Recupere le trainFrame avant le les training supplementaires (LOO, BS)
    """ 
    if not options.test:
        options.test = options.source
    try:
        row = gettitles(options.test, options.filetype, 
            datarange=options.testrange, datafmt=options.testfields)  #, titlesfirst=True)
        return  apiTrainResults(options, resfile=None, titles=row, extratype=extratype, mynames=mynames)   #titles
    except Exception as err:
        print(err)
        raise
#        return None, None, "", "", -1, ""
           
def resamplingTrainModule(module, inittype=C.INIT_START_PARAM, initlist=[], 
        initcount=1, count=0, epochs=0, BStype=RE_NONE, weightsstddev=0.1,
        computeDispersion=False, selected_LOO=None, LOOcriterion=-1,
        callBack=None, onReturnResult=None, trainstyle=0, seed=-1):
    """Launching a special training session. Special may mean Leave-One-out or Bootstrap.
    Parameters:
    
        - module -> In memory training module.
        
        - inittype ->  . Default INIT_START_PARAM
        
            Available:
            
            - INIT_START_PARAM -> Initialization with the parameters of the starting train process
            
            - INIT_END_PARAM -> Initialization with the parameters at the end of the training process
            
            - INIT_RANDOM -> Random initialization.
        
        - initlist -> Rekated to super training.ƒ
            Initialization parameters list. Each item of this list is 
            a tuple of at least 4 elements. Element 2 is used with 
            INIT_END_PARAM inittype, and element 3 is used with INIT_START_PARAM 
            inittype. Default []
        
        - inicount -> Number of initialization for Leave-One-out. Default 1
        
        - count -> Number of Bootstrap resampling. Meaningless for Leave-One-out. Default 0
        
        - epochs -> Training epochs. Default 0
         
        - BStype -> Resampling type. Default RE_NONE
        
            Available:
            - RE_NONE -> no resampling
            
            - RE_BS_STD -> standard Bootstrap.
            
            - RE_BS_RESIDU -> residual Bootstrap.
            
            - RE_LOO -> Leave-One-Out.

        - computeDispersion -> Compute leverages and dispersion matrix. Default False
         
        - selected_LOO -> Debug. With serial training only. List of selected initialization in training base list. Default None
        
        - LOOcriterion -> selection criterion for LOO result. Default CRITER_PRESS
        
            Available: 
            
            - CRITER_STDDEV -> minimum standard deviation 
            
            - CRITER_PRESS -> minimum PRESS
            
            - CRITER_LEV -> minimum pseudo-leverage
        
        - callBack -> Follow up callback function. Default None
    
    return
    
        - loccount -> Number of local training performed.
        
    Constants are defined in module monal.monalconst
    """

    assert(isinstance(module, DriverLib))
    if trainstyle > 0:
        try:
            trainstylemem = module.lib.gettrainstyle()
            ntrainstyle = trainstyle | trainstylemem
            module.lib.settrainstyle(ntrainstyle)
        except:
            pass
                        
    if BStype == RE_LOO:
        res = module.trainLOO(inittype=inittype, initlist=initlist, 
            initcount=initcount, weightsstddev=weightsstddev, epochs=epochs, 
            selected_LOO=selected_LOO, LOOcriterion=LOOcriterion, 
            callback=callBack, onReturnResult=onReturnResult, 
            trainstyle=trainstyle, seed=seed)  #, parallel=False
    elif BStype == RE_SUPER:
        res = module.trainSuper(inittype=inittype, initlist=initlist, 
            initcount=initcount, weightsstddev=weightsstddev, BScount=count, 
            epochs=epochs, selected_LOO=selected_LOO, callback=callBack, 
            onReturnResult=onReturnResult, trainstyle=trainstyle, seed=seed)
    elif BStype in BSGROUP:
        res = module.trainBS(inittype=inittype, initlist=initlist, 
            initcount=initcount, weightsstddev=weightsstddev, BScount=count, 
            epochs=epochs, BStype=BStype, selected_LOO=selected_LOO, 
            LOOcriterion=LOOcriterion, callback=callBack, 
            onReturnResult=onReturnResult, trainstyle=trainstyle, seed=seed)
    # mettre trainstyle=0  ???
    if trainstyle > 0:
        try:
            module.lib.settrainstyle(trainstylemem)
        except:
            pass
    return res
  
def getOrderField(options, default="ID"):
    try:
        if options.curaction in ['loo', 'lootest']:
            return options.looorderfield
        if options.curaction in ['botstrap', 'bs', 'bootstraptest', 'bstest']:
            return options.bootstraporderfield
        else:
            return options.orderfield
    except:
        return default

def _hasTrain(options):
    return len(intersection(options.actionlist, ['train', 'loo', 'bootstrap']))


def _hasTest(options):
    return len(intersection(options.actionlist, ['test', 'lootest', 'bootstraptest']))


def _actionListMgmt(llist):
    def replaceInList(mylist, target, substitute=[], exclusive=False):
        try:
            ind = mylist.index(target)
            if exclusive:
                mylist = substitute
            else:
                mylist = mylist[:ind] + substitute + mylist[ind+1:]
        except ValueError:
            pass
        return mylist
            
    llist = [val.lower() for val in llist]
    llist = [val if not val.startswith('bs') else val.replace('bs', 'bootstrap') for val in llist]
    
    llist = replaceInList(llist, 'alltraintest', ['train', 'test', 'loo', 'lootest', 'bootstrap', 'bootstraptest'], True)
    llist = replaceInList(llist, 'allall', ['train', 'test', 'loo', 'lootest', 'bootstrap', 'bootstraptest'], True)
    llist = replaceInList(llist, 'all', ['train', 'test'])
    llist = replaceInList(llist, 'looall', ['loo', 'lootest'])
    llist = replaceInList(llist, 'lootraintest', ['loo', 'lootest'])
    llist = replaceInList(llist, 'bootstrapall', ['bootstrap', 'bootstraptest'])
    llist = replaceInList(llist, 'bootstratraintest', ['bootstrap', 'bootstraptest'])
    
    return llist
 
def getExcelFileName(options, forcename="", ext=".xlsm"):
    sourceroot = options.root  
    fname = os.path.join(options.targetfolder, sourceroot)
    decor = []
    if forcename:
        fname = "{}_{}".format(fname, forcename) 
        decor = ['_']
    return decorfile(fname, options, ext, decor=decor, indextemplate="(%s)")

def saveFrameToExcel(options, frame, excelwriter, sheetname, actionName=""):
    if frame is None:
        return  
    if not actionName:
        actionName = options.lastaction
    if frame.shape[0] and frame.shape[1] and options.copytype:
        if options.copyexcel:
            frame.to_excel(excelwriter, sheetname)  
            excelwriter.book.set_custom_property('{0}count'.format(actionName), frame.shape[0], 'number')
        elif options.copytxtcsv and os.path.exists(options.targetfolder):
            fname = os.path.join(options.targetfolder, '{0}Frame'.format(actionName))
            fname = decorfile(fname, options, ".%s"% options.copytype, indextemplate="(%d)") 
            with open(fname, 'w') as ff:
                ff.write(frame.to_csv(sep=options.sep, decimal=options.decimal))

def CloseExcelwriter(options, excelwriter, forcename="", forbiden=[], Sheet=None, decor=[]):
    sourceroot = options.root 
    if forcename:
        sourceroot = "{}_{}".format(sourceroot, forcename) 
        if hasattr(options, "probecount"):
            decor.append('probecount')
        if options.seed > 0:
            decor.append('seed')
        if hasattr(options, "randomSource"):
            decor.append("randomSource")
        
        if not len(decor):
            decor = ["_"]
    fname = os.path.join(options.targetfolder, sourceroot)
    excelresult = decorfile(fname, options, ".xlsm", decor=decor, forbiden=forbiden, indextemplate="(%s)")
    workbook = excelwriter.book
    workbook.set_size(1490, 1300)
    vbaProjectBin = getVbaProjectBin()  #options.binfolder
    if vbaProjectBin:
        workbook.add_vba_project(vbaProjectBin)
        workbook.set_vba_name('ThisWorkbook')
    else:
        excelresult = decorfile(fname, options, ".xlsx", decor=decor, forbiden=forbiden, indextemplate="(%s)")
    enrichSimpleSheet(workbook, Sheet, None, excelwriter)
    # ecriture du fichier Excel et fermeture du writer
    excelwriter.save()
    tempres = excelwriter.path
    workbook.close()  # ajout du 19/04/2019
    excelwriter.close()
    os.chmod(tempres, 0o666)
    os.rename(tempres, excelresult)
    excelwriter = None
    return excelresult

##     fname = filename
#     if options.copyexcel:
#         tempstr = ''.join(choice(ascii_uppercase) for _ in range(8))
#         if not fname:
#             fname = os.path.join(options.targetfolder, "{0}.xlsx".format(tempstr))
#         excelwriter = ExcelWriter(fname, engine='xlsxwriter')
#         Frame.to_excel(excelwriter, sheetname)  #, index=with index)
#     elif options.copytxtcsv and os.path.exists(options.targetfolder):
#         if not fname:
#             fname = os.path.join(options.targetfolder, 'resultFrame')
#         fname = decorfile(fname, options, ".{0}".format(options.copytype), indextemplate="(%d)")                    
#         with open(fname, 'w') as ff:
#             ff.write(Frame.to_csv(sep=options.sep, decimal=options.decimal))
#     return fname, excelwriter

def _getBestWeights(dbConnect, options):
    table = options.datatable
    maxrec = options.maxrec 
#    basedir = options.folder
    extraselect = options.extraselect 
    extraselectrelaxed = options.extraselectrelaxed 
    orderfield = options.orderfield
    verbose = options.verbosexls
    fieldlist = ['ID', 'param_end']
    resultFrame = getDataFrame(dbConnect, table=table, index="ID",
        fieldlist=fieldlist, comp=0, maxrec=1, 
        extraselect=extraselect, orderfield=orderfield, reverse=False, 
        substitute=C.SUBSTITUTE_FIELD)
    try:
        wgt = resultFrame['param_end'][0]
    except IndexError:
        wgt = None
    return wgt

def getResultFrame(dbConnect, options=None, resfile="", 
        table=stdTable, maxrec=10, basedir="", extraselect="", 
        orderfield="PRESS", verbosexls=0):
    
    if not options is None:
        table = options.datatable
        maxrec = options.maxrec 
        basedir = options.workfolder  #folder
        extraselect = options.extraselect 
        extraselectrelaxed = options.extraselectrelaxed 
        orderfield = options.orderfield
        verbosexls = options.verbosexls
    
    if not isinstance(dbConnect, sqlConnection):
        if resfile and isinstance(resfile, str):
            confResult = defaultedConfigParser(resfile)
            cfgfile = confResult.get(options.root, "cfgfile")
            if os.path.exists(cfgfile):
                confResult = defaultedConfigParser(cfgfile)
                root = confResult.get("projects", "0")
                savedir = os.path.join(basedir, root)
                if hasattr(options, "sqlFileName") and options.sqlFileName:
                    sqlFileName = options.sqlFileName
                else:
                    sqlFileName = confResult.get(root, "sqlfilename")
                dbConnect = sqlconnect(sqlFileName, detect_types=sqlPARSE_DECLTYPES)
                options.sqlFileName = sqlFileName
                options.modulename = confResult.get(root, "module")
                if demodebug & DEMO_DEBUG_USAGE:
                    print("sqlFileName", sqlFileName)  
    if verbosexls > 3:
        fieldlist = ["ID", "StdDev", "PRESS", 'RoundoffTest', "DeltaRank", "R2", 
            "Determinant", "Conditionning",  "CorrelMean", "EigenMin",  
            "EigenMax",  "Mu",  "Correl",  "CorrelMax", "StdDevBiasless", 
            "Trace", "Epochs", "Hidden", "seed"]  #, "AdjustedR2"
    elif verbosexls == 3:
        fieldlist = ["ID", "StdDev", "PRESS", "RoundOffTest", "DeltaRank", "seed"]
    elif verbosexls == 2:
        fieldlist = ["ID", "StdDev", "PRESS", "seed"]
    else:
        fieldlist = ["ID", "StdDev", "PRESS"]
        
    reverse = orderfield in C.TCR_MAXIMIZE 
    index = 'ID'  if 'ID' in  fieldlist else None
    resultFrame = getDataFrame(dbConnect, table=table, index=index,
        fieldlist=fieldlist, comp=0, maxrec=maxrec, 
        extraselect=extraselect, orderfield=orderfield, reverse=reverse, 
        substitute=C.SUBSTITUTE_FIELD)
    if 'ID' in resultFrame.columns:
        resultFrame.set_index('ID', inplace=True)
        
    return resultFrame

def apiCreateExcelAndResultFrame(options, resultFrame, #resultsheetname=None, 
        excelwriter=None, resfile=None, doprint=doNothing):
    tempres = ""
    if options.copyexcel and not excelwriter:
        tempstr = ''.join(choice(ascii_uppercase) for _ in range(8))  # nom aleatoire
        tempres = os.path.join(options.targetfolder, "%s.xlsx"% tempstr)  # nom de fichier excel aleatoire
        excelwriter = ExcelWriter(tempres, engine='xlsxwriter')
    if not resfile:
        resfile = os.path.join(options.savedir, "train.cfg")
        if options.maxrec:
            for maxcount in range(1, options.maxrec+1):
                temp = os.path.join(options.savedir, "train_{0}.cfg".format(maxcount))
                if os.path.exists(temp):
                    resfile = temp
                    break
    if options.notrain:
        sourceroot = options.root  #os.path.splitext(os.path.basename(options.source))[0]
        if not options.savedir:
            options.savedir = os.path.join(options.workdir, sourceroot)
#            options.savedir = os.path.join(options.folder, sourceroot)
            if not os.path.exists(options.savedir):
                os.makedirs(options.savedir)
            else:
                options.savedir = IndexFilename(options.savedir, "_{0}", last=True)            
        if options.savefolder:
            origin = getOrigin(options)
            if origin:  # ici
                dico = getcustomproperties(options.origin, 'Utilities')
                if not len(dico):
                    updateOptionsFromGmx(options, options.origin)
#                     dico = getDictFromGmx(options.origin)
#                     !!!!
                else:
                    for key, value in dico.items():
                        if key == 'Hidden neurons': 
                            options.hidden = value
                        elif key == 'Configuration string': 
                            options.configstr = value
                        elif key == 'Data count': 
                            options.datacount = value
                        elif key ==  'Training init count': 
                            options.initcount = value
                        elif key == 'Training epochs': 
                            options.epochs = value
                        elif key == 'Test selection threshold': 
                            if isinstance(value, text_type):
                                value = value[:3]
                            options.leveragethreshold = float(value)
                        elif key == 'Best trainings': 
                            options.maxrec = value
                        elif key == 'Random seed': 
                            options.seed = value
                        elif key == "SQL file":
                            options.sqlFileName = make_intern(value, options)
                        elif key == "SQL LOO file":
                            options.sqlLOOFileName = make_intern(value, options)
                        elif key == "Model file":
                            options.modelfile = make_intern(value, options)
                        elif key == "Model BS file":
                            options.modelbsfile = make_intern(value, options)
                        elif key == "Model LOO file":
                            options.modelloofile = make_intern(value, options)
        if not options.notrain or not(options.origin.endswith('nnx') or options.origin.endswith('gmx')):
            resultFrame = getResultFrame(None, options, resfile)
            if not resultFrame.shape[0]:
                st = "All the trained models are degenerated. The full rank condition is now relaxed\n"
                doprint(st)
                options.extraselect = options.extraselectrelaxed
                resultFrame = getResultFrame(None, options, resfile)
    return excelwriter, resfile, resultFrame, tempres


@hookable.indirect('mode')
def getTrainingModule(options, dataframe=None, config=None, outputdir="", 
        originbase="", unitfilename="", keeptemp=0,
        compiler="", outfile=sys.stdout, verbose=0, doprinttime=False, 
        debug=0, progress=None, callbackcentral=None):  #
    """Fournit un modèle compilé defini par les paramètres de options.
    On definit le nom du fichier recherché, puis on recherche s'il existe.
    S'il n'existe pas, il est crée.
    Ce modèle créé est générique. Aucun nom d'entrée ou de sqortie, et aucun 
    dimensionnement de la mémoire pour les données.
    """
    servicelist = []
    #if ext is None:
#    dataframe = sourceframe
    extrares = None
    ext = libExtension()
    doprinttime = options.verbose
    savedir = options.libfolder  #options.workfolder
    if not savedir:
        savedir = options.savedir
    if dataframe:
        inputs = dataframe.fieldsOf('inputs')
        outputs = dataframe.fieldsOf('outputs')
    elif not options.notrain:
        inputs = options.datafields[options.grouplist.index('inputs')]
        outputs = options.datafields[options.grouplist.index('outputs')]
    else:
        inputs = options.testfields[options.grouplist.index('inputs')]
        outputs = options.testfields[options.grouplist.index('outputs')]
    ni = len(inputs)
    nh = options.hidden
    no = len(outputs)
    netname = "nn_{0}_{1}_{2}".format(ni, nh, no)
    modulename = "lib{0}{1}".format(netname, ext)
    fullmodelname = os.path.join(savedir, modulename)
    modeldata = ModelData(input=ni, output=no, hidden=nh, name=netname)
    modelmode = ""
    if not options.modelcreation and os.path.exists(fullmodelname):
        lib = loadModule(fullmodelname)  
        OK = False if lib is None else lib.OKVersion
        modelmode = "load"
        if OK:
#             if options.verbose >= 3 and outfile:
#                 outfile.write("\tloaded {0}\n".format(modulename))
            lib.modeldata = modeldata
            lib.modelmode = modelmode
            return lib  #, fullmodelname, modeldata, modelmode
        if lib:
            lib.__del__()
        lib = None
    if os.path.exists(fullmodelname):
        removemodule(fullmodelname)
    try:
        base = appdatadir("", "metaphor")
        tempdir = os.path.join(base, "temp", str(options.keeptemp))
#         if options.keeptemp  and (options.keeptemp != 1):
#             if outfile and (doprinttime >= 2):
#                 outfile.write("tempdir: %s\n"% tempdir)#                 cleanDir(tempdir, d oprint=True, stoponerror=False, writer=outfile)
#         if not os.path.exists(tempdir):
#             os.makedirs(tempdir)
        with FanWait('\tcompiling', outfile, interval=0.2, dotime=doprinttime):
            modulename = createModule(modeldata, savedir, tempdir, options.keeptemp)
        modelmode = "compile"
        if savedir:
            modulename = os.path.join(savedir, modulename)
#         if options.verbose >= 3 and outfile:
#             outfile.write("compiled {0}\n".format(modulename))
    except:
        raise
    lib = loadModule(modulename)
    lib.modeldata = modeldata
    lib.modelmode = modelmode
    return lib, servicelist


def createModule(modeldata, savedir="", tempdir="", keeptemp=0, trainable=True):
    driver = Driver(modeldata=modeldata)
    driver.mainModel.trainable = trainable
    driver.modelType = 3
    driver.mainModel.mark = "Model created with metaphor.monal {0}".format(monalversion)
    savingformat = C.SF_DLLTRAIN if trainable else  C.SF_DLL
    modulename = driver.saveModel(savingformat=savingformat, savedir=savedir, 
        tempdir=tempdir, package="", keeptemp=keeptemp, verbose=0, compiler="", 
        forcelib=False)  #, appliname="metaphor")
    return modulename

def prepareUsageAction(options=None, modelfile=None, data=""):
    inputnames = []
    outputnames = []
    datalist = []
    
    datamode = 'single'
    if modelfile is None:  #
        modelfile = options.origin    
    if data is None or data == "":
        data = options.usagedata
    if data is None or data == "":
        data = options.source
        datamode = 'multi'
    if isinstance(data, list):
        options.datalist = data
        data = data[0]
    else:
        options.datalist = [data]
    if data and data.startswith('@'):
        data = data[1:]
        datamode = 'multi'
    source = getDictFromGmx(modelfile)
    xml = source['xml'] if 'xml' in source.keys() else ""
    xml = xml if not xml.startswith('unknown') else ""
    extracount = 0
    if 'extraweights' in source and source['extraweights'] is not None:
        #ewshape = source['extraweights'].shape
        if source['extraweights'].ndim == 2:
            extracount = source['extraweights'].shape[0]
    mode = 'gm' if 'occurence' in source.keys() else 'nn'  #  ici GM
    modeldict = source["model"]
    hidden = int(modeldict["hidden"])    
    if 'inputnames' in modeldict and modeldict['inputnames']:
        inputnames = modeldict['inputnames'].split(',')
    if 'outputname' in modeldict:
        outputnames = modeldict["outputname"].split(',')
    if not len(outputnames) or not outputnames[0]:
        outputnames = [options.propertyname]
    ni = len(inputnames)
    no = len(outputnames)
    if options.debug & DEMO_DEBUG_USAGE:
        print('previous grouplist', options.grouplist)    
    dsize = -1
    grouplist = []
    if datamode == "single":
        datafulllist = []
        for st in options.datalist:
            datalist = []
            lst = st.split(";")
            testlen = len(lst)
            if testlen > 1:
                for val in lst:
                    sublst = val.split(",")
                    sublst2 = []
                    for subval in sublst:
                        try:
                            subval2 = float(subval)
                            dsize = get_decimal_size(subval2)
                        except:
                            subval2 = subval
                        sublst2.append(subval2)
                    datalist.append(sublst2)
            else:   
                datalist = []
                for val in st.split(","):
                    try:
                        val2 = float(val)
                        dsize = get_decimal_size(val2)
                    except:
                        val2 = val
                    datalist.append(val2)
                datalist = [datalist]
                testlen = len(datalist)
            if not hasattr(options, "grouplist") or options.grouplist == []:
                if mode == 'nn':
                    if testlen == 3:
                        options.grouplist = ['identifiers', 'inputs', 'outputs']
                    elif testlen == 2: 
                        if isinstance(datalist[0][0], str):
                            options.grouplist = ['identifiers', 'inputs']  
                        else:
                            options.grouplist = ['inputs', 'outputs']  
                    elif testlen == 1: 
                        options.grouplist = ['inputs'] 
                elif mode == 'gm':  # ici GM
                    if testlen == 3: 
                        options.grouplist = ['identifiers', 'smiles', 'outputs'] 
                    elif len(datalist) == 1:
                        options.grouplist = ['smiles']
                    elif testlen == 2:
                        if isinstance(datalist[1][0], str):
                            options.grouplist = ['identifiers', 'smiles'] 
                        else:
                            options.grouplist = ['smiles', 'outputs'] 
            if 'outputs' in options.grouplist:
                test = datalist[options.grouplist.index('outputs')][0]
                if not isFloat(test):
                    datalist = datalist[:-1]
                    options.grouplist = options.grouplist[:-1]
            datafulllist.append(datalist)
        grouplist = ['targets' if val == 'outputs' else val  for val in options.grouplist]
        datalist = datafulllist
    else: # mode 'multi'
#        options.actionlist = ['analyse', 'usage']
        res = analyseDataFiles(options=options, forceAnalyse=True, doprint=doNothing)#     return sourcefile, datafiletype, datarange, datafields, \
        options.source = res[0]
        options.filetype = res[1] 
        options.datarange = res[2]
        options.datatitles = res[3]
        datalist = options.datatitles
        options.datafields = res[4]
        options.test = res[5]
        options.source = options.source if options.source else options.test
        options.testfiletype = res[6] 
        options.testrange = res[7]
        options.testtitles = res[8]
        options.testfields = res[9]
        options.configstr = res[10]
        options.grouplist = res[11]
        grouplist = options.grouplist
        options.classif = res[12]
        data = options.source
        config = res[13]
        ranges = res[14] 
        commonFieldExclude = res[15] 
        options.datatitles = res[16]
    
    if options.debug & DEMO_DEBUG_USAGE:
        print('datamode', datamode)
        print('mode', mode)
#         print('grouplist', grouplist)
                
    return datamode, data, source, mode, inputnames, outputnames, hidden, datalist, grouplist, extracount, xml, dsize

def getSumaryFrame(resultFrameList, options):
    drow0 = max(options.multimaxrec)
    drow = 3 * drow0 
    dcol = 1 + len(options.multihidden)
    
    arr = np.zeros((drow, dcol))
    bsname = "Best selection"
    cols = [bsname]
    for hidden in options.multihidden:
        cols.append("%dN"% hidden)
    sumaryFrame = DataFrame(arr, columns=cols)
    rg = []
    for ind in range(drow0):
        rg.append("Avg VLOO(%d)" % (ind+1))
        rg.append("StdDev VLOO(%d)" % (ind+1))
        rg.append("avg RMSE(%d)" % (ind+1))
    sumaryFrame[bsname] = rg
    for hidden, frame, _ in resultFrameList:
        avgstdscores = []
        for ind in range(drow0):
            lst = frame["VLOO score"][:ind+1]
            val = lst.sum()/(ind+1)
            stdvloo = lst.std() if ind else 0
            lst2 = frame["RMSE"][:ind+1]
            val2 = lst2.sum()/(ind+1)
            avgstdscores.append(val)
            avgstdscores.append(stdvloo)
            avgstdscores.append(val2)
        sumaryFrame["%dN"% hidden] = avgstdscores

    return sumaryFrame 

def excelRecapitulation(options, resultFrameList, modeldic, gmCustomProperties, doprint):
    recapFrame = getSumaryFrame(resultFrameList, options)
    lst = [val[0] for val in resultFrameList]
    st = strintlist(lst, compact=True, groupdelimiter="--")
    recapSheetName = "Recap_{0}N".format(st) # 
    excelwriter, resfile, recapFrame, tempres = \
        createExcelRecapAndResultFrame(options, recapFrame, 
            recapSheetName, doprint=doprint)
    
    nametemplate = "summary %dN"
    for index, (hidden, frame, _) in enumerate(resultFrameList):
        fname = nametemplate % hidden
        frame.to_excel(excelwriter, fname, index=True)  #, startcol=1)
    if options.copytxtcsv:
        pass
    if options.copyexcel:
        sourceroot = "%s_RECAP"% options.root  
        fname = os.path.join(options.targetfolder, sourceroot)
        excelresult = decorfile(fname, options, ".xlsm", 
            indextemplate="(%s)", multihidden=True)
        modeldic["hiddenlist"] = options.multihidden
        modeldic['paramCount'] = [val[2] for val in resultFrameList]
        modeldic['bestCount'] = options.multimaxrec
        if hasattr(options, "configstrMem"):
            modeldic['configmem'] = options.configstrMem
        
        excelwriter, _ = initiateExcelWriter(excelwriter, modeldic, # ici modif du 11/01/20 ajout "_"
            gmCustomProperties, origin=options.savedir, recap=True)

        enrichRecapExcelFile(excelwriter, options, recapSheetName, 
            recapFrame, nametemplate, resultFrameList)
        
        filename = make_extern(excelresult, options)
        doprint("Writing recapitulation results in file: {}".format(filename))       
        # ajout de la macro autorisant les sauvegardes directes des xlsx
        # meme apres calcul des formules
        workbook = excelwriter.book
        workbook.set_size(1490, 1175)
        vbaProjectBin = getVbaProjectBin()  #options.binfolder
        workbook.add_vba_project(vbaProjectBin)
        workbook.set_vba_name('ThisWorkbook')
        # ecriture du fichier Excel et fermeture du writer
        workbook.close()
        excelwriter.close()
        excelwriter.save()
        os.chmod(tempres, 0o666)
        os.rename(tempres, excelresult)

def createExcelRecapAndResultFrame(options, resultFrame, 
        resultsheetname=None, excelwriter=None, startswithtest=False, 
        resfile=None, doprint=doNothing):  #outfile=None, wit hindex=False, 
    tempres = ""
    if options.copyexcel and not excelwriter:
        tempstr = ''.join(choice(ascii_uppercase) for _ in range(8))  # nom aleatoire
        tempres = os.path.join(options.targetfolder, "%s.xlsx"% tempstr)  # nom de fichier excel aleatoire
        excelwriter = ExcelWriter(tempres, engine='xlsxwriter')
    if startswithtest:
        sourceroot = options.root  #os.path.splitext(os.path.basename(options.source))[0]
        if not options.savedir:
            if options.savefolder:
                if options.origin:  # 
                    dico = getcustomproperties(options.origin, 'Utilities')
                    options.hidden = dico['Hidden neurons']
                    options.configstr = dico['Configuration string']
                    options.initcount = dico['Training init count']
                    options.epochs = dico['Training epochs']
                    options.leveragethreshold = dico['Test selection threshold']
                    options.maxrec = dico['Best trainings']
                    options.seed = dico['Random seed']
                options.savedir = options.savefolder
            else:
                options.savedir = os.path.join(options.workfolder, sourceroot)
                if not os.path.exists(options.savedir):
                    os.makedirs(options.savedir)
                else:
                    options.savedir = IndexFilename(options.savedir, "_{0}", last=True)
        if not resfile:
            resfile = os.path.join(options.savedir, "train.cfg")
            if options.maxrec:
                for maxcount in range(1, options.maxrec+1):
                    temp = os.path.join(options.savedir, "train_{0}.cfg".format(maxcount))
                    if os.path.exists(temp):
                        resfile = temp
                        break
            
        resultFrame = getResultFrame(None, options, resfile)
        if not resultFrame.shape[0]:
            st = "All the trained models are degenerated. The full rank condition is now relaxed\n"
            doprint(st)
            options.extraselect = options.extraselectrelaxed
            resultFrame = getResultFrame(None, options, resfile)
    if (resultFrame is not None) and options.copytype:
        if options.copyexcel:
            resultFrame.to_excel(excelwriter, resultsheetname)  #, index=with index)
        elif options.copytxtcsv and os.path.exists(options.targetfolder):
            fname = os.path.join(options.targetfolder, 'resultFrame')
            fname = decorfile(fname, options, ".%s"% options.copytype, indextemplate="(%d)")                    
            with open(fname, 'w') as ff:
                ff.write(resultFrame.to_csv(sep=options.sep, decimal=options.decimal))
                
    return excelwriter, resfile, resultFrame, tempres

@connectMgr
def getInitList(dbConnect, options, indexhead=0):
    initlist = []
    fieldlist = ["ID", "prevID", paramStartStr, paramEndStr, dispStr, roundOffTestStr]
    orderfield = getOrderField(options)
    frameLoc = getDataFrame(dbConnect, table=stdTable, index=None,  
        fieldlist=fieldlist, comp=0, maxrec=options.maxrec, extraselect=options.extraselect, 
        orderfield=orderfield, reverse=False, substitute=C.SUBSTITUTE_FIELD)
    initlist = [tuple(frameLoc.ix[index]) for index in range(frameLoc.shape[0])]
    # Future warning "ix"
    return initlist
    
@connectMgr
def getLOOFrame(dbConnect, options, sourceFrame):
    datacount = sourceFrame.shape[0]
    sourceindex = sourceFrame.index
    pptyname = options.propertyName
    fielddict = {
        'out': "LOO_{0}_{{0}}".format(pptyname),
        "StdDev": "LOO_{0}_RMSE_{{0}}".format(pptyname), 
        "PRESS": "LOO_{0}_VLOO_{{0}}".format(pptyname), 
        "leverages": "LOO_{0}_Leverage_{{0}}".format(pptyname)
        }
    meanField = _linkstr(estimatedstr, "LOO_{0}".format(pptyname))
    targetfield = _linkstr(targetstr, pptyname)
    estimationerrorfield = _linkstr(trainresidualstr, "LOO_{0}".format(pptyname))
    maxrec = min(options.loomaxrec, options.looinitcount)  # 
    fieldlist = ['out', "leverages", "StdDev", "PRESS"]
    if options.verbosexls > 1:
        loowidth = 4
    else:
        loowidth = 2
    fieldlist = fieldlist[:max(2, loowidth)]
    extraselect = options.extraselect
    selectOnlev = options.looleveragethreshold > 0
    template = tableTemplate['loo']
    if options.looinittype != 2:
        extraselect = ""
    elif selectOnlev:
        levselect = "(leverages < {0})".format(options.looleveragethreshold)
        extraselect = "({0} AND {1})".format(extraselect, levselect)
    if options.verbosexls > 1:
        cols = [meanField, estimationerrorfield, "SCount"] 
        for index in range(maxrec):
            locfieldlist = [fielddict[val].format(index) for val in fieldlist]
            cols.extend(locfieldlist)
    else:
        cols = [meanField, estimationerrorfield]
    fullcol = list(sourceFrame) + cols
    newcol = OrderedDict({val: float('nan') for val in cols})
    looFrame = sourceFrame.assign(**newcol)  
    looFrame = looFrame[fullcol]
    looFrame.rename(columns={pptyname: targetfield}, inplace=True)      
    orderfield = getOrderField(options)
    for molindex, molname in enumerate(sourceindex):
        # pour chaque molecule, on selectionne la liste des entrainement LOO
        cumul = 0
        rescount = 0
        table = template % molindex
        # On recherche les 'loomaxrec' premiers apprentissage par ordre de VLOO score croissant
        # rappel extraselect = "((DeltaRank = 0) AND (abs(RoundOffTest) < options.roundthreshold) )" 
        # et si selectOnlev est vrai, on ajoute la contrainte "(leverages < options.looleveragethreshold)"
        frameloc = getDataFrame(dbConnect, table, fieldlist=fieldlist, 
            orderfield=orderfield, extraselect=extraselect, maxrec=maxrec) 
        # le shape de frameloc est (loomaxrec, loowidth)
        cumul = 0.0
        if frameloc.shape[0]:
            # il y a des enregistrements qui repondent aux criteres definis par extraselect
            
            for indloc, row in frameloc.iterrows():
                cumul += row['out']
            meanvalue = cumul / frameloc.shape[0]
            looFrame.at[molname, meanField] = meanvalue
            looFrame.at[molname, estimationerrorfield] = looFrame.at[molname, targetfield] - meanvalue
#             looFrame.at[molname, estimationerrorfield] = meanvalue - looFrame.at[molname, targetfield]
            if options.verbosexls > 1:
                looFrame.at[molname, "SCount"] = frameloc.shape[0]
                for indloc, row in frameloc.iterrows():
                    for field, val in row.items():
                        fieldname = fielddict[field].format(indloc)
                        looFrame.at[molname, fieldname] = val
        # Fin de la boucle sur les data
    return looFrame, len(fieldlist)

def manageSingleUsage(options, model, outs, levs, stds, students):
    printcond = options is not None and hasattr(options, 'debug') and options.debug & DEMO_DEBUG_USAGE       

    ics = [np.sqrt(lev)*studentvar*stddev for lev, stddev, studentvar in zip(levs, stds, students)]
    extraVLOOs = model.extraVLOO[:len(outs)] if model.extraVLOO is not None else [np.nan for _ in range(len(outs))]
    #extraVLOOs = extraVLOOs[:len(outs)]

    ar = np.asarray([outs, levs, stds, students, ics, extraVLOOs]).T
    if printcond:
        print('outs len:', len(outs))
        print('levs len:', len(levs))
        print('stds len:', len(stds))
        print('students len:', len(students))
        print('ics len:', len(ics))
        print('extraVLOOs len:', len(extraVLOOs))
    names = ['output', 'leverage', 'stddev', 'student', 'IC', 'VLOO']
    usageFrame = DataFrame(ar, columns=names)
    if printcond:
        print('usageFrame.shape:', usageFrame.shape)
    thres = options.leveragethreshold
    validCount = 0
    todrop = []
    minlev = float('inf')
    indexminlev = -1
    
    # recherche des lev invalides
    for index, val in usageFrame['leverage'].items():
        try:
            val = val.squeeze()
        except: pass
        if val < minlev:
            minlev = val
            indexminlev = index
        if (thres > 0) and (val > thres):
            todrop.append(index)
        else:
            validCount += 1
    if indexminlev in todrop:
        todrop.pop(todrop.index(indexminlev))
    if not validCount:
        print("minimum leverage ( {0} ) overpass the limit ( {1} )".format(minlev, thres))
        print("only one value wil be kept with leverage {0}".format(minlev))
    elif validCount < len(outs):
        print("only {0}/{1} models will be kept".format(validCount, len(outs))) 
        usageFrame.drop(todrop, inplace=True)
    return usageFrame

def finishMultiUsage(resultFrame, pptyname, basefieldlist, modelNames, 
                     outslist, levslist, icslist, levthres, verbose):
    def getindex(col):
        n1 = col.rfind('(')
        if n1 < 0:
            return -1
        else:
            tst = col[n1+1:-1]
            try:
                index = int(tst)
            except:
                index = 0
        return index
    
    minslist = []
    maxslist = []
    meanlist = []
    countlist = []
    for outs, ics, levs in zip(outslist, icslist, levslist):
        minlst = []
        maxlst = []
        cumul = 0
        count = 0
        for out, ic, lev in zip(outs, ics, levs):
            ic = ic.squeeze()
            out = out.squeeze()
            lev = lev.squeeze()
            if (levthres <= 0) or (lev < levthres):
                minlst.append(out - ic)
                maxlst.append(out + ic)
                cumul += out
                count += 1
        countlist.append(count)
        minslist.append(minlst)
        maxslist.append(maxlst)
        if count:
            meanlist.append(cumul / count)
        else:
            meanlist.append(float('nan'))
    
    IDs = list(resultFrame.index)
    for col in resultFrame.columns:
        curindex = getindex(col)
        if col.startswith('mean'):
            for ID, mean in zip(IDs, meanlist):
                resultFrame.at[ID, col] = mean 
        elif col.startswith('SCount'):
            for ID, cnt in zip(IDs, countlist):
                resultFrame.at[ID, col] = cnt 
        elif col.startswith("estimated"):
            for ID, outs in zip(IDs, outslist):
                try:
                    out = outs[curindex]
                    resultFrame.at[ID, col] = out
                except: pass  
        elif col.startswith("min"):
            for ID, mins in zip(IDs, minslist):
                try:
                    Min = mins[curindex]
                    resultFrame.at[ID, col] = Min 
                except: pass 
        elif col.startswith("max"):
            for ID, maxs in zip(IDs, maxslist):
                try:
                    Max = maxs[curindex]
                    resultFrame.at[ID, col] = Max  
                except: pass 
        elif col.startswith("leverage"):
            for ID, levs in zip(IDs, levslist):
                try:
                    lev = levs[curindex]
                    resultFrame.at[ID, col] = lev 
                except: pass 
    return resultFrame 

def finishSingleUsage(usageFrame, modelname, smile, inputs, target, 
    inputnames, outputname, leveragethreshold, dsize, verbose=3, verbosexls=0, 
    options=None):
    # usageFrame columns: output', 'leverage', 'stddev', 'student', 'IC', 'VLOO'
    def formattedvalue(value, verb, dsize=0):
        if dsize > 0:
            fmt = "{{0:.{0}f}}".format(dsize)
            return fmt.format(value)
        if not verb:
            return "{0:.2f}".format(value)
        if verb == 1:
            return "{0:.3f}".format(value)
        if verb > 1:
            return "{0:.6f}".format(value)
    outputname = outputname if outputname else "output"
    if target is not None:
        st = "target: {0}".format(formattedvalue(target, verbosexls, dsize))
        st = "{0} {1}".format(outputname, st)
        if modelname:
            st = "{0} {1}".format(modelname, st)
        print(st)
    if verbose >= 3:
        if smile:
            print("smiles {0}".format(smile))
        if inputs is not None and len(inputs) > 1:
            if len(inputnames):
                if verbosexls > 1:
                    print("\t\t".join(inputnames))
                else:
                    print("\t".join(inputnames))
            lst = [formattedvalue(val, verbosexls, dsize) for val in inputs]
            stt = "\t".join(lst)
            if len(inputnames):
                print(stt)
            else:
                print("inputs: {}".format(stt))
    cumul = 0
    valmin = float('inf')
    valmax = -float('inf')
    for ind, row in usageFrame.iterrows(): 
        out = row['output'].squeeze()
        ic = row['IC'].squeeze()
        cumul += out
        valmin = min(valmin, out - ic)
        valmax = max(valmax, out + ic)
    mean = cumul / (ind + 1)
        
    if verbose <= 2:
        st = "estimated {0} {1}".format(outputname, formattedvalue(mean, verbosexls, dsize))
        if modelname:
            st = "{0} {1}".format(modelname, st)
#         else:
#             st = "{0} {1}".format(outputname, st)
        print(st)
    elif verbose >= 3:
        st = "estimated {0}: {1} (min: {2}, max: {3})".format(outputname, formattedvalue(mean, verbosexls, dsize), formattedvalue(valmin, verbosexls, dsize), formattedvalue(valmax, verbosexls, dsize))
        if modelname:
            st = "{0} {1}".format(modelname, st)
#            st = "{0} {1} {2}".format(modelname, outputname, st)
#        else:
#            st = "{0} {1}".format(outputname, st)
        print(st)
    if verbose >= 4:
        if modelname:
            print(modelname)
        st = "leverage threshold {0}".format(leveragethreshold)
        print(st)
        print("model details:")
        if verbose == 3:
            if verbosexls > 1:
                print("{0}\t\t{1}\t\t{2}".format(outputname, "min", "max"))
            else:
                print("{0}\t{1}\t{2}".format(outputname, "min", "max"))
        else:
            if verbosexls > 1:
                print("{0}\t\t{1}\t\t{2}\t\t{3}".format(outputname, "min", "max", "leverage"))
            else:
                print("{0}\t{1}\t{2}\t{3}".format(outputname, "min", "max", "leverage"))
        for ind, row in usageFrame.iterrows():
            out = row['output'].squeeze()
            ic = row['IC'].squeeze()
            outmin = out - ic
            outmax = out + ic
            if verbose == 3:
                st = "{0:.6f}\t{1:.6f} {2:.6f}".format(formattedvalue(out, verbosexls, dsize), formattedvalue(outmin, verbosexls, dsize), formattedvalue(outmax, verbosexls, dsize))
            else:
                lev = row['leverage'].squeeze()
                st = "{0}\t{1}\t{2}\t{3}".format(formattedvalue(out, verbosexls, dsize), formattedvalue(outmin, verbosexls, dsize), formattedvalue(outmax, verbosexls, dsize), formattedvalue(lev, verbosexls, dsize))
            if (target is not None) and ((outmin > target) or (outmax < target)):
                print(st, file=sys.stderr)
            else:
                print(st)

def getSimpleExtraFields(maxrec, pptyname, fieldlist, cols=[]):
    for ind in range(maxrec):
        for field in fieldlist:
            fieldstr = "{0}({1})".format(_linkstr(field, pptyname), ind)
            cols.append(fieldstr)
    return cols

def singleCoreUsageAction(options, xml, source, ni, nh, no, idName, grouplist, datalist):
    if xml:
        #model = Driver(source=xml)
        modelparam = {'source': xml}
    else:
        modeldata = ModelData(input=ni, output=no, hidden=nh, name=id)
        modelparam = {'modeldata': modeldata}
        #model = Driver(modeldata=modeldata)
    
    model = Driver(**modelparam)
    try:
        model.loadFromDict(source)
        if not idName:
            idName = model.mainModel.name
            if idName.startswith("nn_"):
                idName = ""
        try:
            inputs = np.asarray([float(val) for val in datalist[grouplist.index('inputs')]])
        except ValueError:
            inputs = None
        if 'targets' in grouplist:
            target = float(datalist[grouplist.index('targets')][0])
        else:
            target = None
        
        outs, levs, stds, students = model.transferEx(inputs, withCI=True)  
        usageFrame = manageSingleUsage(options, model, outs, levs, stds, 
            students)
    finally:
        model.__del__()

    return usageFrame, target, idName, outs, levs, stds, students

def multiCoreUsageAction(xml, source, dataFrame, options, ni, nh, no, idd):
    modelNames = []
    outslist = []
    levslist = []
    icslist = []
    stdslist = []
    studentslist = []
    count = 0
    if xml:
        model = Driver(xml)
    else:
        modeldata = ModelData(input=ni, output=no, hidden=nh, name=idd)
        model = Driver(modeldata=modeldata)
    try:
        model.loadFromDict(source)
    #     modelName = model.mainModel.name            
        with Progress_tqdm(dataFrame.shape[0], desc="\tcomputing model", nobar=options.verbose<nobarverb) as update:
            for _, row in dataFrame.iterrows():
                count += 1
                update(count)
                if ni:
                    inputs = row[:ni]
                res = model.transferEx(inputs, withCI=True)  #original=True
                outs, levs, stds, students = res
                ics = [np.sqrt(lev)*studentvar*stddev for lev, stddev, studentvar in zip(levs, stds, students)]
                outslist.append(outs)
                levslist.append(levs)
                stdslist.append(stds)
                studentslist.append(students)
                icslist.append(ics)
            update.flush()
    finally:
        model.__del__()
    return outslist, levslist, stdslist, studentslist, icslist, []

def testAction(options, testframe, datacount, IDlist, 
        cfgfile, gmxfile, dico, doprint=doNothing):
    options.curaction = 'test'
    options.lastaction = options.curaction
    options.lastactions.append(options.curaction)
    if not options.test:
        options.test = options.source
    sourceroot = options.root 
    if not options.savedir:
        options.savedir = os.path.join(options.workfolder, sourceroot)
#        options.savedir = os.path.join(options.folder, sourceroot)
        options.savedir = IndexFilename(options.savedir, "_{0}", True)
    if hasattr(options, 'libuse'):
        libuse = options.libuse
    else:
        libuse = True
    if libuse:
        options.debug &= (~DEMO_USAGE_NO_LIB)
    else:
        options.debug |= DEMO_USAGE_NO_LIB
    if options.notrain and len(options.multimaxrec):
        for val in options.multimaxrec[1:]:
            newfile, mess = getReducedSelectedGmx(dico, val, gmxfile)
            if mess:
                doprint(mess)
#     val = testframe.columns
    res = apiTestResults(cfgfile, datacount=datacount, 
        modeltestframe=testframe, IDlist=IDlist, options= options)                                      
    testFrame, _, _, resultColumn, gmxfile = res  #, testinputColumns
    options.curaction = ""
    return testFrame, resultColumn-1 #,testinputColumns

def looTestAction(options, testframe, resfile, IDlist, gmxfileextra="", 
        doprint=doNothing):  #tempres, ex celwriter, sheetname, apiTrainRes, 

    options.curaction = 'lootest'
    options.lastaction = options.curaction
    options.lastactions.append(options.curaction)
    traintype = 'loo'
    if not options.test:
        options.test = options.source
    sourceroot = options.root  #os.path.splitext(os.path.basename(options.source))[0]
    if not options.savedir:
        options.savedir = os.path.join(options.workfolder, sourceroot)
        options.savedir = IndexFilename(options.savedir, "_%d", True)
    if not resfile:
        resfile = os.path.join(options.savedir, "train.cfg")

    if options.libuse:
        options.debug &= (~DEMO_USAGE_NO_LIB)
    else:
        options.debug |= DEMO_USAGE_NO_LIB
    
    datacount = testframe.shape[0]
    orderfield = getOrderField(options)
    res = apiTestResults(resfile, datacount, testframe, IDlist, 
        options, leveragethreshold = options.leveragethreshold,
        extraselect="", orderfield=orderfield,  traintype='loo', 
        gmxfile = gmxfileextra, todoprint=True);  
    looTestFrame, patternlist, _, _, _ = res
    options.curaction = ""                                        
    return looTestFrame

def bsTestAction(options, testframe, resfile, IDlist, gmxfileextra="",  doprint=doNothing):
#     doprint("bsTestAction not yet implemented")
    options.curaction = 'bootstraptest'
    options.lastaction = options.curaction
    options.lastactions.append(options.curaction)
    mode = options.mode
    bsTestFrame = None
    traintype = 'bootstrap'
    if not options.test:
        options.test = options.source
    sourceroot = options.root  #os.path.splitext(os.path.basename(options.source))[0]
    if not options.savedir:
        options.savedir = os.path.join(options.workfolder, sourceroot)
#        options.savedir = os.path.join(options.folder, sourceroot)
        options.savedir = IndexFilename(options.savedir, "_%d", True)
    if not resfile:
        resfile = os.path.join(options.savedir, "train.cfg")

    if options.libuse:
        options.debug &= (~DEMO_USAGE_NO_LIB)
    else:
        options.debug |= DEMO_USAGE_NO_LIB
    
    datacount = testframe.shape[0]
    orderfield = getOrderField(options)
    res = apiTestResults(resfile, datacount, testframe, IDlist, 
        options, leveragethreshold=options.leveragethreshold,
        extraselect="", orderfield=orderfield,  traintype='bootstrap', 
        gmxfile=gmxfileextra,
        todoprint=True); 
    bsTestFrame, patternlist, _, _, _ = res
    options.curaction = "" 
    return bsTestFrame

@hookable.direct
def deepDataAnalysis(mode, dataFrame, config=None, options=None,
    acceptdefault=False, classif=False, doprint=doNothing):
    return ""

def analyseDataFiles(options=None, commonFieldExclude=True, 
        forceAnalyse=False, doprint=doNothing):  #dee pDataAnalysis=None,
    """Analyse the content of data files.
    
    Parameters:
     - options -> proposed parameter namespace.
         Following attributes must exists:
          - options.source -> data file.
     - commonFieldExclude -> Exclusion of common fields in data groups. 
     - forceAnalyse -> force the full analyse of data file.analyseGraphmachineData
     - doprint -> print function.
     
    Return a tuple containing:
     - sourcefile -> data training file
     - datafiletype -> type of data file
     - datarange -> range of train data
     - datafields -> list of used fields in data file/ range for train
     - datafieldlist ->  list of fields index in each data group for train
     - testfile ->  data testing file
     - testfiletype ->  type of test file 
     - testrange ->  range of train test
     - testfields ->  list of used fields in data file/ range for test
     - testfieldlist -> list of fields index in each data group for test
     - configstr -> configuration string for graphmachine model construction.
     - grouplist ->  list of data groups. A group may be one of ['indentifiers', 'smiles', 'inputs', 'outputs']
     - classif ->  classification model.
     - config -> configuration object of the project
    """
    
    if options is None:
        options, _, _ = api_options([])
        options.yes = False
    accept = True
    if 'analyse' in options.actionlist:
        if not forceAnalyse:
            mess = "Will you check the data file(s) ?"
            valdef = dialogdefaults['data']['check_data']
            accept = yesNoQuestion(mess, valdef, doprint=doprint)
        if accept:
            if not hasattr(options, 'grouplist') or options.grouplist == []:
                options.grouplist = list(groupavailables[options.mode].keys())
                # groupdefault
            forceyes = not accept or options.yesyes
            options.grouplist = _checkGroupList(options.mode, groups=options.grouplist, 
                forcedefault=forceyes, doprint=doprint, verbose=options.verbose)
    if len(options.groupcount) != len(options.grouplist):
        options.groupcount = [1 for _ in options.grouplist]
    sourcefile = options.source
    filetype = options.filetype
    datarange = options.datarange
    datafieldlist = options.datafields
#     if isinstance(datafieldlist, str):
#         datafieldlist = datafieldlist.split(',')
    if datafieldlist is None or not len(datafieldlist):
        datafieldlist = []
        options.datafields = []
    if hasattr(options, 'test'):
        testfile = options.test
        testrange = options.testrange
        testfieldlist = options.testfields
    else:
        testfile = ""
        options.test = ""
        testrange = ""
        options.testrange = ""
        testfieldlist = []
        options.testfields = []
    forcedefault = options.yes or not accept
    grouplist = options.grouplist
    groupCount = options.groupcount 
    verbose = options.verbose 
    commonFieldExclude = True,
     
    assert sourcefile or testfile, "Need a data file"
    
    commonfiles = ""
    testfile == ""
    testfiletype = ""
    testfields = []
    ranges = []
    dotrain = 'train' in options.actionlist 
    if 'analyse' in options.actionlist or (dotrain and (datafieldlist == [] or datafieldlist is None)):  #not filetype or 
        filetype, datarange, datafields, ranges, dialect = _checkFile(
            sourcefile, 
            datarange=datarange,
            datafor='train', 
            indexdefault=0, 
            forcedefault=forcedefault, 
            doprint=doprint, 
            verbose=verbose)

        assert datafields is not None, "File {0} has been refused. \nCannot proceeed".format(sourcefile)
        assert len(datafields), "Need data in file {0}".format(sourcefile)
        fieldprompt = "Please choose {0} values by their indexes comma separated for the {1} group in the followings:"
        fieldprompt1 = "Please choose the index of the {0} field"
        if 'analyse' in options.actionlist:
            try:
                defaultlist = datafieldlist.copy()
            except:
                defaultlist = datafieldlist
        if not 'analyse' in options.actionlist or not len(defaultlist):
            defaultlist = []
            value = 0
            if len(datafields) == len(groupCount) -1:
                groupCount.pop(-2)
                grouplist.pop(-2)
            else:
                groupCount = groupCount[:len(datafields)]
                grouplist = grouplist[:len(datafields)]
            for countval in groupCount:
                lloc = []
                for _ in range(countval):
                    lloc.append(value)
                    value += 1
                defaultlist.append(lloc)
        printMessage = "Chosen fields"
        dicodef = dialogdefaults["data"]
        datafieldlist = chooseFields(fieldprompt, fieldprompt1, datafields, 
            grouplist=grouplist, groupCount=groupCount, defaultlist=defaultlist,
            dicodefault=dicodef,
            mutualExclude=commonFieldExclude, printMessage=printMessage,
            doprint=doprint, forcedefault=forcedefault, acceptnull=True, 
            verbose=verbose, debug=1)   
        idlst = [] if not 'identifiers' in grouplist else datafieldlist[0]
        for ind, val in enumerate(datafieldlist):
            groupCount[ind] = len(val)
        if (len(idlst) == 1) and (idlst[0] < 0):
            grouplist.pop(0)
            groupCount.pop(0)
            datafieldlist.pop(0)
        options.groupcount = groupCount
        datafiletype = filetype
        while [] in datafieldlist:
            indexnull = rindex(datafieldlist, [])
            grouplist.pop(indexnull)
            datafieldlist.pop(indexnull)
    elif sourcefile:
        if not os.path.exists(sourcefile):
            mess = "Sorry, cannot find data source {0}".format(sourcefile)
            raise nn1Error(mess)
        datafiletype = filetype
        datafields = gettitles(sourcefile, filetype, datarange=datarange, datafmt=options.datafields)
    else:
        datafiletype = filetype
        datafields = []
    if len(datafieldlist):
        try:
            options.groupcount = [len(val) for val in datafieldlist]
        except TypeError:
            datafieldlist = [[1] for _ in datafieldlist]
            options.groupcount = [1 for _ in datafieldlist]

#=======================================================================#    
#    input type checking 
    testframe = None 
    dataframe = None       
    if sourcefile:
        dataframe, datafieldlist, grouplist, mode, badfields, titlelist = \
        CheckInputTypes(sourcefile, datarange, datafieldlist, grouplist, 
            datafiletype, options.mode, forcedefault=options.yesyes,
            doprint=doprint, debug=options.debug)
    else:
        testframe, testfieldlist, grouplist, mode, badfields, titlelist = \
        CheckInputTypes(testfile, testrange, testfieldlist, grouplist, 
            datafiletype, options.mode, forcedefault=options.yesyes,
            doprint=doprint, debug=options.debug)
# here, a 'smiles' item may be included in grouplist, and 
# 'inputs' item may have desappeared
#=======================================================================# 
    if len(badfields):
        return badfields
    options.mode = mode
    if verbose >= 3:
        doprint("\tmode {0}".format(mode))
    if dotrain or not 'analyse' in options.actionlist:
        classif = options.classif
    else:
        if (mode == 'gm'):  # 
            mess = "Is this Graphmachine model a full hydrogen model ?"
            valdef = int(dialogdefaults['model']['fullH'])
            options.fullH = yesNoQuestion(mess, valdef, forcedefault=options.yesyes, doprint=doprint)
        mess = "Is this model a classification model ?"
        valdef = int(dialogdefaults['model']['classif'])
        forcedef = options.yesyes or dialogdefaults['model']['hidden']['classif']
        classif = yesNoQuestion(mess, valdef, forcedefault=forcedef, doprint=doprint)
        
    config = defaultCfg(mode) 

    acceptdefault = not forceAnalyse or options.yesyes
    if not hasattr(options, "configstr"):
        options.configstr = ""
    if not (options.configstr and options.notrain) and not ('usage' in options.actionlist):
        options.configstr = deepDataAnalysis(mode, dataframe, config=config, 
            options=options, acceptdefault=acceptdefault, classif=classif,
            doprint=doprint)
        
    if options.configstr:
        doprint("\tconfigstr: {0}".format(options.configstr))
#     elif options.mode == 'gm':
#         doprint("\tconfigstr empty")  Suppress 26/06/2019 pour demo

    return sourcefile, datafiletype, datarange, datafields, \
        datafieldlist, testfile, testfiletype, testrange, testfields, \
        testfieldlist, options.configstr, grouplist, classif, config, \
        ranges, commonFieldExclude, titlelist  # analyseDataFiles
            
def testChecking(options, dotestanalysis, ranges, commonFieldExclude, 
        forcedefault, doprint, verbose):
    testfieldlist = options.testfields
    commonfiles = options.test == ""
    usedranges = [options.datarange]
    
    if not options.notest:  #  le 28/02/2019
        if options.filetype in simpleRangeType:
            oktest = bool(options.test)
        elif options.filetype in multiRangesType:
            oktest = len(ranges)
        else:
            oktest = False
        options.notest = not oktest
    if not options.notest:
        
        if 'analyse' in options.actionlist or testfieldlist == []:
            if commonfiles:
                testfileloc = options.source
            else:
                testfileloc = options.test
            testfiletype, testrange, testfields, ranges, dialect = _checkFile(
                testfileloc, 
                excluded=usedranges,
                datafor='test', 
                datarange=options.testrange,
                indexdefault=1, 
                forcedefault=forcedefault, 
                doprint=doprint, 
                verbose=verbose) 
 
#         dotestanalysis = 'analyse' in options.actionlist and (testfields != options.datafields)        
        commonstruct = len(options.datafields) and ((testfieldlist == []) or (testfieldlist is None) or (testfields == options.datafields))
#         if not dotestanalysis and commonstruct:
        if commonstruct:
            mess = "Data and test files seems to have the same structrure. Will you set the sames field choice ?"
            valdef = dialogdefaults['data']['same_struct']
            res = yesNoQuestion(mess, valdef, "", doprint=doprint, forcedefault=forcedefault, verbose=verbose)  
            dotestanalysis = not res
            if res:
                testfieldlist = options.datafields
        if dotestanalysis:
            fieldprompt = "Please choose {0} values by their indexes comma separated for the {1} group in the followings:"
            fieldprompt1 = "Please choose the index of the {0} field"
            defaultlist = []
            value = 0
            for countval in options.groupcount:
                lloc = []
                for _ in range(countval):
                    lloc.append(value)
                    value += 1
                defaultlist.append(lloc)
            printMessage = "Chosen fields"
            dicodef = dialogdefaults["data"]
            testfieldlist = chooseFields(fieldprompt, fieldprompt1, testfields, 
                dicodefault=dicodef,
                grouplist=options.grouplist, groupCount=options.groupcount, defaultlist=defaultlist,
                mutualExclude=commonFieldExclude, printMessage=printMessage,
                doprint=doprint, forcedefault=forcedefault, acceptnull=True,
                verbose=verbose)   
            testfiletype = options.filetype
            if not len(testfields):
                testfields = gettitles(options.test, options.testfiletype, datarange=testrange, datafmt=None)
        else:
            testfiletype = options.filetype
            testfields = gettitles(options.test, options.testfiletype, datarange=testrange, datafmt=options.testfields)
    options.testfields = testfieldlist
#     return testfieldlist

def analysisAction(options=None, doprint=doNothing, forceAnalyse=True):  
    """Data file analysis.
    
    Parameters:
     - options -> Namespace to write with the datasource informations and the user choices.
     - doprint -> print function.
     - forceAnalyse -> If True, a full datafile analysis is perdirmed.
    
    Return:
     - options -> options namespace.
     - modeldataframe -> object modelDataFrame for training data.
     - modeltestframe -> object modelDataFrame for testing data.
    """

    doprint("Running source file analysis")
#     newtrain = False
    if options is None:
        options, _, _ = api_options([])        
        options.yes = False
    oldyes = options.yes
    if 'analyse' in options.actionlist:
        if not options.yesyes:
            if hasattr(options, 'source') and options.source:
                options.yes = False
    sourceloc = os.path.basename(options.source)
    doprint("\tdatafile: {0}".format(sourceloc))
    if hasattr(options, 'test') and options.test:
        testloc = os.path.basename(options.test)
        if testloc and (testloc != sourceloc):
            doprint("\ttestfile: {0}".format(testloc))     
    if hasattr(options, 'origin') and options.origin:
        originloc = os.path.basename(options.origin)
        doprint("\toriginfile: {0}".format(originloc))    
    newtrain = 'train' in options.actionlist
    try:
        res = analyseDataFiles(options, doprint=doprint, forceAnalyse=forceAnalyse)
    except Exception as err:        
        doprint("Error in _api_service.analyseDataFiles")
        doprint(err)
        return None
    try:
        options.source = res[0] 
        options.filetype = res[1] 
        options.datarange = res[2]
        options.datatitles = res[3]
        options.datafields = res[4]
        options.test = res[5]
        options.testfiletype = res[6] 
        options.testrange = res[7]
        options.testtitles = res[8]
        options.testfields = res[9]
        options.configstr = res[10]
        options.grouplist = res[11]
        options.classif = res[12]
        config = res[13]
        ranges = res[14] 
        commonFieldExclude = res[15] 
        options.datatitles = res[16]
    except Exception as err:
        badfields = res
        doprint("Input data should be numerical !")
        doprint('Following input field(s) is(are) string: "{0}"'.format(badfields))
        return None
#     options.notest = not res[14]
#    try:
#        connect, central, classif, hidden, fullH = ReverseConfigString(options.configstr)
        #_, options.central, _, _, _ =  
#    except: pass
    if (options.verbose >= 4):
        if options.datarange:
            doprint("\tdata range: {0}".format(options.datarange))
        else:
            doprint("\tdata fields")
        if len(options.grouplist) == len(options.datatitles):
            for group, titles in zip(options.grouplist, options.datatitles):
                fieldlist = ", ".join(titles)
                doprint("\t{0} -> {1}".format(group, fieldlist))
        else: 
            start = 0
            for group, fields in zip(options.grouplist, options.datafields):
                stop = start + len(fields)
                titles = options.datatitles[start:stop]
                start = stop
                doprint("\t{0} -> {1}".format(group, ", ".join(titles)))
            pass 
        if options.test:
            doprint("\ttest source: {0}".format(options.test))
            if options.testrange:
                doprint("\ttest range: {0}".format(options.testrange))
            else:
                doprint("\ttest fields")
            
    options.savedir = options.workfolder
    savedir = os.path.join(options.workfolder, options.root)
    savedir = IndexFilename(savedir, "_{0}", last=not newtrain, docreate=True)
#     if not os.path.exists(savedir):
#         os.makedirs(savedir)
    filest = "{0}.cfg".format(options.root)
#     filest = "{0}_{1}.cfg".format(options.root, options.hidden)
    cfgfile = os.path.join(savedir, filest)
    if newtrain:
        inputnames = ""
        if len(options.datatitles) and isinstance(options.datatitles[0], list):
            if 'inputs' in options.grouplist:
                index = options.grouplist.index('inputs')
                inputnames = ",".join(options.datatitles[index])
        outputnames = ""
        if len(options.datatitles) and isinstance(options.datatitles[0], list):
            if 'outputs' in options.grouplist:
                index = options.grouplist.index('outputs')
                outputnames = ",".join(options.datatitles[index])
        config.set("model", "outputname", outputnames)
        config.set("model", "inputnames", inputnames)
        config._filename = cfgfile  
        config.save()
        
    options.savefolder = savedir
    options.cfgfile = cfgfile
    
    resprepro = preAction(options, doprint=doprint)  #, forcedefault=forcedefault)
    
    if 'analyse' in options.actionlist:
        indextest = None  
        if options.notest:
            index = options.index  
            if (index is not None and (index >= 0)):  # and not nofile:
                searchbases = [options.datafolder]
                candidates, searchdir = _getDataFileCandidates(searchbase=searchbases)
            
            addTest(options, index, 
                searchdir, candidates, ranges, commonFieldExclude, 
                doprint=doprint)
        if not options.notest and (indextest is not None) and (indextest == index):
            options.test = ""

        mess = "Will you check the training parameters ?"
        if options.yesyes:
            accept = False
        else:
            valdef = dialogdefaults['train']['check']
            accept = yesNoQuestion(mess, valdef, doprint=doprint)
        if accept:
            try:
                res = _CheckTrainingParameters(options, doprint=doprint)
            except Exception as err:
                doprint(err)
                return None
        if 'loo' in options.actionlist:
            mess = "Will you check the Leave-One-Out parameters ?"
            valdef = dialogdefaults['action']['check_LOO']
            accept = yesNoQuestion(mess, valdef, doprint=doprint)
            if accept:
                try:
                    res = _CheckLOOParameters(options, doprint=doprint)
                except Exception as err:
                    doprint(err)
                    return None
        if 'bootstrap' in options.actionlist:
            mess = "Will you check the Bootstrap parameters ?"
            valdef = int(dialogdefaults['action']['check_bootstrap'])
            accept = yesNoQuestion(mess, valdef, doprint=doprint)
            if accept:
                try:
                    res = _CheckBSParameters(options, doprint=doprint)
                except Exception as err:
                    doprint(err)
                    return None
    options.yes = oldyes
    doprint('Source file analysis done')
    return options  #, modeldataframe, modeltestframe 

def _createExcelwriter(options, Frame, sheetname="Sheet 1"):  #, with index=False):
    # recupéré sur old
    excelwriter = None
    fname = ""
    if options.copyexcel:
        tempstr = ''.join(choice(ascii_uppercase) for _ in range(8))
        fname = os.path.join(options.targetfolder, "{0}.xlsx".format(tempstr))
        excelwriter = ExcelWriter(fname, engine='xlsxwriter')
        Frame.to_excel(excelwriter, sheetname)  #, index=with index)
    elif options.copytxtcsv and os.path.exists(options.targetfolder):
        fname = os.path.join(options.targetfolder, 'resultFrame')
        fname = decorfile(fname, options, ".{0}".format(options.copytype), indextemplate="(%d)")                    
        with open(fname, 'w') as ff:
            ff.write(Frame.to_csv(sep=options.sep, decimal=options.decimal))
    return excelwriter

def preAction(options, doprint=doNothing, forcedefault=False):
    return 0

@hookable.indirect('mode')
def createTrainingDataTable(options, dbConnect):
    return 0;

def traiterCentralList(centralList, config):
    cumul = defaultdict(lambda :0)
    if config:
        for token, smiles, _ in centralList:  #name
            sym = token.symbol
            cumul[sym] += 1
        if not config.has_section("centralatom"):
            config.add_section("centralatom")
        for key, value in cumul.items():
            config.set("centralatom", key, str(value))
    return cumul        

def trainAction(options=None, sourceframe=None, hidden=3, moduledir="", 
        modulename="", initcount=12, multimodel=10, epochs=150, seed=-1, 
        initstddev=0.1, extraselect="", trainstyle=0, datarange="",
        savedir="", tablename='trainingResult', verbose=3, doprint=doNothing, 
        forceyes=False, prefix="\t", resultFrameList=[]):  
    """Training action
    """
    centrallist = []
    options.curaction = 'train'
    options.lastaction = options.curaction
    options.lastactions.append(options.curaction)
    
    if options is not None:
        hidden = options.hidden
        moduledir = options.sharedfolder
        initcount = options.initcount
        multimodel = options.maxrec
        epochs = options.epochs
        initstddev = options.initstddev
        forceyes = options.yes
        verbose = options.verbose
        root = options.root
        cfgfile = options.cfgfile
        tablename = options.tableName
        pptyname = options.propertyName
        pptyunit = options.propertyunit
        seed = options.seed
        trainstyle = options.trainstyle
        datarange = options.datarange
         
    config = defaultedConfigParser(cfgfile)
    if not config.has_section("projects"):
        config.add_section("projects")
    config.set("projects", "0", root)
    if not config.has_section(root):
        config.add_section(root)
    config.set(root, 'tablename', tablename)
    config.set(root, "propertyname", pptyname)
    config.set(root, "propertyunit", pptyunit)
    config.set(root, "datacount", str(sourceframe.shape[0]))
    config.set(root, "datarange", str(datarange))

    if hidden < 0:
        hiddendefault = - hidden
        hidden = valueQuestion("Enter the number of hidden neurons", 
            hiddendefault, "Hidden neurons", doprint=doprint, 
            verbose=verbose, forcedefault=forceyes, prefix=prefix)

    
    doprint("{0}required hidden: {1}".format(prefix, hidden))
    if verbose > 3:
        doprint("{0}random std-dev: {1:g}".format(prefix, initstddev))
    config.set("model", "hidden", str(hidden))
    config.set("training", "initcount", str(initcount))
    config.set("training", "epochs", str(epochs))
    config.set("training", "seed", str(seed))
#     def callbackcentral(value):
#         global centrallist
#         centrallist = value.copy()
# #        return value
#         traiterCentralList(centrallist, config)
    config.save()
    
    # chargement ou creation du module d'apprentissage
    
    baselen = sourceframe.shape[0]
    updatetuple = (baselen, '\tsourcing', '\tcompiling', verbose<3, sys.stdout)
    doprinttime = False
    debug = 0
    try:
        lib, servicelist = getTrainingModule(options, dataframe=sourceframe, 
            config=config, outputdir=savedir, compiler="", 
            keeptemp=options.keeptemp, verbose=verbose, doprinttime=doprinttime, 
            debug=debug, progress=updatetuple)  #
    except Exception as err:
#        print(err)
        raise
    if servicelist:
        traiterCentralList(servicelist, config)
    if lib is None:
        raise nn1Error("training module cannot be created or loaded")
    fullmodname = lib.libfilename
    config.set(root, "module", fullmodname)
    config.set(root, "module_{0}".format(options.hidden), fullmodname)

    if lib.modeldata is None:
        inputcount = -1
        outputcount = -1
    else:
        inputcount = lib.modeldata.input
        outputcount = lib.modeldata.output
    options.paramCount = lib.paramCount
    try:    
        datacount, datasize = lib.loadTrainingDataFromFrame(sourceframe, inputcount, outputcount)
        options.modulename = fullmodname
        options.datacount = datacount
        options.datasize = datasize
    except: pass
#     print("columns 3", sourceframe.columns, file=sys.stderr)

    if doprint:
        if lib.modelmode == "load":
            prefixx = "\tloading module"
        elif lib.modelmode == "compile":
            prefixx = "\tloading compiled module"
        else:
            prefixx = "module"
        if (verbose >= 4):
            st = lib.repr('long')
        elif (verbose == 3):
            st = lib.repr('short', tab = "\t\t", prefix=prefixx)
#            st = "\t{}".format(st)
        else:
            st = ""
        if st:
            doprint("{}".format(st))
#             if prefixx:
#                 doprint("{0}:\n{1}".format(prefixx, st))
#             else:
#                 doprint()
#     
    initcount = valueQuestion("Enter the number of training run", initcount, 
        "training count", forcedefault=forceyes, prefix=prefix, doprint=doprint,
        verbose=verbose)  
    options.initcount = initcount  
    epochs = valueQuestion("Enter the number epochs per run", epochs, 
        "epochs", forcedefault=forceyes, prefix=prefix, doprint=doprint,
        verbose=verbose)    
    options.epochs = epochs
    if (seed > 0):
        doprint("{0}seed: {1}".format(prefix, seed))
    
    multimodel = min(multimodel, initcount)
    if not savedir:
        try:
            savedir = options.savefolder
        except: pass
    if not savedir:
        savedir = os.path.join(moduledir, root)
        savedir = IndexFilename(savedir, "_{0}", docreate=True)
        if not os.path.exists(savedir):
            os.makedirs(savedir)
    options.savefolder = savedir
    sqlFileName = os.path.join(savedir, "{}_{}.db".format(root, options.hidden))
    config.set(root, 'sqlfilename', sqlFileName)
    if os.path.exists(sqlFileName):
        os.remove(sqlFileName)
    dbConnect = sqlconnect(sqlFileName, detect_types=sqlPARSE_DECLTYPES)
    options.sqlFileName = sqlFileName
    traindata = C.TRAIN_DATA
    try:
        createTableDb(dbConnect, tablename, traindata)
    except sqlOperationalError:
        cleanTableDb(dbConnect, tablename)
    createTrainingDataTable(options, dbConnect)
    
    if servicelist:
        for token, smiles, modelname in servicelist:
            data = {'ID': modelname, 'smiles': smiles, 'central': token.symbol, 'smilesindex': token.smilesindex}
            insertDataToDb(dbConnect, table="trainingData", data=data)
    
    propertyname = pptyname if pptyname else options.datatitles[options.grouplist.index('outputs')][0]
    
    config = setTrainingActionParams(config, propertyname, initcount=initcount, 
        initstddev=initstddev, epochs=epochs, resultdir=moduledir, seed=seed, 
        criterion=C.TCR_PRESS)
    config.save(cfgfile)
    
#     gmxfilename = getGmxFileName(options, dosave=True, ext=".gmx", forbiden=[])
    with Progress_tqdm(initcount, desc='\ttraining', nobar=verbose<nobarverb) as update:
        onEndIterloc = ft.partial(onEndIter, progress=update, dowrite=None)
        onReturnResultloc = ft.partial(onReturnResult, dbConnect, tablename)
        nfail = lib.multitrain(
                initcount=initcount,
                epochs=epochs,
                weightsstddev=initstddev, 
                seed=seed,
                onEndIter=onEndIterloc,
                onReturnResult=onReturnResultloc,
                trainstyle=trainstyle)
        if update:
            update.flush()
    bestweight = _getBestWeights(dbConnect, options)
#     print("columns 4", sourceframe.columns, file=sys.stderr)
    
    lib.weights = bestweight
    resultFrame = getResultFrame(dbConnect, options=options)
    if not resultFrame.shape[0]:
        st = "All the trained models are degenerated. The full rank condition is now relaxed."
        doprint(st)
        options.extraselect = options.extraselectrelaxed
        resultFrame = getResultFrame(dbConnect, options=options)
        if not resultFrame.shape[0]:
            st = "All the round-off test failed. Full training process failed."
            doprint(st)
    if "ID" in resultFrame.columns:
        resultFrame.set_index("ID", inplace=True)
    countmax = min(multimodel, resultFrame.shape[0])
    if countmax < multimodel:
        st = "Number of selected models has been reduced from {0} downto {1}.".format(multimodel, countmax)
        doprint(st)
    if not countmax:
            return fullmodname, None, cfgfile, None, None, sqlFileName

    
    resultFrameList.append((options.hidden, resultFrame.copy(), lib.paramCount)) 
    
    # sauvegarde dans un fichier d'utilisation gmx ou nnx
    gm0 = getModelDict(config, lib, version=metaphorversion)  #, model data)
    indexlist = resultFrame.index[:countmax] 
    gmxfile, dico = getGmxFileAndSave(dbConnect, gm0, config, indexlist, options, "nn1", full=True)  #  gmx
    options.modelfile = gmxfile
    
#     if len(options.multimaxrec) > 1:
#         available = dico['extracount']
#         count = 0
#         for val in options.multimaxrec[1:]:
#             if val < available:
#                 count += 1
#                 newfile, mess = getReducedSelectedGmx(dico, val, gmxfile)
#                 if mess:
#                     doprint(mess)
#         if not count:
#             newfile, mess = getReducedSelectedGmx(dico, available-1, gmxfile)
#             if not mess:
#                 mess = "saved available {} results".format(available)
#                 if mess:
#                     doprint(mess)

    confResult = config
    confResult.set(root, "mcount", "%d" % countmax)
    confResult.set(root, "gmxfile", gmxfile)
    confResult.set(root, "sqlfilename", sqlFileName)
    confResult.set(root, "sqlfilename_{}".format(options.hidden), sqlFileName)
    confResult.set(root, "tablename", tablename)
    st = ";".join(list(lib.parameterNames))
    confResult.set(root, "paramnames", st)
    confResult.set(root, "paramnames_{0}".format(options.hidden), st)
    if lib.inputCount:
        confResult.set(root, 'inputnorm', ";".join([str(val) for val in lib.inputnorm]))
    confResult.set(root, 'outputnorm', ";".join([str(val) for val in lib.outputnorm]))
    st = "{0}".format(lib.paramCount)
    confResult.set(root, 'paramcount', st)
    confResult.set(root, "paramcount_{0}".format(options.hidden), st)
    confResult.set(root, 'baselen', "{0}".format(lib.modelCount))
                   
    confResult.save()
    dbConnect.close()
    if verbose and doprint:
        if nfail:
            doprint("\t%s fails\n"% nfail)
        elif verbose >= 2:
            formatters = {'RoundoffTest': roundoff_format(), 
                          'ID': IDformat(),
                          #'RMSE': floatFormat(),
                          #'VLOO score': floatFormat(),
                          }
            formst = "\n\t{0} first training results ordered by increasing VLOO score:"
            doprint(formst.format(countmax))
            columns = [resultFrame.index.name] + list(resultFrame.columns)
            st = resultFrame.to_string(float_format=float_format(), 
                index_names=True, formatters=formatters, col_space=6)
            lst = st.split("\n")
            lst1 = lst[1].strip()
            ll1 = len(lst1)
            tst = lst[0][:ll1]
            OK = True
            for c in tst:
                OK = OK and (c==" ")
            if OK:
                st = lst1 + lst[0][ll1:]
                lst[0] = st
                lst.pop(1)
                st = "\n\t".join(lst)
                st = "\t{}".format(st)
            doprint(st)
    if lib:
        lib.__del__()
        lib = None
    options.curaction = "" 
    return fullmodname, resultFrame, cfgfile, gmxfile, dico, sqlFileName

def looTrainAction(options, model, sourceFrame, resultFrame, doprint=doNothing, mynames=None):
    options.curaction = 'loo'
    options.lastaction = options.curaction
    options.lastactions.append(options.curaction)
    seed = options.seed
    looTrainFrame = None
    lootrainfailed = False
    traintype = 'loo'
    sqlFileName = options.sqlFileName
    resfile = options.cfgfile
    config = defaultedConfigParser(options.cfgfile)
    try:
        res = _apiDemoLOO(config, options, sourceFrame, resultFrame, model, 
            seed, mynames=mynames)  #, resfile)
        model, looTrainFrame, gmxfileLOO, sqlLOOFileName, IDlist, \
            LOOResultTrainColumn = res
#        print("LOOResultTrainColumn", LOOResultTrainColumn)
    except:
        lootrainfailed = True   
        raise
    options.curaction = '"'
    return looTrainFrame, lootrainfailed, LOOResultTrainColumn +1, gmxfileLOO, sqlLOOFileName          

def bsTrainAction(options, model, sourceFrame, resultFrame, doprint=doNothing, mynames=None):
    options.curaction = 'bootstrap'
    options.lastaction = options.curaction
    options.lastactions.append(options.curaction)
    seed = options.seed
    bsTrainFrame = None
    bstrainfailed = False
    traintype = 'bootstrap'
    sqlFileName = options.sqlFileName
    resfile = options.cfgfile
    config = defaultedConfigParser(options.cfgfile)
    try:
        res = _apiDemoBS(config, options, sourceFrame, resultFrame, model, seed, 
                mynames=mynames)  #, resfile)
        model, bsTrainFrame, gmxfileBS, sqlBSFileName, IDlist, \
            BSResultTrainColumn = res
    except:
        bstrainfailed = True   
        raise
    options.curaction = ""
    return bsTrainFrame, bstrainfailed, BSResultTrainColumn +1, gmxfileBS, sqlBSFileName          

@hookable.indirect('mode')
def singleUsageAction(options, prepare=None):
    if prepare is not None: 
        _, data, source, mode, inputnames, outputnames, nh, datalist,\
            grouplist, extracount, xml, dsize = prepare
    else:
        pass
        
    options.curaction = 'usage'
    options.lastaction = options.curaction
    options.lastactions.append(options.curaction)
    for curdatalist in datalist:
        locdatalist = []
        if len(curdatalist) == 1 and isinstance(curdatalist[0], list):
            locdatalist = curdatalist[0]
        if 'identifiers' in grouplist and len(curdatalist):
            idName = curdatalist[grouplist.index('identifiers')][0]
        else:
            idName = None
        ni = len(inputnames)
        no = len(outputnames)
        inputs = locdatalist
#         id = ""
#         if 'identifiers' in grouplist:
#             id = curdatalist[grouplist.index('identifiers')][0]
        if options.debug & DEMO_DEBUG_USAGE:
            print("datalist", curdatalist)
            print("grouplist", grouplist)
        usageFrame, target, idName, outs, levs, stds, students = \
            singleCoreUsageAction(options, xml, source, ni, nh, no, idName, 
                grouplist, curdatalist)
    
        finishSingleUsage(usageFrame, idName, "", inputs, target, 
            inputnames, outputnames[0], options.leveragethreshold, 
            dsize, options.verbose, options.verbosexls)

@hookable.indirect('mode')
def multiUsageAction(options, prepare=None): 
    _, data, source, mode, inputnames, outputnames, nh, datalist,\
        grouplist, extracount, xml, dsize = prepare
    options.curaction = 'usage'
    options.lastaction = options.curaction
    options.lastactions.append(options.curaction)
#     if 'identifiers' in grouplist and len(datalist):
#         idName = datalist[grouplist.index('identifiers')][0]
#     else:
#         idName = None
    target = None
    ni = len(inputnames)
    no = len(outputnames)
    model = None
    inputs = None
    smile = ""
    datafile = options.test
    testrange = options.testrange
    fieldlist = options.testfields
    drop = ('identifiers' in grouplist) and not grouplist.index('identifiers') and (len(fieldlist[0]) == 1)
    dataFrame, titlelist = get_modelDataframe(datafile, testrange, fieldlist, grouplist, drop=drop) 
    cols = ['mean_{0}'.format(outputnames[0]), 'SCount']
    fieldlist = ["estimated", 'min', 'max', "leverage"]
    cols = getSimpleExtraFields(extracount, outputnames[0], fieldlist, cols)
    fullCol = list(dataFrame.columns) + cols
    newcol = OrderedDict({val: float('nan') for val in cols})  
    resultFrame = dataFrame.assign(**newcol)  
    resultFrame = resultFrame[fullCol] 
    idd = "NNUsage"
    
    outslist, levslist, stdslist, studentslist, icslist, modelNames = \
        multiCoreUsageAction(xml, source, dataFrame, options, ni, nh, no, idd)
    
    resultFrame = finishMultiUsage(resultFrame, outputnames[0], fieldlist, 
        modelNames, outslist, levslist, icslist, options.leveragethreshold, 
        options.verbosexls)
    excelwriter = _createExcelwriter(options, resultFrame, "Usage")
    usageSheet = getSheet(excelwriter, "Usage")
    excelresult = CloseExcelwriter(options, excelwriter, Sheet=usageSheet)
    dispExcelresult = make_extern(excelresult, options)
    #callerView(excelresult, options.caller, options.externpath)
    mess = "Writing results in file {0}".format(dispExcelresult)
    print(mess)

def usageAction(options=None, modelfile=None, data=""):
    """Usage of a model resulting from training action.
    
     - modelfile -> filename in format NML, NNX or GMX, holding the training results.
     - options -> namespace holding datas. Following fields may be used:
         - options.source -> data file
         - options.datarange -> range of data for excel type files
         - options.grouplist -> list of data types from ('identifiers', 'smiles', 'inputs', 'outputs')
         - options.groupcount -> list of datacount in each type
         - options.datafields -> list of data indexes per data types.
     - data -> single line data in format "identifier;[smiles;][inputs[,followings inputs comma separated];][target output]".
         - identifier may be a name or "_" if no known name
         - smiles is a string data in SMILES format, representing a chemical molecule. Optional
         - inputs is a comma separated list of float values. Optional. At least one of smiles and inputs field must be present.
         - output is a float value representing the target value. Optional
    """
    prepare = prepareUsageAction(options, modelfile, data)
    options.mode = prepare[3]
    datamode = prepare[0]
    if datamode == "single":
        singleUsageAction(options, prepare=prepare)
        
    elif datamode == 'multi':
        st = os.path.splitext(os.path.basename(options.source))[0]
        options.root  = st
        multiUsageAction(options, prepare=prepare)

#link ToServices(toPrint(sys.stderr))

if __name__ == '__main__':
#     import json
    filename = '/Users/jeanluc/docker/dialogdefaults_test.ini'
    data = dialogdefaults
    with open(filename, "w") as write_file:
        json.dump(data, write_file, indent=4)
#     with open(filename) as ff:
#         data = json.load(ff)
#         
#     print(data)



#     with open(filename, 'r') as ff:
#         res = ff.read()
#     print (res)
    
#     import pprint 
#     from io import StringIO
#     output = StringIO()
#     pp = pprint.PrettyPrinter(indent=2, stream = output)
# #     for key, val in dicoversion.items():
# #         print(key, val)
#     dd = dialogdefaults
#     pp.pprint(dd)
#     #js = json.dumps(dd)
#     
#     print(output.getvalue())
    print("done")

        
        
        