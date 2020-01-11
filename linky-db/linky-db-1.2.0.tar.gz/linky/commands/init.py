from cliff.command import Command

from linky.actions import init
from linky.utils.path_utils import abs_path


class InitCommand(Command):
    """
    Initializes a directory it it hasn't been done before
    """

    def get_parser(self, prog_name):
        parser = super(InitCommand, self).get_parser(prog_name)
        parser.add_argument("--overwrite-config",
                            action="store_true",
                            help="Overwrites existing configuration if "
                                 "a new configuration directory is found in "
                                 "the provided path")
        parser.add_argument("path")
        return parser

    def take_action(self, parsed_args):
        init(abs_path(parsed_args.path), parsed_args.overwrite_config)
