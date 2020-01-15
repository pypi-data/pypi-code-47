import argparse
import os
import sys

from django.core.management import find_commands, load_command_class, call_command

from django_init.utils.config import get_package_namespace as pkg_ns


def execute_from_command_line():
    commands = find_commands(os.path.dirname(os.path.realpath(__file__)))
    try:
        command_name = sys.argv[1]
    except IndexError:
        command_name = None

    if command_name:
        if command_name in commands:
            parser = argparse.ArgumentParser()
            command = load_command_class(pkg_ns(), command_name)
            command.add_arguments(parser)
            args = parser.parse_args()
            if command_name == 'project':
                args = (v for k, v in vars(args).items() if v)
                call_command(command, *args)
            elif command_name == 'apps':
                args = parser.parse_args()
                call_command(command, args.command_name, *args.apps_name)
            elif command_name == 'db':
                call_command(command, args.command_name, args.database_name, engine=args.engine)
                # call_command(command, *args, **kwargs)
        else:
            print('Unknown command: %r' % command_name)
            print('Type "django-init --help" for usage.')
            print('Available commands:')
            [print('    %s' % command_name) for command_name in commands]
    else:
        print('Type "django-init --help <command>" for help on a specific command.')
        print('Available commands:')
        [print('    %s - ' % command_name) for command_name in commands]
