from . import helloworld
from . import print_to_console

from xbus import service

service.register('demo.helloworld', helloworld.HelloWorld)
service.register('demo.print-to-console', print_to_console.PrintToConsole)
