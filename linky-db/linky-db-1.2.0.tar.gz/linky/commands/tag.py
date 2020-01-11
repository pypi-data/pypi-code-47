from cliff.command import Command

from linky.actions import tag
from linky.config import read_conf
from linky.utils.path_utils import abs_path


class TagCommand(Command):
    """
    Tags a given file
    """

    def get_parser(self, prog_name):
        parser = super(TagCommand, self).get_parser(prog_name)

        parser.add_argument("-d", "--delete",
                            action="store_true",
                            help="Deletes the tags from the file")
        parser.add_argument("-b", "--best-effort",
                            action="store_true",
                            help="Ignores errors and tries to apply changes to each given path")
        parser.add_argument("-t", "--tags",
                            required=True,
                            action="append",
                            help="The category and tag to use separated by a '/' e.g Rating/1\n"
                                 "Can be repeated as many times as necessary")
        parser.add_argument("paths", nargs="+", type=abs_path)

        return parser

    def take_action(self, parsed_args):
        config = read_conf(parsed_args.paths[0])
        tag(
            parsed_args.paths,
            parsed_args.tags,
            config,
            parsed_args.delete,
            parsed_args.best_effort,
        )
