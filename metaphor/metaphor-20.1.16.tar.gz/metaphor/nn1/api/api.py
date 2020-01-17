# -*- coding: ISO-8859-1 -*-
'''
Created on 13 dÃ©c. 2018

@author: jeanluc
'''

import os, types
from functools import reduce
import numpy as np
import concurrent.futures as cf

try:
    from ...chem_gm.api import _api_service as gmserv
except:
    gmserv = None
from metaphor.nntoolbox.filetoolbox import getDictFromGmx
from metaphor.nntoolbox.utils import basefolder
from metaphor.monal import monalconst as C
from metaphor.monal.monalrecords import ModelData
from metaphor.monal.driver import Driver, DriverLib  #optim_leastsq,
from metaphor.monal.model import Model
from metaphor.monal.Property import IndexedProperty
# from ...nn1.api import _api_service as nn1serv

keeptemp="USE$$$"  # mettre à ""

def do_save_model(filename="", savingformat=C.SF_XML,
            savedir=None, tempdir=None, package="", modeltemplate="m%d_", 
            keeptemp=keeptemp, verbose=0, compiler="", forcelib=False, 
            forcecreate=False):
    Driver.saveModel(filename=filename, savingformat=savingformat,
            savedir=savedir, tempdir=tempdir, package=package, 
            modeltemplate=modeltemplate, keeptemp=keeptemp, verbose=verbose, 
            compiler=compiler, forcelib=forcelib, forcecreate=forcecreate)

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
     - paramCount -> Number of weights
     - weights -> Current weights vector
     - dispersionMatrix -> Current dispersion matrix
    """
    return driver.mainModel

def get_driver(source="", modelname="", smiles="", docompile=False, **kwd):  #, name_smiles_list=[]):
    """Creation of a model driver from a model file. This driver may be as well
    a neural network driver as a graphmachine driver, depending upon the
    source provided. In case of a graphmachine driver, the parameter
    'smiles' is mandatory.
    
    parameters:
     - source -> file created at the end of the training process (extensions may be 'nnx', 'gmx' or 'nml' for upstream compatibility).
     - modelname -> name of the molecule you want to apply the model to optional parameter.
     - smiles -> smiles code of the molecule you want to apply the model to. Mandatory parameter.
     - kwd -> garbage dictionary for unused parameters.
     
    modelname and  smiles may be lists of name and smiles pairs. The lists must be of the same length.    
    
    The model has many interesting properties:
     - modelName -> Name of the model
     - inputCount -> Number of inputs
     - weights -> Current weights vector
     - paramCount -> Number of weights
     - compile -> ask for model compilation if possible.
     
    """
    if isinstance(smiles, list):
        return [get_model(source,  mname, smile) for mname, smile in zip(modelname, smiles)]
#     if name_smiles_list is not None and len(name_smiles_list):
#         return [get_model(source, modelname, smiles) for modelname, smiles in name_smiles_list]
    dico = None
    model = None
    modeldata = None
    innames = []
    outames = []
    if smiles:
        if gmserv is not None:
            model = gmserv.createSpecialModel(source, modelname, smiles)
        return model
    else:
        try:
            source = source if source else kwd.get('sourcefile', "")
            model = Driver(source)
            if model:
                if not model.name:
                    model.name = modelname
                if not model.name and os.path.exists(source):
                    model.name = os.path.splitext(os.path.basename(source))[0]
                # return model
        except Exception as err:
            err = err
            model = None
        if not model:
            dico = getDictFromGmx(source)
            if "xml" in dico.keys():
                xml = dico["xml"]
                model = Driver(xml)
            elif "modeldata" in dico.keys():
                modeldata = dico['modeldata']
            elif "model" in dico.keys():
                modeldict = dico['model']
                innames = modeldict["inputnames"].split(',')
                ni = len(innames)
                outames = modeldict["outputname"].split(',')
                no = len(outames)
                nh = int(modeldict["hidden"])
                id = modelname
                modeldata = ModelData(input=ni, output=no, hidden=nh, name=id)
            if modeldata:
                model = Driver(modeldata=modeldata)
                model.loadFromDict(dico)
    if model and docompile and not isinstance(model, DriverLib):
        model.modelType = 3
        savedir = os.path.join(basefolder(), "modules")
        os.makedirs(savedir, exist_ok=True)
        modulename = model.saveModel(savedir=savedir, trainable=False,
            savingformat=C.SF_DLLTRAIN, keeptemp=keeptemp)
        fullmodulename = os.path.join(savedir, modulename)
        model = DriverLib(fullmodulename)
    
    return model

def get_func_prefix(driver, root_func_name, prefix, schema='dm'):
    """retrieve in driver a function name with a prefix and a root name
    schema specify the research schema:
     'm' -> model
     'd' -> driver
    """
#     def relay(result):
#         def relaymethod():
#             return result
#         return relaymethod
    if isinstance(prefix, list):
        result = None
        for prefixitem in prefix:
            res = get_func_prefix(driver, root_func_name, prefixitem)
            if res is not None:
                if isinstance(res, (types.FunctionType, types.MethodType)):
                    result = res
                elif isinstance(res, IndexedProperty):
#                     print(res[0])
                    result = (lambda x: lambda: x)(res)  #relay(res)
                else:
                    result = (lambda x: lambda: x)(res)  #relay(res)
                break
        return result
    funcname = root_func_name if prefix is None else \
        "{0}{1}".format(prefix, root_func_name)
    result = None
    for val in schema:
        if val == 'm':
            try:
                result = getattr(driver.mainModel, funcname) 
                break
            except AttributeError:
                pass
        elif val == 'd':
            try:
                result = getattr(driver, funcname)
                break
            except AttributeError:
                pass
        else:
            raise KeyError("'{}' is unknown in function retrieving".format(val))
      
    return result

def get_func_value(driver, root_func_name, schema='dm', prefix=['', 'get', 'get'], **kwds):
    funct = get_func_prefix(driver, root_func_name, prefix, schema=schema)
    if funct:
        try:
            res = funct(**kwds)
#             if isinstance(res, IndexedProperty):
#                 res = list(res)
            return res
        except Exception as err:
            return err
    return None

def set_func_value(driver, root_func_name, schema='dm', prefix=['', 'set', 'set_', 'add', 'add_'], **kwds):
#    is_long = kwds.get("is_long", False)  
#False if not "is_long" in kwds else kwds["is_long"]
#    prefix = "" if no_prefix else ['set', 'set_', 'add', 'add_', '']
    funct = get_func_prefix(driver, root_func_name, prefix, schema=schema)
    if funct:
        try:
            return funct(**kwds)
        except Exception as err:
            return err
    return None

def get_attribute(driver, attribute, generator2list=True):
    try:
        if hasattr(driver.mainModel, attribute):
            res = getattr(driver.mainModel, attribute)
        elif hasattr(driver, attribute):
            res = getattr(driver, attribute)

        elif attribute == 'meanInputs':
            return [node.mean for node in driver.mainModel.inputNodes]
        elif attribute == 'inputRanges':
            return [node.interval for node in driver.mainModel.inputNodes]

        elif attribute == 'meanPutputs':
            return [node.mean for node in driver.mainModel.outputNodes]
        elif attribute == 'outputRanges':
            return [node.interval for node in driver.mainModel.outputNodes]

        else:
            return "unknown {}".format(attribute) 
        if generator2list and isinstance(res, IndexedProperty):
            res = list(res)
        return res
    except Exception as err:
        return err

def set_attribute(driver, attribute, value, test= False):
    try:
        target = driver.mainModel if hasattr(driver.mainModel, attribute) else driver
        try:
            res = setattr(target, attribute, value)
            if test:
                res = getattr(target, attribute) == value
        except AttributeError:
            res = "unknown {}".format(attribute) 
        return res
    except Exception as err:
        return err

def get_weights(driver):
    """Read the current weight list of a driver.
    
    parameters:
     - driver -> driver to read, obtained with 'get_driver' function.
    """
    return driver.weights

def get_property(driver):
    """Read the current property name of a driver.
    
    parameters:
     - driver -> driver to read, obtained with 'get_driver' function.
    """
    return driver.propertyName

def get_input_names(model):
    """Read the current input names of a model.
    
    parameters:
     - model -> model to read, obtained with 'get_model' function.
    """
    return model.inputNames

def get_inputs(model):
    """Read the current input values of a model.
    
    parameters:
     - model -> model to read, obtained with 'get_model' function.
    """
    return model.inputs  #[value for value in model.inputs]

def get_input_norms(model):
    return model.inputNorm

def get_output_names(model):
    """Read the current output names of a model.
    
    parameters:
     - model -> model to read, obtained with 'get_model' function.
    """
    return model.outputNames

def get_outputs(model):
    """Read the current output values of a model.
    
    parameters:
     - model -> model to read, obtained with 'get_model' function.
    """
    try:
        return [value for value in model.outputs]
    except AttributeError:
        return model.outputs
        

def get_minmax_inputs(model):
    """Read the min and max input values registered in the model, if any.
    """
    try:
        return [(node.minimum, node.maximum) for node in model.inputNodes]
    except:
        return None

def get_mean_inputs(model):
    """Read the mean input values registered in the model, if any.
    """
    try:
        return [node.mean for node in model.inputNodes]
    except AttributeError:
        try:
            return [node.mean for node in model.mainModel.inputNodes]
        except AttributeError:
            try:
                ranges = model.inputRanges
                return [(val[0] + val[1])/2 for val in ranges]
            except:
                return None

def get_minmax_outputs(model):
    try:
        return [(node.minimum, node.maximum) for node in model.outputNodes]
    except:
        return None

def get_mean_outputs(model):
    """Read the mean output values registered in the model, if any.
    """
    try:
        return [node.mean for node in model.outputNodes]
    except:
        return None

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
    if isinstance(model, (list, tuple)):
        ## mettre en parallel ?!?
        return [get_result(mod, inputs, level, modelindex) for mod in model]
    if isinstance(inputs, dict):
        if 'level' in inputs:
            # On ne supprime pas la cle 'level' du dictionnaire.
            level = inputs['level']
        if hasattr(model, 'inputNames'):
            namegen = model.inputNames
        else:
            namegen = model.mainModel.inputNames
        inputs = [inputs[inname] for inname in namegen]    
    if isinstance(model, Model):
        res = model(inputs, computelevel=level)
        return res
    if isinstance(inputs, list):
        inputs = np.asarray(inputs)
    res = model.transfer(inputs)
    
    res = model.transferEx(inputs, withCI=2, modelindex=modelindex)
    outs = [float(val) for val in res[0]]
    CIps = [float(val) for val in res[1]]
    CIms = [float(val) for val in res[2]]
    levs = [float(val) for val in res[3]]
    if modelindex == -1:
        outmean = reduce(lambda x, y: x + y, outs) / float(len(outs))
        try:
            minCIms = min(CIms)
            maxCIps = max(CIps)
        except:
            minCIms = maxCIps = None
    else:
        outmean = np.squeeze(outs)
        minCIms = np.squeeze(CIms)
        maxCIps = np.squeeze(CIps)
    model.lastoutput = outmean
    if not level:
        return outmean
    if level == 1:
        return minCIms, outmean, maxCIps

    return outs, CIms, CIps, levs

def get_reverse_result(model, target, inputs=None, freeinputs='all',
        level=0 , epochs=None, modelindex=-1, callback=None, debug=0,
        fullres=False): 
    """**Only for neural network models with inputs.**
    
    Run a reverse training, modifying the inputs in order to fit the model output to the target. 
    
    Parameters:    
     - model -> model obtained with 'get_model' function.
     - target -> output value target.
     - inputs -> initial input values. It may be a vector-like, a dictionary or None:
         - vector-like : vector of the initial input values, in the order of the inputs.
         - dictionary: initial input value for each input name.
         - None : no imposed initial input values (default).
     - freeinputs -> free input values.  It may be a vector-like, a dictionary or None:
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
    if epochs is None or epochs <= 0:
        epochs = 100
    newinputs, epochs, ender, history = model.reverse_train(target, inputs, 
        freeinputs=freeinputs, epochs=epochs, modelindex=modelindex, 
        callback=callback, debug=debug, withhistory=True)
    res = get_result(model, newinputs, level, modelindex)
    if fullres:
        return res, newinputs, epochs, ender, history
    return res

if __name__ == '__main__':
#    source = "/Users/jeanluc/Desktop/Tests SAP Samir MEDROUK/Modeles fusionnes/Modele_Final_V2.NML"
    inidir = "/Users/jeanluc/Desktop/Reserve/Tests SAP Samir MEDROUK"
    #destlibname = os.path.join(inidir, "_.so")
    tempdir = os.path.join(inidir, "$$$")
    source = os.path.join(inidir, "Modeles fusionnes", "Modele_Final.NML")
    model = get_driver(source, docompile=True)
    inpts = list(model.inputs)
    st = repr(model)
    
    print(st) 

    try:
        names = model.inputNames
        outnames = model.outputNames
    except AttributeError:
        names = model.mainModel.inputNames
        outnames = model.mainModel.outputNames
    inputs = get_inputs(model)
    inputnorms = get_input_norms(model)
    inputmeans = get_mean_inputs(model)
    #[sum(val)/2 for val in intervals]
    
    dicoval = {inname: inpt for inname, inpt in zip(names, inputmeans)}
    print()
    for key, value in dicoval.items():
        print (key, ":", value)
    print()
    outs = get_outputs(model)
    ppty = model.propertyName
    print("mean", ppty, outs[0])

    res = get_result(model, dicoval)  
    print("computed ", ppty, res)
    target = res+0.02
#    freeinputs = ["PeolpleCBP1", "PeolpleCBP2"]
    freeinputs = ["PeolpleCBP1", 10]
#    freeinputs = 'all'
    res = get_reverse_result(model, target, dicoval, freeinputs=None, 
        fullres=True)#, debug=C.debugFromStr('all'))
    print("target", target)
    print("result", res[0])
    print("epochs ", res[2])
    ender = res[3]
    print("ender ", C.END_TRAINING_DICT[ender])
    print("cost history :")
    for ind, val in enumerate(res[4]):
        print("\t{0:6.3E}".format(val))
        if ind >= res[2]:
            break
    print()
    curinputs = model.inputs
    for (key, val), inp in zip(res[1].items(), curinputs):
        print(key, "\t", val, "\t", inp)

#     dicoval2 = dicoval.copy()
#     for ind, name in enumerate(model.inputNames):
#         mean = model.inputNodes[ind].mean
#         dicoval2[name] = mean
#         print(name, mean)
#     res = get_result(driver, dicoval2) 
#     print("Computed mean {1} \t{0}".format(res, ppty))
#     
#     tg = names[0]
#     res = model.inputNodeByName(tg)
#     print (res.name)
                            
    
#     for ind in range(len(names)):
#         dicoval2 = dicoval.copy()
#         dicoval2[names[ind]] = 5
#         res = get_result(driver, dicoval2)  #, modelindex=modelindex)
#         print("Computed {1} \t{0}".format(res, ppty))
    

#     
    
#     print("weights :")
#     for ind, ww in enumerate(driver.weights) :
#         print("\t {0}\t{1}".format(ind, ww))
    
    #print("weights :", driver.weights)
    
    
#     from ipwidget_nn.model_widget import ModelWidget
# 
# 
#     w = ModelWidget(driver)  #, modelindex=modelindex)
    
    #     source = '/Users/jeanluc/Documents/Workspace/Monal_Test/src/testFiles/GM_B13C81Acetophenones_50T_0I_150E_10S_SEED1947_5N.nnx'
#     modellist = [(source, "2,2-dichloroacetophenone0" , "c(cc1)cc[c:1]1C(=O)C(Cl)Cl", None),
# (source, "2,2-dichloroacetophenone1", "c(c[c:1]1)ccc1C(=O)C(Cl)Cl", None),
# (source, "2,2-dichloroacetophenone2", "c([c:1]c1)ccc1C(=O)C(Cl)Cl", None),
# (source, "2,2-dichloroacetophenone3", "[c:1](cc1)ccc1C(=O)C(Cl)Cl", None),
# (source, "4'-butoxyacetophenone0", "CCCCO[c:1]1ccc(cc1)C(=O)C", None),
# (source, "4'-butoxyacetophenone1", "CCCCOc1ccc(c[c:1]1)C(=O)C", None),
# (source, "4'-butoxyacetophenone2", "CCCCOc1ccc([c:1]c1)C(=O)C", None),
# (source, "4'-butoxyacetophenone3", "CCCCOc1cc[c:1](cc1)C(=O)C", None),
# (source, "2-bromoacetophenone0", "BrCC(=O)[c:1]1ccccc1", None),
# (source, "2-bromoacetophenone1", "BrCC(=O)c1cccc[c:1]1", None),
# (source, "2-bromoacetophenone2", "BrCC(=O)c1ccc[c:1]c1", None),
# (source, "2-bromoacetophenone3", "BrCC(=O)c1cc[c:1]cc1", None),]
#     
#     res = get_results_from_smiles(modellist, None, level=1, modelindex=-1, parallel=True)
#     for mname, val in res:
#         st = "{0} : \t{1}".format(mname, str(val))
#         print(st)
# #        print(mname, "->", val)
    
    
    
    
    
#     inputs = [28, 11, 18, 79, 17]
#     model = get_model(source)
#     model.reprdepth = 1
#     print(repr(model))
#     dico = {
#         'X1': 28.0,
#         'X2': 11.0,
#         'X3': 18.0,
#         'X4': 79.0,
#         'X5': 17.0,
#     }
#     modelindex = 1
#     res = get_result(model, dico, modelindex=modelindex)
#     print(model.lastoutput)
#     print(res)
#     print()
#     target = 25
#     print("target", target)
#     fixed = None
# #     fixed = [1,1,0,1,1]
#     epochs = None
#     res = get_reverse_result(model, target, freeinputs=fixed, epochs=epochs, modelindex=modelindex, debug=1)
#     newinputs = get_inputs(model)
#     print(newinputs)
#     print("result", res)
#     print("residu", res - target)

# 2,2,3-trimethylbutane    CC(C)(C)C(C)C

#     sourcegm = "/Users/jeanluc/Documents/Workspace/Monal_Test/src/testFiles/GM_B13C81Acetophenones_50T_0I_150E_10S_SEED1947_5N.nnx"
#     modelname = "acetophenone0"
#     smile = "c(cc1)cc[c:1]1C(=O)C"
#     pair0 = ("acetophenone0", "[c:1](cc1)ccc1C(=O)C")
#     pair1 = ("acetophenone1", "c(cc1)cc[c:1]1C(=O)C")
#     pair2 = ("2,2,3-trimet
#     modelgms = get_model(sourcegm, name_smiles_list=(pair0, pair1))
#     valuegms = get_result(modelgms, level=1)
#     for val in valuegms:
#         print("gm value", val)
#     print("gm value", valuegm)
#     model = get_model(source, 'unknown')
#     print(model.name, model.propertyName)
#
# # call with level 0
#     print("mean best value:")
#     value = get_result(model, inputs)
#
#     print("\t{0:9.6f}".format(value))
#     print()
#     titles = ["min", "value", "max"]
#     print("\t".join(titles))
#
# # call with level 1
#     mini, val, maxi = get_result(model, inputs, level=1)
#
#     values = ["{0:6.3f}".format(val) for val in [mini, val, maxi]]
#     print("\t".join(values))
#     print()
#     print("available results")
#     titles = ["value", "max", "min", "leverage"]
#     print("\t".join(titles))
#
# # call with level 2
#     outs, CIps, CIms, levs = get_result(model, inputs, level=2)
#     for out, CIp, CIm, lev in zip(outs, CIps, CIms, levs):
#         res = ["{0:6.3f}".format(val) for val in [out, CIp, CIm, lev]]
#         st = "\t".join(res)
#         print(st)
    print('Done')

