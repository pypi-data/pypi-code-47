"""
Main interface for qldb-session service client

Usage::

    import boto3
    from mypy_boto3.qldb_session import QLDBSessionClient

    session = boto3.Session()

    client: QLDBSessionClient = boto3.client("qldb-session")
    session_client: QLDBSessionClient = session.client("qldb-session")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from __future__ import annotations

from typing import Any, Dict
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_qldb_session.client as client_scope
from mypy_boto3_qldb_session.type_defs import (
    CommitTransactionRequestTypeDef,
    ExecuteStatementRequestTypeDef,
    FetchPageRequestTypeDef,
    SendCommandResultTypeDef,
    StartSessionRequestTypeDef,
)


__all__ = ("QLDBSessionClient",)


class QLDBSessionClient(BaseClient):
    """
    [QLDBSession.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/qldb-session.html#QLDBSession.Client)
    """

    exceptions: client_scope.Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/qldb-session.html#QLDBSession.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/qldb-session.html#QLDBSession.Client.generate_presigned_url)
        """

    def send_command(
        self,
        SessionToken: str = None,
        StartSession: StartSessionRequestTypeDef = None,
        StartTransaction: Dict[str, Any] = None,
        EndSession: Dict[str, Any] = None,
        CommitTransaction: CommitTransactionRequestTypeDef = None,
        AbortTransaction: Dict[str, Any] = None,
        ExecuteStatement: ExecuteStatementRequestTypeDef = None,
        FetchPage: FetchPageRequestTypeDef = None,
    ) -> SendCommandResultTypeDef:
        """
        [Client.send_command documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/qldb-session.html#QLDBSession.Client.send_command)
        """


class Exceptions:
    BadRequestException: Boto3ClientError
    ClientError: Boto3ClientError
    InvalidSessionException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    OccConflictException: Boto3ClientError
    RateExceededException: Boto3ClientError
