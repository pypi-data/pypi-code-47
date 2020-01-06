"""
Main interface for kafka service type definitions.

Usage::

    from mypy_boto3.kafka.type_defs import BrokerEBSVolumeInfoTypeDef

    data: BrokerEBSVolumeInfoTypeDef = {...}
"""
from __future__ import annotations

from datetime import datetime
import sys
from typing import Dict, IO, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BrokerEBSVolumeInfoTypeDef",
    "EBSStorageInfoTypeDef",
    "StorageInfoTypeDef",
    "BrokerNodeGroupInfoTypeDef",
    "TlsTypeDef",
    "ClientAuthenticationTypeDef",
    "ConfigurationInfoTypeDef",
    "CreateClusterResponseTypeDef",
    "ConfigurationRevisionTypeDef",
    "CreateConfigurationResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "ErrorInfoTypeDef",
    "JmxExporterTypeDef",
    "NodeExporterTypeDef",
    "PrometheusTypeDef",
    "OpenMonitoringTypeDef",
    "MutableClusterInfoTypeDef",
    "ClusterOperationInfoTypeDef",
    "DescribeClusterOperationResponseTypeDef",
    "BrokerSoftwareInfoTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionInTransitTypeDef",
    "EncryptionInfoTypeDef",
    "ClusterInfoTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "GetBootstrapBrokersResponseTypeDef",
    "ListClusterOperationsResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ConfigurationTypeDef",
    "ListConfigurationsResponseTypeDef",
    "BrokerNodeInfoTypeDef",
    "ZookeeperNodeInfoTypeDef",
    "NodeInfoTypeDef",
    "ListNodesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "JmxExporterInfoTypeDef",
    "NodeExporterInfoTypeDef",
    "PrometheusInfoTypeDef",
    "OpenMonitoringInfoTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateBrokerCountResponseTypeDef",
    "UpdateBrokerStorageResponseTypeDef",
    "UpdateClusterConfigurationResponseTypeDef",
    "UpdateMonitoringResponseTypeDef",
)

BrokerEBSVolumeInfoTypeDef = TypedDict(
    "BrokerEBSVolumeInfoTypeDef", {"KafkaBrokerNodeId": str, "VolumeSizeGB": int}
)

EBSStorageInfoTypeDef = TypedDict("EBSStorageInfoTypeDef", {"VolumeSize": int}, total=False)

StorageInfoTypeDef = TypedDict(
    "StorageInfoTypeDef", {"EbsStorageInfo": EBSStorageInfoTypeDef}, total=False
)

_RequiredBrokerNodeGroupInfoTypeDef = TypedDict(
    "_RequiredBrokerNodeGroupInfoTypeDef", {"ClientSubnets": List[str], "InstanceType": str}
)
_OptionalBrokerNodeGroupInfoTypeDef = TypedDict(
    "_OptionalBrokerNodeGroupInfoTypeDef",
    {
        "BrokerAZDistribution": Literal["DEFAULT"],
        "SecurityGroups": List[str],
        "StorageInfo": StorageInfoTypeDef,
    },
    total=False,
)


class BrokerNodeGroupInfoTypeDef(
    _RequiredBrokerNodeGroupInfoTypeDef, _OptionalBrokerNodeGroupInfoTypeDef
):
    pass


TlsTypeDef = TypedDict("TlsTypeDef", {"CertificateAuthorityArnList": List[str]}, total=False)

ClientAuthenticationTypeDef = TypedDict(
    "ClientAuthenticationTypeDef", {"Tls": TlsTypeDef}, total=False
)

ConfigurationInfoTypeDef = TypedDict("ConfigurationInfoTypeDef", {"Arn": str, "Revision": int})

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "ClusterArn": str,
        "ClusterName": str,
        "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"],
    },
    total=False,
)

_RequiredConfigurationRevisionTypeDef = TypedDict(
    "_RequiredConfigurationRevisionTypeDef", {"CreationTime": datetime, "Revision": int}
)
_OptionalConfigurationRevisionTypeDef = TypedDict(
    "_OptionalConfigurationRevisionTypeDef", {"Description": str}, total=False
)


class ConfigurationRevisionTypeDef(
    _RequiredConfigurationRevisionTypeDef, _OptionalConfigurationRevisionTypeDef
):
    pass


CreateConfigurationResponseTypeDef = TypedDict(
    "CreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "LatestRevision": ConfigurationRevisionTypeDef,
        "Name": str,
    },
    total=False,
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {"ClusterArn": str, "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"]},
    total=False,
)

ErrorInfoTypeDef = TypedDict(
    "ErrorInfoTypeDef", {"ErrorCode": str, "ErrorString": str}, total=False
)

JmxExporterTypeDef = TypedDict("JmxExporterTypeDef", {"EnabledInBroker": bool})

NodeExporterTypeDef = TypedDict("NodeExporterTypeDef", {"EnabledInBroker": bool})

PrometheusTypeDef = TypedDict(
    "PrometheusTypeDef",
    {"JmxExporter": JmxExporterTypeDef, "NodeExporter": NodeExporterTypeDef},
    total=False,
)

OpenMonitoringTypeDef = TypedDict("OpenMonitoringTypeDef", {"Prometheus": PrometheusTypeDef})

MutableClusterInfoTypeDef = TypedDict(
    "MutableClusterInfoTypeDef",
    {
        "BrokerEBSVolumeInfo": List[BrokerEBSVolumeInfoTypeDef],
        "ConfigurationInfo": ConfigurationInfoTypeDef,
        "NumberOfBrokerNodes": int,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "OpenMonitoring": OpenMonitoringTypeDef,
    },
    total=False,
)

ClusterOperationInfoTypeDef = TypedDict(
    "ClusterOperationInfoTypeDef",
    {
        "ClientRequestId": str,
        "ClusterArn": str,
        "CreationTime": datetime,
        "EndTime": datetime,
        "ErrorInfo": ErrorInfoTypeDef,
        "OperationArn": str,
        "OperationState": str,
        "OperationType": str,
        "SourceClusterInfo": MutableClusterInfoTypeDef,
        "TargetClusterInfo": MutableClusterInfoTypeDef,
    },
    total=False,
)

DescribeClusterOperationResponseTypeDef = TypedDict(
    "DescribeClusterOperationResponseTypeDef",
    {"ClusterOperationInfo": ClusterOperationInfoTypeDef},
    total=False,
)

BrokerSoftwareInfoTypeDef = TypedDict(
    "BrokerSoftwareInfoTypeDef",
    {"ConfigurationArn": str, "ConfigurationRevision": int, "KafkaVersion": str},
    total=False,
)

EncryptionAtRestTypeDef = TypedDict("EncryptionAtRestTypeDef", {"DataVolumeKMSKeyId": str})

EncryptionInTransitTypeDef = TypedDict(
    "EncryptionInTransitTypeDef",
    {"ClientBroker": Literal["TLS", "TLS_PLAINTEXT", "PLAINTEXT"], "InCluster": bool},
    total=False,
)

EncryptionInfoTypeDef = TypedDict(
    "EncryptionInfoTypeDef",
    {
        "EncryptionAtRest": EncryptionAtRestTypeDef,
        "EncryptionInTransit": EncryptionInTransitTypeDef,
    },
    total=False,
)

ClusterInfoTypeDef = TypedDict(
    "ClusterInfoTypeDef",
    {
        "ActiveOperationArn": str,
        "BrokerNodeGroupInfo": BrokerNodeGroupInfoTypeDef,
        "ClientAuthentication": ClientAuthenticationTypeDef,
        "ClusterArn": str,
        "ClusterName": str,
        "CreationTime": datetime,
        "CurrentBrokerSoftwareInfo": BrokerSoftwareInfoTypeDef,
        "CurrentVersion": str,
        "EncryptionInfo": EncryptionInfoTypeDef,
        "EnhancedMonitoring": Literal["DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER"],
        "OpenMonitoring": OpenMonitoringTypeDef,
        "NumberOfBrokerNodes": int,
        "State": Literal["ACTIVE", "CREATING", "UPDATING", "DELETING", "FAILED"],
        "Tags": Dict[str, str],
        "ZookeeperConnectString": str,
    },
    total=False,
)

DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef", {"ClusterInfo": ClusterInfoTypeDef}, total=False
)

DescribeConfigurationResponseTypeDef = TypedDict(
    "DescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": ConfigurationRevisionTypeDef,
        "Name": str,
    },
    total=False,
)

DescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "DescribeConfigurationRevisionResponseTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "Revision": int,
        "ServerProperties": Union[bytes, IO],
    },
    total=False,
)

GetBootstrapBrokersResponseTypeDef = TypedDict(
    "GetBootstrapBrokersResponseTypeDef",
    {"BootstrapBrokerString": str, "BootstrapBrokerStringTls": str},
    total=False,
)

ListClusterOperationsResponseTypeDef = TypedDict(
    "ListClusterOperationsResponseTypeDef",
    {"ClusterOperationInfoList": List[ClusterOperationInfoTypeDef], "NextToken": str},
    total=False,
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef",
    {"ClusterInfoList": List[ClusterInfoTypeDef], "NextToken": str},
    total=False,
)

ListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ListConfigurationRevisionsResponseTypeDef",
    {"NextToken": str, "Revisions": List[ConfigurationRevisionTypeDef]},
    total=False,
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Arn": str,
        "CreationTime": datetime,
        "Description": str,
        "KafkaVersions": List[str],
        "LatestRevision": ConfigurationRevisionTypeDef,
        "Name": str,
    },
)

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {"Configurations": List[ConfigurationTypeDef], "NextToken": str},
    total=False,
)

BrokerNodeInfoTypeDef = TypedDict(
    "BrokerNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "BrokerId": float,
        "ClientSubnet": str,
        "ClientVpcIpAddress": str,
        "CurrentBrokerSoftwareInfo": BrokerSoftwareInfoTypeDef,
        "Endpoints": List[str],
    },
    total=False,
)

ZookeeperNodeInfoTypeDef = TypedDict(
    "ZookeeperNodeInfoTypeDef",
    {
        "AttachedENIId": str,
        "ClientVpcIpAddress": str,
        "Endpoints": List[str],
        "ZookeeperId": float,
        "ZookeeperVersion": str,
    },
    total=False,
)

NodeInfoTypeDef = TypedDict(
    "NodeInfoTypeDef",
    {
        "AddedToClusterTime": str,
        "BrokerNodeInfo": BrokerNodeInfoTypeDef,
        "InstanceType": str,
        "NodeARN": str,
        "NodeType": Literal["BROKER"],
        "ZookeeperNodeInfo": ZookeeperNodeInfoTypeDef,
    },
    total=False,
)

ListNodesResponseTypeDef = TypedDict(
    "ListNodesResponseTypeDef",
    {"NextToken": str, "NodeInfoList": List[NodeInfoTypeDef]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

JmxExporterInfoTypeDef = TypedDict("JmxExporterInfoTypeDef", {"EnabledInBroker": bool})

NodeExporterInfoTypeDef = TypedDict("NodeExporterInfoTypeDef", {"EnabledInBroker": bool})

PrometheusInfoTypeDef = TypedDict(
    "PrometheusInfoTypeDef",
    {"JmxExporter": JmxExporterInfoTypeDef, "NodeExporter": NodeExporterInfoTypeDef},
    total=False,
)

OpenMonitoringInfoTypeDef = TypedDict(
    "OpenMonitoringInfoTypeDef", {"Prometheus": PrometheusInfoTypeDef}
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateBrokerCountResponseTypeDef = TypedDict(
    "UpdateBrokerCountResponseTypeDef", {"ClusterArn": str, "ClusterOperationArn": str}, total=False
)

UpdateBrokerStorageResponseTypeDef = TypedDict(
    "UpdateBrokerStorageResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)

UpdateClusterConfigurationResponseTypeDef = TypedDict(
    "UpdateClusterConfigurationResponseTypeDef",
    {"ClusterArn": str, "ClusterOperationArn": str},
    total=False,
)

UpdateMonitoringResponseTypeDef = TypedDict(
    "UpdateMonitoringResponseTypeDef", {"ClusterArn": str, "ClusterOperationArn": str}, total=False
)
