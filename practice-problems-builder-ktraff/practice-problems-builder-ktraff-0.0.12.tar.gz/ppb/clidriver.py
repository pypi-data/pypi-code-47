# MIT License

# Copyright (c) [year] [fullname]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import argparse
from typing import List

import ppb.argparser
from ppb.logging import setup_logger

_log = setup_logger(__name__)
PROGRAM_NAME = 'ppb'
PROGRAM_DESC = 'Build and maintain practice programming problems for multiple languages'


def main():
    driver = create_cli_driver()
    driver.main()


def create_cli_driver():
    return CliDriver(parsers=load_parsers())


def load_parsers():
    return [
        ppb.argparser.LogParser(),
        ppb.argparser.NewProblemParser(),
        ppb.argparser.AddLanguageParser(),
    ]


class CliDriver:

    def __init__(self, parsers: List[ppb.argparser.Parser]):
        self.root_parser = argparse.ArgumentParser(prog=PROGRAM_NAME, description=PROGRAM_DESC)
        self.subparser = self.root_parser.add_subparsers(help="Commands")
        self.parsers = parsers

    def _parse(self):
        for parser in self.parsers:
            parser.modify_parser(self.root_parser, self.subparser)
        return self.root_parser.parse_args()

    def _run(self, args):
        """Creates and runs the worker provided by the argument parser plugins."""
        if hasattr(args, 'activate_worker'):
            # Activate a worker that will consume the subcommand designated by this argument
            args.activate_worker()
        for parser in self.parsers:
            if parser.worker_is_active:
                parser.create_worker(args).run()

    def main(self):
        try:
            args = self._parse()
            self._run(args)
        except argparse.ArgumentTypeError as exc:
            _log.error(f"There was an error with the arguments provided: {exc}")
            self.root_parser.print_help()
