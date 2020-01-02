"""
Main interface for mgh service.

Usage::

    import boto3
    from mypy_boto3.mgh import (
        Client,
        ListCreatedArtifactsPaginator,
        ListDiscoveredResourcesPaginator,
        ListMigrationTasksPaginator,
        ListProgressUpdateStreamsPaginator,
        MigrationHubClient,
        )

    session = boto3.Session()

    client: MigrationHubClient = boto3.client("mgh")
    session_client: MigrationHubClient = session.client("mgh")

    list_created_artifacts_paginator: ListCreatedArtifactsPaginator = client.get_paginator("list_created_artifacts")
    list_discovered_resources_paginator: ListDiscoveredResourcesPaginator = client.get_paginator("list_discovered_resources")
    list_migration_tasks_paginator: ListMigrationTasksPaginator = client.get_paginator("list_migration_tasks")
    list_progress_update_streams_paginator: ListProgressUpdateStreamsPaginator = client.get_paginator("list_progress_update_streams")
"""
from mypy_boto3_mgh.client import MigrationHubClient as Client, MigrationHubClient
from mypy_boto3_mgh.paginator import (
    ListCreatedArtifactsPaginator,
    ListDiscoveredResourcesPaginator,
    ListMigrationTasksPaginator,
    ListProgressUpdateStreamsPaginator,
)


__all__ = (
    "Client",
    "ListCreatedArtifactsPaginator",
    "ListDiscoveredResourcesPaginator",
    "ListMigrationTasksPaginator",
    "ListProgressUpdateStreamsPaginator",
    "MigrationHubClient",
)
