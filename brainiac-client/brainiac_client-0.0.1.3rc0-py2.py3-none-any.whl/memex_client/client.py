import atexit
import os
from typing import Dict, List, Optional
from urllib.parse import urljoin
import cloudpickle

import grpc
import requests
from google.protobuf.struct_pb2 import Struct

from memex_client.errors import AuthenticationError
from memex_client.protos.brainiac_pb2 import (BrainiacRequest, BrainiacResponse, ProjectData,
                                              ThirdPartyRequest, ThirdPartyResponse, UserData)
from memex_client.protos.brainiac_pb2_grpc import EngineStub

BRAINIAC_CLIENT_USERNAME = "BRAINIAC_CLIENT_USERNAME"
BRAINIAC_CLIENT_PASSWORD = "BRAINIAC_CLIENT_PASSWORD"
DEFAULT_PORT = 5000


class ModelClient:
    def __init__(self, grpc_stub, client, project, force_download, url):
        self.stub = grpc_stub
        self.client = client
        self.project = project
        self.force_download = force_download
        self.url = url

    def set_methods(self, methods: List[str], http):
        if http:
            [setattr(self, method, self.__create_http_method(method)) for method in methods]
        else:
            [setattr(self, method, self.__create_grpc_method(method)) for method in methods]

    def __create_http_method(self, name: str):
        def wrapper(body: Dict):
            struct = Struct()
            struct.update(body)
            br_req = BrainiacRequest(client=self.client,
                                     project=self.project,
                                     function_name=name,
                                     body=struct,
                                     force_download=self.force_download)
            url = urljoin(self.url, "/runFunction")
            res = requests.get(url, data=br_req.SerializeToString())
            response = BrainiacResponse.FromString(res.content)
            if response.status.status_code == 200:
                return response.body
            return None

        return wrapper

    def __create_grpc_method(self, name: str):
        def wrapper(body: Dict):
            struct = Struct()
            struct.update(body)
            response = self.stub.runFunction(
                BrainiacRequest(client=self.client,
                                project=self.project,
                                function_name=name,
                                body=struct,
                                force_download=self.force_download))
            if response.status.status_code == 200:
                return response.body
            return None

        return wrapper


class BrainiacClient:
    def __init__(self, url: Optional[str] = None, stub: EngineStub = None, http=True):
        if url is None:
            url = 'https://brainiac-engine.herokuapp.com' if http else 'localhost:{}'.format(
                DEFAULT_PORT)
        self.url = url
        self.channel = grpc.insecure_channel(url)
        self.stub = stub or EngineStub(self.channel)
        self.http = http
        self.client = UserData(username=os.environ.get(BRAINIAC_CLIENT_USERNAME),
                               password=os.environ.get(BRAINIAC_CLIENT_PASSWORD))
        atexit.register(self.channel.close)

    def __make_request(self, url: str, request_object, response_type):
        res = requests.get(url, data=request_object.SerializeToString())
        return response_type.FromString(res.content)

    def get_model_client(self, creator: str, project: str,
                         force_download=False) -> Optional[ModelClient]:
        project_data = ProjectData(creator=creator, name=project)
        br_req = BrainiacRequest(client=self.client, project=project_data)
        response = None
        if self.http:
            url = urljoin(self.url, "/listFunctions")
            response = self.__make_request(url, br_req, BrainiacResponse)
        else:
            response = self.stub.listFunctions(br_req)
        if response.status.status_code == 200:
            methods = response.body["response"]
            model = ModelClient(self.stub, self.client, project_data, force_download, self.url)
            model.set_methods(methods, self.http)
            return model
        elif response.status.status_code == 404:
            return None
        elif response.status.status_code == 401:
            raise AuthenticationError(response.status.status_reason)
        else:
            raise Exception(response.status.status_reason)

    def runThirdPartyFunction(self, models: ModelClient, function, data: Dict,
                              force_download=False) -> Dict:
        body = Struct()
        body.update(data)
        thpr = ThirdPartyRequest(client=self.client,
                                 projects=[model.project for model in models],
                                 function=cloudpickle.dumps(function),
                                 body=body,
                                 force_download=force_download)
        response = None
        if self.http:
            url = urljoin(self.url, "/thirdPartyFunction")
            response = self.__make_request(url, thpr, ThirdPartyResponse)
        else:
            response = self.stub.thirdPartyFunction(thpr)
        if response.status.status_code == 200:
            return response.body
        return None
