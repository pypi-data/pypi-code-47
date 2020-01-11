"""
The report module.
"""
import argparse
from typing import Any, List, Dict, Tuple

from .configs import append_config_parser


class ReportBase():
    """The base report class.
    FIXME (comaniac): This class is unfinished.
    """
    def __init__(self, configs: argparse.Namespace):
        self.configs = configs
        self.sections: Dict[str, Dict[str, Any]] = {'summary': {}, 'results': {}}

    def add_to_section(self, section: str, field: str, content: str):
        """Add data to a specific section in the report.

        Parameters
        ----------
        section: str
            The section to be added.

        field: str
            The field name.

        content: str
            The information to be displayed.
        """

        if section not in self.sections:
            raise RuntimeError('Unrecognized section %s in report' % section)
        self.sections[section][field] = content


@append_config_parser('top.tune', 'Tuning report options')
def define_config() -> List[Tuple[List[str], Dict[str, Any]]]:
    """Define the command line interface for report. Note that the report config
    is supposed to be appended to the tuner CLI.

    Returns
    -------
    actions: List[Tuple[List[str], Dict[str, Any]]]
        The report related configs.
    """
    actions: List[Tuple[List[str], Dict[str, Any]]] = []

    return actions
