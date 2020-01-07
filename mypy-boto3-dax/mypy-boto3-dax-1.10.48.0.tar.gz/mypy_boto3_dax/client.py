"""
Main interface for dax service client

Usage::

    import boto3
    from mypy_boto3.dax import DAXClient

    session = boto3.Session()

    client: DAXClient = boto3.client("dax")
    session_client: DAXClient = session.client("dax")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_dax.client as client_scope

# pylint: disable=import-self
import mypy_boto3_dax.paginator as paginator_scope
from mypy_boto3_dax.type_defs import (
    CreateClusterResponseTypeDef,
    CreateParameterGroupResponseTypeDef,
    CreateSubnetGroupResponseTypeDef,
    DecreaseReplicationFactorResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteParameterGroupResponseTypeDef,
    DeleteSubnetGroupResponseTypeDef,
    DescribeClustersResponseTypeDef,
    DescribeDefaultParametersResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeParameterGroupsResponseTypeDef,
    DescribeParametersResponseTypeDef,
    DescribeSubnetGroupsResponseTypeDef,
    IncreaseReplicationFactorResponseTypeDef,
    ListTagsResponseTypeDef,
    ParameterNameValueTypeDef,
    RebootNodeResponseTypeDef,
    SSESpecificationTypeDef,
    TagResourceResponseTypeDef,
    TagTypeDef,
    UntagResourceResponseTypeDef,
    UpdateClusterResponseTypeDef,
    UpdateParameterGroupResponseTypeDef,
    UpdateSubnetGroupResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DAXClient",)


class DAXClient(BaseClient):
    """
    [DAX.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client)
    """

    exceptions: client_scope.Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.can_paginate)
        """

    def create_cluster(
        self,
        ClusterName: str,
        NodeType: str,
        ReplicationFactor: int,
        IamRoleArn: str,
        Description: str = None,
        AvailabilityZones: List[str] = None,
        SubnetGroupName: str = None,
        SecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        ParameterGroupName: str = None,
        Tags: List[TagTypeDef] = None,
        SSESpecification: SSESpecificationTypeDef = None,
    ) -> CreateClusterResponseTypeDef:
        """
        [Client.create_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.create_cluster)
        """

    def create_parameter_group(
        self, ParameterGroupName: str, Description: str = None
    ) -> CreateParameterGroupResponseTypeDef:
        """
        [Client.create_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.create_parameter_group)
        """

    def create_subnet_group(
        self, SubnetGroupName: str, SubnetIds: List[str], Description: str = None
    ) -> CreateSubnetGroupResponseTypeDef:
        """
        [Client.create_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.create_subnet_group)
        """

    def decrease_replication_factor(
        self,
        ClusterName: str,
        NewReplicationFactor: int,
        AvailabilityZones: List[str] = None,
        NodeIdsToRemove: List[str] = None,
    ) -> DecreaseReplicationFactorResponseTypeDef:
        """
        [Client.decrease_replication_factor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.decrease_replication_factor)
        """

    def delete_cluster(self, ClusterName: str) -> DeleteClusterResponseTypeDef:
        """
        [Client.delete_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.delete_cluster)
        """

    def delete_parameter_group(
        self, ParameterGroupName: str
    ) -> DeleteParameterGroupResponseTypeDef:
        """
        [Client.delete_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.delete_parameter_group)
        """

    def delete_subnet_group(self, SubnetGroupName: str) -> DeleteSubnetGroupResponseTypeDef:
        """
        [Client.delete_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.delete_subnet_group)
        """

    def describe_clusters(
        self, ClusterNames: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeClustersResponseTypeDef:
        """
        [Client.describe_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.describe_clusters)
        """

    def describe_default_parameters(
        self, MaxResults: int = None, NextToken: str = None
    ) -> DescribeDefaultParametersResponseTypeDef:
        """
        [Client.describe_default_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.describe_default_parameters)
        """

    def describe_events(
        self,
        SourceName: str = None,
        SourceType: Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.describe_events)
        """

    def describe_parameter_groups(
        self, ParameterGroupNames: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeParameterGroupsResponseTypeDef:
        """
        [Client.describe_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.describe_parameter_groups)
        """

    def describe_parameters(
        self,
        ParameterGroupName: str,
        Source: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeParametersResponseTypeDef:
        """
        [Client.describe_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.describe_parameters)
        """

    def describe_subnet_groups(
        self, SubnetGroupNames: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeSubnetGroupsResponseTypeDef:
        """
        [Client.describe_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.describe_subnet_groups)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.generate_presigned_url)
        """

    def increase_replication_factor(
        self, ClusterName: str, NewReplicationFactor: int, AvailabilityZones: List[str] = None
    ) -> IncreaseReplicationFactorResponseTypeDef:
        """
        [Client.increase_replication_factor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.increase_replication_factor)
        """

    def list_tags(self, ResourceName: str, NextToken: str = None) -> ListTagsResponseTypeDef:
        """
        [Client.list_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.list_tags)
        """

    def reboot_node(self, ClusterName: str, NodeId: str) -> RebootNodeResponseTypeDef:
        """
        [Client.reboot_node documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.reboot_node)
        """

    def tag_resource(self, ResourceName: str, Tags: List[TagTypeDef]) -> TagResourceResponseTypeDef:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.tag_resource)
        """

    def untag_resource(self, ResourceName: str, TagKeys: List[str]) -> UntagResourceResponseTypeDef:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.untag_resource)
        """

    def update_cluster(
        self,
        ClusterName: str,
        Description: str = None,
        PreferredMaintenanceWindow: str = None,
        NotificationTopicArn: str = None,
        NotificationTopicStatus: str = None,
        ParameterGroupName: str = None,
        SecurityGroupIds: List[str] = None,
    ) -> UpdateClusterResponseTypeDef:
        """
        [Client.update_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.update_cluster)
        """

    def update_parameter_group(
        self, ParameterGroupName: str, ParameterNameValues: List[ParameterNameValueTypeDef]
    ) -> UpdateParameterGroupResponseTypeDef:
        """
        [Client.update_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.update_parameter_group)
        """

    def update_subnet_group(
        self, SubnetGroupName: str, Description: str = None, SubnetIds: List[str] = None
    ) -> UpdateSubnetGroupResponseTypeDef:
        """
        [Client.update_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Client.update_subnet_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_clusters"]
    ) -> paginator_scope.DescribeClustersPaginator:
        """
        [Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Paginator.DescribeClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_default_parameters"]
    ) -> paginator_scope.DescribeDefaultParametersPaginator:
        """
        [Paginator.DescribeDefaultParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Paginator.DescribeDefaultParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> paginator_scope.DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_parameter_groups"]
    ) -> paginator_scope.DescribeParameterGroupsPaginator:
        """
        [Paginator.DescribeParameterGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Paginator.DescribeParameterGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_parameters"]
    ) -> paginator_scope.DescribeParametersPaginator:
        """
        [Paginator.DescribeParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Paginator.DescribeParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subnet_groups"]
    ) -> paginator_scope.DescribeSubnetGroupsPaginator:
        """
        [Paginator.DescribeSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Paginator.DescribeSubnetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags"]
    ) -> paginator_scope.ListTagsPaginator:
        """
        [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.48/reference/services/dax.html#DAX.Paginator.ListTags)
        """


class Exceptions:
    ClientError: Boto3ClientError
    ClusterAlreadyExistsFault: Boto3ClientError
    ClusterNotFoundFault: Boto3ClientError
    ClusterQuotaForCustomerExceededFault: Boto3ClientError
    InsufficientClusterCapacityFault: Boto3ClientError
    InvalidARNFault: Boto3ClientError
    InvalidClusterStateFault: Boto3ClientError
    InvalidParameterCombinationException: Boto3ClientError
    InvalidParameterGroupStateFault: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidSubnet: Boto3ClientError
    InvalidVPCNetworkStateFault: Boto3ClientError
    NodeNotFoundFault: Boto3ClientError
    NodeQuotaForClusterExceededFault: Boto3ClientError
    NodeQuotaForCustomerExceededFault: Boto3ClientError
    ParameterGroupAlreadyExistsFault: Boto3ClientError
    ParameterGroupNotFoundFault: Boto3ClientError
    ParameterGroupQuotaExceededFault: Boto3ClientError
    ServiceLinkedRoleNotFoundFault: Boto3ClientError
    SubnetGroupAlreadyExistsFault: Boto3ClientError
    SubnetGroupInUseFault: Boto3ClientError
    SubnetGroupNotFoundFault: Boto3ClientError
    SubnetGroupQuotaExceededFault: Boto3ClientError
    SubnetInUse: Boto3ClientError
    SubnetQuotaExceededFault: Boto3ClientError
    TagNotFoundFault: Boto3ClientError
    TagQuotaPerResourceExceeded: Boto3ClientError
