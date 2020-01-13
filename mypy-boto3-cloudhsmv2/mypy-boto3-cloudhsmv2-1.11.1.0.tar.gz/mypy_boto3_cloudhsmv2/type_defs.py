"""
Main interface for cloudhsmv2 service type definitions.

Usage::

    from mypy_boto3.cloudhsmv2.type_defs import ClientCopyBackupToRegionResponseDestinationBackupTypeDef

    data: ClientCopyBackupToRegionResponseDestinationBackupTypeDef = {...}
"""
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCopyBackupToRegionResponseDestinationBackupTypeDef",
    "ClientCopyBackupToRegionResponseTypeDef",
    "ClientCreateClusterResponseClusterCertificatesTypeDef",
    "ClientCreateClusterResponseClusterHsmsTypeDef",
    "ClientCreateClusterResponseClusterTypeDef",
    "ClientCreateClusterResponseTypeDef",
    "ClientCreateHsmResponseHsmTypeDef",
    "ClientCreateHsmResponseTypeDef",
    "ClientDeleteBackupResponseBackupTypeDef",
    "ClientDeleteBackupResponseTypeDef",
    "ClientDeleteClusterResponseClusterCertificatesTypeDef",
    "ClientDeleteClusterResponseClusterHsmsTypeDef",
    "ClientDeleteClusterResponseClusterTypeDef",
    "ClientDeleteClusterResponseTypeDef",
    "ClientDeleteHsmResponseTypeDef",
    "ClientDescribeBackupsResponseBackupsTypeDef",
    "ClientDescribeBackupsResponseTypeDef",
    "ClientDescribeClustersResponseClustersCertificatesTypeDef",
    "ClientDescribeClustersResponseClustersHsmsTypeDef",
    "ClientDescribeClustersResponseClustersTypeDef",
    "ClientDescribeClustersResponseTypeDef",
    "ClientInitializeClusterResponseTypeDef",
    "ClientListTagsResponseTagListTypeDef",
    "ClientListTagsResponseTypeDef",
    "ClientRestoreBackupResponseBackupTypeDef",
    "ClientRestoreBackupResponseTypeDef",
    "ClientTagResourceTagListTypeDef",
    "BackupTypeDef",
    "DescribeBackupsResponseTypeDef",
    "CertificatesTypeDef",
    "HsmTypeDef",
    "ClusterTypeDef",
    "DescribeClustersResponseTypeDef",
    "TagTypeDef",
    "ListTagsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCopyBackupToRegionResponseDestinationBackupTypeDef = TypedDict(
    "ClientCopyBackupToRegionResponseDestinationBackupTypeDef",
    {"CreateTimestamp": datetime, "SourceRegion": str, "SourceBackup": str, "SourceCluster": str},
    total=False,
)

ClientCopyBackupToRegionResponseTypeDef = TypedDict(
    "ClientCopyBackupToRegionResponseTypeDef",
    {"DestinationBackup": ClientCopyBackupToRegionResponseDestinationBackupTypeDef},
    total=False,
)

ClientCreateClusterResponseClusterCertificatesTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)

ClientCreateClusterResponseClusterHsmsTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterHsmsTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS", "ACTIVE", "DEGRADED", "DELETE_IN_PROGRESS", "DELETED"
        ],
        "StateMessage": str,
    },
    total=False,
)

ClientCreateClusterResponseClusterTypeDef = TypedDict(
    "ClientCreateClusterResponseClusterTypeDef",
    {
        "BackupPolicy": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List[ClientCreateClusterResponseClusterHsmsTypeDef],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS",
            "UNINITIALIZED",
            "INITIALIZE_IN_PROGRESS",
            "INITIALIZED",
            "ACTIVE",
            "UPDATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "DELETED",
            "DEGRADED",
        ],
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": ClientCreateClusterResponseClusterCertificatesTypeDef,
    },
    total=False,
)

ClientCreateClusterResponseTypeDef = TypedDict(
    "ClientCreateClusterResponseTypeDef",
    {"Cluster": ClientCreateClusterResponseClusterTypeDef},
    total=False,
)

ClientCreateHsmResponseHsmTypeDef = TypedDict(
    "ClientCreateHsmResponseHsmTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS", "ACTIVE", "DEGRADED", "DELETE_IN_PROGRESS", "DELETED"
        ],
        "StateMessage": str,
    },
    total=False,
)

ClientCreateHsmResponseTypeDef = TypedDict(
    "ClientCreateHsmResponseTypeDef", {"Hsm": ClientCreateHsmResponseHsmTypeDef}, total=False
)

ClientDeleteBackupResponseBackupTypeDef = TypedDict(
    "ClientDeleteBackupResponseBackupTypeDef",
    {
        "BackupId": str,
        "BackupState": Literal["CREATE_IN_PROGRESS", "READY", "DELETED", "PENDING_DELETION"],
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
    },
    total=False,
)

ClientDeleteBackupResponseTypeDef = TypedDict(
    "ClientDeleteBackupResponseTypeDef",
    {"Backup": ClientDeleteBackupResponseBackupTypeDef},
    total=False,
)

ClientDeleteClusterResponseClusterCertificatesTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)

ClientDeleteClusterResponseClusterHsmsTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterHsmsTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS", "ACTIVE", "DEGRADED", "DELETE_IN_PROGRESS", "DELETED"
        ],
        "StateMessage": str,
    },
    total=False,
)

ClientDeleteClusterResponseClusterTypeDef = TypedDict(
    "ClientDeleteClusterResponseClusterTypeDef",
    {
        "BackupPolicy": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List[ClientDeleteClusterResponseClusterHsmsTypeDef],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS",
            "UNINITIALIZED",
            "INITIALIZE_IN_PROGRESS",
            "INITIALIZED",
            "ACTIVE",
            "UPDATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "DELETED",
            "DEGRADED",
        ],
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": ClientDeleteClusterResponseClusterCertificatesTypeDef,
    },
    total=False,
)

ClientDeleteClusterResponseTypeDef = TypedDict(
    "ClientDeleteClusterResponseTypeDef",
    {"Cluster": ClientDeleteClusterResponseClusterTypeDef},
    total=False,
)

ClientDeleteHsmResponseTypeDef = TypedDict(
    "ClientDeleteHsmResponseTypeDef", {"HsmId": str}, total=False
)

ClientDescribeBackupsResponseBackupsTypeDef = TypedDict(
    "ClientDescribeBackupsResponseBackupsTypeDef",
    {
        "BackupId": str,
        "BackupState": Literal["CREATE_IN_PROGRESS", "READY", "DELETED", "PENDING_DELETION"],
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
    },
    total=False,
)

ClientDescribeBackupsResponseTypeDef = TypedDict(
    "ClientDescribeBackupsResponseTypeDef",
    {"Backups": List[ClientDescribeBackupsResponseBackupsTypeDef], "NextToken": str},
    total=False,
)

ClientDescribeClustersResponseClustersCertificatesTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersCertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)

ClientDescribeClustersResponseClustersHsmsTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersHsmsTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "HsmId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS", "ACTIVE", "DEGRADED", "DELETE_IN_PROGRESS", "DELETED"
        ],
        "StateMessage": str,
    },
    total=False,
)

ClientDescribeClustersResponseClustersTypeDef = TypedDict(
    "ClientDescribeClustersResponseClustersTypeDef",
    {
        "BackupPolicy": str,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List[ClientDescribeClustersResponseClustersHsmsTypeDef],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS",
            "UNINITIALIZED",
            "INITIALIZE_IN_PROGRESS",
            "INITIALIZED",
            "ACTIVE",
            "UPDATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "DELETED",
            "DEGRADED",
        ],
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": ClientDescribeClustersResponseClustersCertificatesTypeDef,
    },
    total=False,
)

ClientDescribeClustersResponseTypeDef = TypedDict(
    "ClientDescribeClustersResponseTypeDef",
    {"Clusters": List[ClientDescribeClustersResponseClustersTypeDef], "NextToken": str},
    total=False,
)

ClientInitializeClusterResponseTypeDef = TypedDict(
    "ClientInitializeClusterResponseTypeDef",
    {
        "State": Literal[
            "CREATE_IN_PROGRESS",
            "UNINITIALIZED",
            "INITIALIZE_IN_PROGRESS",
            "INITIALIZED",
            "ACTIVE",
            "UPDATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "DELETED",
            "DEGRADED",
        ],
        "StateMessage": str,
    },
    total=False,
)

ClientListTagsResponseTagListTypeDef = TypedDict(
    "ClientListTagsResponseTagListTypeDef", {"Key": str, "Value": str}, total=False
)

ClientListTagsResponseTypeDef = TypedDict(
    "ClientListTagsResponseTypeDef",
    {"TagList": List[ClientListTagsResponseTagListTypeDef], "NextToken": str},
    total=False,
)

ClientRestoreBackupResponseBackupTypeDef = TypedDict(
    "ClientRestoreBackupResponseBackupTypeDef",
    {
        "BackupId": str,
        "BackupState": Literal["CREATE_IN_PROGRESS", "READY", "DELETED", "PENDING_DELETION"],
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
    },
    total=False,
)

ClientRestoreBackupResponseTypeDef = TypedDict(
    "ClientRestoreBackupResponseTypeDef",
    {"Backup": ClientRestoreBackupResponseBackupTypeDef},
    total=False,
)

_RequiredClientTagResourceTagListTypeDef = TypedDict(
    "_RequiredClientTagResourceTagListTypeDef", {"Key": str}
)
_OptionalClientTagResourceTagListTypeDef = TypedDict(
    "_OptionalClientTagResourceTagListTypeDef", {"Value": str}, total=False
)


class ClientTagResourceTagListTypeDef(
    _RequiredClientTagResourceTagListTypeDef, _OptionalClientTagResourceTagListTypeDef
):
    pass


_RequiredBackupTypeDef = TypedDict("_RequiredBackupTypeDef", {"BackupId": str})
_OptionalBackupTypeDef = TypedDict(
    "_OptionalBackupTypeDef",
    {
        "BackupState": Literal["CREATE_IN_PROGRESS", "READY", "DELETED", "PENDING_DELETION"],
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
    },
    total=False,
)


class BackupTypeDef(_RequiredBackupTypeDef, _OptionalBackupTypeDef):
    pass


DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {"Backups": List[BackupTypeDef], "NextToken": str},
    total=False,
)

CertificatesTypeDef = TypedDict(
    "CertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)

_RequiredHsmTypeDef = TypedDict("_RequiredHsmTypeDef", {"HsmId": str})
_OptionalHsmTypeDef = TypedDict(
    "_OptionalHsmTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "State": Literal[
            "CREATE_IN_PROGRESS", "ACTIVE", "DEGRADED", "DELETE_IN_PROGRESS", "DELETED"
        ],
        "StateMessage": str,
    },
    total=False,
)


class HsmTypeDef(_RequiredHsmTypeDef, _OptionalHsmTypeDef):
    pass


ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "BackupPolicy": Literal["DEFAULT"],
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List[HsmTypeDef],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS",
            "UNINITIALIZED",
            "INITIALIZE_IN_PROGRESS",
            "INITIALIZED",
            "ACTIVE",
            "UPDATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "DELETED",
            "DEGRADED",
        ],
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": CertificatesTypeDef,
    },
    total=False,
)

DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {"Clusters": List[ClusterTypeDef], "NextToken": str},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

_RequiredListTagsResponseTypeDef = TypedDict(
    "_RequiredListTagsResponseTypeDef", {"TagList": List[TagTypeDef]}
)
_OptionalListTagsResponseTypeDef = TypedDict(
    "_OptionalListTagsResponseTypeDef", {"NextToken": str}, total=False
)


class ListTagsResponseTypeDef(_RequiredListTagsResponseTypeDef, _OptionalListTagsResponseTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
