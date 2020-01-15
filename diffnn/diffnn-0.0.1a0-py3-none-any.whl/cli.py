"""
"""
import argparse
import importlib
import pkgutil

from pathlib import Path

from . import __version__
from . import logging


class HelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar
        else:
            parts = []
            # if the Optional doesn't take a value, format is:
            #    -s, --long
            if action.nargs == 0:
                parts.extend(action.option_strings)

            # if the Optional takes a value, format is:
            #    -s ARGS, --long ARGS
            # change to
            #    -s, --long ARGS
            else:
                default = action.dest.upper()
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append("%s" % option_string)
                parts[-1] += " %s" % args_string
            return ", ".join(parts)


def parse_args():
    parser = argparse.ArgumentParser(
        description="diffnn - differencing deep neural networks",
        prog="diffnn",
        formatter_class=HelpFormatter,
    )
    parser.add_argument("-V", "--version", action="version", version=__version__)
    parser.add_argument("--seed", type=int, default=None, help="the random seed to use")
    logging.add_arguments(parser)

    # TODO : should probably read in a configuration file instead
    parser.add_argument("network1", type=Path)
    parser.add_argument("network2", type=Path)

    known_args, extra_args = parser.parse_known_args()
    return known_args, extra_args
