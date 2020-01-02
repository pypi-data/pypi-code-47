"""
Main interface for mgh service client paginators.

Usage::

    import boto3
    from mypy_boto3.mgh import (
        ListCreatedArtifactsPaginator,
        ListDiscoveredResourcesPaginator,
        ListMigrationTasksPaginator,
        ListProgressUpdateStreamsPaginator,
    )

    client: MigrationHubClient = boto3.client("mgh")

    list_created_artifacts_paginator: ListCreatedArtifactsPaginator = client.get_paginator("list_created_artifacts")
    list_discovered_resources_paginator: ListDiscoveredResourcesPaginator = client.get_paginator("list_discovered_resources")
    list_migration_tasks_paginator: ListMigrationTasksPaginator = client.get_paginator("list_migration_tasks")
    list_progress_update_streams_paginator: ListProgressUpdateStreamsPaginator = client.get_paginator("list_progress_update_streams")
"""
# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
from __future__ import annotations

from typing import Generator
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mgh.type_defs import (
    ListCreatedArtifactsResultTypeDef,
    ListDiscoveredResourcesResultTypeDef,
    ListMigrationTasksResultTypeDef,
    ListProgressUpdateStreamsResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListCreatedArtifactsPaginator",
    "ListDiscoveredResourcesPaginator",
    "ListMigrationTasksPaginator",
    "ListProgressUpdateStreamsPaginator",
)


class ListCreatedArtifactsPaginator(Boto3Paginator):
    """
    [Paginator.ListCreatedArtifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.46/reference/services/mgh.html#MigrationHub.Paginator.ListCreatedArtifacts)
    """

    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListCreatedArtifactsResultTypeDef, None, None]:
        """
        [ListCreatedArtifacts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.46/reference/services/mgh.html#MigrationHub.Paginator.ListCreatedArtifacts.paginate)
        """


class ListDiscoveredResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListDiscoveredResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.46/reference/services/mgh.html#MigrationHub.Paginator.ListDiscoveredResources)
    """

    def paginate(
        self,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Generator[ListDiscoveredResourcesResultTypeDef, None, None]:
        """
        [ListDiscoveredResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.46/reference/services/mgh.html#MigrationHub.Paginator.ListDiscoveredResources.paginate)
        """


class ListMigrationTasksPaginator(Boto3Paginator):
    """
    [Paginator.ListMigrationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.46/reference/services/mgh.html#MigrationHub.Paginator.ListMigrationTasks)
    """

    def paginate(
        self, ResourceName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListMigrationTasksResultTypeDef, None, None]:
        """
        [ListMigrationTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.46/reference/services/mgh.html#MigrationHub.Paginator.ListMigrationTasks.paginate)
        """


class ListProgressUpdateStreamsPaginator(Boto3Paginator):
    """
    [Paginator.ListProgressUpdateStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.46/reference/services/mgh.html#MigrationHub.Paginator.ListProgressUpdateStreams)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Generator[ListProgressUpdateStreamsResultTypeDef, None, None]:
        """
        [ListProgressUpdateStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.46/reference/services/mgh.html#MigrationHub.Paginator.ListProgressUpdateStreams.paginate)
        """
