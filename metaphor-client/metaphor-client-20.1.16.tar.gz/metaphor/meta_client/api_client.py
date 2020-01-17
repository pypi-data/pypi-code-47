# -*- coding: UTF-8 -*-
#----------------------------------------------------------------------------
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

"""Low level client interface for Metaphor server.

This module expose procedures that call directly the metaphor server through the RESTful interface implemented with Sanic.
"""

import requests

from metaphor.meta_client import client_toolbox as ct

def initiate_connection(server="0.0.0.0", port=5005, application='metaphor', 
        APIver=ct.APIversion):
    """Initiate metaphor client interface routes and establish contact.
    
    parameters:
    
    - server -> IP address or name of the server machine. default "0.0.0.0"
    - port -> Number of port. default 5005 
    - application -> Application name. default 'metaphor' 
    - APIver -> Version of the interface. default APIversion
    
    return the server welcome message if success, otherwise an error message.
    """
    ct.initiate_routes(server, port, application, APIver)
    return contact()

def contact():  #application=ct.application
    """Establish a first contact with the metaphor server. 
    It returns a welcome message.
    
    parameters:
    
    - application (optional) -> the application name get in contact with. Defaul **metaphor**
    """
    url = ct.welcome_url
    r = requests.get(url)
    return r.text

def check_user(username="", getID=False): 
#   .../metaphor/vx.x/user/<user_name> 
    """Check the user situation.
    
    return :
    
        ================  =========  ==========================================
        user registered   no         yes
        ================  =========  ==========================================
        getID True        -1         ID 
        getID False       warning    3-tuple : name, ID, belongings dictionary
        ================  =========  ==========================================    
    """
    url = ct.user_url.format(username)
    r = requests.get(url)  
    try:
        res = r.json()
        if not getID:
            return res
        elif res[0] == username:
            return res[1]#int(res[1]['id'])
        else:
            return -1
    except:
        return r.content

def get_user_name(user_ID):
#  .../metaphor/vx.x/user/<user_ID>
    """Retrieve user name.
    
    parameter:
    
    - user_ID -> ID to find
    
    return user name if found, else empty string.
    """
    url = ct.user_url.format(user_ID)
    r = requests.get(url)
    res = r.json()
    return res

def get_users():
#  .../metaphor/vx.x/users
    """Retrieve registered user dictionary.
    
    - keys -> user ID(s)
    - values -> user names
    """
    url = ct.users_url
    r = requests.get(url)
    try:
        return r.json()
    except:
        return r.content

def add_user(user_ame=""):
#  .../metaphor/vx.x/users
    """Add a user to the registered user list.
    
    parameter:
    
    - user_ame -> name of the user to add
    """
    url = ct.users_url 
    r = requests.post(url, json=user_ame)
    try:
        return r.json()
    except:
        return r.text

def delete_user(user_name=""):
#  .../metaphor/vx.x/users
    """Unregister the designed user.
    
    All the user belongings are destroyed.
    
    parameter:
    
    - user_name -> name of the user to unregister. If this name is "*", all the registered users are unregistered.
    """
    url = ct.users_url
    r = requests.delete(url, json=user_name)
    try:
        return r.json()
    except:
        return r.text

def get_model_list(userid):
#  .../metaphor/vx.x/user/<user_id>/models
    """Retrieve the list of models belongings to the given user.
    
    parameter:
    
    - userid -> ID of the user to examine.
    """
    url = ct.models_url.format(userid)
    r = requests.get(url)
    try:
        return r.json()
    except:
        return r.text
        
def create_model(userid, data="", raw=False):
    """create a new model.
    
    - data -> dictionary describing creation parameters.
    
        - training -> boolean giving the purpose of creation
        
        - source -> data file or data file content 
        
        - modelname -> name imposed to the model
        
        - trainable -> training capacity (default True)
        
        - inputs -> input number (default 1) 
        
        - outputs -> output number (default 1) 
        
        - hidden -> number of hidden neurons (default 2)
        
        - activfunc -> activation fonction (default TANH)
        
        - statelayer -> state layer (default -1 )
        
        - statenodeindex index of state node (default -1) 
        
        - order order of the network default 0) 
        
        - nosynapse -> build model without any synapses (default False)
         
        - existingnode -> already existing nodes (default 0) 
        
        - polytype -> type de polynome (default 0)
        
        - classif -> classifier (deafult False)
        
        - verbose=0,
         
        - data=None, 
        
        - dataformat=None,
         
        - normalize=False, 
        
        - weights=None, 
        
        - disp=0, 
        
        - callback=None  unused
        
    - raw -> If True, return raw request
    """
#    - modeldata=None, 
#    - callbackfct=None, 

#  .../metaphor/vx.x/user/<user_id>/models
    url = ct.models_url.format(userid)
    r = requests.post(url, json=data)
    if raw:
        return r
    try:
        return r.json()
    except:
        return r.content
        
def load_model(userid, data="", getID=False, raw=False):
    """load a new model from file.
    
    - datas :
    
        - source -> file or file content
        - 'modelname' -> name imposed to the model
        - 'descriptor' -> smiles code or similar descriptor
        - 'docompile' -> 

    raw -> If True, return raw request
    """
#  .../metaphor/vx.x/user/<user_id>/models
    url = ct.models_url.format(userid)
    if isinstance(data, str):
        data = {'source': data}
    r = requests.post(url, json=data)
    if raw:
        return r
    try:
        res = r.json()
        if not getID:
            return res
        else:
            return tuple(res[:2])
    except:
        return r.text

def get_model_attribute(userid, modelid, data=""):
    #  .../metaphor/vx.x/user/<user_id>/models/<model_id>
    """Retrieve model attributes.

    parameters:
    
    - userid -> user ID
    - modelid -> model ID belonging to the designed user.
    - data -> dictionary describing the attribute to read.
    
        - {'attributes': <attribute name>}
        
    return depending on the attribute.
    """
    url = ct.model_url.format(userid, modelid)
    r = requests.get(url, json=data)
    try:
        return r.json()
    except:
        return r.text

def set_model_attribute(userid, modelid, data=""):
    #  .../metaphor/vx.x/user/<user_id>/models/<model_id>
    """Write an attribute to the model. Can be used for user defined attributes.
    
    parameters:
    
    - userid -> user ID
    - modelid -> model ID belonging to the designed user
    - data -> dictionary describing the attribute to write
        - {'attributes': <attribute name>}
    """
    url = ct.model_url.format(userid, modelid)
    r = requests.put(url, json=data)
    try:
        return r.json()
    except:
        return r.text

def delete_models(userid, modelid):
    #  .../metaphor/vx.x/user/<user_id>/models
    """Delete a registered model.
    
    parameters:
    
    - userid -> user ID
    - modelid -> model ID belonging to the designed user. modelid may be "*" to delete all the user's models.
    """
    url = ct.models_url.format(userid)
    r = requests.delete(url, json=modelid)
    try:
        return r.json()
    except:
        return r.text

def get_function(userid, modelid, root_func_name, data=""): 
    #  /metaphor/vx.x/users/<user_id>/models/<model_id>/<root_func_name>  GET
    """Call a function to apply to the designed model. 
    The function called may **not** modify the sate of the designed model.
    
    parameters:
    
    - userid -> user ID
    - modelid -> model ID belonging to the designed user
    - root_func_name, data -> function to call. **data** is related to function:
    
        =============== ====================================
        function name   data
        =============== ====================================
        paramCount      None
        dataCount       None
        newWeights      {'stddev': stddev, 'bias0': bias0}
        getTrainingData {'prefix': None}
        inputNames      None
        outputNames     None
        inputs          None
        outputs         None
        inputNorm       None
        outputNorm      None
        targets         None
        getWeights      {'prefix': None}
        =============== ====================================
    
    """
    url = ct.model_fct_url.format(userid, modelid, root_func_name)
    r = requests.get(url, json=data)
    try:
        return r.json()
    except:
        return r.text
    
def _put_function(userid, modelid, root_func_name, data=""):
    #  /metaphor/vx.x/users/<user_id>/models/<model_id>/<root_func_name>  PUT
    url = ct.model_fct_url.format(userid, modelid, root_func_name)
    r = requests.put(url, json=data)
    try:
        return r.json()
    except:
        return r.text
    
def post_function(userid, modelid, root_func_name, data=""):
    #  /metaphor/vx.x/users/<user_id>/models/<model_id>/<root_func_name>  POST
    """Call a function to apply to the designed model. The function called may modify the sate of the designed model.
    
    parameters:
    
    - userid -> user ID
    - modelid -> model ID belonging to the designed user
    - root_func_name -> function to call. Availables functions are:
    
        - transfer
        - train
        - reverse_train
        - setWeights
    
    - data -> a dictionary depending upon the called function:
    
        - transfer:
        
            - inputs -> input vector.
            - index -> index of training data to use as inputs.
            - weights -> parameters to use. If None, current parameters are used.
            
        - train ->
        
            - startWeights -> starting parameter set to strat training with.
            - epochs -> maximum number of epochs allowed to training job
            - trainstyle -> unused
            - callback -> unused

        - reverse_train ->
        
            - outputtarget -> output value to target
            - inputs -> starting inputs
            - fixedinputs -> vector of boolean giving the input mobility freedom
            - epochs -> maximum number of epochs allowed to training job
            
        - setWeights ->
        
            - weights -> parameter vector to affect
            - prefix -> None
    
    """
    url = ct.model_fct_url.format(userid, modelid, root_func_name)
    r = requests.post(url, json=data)  #await 
    try:
        return r.json()
    except:
        return r.text
    
def post_file(userid, filepath=None, dest= "", extra={}):
    # /metaphor/vx.x/users/<user_id>/files
    """Upload a file to the server.
    
    parameters:
    
    - filepath -> path of the file to upload
    
    - dest -> relative destination path in the server
    
    - extra -> unused
    """
    url = ct.files_url.format(userid)
    data = extra.update({'dest': dest})
    if filepath is not None:
        with open(filepath,'rb') as ff:
            files={'file': ff}
            r = requests.post(url, params=data, files=files)
    try:
        return r.json()
    except:
        return r.text

#-----------------------------------------------------------------------

if __name__ == "__main__":
    server = 'macprosigma'
    port = 5005
    APIver = ct.APIversion
    
    result = initiate_connection(server=server, port=port, APIver=APIver)
    print(result)
    
    res = get_users()
    print("User list", res)
    
    res = get_user_name(946040)
    print(res)
    
    res = add_user(res)
    print("add existing user", res)
    
    res = add_user('abc')
    print("add non existing user", res)
    
    res = check_user('jeanluc', getID=False)
    print(res)
    try:
        for val in res:
            print(val)
    except:
        pass
    print('done')
#     modelNML_0 = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_api/src/testfiles/Tests SAP Samir MEDROUK/Modeles fusionnes/Modele_Final_V2.NML"
#     
#     myname = 'jeanluc'
#     res = requests.get(welcome_url)
#     print(res.text)
#     print("end welcome")
#     res = add_user(myname)
#     for key, val in res[1].items():
#         if val:
#             print("{0} is already registered".format(key))
#         else:
#             print("added", key)
#     add_user("albert")
#     add_user("jo")
#     res = delete_user("albert")
#     for val in res:
#         print(val)
#         
#     users = get_users()
#     print('registered users')
#     for key, val in users.items():
#         print("\t{}\t{}".format(val, key))
# 
#     
#     
#     userID = check_user(myname, True)
#     data = {'modelname': 'MyFirstModel',
#             'source': modelNML_0}
#     user_id, model_id = load_model(userID, data, True)
#     print('user \t->', user_id)
#     print('model \t->', model_id)
# 
#     user_id, model_id2 = load_model(userID, data, True)
#     
#     
#     res = get_model_list(user_id)
#     nm = get_user_name(user_id)
#     print("models belonging to {}".format(nm))
#     modelDict = res['models']
#     for ind, (key, val) in enumerate(modelDict.items()):
#         if not ind:
#             key0 = key
#         print("\t{0} -> {1}".format(key, val))
#         
#     data = {'delete': key0}
#     res = delete_models(user_id, data)
#     for val in res:
#         print(val)
#     print()
#     res = get_model_list(user_id)
#     modelDict = res['models']
#     print("models belonging to {}".format(nm))
#     key0 = 0
#     if not len(modelDict):
#         print("\tnone")
#     else:
#         for ind, (key, val) in enumerate(modelDict.items()):
#             if not ind:
#                 key0 = key
#             print("\t{0} -> {1}".format(key, val))
#     
#     data = {'inputs': (1,1,1,1),}
#     res = get_function(user_id, key0, 'transfer', data=data)
#     print("model({0}, {1})(inputs=(1,1,1,1)) = {2}".format(myname, key0, res))
#     
#     filename = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_Test/src/metaphor/test_monal/testFiles/fullalea.csv"
#     filename2 = "/Users/jeanluc/Documents/LiClipseWorkspace/Metaphor_Test/src/metaphor/test_monal/testFiles/l_153.xlsx"
#     
# #    res = post_file(user_id, dest='host/suite')
#     
#     res = post_file(user_id, filename, dest='suite')
#     print(res)
#     res = post_file(user_id, filename2)
#     print(res)
#     
#     print("Done")
