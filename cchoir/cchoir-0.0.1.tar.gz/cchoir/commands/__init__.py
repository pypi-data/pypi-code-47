"""Caasa commands module."""
from argparse import ArgumentParser

from .command import Command
from .deploy import DeployCommand


def configure(arguments):
    """Load command line argument parser and parse arguments.

    Args:
        arguments (List[str]) : Command line arguments to parse.

    Return:
        command, arguments (Command, Namespace) : The selected command and
                                                  parsed arguments.

    """
    parser = ArgumentParser()
    commands = [
        DeployCommand()
    ]

    command_index = {it.name: it for it in commands}

    subparsers = parser.add_subparsers(
        help='Caasa command to run.',
        dest='selected_command'
    )

    for command_it in commands:
        subparsers.add_parser(
            name=command_it.name,
            description=command_it.__class__.__doc__,
            help=command_it.__class__.__doc__,
        )
        command_it.configure(parser)

    arguments = parser.parse_args(arguments)
    command_name = arguments.selected_command
    command = command_index[command_name]

    return (command, arguments)
