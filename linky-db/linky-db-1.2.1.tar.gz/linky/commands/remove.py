import logging

from cliff.command import Command

import linky.utils.path_utils as path_utils
from linky.actions import remove


class RemoveCommand(Command):
    """
    Permanently removes / deletes a file or folder and all its links.
    Warning: This is a NON-REVERSIBLE action!
    """

    def get_parser(self, prog_name):
        parser = super(RemoveCommand, self).get_parser(prog_name)
        parser.add_argument("paths", nargs="+", type=path_utils.abs_path,
                            help="The file or directory to remove")
        return parser

    def take_action(self, parsed_args):
        _log = logging.getLogger("command.remove")
        for _abs_path in parsed_args.paths:
            if _abs_path.exists():
                try:
                    remove(_abs_path)
                # pylint:disable=broad-except
                except Exception as exception:
                    _log.error("Couldn't remove '%s': %s",
                               _abs_path, exception,
                               exc_info=True)
            else:
                _log.info("Ignored nonexistent: %s", _abs_path)
