from datetime import datetime
import os.path as op
import logging as log
from bx.parse import Command
from bx import parse


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


    def __init__(self, *args, **kwargs):
        super(DTIFITCommand, self).__init__(*args, **kwargs)

    def parse(self, test=False):
        subcommand = self.args[0]
        id = self.args[1] #should be a project or an experiment_id

        if subcommand in ['files', 'report', 'snapshot']:
            self.subcommand_download(test)

        elif subcommand == 'tests':
            from bx.validation import subcommand_tests
            subcommand_tests(parser=self, test=test, validator='DTIFITValidator',
                version=['*', '4e37c9d0'])



    def subcommand_download(self, test=False):
        ''' following subcommands: files, report and snapshot '''

        subcommand = self.args[0]
        id = self.args[1]
        validation_report = 'DTIFITValidator'

        resource_name = self.resource_name if  subcommand != 'report' else None

        if subcommand in ['files', 'report']:
            parse.download_experiments(self.xnat, id, resource_name,
                validation_report, self.destdir, self.overwrite,
                test=test)

        elif subcommand in ['snapshot']:
            parse.download_snapshots(self.xnat, id, validation_report,
                self.destdir, self.overwrite, test=test)
