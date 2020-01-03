from ...yarn import yarn_adapter
from ..base import BaseYarnCommand


class Command(BaseYarnCommand):
    args = 'command'
    help = 'Call yarn in node modules root ({0}).'.format(
        yarn_adapter._node_modules_root)

    def add_arguments(self, parser):
        parser.add_argument('command', nargs='*')

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        args = args or tuple(options.pop('command'))
        if self._is_single_command('install', args):
            self._install([])
        else:
            yarn_adapter.call_bower(args)

    def _is_single_command(self, name, args):
        return len(args) == 1 and args[0] == name
