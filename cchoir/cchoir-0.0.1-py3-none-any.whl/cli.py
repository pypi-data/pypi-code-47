"""Caasa command line entry point."""
from sys import argv
from sys import exit as sys_exit

from cchoir.commands import configure


def main():
    """Caasa entry point."""
    command, arguments = configure(argv[1:])
    return command.run(arguments)


if __name__ == '__main__':
    RESULT = main()
    sys_exit(RESULT)
