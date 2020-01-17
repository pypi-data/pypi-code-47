#! python3
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

'''Metaphor program NN and GM
'''

import os
import sys
sys.path.append('..')

import time
import importlib
from six.moves.configparser import NoOptionError
from collections import OrderedDict  
from random import randint

from ....nntoolbox.modelutils import getModelDict
from ....nntoolbox.modelutils import getGmxFileAndSave
from ....nntoolbox.filetoolbox import adaptConfigStr2hidden, IndexFilename, \
    getDictFromGmx, setEnvironFromFile
from ....nntoolbox.excelutils import  finishExcel, getCustomDict
from ....nntoolbox.utils import Namespace, finished, hasOneOf, \
    strintlist, doNothing, float_format, IDformat, roundoff_format, \
    make_extern 
from ....nntoolbox import utils as nnu
from ....nntoolbox.cmd_line_dialogs import yesNoQuestion, QuestionInterrupt
from ....nntoolbox.utils import toPrint
from ....nntoolbox.timetb import second2str
from ....nntoolbox.lineartoolbox import gramSchmidt, cosTheta  
from ....nntoolbox.datareader.modeldataframe import get_modelDataframe
from ....nntoolbox.datareader.excelsource import getFrameFromExcel  
from ....nntoolbox.configparsertoolbox import defaultedConfigParser

from ....version import __version__ as metaphorversion 
from ....monal.util.monaltoolbox import  debugOutput
#from ....monal.driver._driverlib import DriverLib
#from ....monal.util.toolbox import defaultedConfigParser
from ....monal.util.utils import getuserbase, CCharOnlys
from ....monal.modelutils import ReadModule

#from .. import _api_service as nn1serv
from ..use.nn_use import usage, usageInterne
from ..printfile import printInfo

nn1serv = None
#demodebug = nn1serv.demodebug & nn1serv.DEMO_DEBUG_DEMO
monalversion = metaphorversion
nntoolboxversion = metaphorversion

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

debugrun = 0
debug = os.environ.get('DEBUG', '')
debugrun = debug.lower() == 'run'

fullActionNames = {
    'test': 'Test',
    'loo': 'Leave-One-Out Cross Validation',
    'lootest': 'Leave-One-Out test', 
    'bootstrap': 'Bootstrap', 
    'bootstraptest': 'Bootstrap test'}

namesdict = {
    "libfilename": "",
    "resultsheetname":'Training sumary',
    "trainsheetname": 'Training results',
    "testsheetname": 'Test results',
    "tstshname": "",
    "lootestsheetname": 'LOO test results',
    "lootstshname": "",
    "bstestsheetname": 'Bootstrap test results',
    "trnshname": "",
    "lootrainsheetname": 'LOO CV results',
    "bstrainsheetname": 'Bootstrap training results',
    }
#     "sumarysheetname":'Training summary',

def mainAcvtionFromTest(testaction):
    res = ""
    if testaction.endswith('test'):
        res = testaction[:-4]
        if not res:
            return "train"
    return res

def startExtraAction(options, config, module=None, trainDataFrame=None,
        testDataFrame=None, apiTrainRes=None,
        tempres="", actiontype="test", excelwriter=None,
        currentTrainFrame=None, sheetname="", resfile="", 
        doprint=doNothing, mynames=None):
    trainortest = ''
    startwithtest = currentTrainFrame is None
    startwithlootest = not 'loo' in options.actionlist
    startwithbstest = not 'bootstrap' in options.actionlist
    if actiontype.endswith('test'):
        trainortest = 'test'
        trainortest ='train'
    m0 = "launch {0}".format(fullActionNames[actiontype])
    m1 = "launch {0} ?".format(fullActionNames[actiontype])
    m2 = "continue and launch {0} ?".format(fullActionNames[actiontype])
    message0 = m1 if options.notrain else m2
    message = m0 if options.verbose else ""
    valdef = int(nn1serv.dialogdefaults['action']['continue'])
    if not yesNoQuestion(message0, valdef, message, forcedefault=options.yes, 
                         doprint=doprint):
        doprint("aborted")
        finished(tempres)
        return
    doprint("Running {0} {1}".format(fullActionNames[actiontype], trainortest))  
    
    if  actiontype in ['loo', 'bootstrap']:       
        datacount, datasize = 0, 0
        dico = None
        gmxfile = ""
        root = options.root
        if module is None:
            module = nn1serv.LoadModuleFromCfg(config)
        elif config.has_section(root):
            gmxfile = config.get(root, "gmxfile")
            dico = getDictFromGmx(gmxfile)
            module.loadParameters(dico)
        if trainDataFrame is not None:
            datacount, datasize = \
                module.loadTrainingDataFromFrame(trainDataFrame)
        return module, datacount, datasize, dico, gmxfile, startwithbstest
    
    elif actiontype in ['lootest', 'bootstraptest']:
        ResultTrainColumn = 0
        IDList = None
        startwithtest = ((actiontype == 'lootest') and (startwithlootest)) or \
            ((actiontype == 'bootstraptest') and (startwithbstest))
        if startwithtest and (options.verbose >= 3):  # and not testindex:
            foldername = make_extern(options.savedir, options)
            doprint("working folder: %s\n"% (foldername))  #outputmarker
            currentTrainFrame = getFrameFromExcel(options.origin, sheetname, 
                reduce=True)
            if currentTrainFrame is None:
                mess = "cannot find {}|{}".format(options.origin, sheetname)
                raise Exception(mess)
            ResultTrainColumn = testDataFrame.shape[1]  #LOOResultTrainColumn
        #ResultTrainColumn = sum([len(val) for val in options.datafields]) + 1 
        else:
            sheetname = ""  

        if apiTrainRes is None:
            extratype = "loo" if actiontype == 'lootest' else "bs"
            apiTrainRes = nn1serv.apiTrainResults(options, resfile, 
                                        extratype=extratype, mynames=mynames) 
        currentTrainFrame = apiTrainRes[0]
        IDlist = apiTrainRes[3]
        root = apiTrainRes[4] 
        ResultTrainColumn = apiTrainRes[5] 
        gmxfile = apiTrainRes[6]
        
        return None, currentTrainFrame, sheetname, ResultTrainColumn, IDList, \
            startwithtest

def basicTrainTestAction(options,
                         trainDataFrame, testDataFrame,
                         doprint, resultFrameList, excelactionlist,
                         mynames):
    """Train and test basic action.
    seed and hidden variables are fixed
    """
    excelwriter = None
    resultFrame = None
    trainFrame = None
    testFrame = None
    looTrainFrame = None
    looTestFrame = None
    bsTrainFrame = None
    bsTestFrame = None
    LOOResultTrainColumn = 0
    testresultColumn = -1
    startsloowithtest = True
    startsbswithtest = True
    loowidth = 0
    traintype = ""
    starttimeloc = time.time()
    if hasattr(options, "configstrMem"):
        options.configstr = adaptConfigStr2hidden(options.configstrMem, 
                                                  options.hidden)
    trainfailed = False
    resfile = os.path.join(options.savedir, 'train.cfg')
    sqlFileName = ""
    sqlLOOFileName = ""
    sqlBSFileName = ""
    gmxfile = ""
    gmxfileLOO = ""
    gmxfileBS = ""
    module = None

    if 'train' in options.actionlist:
        doprint("Running Train")

        rest = nn1serv.trainAction(options,
                                  sourceframe=trainDataFrame,
                                  doprint=doprint,
                                  resultFrameList=resultFrameList)
        libfilename, resultFrame, cfgfile, gmxfile, dico, sqlFileName = rest
        confResult = defaultedConfigParser(resfile)
        if not confResult.has_section(options.root):
            confResult.add_section(options.root)
        confResult.set(options.root, "cfgfile", cfgfile)
        confResult.save()

        trainfailed = resultFrame is None
        if not trainfailed:
            if "ID" in resultFrame.columns:
                resultFrame.set_index("ID", inplace=True)
            fname = make_extern(gmxfile, options)
            doprint("Writing model file: {0}".format(fname))
            doprint('Train done')
#         else:
#             doprint("train failed")
    if trainfailed:
        doprint('train failed')
        return None, None  # basicTrainTestAction
    
    maxrec = options.multimaxrec[0]
    if resultFrame is not None:
        maxrec = min(maxrec, resultFrame.shape[0])  # ici 2019/11/15
    options.maxrec = maxrec
    if options.copytype and hasOneOf(options.actionlist, excelactionlist):
        res = nn1serv.apiCreateExcelAndResultFrame(options, resultFrame,
            excelwriter, resfile, doprint) 
        excelwriter, resfile, resultFrame, tempres = res
        confResult = defaultedConfigParser(resfile)
        countmax = options.maxrec
        if resultFrame is not None:
            countmax = min(countmax, resultFrame.shape[0])
        root = options.root 
        cfgfile = confResult.get(root, "cfgfile")
        config = defaultedConfigParser(cfgfile)
        paramcount = config.getint(root, "paramcount")
#    if resultFrame is not None:
    nn1serv.saveFrameToExcel(options, resultFrame, excelwriter,
        mynames.resultsheetname, actionName='result')        

    if options.notrain:
        if hasattr(options, "modelfile") and options.modelfile:
            gmxfile = options.modelfile
        else:
            gmxfile = config.get(root, 'gmxfile')
        if hasattr(options, "modelloofile") and options.modelloofile:
            gmxfileLOO = options.modelloofile
        elif config.has_option(root, 'gmxfileloo'):
            gmxfileLOO = config.get(root, 'gmxfileloo')
        if hasattr(options, "modelbsfile") and options.modelbsfile:
            gmxfileBS = options.modelbsfile
        elif config.has_option(root, 'gmxfilebs'):
            gmxfileBS = config.get(root, 'gmxfilebs')
 
        
        try:
            mcount = config.getint(root, "mcount")
        except NoOptionError:
            mcount = -1
            
        pptyname = config.get(root, "propertyname")
        paramnames = config.get(root, "paramnames").split(";")
        outputnorm = config.get(root, "outputnorm").split(";")
        outputnorm = [float(val) for val in outputnorm]
        dataCount = config.getint(root, "datacount")
        options.seed = config.getint("training_%s"% pptyname, 'seed')
        if hasattr(options, "sqlFileName") and options.sqlFileName:
            sqlFileName = options.sqlFileName
        else:
            sqlFileName = config.get(root, "sqlfilename")
        gm0 = getModelDict(config, propertyName=pptyname, 
            parameterNames=paramnames, outputnorm=outputnorm, 
            paramCount=paramcount, dataCount=dataCount, 
            version=metaphorversion)
        if resultFrame is None:
            if os.path.exists(gmxfile):
                dico = getDictFromGmx(gmxfile)            
        else:
            if "ID" in resultFrame.columns:
                indexlist = resultFrame["ID"][:countmax]
            else:
                indexlist = resultFrame.index[:countmax]
            config.set(root, "mcount", "%d" % countmax)
            if not gmxfile or not os.path.exists(gmxfile):
                gmxfile, dico = getGmxFileAndSave(sqlFileName, gm0, 
                    config, indexlist, options, full=True, 
                    dosave=(mcount != countmax))
                config.set(root, "gmxfile", gmxfile)
            else:
                dico = getDictFromGmx(gmxfile)
    
    apiTrainRes = nn1serv.apiTrainResults(options, resfile, 
        gmxfile=gmxfile, trainDataFrame=trainDataFrame, mynames=mynames) 
    trainFrame, looTrainFrame, bsTrainFrame, IDlist, root, \
        trainresultColumn, gmxfile = apiTrainRes # 
#     module.__del__()
#     module = None
    if options.notrain and (trainFrame is not None) and (trainFrame.shape[0] > dataCount):
        lst = list(trainFrame.index)[dataCount:]
        trainFrame.drop(lst, inplace = True)
        
    nn1serv.saveFrameToExcel(options, trainFrame, excelwriter, 
        mynames.trainsheetname, actionName='train')
    # if looTrainFrame is not None:
    nn1serv.saveFrameToExcel(options, looTrainFrame, excelwriter, 
        mynames.lootrainsheetname, actionName='lootrain')
    # if bsTrainFrame is not None:
    nn1serv.saveFrameToExcel(options, bsTrainFrame, excelwriter, 
        mynames.bstrainsheetname, actionName='bstrain')
        
    if 'test' in options.actionlist and options.test:
        
        message0 = "launch test?" if options.notrain else  "continue and launch test?"
        message = ""
        valdef = int(nn1serv.dialogdefaults['action']['run_test'])
        if not yesNoQuestion(message0, valdef, message, forcedefault=options.yes, doprint=doprint):
            doprint("aborted")
            finished(tempres)
            return None, None  # basicTrainTestAction
        doprint("Running Test")
        cfgfile = cfgfile if cfgfile else options.cfgfile 
        datacount = 0 if trainFrame is None else trainFrame.shape[0]
        testFrame, testresultColumn = \
        nn1serv.testAction(options, testDataFrame, datacount, IDlist, 
            cfgfile, gmxfile, dico, doprint=doprint)
            
        doprint('Test done')
    
        if options.verbose >= 5:  
            formatters = {'RoundoffTest': roundoff_format(), 'ID': IDformat()}
            doprint(testFrame.to_string(float_format=float_format(options.verbose), formatters=formatters))
            
        nn1serv.saveFrameToExcel(options, testFrame, excelwriter, 
            mynames.testsheetname, actionName='test')  
    
    startwithlootest = True
    if 'loo'in options.actionlist:
        startwithlootest = False
        
        res = startExtraAction(options, config, module, trainDataFrame, 
                tempres, actiontype='loo', excelwriter=excelwriter, 
                doprint=doprint, mynames=mynames) 
        if res is None: 
            return None, None  # basicTrainTestAction
        module, datacount, datasize, dico, gmxfile, startwithbstest = res
        
        res = nn1serv.looTrainAction(options, module, trainDataFrame, 
                resultFrame, doprint=doprint, mynames=mynames) 
        looTrainFrame, lootrainfailed, LOOResultTrainColumn, gmxfileLOO, \
            sqlLOOFileName = res
            
#         decorname = "{0}train".format(fullActionNames[options.lastaction])
        decorname = fullActionNames[options.lastaction]
        nn1serv.saveFrameToExcel(options, looTrainFrame, excelwriter, 
            mynames.lootrainsheetname, decorname)
        doprint("Writing LOO model file: {0}".format(make_extern(gmxfileLOO, options)))
        doprint("{0} done".format(fullActionNames[options.lastaction]))
        if lootrainfailed:
            looTrainFrame = None                
    if 'lootest' in options.actionlist:
        if startwithlootest:
            res = startExtraAction(options, config, module, trainDataFrame, 
                testDataFrame, apiTrainRes, tempres, actiontype='lootest', 
                excelwriter=excelwriter,
                currentTrainFrame=trainDataFrame, 
                sheetname=mynames.lootrainsheetname, resfile=resfile, 
                doprint=doNothing) 
            if res is None: 
                return None, None  # basicTrainTestAction
            module, _, looTrainSheetName, ResultTrainColumn,\
                IDList, startsloowithtest = res
            
            LOOResultTrainColumn = sum([len(val) for val in options.datafields])
            if not 'identifiers' in options.grouplist:
                LOOResultTrainColumn += 1
             
        looTestFrame = nn1serv.looTestAction(options, testDataFrame, resfile, 
            IDlist, gmxfileextra=gmxfileLOO ,doprint=doprint) #tempres, excelwriter, lootrainsheetname, apiTrainRes, 
        nn1serv.saveFrameToExcel(options, looTestFrame, excelwriter, 
            mynames.lootestsheetname)  #, with index='identifiers' in options.grouplist)
        doprint("{0} done".format(fullActionNames[options.lastaction])) 
        
    startwithbstest = True
    if 'bootstrap' in options.actionlist:
        startwithbstest = False
#         curaction = 'bootstrap'
        res = startExtraAction(options, config, module, trainDataFrame, 
                tempres, actiontype='bootstrap', excelwriter=excelwriter, 
                doprint=doNothing)
        if res is None: 
            return None, None  # basicTrainTestAction 
        module, datacount, datasize, dico, gmxfile, startwithbstest = res
        
        bsTrainFrame, bstrainfailed, BSResultTrainColumn, gmxfileBS, \
            sqlBSFileName = \
            nn1serv.bsTrainAction(options, module, trainDataFrame, resultFrame, 
                                 doprint=doprint, mynames=mynames)
        decorname = "{0}train".format(fullActionNames[options.lastaction])
        nn1serv.saveFrameToExcel(options, bsTrainFrame, excelwriter, 
            mynames.bstrainsheetname, decorname)
        doprint("{0} train done".format(fullActionNames[options.lastaction])) 
        if  bstrainfailed:
            bsTrainFrame = None                     
    
    if 'bootstraptest' in options.actionlist:
        if startwithbstest:
            module, bsTrainFrame, bstrainsheetname, trainresultColumn, IDList, \
            startsbswithtest = \
            res = startExtraAction(options, config, module, trainDataFrame, 
                testDataFrame, apiTrainRes, tempres, actiontype='bootstraptest', 
                excelwriter=excelwriter, currentTrainFrame=bsTrainFrame, 
                sheetname=mynames.bstrainsheetname, resfile=resfile, 
                doprint=doNothing)
            if res is None: 
                return None, None  # basicTrainTestAction
            module, bsTrainFrame, bstrainsheetname, trainresultColumn, IDList, \
            startsbswithtest = res
    
        bsTestFrame = nn1serv.bsTestAction(options, testDataFrame, resfile, 
            IDlist, gmxfileextra=gmxfileBS ,doprint=doprint) 
        nn1serv.saveFrameToExcel(options, bsTestFrame, excelwriter, 
            mynames.bstestsheetname) 
        doprint("{0} test done".format(fullActionNames[options.lastaction])) 

    if 'usage' in options.actionlist:
        nn1serv.usageAction(options, options.origin, options.data)

    
    if options.dotimer and (len(options.multihidden) > 1): 
        delta = float(time.time() - starttimeloc)
        doprint("Running time for {0} hidden neurons: {1}".format(
            options.hidden, second2str(delta)))

    
    libfilename = options.modulename
    if not libfilename and cfgfile:
        config = defaultedConfigParser(cfgfile)
        libfilename = config.get(root, "module")
    if not os.path.exists(libfilename):
        libfilename = os.path.join(options.savedir, libfilename)
    excelfilename = nn1serv.getExcelFileName(options)
    options.metaphorResult.append(excelfilename)
    dico = OrderedDict()
    for key, value in nn1serv.dicoversion.items():
        dico["{} version".format(key)] = (value, 'text')
    if sqlFileName:
        dico["SQL file"] = (make_extern(sqlFileName, options), 'text')
    if sqlLOOFileName:
        dico["SQL LOO file"] = (make_extern(sqlLOOFileName, options), 'text')
    if sqlBSFileName:
        dico["SQL BS file"] = (make_extern(sqlBSFileName, options), 'text')
    if gmxfile:
        dico["Model file"] = (make_extern(gmxfile, options), 'text')
    if gmxfileLOO:
        dico["Model LOO file"] = (make_extern(gmxfileLOO, options), 'text')
    if gmxfileBS:
        dico["Model BS file"] = (make_extern(gmxfileBS, options), 'text')
        
    gmCustomProperties = getCustomDict(options, dico)

    if options.copytype and libfilename: 
        sheetList = [mynames.resultsheetname, mynames.trainsheetname, 
            mynames.testsheetname, mynames.lootrainsheetname, 
            mynames.lootestsheetname, mynames.bstrainsheetname, 
            mynames.bstestsheetname] 
        frameList = [resultFrame, trainFrame, testFrame, looTrainFrame, 
            looTestFrame, bsTrainFrame, bsTestFrame]
        modeldic, _ = ReadModule(libfilename, pptyname=options.pptyname, 
            dodelete=True)
        modeldic['bestCount'] = sorted(options.multimaxrec)
        excelresult = finishExcel(excelwriter,
            options, 
            gmCustomProperties, 
            sheetList, 
            frameList, 
            modeldic, 
            libfilename, 
            IDlist, 
            trainresultColumn,  
            testresultColumn, 
            LOOResultTrainColumn,
            loowidth, 
            traintype, 
            tempres)
        if excelresult and cfgfile and nn1serv._hasTrain(options):
            # on ne sauvegarde que si on vient d'apprendre.
            config = defaultedConfigParser(cfgfile)
            config.set('training', 'excelresult', excelresult)
            config.save()
    else:
        doprint("no copy")

    return modeldic, gmCustomProperties # basicTrainTestAction
    
def manageApiOptionsResult(options, toprint, stopcode, doprint, encoding):
    """Processing special asking (stop, display) in options.
    Return True to stop the program.
    """
    if stopcode & nnu.OPTION_STOP:
        doprint(toprint, file=sys.stderr)
        return 1      
    
    if stopcode & nnu.OPTION_DISPLAY_FILE_AND_STOP:
        # affichage la licence ou de l'aide prise dans le fichier "toprint"
        #if (ou tfile is not None):
        if int(options.verbose) >= 5:
            doprint(toprint, file=sys.stderr)
#            doprint()
            doprint(encoding)
            doprint()
        with open(toprint, 'rb') as ff:  #, encoding='UTF-8'
            line = ff.readline()
            while line:
                #val = line.decode("ISO-8859-15") 
                val = line.decode("UTF-8") 
                doprint(val.rstrip(), file=sys.stderr) 
                line = ff.readline()
            # val = ff.read().decode("ISO-8859-15") 
        doprint()
        return 2
    
    elif stopcode & nnu.OPTION_WARN_AND_STOP: 
        # affichage du message toprint   
        doprint(toprint, file=sys.stderr)
        return 3
    
    if options.verbose >= 5:
        import platform
        doprint("Python", platform.python_version())               
    
    if toprint:
        # affichage du message
        doprint(toprint)
        if stopcode & nnu.OPTION_WARN_AND_ASK: 
            # test si possibilite d'arret
            message = "corrected options accepted"
            valdef = int(nn1serv.dialogdefaults['action']['continue_anyway'])
            if not yesNoQuestion("continue anyway?", 'y', message, 
                forcedefault=options.yes, doprint=doprint):
                doprint("aborted")
                finished("")
                return 4
    return 0
    
def startRun(argv=[], externaloptions=None, tolink=True, nofile=False, 
        internalEnv=0, debug=0):
    if tolink:
        targetfile = os.path.expanduser("~/linkedServices.txt")
        with open(targetfile, 'w')  as ff:
            nn1serv.linkToServices(file=ff, nn1serv=nn1serv)
    # traitement de l'environnement interne        
    if internalEnv:
        if internalEnv ==1:
            target = 'arguments.txt'
        else:
            target = 'arguments{}.txt'.format(internalEnv)
        if debug:
            print('internalEnv {}'.format(target))
        argsfile = ""
        argsfile0 = os.path.expanduser(os.path.join('~', 'argsdir', target))     
        if os.path.exists(argsfile0):
            argsfile = argsfile0
        else:
            argsfile1 = os.path.expanduser(os.path.join('~', 'docker', 
                                                        'argsdir', target))
            if os.path.exists(argsfile1):
                argsfile = argsfile1
            else:
                print("cannot find argument file", argsfile0, "or", argsfile1)
        if not os.path.exists(argsfile):
            print("demo{} argument is not recognized a valid command".format(
                internalEnv))
            return  # runOnce
        setEnvironFromFile(argsfile)
        if debug:
            print("argsfile", argsfile)
            print("argv", argv)
            
    options, toprint, stopcode = nn1serv.api_options(argv, 
        proposedOptions=externaloptions, nofile=nofile, debug=debugrun)
    return options, toprint, stopcode
        
def runOnce(argv=[], externaloptions=None, doprint=False, tolink=True, 
            nofile=False, internalEnv=0):
    global nn1serv

    starttime = time.time()
    excelactionlist = ['train', 'test', 'loo', 'lootest', 'bootstrap', 
                       'bootstraptest']   
    mynames = Namespace(**namesdict)
    
    tempres = ""
    toprint = ""
    stopcode = False
    
    nn1serv = importlib.import_module("metaphor.nn1.api._api_service")
    demodebug = nn1serv.demodebug & nn1serv.DEMO_DEBUG_DEMO
    options, toprint, stopcode = startRun(argv=argv, 
        externaloptions=externaloptions, nofile=nofile, tolink=tolink, 
        internalEnv=internalEnv, debug=demodebug)
    
    if debugrun or demodebug:
        for ind, val in enumerate(argv):
            print("argv[{0}]: {1}".format(ind, val))
    
#     if internalEnv:
#         if internalEnv ==1:
#             target = 'arguments.txt'
#         else:
#             target = 'arguments{}.txt'.format(internalEnv)
#         if demodebug:
#             print('internalEnv {}'.format(target))
#         argsfile = ""
#         argsfile0 = os.path.expanduser(os.path.join('~', 'argsdir', target))     
#         if os.path.exists(argsfile0):
#             argsfile = argsfile0
#         else:
#             argsfile1 = os.path.expanduser(os.path.join('~', 'docker', 
#                                                         'argsdir', target))
#             if os.path.exists(argsfile1):
#                 argsfile = argsfile1
#             else:
#                 print("cannot find argument file", argsfile0, "or", argsfile1)
#         if not os.path.exists(argsfile):
#             print("demo{} argument is not recognized a valid command".format(
#                 internalEnv))
#             return  # runOnce
#         setEnvironFromFile(argsfile)
#         if demodebug:
#             print("argsfile", argsfile)
#             print("argv", argv)

    try:
        options.debug |= nn1serv.demodebug
    except: pass
    try:
        outfile = options.outfile
    except:
        outfile = sys.stderr
    doprint = toPrint(outfile) 
    if outfile:
        encoding = outfile.encoding  
        
    if manageApiOptionsResult(options, toprint, stopcode, doprint, encoding):
        # il y a eu une erreur ou une demande d'affichage, On sort du programme.
        return  # runOnce               
    
    if 'usage' in options.action:
        # demande d'usage
        return nn1serv.usageAction(options) # runOnce 
    
    if not options.source and 'train' in options.actionlist:
        raise nn1serv.monalError("This program needs a data file.")
    elif not options.source and not options.test and \
        'test' in  options.actionlist:
        raise nn1serv.monalError("This program needs a test file.") 
    
    createArgumentFile = 'analyse' in options.actionlist or \
        ('preproc' in options.actionlist and len(options.actionlist)==1)
        # Lecture et analyse d'un nouveau fichier de données, creation du 
        # fichier d'arguments

    # analysisAction est toujours appelée
    
    options = nn1serv.analysisAction(options, doprint=doprint, 
        forceAnalyse=createArgumentFile)
    if options is None:
        doprint("Input error. Program stopped !!!")
        return -1  # runOnce  
    
    if createArgumentFile:
        if options.notest:
            forceAction = "train"
        else:
            forceAction = "train,test"
        res = nn1serv.saveOptionsToFile(options, forceAction=forceAction, 
            forceYes=True, forceModel=True, doprint=doprint)
        return res  # runOnce
#######################################################################
    trainDataFrame = None
    filetype = options.filetype
    grouplist = options.grouplist
    if nn1serv._hasTrain(options):
        datafile = options.source
        datarange = options.datarange
        fieldlist = options.datafields
        drop = ('identifiers' in grouplist) and \
            not grouplist.index('identifiers') and (len(fieldlist[0]) == 1)
        trainDataFrame, _ = get_modelDataframe(datafile, datarange, fieldlist, 
            grouplist, filetype=filetype, drop=drop, withindexdict=False) 

    testDataFrame = None
    if nn1serv._hasTest(options):
        if not options.test:
            options.test = options.source
        if not options.testrange:
            options.testrange = 'TEST'
        if not options.testfields:
            options.testfields = options.datafields
        datafile = options.test
        datatest = options.testrange
        fieldlist = options.testfields
        testfiletype = options.testfiletype
        drop = ('identifiers' in grouplist) and \
            not grouplist.index('identifiers') and (len(fieldlist[0]) == 1)
        try:
            testDataFrame, _ = get_modelDataframe(datafile, datatest, fieldlist, 
                grouplist, filetype=testfiletype, drop=drop, 
                withindexdict=False) 
        except AttributeError as err:
            if drop:                
                fieldlist = fieldlist[1:]
                newfieldlist = [[val - 1 for val in lst] for lst in fieldlist]
                grouplist = grouplist[1:]
                drop = ('identifiers' in grouplist) and \
                    not grouplist.index('identifiers') and \
                    (len(fieldlist[0]) == 1)
                testDataFrame, _ = get_modelDataframe(datafile, datarange, 
                    newfieldlist, grouplist, filetype=filetype, drop=drop, 
                    withindexdict=False)
            else:
                testDataFrame = None
        except Exception as err:
            raise
#         except ValueError as err:
#             raise dataReadingError("Empty data in line {}".format(ind))
#             raise nn1serv.monalError("Error while reading test data")
            
        
    if not 'usage' in options.action:
        if not trainDataFrame:
            options.propertyName = testDataFrame.fieldsOf('outputs')[0]
            options.propertyunit = testDataFrame.units[options.propertyName]
            options.inputcount = len(testDataFrame.fieldsOf('inputs'))
        # 
            origin = nn1serv.getOrigin(options)
            if origin and os.path.isfile(origin):
                filename = origin 
                
        else:
            options.propertyName = trainDataFrame.fieldsOf('outputs')[0]
            options.propertyunit = trainDataFrame.units[options.propertyName]
            options.inputcount = len(trainDataFrame.fieldsOf('inputs'))
    
    options.tableName = 'trainingResult'
    options.inoutcount = 0
    memtarget = options.targetfolder[:]
    options.metaphorResult = []
    for seed in options.multiseed:
        # boucle sur les graines aleatoires (seed)
        excelresult = ""
        excelwriter = None
        cfgfile = ""
        resfile = ""
        trainfailed = False
        dico = None
        resultFrameList = []
        if seed < 0:
            seed = randint(0x10, 0xFFFFFFFF)    
        options.seed = seed
        if len(options.multihidden) > 1:
            # si on est en multihidden, on cree un repertoire ici pour la seed 
            # en cours
            st = strintlist(options.multihidden, delimiter="-", 
                groupdelimiter="--", compact=True)
            dirname = "{0}-SEED{1}-{2}N".format(options.root, seed, st)
            options.targetfolder = os.path.join(memtarget, dirname)
            options.targetfolder = IndexFilename(options.targetfolder)
            if not os.path.exists(options.targetfolder):
                os.makedirs(options.targetfolder)
            if options.arg_file:
                targetfile = os.path.join(options.targetfolder, "arguments.txt")
                with open(options.arg_file, 'r') as sf:
                    with open(targetfile, 'w') as tf:
                        for line in sf:
                            if len(line) and not line.startswith("#"):
                                lst = line.split("=")
                                if (len(lst) > 1) and lst[0].strip() == "SEED":
                                    lst[1] = str(seed)
                                    if line.endswith("\n"):
                                        lst[1] += "\n"  
                                line = "=".join(lst)
                            tf.write(line)

        options.configstrMem = options.configstr
        for options.hidden in options.multihidden:  # 
            # boucle sur les neurones caches (hidden)
            newtestframe = None if testDataFrame is None else \
                testDataFrame.copy()
            try:
                modeldic, gmCustomProperties = basicTrainTestAction(options, 
                    trainDataFrame, newtestframe, doprint, resultFrameList, 
                    excelactionlist, mynames)
            except Exception as err:
                raise
        # fin boucle sur hidden

        if len(options.multihidden) > 1:
            nn1serv.excelRecapitulation(options, resultFrameList, modeldic, 
                gmCustomProperties, doprint)
                
    # fin boucle sur seed

    if options.dotimer: 
        delta = float(time.time() - starttime)
        doprint("Running time {0}".format(second2str(delta)))
    finished(tempres)
    return   # runOnce 
    # end runOnce               

def run(argv=[], doprint=True, internalEnv=0):
    if debugrun:
        print("inside run:")
#     now = time.strftime("%c")
    try:
        res = runOnce(argv, doprint=doprint, internalEnv=internalEnv)
    except QuestionInterrupt:
        print("User interruption")
        res = None
    except Exception as err:
        res = None
        print(err)
        
    if isinstance(res, tuple) and len(res) >= 2:
        options = res[0]
        argname = res[1]
        if argname and os.path.exists(argname):
            mess = "do you want to run the new project ?"
            valdef = int(nn1serv.dialogdefaults['action']['run_new_project'])
            if yesNoQuestion(mess, default=valdef, outfile=sys.stdout, 
                forcedefault=options.yesyes):  #, verbose=verbose)
                argumentfile = "@{0}".format(argname)
                options.modelcreation = False
                try:
                    res = runOnce(argv=["", argumentfile], 
                              externaloptions=options, tolink=False)
                except Exception as err:
                    res = None
                    print(err)
    return res
    
def supervisor(args=None): 
    res = 1
    caller = os.getenv("CALLER", 0)
    argv = args if args is not None else sys.argv[1:] 
    if debugrun:
        print("supervisor entry point") 
        for val in argv:
            print("\t", val)
    firstarg = None if not len(argv) else str(argv[0])  #.lower()       
    if firstarg is None:
        # pas d'argument
        res = run(argv)
    else:
        if debugrun:
            print("firstarg", firstarg)
        if firstarg.startswith('demo'):  # and caller == 2
            # run demo
            ends = firstarg[len('demo'):] 
            if not len(ends):
                index = 1
                print('Run demo')
            else:
                index = int(ends)
                print('Run demo {}'.format(index))
            res = run(argv[1:], doprint=True, internalEnv=index)
        elif firstarg.startswith('@'):
            # fichier d'arguments en premier
            setEnvironFromFile(firstarg[1:])
            res = supervisor (argv[1:])
        elif firstarg.startswith('-'):
            # arguments en ligne de commande
            res = run(argv) 
        elif firstarg in ['version', 'license', 'help', 'description', 'env', 
                          'vba']:
            # information specifiques
            res = printInfo(firstarg, caller)
        elif firstarg in ['use', 'usage']:
            # mode utilisation
            res = usage(argv[1:])
        elif firstarg in ['get', 'getproperty']:
            # mode utilisation interne
            if caller == 2:
                res = usageInterne(argv[1:])
            else:
                res = usage(argv[1:])
        elif firstarg == 'run':
            # run standard
            res = run(argv[1:])
        elif firstarg == 'server':
            try:
                from metaphor.metaphor_api_server import api_server
                res = api_server.run(argv[1:])
            except Exception as err:
                print(err)
                print("cannot open metaphor server") 
                res = -1
        else:
            print("'{}' argument is not recognized as a valid command".format(
                firstarg)) 
            res = -1
    return res  
              
if __name__ == '__main__':

    res = supervisor()
#    print("Metaphor done")