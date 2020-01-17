import shutil
import os
import os.path as op
import tempfile
import logging as log
from glob import glob

def get_validation_report(x, e, report_name):
    r = x.select.experiment(e).resource('BBRC_VALIDATOR')
    pdf = {each.label():each for each in list(r.files()) \
        if report_name in each.label() and \
        each.label().endswith('.pdf')}

    if not r.exists():
        log.error('%s has no BBRC_VALIDATOR resource'%e)
        return None
    if len(pdf.items()) == 0:
        log.error('%s has no %s'%(e, report_name))
        return None

    assert(len(list(pdf.keys())) == 1)
    f = pdf[list(pdf.keys())[0]]
    return f

def download_experiment(x, e, resource_name, validation_report, overwrite,
        destdir):

    # resource_name is None when downloading reports only
    if not resource_name is None:
        r = x.select.experiment(e).resource(resource_name)
        if not r.exists():
            log.error('%s has no %s resource'%(e, resource_name))
            return
        dd = op.join(destdir, e)
        if op.isdir(dd) and not overwrite:
            msg = '%s already exists. Skipping %s.'%(dd, e)
            log.error(msg)
        else:
            if op.isdir(dd) and overwrite:
                msg = '%s already exists. Overwriting %s.'%(dd, e)
                log.warning(msg)
            elif not op.isdir(dd):
                os.mkdir(dd)
            r.get(dest_dir=dd)

    f = get_validation_report(x, e, validation_report)
    if not f is None:
        fp = op.join(destdir, f.label()) if resource_name is None \
            else op.join(dd, f.label())
        #if resource_name is None:
        log.debug('Saving it in %s.'%fp)
        f.get(dest=fp)



def extract_file(fp):
    dn = op.dirname(fp)

    with open(fp, "rb") as file:
        pdf = file.read()

    startmark = b"\xff\xd8"
    startfix = 0
    endmark = b"\xff\xd9"
    endfix = 2
    i = 0

    njpg = 0
    while True:
        istream = pdf.find(b"stream", i)
        if istream < 0:
            break
        istart = pdf.find(startmark, istream, istream + 20)
        if istart < 0:
            i = istream + 20
            continue
        iend = pdf.find(b"endstream", istart)
        if iend < 0:
            raise Exception("Didn't find end of stream!")
        iend = pdf.find(endmark, iend - 20)
        if iend < 0:
            raise Exception("Didn't find end of JPG!")

        istart += startfix
        iend += endfix
        jpg = pdf[istart:iend]
        with open(op.join(dn, "jpg%d.jpg" % njpg), "wb") as jpgfile:
            jpgfile.write(jpg)

        njpg += 1
        i = iend

def subcommand_download(self, validation_report,
        test=False):
    subcommand = self.args[0]
    id = self.args[1]

    resource_name = self.resource_name if subcommand != 'report' else None

    from bx import parse
    if subcommand in ['files', 'report']:
        parse.download_experiments(self.xnat, id, resource_name,
            validation_report, self.destdir, self.overwrite, test=test)
    elif subcommand in ['snapshot']:
        parse.download_snapshots(self.xnat, id, validation_report,
            self.destdir, self.overwrite, test=test)

def download_snapshot(x, e, validation_report, overwrite, dest_dir):
    # download validation report only
    f = get_validation_report(x, e, validation_report)
    if f is None:
        log.error('%s not found for experiment %s'%(validation_report, e))
        return
    fp = op.join(dest_dir, f.label())
    log.debug('Saving it in %s.'%fp)
    f.get(dest=fp)

    extract_file(fp)
    #print(glob(op.join(dest_dir, '*.jpg')))
    if len(glob(op.join(dest_dir, '*.jpg'))) == 0:
        log.error('No snapshot found in report. %s %s'%(e, validation_report))
        return

    import tempfile
    f, fp2 = tempfile.mkstemp(suffix='.jpg')
    os.close(f) # we dont need the handle
    cmd = 'montage %s/jpg*jpg -background black -geometry 2600x+0+0 -tile 1x %s'%(dest_dir, fp2)
    os.system(cmd)

    fp3 = op.join(dest_dir, '%s.jpg'%e)
    cmd = 'mv %s %s; rm %s/jpg*.jpg'%(fp2, fp3, dest_dir)
    os.system(cmd)
    cmd = 'rm %s'%fp
    os.system(cmd)


def download_rc(self, id, test, destdir, rc_files=['rc1', 'rc2'], overwrite=False):
    from tqdm import tqdm
    import os
    import os.path as op

    from bx.parse import check_xnat_item
    t = check_xnat_item(id, self.xnat)

    max_rows = 1 if test else None

    experiments = []
    if t == 1:
        experiments = [id]

    elif t == 0:
        for e in x.array.experiments(project_id=id,
                columns=['label']).data[:max_rows]:
            experiments.append(e['ID'])
    elif t == 2:
        from bx import lists
        experiments = getattr(lists, id)
    else:
        print('%s is not a project or an experiment nor a list'%id)

    for e in tqdm(experiments):
        log.debug(e)

        # resource_name is None when downloading reports only
        r = self.xnat.select.experiment(e).resource(self.resource_name)
        if not r.exists():
            log.error('%s has no %s resource'%(e, self.resource_name))
            continue
        try:
            for each in rc_files:
                subject_label = self.xnat.array.experiments(experiment_id=e,
                    columns=['subject_label']).data[0]['subject_label']
                fp = '%s_%s_%s.nii.gz'%(each[-3:], subject_label, e)
                list(r.files('%s*'%each))[0].get(op.join(destdir, fp))

            from bx.download import download_snapshot
            download_snapshot(self.xnat, e, self.validator, overwrite, destdir)
        except KeyboardInterrupt:
            return
        except:
            log.error('%s failed. Skipping.'%e)
            continue
