import logging as log
from datetime import datetime
import os.path as op
from bx.parse import Command


class ArchivingCommand(Command):
    '''Archiving - used to collect automatic tests from `ArchivingValidator`

    Available subcommands:
     tests:\t\tcreates an Excel table with all automatic tests outcomes from `ArchivingValidator`
    '''
    nargs = 2
    resource_name = 'ArchivingValidator'
    subcommands = ['tests']


    def __init__(self, *args, **kwargs):
        super(ArchivingCommand, self).__init__(*args, **kwargs)

    def parse(self, test=False):
        subcommand = self.args[0]
        id = self.args[1]
        if subcommand == 'tests':
            from bx.validation import subcommand_tests
            subcommand_tests(parser=self, test=test, validator=self.resource_name,
                version=['*', '0390c55f'])#, '2bc4d861'])
        else:
            self.wrong_subcommand(subcommand)
