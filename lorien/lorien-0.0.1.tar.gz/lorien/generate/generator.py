"""
Workload generators.
"""
import argparse
from typing import Callable, List

import yaml

from ..configs import create_config_parser, register_config_parser
from ..logger import get_logger
from ..workload import Workload

log = get_logger('Generator')


def gen(gen_func: Callable[[argparse.Namespace], List[Workload]]) -> Callable:
    """Generate workloads based on configs.

    Parameters
    ----------
    gen_func: Callable[[argparse.Namespace], List[Workload]]
        The generator function that accepts generator specific configs and returns
        a list of generated workloads.

    Returns
    -------
    ret: Callable
        The entry function that uses the given generation function to generate workloads.
    """
    def _do_gen(configs: argparse.Namespace):
        """Invoke the generator function to get the workload list, and validate if the workload
        is a valid for AutoTVM.

        Parameters
        ----------
        configs: argparse.Namespace
            The configuration of the generator.
        """
        # Collect workloads
        log.info('Generating workloads...')
        workloads: List[Workload] = gen_func(configs)

        # Save to a file
        with open(configs.output, 'w') as workload_file:
            yaml.safe_dump({'workload': [w.to_yaml() for w in workloads]},
                           workload_file,
                           width=float('inf'))

    return _do_gen


@register_config_parser('top.generate')
def define_config() -> argparse.ArgumentParser:
    """Define the command line interface for workload generation.

    Returns
    -------
    parser: argparse.ArgumentParser
        The defined argument parser.
    """
    parser = create_config_parser('Workload Generation')

    # Define generators
    subparsers = parser.add_subparsers(dest='mode', description='The mode to generate workloads')
    subparsers.required = True
    return parser
