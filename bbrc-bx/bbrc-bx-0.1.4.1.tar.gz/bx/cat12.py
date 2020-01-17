import logging as log
from datetime import datetime
import os.path as op
from bx.parse import Command


class CAT12Command(Command):
    '''CAT12

    Available subcommands:
     files:\t\tdownload all `CAT12` outputs (segmentation maps, warp fields, everything...)
     volumes:\t\tcreates an Excel table with GM/WM/CSF volumes
     snapshot:\t\tdownload a snapshot from the segmentation results
     report:\t\tdownload the validation report issued by `CAT12Validator`
     tests:\t\tcreates an Excel table with all automatic tests outcomes from `CAT12Validator`
    '''
    nargs = 2
    resource_name = 'CAT12_SEGMENT'
    validator = 'CAT12SegmentValidator'

    subcommands = ['volumes', 'files', 'report', 'snapshot', 'tests', 'rc']


    def __init__(self, *args, **kwargs):
        super(CAT12Command, self).__init__(*args, **kwargs)

    def parse(self, test=False):
        subcommand = self.args[0]
        id = self.args[1]

        if subcommand in ['files', 'report', 'snapshot']:
            from bx.download import subcommand_download
            subcommand_download(self, self.validator, test)

        elif subcommand in ['rc']:
            from bx.download import download_rc
            files = ['mri/rp1', 'mri/rp2']
            download_rc(self, id, test=test, overwrite=self.overwrite,
                destdir=self.destdir, rc_files=files)

        elif subcommand == 'volumes':
            self.subcommand_volumes(test)

        elif subcommand == 'tests':
            from bx.validation import subcommand_tests
            subcommand_tests(parser=self, test=test, validator='CAT12SegmentValidator',
                version=['##0390c55f', '2bc4d861'])


    def subcommand_volumes(self, test=False):

        subcommand = self.args[0]
        id = self.args[1]

        from bx import parse
        df = parse.download_measurements(self.xnat, cat12_volumes, id, test,
            resource_name='CAT12_SEGMENT')

        self.to_excel(id, df)


def cat12_volumes(x, experiments, resource_name):
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
            for kls in ['p1', 'p2', 'p3']:

                f = [each for each in r.files('mri/%s*'%kls)][0]
                fh, fp = tempfile.mkstemp('.nii.gz')
                os.close(fh)
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
