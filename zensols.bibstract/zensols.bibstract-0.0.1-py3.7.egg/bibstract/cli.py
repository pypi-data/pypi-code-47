"""Command line entrance point to the application.

"""
__author__ = 'plandes'

from pathlib import Path
from zensols.actioncli import OneConfPerActionOptionsCliEnv
from zensols.bibstract import Extractor


class ExtractorCli(object):
    def __init__(self, master_bib: str = None, texpath: str = None):
        if master_bib is not None:
            master_bib = Path(master_bib)
        if texpath is not None:
            texpath = Path(texpath)
        self.ex = Extractor(master_bib, texpath)

    def print_bibtex_ids(self):
        self.ex.print_bibtex_ids()

    def print_texfile_refs(self):
        self.ex.print_texfile_refs()

    def print_exported_ids(self):
        self.ex.print_exported_ids()

    def export(self):
        self.ex.export()


class ConfAppCommandLine(OneConfPerActionOptionsCliEnv):
    def __init__(self):
        masterbib_op = ['-m', '--masterbib', False,
                        {'dest': 'master_bib',
                         'metavar': 'FILE',
                         'default': 'master.bib',
                         'help': 'the directory to masterbib the website'}]
        texpathbib_op = ['-t', '--texpath', False,
                         {'dest': 'texpath',
                          'metavar': 'PATH',
                          'default': 'texpath.bib',
                          'help': 'the file or directory to scan for citation references'}]
        cnf = {'executors':
               [{'name': 'exporter',
                 'executor': lambda params: ExtractorCli(**params),
                 'actions': [{'name': 'printbib',
                              'meth': 'print_bibtex_ids',
                              'doc': 'print BibTex citation keys',
                              'opts': [masterbib_op]},
                             {'name': 'printtex',
                              'meth': 'print_texfile_refs',
                              'doc': 'print citation references from the tex file',
                              'opts': [texpathbib_op]},
                             {'name': 'printexport',
                              'meth': 'print_exported_ids',
                              'doc': 'print BibTex citation keys to be exported',
                              'opts': [masterbib_op, texpathbib_op]},
                             {'name': 'export',
                              'doc': 'export matching references from the master BibTex file found in Tex file ',
                              'opts': [masterbib_op, texpathbib_op]}]}],
               'whine': 1}
        super(ConfAppCommandLine, self).__init__(
            cnf, config_env_name='bibstractrc', pkg_dist='zensols.bibstract')


def main():
    cl = ConfAppCommandLine()
    cl.invoke()
