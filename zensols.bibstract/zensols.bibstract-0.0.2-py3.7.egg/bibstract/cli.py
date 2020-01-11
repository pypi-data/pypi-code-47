"""Command line entrance point to the application.

"""
__author__ = 'plandes'

import sys
from zensols.actioncli import OneConfPerActionOptionsCliEnv
from zensols.bibstract import AppConfig, Extractor


class ExtractorCli(object):
    def __init__(self, *args, texpath: str = None, **kwargs):
        config = AppConfig.from_args(*args, **kwargs)
        self.ex = Extractor(config, texpath)

    def _assert_master_bib(self):
        if self.ex.master_bib is None:
            sys.stderr.write(f'missing the master BibTex -m option\n')
            sys.exit(1)

    def _assert_texpath(self):
        if self.ex.texpath is None:
            sys.stderr.write(f'missing the (La)Tex path -t option\n')
            sys.exit(1)

    def print_bibtex_ids(self):
        self._assert_master_bib()
        self.ex.print_bibtex_ids()

    def print_texfile_refs(self):
        self._assert_texpath()
        self.ex.print_texfile_refs()

    def print_exported_ids(self):
        self._assert_master_bib()
        self.ex.print_exported_ids()

    def export(self):
        self._assert_master_bib()
        self._assert_texpath()
        self.ex.export()


class ConfAppCommandLine(OneConfPerActionOptionsCliEnv):
    def __init__(self):
        masterbib_op = ['-m', '--masterbib', False,
                        {'dest': 'master_bib',
                         'metavar': 'FILE',
                         'help': 'the directory to masterbib the website'}]
        texpathbib_op = ['-t', '--texpath', False,
                         {'dest': 'texpath',
                          'metavar': 'PATH',
                          'help': 'the file or directory to find citations'}]
        cnf = {'executors':
               [{'name': 'exporter',
                 'executor': lambda params: ExtractorCli(**params),
                 'actions': [{'name': 'printbib',
                              'meth': 'print_bibtex_ids',
                              'doc': 'print BibTex citation keys',
                              'opts': [masterbib_op]},
                             {'name': 'printtex',
                              'meth': 'print_texfile_refs',
                              'doc': 'print citation references',
                              'opts': [texpathbib_op]},
                             {'name': 'printexport',
                              'meth': 'print_exported_ids',
                              'doc': 'print BibTex export citation keys',
                              'opts': [masterbib_op, texpathbib_op]},
                             {'name': 'export',
                              'doc': 'export the derived BibTex file',
                              'opts': [masterbib_op, texpathbib_op]}]}],
               'config_option': {'name': 'config',
                                 'expect': False,
                                 'opt': ['-c', '--config', False,
                                         {'dest': 'config',
                                          'metavar': 'FILE',
                                          'help': 'configuration file'}]},
               'whine': 1}
        super(ConfAppCommandLine, self).__init__(
            cnf, config_env_name='bibstractrc', pkg_dist='zensols.bibstract',
            config_type=AppConfig)


def main():
    cl = ConfAppCommandLine()
    cl.invoke()
