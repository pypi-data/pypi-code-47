import unittest
import mock
import os
import cloudpickle
from brainiac_client.client import (BrainiacClient, BRAINIAC_CLIENT_USERNAME,
                                    BRAINIAC_CLIENT_PASSWORD)
from brainiac_client.protos.brainiac_pb2 import (BrainiacRequest, BrainiacResponse, Status,
                                                 ThirdPartyRequest, ThirdPartyResponse)
from brainiac_client.tests.third_party import action
from google.protobuf.struct_pb2 import Struct


class MockStub:
    def __init__(self, channel):
        # self.runFunction = self.runfunc
        pass

    def runFunction(self, request: BrainiacRequest) -> BrainiacResponse:
        body = Struct()
        body.update({
            "response": {
                "function_name": request.function_name,
                "force_download": request.force_download,
                "project": {
                    "owner": request.project.owner,
                    "name": request.project.name
                },
                "client": {
                    "username": request.client.username,
                    "password": request.client.password
                },
                "body": request.body["number"]
            }
        })
        return BrainiacResponse(status=Status(status_code=200), body=body)

    def listFunctions(self, request: BrainiacRequest) -> BrainiacResponse:
        body = Struct()
        body.update({"response": ["some_function"]})
        return BrainiacResponse(status=Status(status_code=200), body=body)

    def thirdPartyFunction(self, request: ThirdPartyRequest) -> ThirdPartyResponse:
        body = Struct()
        body.update({
            "response": {
                "function":
                cloudpickle.loads(request.function).__name__,
                "force_download":
                request.force_download,
                "project": [{
                    "owner": project.owner,
                    "name": project.name
                } for project in request.projects],
                "client": {
                    "username": request.client.username,
                    "password": request.client.password
                },
                "body":
                request.body["number"]
            }
        })
        return ThirdPartyResponse(status=Status(status_code=200), body=body)


class TestServer(unittest.TestCase):
    @mock.patch.dict(os.environ, {
        BRAINIAC_CLIENT_USERNAME: "username",
        BRAINIAC_CLIENT_PASSWORD: "password"
    })
    def test_CreateFunctionGrpc(self):
        stub = MockStub(None)
        client = BrainiacClient(http=False, stub=stub)
        model = client.get_model_client("testUser0", "testProject0")
        response = model.some_function({"number": 10})
        expected_response = Struct()
        expected_response.update({
            "response": {
                "function_name": "some_function",
                "force_download": False,
                "project": {
                    "owner": "testUser0",
                    "name": "testProject0"
                },
                "client": {
                    "username": 'username',
                    "password": 'password'
                },
                "body": 10
            }
        })
        assert response == expected_response

    @mock.patch.dict(os.environ, {
        BRAINIAC_CLIENT_USERNAME: "username",
        BRAINIAC_CLIENT_PASSWORD: "password"
    })
    def test_ThirdPartyFunctionGrpc(self):
        stub = MockStub(None)
        client = BrainiacClient(http=False, stub=stub)
        model = client.get_model_client("testUser0", "testProject0")
        response = client.runThirdPartyFunction([model], action, {"number": 10})
        expected_response = Struct()
        expected_response.update({
            "response": {
                "function": "action",
                "force_download": False,
                "project": [{
                    "owner": "testUser0",
                    "name": "testProject0"
                }],
                "client": {
                    "username": "username",
                    "password": "password"
                },
                "body": 10
            }
        })
        assert response == expected_response
