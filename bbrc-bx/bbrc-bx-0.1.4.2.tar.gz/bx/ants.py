from bx.parse import Command
from bx import download as dl

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
    validator = 'ANTSValidator'

    def __init__(self, *args, **kwargs):
        super(ANTSCommand, self).__init__(*args, **kwargs)


    def parse(self):

        subcommand = self.args[0]
        id = self.args[1] #should be a project or an experiment_id
        validator = 'ANTSValidator'

        if subcommand in ['files', 'report', 'snapshot']:
            self.run_id(id, dl.download, resource_name=self.resource_name,
                    validator=self.validator, destdir=self.destdir,
                    overwrite=self.overwrite, subcommand=subcommand)

        elif subcommand == 'tests':

            from bx import validation as val
            df = val.validation_scores(self.xnat, validator=self.validator,
                id=id, version=['*', '0390c55f'])
            self.to_excel(id, df)
