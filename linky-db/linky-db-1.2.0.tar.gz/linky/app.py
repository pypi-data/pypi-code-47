import inspect
import logging
import sys
from importlib import import_module

import pkg_resources
from cliff.app import App
from cliff.commandmanager import CommandManager

from linky.utils.str_utils import camel2kebab

COMMAND_SUFFIX = "Command"
VERSION = pkg_resources.resource_string(__name__, "VERSION").decode().strip()


class LinkyCommandManager(CommandManager):
    """
    Customized manager to load linky commands
    """

    def load_commands(self, namespace):
        """
        Creates commands from all *Command classes in the namespace

        :type namespace: basestring
        """
        module = import_module(namespace)
        for name, o in inspect.getmembers(module):
            if not (inspect.isclass(o) and name.endswith(COMMAND_SUFFIX)):
                continue

            # We make sure to remove the redundant "Command" suffix
            self.add_command(
                camel2kebab(name[:-len(COMMAND_SUFFIX)]),
                o
            )


App.NAME = "linky"


# pylint: disable=missing-class-docstring
class LinkyApp(App):
    CONSOLE_MESSAGE_FORMAT = logging.BASIC_FORMAT

    def __init__(self):
        super(LinkyApp, self).__init__(
            description="Helps keep files organized by linking them to a base folder",
            version=VERSION,
            command_manager=LinkyCommandManager("linky.commands"),
        )


# pylint: disable=missing-function-docstring
def main(argv=None):
    argv = argv or sys.argv[1:]
    myapp = LinkyApp()
    if len(argv) == 0:
        argv = ["help"]
    return myapp.run(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
