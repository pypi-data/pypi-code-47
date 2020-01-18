import shutil
import os
import os.path as op
import tempfile
import logging as log
from glob import glob
from tqdm import tqdm


def download_experiment(x, e, resource_name, validator, overwrite, destdir):

    e_id = e['ID']
    e = x.select.experiment(e_id)
    # resource_name is None when downloading reports only
    if not resource_name is None:
        r = e.resource(resource_name)
        if not r.exists():
            log.error('%s has no %s resource'%(e_id, resource_name))
            return
        dd = op.join(destdir, e_id)
        if op.isdir(dd) and not overwrite:
            msg = '%s already exists. Skipping %s.'%(dd, e_id)
            log.error(msg)
        else:
            if op.isdir(dd) and overwrite:
                msg = '%s already exists. Overwriting %s.'%(dd, e_id)
                log.warning(msg)
            elif not op.isdir(dd):
                os.mkdir(dd)
            r.get(dest_dir=dd)

    v = e.resource('BBRC_VALIDATOR')
    f = v.pdf(validator)

    if not f is None:
        fp = op.join(destdir, f.label()) if resource_name is None \
            else op.join(dd, f.label())
        #if resource_name is None:
        log.debug('Saving it in %s.'%fp)
        f.get(dest=fp)



def download(x, experiments, resource_name, validator, destdir, subcommand,
        overwrite=False):

    from bx import xnat
    if subcommand in ['files', 'report']:
        type = 'experiment'
    elif subcommand == 'snapshot':
        type = 'snapshot'
    elif subcommand == 'rc':
        type = 'rc'
    else:
        log.error('Invalid subcommand (%s).'%subcommand)

    log.info('Now initiating download for %s experiments.'%len(experiments))
    for e in tqdm(experiments):
        log.debug(e)
        try:
            if type == 'experiment':
                download_experiment(x, e, resource_name, validator, overwrite,
                    destdir)

            elif type == 'snapshot':
                download_snapshot(x, e, resource_name, validator, overwrite,
                        destdir)

            elif type == 'rc':
                download_rc(x, e, resource_name, validator, destdir)
        except KeyboardInterrupt:
            return

def download_snapshot(x, e, resource_name, validator, overwrite, destdir):
    r = x.select.experiment(e['ID']).resource(validator)
    if r.exists():
        fp = op.join(destdir, '%s.jpg'%e['ID'])
        r.download_snapshot(fp)
    else:
        log.error('%s has no %s'%(e, validator))


def download_rc(x, e, resource_name, validator, destdir):
    e_id = e['ID']
    log.debug(e_id)
    subject_label = e['subject_label']

    e = x.select.experiment(e_id)
    r = e.resource(resource_name)
    if not r.exists():
        log.error('%s has no %s resource'%(e, resource_name))
        return
    try:
        r.download_rc(destdir)
        v = e.resource('BBRC_VALIDATOR')
        if v.exists():
            fp = op.join(destdir, '%s_%s.jpg'%(subject_label, e_id))
            v.download_snapshot(validator, fp)
        else:
            log.warning('%s has not %s'%(e, validator))

    except Exception as exc:
        log.error('%s failed. Skipping (%s).'%(e_id, exc))
