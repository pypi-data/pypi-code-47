#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse
from pathlib import Path

from fsttest import __version__ as VERSION
from fsttest import run_tests

parser = argparse.ArgumentParser(prog="fsttest", description="Test FOMA FSTs")
parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")

parser.add_argument(
    "dir",
    type=Path,
    nargs="?",
    default=Path("./tests"),
    help="Path to directory containing tests",
)


def main():
    args = parser.parse_args()
    run_tests(args.dir)


if __name__ == "__main__":
    main()
