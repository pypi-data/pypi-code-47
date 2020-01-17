from bx.parse import Command

class ANTSCommand(Command):
    '''ANTS

    Available subcommands:
     files:\t\tdownload all `ASHS` outputs (segmentation maps, volumes, everything...)
     snapshot:\t\tdownload a snapshot from the `ASHS` pipeline
     report:\t\tdownload the validation report issued by `ASHSValidator`
     tests:\t\tcreates an Excel table with all automatic tests outcomes from `ASHSValidator`
    '''
    nargs = 2
    resource_name = 'ANTS'
    subcommands = ['files', 'report', 'snapshot', 'tests']


    def __init__(self, *args, **kwargs):
        super(ANTSCommand, self).__init__(*args, **kwargs)


    def parse(self, test=False):

        subcommand = self.args[0]
        id = self.args[1] #should be a project or an experiment_id
        validator = 'ANTSValidator'

        if subcommand in ['files', 'report', 'snapshot']:
            from bx.download import subcommand_download
            subcommand_download(self, validator, test)

        elif subcommand == 'tests':
            from bx.validation import subcommand_tests
            subcommand_tests(parser=self, test=test, validator='ANTSValidator',
                version=['0390c55f'])#, '2bc4d861'])

        else:
            self.wrong_subcommand(subcommand)
