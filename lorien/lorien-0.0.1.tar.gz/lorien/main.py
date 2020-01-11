"""
The main flow that integrates all modules
"""
import sys
from .configs import create_config_parser, make_config_parser, register_config_parser
from .logger import enable_log_file


@register_config_parser('top')
def define_config():
    """Define the command line interface for the main entry.

    Returns
    -------
    parser: argparse.ArgumentParser
        The defined argument parser.
    """

    parser = create_config_parser('Lorien: TVM Optimized Schedule Database', prog='lorien')
    parser.add_argument('--log-run',
                        action='store_true',
                        default=False,
                        help='Log execution logs to a file')
    subparsers = parser.add_subparsers(dest='command', help='The command being executed')
    subparsers.required = True
    return parser


class Main():
    """The main entry."""
    def __init__(self):
        args = make_config_parser(sys.argv[1:])
        if args.log_run:
            enable_log_file()
        args.entry(args)
