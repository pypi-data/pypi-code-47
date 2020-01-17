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
'''
Created on 13 dec. 2018

@author: jeanluc
'''

'''**Usage running functionalities.**
'''
import os
from metaphor.nntoolbox.datareader.datasource import DataSource
from metaphor.nntoolbox.utils import basefolder
from metaphor.monal import monalconst as C
from metaphor.monal.modelutils import loadModule
from metaphor.monal.driver import Driver
from metaphor.monal.util.utils import getLibExt as libExtension
from metaphor.nn1.api import api as nn_api
from metaphor.version import __version__ as metaphorversion
try:
    from metaphor.chem_gm.api import api as gm_api
    has_gm = True
except ImportError:
    has_gm = False

def analyseTrainingDatafile(filename, filetype="" , datarange="", skipline=0, 
        delimiter=';', dataformat=[0, 1, 2], maxlength=50000, 
        titlesfirst=True, fullH=False, debug=0):
    """Analyse data source content.
    
    - filename -> data file name.
    
    - filetype -> "", "csv", "xls", "xlsx". If filetype=="", filetype will be assigned filename extension.
    
    - datarange -> Name of the data range for xls and xlsx type files only.
    
    - skipline -> number of beginning skipped lines or csv type files only.
    
    - delimiter -> suggested data delimiter character for csv type files only.
    
    - datafmt -> list of data column indexes. Default [0,1,2]
    
    - maxlength -> max number of analysed lines. Default 50000.
    
    - titlesfirst -> boolean: include titles as first line. Default True
    
    return a tuple of 14 elements:
    
    - atoms -> List of atoms present in the base
    
    - grademax -> maximum grade in the base.
    
    - isomax -> maximum isomeric index in the base.
    
    - chiralmax -> maximum chiral index in the base.
    
    - occurs -> dictionary of the atom and structure elements oocurrences.
    
    - occurmols -> dictionary of the molecules occurrences for atom and structure elements.
    
    - cycles -> dictionary of the cycle structure occurrences.
    
    - delimiter -> delimiter. meaningful only for csv type files.
    
    - baselen -> base length
    
    - names -> name list (index 0 of datafmt)
    
    - smilist -> smiles list (index 1 of datafmt)
    
    - pptylist -> property value list (index 2 of datafmt)
    
    - reslist -> list of occurences in each molecule as dictionary
    
    - reslimit -> limited base bool.
    """
    if not has_gm:
        raise Exception("analyseTrainingDatafile is not available")
    return gm_api.analyseTrainingDatafile(filename, filetype, datarange, 
        skipline, delimiter, dataformat, maxlength, titlesfirst, fullH, debug)
    
def get_results_from_smiles(modellist, inputs=None, level=0, 
                            modelindex=-1, parallel=True, progress=None):
    """Create graphmachine models and obtain their results.
     
    parameters:
     - modellist -> list of triplets (sourcefile, model name, smiles code) to perocess.
     - inputs -> None, vector or dictionary
         - None : no input values (default).
         - vector : vector of the input values, in the order of the inputs.
         - dictionary: input value for each input name.
     - level -> level of the required transfer.    
     - modelindex -> Index of the model used in the extra model list. For -1 value, the mean model is used.
     - parallel -> if True, the computation will be processed in parallel mode
     
    return depending on level value :
        - 0 -> return a list of the best approximation of the required result
        - 1 -> return a list of the absolute minimum value, best value, absolute maximum value
        - 2 -> return a list of the list of (minimum, value, maximum) for each extra model
    """
    if not has_gm:
        raise Exception("get_results_from_smiles is not available")
    return gm_api.get_results_from_smiles(modellist, inputs, level, 
                            modelindex, parallel, progress)

def create_training_driver(
        mode='nn',
        datasource=None, 
        modelsource="", 
        modeldata=None, 
        modelname=None, 
        dataformat="",
        datarange="",
        titles=True,
        inputs=1, 
        outputs=1, 
        hidden=2, 
        activfunc="TANH", 
        statelayer=-1, 
        statenodeindex=-1, 
        order=0, 
        polytype=0, 
        classif=False,         
        callback=None, 
        keeptemp=False, 
        moduledir="", 
        trainable=True,
        forcecreate=False, 
        verbose=0, 
        **kwd):  
    # dataformat=None, existingnode=0, nosynapse=0, trainable=1, normalize=False, weights=None, disp=0, callbackfct=None, 
    
    if isinstance(dataformat, list):
        grplist = dataformat
        outputs = len(grplist[-1])
        inputs = len(grplist[-2])
    elif isinstance(dataformat, str) and dataformat:
        grplist = [[int(sub) for sub in val.split(',')] for val in dataformat.split(';')]
        outputs = len(grplist[-1])
        inputs = len(grplist[-2])
    else:
        grplist = None
        inputs = int(inputs) 
        outputs = int(outputs)
    hidden = int(hidden)
    statelayer = int(statelayer)  
    statenodeindex = int(statenodeindex)  
    order = int(order) 
    polytype = int(polytype) 
    
    if not moduledir or not os.path.exists(moduledir):
        moduledir = os.path.join(basefolder(), "modules")
        
        
        
    os.makedirs(moduledir, exist_ok=True)
    dataset = None
    if datasource:
        dataset = None
#         if isinstance(datasource, DataManager):
#             dataset = datasource
#         elif isinstance(datasource, str):
#             dataset = DataManager(datasource, dataformat=grplist)
        if isinstance(datasource, DataSource):
            dataset = datasource
        elif isinstance(datasource, str):
            dataset = DataSource(datasource, datafmt=grplist, datarange=datarange, 
                titles=titles, doload=True)
        if dataset is not None:
#            baselen = dataset.baselen
            inputs = dataset.inputCount
            outputs = dataset.outputCount
#             baselen, ninout = dataset.shape
#            baselen, ninout = dataset.datas.shape
#            inputs = ninout - 1
#            outputs = 1
    ni = inputs
    nh = hidden
    no = outputs
    netname = "nn_{0}_{1}_{2}".format(ni, nh, no)
    if modelname:
        modelname = modelname.lower()
        modelname = "{0}_{1}".format(modelname, netname)
    else:
        modelname = netname
    modulename = "lib{0}{1}".format(modelname, libExtension())
    fullmodulename = os.path.join(moduledir, modulename)
    if forcecreate or not os.path.exists(fullmodulename):
    
        driver = Driver(
                source=modelsource, 
                modeldata=modeldata, 
                modelname=modelname,
                inputs=inputs, 
                outputs=outputs, 
                hidden=hidden, 
                activfunc=activfunc, 
                statelayer=statelayer, 
                statenodeindex=statenodeindex, 
                order=order, 
                polytype=polytype,
                classif=classif, 
                trainable=trainable,
                verbose=verbose,               
                **kwd)
#         if not driver.name and not driver.mainModel.name:
#             duename = modelname if modelname else netname
#             driver.name = duename
#             driver.mainModel.name = duename    
        # ici creer le modele compile
        driver.mainModel.setInputNames(dataset.inputTitles)
        driver.mainModel.setOutputNames(dataset.outputTitles)
        driver.modelType = 3
        driver.mainModel.mark = "Model created with Mmetaphor {0}".format(metaphorversion)
        savingformat = C.SF_DLLTRAIN if trainable else  C.SF_DLL
        driver.saveModel(savingformat=savingformat, filename=fullmodulename, 
            tempdir=None, keeptemp=keeptemp, verbose=verbose, forcelib=False, 
            forcecreate=forcecreate)  #appliname="metaphor", 
    # ici charger ce modele compile
    driver = loadModule(fullmodulename)
    driver.setcallback(callback)
    if dataset is not None:
        # ici charger les donnees
        driver.loadTrainingDataFromArray(dataset.data_array)  #, baselen, ninout)  #datacount, datasize

    return driver  #, fullmodulename  #, modeldata

def get_driver(sourcefile, modelname="", smiles=""):
    """Creation of a model from a model file. This model may be as well
    a neural network model as a graphmachine model, depending upon the
    model file provided. In case of a graphmachine model, the parameter
    'smiles' is mandatory.
    
    parameters:
     - sourcefile -> file created at the end of the training process (extensions may be 'nnx', 'gmx' or 'nml' for upstream compatibility).
     - modelname -> name of the molecule you want to apply the model to optional parameter.
     - smiles -> smiles code of the molecule you want to apply the model to. Mandatory parameter.
     
    modelname and  smiles may be lists of name and smiles pairs. The lists must be of the same length.    
    
    The model has many interesting properties:
     - propertyName -> Name of the current property
     - modelName -> Name of the model
     - baselen -> Length of the training base
     - extraCount -> Number of side models included
     - inputCount -> Number of inputs
     - weights -> Current weights vector
     - paramCount -> Number of weights
     - dispersionMatrix -> Current dispersion matrix
    """
    return nn_api.get_driver(sourcefile=sourcefile, modelname=modelname, smiles=smiles)

def get_model(driver):
    """Reading a model from its driver.
    
    parameters:
     - driver -> driver to read, obtained with 'get_driver' function.

    The model has many interesting properties:
     - propertyName -> Name of the current property
     - baselen -> Length of the training base
     - extraCount -> Number of side models included
     - modelName -> Name of the model
     - inputCount -> Number of inputs
     - weights -> Current weights vector
     - paramCount -> Number of weights
     - dispersionMatrix -> Current dispersion matrix
    """
    return nn_api.get_model(driver)

def get_weights(driver):
    """Read the current weight list of a driver.
    
    parameters:
     - driver -> driver to read, obtained with 'get_driver' function.
    """
    return driver.weights

#def get_targets(driver):

def get_property(model):
    """Read the current property name of a model.
    
    parameters:
     - model -> model to read, obtained with 'get_model' function.
    """
    return nn_api.get_property(model)
    
def get_input_names(model):
    """Read the current input names of a model.
    
    parameters:
     - model -> model to read, obtained with 'get_model' function.
    """
    return nn_api.get_input_names(model)

def get_output_names(model):
    """Read the current output names of a model.
    
    parameters:
     - model -> model to read, obtained with 'get_model' function.
    """
    return nn_api.get_output_names(model)

def get_inputs(model):
    """Read the current input values of a model.
    
    parameters:
     - model -> model to read, obtained with 'get_model' function.
    """
    return nn_api.get_inputs(model)

def get_outputs(model):
    """Read the current output values of a model.
    
    parameters:
     - model -> model to read, obtained with 'get_model' function.
    """
    return nn_api.get_outputs(model)

def get_minmax_inputs(model):
    """Read the min and max input values registered in the model, if any.
    """
    return nn_api.get_minmax_inputs(model)

def get_mean_inputs(model):
    """Read the mean input values registered in the model, if any.
    """
    return nn_api.get_mean_inputs(model)

def get_minmax_outputs(model):
    return nn_api.get_minmax_outputs(model)

def get_mean_outputs(model):
    """Read the mean output values registered in the model, if any.
    """
    return nn_api.get_mean_outputs(model)


def get_result(model, inputs=None, level=0, modelindex=-1):
    """Obtain the result of model transfer function.
    
    Parameters:
     - model -> model obtained with 'get_model' function. May be a list of models.
     - inputs -> vector, dictionary or None
         - vector : vector of the input values, in the order of the inputs.
         - dictionary: input value for each input name. This dictionary may include a level item. If it exists, this value will overwrite the explicit level value.
         - None : no new input values (default).
     - level -> level of the required transfer.    
     - modelindex -> Index of the model used in the extra model list. For -1 value, the mean model is used.
    
    return depending on level value :
        - 0 -> return the best approximation of the required result
        - 1 -> return absolute minimum value, best value, absolute maximum value
        - 2 -> return list of (minimum, value, maximum) for each extra model
    """
    return nn_api.get_result(model, inputs, level, modelindex)

def get_reverse_result(model, target, inputs=None, fixedinputs=None,
        level=0 , epochs=None, modelindex=-1, callback=None, debug=0): 
    """**Only for neural network models with inputs.**
    
    Run a reverse training, modifying the inputs in order to fit the model output to the target. 
    
    Parameters:    
     - model -> model obtained with 'get_model' function.
     - target -> output value target.
     - inputs -> initial input values. It may be a vector-like, a dictionary or None:
         - vector-like : vector of the initial input values, in the order of the inputs.
         - dictionary: initial input value for each input name.
         - None : no imposed initial input values (default).
     - fixedinputs -> fixed input values.  It may be a vector-like, a dictionary or None:
         - vector-like : vector of boolean values, in the order of the inputs.
         - dictionary : each input may be fixed (or not) by its name. A missing input is considered as free.
         - None : all input values are free
     - epochs -> maximum number of optimizing computation epochs. Defaulted to 100.
     - callback -> callback function. It takes a current index as parameter. Default None
     - modelindex -> Index of the model used in the extra model list. For -1 value, the mean model is used.
     
    return tuple (newinputs, code):
     - newinputs -> the new set of input values
         - code & 1 : an unacceptable point has been ontained
         - code & 2 : accuracy limot has been reached
         - code & 4 : epochs limit has been reached
    """
    return nn_api.get_reverse_result(model, target, inputs, fixedinputs,
        level , epochs, modelindex, callback, debug)
    
if __name__ == '__main__':
    source = "/Users/jeanluc/Desktop/Reserve/Tests SAP Samir MEDROUK/Modeles fusionnes/Modele_Final_V2.NML"
#    netfile = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_Test/src/metaphor/test_monal/testFiles/Modeletest_V2.NML"
    driver = get_driver(source)
    model = get_model(driver)
    inputs = get_inputs(model)
    names = get_input_names(model)
    outnames = get_output_names(model)
    dicoval = {inname: inpt for inname, inpt in zip(names, inputs)}
    outputs = get_outputs(model)
    ppty = get_property(driver) 
    weights = get_weights(driver)
    
    print(driver)
    print()
    print("Registered values :")
    for key, value in dicoval.items():
        print ("\t{0} \t\t{1}".format(key, value))
    print()
    print("\t{0}\t\t{1}".format(ppty, outputs[0]))   
    print("weights") 
    for w in weights:
        print("\t{0}".format(w))
    
#     outlist = ["config", "iter1", "pptylist", "pptyname", "baselen", "titles"]
#     source = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_Test/src/metaphor/test_monal/testFiles/L_153.csv"
#     res = analyseTrainingDatafile(source, dataformat=[0,1,2,3,4,5], titlesfirst=True)
#     for title, val in zip(outlist, res):
#         print("{0} : {1}".format(title, val))
#     print("")
#     source = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_Test/src/metaphor/test_monal/testFiles/Base321E_chem.xlsx"
#     res = analyseTrainingDatafile(source, dataformat=[0,1,2], datarange="DATA", titlesfirst=True)
#     for title, val in zip(outlist, res):
#         print("{0} : {1}".format(title, val))
    
#     source = "/Users/jeanluc/Desktop/Tests SAP Samir MEDROUK/Modeles fusionnes/Modele_Final_V2.NML"
#     driver = get_model(source)
#     model = driver.mainModel
#     print(driver) 
#     names = driver.mainModel.inputNames
#     inputs = get_inputs(model)
#     dicoval = {inname: inpt for inname, inpt in zip(names, inputs)
#     print()
#     for key, value in dicoval.items():
#         print (key, ":", value)
#     print()
#     outs = get_outputs(model)
#     ppty = driver.propertyName
#     print("registered", ppty, outs[0])
# 
#     names = driver.mainModel.inputNames
#     outnames = driver.mainModel.outputNames
#     res = get_result(driver, dicoval)  
#     print("computed  ", ppty, res)    
#     dicoval["SDACBP2"] = 5
#     res = get_result(driver, dicoval)
#     print("computed2 ", ppty, res)
#     print()
#     dicoval2 = dicoval.copy()
#     for ind, name in enumerate(driver.mainModel.inputNames):
#         mean = driver.mainModel.inputNodes[ind].mean
#         dicoval2[name] = mean
#         print(name, mean)
#     res = get_result(driver, dicoval2) 
#     print("Computed mean {1} \t{0}".format(res, ppty))
#     
#     tg = names[0]
#     res = model.inputNodeByName(tg)
#     print (res.name)
#                             
#     from ipwidget_nn.model_widget import ModelWidget
#     w = ModelWidget(driver) 
    
    print('Done')

