'''
Created on 20 févr. 2019

@author: jeanluc
'''
import os
import numpy as np
from pandas import DataFrame
from string import ascii_uppercase
#from random import choice
import random as rnd
from pandas import ExcelWriter

#import metaphor
from ..nntoolbox.datareader.datasource import DataSource
from ..nntoolbox.utils import orderedIndexes, make_extern
from ..nntoolbox.lineartoolbox import randomProbe  
from ..nntoolbox.utils import doNothing, setRandSeed
from ..nntoolbox.cmd_line_dialogs import choiceQuestion, \
    valueQuestion, yesNoQuestion #, chooseFields
from ..nntoolbox.progress import Progress_tqdm  #FanWait, 
from ..nntoolbox.constants import nobarverb
from ..nntoolbox.excelutils import enrichExcelPreproc
from ..nntoolbox.filetoolbox import decorfile

from ..nn1.api._api_service import CloseExcelwriter  #, getExcelFileName, createExcelwriter 
#from 

normalizeVectors = False # Ne sert a rien de mettre "True"

preprocdefaults = {
    'dopreproc': 1,
    'new_threshold': 0,
    'new_preproc': 0,
    }

dialogdefaults = preprocdefaults
preproctypelist = ['', 'linear', 'crossproduct', 'full2ndorder']
""" crossproduct -> only cross products in the second order.
    full2ndorder -> full second order.
"""
preprocnamelist = ['', 'linear', 'linear + cross-products', 'full quadratic']
    
def printresult(options, message, vecind, Pertinence, inputTitles, choices=None, 
        printTitles=True, resultstr="score", doprint=doNothing):
    doprint(message)
    lmax = max([len(val) for val in inputTitles])
    nametitle = "input{0}".format(" "*(lmax-4))
    if printTitles:
        doprint("\t".join(["ind", nametitle, resultstr]))
    addon = [lmax-len(val) for val in inputTitles]
    for ind in vecind:
        if choices is not None:
            choicex = choices[ind]
        else:
            choicex = True
        if choicex:
            prob = "{0:<4.3g}".format(Pertinence[ind])
            supp = " " * addon[ind]
            title = "{0}{1}".format(inputTitles[ind], supp)
            doprint(ind, title, prob, sep="\t")        

def doPreProc(options, Inputs, Outputs, inputTitles, probecount=-1, 
        randomSource='normal', doprint=doNothing):
    
    if not options.preproctype in preproctypelist[1:]:
        doprint("Random probe analysis failed")
        return None, None
    
    preprocindex = preproctypelist[1:].index(options.preproctype)
    directsquare = preprocindex == 2 
    crossprod = preprocindex > 0
    testconstitution = (crossprod, directsquare)
    if probecount < 0:
        mess = "Enter number of random probe tests"
        probecount = valueQuestion(mess, options.probecount, 
            "Probe tests", doprint=doprint, verbose=options.verbose, 
            forcedefault=options.yes)  #, prefix=prefix)
    options.probecount = probecount
    
    with Progress_tqdm(options.probecount, desc=options.preproctype,   #'random probe', 
            nobar=options.verbose<nobarverb) as update:
        
        ndc, indexes, results2 = randomProbe(Inputs.T, Outputs.T, 
            options.probecount, seed=options.seed, randomSource=randomSource, 
            testconstitution=testconstitution, progress=update,
            detailedoutput=True, donorm=normalizeVectors) 
        
        update.ends()

    Pertinence = np.zeros((ndc))
    for index, value in zip(indexes, results2):
        for ind in index:
            Pertinence[ind] = max(Pertinence[ind], value)  
    vecind = orderedIndexes(Pertinence)
    message = "Probe results with {0} selection ({1}):".format(options.preproctype, options.probecount)
    printresult(options, message, vecind, Pertinence, 
        inputTitles=inputTitles, printTitles=True, doprint=doprint)
    return Pertinence, vecind, indexes, results2

def _preprocAction(options, doprint=doNothing):
    
    preprocSheetName = "Pre Processing"
    seedmem = options.seed
    pertinenceFrame, vecinds, localframes = _doPreProcToFrames(options, doprint=doprint)
    
    if options.copyexcel: 
        tempstr = ''.join([rnd.choice(ascii_uppercase) for _ in range(8)])
        fname = os.path.join(options.targetfolder, "{0}.xlsx".format(tempstr))
        excelwriter = ExcelWriter(fname, engine='xlsxwriter')
        pertinenceFrame.to_excel(excelwriter, preprocSheetName)
        for key, frame in localframes.items():
            frame.to_excel(excelwriter, key)
        for key in localframes.keys():
            enrichExcelPreproc(excelwriter, key, fname)
        enrichExcelPreproc(excelwriter, preprocSheetName, fname, True)
        fname = CloseExcelwriter(options, excelwriter, forcename="PreProc", 
            forbiden=['hidden'], Sheet=preprocSheetName)
    elif options.copytxtcsv and os.path.exists(options.targetfolder):
        fname = os.path.join(options.targetfolder, 'resultFrame')
        fname = decorfile(fname, options, ".{0}".format(options.copytype), indextemplate="(%d)")                    
        with open(fname, 'w') as ff:
            ff.write(pertinenceFrame.to_csv(sep=options.sep, decimal=options.decimal))
    options.seed = seedmem
    externpath = make_extern(fname, options)
    doprint("Pertinence analysis is saved in file : {}".format(externpath))
    inputTitles = list(pertinenceFrame.index)
    dopreproc = options.preproctype in preproctypelist[1:] 
    res = False 
    while dopreproc:
        preproctype = preproctypelist.index(options.preproctype)  
        mess = "Choose the preprocessor action by its index."
        printMessage = "Preprocessor action"
        choicelist = ["No_Action", "Linear random probe", "Linear + cross-product random probe", "Full 2nd order random probe"]
#         try:
        preproctype, index = choiceQuestion(mess, choicelist, 
            preproctype, printMessage, returnType=str, doprint=doprint, 
            extradisplay=True, listindexed=True, forcedefault=options.yes,
            fulloutput=True)
#         except QuestionInterrupt:
#             
        if not index: 
            return None
        options.preproctype = preproctypelist[index]
        Pertinence = pertinenceFrame.ix[index-1]
        vecind = vecinds[index-1]
        
        if Pertinence is None:
            return -1
        doselect = True
        while doselect:
            try:
                options.pertinencethreshold = valueQuestion("Enter the input selection pertinence", 
                    options.pertinencethreshold, "Input selection pertinence", 
                    forcedefault=options.yes, doprint=doprint, 
                    verbose=options.verbose, returnType=float) 
            except Exception as err:
                doprint(str(err))
                return 1
            res = False            
            if (0.0 < options.pertinencethreshold < 1.0):
                PertColName = pertinenceFrame.columns[index-1]
                Perts = list(pertinenceFrame[PertColName])
                choices = [val < options.pertinencethreshold for val in Perts]
                if any(choices):
                    mess = "Following inputs may be removed:"
                    printresult(options, mess, vecind, Perts, 
                        inputTitles=inputTitles, choices=choices, printTitles=False, 
                        doprint=doprint)
                    mess = "Do you accept?"
                    selcount = 0
                    for choicex in choices:
                        if not choicex:
                            selcount += 1
                    OKChoice = vecind[:selcount]
                    OKChoice.sort()
                    OKTitles = [inputTitles[val] for val in OKChoice]
                    st = ", ".join(OKTitles)
                    printMessage = ""  
                    res = yesNoQuestion(mess, default='Y', printMessage=printMessage, 
                        forcedefault=options.yes, verbose=options.verbose, 
                        doprint=doprint)
                    if res:
                        inputindex = options.grouplist.index('inputs')
                        inputini = options.datafields[inputindex]
                        
                        Inputs = [val for ind, val in enumerate(inputini) if ind in OKChoice]
                        options.groupcount[inputindex] = len(Inputs)
                        options.datafields[inputindex] = Inputs
                        if options.test:
                            testinputini = options.testfields[inputindex]
                            Inputs = [val for ind, val in enumerate(testinputini) if ind in OKChoice]
                            options.testfields[inputindex] = Inputs
                if res:
                    doselect = False
                else:
                    mess = "will you try a new selection threshold ? "
                    valdef = int(dialogdefaults['preproc']['new_threshold'])
                    doselect = yesNoQuestion(mess, default=valdef, printMessage="", 
                            forcedefault=options.yes, verbose=options.verbose, 
                            doprint=doprint)
        if res:
            dopreproc = False
            doprint("Inputs will be {0}".format(st))
        else:
            mess = "will you try a new pre-processing ? "
            valdef = int(dialogdefaults['preproc']['new_preproc'])
            dopreproc = yesNoQuestion(mess, default='y', printMessage="", 
                    forcedefault=options.yes, verbose=options.verbose, 
                    doprint=doprint)
    if res:
        return options
    return None


def _doPreProcToFrames(options, verbose=3, doprint=doNothing):
    
    options.seed = valueQuestion("Enter a random seed (-1 for no seed)", 
        options.seed, "Seed",  
        doprint=doprint, verbose=verbose, returnType=int)  #forcedefault=forceyes, prefix=prefix,
    setRandSeed(options.seed)
    curpreproc = options.preproctype
    source = DataSource(options.source, options.filetype, options.datarange, 
        datafmt=options.datafields, titles=True)
    datas, titles = source.getDataArrays(options.datarange, 
        fieldsList=options.datafields, titles=True)  
    inputTitles = titles[options.grouplist.index('inputs')]
    Inputs = np.asarray(datas[options.grouplist.index('inputs')])
    Outputs = np.asarray(datas[options.grouplist.index('outputs')])
    perts = []
    vecinds = []
    options.probecount = valueQuestion("Enter number of random probe tests", 
        options.probecount, "Probe tests", doprint=doprint, 
        verbose=options.verbose, forcedefault=options.yes)  

    choicelist = ['normal', 'shuffle']
    printMessage = "Random method"
    mess = "Please choose the random method :"
    randomSource, _ = choiceQuestion(mess, choicelist, defaultindex=1, 
        printMessage=printMessage, returnType=int, extradisplay=True, 
        listindexed=True, fulloutput=True, doprint=doprint)
    options.randomSource = randomSource
    localframes = {}
    for preproctype in preproctypelist[1:]:
        options.preproctype = preproctype
        Pertinence, vecind, indexes, results2 = doPreProc(options, Inputs, 
                                                          Outputs, 
            inputTitles, randomSource=randomSource,
            probecount=options.probecount) 
        if Pertinence is None:
            break
        pertlist = list(Pertinence)
        Pertinence = np.asarray(pertlist)
        perts.append(Pertinence)
        vecinds.append(vecind)
        localTitles = [(" * ".join([inputTitles[val] for val in indx])) 
                       for indx in indexes]
        localframe = DataFrame(results2, columns=[preproctype], 
                               index=localTitles)
        localframes[str(preproctype)] = localframe 
    ll = list(map(list, zip(*perts)))
    pertinenceFrame = DataFrame(ll, columns=preprocnamelist[1:], 
                                index=inputTitles) 
    
    if doprint:
        doprint(pertinenceFrame)
    
    options.preproctype = curpreproc
    return pertinenceFrame, vecinds, localframes#, randomSource

if __name__ == '__main__':
    pass