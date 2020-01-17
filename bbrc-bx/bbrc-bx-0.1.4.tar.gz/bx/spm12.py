import logging as log
from datetime import datetime
import os.path as op
from bx.parse import Command


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
            from bx.download import subcommand_download
            subcommand_download(self, self.validator, test)

        elif subcommand in ['rc']:
            from bx.download import download_rc
            download_rc(self, id, test=test, overwrite=self.overwrite,
                destdir=self.destdir)

        elif subcommand == 'volumes':
            self.subcommand_volumes(test)

        elif subcommand == 'tests':
            from bx.validation import subcommand_tests
            subcommand_tests(parser=self, test=test, validator=self.validator,
                version=['*', '0390c55f'])#, '2bc4d861'])
        else:
            self.wrong_subcommand(subcommand)

    def subcommand_volumes(self, test=False):

        subcommand = self.args[0]
        id = self.args[1]

        from bx import parse
        df = parse.download_measurements(self.xnat, spm12_volumes, id, test, resource_name='SPM12_SEGMENT')

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
