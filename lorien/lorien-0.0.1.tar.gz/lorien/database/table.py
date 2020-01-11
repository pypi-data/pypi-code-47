"""
The module to interact with DynamoDB.
"""
from typing import List

import boto3

from ..logger import get_logger

log = get_logger('Database')

TABLE_NAME_FORMAT = '{lib}-{target}'


def create_table(lib_name: str, target: str, **db_kwargs) -> str:
    """Create an empty table in the DynamoDB.

    Parameters
    ----------
    lib_name: str
        The library name (e.g., TOPI).

    target: str
        The TVM target (e.g., llvm, cuda)

    **db_kwargs
        The kwargs of boto3 client. Commonly used: "region_name='us-west-1'"
        or "endpoint_url=http://localhost:8000".

    Returns
    -------
    table_name: str
        The created table name.
    """
    table_name = TABLE_NAME_FORMAT.format(lib=lib_name, target=target)
    # Key attributes in the table.
    attrs = [{
        "AttributeName": "Platform",
        "AttributeType": "S"
    }, {
        "AttributeName": "PrimaryRangeKey",
        "AttributeType": "S"
    }, {
        "AttributeName": "OpShapePropertiesDTypes",
        "AttributeType": "S"
    }]

    key_schema = [{
        "AttributeName": "Platform",
        "KeyType": "HASH"
    }, {
        "AttributeName": "PrimaryRangeKey",
        "KeyType": "RANGE"
    }]

    local_secondary_indexes = [{
        "IndexName":
        "OpShapePropertiesDTypesIndex",
        "KeySchema": [{
            "AttributeName": "Platform",
            "KeyType": "HASH"
        }, {
            "AttributeName": "OpShapePropertiesDTypes",
            "KeyType": "RANGE"
        }],
        "Projection": {
            "ProjectionType": "ALL"
        },
    }]

    try:
        client = boto3.client('dynamodb', **db_kwargs)
        client.create_table(TableName=table_name,
                            AttributeDefinitions=attrs,
                            KeySchema=key_schema,
                            LocalSecondaryIndexes=local_secondary_indexes,
                            ProvisionedThroughput={
                                "ReadCapacityUnits": 100,
                                "WriteCapacityUnits": 10
                            })
        log.info('Table %s created successfully', table_name)
        return table_name
    except Exception as err:  # pylint:disable=broad-except
        raise RuntimeError('Error creating table %s: %s' % (table_name, str(err)))


def delete_table(table_name: str, **db_kwargs) -> None:
    """Delete the given table in the database.

    Parameters
    ----------
    table_name: str
        The table name in string.

    **db_kwargs
        The kwargs of boto3 client. Commonly used: "region_name='us-west-1'"
        or "endpoint_url=http://localhost:8000".
    """
    try:
        client = boto3.client('dynamodb', **db_kwargs)
        client.delete_table(TableName=table_name)
        log.info('Table %s has been deleted', table_name)
    except Exception as err:  # pylint:disable=broad-except
        log.error('Failed to delete table %s: %s', table_name, str(err))


def list_tables(prefix: str = '', **db_kwargs) -> List[str]:
    """List all table names in the database.

    Parameters
    ----------
    prefix: str
        The prefix of table names. Empty means all.

    **db_kwargs
        The kwargs of boto3 client. Commonly used: "region_name='us-west-1'"
        or "endpoint_url=http://localhost:8000".

    Returns
    -------
    tables: List[str]
        A list of sorted table names.
    """
    try:
        client = boto3.client('dynamodb', **db_kwargs)
        table_names = [
            name for name in sorted(client.list_tables()['TableNames'], reverse=True)
            if not prefix or name.startswith(prefix)
        ]
    except Exception as err:  # pylint:disable=broad-except
        raise RuntimeError('Failed to fetch the table list: %s' % str(err))

    return table_names
