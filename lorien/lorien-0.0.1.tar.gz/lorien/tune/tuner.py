"""
The tuning worker.
"""
import os
from enum import Enum
from typing import Any, Callable, Dict, Optional, Tuple
from uuid import uuid4

import boto3
import numpy as np

from tvm import autotvm
from tvm.autotvm.tuner import GATuner, GridSearchTuner, RandomTuner, XGBTuner

from ..database.commit import commit_tuning_log
from ..database.query import query_result_by_tasks
from ..database.table import list_tables
from ..logger import get_logger
from ..workload import Workload
from ..util import get_tvm_commit

log = get_logger('Tuner')

TVM_COMMIT = get_tvm_commit()


class TuneErrorCode(Enum):
    """Error code for the tuning."""
    NORMAL = 0
    NO_PREV_RESULT = 1  # Do not have previous result to compare with.
    NO_VALID_RESULT = 2  # Do not find any valid schedule config.
    FAIL_TO_SUBMIT = 3  # Fail to submit the workload for tuning.
    FAIL_TO_LOAD_WORKLOAD = 4  # Fail to load the workload from a JSON string.
    FAIL_TO_CREATE_TASK = 5  # Fail to create an AutoTVM task from a workload.
    FAIL_TO_GET_RESULT = 6  # Fail to retrieve results from worker.
    STORAGE_ERROR = 7  # Database or S3 bucket related errors.


class TuneMetadata():
    """Metadata for a tuning process."""
    def __init__(self):
        self.max_thrpt = 0  # Maximum throughput (GFLOP/s).
        self.trial_count = 0
        self.failed_count = 0  # The number of trails with error number != 0.


def create_autotvm_tuner(tuner_name: str, task: autotvm.task.Task) -> autotvm.tuner.Tuner:
    """Create an AutoTVM tuner by its name.

    Parameters
    ----------
    tuner_name: str
        The AutoTVM tuner name.

    task: autotvm.task.Task
        The AutoTVM task to be tuned.

    Returns
    -------
    autotvm_tuner: autotvm.tuner.Tuner
        The AutoTVM tuner.
    """
    if tuner_name == 'xgb':
        return XGBTuner(task)
    if tuner_name == 'ga':
        return GATuner(task, pop_size=100)
    if tuner_name == 'random':
        return RandomTuner(task)
    if tuner_name == 'gridsearch':
        return GridSearchTuner(task)

    raise RuntimeError('Invalid AutoTVM tuner name: %s' % tuner_name)


def callback_metadata(metadata: TuneMetadata) -> Callable:
    """An AutoTVM callback function to update the tuning metadata.

    Parameters
    ----------
    metadata: TuneMetadata
        The statistic information for the tuning process.

    Returns
    -------
    callback: Callable
        The callable function that maintains the metadata.
    """
    def _callback(_, inputs, results):
        for inp, res in zip(inputs, results):
            metadata.trial_count += 1
            if res.error_no == 0:
                metadata.max_thrpt = max(metadata.max_thrpt,
                                         inp.task.flop / np.mean(res.costs) / 1e9)
            elif res.error_no != 1:
                # Error code 1 (task instantiation error) is not considered a failure
                # because it is caused by improper schedule configs for GPU kernels.
                metadata.failed_count += 1

    return _callback


def tune(options: Dict[str, Any],
         workload: Workload,
         bucket_n_dir: Optional[Tuple[str, str]] = None,
         **db_kwargs) -> Tuple[TuneErrorCode, Any]:
    """Tune the workloads with the given configuration.

    Parameters
    ----------
    options: Dict[str, Any]
        The AutoTVM tuning options.

    workload: Workload
        The worklaod being tuned.

    bucket_n_dir: Optional[Tuple[str, str]]
        A pair of a S3 bucket and a folder name to upload the tuning logs. When unset,
        full tuning logs will not be stoed.

    **db_kwargs
        The kwargs of boto3 client. Commonly used: "region_name='us-west-1'"
        or "endpoint_url=http://localhost:8000".

    Returns
    -------
    ret: Tuple[TuneErrorCode, Any]
        A tuple of tuning error code and (prev_best_thrpt, curr_best_thrpt, message).
    """

    try:
        task = workload.to_task()
    except RuntimeError as err:
        return (TuneErrorCode.FAIL_TO_CREATE_TASK, str(err))

    log_file_name = '{}.json'.format(uuid4())

    # Get table list
    try:
        table_names = list_tables('{0}-{1}'.format(workload['lib'], workload['target']),
                                  **db_kwargs)
    except RuntimeError:
        table_names = []

    if not table_names:
        return (TuneErrorCode.STORAGE_ERROR, 'failed to get valid tables from database')
    table_name = table_names[0]

    # Create a local folder to temporary keep tuning logs.
    if not os.path.exists(table_name):
        os.mkdir(table_name)
    log_file_path = os.path.join(table_name, log_file_name)

    result_code = TuneErrorCode.NORMAL

    # Query for the previous result.
    try:
        best_prev_results = query_result_by_tasks([task], table_name, **db_kwargs)
        assert len(best_prev_results) == 1

        best_prev_result = max(best_prev_results[0], key=lambda r: r['thrpt'])
        assert best_prev_result

        prev_thrpt = best_prev_result['thrpt']
        if prev_thrpt == -1:
            raise RuntimeError(best_prev_result['FailMsg'])
    except RuntimeError as err:
        # Runtime error happens due to the database issues.
        log.warning('No prev result: %s', str(err))
        result_code = TuneErrorCode.NO_PREV_RESULT
        prev_thrpt = 0

    autotvm_tuner = create_autotvm_tuner(options['tuner'], task)

    log.info('Tuning workload %s and save log to %s', str(workload), log_file_name)

    metadata = TuneMetadata()

    # Test run for a few trial.
    test_trial = min(5, options['n_trial'])
    autotvm_tuner.tune(
        n_trial=test_trial,
        early_stopping=None,
        measure_option=options['measure_option'],
        callbacks=[autotvm.callback.log_to_file(log_file_path),
                   callback_metadata(metadata)])

    # Stop this workload if all test trials are failed.
    if metadata.failed_count == metadata.trial_count:
        log.info('Test run failed, stop')
        return (TuneErrorCode.NO_VALID_RESULT,
                (prev_thrpt, 0,
                 'Early stop due to no valid result after {} trials'.format(test_trial)))

    # Keep tuning.
    n_trial = options['n_trial'] - test_trial
    if n_trial:
        autotvm_tuner.tune(n_trial=n_trial,
                           early_stopping=None,
                           measure_option=options['measure_option'],
                           callbacks=[
                               autotvm.callback.log_to_file(log_file_path),
                               autotvm.callback.progress_bar(n_trial, 'Status'),
                               callback_metadata(metadata)
                           ])

    # Submit results to DB.
    err_msg = ''
    try:
        commit_tuning_log(log_file_path=log_file_path,
                          table_name=table_name,
                          tvm_commit=TVM_COMMIT,
                          **db_kwargs)
        log.info('Results are submitted to the database')
    except RuntimeError as err:
        result_code = TuneErrorCode.STORAGE_ERROR
        err_msg = 'Failed to commit result: {}'.format(str(err))
        log.warning(err_msg)

    # Upload tuning log to S3 bucket.
    if bucket_n_dir is not None:
        try:
            client = boto3.client('s3')
            client.upload_file(log_file_path, bucket_n_dir[0],
                               '{0}/{1}'.format(bucket_n_dir[1], log_file_name))
            log.info('Full tuning log has been uploaded to s3://%s/%s/%s', bucket_n_dir[0],
                     bucket_n_dir[1], log_file_name)
        except Exception as err:  # pylint: disable=broad-except
            result_code = TuneErrorCode.STORAGE_ERROR
            err_msg = 'Failed to upload tuning log to S3: {}'.format(str(err))
            log.warning(err_msg)

    return (result_code, (prev_thrpt, metadata.max_thrpt, err_msg))
