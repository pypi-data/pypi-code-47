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
"""
This module defines the routes for metaphor server.
"""
import sys

application = "metaphor"
APIversion = 1.0

def initiate_routes(server="0.0.0.0", port=5005, appli=application, 
        APIver=APIversion):
    """Initiate metaphor client interface routes.
    
    parameters:
    
    - server -> IP address or name of the server machine. default "0.0.0.0"
    - port -> Number of port. default 5005 
    - application -> Application name. default 'metaphor' 
    - APIversion -> Version of the interface. default APIversion
    """
    global welcome_url, root_url, events_url, user_url, users_url, files_url, \
        models_url, model_url, model_fct_url, application, APIversion
        # removed scheme
    
    application = appli
    APIversion = APIver
    scheme = "http://{0}:{1}".format(server, port)
    # http://<server>:<port>
    
    welcome_url = "{0}/{1}".format(scheme, application)
    # "http://<server>:<port>/metaphor"
    
    root_url = "{0}/{1}/v{2}".format(scheme, application, APIversion)
    #  http://<server>:<port>/metaphor/vx.x
    
    events_url = "{0}/events".format(root_url)
    # http://<server>:<port>/metaphor/vx.x/events
    
    user_url = '{0}/user/{{0}}'.format(root_url)
    #  http://<server>:<port>/metaphor/vx.x/user/<string:user_name>
    
    users_url = '{0}/users'.format(root_url)
    #  http://<server>:<port>/metaphor/vx.x/users
    
    files_url = '{0}/{{0}}/files'.format(users_url)
    # http://<server>:<port>/metaphor/vx.x/users/<user_id>/files
    
    models_url = '{0}/{{0}}/models'.format(users_url)
    #  http://<server>:<port>/metaphor/vx.x/user/<user_id>/models
    
    model_url = '{0}/{{0}}/models/{{1}}'.format(users_url)
    #  http://<server>:<port>/metaphor/vx.x/user/<user_id>/models
    
    model_fct_url = '{0}/{{0}}/models/{{1}}/{{2}}'.format(users_url)
    #  http://<server>:<port>/metaphor/vx.x/users/<user_id>/models/<model_id>/<func_name>

