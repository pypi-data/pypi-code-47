import argparse

from cliff.command import Command

from linky.actions import move
from linky.utils.path_utils import abs_path


class MinArgsAction(argparse.Action):
    """
    A validator for options that need a minimum amount of values.
    """
    def __init__(self, option_strings, dest, **kwargs):
        self.min_count = int(kwargs.pop("nargs"))
        kwargs["nargs"] = "+"
        super(MinArgsAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if len(values) < self.min_count:
            raise argparse.ArgumentError(self, "At least %s required" % self.min_count)
        setattr(namespace, self.dest, values)


class MoveCommand(Command):
    """
    Move a file or directory.
    The change will be mirrored in the base.
    """

    def get_parser(self, prog_name):
        parser = super(MoveCommand, self).get_parser(prog_name)
        parser.add_argument(
            "paths", nargs=2, action=MinArgsAction, type=abs_path,
            help="At least 2 paths.\n"
                 "More than 2 paths means move these SOURCES into DIR"
        )
        return parser

    def take_action(self, parsed_args):
        move(*parsed_args.paths)
