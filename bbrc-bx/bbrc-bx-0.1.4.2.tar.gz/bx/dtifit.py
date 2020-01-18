from datetime import datetime
import os.path as op
import logging as log
from bx.parse import Command
from bx import parse
from bx import download as dl


class DTIFITCommand(Command):
    '''Processing of Diffusion-weighted Imaging data

    Available subcommands:
    files:\t\tdownload all outputs from the `DTIFIT` pipeline (up to parametric maps)
    report:\t\tdownload the validation report issued by `DTIFITValidator`
    snapshot:\t\tdownload a snapshot with FA map, RGB tensor and TOPUP distortion correction map
    '''
    nargs = 2
    resource_name = 'TOPUP_DTIFIT'
    subcommands = ['files', 'report', 'snapshot', 'tests']
    validator = 'DTIFITValidator'

    def __init__(self, *args, **kwargs):
        super(DTIFITCommand, self).__init__(*args, **kwargs)

    def parse(self):
        subcommand = self.args[0]
        id = self.args[1] #should be a project or an experiment_id

        if subcommand in ['files', 'report', 'snapshot']:
            self.run_id(id, dl.download, resource_name=self.resource_name,
                    validator=self.validator, destdir=self.destdir,
                    overwrite=self.overwrite, subcommand=subcommand)

        elif subcommand == 'tests':
            version = ['*', '4e37c9d0']
            from bx import validation as val
            df = val.validation_scores(self.xnat, validator=self.validator,
                id=id, version=version)
            self.to_excel(id, df)
