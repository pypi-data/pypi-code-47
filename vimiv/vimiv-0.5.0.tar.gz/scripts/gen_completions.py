#!/usr/bin/env python3
# vim: ft=python fileencoding=utf-8 sw=4 et sts=4

# This file is part of vimiv.
# Copyright 2017-2019 Christian Karl (karlch) <karlch at protonmail dot com>
# License: GNU GPL v3, see the "LICENSE" and "AUTHORS" files for details.

"""Generate shell completion files from the vimiv argument parser."""

import argparse
from typing import NamedTuple, List

import vimiv
import vimiv.parser


class Argument(NamedTuple):
    """Storage class for a command line argument."""
    longname: str = None
    shortname: str = None
    description: str = None


def create_argument(action: argparse.Action) -> Argument:
    names = action.option_strings
    longname = names[-1]
    shortname = None if len(names) == 1 else names[0]
    return Argument(longname, shortname, action.help)


def write_zsh_completion(arguments: List[Argument], outfile: str = "_vimiv") -> None:
    with open(outfile, "w") as f:
        f.write(
            f"#compdef {vimiv.__name__}\n\n"
            "local context state line\n"
            "local -A opt_args\n\n"
            "_arguments \\\n"
        )
        for argument in arguments:
            if argument.shortname is not None:
                first = f"{argument.shortname} {argument.longname}"
                second = f"{{{argument.shortname},{argument.longname}}}"
            else:
                first = second = argument.longname
            f.write(f"    '({first})'{second}'[{argument.description}]' \\\n")
        f.write("    '*:images:_files -g \"*\"'\n")


if __name__ == "__main__":
    vimiv_parser = vimiv.parser.get_argparser()
    arguments = [
        create_argument(action)
        for group in vimiv_parser._action_groups
        for action in group._group_actions
        if action.option_strings
    ]
    write_zsh_completion(arguments)
