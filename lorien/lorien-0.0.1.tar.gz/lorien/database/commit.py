"""
The module of committing to the database.
"""
import os
from typing import Dict, Optional, Tuple

import boto3
import botocore
import numpy as np

from tvm.autotvm.measure import MeasureInput, MeasureResult
from tvm.autotvm.record import encode, load_from_file
from tvm.autotvm.task import create

from ..logger import get_logger
from .query import query_table_by_targets
from .util import (convert_to_db_list, gen_primary_key, parse_target)

log = get_logger('DB-Commit')


def commit_single_record(record: Tuple[MeasureInput, MeasureResult],
                         table_name: str,
                         log_file_name: Optional[str] = None,
                         tvm_commit: Optional[str] = None,
                         **db_kwargs):
    """Commit a single record to the database.
    If the record exists, then the best config will be appended.

    Parameters
    ----------
    record: Tuple[MeasureInput, MeasureResult]
        The record to be committed.

    table_name: str
        The table name to commit.

    log_file_name: Optional[str]
        The tuning log name contains this record.

    tvm_commit: str
        The TVM commit used for generating this record.

    **db_kwargs
        The kwargs of boto3 client. Commonly used: "region_name='us-west-1'"
        or "endpoint_url=http://localhost:8000".
    """
    # Generate necessary fields for commit.
    _, platform = parse_target(str(record[0].target))
    primary_range_key = gen_primary_key(record[0].task)

    # The temp task is only used for computing FLOPS
    temp_task = create(record[0].task.name,
                       record[0].task.args,
                       record[0].target,
                       template_key=record[0].config.template_key)
    gflops = temp_task.flop / 1e9
    thrpt = gflops / np.mean(record[1].costs)

    best_config = {
        'config': encode(*record),
        'latency': np.mean(record[1].costs),
        'thrpt': thrpt,
        'log_path': log_file_name if log_file_name is not None else ' ',
        'tvm_commit': tvm_commit if tvm_commit is not None else 'unknown'
    }

    # Generate the DynamoDB commit item.
    item = {
        'Platform': {
            'S': platform
        },
        'OpName': {
            'S': record[0].task.workload[0]
        },
        'TaskName': {
            'S': record[0].task.name
        },
        'Args': convert_to_db_list(record[0].task.args),
        'PrimaryRangeKey': {
            'S': primary_range_key
        },
        'BestConfigs': convert_to_db_list([best_config])
    }

    # Setup the commit condition to avoid overwritten in case the item exists.
    cond_expr_vals = {':platform': {'S': platform}, ':key': {'S': primary_range_key}}

    # Commit the best config to the database.
    try:
        client = boto3.client('dynamodb', **db_kwargs)
        client.put_item(TableName=table_name,
                        Item=item,
                        ConditionExpression='Platform <> :platform AND PrimaryRangeKey <> :key',
                        ExpressionAttributeValues=cond_expr_vals)
        return
    except Exception as err:  # pylint:disable=broad-except
        if (not isinstance(err, botocore.exceptions.ClientError)
                or err.response['Error']['Code'] != 'ConditionalCheckFailedException'):
            raise RuntimeError('Failed to commit: %s' % str(err))

    # Append the best config to the exist record.
    try:
        update_expr = 'SET BestConfigs = list_append(BestConfigs, :config)'
        update_expr_vals = {':config': convert_to_db_list([best_config])}
        client.update_item(TableName=table_name,
                           Key={
                               'Platform': {
                                   'S': platform
                               },
                               'PrimaryRangeKey': {
                                   'S': primary_range_key
                               }
                           },
                           UpdateExpression=update_expr,
                           ExpressionAttributeValues=update_expr_vals)
    except Exception as err:  # pylint:disable=broad-except
        raise RuntimeError('Failed to append the best config: %s' % str(err))


def commit_tuning_log(log_file_path: str,
                      table_name: Optional[str] = None,
                      tvm_commit: Optional[str] = None,
                      **db_kwargs):
    """Commit tuning results to the database and upload the tuning log to the target path.

    Parameters
    ----------
    log_file_path: str
        The path of AutoTVM log file for the task.

    table_name: str
        The table name to commit. If None, then the latest table for the corresponding target
        will be selected.

    tvm_commit: str
        The TVM commit used for generating this record.

    **db_kwargs
        The kwargs of boto3 client. Commonly used: "region_name='us-west-1'"
        or "endpoint_url=http://localhost:8000".
    """

    if not os.path.exists(log_file_path):
        raise RuntimeError('Tuning log not found: %s' % log_file_path)
    log_file_name = os.path.basename(log_file_path)

    # Parse the records and group by tasks.
    best_records: Dict[str, Tuple[MeasureInput, MeasureResult]] = {}
    for record in load_from_file(log_file_path):
        task_str = str(record[0].task)
        if task_str not in best_records:
            best_records[task_str] = record
        if record[1].error_no != 0:  # Ignore invalid records.
            continue
        best_records[task_str] = min([best_records[task_str], record],
                                     key=lambda p: np.mean(p[1].costs))

    # Map target to the latest table name in the database.
    if table_name is not None:
        table_names = [table_name for _ in range(len(best_records))]
    else:
        targets = [parse_target(str(record[0].target))[0] for record in best_records.values()]
        exist_table_names = query_table_by_targets(list(set(targets)), **db_kwargs)
        table_names = [exist_table_names[t] for t in targets]

    # Commit the best record of each task.
    commit_count = 0
    for table, record in zip(table_names, best_records.values()):
        if record[1].error_no != 0:
            log.warning('Task %s has no valid record to be committed', str(record[0].task))
            continue
        commit_single_record(record=record,
                             log_file_name=log_file_name,
                             table_name=table,
                             tvm_commit=tvm_commit,
                             **db_kwargs)
        commit_count += 1

    if not best_records or not commit_count:
        raise RuntimeError('No valid record in the log file %s' % log_file_path)
