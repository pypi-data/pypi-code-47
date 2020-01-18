import logging as log
from bx.parse import Command
from bx import parse
from bx import download as dl

class ASHSCommand(Command):
    '''ASHS (Hippocampal subfield segmentation)

    Available subcommands:
     files:\t\tdownload all `ASHS` outputs (segmentation maps, volumes, everything...)
     volumes:\t\tcreates an Excel table with all hippocampal subfield volumes
     snapshot:\t\tdownload a snapshot from the `ASHS` pipeline
     report:\t\tdownload the validation report issued by `ASHSValidator`
     tests:\t\tcreates an Excel table with all automatic tests outcomes from `ASHSValidator`
    '''
    nargs = 2
    resource_name = 'ASHS'
    subcommands = ['volumes', 'files', 'report', 'snapshot', 'tests']
    validator = 'ASHSValidator'

    def __init__(self, *args, **kwargs):
        super(ASHSCommand, self).__init__(*args, **kwargs)

    def parse(self):
        subcommand = self.args[0]
        id = self.args[1] #should be a project or an experiment_id
        validator = 'ASHSValidator'
        if subcommand in ['volumes']:
            df = self.run_id(id, ashs_measurements, resource_name=self.resource_name)
            self.to_excel(id, df)


        elif subcommand in ['files', 'report', 'snapshot']:
            self.run_id(id, dl.download, resource_name=self.resource_name,
                    validator=self.validator, destdir=self.destdir,
                    overwrite=self.overwrite, subcommand=subcommand)

        elif subcommand == 'tests':

            from bx import validation as val
            df = val.validation_scores(self.xnat, validator=self.validator,
                id=id, version=['beed8758', 'f80f2b13'])
            self.to_excel(id, df)


def ashs_measurements(x, experiments, resource_name='ASHS'):
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
            volumes = r.volumes()
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
