# -*- coding: utf-8 -*-
from typing import Dict

from .grpc_client import StaticFileServiceException, StaticFileServiceGRPCClient, UploadCredentials, OSSBucketInfo

__all__ = ["init_service", "get_oss_bucket_info", "get_upload_credentials", "move_static_file", "StaticFileServiceException", "UploadCredentials", "OSSBucketInfo"]
_static_file_service_grpc_client: StaticFileServiceGRPCClient


def init_service(endpoint: str) -> None:
    global _static_file_service_grpc_client
    assert type(endpoint) == str, "endpoint must be a str"
    _static_file_service_grpc_client = StaticFileServiceGRPCClient(endpoint=endpoint)


def get_oss_bucket_info() -> OSSBucketInfo:
    global _static_file_service_grpc_client
    assert _static_file_service_grpc_client is not None, "log service sdk must be init first"
    return _static_file_service_grpc_client.get_oss_bucket_info()


def get_upload_credentials() -> UploadCredentials:
    global _static_file_service_grpc_client
    assert _static_file_service_grpc_client is not None, "log service sdk must be init first"
    return _static_file_service_grpc_client.get_upload_credentials()


def move_static_file(from_path: str, to_path: str) -> None:
    global _static_file_service_grpc_client
    assert _static_file_service_grpc_client is not None, "log service sdk must be init first"
    assert type(from_path) == str, "from_path must be a str"
    assert type(to_path) == str, "to_path must be a str"
    _static_file_service_grpc_client.move_static_file(from_path=from_path, to_path=to_path)
