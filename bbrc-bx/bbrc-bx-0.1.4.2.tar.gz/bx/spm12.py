import logging as log
from datetime import datetime
import os.path as op
from bx.parse import Command
from bx import download as dl

class SPM12Command(Command):
    '''SPM12

    Available subcommands:
     files:\t\tdownload all `SPM12` outputs (segmentation maps, warp fields, everything...)
     volumes:\t\tcreates an Excel table with GM/WM/CSF volumes
     snapshot:\t\tdownload a snapshot from the segmentation results
     report:\t\tdownload the validation report issued by `SPM12Validator`
     tests:\t\tcreates an Excel table with all automatic tests outcomes from `SPM12`
     rc:\t\tdownloads rc* files (DARTEL imports)
    '''
    nargs = 2
    resource_name = 'SPM12_SEGMENT'
    validator = 'SPM12SegmentValidator'

    subcommands = ['volumes', 'files', 'report', 'snapshot', 'tests', 'rc']


    def __init__(self, *args, **kwargs):
        super(SPM12Command, self).__init__(*args, **kwargs)

    def parse(self, test=False):
        subcommand = self.args[0]
        id = self.args[1]

        if subcommand in ['files', 'report', 'snapshot']:
            self.run_id(id, dl.download, resource_name=self.resource_name,
                    validator=self.validator, destdir=self.destdir,
                    overwrite=self.overwrite, subcommand=subcommand)

        elif subcommand in ['rc']:
            self.run_id(id, dl.download, resource_name=self.resource_name,
                    validator=self.validator, destdir=self.destdir,
                    subcommand='rc')

        elif subcommand == 'volumes':
            df = self.run_id(id, spm12_volumes, resource_name=self.resource_name)
            self.to_excel(id, df)


        elif subcommand == 'tests':
            version = ['*', '0390c55f']
            from bx import validation as val
            df = val.validation_scores(self.xnat, validator = self.validator,
                id = id, version = version)
            self.to_excel(id, df)


    def subcommand_volumes(self):

        subcommand = self.args[0]
        id = self.args[1]

        from bx import parse
        df = parse.download_measurements(self.xnat, spm12_volumes, id, resource_name='SPM12_SEGMENT')

        self.to_excel(id, df)


def spm12_volumes(x, experiments, resource_name):
    from tqdm import tqdm
    import pandas as pd
    import tempfile
    import nibabel as nib
    import numpy as np
    import os

    table = []

    for e in tqdm(experiments):
        log.debug(e)
        try:

            r = x.select.experiment(e['ID']).resource(resource_name)
            if not r.exists():
                log.error('%s has no %s resource'%(e['ID'], resource_name))
                continue
            vols = [e['ID']]
            for kls in ['c1', 'c2', 'c3']:
                f = [each for each in r.files() if each.id().startswith(kls)][0]
                fp = tempfile.mkstemp('.nii.gz')[1]
                f.get(fp)
                d = nib.load(fp)
                size = np.prod(d.header['pixdim'].tolist()[:4])
                v = np.sum(d.dataobj) * size
                os.remove(fp)
                vols.append(v)
            table.append(vols)

        except KeyboardInterrupt:
            return pd.DataFrame(table, columns=['ID', 'c1', 'c2', 'c3']).set_index('ID').sort_index()
        except Exception as exc:
            log.error('Failed for %s. Skipping it.'%e)
            log.error(exc)
            continue

    df = pd.DataFrame(table, columns=['ID', 'c1', 'c2', 'c3']).set_index('ID').sort_index()
    return df
