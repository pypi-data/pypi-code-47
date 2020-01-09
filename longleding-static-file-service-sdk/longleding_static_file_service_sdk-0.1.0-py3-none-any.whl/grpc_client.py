# -*- coding: utf-8 -*-
import time
from datetime import datetime, timezone, timedelta
from typing import Dict

import grpc
from . import common_pb2
from . import staticFileService_pb2, staticFileService_pb2_grpc


class StaticFileServiceException(Exception):
    """ Static File Service Exception. """
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def __new__(*args, **kwargs):
        pass


class OSSBucketInfo:

    def __init__(self, bucket_name: str, endpoint: str):
        self.bucket_name = bucket_name
        self.endpoint = endpoint

    @classmethod
    def from_pb(cls, oss_bucket_info: staticFileService_pb2.OSSBucketInfoMessage):
        return cls(oss_bucket_info.bucket_name, oss_bucket_info.endpoint)

    @property
    def bucket_name(self):
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, value):
        assert type(value) == str, "bucket_name must be a str"
        self._bucket_name = value

    @property
    def endpoint(self):
        return self._endpoint

    @endpoint.setter
    def endpoint(self, value):
        assert type(value) == str, "endpoint must be a str"
        self._endpoint = value

    def _desc(self):
        return "<OSSBucketInfo(bucket_name:{} endpoint:{})>".format(
            self.bucket_name,
            self.endpoint
        )

    def __str__(self):
        return self._desc()

    def __repr__(self):
        return self._desc()


class UploadCredentials:

    def __init__(self, access_key_id: str, access_key_secret: str, expiration: datetime, security_token: str):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.expiration = expiration
        self.security_token = security_token

    @classmethod
    def from_pb(cls, upload_credentials: staticFileService_pb2.UploadCredentialsMessage):
        expiration = datetime.fromtimestamp(upload_credentials.expiration.seconds)
        expiration.replace(tzinfo=timezone(timedelta(hours=8)))
        return cls(upload_credentials.access_key_id,
                   upload_credentials.access_key_secret,
                   expiration,
                   upload_credentials.security_token)

    @property
    def access_key_id(self):
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, value):
        assert type(value) == str, "access_key_id must be a str"
        self._access_key_id = value

    @property
    def access_key_secret(self):
        return self._access_key_secret

    @access_key_secret.setter
    def access_key_secret(self, value):
        assert type(value) == str, "access_key_secret must be a str"
        self._access_key_secret = value

    @property
    def expiration(self):
        return self._expiration

    @expiration.setter
    def expiration(self, value):
        assert type(value) == datetime, "expiration must be a datetime"
        self._expiration = value

    @property
    def security_token(self):
        return self._security_token

    @security_token.setter
    def security_token(self, value):
        assert type(value) == str, "security_token must be a str"
        self._security_token = value

    def _desc(self):
        return "<UploadCredentials(access_key_id:{} access_key_secret:{} expiration:{} security_token:{})>".format(
            self.access_key_id,
            self.access_key_secret,
            self.expiration,
            self.security_token
        )

    def __str__(self):
        return self._desc()

    def __repr__(self):
        return self._desc()


class StaticFileServiceGRPCClient:
    _endpoint = None
    _retry_time = 3
    _retry_interval = 2

    def __init__(self, endpoint):
        self._endpoint = endpoint

    def get_oss_bucket_info(self) -> OSSBucketInfo:
        with grpc.insecure_channel(self._endpoint) as channel:
            stub = staticFileService_pb2_grpc.StaticFileServiceStub(channel)
            empty = common_pb2.Empty()
            response = None
            error = None
            for i in range(self._retry_time):
                try:
                    response = stub.GetOSSBucketInfo(empty)
                    break
                except grpc.RpcError as e:
                    error = e
                    time.sleep(self._retry_interval * (i + 1))
            if response is None:
                raise error
            if response.code != 0:
                raise StaticFileServiceException(response.msg)
            unpacked_msg = staticFileService_pb2.OSSBucketInfoMessage()
            response.data.Unpack(unpacked_msg)
            return OSSBucketInfo.from_pb(unpacked_msg)

    def get_upload_credentials(self) -> UploadCredentials:
        with grpc.insecure_channel(self._endpoint) as channel:
            stub = staticFileService_pb2_grpc.StaticFileServiceStub(channel)
            empty = common_pb2.Empty()
            response = None
            error = None
            for i in range(self._retry_time):
                try:
                    response = stub.GetUploadCredentials(empty)
                    break
                except grpc.RpcError as e:
                    error = e
                    time.sleep(self._retry_interval * (i + 1))
            if response is None:
                raise error
            if response.code != 0:
                raise StaticFileServiceException(response.msg)
            unpacked_msg = staticFileService_pb2.UploadCredentialsMessage()
            response.data.Unpack(unpacked_msg)
            return UploadCredentials.from_pb(unpacked_msg)

    def move_static_file(self, from_path: str, to_path: str) -> None:
        with grpc.insecure_channel(self._endpoint) as channel:
            stub = staticFileService_pb2_grpc.StaticFileServiceStub(channel)
            request = staticFileService_pb2.MoveStaticFileRequest(from_path=from_path, to_path=to_path)
            response = None
            error = None
            for i in range(self._retry_time):
                try:
                    response = stub.MoveStaticFile(request)
                    break
                except grpc.RpcError as e:
                    error = e
                    time.sleep(self._retry_interval * (i + 1))
            if response is None:
                raise error
            if response.code != 0:
                raise StaticFileServiceException(response.msg)
            return
