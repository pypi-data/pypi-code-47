"""
Main interface for docdb service client

Usage::

    import boto3
    from mypy_boto3.docdb import DocDBClient

    session = boto3.Session()

    client: DocDBClient = boto3.client("docdb")
    session_client: DocDBClient = session.client("docdb")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from __future__ import annotations

from datetime import datetime
import sys
from typing import Any, Dict, List, overload
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_docdb.client as client_scope

# pylint: disable=import-self
import mypy_boto3_docdb.paginator as paginator_scope
from mypy_boto3_docdb.type_defs import (
    ApplyPendingMaintenanceActionResultTypeDef,
    CertificateMessageTypeDef,
    CloudwatchLogsExportConfigurationTypeDef,
    CopyDBClusterParameterGroupResultTypeDef,
    CopyDBClusterSnapshotResultTypeDef,
    CreateDBClusterParameterGroupResultTypeDef,
    CreateDBClusterResultTypeDef,
    CreateDBClusterSnapshotResultTypeDef,
    CreateDBInstanceResultTypeDef,
    CreateDBSubnetGroupResultTypeDef,
    DBClusterMessageTypeDef,
    DBClusterParameterGroupDetailsTypeDef,
    DBClusterParameterGroupNameMessageTypeDef,
    DBClusterParameterGroupsMessageTypeDef,
    DBClusterSnapshotMessageTypeDef,
    DBEngineVersionMessageTypeDef,
    DBInstanceMessageTypeDef,
    DBSubnetGroupMessageTypeDef,
    DeleteDBClusterResultTypeDef,
    DeleteDBClusterSnapshotResultTypeDef,
    DeleteDBInstanceResultTypeDef,
    DescribeDBClusterSnapshotAttributesResultTypeDef,
    DescribeEngineDefaultClusterParametersResultTypeDef,
    EventCategoriesMessageTypeDef,
    EventsMessageTypeDef,
    FailoverDBClusterResultTypeDef,
    FilterTypeDef,
    ModifyDBClusterResultTypeDef,
    ModifyDBClusterSnapshotAttributeResultTypeDef,
    ModifyDBInstanceResultTypeDef,
    ModifyDBSubnetGroupResultTypeDef,
    OrderableDBInstanceOptionsMessageTypeDef,
    ParameterTypeDef,
    PendingMaintenanceActionsMessageTypeDef,
    RebootDBInstanceResultTypeDef,
    RestoreDBClusterFromSnapshotResultTypeDef,
    RestoreDBClusterToPointInTimeResultTypeDef,
    StartDBClusterResultTypeDef,
    StopDBClusterResultTypeDef,
    TagListMessageTypeDef,
    TagTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_docdb.waiter as waiter_scope

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DocDBClient",)


class DocDBClient(BaseClient):
    """
    [DocDB.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client)
    """

    exceptions: client_scope.Exceptions

    def add_tags_to_resource(self, ResourceName: str, Tags: List[TagTypeDef]) -> None:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, ResourceIdentifier: str, ApplyAction: str, OptInType: str
    ) -> ApplyPendingMaintenanceActionResultTypeDef:
        """
        [Client.apply_pending_maintenance_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.apply_pending_maintenance_action)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.can_paginate)
        """

    def copy_db_cluster_parameter_group(
        self,
        SourceDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupIdentifier: str,
        TargetDBClusterParameterGroupDescription: str,
        Tags: List[TagTypeDef] = None,
    ) -> CopyDBClusterParameterGroupResultTypeDef:
        """
        [Client.copy_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.copy_db_cluster_parameter_group)
        """

    def copy_db_cluster_snapshot(
        self,
        SourceDBClusterSnapshotIdentifier: str,
        TargetDBClusterSnapshotIdentifier: str,
        KmsKeyId: str = None,
        PreSignedUrl: str = None,
        CopyTags: bool = None,
        Tags: List[TagTypeDef] = None,
    ) -> CopyDBClusterSnapshotResultTypeDef:
        """
        [Client.copy_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.copy_db_cluster_snapshot)
        """

    def create_db_cluster(
        self,
        DBClusterIdentifier: str,
        Engine: str,
        MasterUsername: str,
        MasterUserPassword: str,
        AvailabilityZones: List[str] = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        DBSubnetGroupName: str = None,
        EngineVersion: str = None,
        Port: int = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        Tags: List[TagTypeDef] = None,
        StorageEncrypted: bool = None,
        KmsKeyId: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
    ) -> CreateDBClusterResultTypeDef:
        """
        [Client.create_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.create_db_cluster)
        """

    def create_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        DBParameterGroupFamily: str,
        Description: str,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDBClusterParameterGroupResultTypeDef:
        """
        [Client.create_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.create_db_cluster_parameter_group)
        """

    def create_db_cluster_snapshot(
        self,
        DBClusterSnapshotIdentifier: str,
        DBClusterIdentifier: str,
        Tags: List[TagTypeDef] = None,
    ) -> CreateDBClusterSnapshotResultTypeDef:
        """
        [Client.create_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.create_db_cluster_snapshot)
        """

    def create_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str,
        Engine: str,
        DBClusterIdentifier: str,
        AvailabilityZone: str = None,
        PreferredMaintenanceWindow: str = None,
        AutoMinorVersionUpgrade: bool = None,
        Tags: List[TagTypeDef] = None,
        PromotionTier: int = None,
    ) -> CreateDBInstanceResultTypeDef:
        """
        [Client.create_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.create_db_instance)
        """

    def create_db_subnet_group(
        self,
        DBSubnetGroupName: str,
        DBSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List[TagTypeDef] = None,
    ) -> CreateDBSubnetGroupResultTypeDef:
        """
        [Client.create_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.create_db_subnet_group)
        """

    def delete_db_cluster(
        self,
        DBClusterIdentifier: str,
        SkipFinalSnapshot: bool = None,
        FinalDBSnapshotIdentifier: str = None,
    ) -> DeleteDBClusterResultTypeDef:
        """
        [Client.delete_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.delete_db_cluster)
        """

    def delete_db_cluster_parameter_group(self, DBClusterParameterGroupName: str) -> None:
        """
        [Client.delete_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.delete_db_cluster_parameter_group)
        """

    def delete_db_cluster_snapshot(
        self, DBClusterSnapshotIdentifier: str
    ) -> DeleteDBClusterSnapshotResultTypeDef:
        """
        [Client.delete_db_cluster_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.delete_db_cluster_snapshot)
        """

    def delete_db_instance(self, DBInstanceIdentifier: str) -> DeleteDBInstanceResultTypeDef:
        """
        [Client.delete_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.delete_db_instance)
        """

    def delete_db_subnet_group(self, DBSubnetGroupName: str) -> None:
        """
        [Client.delete_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.delete_db_subnet_group)
        """

    def describe_certificates(
        self,
        CertificateIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> CertificateMessageTypeDef:
        """
        [Client.describe_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_certificates)
        """

    def describe_db_cluster_parameter_groups(
        self,
        DBClusterParameterGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterParameterGroupsMessageTypeDef:
        """
        [Client.describe_db_cluster_parameter_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_db_cluster_parameter_groups)
        """

    def describe_db_cluster_parameters(
        self,
        DBClusterParameterGroupName: str,
        Source: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterParameterGroupDetailsTypeDef:
        """
        [Client.describe_db_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_db_cluster_parameters)
        """

    def describe_db_cluster_snapshot_attributes(
        self, DBClusterSnapshotIdentifier: str
    ) -> DescribeDBClusterSnapshotAttributesResultTypeDef:
        """
        [Client.describe_db_cluster_snapshot_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_db_cluster_snapshot_attributes)
        """

    def describe_db_cluster_snapshots(
        self,
        DBClusterIdentifier: str = None,
        DBClusterSnapshotIdentifier: str = None,
        SnapshotType: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        IncludeShared: bool = None,
        IncludePublic: bool = None,
    ) -> DBClusterSnapshotMessageTypeDef:
        """
        [Client.describe_db_cluster_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_db_cluster_snapshots)
        """

    def describe_db_clusters(
        self,
        DBClusterIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBClusterMessageTypeDef:
        """
        [Client.describe_db_clusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_db_clusters)
        """

    def describe_db_engine_versions(
        self,
        Engine: str = None,
        EngineVersion: str = None,
        DBParameterGroupFamily: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        DefaultOnly: bool = None,
        ListSupportedCharacterSets: bool = None,
        ListSupportedTimezones: bool = None,
    ) -> DBEngineVersionMessageTypeDef:
        """
        [Client.describe_db_engine_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_db_engine_versions)
        """

    def describe_db_instances(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBInstanceMessageTypeDef:
        """
        [Client.describe_db_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_db_instances)
        """

    def describe_db_subnet_groups(
        self,
        DBSubnetGroupName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DBSubnetGroupMessageTypeDef:
        """
        [Client.describe_db_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_db_subnet_groups)
        """

    def describe_engine_default_cluster_parameters(
        self,
        DBParameterGroupFamily: str,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeEngineDefaultClusterParametersResultTypeDef:
        """
        [Client.describe_engine_default_cluster_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_engine_default_cluster_parameters)
        """

    def describe_event_categories(
        self, SourceType: str = None, Filters: List[FilterTypeDef] = None
    ) -> EventCategoriesMessageTypeDef:
        """
        [Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_event_categories)
        """

    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal[
            "db-instance",
            "db-parameter-group",
            "db-security-group",
            "db-snapshot",
            "db-cluster",
            "db-cluster-snapshot",
        ] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> EventsMessageTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_events)
        """

    def describe_orderable_db_instance_options(
        self,
        Engine: str,
        EngineVersion: str = None,
        DBInstanceClass: str = None,
        LicenseModel: str = None,
        Vpc: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> OrderableDBInstanceOptionsMessageTypeDef:
        """
        [Client.describe_orderable_db_instance_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_orderable_db_instance_options)
        """

    def describe_pending_maintenance_actions(
        self,
        ResourceIdentifier: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> PendingMaintenanceActionsMessageTypeDef:
        """
        [Client.describe_pending_maintenance_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.describe_pending_maintenance_actions)
        """

    def failover_db_cluster(
        self, DBClusterIdentifier: str = None, TargetDBInstanceIdentifier: str = None
    ) -> FailoverDBClusterResultTypeDef:
        """
        [Client.failover_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.failover_db_cluster)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.generate_presigned_url)
        """

    def list_tags_for_resource(
        self, ResourceName: str, Filters: List[FilterTypeDef] = None
    ) -> TagListMessageTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.list_tags_for_resource)
        """

    def modify_db_cluster(
        self,
        DBClusterIdentifier: str,
        NewDBClusterIdentifier: str = None,
        ApplyImmediately: bool = None,
        BackupRetentionPeriod: int = None,
        DBClusterParameterGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Port: int = None,
        MasterUserPassword: str = None,
        PreferredBackupWindow: str = None,
        PreferredMaintenanceWindow: str = None,
        CloudwatchLogsExportConfiguration: CloudwatchLogsExportConfigurationTypeDef = None,
        EngineVersion: str = None,
        DeletionProtection: bool = None,
    ) -> ModifyDBClusterResultTypeDef:
        """
        [Client.modify_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.modify_db_cluster)
        """

    def modify_db_cluster_parameter_group(
        self, DBClusterParameterGroupName: str, Parameters: List[ParameterTypeDef]
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        [Client.modify_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.modify_db_cluster_parameter_group)
        """

    def modify_db_cluster_snapshot_attribute(
        self,
        DBClusterSnapshotIdentifier: str,
        AttributeName: str,
        ValuesToAdd: List[str] = None,
        ValuesToRemove: List[str] = None,
    ) -> ModifyDBClusterSnapshotAttributeResultTypeDef:
        """
        [Client.modify_db_cluster_snapshot_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.modify_db_cluster_snapshot_attribute)
        """

    def modify_db_instance(
        self,
        DBInstanceIdentifier: str,
        DBInstanceClass: str = None,
        ApplyImmediately: bool = None,
        PreferredMaintenanceWindow: str = None,
        AutoMinorVersionUpgrade: bool = None,
        NewDBInstanceIdentifier: str = None,
        CACertificateIdentifier: str = None,
        PromotionTier: int = None,
    ) -> ModifyDBInstanceResultTypeDef:
        """
        [Client.modify_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.modify_db_instance)
        """

    def modify_db_subnet_group(
        self, DBSubnetGroupName: str, SubnetIds: List[str], DBSubnetGroupDescription: str = None
    ) -> ModifyDBSubnetGroupResultTypeDef:
        """
        [Client.modify_db_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.modify_db_subnet_group)
        """

    def reboot_db_instance(
        self, DBInstanceIdentifier: str, ForceFailover: bool = None
    ) -> RebootDBInstanceResultTypeDef:
        """
        [Client.reboot_db_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.reboot_db_instance)
        """

    def remove_tags_from_resource(self, ResourceName: str, TagKeys: List[str]) -> None:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.remove_tags_from_resource)
        """

    def reset_db_cluster_parameter_group(
        self,
        DBClusterParameterGroupName: str,
        ResetAllParameters: bool = None,
        Parameters: List[ParameterTypeDef] = None,
    ) -> DBClusterParameterGroupNameMessageTypeDef:
        """
        [Client.reset_db_cluster_parameter_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.reset_db_cluster_parameter_group)
        """

    def restore_db_cluster_from_snapshot(
        self,
        DBClusterIdentifier: str,
        SnapshotIdentifier: str,
        Engine: str,
        AvailabilityZones: List[str] = None,
        EngineVersion: str = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List[TagTypeDef] = None,
        KmsKeyId: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
    ) -> RestoreDBClusterFromSnapshotResultTypeDef:
        """
        [Client.restore_db_cluster_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.restore_db_cluster_from_snapshot)
        """

    def restore_db_cluster_to_point_in_time(
        self,
        DBClusterIdentifier: str,
        SourceDBClusterIdentifier: str,
        RestoreToTime: datetime = None,
        UseLatestRestorableTime: bool = None,
        Port: int = None,
        DBSubnetGroupName: str = None,
        VpcSecurityGroupIds: List[str] = None,
        Tags: List[TagTypeDef] = None,
        KmsKeyId: str = None,
        EnableCloudwatchLogsExports: List[str] = None,
        DeletionProtection: bool = None,
    ) -> RestoreDBClusterToPointInTimeResultTypeDef:
        """
        [Client.restore_db_cluster_to_point_in_time documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.restore_db_cluster_to_point_in_time)
        """

    def start_db_cluster(self, DBClusterIdentifier: str) -> StartDBClusterResultTypeDef:
        """
        [Client.start_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.start_db_cluster)
        """

    def stop_db_cluster(self, DBClusterIdentifier: str) -> StopDBClusterResultTypeDef:
        """
        [Client.stop_db_cluster documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Client.stop_db_cluster)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_clusters"]
    ) -> paginator_scope.DescribeDBClustersPaginator:
        """
        [Paginator.DescribeDBClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Paginator.DescribeDBClusters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_engine_versions"]
    ) -> paginator_scope.DescribeDBEngineVersionsPaginator:
        """
        [Paginator.DescribeDBEngineVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Paginator.DescribeDBEngineVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_instances"]
    ) -> paginator_scope.DescribeDBInstancesPaginator:
        """
        [Paginator.DescribeDBInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Paginator.DescribeDBInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_db_subnet_groups"]
    ) -> paginator_scope.DescribeDBSubnetGroupsPaginator:
        """
        [Paginator.DescribeDBSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Paginator.DescribeDBSubnetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_events"]
    ) -> paginator_scope.DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_db_instance_options"]
    ) -> paginator_scope.DescribeOrderableDBInstanceOptionsPaginator:
        """
        [Paginator.DescribeOrderableDBInstanceOptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Paginator.DescribeOrderableDBInstanceOptions)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_instance_available"]
    ) -> waiter_scope.DBInstanceAvailableWaiter:
        """
        [Waiter.DBInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Waiter.DBInstanceAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["db_instance_deleted"]
    ) -> waiter_scope.DBInstanceDeletedWaiter:
        """
        [Waiter.DBInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.49/reference/services/docdb.html#DocDB.Waiter.DBInstanceDeleted)
        """


class Exceptions:
    AuthorizationNotFoundFault: Boto3ClientError
    CertificateNotFoundFault: Boto3ClientError
    ClientError: Boto3ClientError
    DBClusterAlreadyExistsFault: Boto3ClientError
    DBClusterNotFoundFault: Boto3ClientError
    DBClusterParameterGroupNotFoundFault: Boto3ClientError
    DBClusterQuotaExceededFault: Boto3ClientError
    DBClusterSnapshotAlreadyExistsFault: Boto3ClientError
    DBClusterSnapshotNotFoundFault: Boto3ClientError
    DBInstanceAlreadyExistsFault: Boto3ClientError
    DBInstanceNotFoundFault: Boto3ClientError
    DBParameterGroupAlreadyExistsFault: Boto3ClientError
    DBParameterGroupNotFoundFault: Boto3ClientError
    DBParameterGroupQuotaExceededFault: Boto3ClientError
    DBSecurityGroupNotFoundFault: Boto3ClientError
    DBSnapshotAlreadyExistsFault: Boto3ClientError
    DBSnapshotNotFoundFault: Boto3ClientError
    DBSubnetGroupAlreadyExistsFault: Boto3ClientError
    DBSubnetGroupDoesNotCoverEnoughAZs: Boto3ClientError
    DBSubnetGroupNotFoundFault: Boto3ClientError
    DBSubnetGroupQuotaExceededFault: Boto3ClientError
    DBSubnetQuotaExceededFault: Boto3ClientError
    DBUpgradeDependencyFailureFault: Boto3ClientError
    InstanceQuotaExceededFault: Boto3ClientError
    InsufficientDBClusterCapacityFault: Boto3ClientError
    InsufficientDBInstanceCapacityFault: Boto3ClientError
    InsufficientStorageClusterCapacityFault: Boto3ClientError
    InvalidDBClusterSnapshotStateFault: Boto3ClientError
    InvalidDBClusterStateFault: Boto3ClientError
    InvalidDBInstanceStateFault: Boto3ClientError
    InvalidDBParameterGroupStateFault: Boto3ClientError
    InvalidDBSecurityGroupStateFault: Boto3ClientError
    InvalidDBSnapshotStateFault: Boto3ClientError
    InvalidDBSubnetGroupStateFault: Boto3ClientError
    InvalidDBSubnetStateFault: Boto3ClientError
    InvalidRestoreFault: Boto3ClientError
    InvalidSubnet: Boto3ClientError
    InvalidVPCNetworkStateFault: Boto3ClientError
    KMSKeyNotAccessibleFault: Boto3ClientError
    ResourceNotFoundFault: Boto3ClientError
    SharedSnapshotQuotaExceededFault: Boto3ClientError
    SnapshotQuotaExceededFault: Boto3ClientError
    StorageQuotaExceededFault: Boto3ClientError
    StorageTypeNotSupportedFault: Boto3ClientError
    SubnetAlreadyInUse: Boto3ClientError
