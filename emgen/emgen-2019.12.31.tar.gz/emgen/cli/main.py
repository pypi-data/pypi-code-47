#!/usr/bin/env python3

import argparse
import os
import sys

import pyperclip

from emgen import __version__
from emgen.core import localpart

DISPLAY = os.getenv("DISPLAY")
LINUX = os.name == "posix"


def _has_clipboard():
    try:
        original = pyperclip.paste()
        pyperclip.copy(original)
        return True
    except pyperclip.PyperclipException:
        return False


def main():
    has_clipboard = _has_clipboard()

    parser = argparse.ArgumentParser(
        prog="emgen", description="Generate random email addresses.",
    )
    parser.add_argument(
        "-c",
        "--clipboard",
        action="store_true",
        default=False,
        help="copy addr to clipboard (default: %(default)s)"
        if has_clipboard
        else argparse.SUPPRESS,
    )
    parser.add_argument(
        "-d",
        "--domain",
        default="example.com",
        type=str,
        help="set the addr domain portion (default: %(default)s)",
        metavar="DOMAIN",
    )
    parser.add_argument(
        "-l",
        "--length",
        default=8,
        type=int,
        help="length of the local-part (from 1 to 64) (default: %(default)s)",
        metavar="LENGTH",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    args = parser.parse_args()

    lp = localpart(args.length)
    addr = f"{lp}@{args.domain}"

    if args.clipboard:
        if has_clipboard:
            pyperclip.copy(addr)
        else:
            warning = "warning: could not find a clipboard for your system"
            print(warning, file=sys.stderr)

    print(addr)
