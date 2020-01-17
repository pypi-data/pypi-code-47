from datetime import datetime
import os.path as op
import logging as log
from bx.parse import Command


class FreeSurfer6Command(Command):
    '''FreeSurfer v6.0

    Available subcommands:
     files:\t\tdownload all `recon-all` outputs (segmentation maps, files, everything...)
     aseg:\t\tcreates an Excel table with all `aseg` measurements
     aparc:\t\tcreates an Excel table with all `aparc` measurements
     hippoSfVolumes:\tsaves an Excel table with hippocampal subfield volumes (if available)
     snapshot:\t\tdownload a snapshot from the `recon-all` pipeline
     report:\t\tdownload the validation report issued by `FreeSurferValidator`
     tests:\t\tcreates an Excel table with all automatic tests outcomes from `FreeSurferValidator`
    '''
    nargs = 2
    resource_name = 'FREESURFER6'
    subcommands = ['aparc', 'aseg', 'hippoSfVolumes', 'snapshot', 'tests', 'report', 'files']


    def __init__(self, *args, **kwargs):
        super(FreeSurfer6Command, self).__init__(*args, **kwargs)

    def parse(self, test=False):
        subcommand = self.args[0]
        id = self.args[1] #should be a project or an experiment_id
        print(id)
        if subcommand in ['aparc', 'aseg', 'hippoSfVolumes']:
            self.subcommand_aparc(test)

        elif subcommand in ['files', 'report', 'snapshot']:
            self.subcommand_download(test)

        elif subcommand == 'tests':
            from bx.validation import subcommand_tests
            subcommand_tests(parser=self, test=test, validation='FreeSurferValidator',
                id=id, version=['##0390c55f', '4e37c9d0'])

    def subcommand_aparc(self, test=False):
        subcommand = self.args[0]
        id = self.args[1]

        resource_name = self.resource_name

        from bx import parse
        if subcommand == 'aparc':
            df = parse.download_measurements(self.xnat, aparc_measurements,  id,
                test, resource_name=resource_name)
        elif subcommand == 'aseg':
            df = parse.download_measurements(self.xnat, aseg_measurements, id,
                test, resource_name=resource_name)
        elif subcommand == 'hippoSfVolumes':
            df = parse.download_measurements(self.xnat, hippoSfVolumes_measurements,
                id, test, resource_name=resource_name)

        self.to_excel(id, df)


    def subcommand_download(self, test=False):
        subcommand = self.args[0]
        id = self.args[1]

        resource_name = self.resource_name
        known_suffixes = ['_HIRES', '_SUBFIELDS']
        suffix = ''
        if '_' in self.command:
            suffix = '_%s'%self.command.split('_')[1].upper()
            if not suffix in known_suffixes:
                print('%s not known (known suffixes: %s)'
                    %(self.command, known_suffixes))
            else:
                resource_name = 'FREESURFER6%s'%suffix


        if subcommand == 'report':
            resource_name = None

        validation_report = 'SPM12SegmentValidator'
        suffix = 'Hires' if resource_name.endswith('_HIRES') else ''
        validation_report = 'FreeSurfer%sValidator'%suffix


        from bx import parse
        if subcommand in ['files', 'report']:
            parse.download_experiments(self.xnat, id, resource_name,
                validation_report, self.destdir, self.overwrite,
                test=test)
        elif subcommand in ['snapshot']:
            parse.download_snapshots(self.xnat, id, validation_report,
                self.destdir, self.overwrite, test=test)

def freesurfer6_measurements(x, func, experiments, resource_name='FREESURFER6'):
    from tqdm import tqdm
    import pandas as pd

    table = []
    for e in tqdm(experiments):
        log.debug(e)
        try:
            s = e['subject_label']
            r = x.select.experiment(e['ID']).resource(resource_name)
            if not r.exists():
                log.error('%s has no %s resource'%(e, resource_name))
                continue
            if func == 'aparc':
                volumes = r.aparc()
            elif func == 'aseg':
                volumes = r.aseg()
            elif func == 'hippoSfVolumes':
                volumes = r.hippoSfVolumes(mode='T1')
            volumes['subject'] = s
            volumes['ID'] = e['ID']
            table.append(volumes)
        except KeyboardInterrupt:
            return pd.concat(table).set_index('ID').sort_index()
        except Exception as exc:
            log.error('Failed for %s. Skipping it.'%e)
            log.error(exc)
            continue
    hippoSfVolumes = pd.concat(table).set_index('ID').sort_index()
    return hippoSfVolumes

def aparc_measurements(x, experiments, resource_name='FREESURFER6'):
    return freesurfer6_measurements(x, 'aparc', experiments, resource_name=resource_name)

def aseg_measurements(x, experiments, resource_name='FREESURFER6'):
    return freesurfer6_measurements(x, 'aseg', experiments, resource_name=resource_name)

def hippoSfVolumes_measurements(x, experiments, resource_name='FREESURFER6'):
    return freesurfer6_measurements(x, 'hippoSfVolumes', experiments, resource_name=resource_name)

class FreeSurfer6HiresCommand(FreeSurfer6Command):
    '''FreeSurfer v6.0 (-hires option)

    Available subcommands:
     files:\t\tdownload all `recon-all` outputs (segmentation maps, files, everything...)
     aseg:\t\tcreates an Excel table with all `aseg` measurements
     aparc:\t\tcreates an Excel table with all `aparc` measurements
     hippoSfVolumes:\tsaves an Excel table with hippocampal subfield volumes (if available)
     snapshot:\t\tdownload a snapshot from the `recon-all` pipeline
     report:\t\tdownload the validation report issued by `FreeSurferHiresValidator`
     tests:\t\tcreates an Excel table with all automatic tests outcomes from `FreeSurferValidator`
    '''
    nargs = 2
    resource_name = 'FREESURFER6_HIRES'


    def __init__(self, *args, **kwargs):
        super(FreeSurfer6HiresCommand, self).__init__(*args, **kwargs)
