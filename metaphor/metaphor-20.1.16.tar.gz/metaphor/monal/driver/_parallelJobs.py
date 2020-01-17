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
Created on 10 juin 2016

@author: jeanluc
'''

import sys, os
import numpy as np
import random
from ctypes import byref, c_int, c_void_p

from .. import monalconst as C
from ...nntoolbox.utils import RE_LOO, RE_SUPER, BSGROUP 
from ...nntoolbox.sqlite_numpy import insertDataToDb

DEBUG_TRAIN_JOB = 0

no_parallel_seed = os.environ.get('NO_PARALLEL_SEED', 0)

def onEndIter(history, trainend, index, counter, epochs, progress=None, 
              dowrite=sys.stdout.write):
    
    message = ""
    curindex = index+1
    docontinue = (index >= 0)
    if docontinue and progress:
        docontinue = progress(counter+1)
        if isinstance(docontinue, tuple):
            docontinue = docontinue[0]
    if dowrite:
        if not docontinue:
            dowrite("Training aborted", color='green')
            dowrite("\n", color='black')
        elif history is not None:    
            lst = ["" if (index < 0) else "training #%s"% (index+1)]
            lst.append( "\tepoch: %s"%(epochs))
            lst.append("\tini-stddev: %s"%(history[0]))
            lst.append("\tend-stddev: %s"%(history[epochs]))
            if trainend:
                lst.append("\ttraining end: %s"% C.END_TRAINING_DICT[trainend])
            lst.append("")
            message = "\n".join(lst)
            dowrite(message)
        
    return not docontinue #, message

def onSpecialResult(dbConnect, tableTmpl, code, epochs, startweights, 
        endweights, molindex, initindex, indexReturn, cost, press, out, lev, 
        resultvector, dispersion, inittype, target, locseed):  #
    startweights0 = 0.0
    for value in startweights:
        if value != 0:
            startweights0 = value
            break 
    disp0 = dispersion[0,0] if dispersion is not None else None
    tablename = tableTmpl % molindex #"trainingResults%03d"% molindex
    data = {cname: val for cname, val in zip(C.CRITERION_NAME.values(), 
                                             resultvector)}
    data.update({
        'param_start': startweights,
        'param_start0': startweights0,
        'param_end': endweights,
        'param_end0': endweights[0],
        'dispersion': dispersion,
        'dispersion0': disp0,
        'code': code,
        'indtrain': initindex,
        'out': out,
        'leverages': lev,
        'inittype': C.INIT_NAME[inittype],
        'seed': locseed,
        'target': target
        })
    insertDataToDb(dbConnect, table=tablename, data=data)
    return 0

def onReturnResult(dbConnect, tablename, indcur, resultvector, startweights, 
                   endweights, leverages, dispersion, history, locseed):
    epochs = int(resultvector[C.TCR_EPOCHS])
    disp0 = dispersion[0,0] if dispersion is not None else None
    data = {cname: C.CRITERION_TYPE[tcr](val) for (tcr, cname), 
            val in zip(C.CRITERION_NAME.items(), resultvector)}
    startweights0 = 0.0
    for value in startweights:
        if value != 0:
            startweights0 = value
            break 
    data.update({'ID': indcur+1,
                 'traintype': 0,
                 'ini_stddev': history[0],
                 'end_stddev': history[epochs],
                 'param_start': startweights,
                 'param_start0': startweights0,
                 'param_end': endweights,
                 'param_end0': endweights[0],
                 'leverages': leverages,
                 'leverages0': leverages[0],
                 'dispersion': dispersion,
                 'dispersion0': disp0,
                 'seed': locseed})
    insertDataToDb(dbConnect, table=tablename, data=data)

def trainJob(model, weightsstddev, epochs, withhistory, index, seed):
    assert epochs
    if no_parallel_seed:
        locseed = seed
        locseed0 = seed
    elif (seed is not None) and (seed >= 0):
        locseed0 = seed + (index+1) * 0x1000   
        # 21/03/2019 locseed = seed + index * 0x1000
        random.seed(locseed0)  # 18/04/2018
        locseed = random.randint(0x10, 0xFFFFFFFF)  # 18/04/2018
    else:
        locseed0 = None
        locseed = None
    model.setRandSeed(locseed)
    code = 0
    if not index:
        weights = model.weights.copy()
    else:
        weights = model.newWeights(weightsstddev)
    memweights = weights.copy()
    try:
        res = model.train_integrated(weights, epochs, withhistory, 
                                     computeDispersion=True)  # True
        cur, N, stddev, trainend, hist, code = res[0] 
        if withhistory:
            history = np.sqrt(hist / model.dataCount)
        else:
            history = None  
    except Exception as exres:
        res = [None, None, None]
        N = -1
        stddev = 0.0
        cur = None
        print("trainJob error:", exres)
        if not code:
            code = -1
        res0 = (index, cur, N, stddev, None, None,  None, locseed, code)      
        return res0, res[1], res[2]
    if code:
        cur = None
        stddev = 0.0
        
    res0 = (index, cur, N, stddev, memweights, trainend,  history, locseed0, 
            code)
    return res0, res[1], res[2]

def trainJobBS(model, initlist, inittype, initindex, residuals, BStype,
        settrainindex, epochs, index, computeDispersion, weightsstddev, 
        targets, seed):    
    model.settrainingset()
    epochsmem = epochs    
    BSindex = index if BStype == RE_LOO else BStype 
     
    if no_parallel_seed:
        locseed = seed  
        locseed0 = seed
    elif (seed is not None) and (seed >= 0):
        locseed0 = seed + ((index + 1) * 0xFFFF) + (initindex * 2)  # 0xFFFF = 65535
        random.seed(locseed0)
        locseed = random.randint(0x10, 0xFFFFFFFF)
    else:
        locseed = None
        
    model.setRandSeed(locseed)
    code = model.settrainingset(settrainindex, BSindex, residuals)
    assert (code == 0)
    if inittype == C.INIT_START_PARAM:
        initrecord = initlist[initindex]
        params = initrecord[2].copy()
    elif inittype == C.INIT_END_PARAM:
        initrecord = initlist[initindex]
        params = initrecord[3].copy()
    else:
        params = model.newWeights(weightsstddev)
    if BStype == RE_SUPER:
        indexReturn = initrecord[0]    
    else:
        indexReturn = initindex

    ini_params = params.copy()
    
    res = model.train_integrated(params, epochs=epochsmem, withhistory=False, 
                                 computeDispersion=computeDispersion)
    params, epochs, stddev, trainend, hist, code = res[0]
    press, residuals, singular, leverages, disp, svdlen, deltash, outputs, \
    jacobians = res[1]
    resvec = res[2]
    if BStype == RE_LOO:
        target = targets[index]
        if computeDispersion:
            out, gradient = model.transfergradientindex(params, index=index)
            lev = np.dot(gradient.T, np.dot(disp, gradient))  
    elif BStype in BSGROUP:
        target = None
        out = None
        lev = None
    else:
        out = model.transferindex(params, index=index)
        lev = 0.0
        target = targets[index]
    return  code, epochs, ini_params.copy(), params.copy(), index, initindex, \
        indexReturn, stddev, press, out, lev, resvec, disp, inittype , target, \
        locseed0                                                      
        
