"""
The base module of workload extraction from models.
"""
import argparse
from typing import Any, Dict, List, Set, Tuple

import tqdm

from tvm import autotvm, relay

from ...logger import get_logger
from ...workload import Workload
from ...configs import create_config_parser, register_config_parser

log = get_logger('Extract')


def extract_from_model(configs: argparse.Namespace,
                       mod_n_params: List[Tuple[relay.Module, Dict[str, Any]]]) -> List[Workload]:
    """Extract workloads from a given model.

    Parameters
    ----------
    configs: argparse.Namespace
        The system configure of generate.extract.<frontend>.
    Returns
    -------
    workloads: List[Workload]
        A list of collected workloads.
    """

    # Extract workloads from models.
    workloads: Set[Workload] = set()
    for mod, params in tqdm.tqdm(mod_n_params, ncols=60):
        # TODO(comaniad): Find a way to extract all tasks without specifying all ops in
        # the argument of this function call.
        for target in configs.target:
            tasks = autotvm.task.extract_from_program(
                mod['main'],
                target=target,
                params=params,
                ops=(relay.op.nn.conv2d, relay.op.nn.conv2d_transpose, relay.op.nn.dense,
                     relay.op.nn.deformable_conv2d))

            # Task to workload
            for task in tasks:
                try:
                    workloads.add(Workload.from_task(task))
                except RuntimeError as err:
                    log.warning('Failed to create workload from task %s: %s', str(task), str(err))
                    continue

    log.info('%d workloads have been generated', len(workloads))
    return list(workloads)


@register_config_parser('top.generate.extract')
def define_config_extract() -> argparse.ArgumentParser:
    """Define the command line interface for workload generation by model extraction.

    Returns
    -------
    parser: argparse.ArgumentParser
        The defined argument parser.
    """
    parser = create_config_parser('Workload Generation by Model Extraction')

    # Define generators
    subparsers = parser.add_subparsers(
        dest='mode', description='The mode to generate workloads by model extraction')
    subparsers.required = True
    return parser
