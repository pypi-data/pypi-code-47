"""
Main interface for kafka service.

Usage::

    import boto3
    from mypy_boto3.kafka import (
        Client,
        KafkaClient,
        ListClusterOperationsPaginator,
        ListClustersPaginator,
        ListConfigurationRevisionsPaginator,
        ListConfigurationsPaginator,
        ListNodesPaginator,
        )

    session = boto3.Session()

    client: KafkaClient = boto3.client("kafka")
    session_client: KafkaClient = session.client("kafka")

    list_cluster_operations_paginator: ListClusterOperationsPaginator = client.get_paginator("list_cluster_operations")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_configuration_revisions_paginator: ListConfigurationRevisionsPaginator = client.get_paginator("list_configuration_revisions")
    list_configurations_paginator: ListConfigurationsPaginator = client.get_paginator("list_configurations")
    list_nodes_paginator: ListNodesPaginator = client.get_paginator("list_nodes")
"""
from mypy_boto3_kafka.client import KafkaClient as Client, KafkaClient
from mypy_boto3_kafka.paginator import (
    ListClusterOperationsPaginator,
    ListClustersPaginator,
    ListConfigurationRevisionsPaginator,
    ListConfigurationsPaginator,
    ListNodesPaginator,
)


__all__ = (
    "Client",
    "KafkaClient",
    "ListClusterOperationsPaginator",
    "ListClustersPaginator",
    "ListConfigurationRevisionsPaginator",
    "ListConfigurationsPaginator",
    "ListNodesPaginator",
)
