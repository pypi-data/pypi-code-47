"""
The query module of the database.
"""
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Any, Dict, List, Optional

import boto3

from tvm.autotvm.task import Task

from ..logger import get_logger
from .table import list_tables
from .util import convert_to_list, gen_primary_key, parse_target

log = get_logger('DB-Query')


def __query_result_by_task(task: Task, table_name: str, **db_kwargs) -> List[Dict[str, Any]]:
    """The internal function for querying results by given a task and other required information.

    Parameters
    ----------
    task: Task
        The AutoTVM tasks.

    table_name: str
        The table name to be queried.

    **db_kwargs
        The kwargs of boto3 client. Commonly used: "region_name='us-west-1'"
        or "endpoint_url=http://localhost:8000".

    Returns
    -------
    items: List[Dict[str, Any]]
        The best configs for the given task.
    """
    _, platform = parse_target(str(task.target))
    primary_key_pattern = gen_primary_key(task)

    # Generate query
    key_condition_expr = 'Platform = :platform'
    expr_vals = {':platform': {'S': platform}}
    key_condition_expr += ' AND begins_with(PrimaryRangeKey, :key)'
    expr_vals[':key'] = {'S': primary_key_pattern}

    query_options = {
        'TableName': table_name,
        'KeyConditionExpression': key_condition_expr,
        'ExpressionAttributeValues': expr_vals,
        'ProjectionExpression': 'BestConfigs'
    }

    try:
        client = boto3.client('dynamodb', **db_kwargs)
        result = client.query(**query_options)
        items = result['Items'][0]['BestConfigs']
    except Exception as err:  # pylint:disable=broad-except
        raise RuntimeError('Failed to query %s from %s: %s' %
                           (primary_key_pattern, table_name, str(err)))

    return convert_to_list(items)


def query_result_by_tasks(tasks: List[Task],
                          table_name: Optional[str] = None,
                          **db_kwargs) -> List[List[Dict[str, Any]]]:
    """Query for the best results for the given AutoTVM tasks.

    Parameters
    ----------
    tasks: List[Task]
        A list of AutoTVM tasks.

    table_name: Optional[str]
        The table name to be queried. The latest table according to the task target and platform
        will be queried if this argument is not presented.

    **db_kwargs
        The kwargs of boto3 client. Commonly used: "region_name='us-west-1'"
        or "endpoint_url=http://localhost:8000".

    Returns
    -------
    items: List[List[Dict[str, Any]]]
        A list of best configs for each given task.
    """

    # Check if target is available in given tasks.
    if any([t.target is None for t in tasks]):
        raise RuntimeError('One or more tasks have no target specified')

    # Process table name
    table_names: List[str] = []
    if table_name is not None:
        table_names = [table_name for _ in range(len(tasks))]
    else:
        # Determine the table name for each task.
        targets: List[str] = [parse_target(str(task.target))[0] for task in tasks]
        db_table_names = query_table_by_targets(list(set(targets)), **db_kwargs)
        table_names = [db_table_names[t] for t in targets]

    results: List[List[Dict[str, Any]]] = []
    with ProcessPoolExecutor(max_workers=len(tasks)) as pool:
        futures = [
            pool.submit(__query_result_by_task, task=task, table_name=table, **db_kwargs)
            for task, table in zip(tasks, table_names)
        ]
        for future in as_completed(futures):
            try:
                results.append(future.result())
            except Exception as err:  # pylint: disable=broad-except
                results.append([{'thrpt': -1, 'FailMsg': str(err)}])
        return results


def query_table_by_targets(target_list: List[str], **db_kwargs) -> Dict[str, str]:
    """Query table names for a given target list.

    target_list: List[str]
        The target list (e.g., ['cuda', 'llvm'])

    **db_kwargs
        The kwargs of boto3 client. Commonly used: "region_name='us-west-1'"
        or "endpoint_url=http://localhost:8000".

    Returns
    -------
    target_2_table: Dict[str, str]
        Map from target to the table name.
    """
    target_2_table: Dict[str, str] = {}
    table_names = list_tables('topi', **db_kwargs)
    for target in target_list:
        desire_name = '{0}-{1}'.format('topi', target)
        if desire_name in table_names:
            target_2_table[target] = desire_name
        else:
            raise RuntimeError('Table %s has not been created' % desire_name)

    return target_2_table
