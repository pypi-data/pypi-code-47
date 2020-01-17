#----------------------------------------------------------------------------
# -*- coding: UTF-8 -*-
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
#----------------------------------------------------------------------------
"""High level client interface for Metaphor server.

This module exposes a first contact with the server, and two classes, *User* and 
*Model*.
It contact the metaphor server through calls the low level interface *api_client*.
"""

from metaphor.meta_client.api_client import initiate_connection, add_user, delete_user, \
    load_model, create_model, get_function, post_function, get_model_attribute,\
    post_file, delete_models  
import numpy as np

class User():
    """User management class.
    
    Every instance of this class represent an accepted user.
    
    parameter:
    
      - user_name -> name of the user. To be checked and registered by th e server.
    """
    _user_name = ""
    _user_id = 0
    
    def __init__(self, user_name):
        result = int(add_user(user_name))
        if result > 0:
            self._user_name = user_name
            self._user_id = result
            
    def __repr__(self):
        return """Metaphor server user:
        {0}
        {1}""".format(self.user_name, self.user_id)
    
    def delete(self):
        """Unregistering the user
        """
        result = delete_user(self._user_name)
        self._user_name = ""
        self._user_id = 0
        return result
        
    @property
    def user_id(self):
        """Id of the registered user
        """
        return self._user_id

    @property
    def user_name(self):
        """Name of the registered user
        """
        return self._user_name
    

class Model():
    """Model initialization.
    
    user -> a registered user
    
    loaddata -> a dictionary with keys:
    
        -> source contains the information for the model to create.
        
            source may be:
            - XML text
            - file name containing the XML text
            - nnx of gmx file, produced by a training process
            
        -> modelname is the name to be given to the model created. This value will overwrite a model name optionaly registered within the source file.
        
        -> descriptor is a small word describing the model. For the GraphMachine models, this parameter will be the smiles code of the molecule to be modelized.
            
    modeldata -> a dictionary describing a model to create. It has the 
        highest priority to create the model.

    """
    _owner_id = 0
    _model_id = 0
    _modelname = "_"
    _description = ""
    
    def __init__(self, user, loaddata=None, modeldata=None): 
        super(Model, self).__init__()
#         self._owner_id = user.user_id
        if modeldata is not None:
            result = create_model(user.user_id, modeldata, raw=True)
        else:
            loaddata['docompile'] = 1
            result = load_model(user.user_id, loaddata, raw=True)
        self._owner_id, self._model_id, modDict = result.json()
        modDict = modDict.get('models', {})
        modDict = modDict.get(self._model_id, {})
        self._modelname = modDict.get('name', "")
        self._description = modDict.get('object', "")
    
    @classmethod
    def createFromData(cls, user, datasource="", hidden=0, dataformat="", 
            arange="", headers=True, mode="nn", forcecreate=False):
        """Model initialization from data set.
        
        user -> a registered user
        
        datasource -> source file from the client side. It will be transfered to
        the server side with the 'post_file' method.
        
        hidden -> number of hidden nodes
        
        dataformat -> data format string
        
        arange -> range of data (excel files)
        
        headers -> Heuh!!!
        
        mode -> nn or gm
        
        forcecreate -> boolean
        
        return the handle of the created model.
        """
        try:
            user_id = user.user_id
        except AttributeError:
            user_id = user
        
        source_id = post_file(user_id, datasource)
        data = {'trainable': 1,
                'datasource': source_id,
                'hidden': hidden,
                'dataformat': dataformat,
                'range': arange,
                'headers': headers,
                'mode': mode,
                'forcecreate': forcecreate,
                }
#                

        res = cls(user, None, data)
        return res
    
    def __del__(self):
        if self._model_id and self._owner_id:
            #data = {'delete': self._model_id}
            res = delete_models(self._owner_id, self._model_id)
    
    @property
    def paramCount(self):
        """Retrieve the size of the parameter vector.
        """
        return int(get_function(self._owner_id, self._model_id, 'paramCount'))
    
    @property
    def dataCount(self):
        """Retrieve the size of the training database.
        """
        return int(get_function(self._owner_id, self._model_id, 'dataCount'))
    
    def newWeights(self, stddev=0.3, bias0=True, doset=False):
        """Generate a new parameter vector.
        
        Parameters:
        
        - stddev -> standard deviation of the random distribution generated. Default 0.3
        - bias0 -> set the linear parameters to 0. Default True
        - doset -> if True, set the model weights to the generated vector
        """
        data = {'stddev': stddev, 'bias0': bias0}
        result = get_function(self._owner_id, self._model_id, 'newWeights', data=data)
        if doset:
            self.weights = result
        return result
    
    def trainigData(self):
        """Retrieve the training data set.
        """
        data = {'prefix': None}
        return get_function(self._owner_id, self._model_id, 'getTrainingData', data=data)
    
#    def transfer(self, inputs=None, indexmove=-1, indexlist=None, weights=None):
    def transfer(self, inputs=None, index=-1, indexlist=None, weights=None):
        """Command a transfer through the model. 
        
        Parameters:
        
        - inputs -> inputs to use. If None, last used inputs are used. Only if index is < 0.
        - index -> if indexlist is None, index of the inputs in the training data base, else index of the input vector to be tested with different values.
        - indexlist -> data to use in the inputs in the index position
        - weights -> the parameter set to use. If None, the current weights is used.
        
        Return result of the transfer, i.e. a float or a list of float
        """
        inputs = inputs if inputs is None else [float(val) for val in inputs]
        indexlist = indexlist if indexlist is None else [float(val) for val in indexlist]
        if indexlist is None:
            data = {'inputs': inputs,
                    'index': index,
                    'weights': weights}
        else:
            data = {'inputs': inputs,
                    'indexmove': index,
                    'weights': weights,
                    'indexlist': indexlist,}
        res = post_function(self._owner_id, self._model_id, 'transfer', data)
        if isinstance(res, list):
            res = [float(val) for val in res]
        return res

    def train(self, 
              startWeights=None, 
              epochs=0, 
              trainstyle=0,
              callback=None):
        """Launch a training job.
        
        Parameters:
        
        - startWeights -> parameter vector to use at the beginning.
        - epochs -> maximum number of epochs of the training job.
        - trainstyle -> unused. Kepp the default
        - callback -> unused. Kepp the default
        """
        data = {
            'startWeights': startWeights,
            'epochs': epochs,
            'trainstyle': trainstyle,
            'callback': 'debug',
            }
        res = post_function(self._owner_id, self._model_id, 'train', data)
        return res
    
    def reverse_train(self, target, inputs=None, freeinputs=None, 
            epochs=None, fullres=False, callback=None, debug=0):
        """Launch a reverse training job. This will compute an input set for 
        which the model gives an output close to a target value. Available only 
        for single models with non zero input number.
        
        Parameters:
        
        - target -> targeted output value.
        - imputs -> starting input values
        - freeinputs -> list of the free inputs (names or indexes in input list).
        - epochs -> maximum number of epochs of the reverse training job.
        - callback -> unused. Kepp the default
        - debug -> unused. Keep the default
        """
#         print("initial inputs", inputs)
#         print("freeinputs", freeinputs)
#         if epochs is None or epochs <= 0:
#             epochs = 100
#         fullres = True
        withhistory = True
        data = {'outputtarget': float(target),
                'inputs': [float(val) for val in inputs],
                'freeinputs': [int(val) for val in freeinputs],
                'epochs': epochs if epochs else 100,
                'withhistory': withhistory,
                'fullres': fullres,
                }
        res = post_function(self._owner_id, self._model_id, 'reverse_train', 
                            data)
        try:
            newinputs, epochs, ender, history = res
        except:
            newinputs, ender = res
        if debug:
            print(res)
        result = self.transfer(newinputs)
        if fullres:
            return result, newinputs, epochs, ender, history
        else:
            return result#, newinputs
   
    def inputIndexFromName(self, targetName, inNames=None):
        """Retrieve the index of a given target input name.
        
        Parameters:
        
        - targetName -> input name to retrieve.
        - inNames -> set of names to check. If None, model input names are used.
        """
        if inNames is None:
            inNames = self.inputNames()
        try:
            return inNames.index(targetName)
        except Exception as err:
            return -1
    
    def inputNames(self):
        """Retrive the list of input names
        """
        return get_function(self._owner_id, self._model_id, 'inputNames')
    
    def outputNames(self):
        """Retrieve the output names.
        """
        return get_function(self._owner_id, self._model_id, 'outputNames') 
    
    def inputs(self, intype=0, index=-1): # intype = 0: registedred inputs, 1: mean inputs, 2: inputs interval
        """Retrieve the input informations.
        
        Parameters:
        
        - intype -> returned information type:
            - 0 -> return input values
            - 1 -> return mean input value inside the allowed input interval.
            - 2 -> return the allowed input interval

        - index -> if < 0, return input info vector. Else return the indexed input info
        """
        if intype == 2:
            data = {'attributes': 'inputRanges'}
            dicores = get_model_attribute(self._owner_id, self._model_id, data)
            res = dicores.get('inputRanges', [])
            res = [(float(mini), float(maxi)) for mini, maxi in res]
            if index >= 0:
                res = res[index]    
            return res    
        if intype == 1:
            data = {'attributes': 'meanInputs'}
            dicores = get_model_attribute(self._owner_id, self._model_id, data)
            res = dicores.get('meanInputs', [])
            res = [float(val) for val in res]
            if index >= 0:
                res = res[index]    
            return res
        res = get_function(self._owner_id, self._model_id, 'inputs')
        if len(res): 
            if not isinstance(res[0], list):
                res = [float(val) for val in res]
            else:
                res = [[float(sub) for sub in val] for val in res]
        if index >= 0:
            res = res[index]    
        return res
    
    def outputs(self, outtype=0): # outtype = 0: registedred outputs, 1: mean inputs, 2: outputs interval
        """Retrieve the outputs informations.
        
        Parameters:
        
        - outtype -> returned information type:
            - 0 -> return output values
            - 1 -> return mean output value inside the allowed output interval.
            - 2 -> return the allowed output interval

        - index -> if < 0, return output info vector. Else return the indexed output info
        """
        if outtype == 2:
            data = {'attributes': 'outputRanges'}
            dicores = get_model_attribute(self._owner_id, self._model_id, data)
            res = dicores.get('outputRanges', [])
            #for (min, max) in res:
            res = [(float(mini), float(maxi)) for mini, maxi in res]    
            return res    
        if outtype == 1:
            data = {'attributes': 'meanOutputs'}
            dicores = get_model_attribute(self._owner_id, self._model_id, data)
            res = dicores.get('meanOutputs', [])
            res = [float(val) for val in res]
            return res
        return get_function(self._owner_id, self._model_id, 'outputs')
    
    @property
    def inputNorm(self):
        """Retrieve the input normalization values.
        """
        return get_function(self._owner_id, self._model_id, 'inputNorm')
    
    @property
    def outputNorm(self):
        """Retrieve the output normalization values.
        """
        return get_function(self._owner_id, self._model_id, 'outputNorm')
    
    def targets(self):
        """Retrieve the training target values.
        """
        res = get_function(self._owner_id, self._model_id, 'targets')
        return res
    
    @property
    def propertyName(self):
        res = self.outputNames()
        return res[0]
    
    @property
    def modelName(self):
        return self._modelname
    @modelName.setter
    def modelName(self, value):
        self._modelname = value

    @property
    def model_id(self):
        return self._model_id

    @property
    def owner_id(self):
        return self._owner_id
    
    @property
    def description(self):
        return self._description
    
    @property
    def weights(self):
        data = {'prefix': None}
        return get_function(self._owner_id, self._model_id, 'getWeights', data=data)
    @weights.setter
    def weights(self, value):
        data = {'weights': value,
                'prefix': None}
        post_function(self._owner_id, self._model_id, 'setWeights', data=data)

#==============================================================================#
def _connectTest(username='jeanluc'):
    
    userjl = User(username)
    print(repr(userjl))
    
    return userjl

def _runNMLTest(userjl):
    modelNML_0 = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_api/src"+\
    "/testfiles/Tests SAP Samir MEDROUK/Modeles fusionnes/Modele_Final_V2.NML"
    data = {'source': modelNML_0,
            'docompile': 1,
#            'modelname': "TestModel"
        }
    mymodel = Model(userjl, data) 
    inpts = mymodel.inputs()
    inptnas = mymodel.inputNames()
    intervals = mymodel.inputs(2)

    for nm, val in zip(inpts, inptnas):
        print(val, "\t", nm)
    
    print('mymodel :')
#    print('\tproperty -> {0}'.format(mymodel.propertyName))
    print("\towner_id -> {0}".format(mymodel.owner_id))
    print("\tmodel_id -> {0}".format(mymodel.model_id))
#    print("\tmodelname -> {0}".format(mymodel.modelName))
    print("\tdescription -> {0}".format(mymodel.description))
    print("inputs:", inpts)
    result = mymodel.transfer(inpts)
    print("output:", result)
    
    result = mymodel.inputs(2)
    print("input ranges:", result)

    means = [(val[0] + val[1])/2 for val in result]
    print("mean inputs:", means)
    result = mymodel.transfer(means)
    print("output with mean inputs:", result)
    
    outInterval = mymodel.outputs(2)[0]
    print("output range", outInterval)
    
#     freeinputs = [0 for _ in range(len(inpts))]
#     freeinputs[9] = 1
#     freeinputs[10] = 1
    freeinputs = [9, 10]
    target = float(result) + 0.02
    inputs = means
    
    newresult, newinputs, *wds = mymodel.reverse_train(target, inputs, freeinputs, 
            epochs=100, callback=None, debug=0, fullres=True)
    oldinputs = mymodel.inputs()
    print("target", target)
    print("result", newresult)
    print("new inputs", newinputs)
    
def _runNMLcurve(userjl): 
    import os   
    modelNML_0 = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_api/src"+\
    "/testfiles/Tests SAP Samir MEDROUK/Modeles fusionnes/Modele_Final_V2.NML"
    data = {'source': modelNML_0,
            'docompile': 1,
#            'modelname': "TestModel"
        }
    mymodel = Model(userjl, data) 
    inpts = mymodel.inputs()
    inptnas = mymodel.inputNames()
    intervals = mymodel.inputs(2)
    inranges = mymodel.inputs(2)
#     print("input ranges:", result)

    means = [(val[0] + val[1])/2 for val in inranges]
    print("mean inputs:", means)
 #   names = mymodel.inputNames()
    do_plot(mymodel, means, inptnas[9], 'toto')

def do_plot(model, inputs, inputname, outputname): 
    inputindex = model.inputNames().index(inputname)
    mini, maxi = model.inputs(2, inputindex)
    Xlist = np.linspace(mini, maxi, 201) 
    result = model.transfer(inputs, index=inputindex, indexlist=Xlist)
    #plt.plot(Xlist, result)
    print(inputname, result)
   

def _runCreateTest(userjl):
    source = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_api/src/testfiles/L_153.csv"
    modeldata = {
        'datasource': source,
#        'modelname': 'myTrainableModel',
        'inputs': '5',
        'hidden': '5',
        'trainable': True,
        'forcecreate': True,
    }
    testmodel = Model(userjl, modeldata=modeldata) 
    print("modelName:", testmodel.modelName)
    print("description:", testmodel.description)

def _runCreateTraining(userjl):
#     delete_models(userjl.user_id, data={'delete': "*"})
    
#     WW22 = np.zeros((22,))
    WW22 = [0 for _ in range(22)]
    WW22[0] = 0.039843524921
    WW22[1] = -0.11974612107
    WW22[2] = -0.048612387027
    WW22[3] = -0.19084323523
    WW22[4] = -0.084070986799
    WW22[5] = -0.03008236605
    WW22[6] = 0.069560996908
    WW22[7] = 0.11159221823
    WW22[8] = 0.047867121706
    WW22[9] = 0.10994423754
    WW22[10] = -0.094399533507
    WW22[11] = -0.021777191667
    WW22[12] = 0.080970843388
    WW22[13] = -0.0061677630808
    WW22[14] = 0.067246044709
    WW22[15] = -0.0019394849107
    WW22[16] = 7.11023083E-05
    WW22[17] = 0.0015981840668
    WW22[18] = 0.1199492128
    WW22[19] = 0.097958760835
    WW22[20] = 0.027484232802
    WW22[21] = 0.16873545622
    
#     filename0 = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_Test/src/metaphor/test_monal/testFiles/fullalea.csv"
    filename1 = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_Test/src/metaphor/test_monal/testFiles/L_153.csv"
    filename2 = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_Test/src/metaphor/test_monal/testFiles/l_153.xlsx"
    filename3 = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_Test/src/metaphor/test_monal/testFiles/l_153.xls"

#     range
#     headers
#     datasource = filename1
    arange = 'DATA'
    hidden = 5
    dataformat = "0,1,2,3,4;5"
    forcecreate = True
    
#     model1 = Model.createFromData(userjl, datasource=filename1, 
#         hidden=hidden, dataformat=dataformat, arange=arange, 
#         forcecreate=forcecreate)
#     print("model_id", model1.model_id)
#     print('inputNames', model1.inputNames())
#     print('outputNames', model1.outputNames())
#     print('targets', model1.targets())
#     
#     model2 = Model.createFromData(userjl, datasource=filename2, 
#         hidden=hidden, dataformat=dataformat, arange=arange, 
#         forcecreate=forcecreate)
#     print("model_id", model2.model_id)
#     print('inputNames', model2.inputNames())
#     print('outputNames', model2.outputNames())
#     print('targets', model2.targets())
    
    model3 = Model.createFromData(userjl, datasource=filename3, 
        hidden=hidden, dataformat=dataformat, arange=arange, 
        forcecreate=forcecreate)
    print("model_id", model3.model_id)
    print('inputNames', model3.inputNames())
    print('outputNames', model3.outputNames())
    targets = model3.targets()
#    print('targets', model3.targets())
    traindata = model3.trainigData()
    print('inputdata[0]', traindata[0])
    print('inputdata[-1]', traindata[-1])
    print('dim', model3.paramCount)
    print(model3.weights)
    nw = model3.newWeights(doset=True)
#    model3.weights = WW22
    print(model3.weights)
    print('inputNorm', model3.inputNorm)
    print('outputNorm', model3.outputNorm)
    
    print()
#    print("inputs(0)", model3.inputs(index = 0))
    res = model3.transfer([28.0, 11.0, 18.0, 79.0, 17.0])
    print('transfer \t{}'.format(res))
    print()
    nn = model3.dataCount
    print('before training')
    for ind, tg in enumerate(targets):
        res = model3.transfer(index=ind)
        print('transfer {0}:\t{1}  {2}'.format(ind, tg, res))
    
    newweights = model3.train(epochs=1000, callback='debug')
    print('after training')
    for ind, tg in enumerate(targets):
        res = model3.transfer(index=ind)
        print('transfer {0}:\t{1}  {2}'.format(ind, tg, res))
        
    
    print(newweights)
    
#     del model1
#     del model2
    del model3
    

if __name__ == "__main__":
    
    server = 'localhost'
    port = 5005
    APIVer = "1.0"
    
    result = initiate_connection(server=server, port=port)
    print(result)
    userjl = _connectTest()
    _runNMLcurve(userjl)
#    _runNMLTest(userjl)
#    _runCreateTest(userjl)
#    _runCreateTraining(userjl)
    print("Done")
    
        