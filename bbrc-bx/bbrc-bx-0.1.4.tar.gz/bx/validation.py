import logging as log
import os.path as op
from datetime import datetime
from tqdm import tqdm

def collect_reports(xnat_instance, experiments,
        validator_name='ArchivingValidator', version=['toto']):
    import json
    url = '/data/experiments/%s/resources/BBRC_VALIDATOR/files/%s'
    reports = {}

    for e in tqdm(experiments):
        try:
            columns = ['ID', 'label', 'xsiType']
            exp = xnat_instance.array.experiments(experiment_id=e,
                                                  columns=columns).data
            assert(len(exp)==1)
            uri = url%(exp[0]['ID'], '%s_%s.json'%(validator_name, exp[0]['label']))
            r = xnat_instance.select.experiment(e).resource('BBRC_VALIDATOR')
            if not r.exists(): continue
            f = r.file('%s_%s.json'%(validator_name, exp[0]['label']))
            if not f.exists(): continue

            j = json.loads(xnat_instance.get(f._uri).text)
            if 'version' not in j.keys():
                log.warning('Version not found in report %s'%j.keys())
                continue
            if j['version'] not in version and not '*' in version: continue
            fields = list(j.keys())
            try:
                for each in ['version', 'generated', 'experiment_id']:
                    fields.remove(each)
            except ValueError:
                msg = 'No valid report found (%s).'%e
                log.error(msg)
                raise Exception(msg)
            reports[e] = j

        except KeyboardInterrupt:
            return reports

    return reports


def validation_scores(x, validator, version,  id, test=False):
    from bx import parse
    import pandas as pd

    t = parse.check_xnat_item(id, x)

    experiments = []
    max_rows = 25 if test else None

    if t == 1:
        experiments = [id]

    elif t == 0:
        experiments = []
        for e in x.array.experiments(project_id=id,
                columns=['label']).data[:max_rows]:
            experiments.append(e['ID'])
    elif t == 2:
        from bx import lists
        experiments = getattr(lists, id)[:max_rows]
    else:
        print('%s is not a project or an experiment nor a list'%id)

    res = []

    # Collecting reports of given version(s)
    log.info('Looking for experiments with %s report with versions %s.'\
                %(validator, version))
    reports = dict(list(collect_reports(x, validator_name=validator,
        experiments=experiments, version=version).items()))
    log.info('Now initiating download for %s experiment(s).'\
            %len(reports.items()))

    # Creating list of columns (intersection between all reports tests)
    fields = list(list(reports.items())[0][1].keys())
    for e, report in tqdm(reports.items()):
        fields = set(fields).intersection(list(report.keys()))
    fields = list(fields)

    # Compiling data from reports (has_passed from each test)
    for e, report in tqdm(reports.items()):
        try:
            row = [e]
            row.extend([report[f]['has_passed'] for f in fields \
                if not f in ['version', 'generated', 'experiment_id']])
            row.extend([report[f] for f in ['version', 'generated']])
            res.append(row)
        except KeyboardInterrupt:
            fields.insert(0, 'ID')
            for each in ['version', 'generated', 'experiment_id']:
                fields.remove(each)
            fields.extend(['version', 'generated'])
            df = pd.DataFrame(res, columns=fields).set_index('ID')
            return df

    # Building DataFrame
    fields.insert(0, 'ID')
    for each in ['version', 'generated', 'experiment_id']:
        fields.remove(each)
    fields.extend(['version', 'generated'])
    df = pd.DataFrame(res, columns=fields).set_index('ID')
    return df


def subcommand_tests(parser, validator, version, test=False):
    subcommand = parser.args[0]
    id = parser.args[1]

    from bx.validation import validation_scores
    df = validation_scores(parser.xnat, validator=validator,
        id=id, version=version, test=test)

    parser.to_excel(id, df)
