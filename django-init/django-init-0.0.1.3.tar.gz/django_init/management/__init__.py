import argparse
import os

from django.core.management import find_commands, load_command_class, call_command

from django_init.utils.config import get_version, get_package_namespace as pkg_ns


def add_arguments(parser):
    parser.add_argument('values', nargs='*', help='Names of the application or project.')
    # parser.add_argument('-v', '--version', action='version', version=get_version())
    parser.add_argument('-a', '--all', help='Name of the application or project.')
    parser.add_argument('-y', '--yes', action='store_true', help='Automatic yes to prompts')
    parser.add_argument('-l', '--list', action='store_true', help='List of values')
    # parser.add_argument('db', choices=['mysql', 'postgres'], help='List of values')


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', nargs='?', help='Name of command')
    add_arguments(parser)
    return vars(parser.parse_args())


def execute_from_command_line():
    commands = find_commands(os.path.dirname(os.path.realpath(__file__)))
    kwargs = get_arguments()
    command, values = kwargs.pop('command'), kwargs.pop('values')

    if command:
        if command in commands:
            call_command(load_command_class(pkg_ns(), command), *values, **kwargs)
        else:
            print('Unknown command: %r' % command)
            print('Type "django-init --help" for usage.')
            print('Available commands:')
            [print('    %s' % command) for command in commands]
    else:
        print('Type "django-init --help <command>" for help on a specific command.')
        print('Available commands:')
        [print('    %s - ' % command) for command in commands]
