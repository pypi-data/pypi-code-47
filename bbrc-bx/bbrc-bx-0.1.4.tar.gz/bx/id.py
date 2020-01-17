import logging as log
from datetime import datetime
import os.path as op
from bx.parse import Command

class IDCommand(Command):
    '''Returns subject/session labels along with parent project.

    Usage: bx id <resource_id>'''
    nargs = 1

    def __init__(self, *args, **kwargs):
        super(IDCommand, self).__init__(*args, **kwargs)

    def parse(self, test=False):
        id = self.args[0]
        df = self.run_id(id, get_id_table, test=test)

        if len(df) == 1:
            print(df.iloc[0])
        else:
            self.to_excel(id, df)


def get_id_table(x, experiments):
    table = []
    from tqdm import tqdm
    columns = ['label', 'subject_label']
    for e in tqdm(experiments):
        exp = x.array.experiments(experiment_id=e['ID'], columns=columns).data[0]
        table.append([exp['ID'], exp['label'], exp['subject_label'], exp['project']])

    import pandas as pd
    columns = ['ID', 'label', 'subject_label', 'project']
    df = pd.DataFrame(table, columns=columns).set_index('ID').sort_index()
    return df
