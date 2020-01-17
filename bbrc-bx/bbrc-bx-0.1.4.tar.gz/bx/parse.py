import pandas as pd
import json
import os.path as op
import os
import tempfile
import argparse
import pkgutil
import inspect
from datetime import datetime
from tqdm import tqdm

from .validation import validation_scores
from bx import download as dl #import download_snapshot, download_experiment

from .dicom import *


def __get_modules__(m):
    modules = []
    prefix = m.__name__ + '.'
    log.info('prefix : %s'%prefix)
    for importer, modname, ispkg in pkgutil.iter_modules(m.__path__, prefix):
        module = __import__(modname , fromlist='dummy')
        if not ispkg:
            modules.append(module)
        else:
            modules.extend(__get_modules__(module))
    return modules

def __find_all_commands__(m):
    ''' Browses bx and looks for any class named as a Command'''
    modules = []
    classes = []
    modules = __get_modules__(m)
    forbidden_classes = [] #Test, ScanTest, ExperimentTest]
    for m in modules:
        for name, obj in inspect.getmembers(m):
            if inspect.isclass(obj) and 'Command' in name \
                    and not obj in forbidden_classes:
                classes.append(obj)
    return classes

class readable_dir(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir=values
        if not os.path.isdir(prospective_dir):
            msg = "readable_dir:{0} is not a valid path".format(prospective_dir)
            raise argparse.ArgumentTypeError(msg)
        if os.access(prospective_dir, os.R_OK):
            setattr(namespace,self.dest,prospective_dir)
        else:
            msg = "readable_dir:{0} is not a readable dir".format(prospective_dir)
            raise argparse.ArgumentTypeError(msg)

def check_xnat_item(a, x):
    projects = [e.label() for e in list(x.select.projects())]
    experiments = []
    for p in projects:
        exp = x.array.experiments(project_id=p).data
        experiments.extend([e['ID'] for e in exp])

    if a in projects:
        log.info('Project detected: %s'%a)
        return 0
    elif a in experiments:
        log.info('Experiment detected: %s'%a)
        return 1
    else:
        from bx import lists
        if hasattr(lists, a):
            print('List detected: %s'%a)
            return 2
        else:
            log.error('%s is not a project/experiment'%a)
            return -1


def download(x, id, resource_name, validation_report, destdir,
         overwrite=False, test=False, type='experiment'):
    t = check_xnat_item(id, x)

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

    log.info('Now initiating download for %s experiments.'%len(experiments))
    for e in tqdm(experiments):
        log.debug(e)
        if type == 'experiment':
            dl.download_experiment(x, e, resource_name, validation_report,
                overwrite, destdir)
        elif type == 'snapshot':
            dl.download_snapshot(x, e, validation_report,
                overwrite, destdir)

def download_experiments(x, id, resource_name, validation_report, destdir,
         overwrite=False, test=False):
     download(x, id, resource_name, validation_report, destdir,
             overwrite=overwrite, test=test, type='experiment')

def download_snapshots(x, id, validation_report, destdir,
         overwrite=False, test=False):
     download(x, id, None, validation_report, destdir,
             overwrite=overwrite, test=test, type='snapshot')

def download_measurements(x, func, id=None, test=False, **kwargs):

    t = check_xnat_item(id, x)
    max_rows = 25 if test else None

    experiments = []
    if t == 1:
        experiments = x.array.experiments(experiment_id=id,
            columns=['label', 'subject_label']).data

    elif t == 0:
        experiments = []
        for e in x.array.experiments(project_id=id,
                columns=['label', 'subject_label']).data[:max_rows]:
            experiments.append(e)
    elif t == 2:
        from bx import lists
        l = getattr(lists, id)
        for e in l[:max_rows]:
            ex = x.array.experiments(experiment_id=e,
                columns=['label', 'subject_label']).data[0]
            experiments.append(ex)
    else:
        print('%s is not a project or an experiment nor a list'%id)

    return func(x, experiments, **kwargs)



def parse(parser, command, test=False):
    c = command(parser.command, parser.args, parser.xnat, parser.destdir,
        parser.overwrite)

    if len(c.args) == 0:
        msg = c.__doc__
        cn = parser.command
        print('\nHelp for command `%s`:\n\n%s'%(cn, msg))

    elif len(c.args) == command.nargs:
        if command.nargs == 1 or c.args[0] in command.subcommands:
            c.parse(test=test)
        else:
            subcommands = '\n - '.join(command.subcommands)
            msg = '\n%s invalid\n\nAvailable subcommands:\n - %s'%(c.args[0], subcommands)
            print(msg)

    else:
        msg = c.__doc__
        cn = parser.command
        msg = '\n\nMissing argument(s)\n\nHelp for command `%s`:\n\n%s'%(cn, msg)
        print(msg)



class Command(object):
    def __init__(self, command, args, xnat_instance, destdir, overwrite):
        self.command = command
        self.args = args
        self.xnat = xnat_instance
        self.destdir = destdir
        self.overwrite = overwrite

    def run_id(self, id, func, test=False, **kwargs):
        from bx import parse
        t = parse.check_xnat_item(id, self.xnat)

        max_rows = 1 if test else None
        columns = ['label', 'subject_label']
        experiments = []
        if t == 1:
            experiments = self.xnat.array.experiments(experiment_id=id,
                    columns=columns).data

        elif t == 0:
            for e in self.xnat.array.experiments(project_id=id,
                    columns=columns).data[:max_rows]:
                experiments.append(e)
        elif t == 2:
            from bx import lists
            experiments = getattr(lists, id)
            experiments = [self.xnat.array.experiments(experiment_id=e,
                    columns=columns).data[0] for e in experiments]
        else:
            print('%s is not a project or an experiment nor a list'%id)


        return func(self.xnat, experiments, **kwargs)

    def to_excel(self, id, df):
        dt = datetime.today().strftime('%Y%m%d_%H%M%S')
        fn = 'bx_%s_%s_%s.xlsx'%(self.command, id, dt)
        fp = op.join(self.destdir, fn)
        log.info('Saving it in %s'%fp)
        df.to_excel(fp)

    def wrong_subcommand(self, subcommand):
        msg = self.__doc__
        cn = self.__class__.__name__.split('Command')[0]
        print('Wrong subcommand `%s`.\n\nHelp for command `%s`:\n\n%s'\
            %(subcommand, cn, msg))

def parse_args(command, args, x, destdir=tempfile.gettempdir(), overwrite=False,
        test=False):

    parser = Command(command, args, x, destdir, overwrite=overwrite)

    import bx
    commands = __find_all_commands__(bx)
    commands = {e.__name__.split('.')[-1].lower()[:-7]: e for e in commands}

    if command in commands.keys():

        log.debug('Command: %s'%command)
        if command == 'freesurfer6':
            ans = ''

            if test == False:
                while not ans in ['1', '2']:
                    msg = 'Please confirm if you want FREESURFER6 or FREESURFER6_HIRES.'\
                      '(1) FREESURFER6  (2) FREESURFER6_HIRES ?'
                    ans = input(msg)

            if ans == '2':
                command = 'freesurfer6hires'
                parser = Command(command, args, x, destdir, overwrite=overwrite)

        parse(parser, commands[command], test=test)

    else:
        msg = '%s not found \n\nValid commands:\n %s'\
            %(command, '\n '.join([e for e, v in commands.items() if e!='']))
        log.error(msg)
        #raise Exception(msg)



def create_parser():
    import argparse
    cfgfile = op.join(op.expanduser('~'), '.xnat.cfg')

    import bx
    commands = __find_all_commands__(bx)
    commands = {e.__name__.split('.')[-1].lower()[:-7]: e.__doc__ \
        for e in commands if e.__name__ != 'Command'}
    from bx import __version__
    epilog = 'bx (v%s)\n\nExisting commands:\n'%__version__

    for e, v in commands.items():
        i = int(len(str(e)) / 6)
        tabs = (3 - i) * '\t'
        v = '%s%s'%(tabs, v) if not v is None else ''
        epilog = epilog + ' %s %s\n'%(e, str(v).split('\n')[0])

    epilog = epilog + '\nbx is distributed in the hope that it will be useful, '\
     'but WITHOUT ANY WARRANTY. \nSubmit issues/comments/PR at http://gitlab.com/xgrg/bx.\n\n'\
     'Authors: Greg Operto, Jordi Huguet - BarcelonaBeta Brain Research Center (2019)'

    from argparse import RawTextHelpFormatter
    parser = argparse.ArgumentParser(description=epilog,
        formatter_class=RawTextHelpFormatter) #, epilog=epilog)
    parser.add_argument('command', help='bx command')
    parser.add_argument('args', help='bx command', nargs="*")
    parser.add_argument('--config', help='XNAT configuration file',
        required=False, default=cfgfile)
    parser.add_argument('--dest', help='Destination folder',
        required=False, action=readable_dir)
    parser.add_argument('--verbose', '-v', action='store_true', default=False,
        help='Display verbosal information (optional)', required=False)
    parser.add_argument('--overwrite', '-O', action='store_true', default=False,
        help='Overwrite', required=False)

    from bx import __version__
    parser.add_argument('-V', '--version', action='version', version="%(prog)s ("+__version__+")")

    return parser
