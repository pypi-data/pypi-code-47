"""
Generate workloads with Gluon CV model zoo.
"""
import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import List, Set

import yaml

from ...configs import create_config_parser, register_config_parser
from ...logger import get_logger
from ...workload import Workload
from ..generator import gen
from ..extract.gcv import extract_from_gcv
from .mutator import MUTATOR_TABLE

log = get_logger('ModelZooMutation')


def __validate_workload(workload: Workload) -> bool:
    """Valiate if the given workload is a legal AutoTVM task.

    Parameters
    ----------
    workload: Workload
        The workload to be validated.

    Returns
    -------
    ret: bool
        True if the workload is valid.
    """
    try:
        workload.to_task()
        return True
    except RuntimeError:
        return False


def mutate_from_model_zoo(configs: argparse.Namespace) -> List[Workload]:
    """Mutate workloads from Gluon CV model zoo.

    Parameters
    ----------
    configs: argparse.Namespace
        The system configure of "ModelZoo".

    Returns
    -------
    workloads: List[Workload]
        A list of collected workloads.
    """

    # Extract workloads from models.
    base_workloads = extract_from_gcv(configs)
    log.info('Mutating %s worklaod extracted from Gluon CV models', len(base_workloads))

    # Process mutation rules.
    with open(configs.rules, 'r') as filep:
        rules = yaml.load(filep, Loader=yaml.Loader)

    # TODO(comaniac): Support other libs.
    rules = rules['topi']

    workload_set: Set[Workload] = set(base_workloads)
    for workload in base_workloads:
        for name, rule in rules.items():
            if workload['task_name'].find(name) != -1:
                workload_set.update(MUTATOR_TABLE[name](rule, workload))

    log.info('%d workloads have been generated', len(workload_set))

    # Validate workloads by checking if they can be AutoTVM tasks.
    if not configs.skip_validate:
        log.info('Validating workloads...')
        with ProcessPoolExecutor(max_workers=len(workload_set)) as pool:
            futures = [
                pool.submit(__validate_workload, workload=workload) for workload in workload_set
            ]
            validations = [future.result() for future in as_completed(futures)]
            validate_count = sum([1 if v else 0 for v in validations])
        log.info('%d workloads failed to create tasks', len(workload_set) - validate_count)
    else:
        # Skip the validation by setting all worklaod are valid.
        validations = [True for _ in range(len(workload_set))]

    return [w for w, valid in zip(workload_set, validations) if valid]


@register_config_parser('top.generate.mutate')
def define_config_mutate() -> argparse.ArgumentParser:
    """Define the command line interface for workload generation with mutation.

    Returns
    -------
    parser: argparse.ArgumentParser
        The defined argument parser.
    """
    parser = create_config_parser('Workload Generation with Mutation')

    # Define generators
    subparsers = parser.add_subparsers(dest='mode',
                                       description='The mode to generate and mutate workloads')
    subparsers.required = True
    return parser


@register_config_parser('top.generate.mutate.modelzoo')
def define_config() -> argparse.ArgumentParser:
    """Define the command line interface for model zoo workload generation and mutation.

    Returns
    -------
    parser: argparse.ArgumentParser
        The defined argument parser.
    """
    parser = create_config_parser('Mutate workloads from Gluon CV model zoo')
    parser.add_argument('rules', help='Mutation rule config file in YAML format')
    parser.add_argument('--model',
                        action='append',
                        default=[],
                        required=True,
                        help='A Gluon CV model name with input shape in YAML format: '
                        '"<model-name>: {<input-name>: [<input-shape>]}". When shape is ignored, '
                        'the default shape (1, 3, 224, 224) will be applied')
    parser.add_argument('--target',
                        action='append',
                        default=[],
                        required=True,
                        help='A TVM target (e.g., llvm, cuda, etc). '
                        'Note that the device tag (e.g., -model=v100) is not required.')
    parser.add_argument('-o', '--output', default='workloads.yaml', help='The output file path')
    parser.add_argument('--skip-validate',
                        default=False,
                        action='store_true',
                        help='Skip the validation process')
    parser.set_defaults(entry=gen(mutate_from_model_zoo))
    return parser
