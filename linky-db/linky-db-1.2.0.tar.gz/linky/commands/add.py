import logging

from cliff.command import Command

import linky.utils.path_utils as path_utils
from linky.actions import add
from linky.config import read_conf
from linky.utils.dupe_handlers import DUPE_HANDLERS


class AddCommand(Command):
    """
    Add an item to the linky management
    """

    def get_parser(self, prog_name):
        parser = super(AddCommand, self).get_parser(prog_name)
        parser.add_argument("-b", "--base-path",
                            type=path_utils.abs_path,
                            help="Where to add the file/dir."
                                 "Can also be a path with a parent containing a base path."
                            )
        parser.add_argument("-d", "--dupe-handler",
                            choices=DUPE_HANDLERS.keys(),
                            help="How an existing destination / dupe is handled\n" +
                            "\n".join(
                                " - %s: %s" % (name, c.__doc__.strip())
                                for name, c in sorted(DUPE_HANDLERS.items())
                            ))
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-l", "--linked-root-prefix",
                           action="store_true",
                           help="Calculates the prefix in the linked root"
                                "Category and tag will be calculated."
                                "e.g"
                                "  path = linked_root/categoryA/tagA/dir/subdir/filename"
                                "  -->prefix = dir/subdir"
                                "  -->result = base_path/dir/subdir/filename"
                                "  -->category = categoryA"
                                "  -->tag = tagA"
                           )
        group.add_argument("-p", "--prefix",
                           default="",
                           help="<base_path>/<prefix>/<path name>\n"
                                "e.g\n"
                                "  path = /tmp/dir/subdir/filename\n"
                                "  prefix = just/a/prefix\n"
                                "  result --> base_path/just/a/prefix/filename\n")
        parser.add_argument("paths",
                            nargs="+", type=path_utils.abs_path,
                            help="The base path will be guessed from these paths "
                                 "if `-b` isn't provided!")
        return parser

    def take_action(self, parsed_args):
        logger = logging.getLogger("commands.add")
        for _abs_path in parsed_args.paths:
            try:
                base_path = path_utils.find_base(parsed_args.base_path or _abs_path)
                add(
                    _abs_path,
                    base_path,
                    read_conf(base_path),
                    prefix=parsed_args.prefix,
                    linked_root_prefix=parsed_args.linked_root_prefix
                )
            # pylint:disable=broad-except
            except Exception as exception:
                logger.warning("Couldn't add '%s': %s", _abs_path, exception)
