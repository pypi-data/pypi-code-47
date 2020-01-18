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

    def parse(self):
        subcommand = self.args[0]
        id = self.args[1]
        if subcommand == 'tests':
            
            from bx import validation as val
            df = val.validation_scores(self.xnat, validator=self.resource_name,
                id=id, version=['*', '0390c55f'])
            self.to_excel(id, df)
