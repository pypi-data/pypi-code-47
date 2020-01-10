# -*- coding: utf-8 -*-

from typing import List, TextIO

from pathlib import Path

from argparse import (ArgumentParser, Namespace)

import izitest
from izitest.path import *

__all__ = [
    "parse_args"
]


def parse_args() -> Namespace:
    """Parse arguments.

    Also check if exec (and ref if provided) are regular executable files and testdir is a valid directory.

    Returns:
        Namespace: parsed arguments

    Raises:
        Exception: if arguments checks failed
    """

    parser = ArgumentParser(description="Easily build a test suite.", allow_abbrev=True)

    parser.add_argument("exec", type=str, help="path to the executable you want to test")

    parser.add_argument("--ref", metavar="ref", type=str, help="specify a reference executable")

    parser.add_argument("-q", "--quiet", action="store_true",
                        help="run silently, do not output ANYTHING (even errors)!")
    parser.add_argument("-d", "--testdir", metavar="dir", type=Path, default=Path("./tests"),
                        help="path to the test suite directory (default is './tests')")
    parser.add_argument("-c", "--cat", metavar="cat", nargs='+', type=str,
                        help="run only the tests of specified categories")
    parser.add_argument("-m", "--memory", action="store_true",
                        help="if set, it will check for any memory leak using valgrind (see https://valgrind.org/)")
    parser.add_argument("-r", "--report", type=Path, metavar="file", nargs='?',
                        help="generate a report (default file is './tests_report')")

    args = parser.parse_args()

    if args.quiet:
        izitest.prettyprint.QUIET = True

    args.exec = args.exec.split(' ')
    execpath: Path = Path(args.exec[0])
    check_file(execpath) and check_exec(execpath)

    if args.ref is not None:
        args.ref = args.ref.split(' ')
        refpath: Path = Path(args.ref[0])
        check_file(refpath) and check_exec(refpath)

    check_dir(args.testdir)

    return args
