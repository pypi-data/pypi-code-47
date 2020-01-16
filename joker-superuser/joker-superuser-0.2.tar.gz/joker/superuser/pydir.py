#!/usr/bin/env python3
# coding: utf-8

import os
import re
import sys
from os.path import join

from joker.textmanip.tabular import format_help_section

from joker.superuser.utils import under_asset_dir

_nsinits = {
    'i': '__import__("pkg_resources").declare_namespace(__name__)',
    'p': '__path__ = __import__("pkgutil").extend_path(__path__, __name__)',
}


def _vk_join(d):
    return {k: join(v, k) for k, v in d.items()}


class ProjectDirectoryMaker(object):
    def __init__(self, nsp, pkg):
        """
        :param nsp: namespace
        :param pkg: package name
        """
        self.nsp = nsp.strip()
        self.pkg = pkg.strip()
        names = [s for s in [self.nsp, self.pkg]]
        self.names = ['-'.join(names)] + names
        testdir_name = '_'.join(['test'] + self.names[1:])
        self.common_dirs = {
            'docs': self.under_proj_dir('docs'),
            'templates': self.under_pkg_dir('templates'),
            'test': self.under_proj_dir(testdir_name),
        }
        self.common_files = _vk_join({
            '.gitignore': self.names[0],
            'requirements.txt': self.names[0],
            'MANIFEST.in': self.names[0],
            'setup.py': self.names[0],
            '__init__.py': self.under_pkg_dir(),
        })
        if self.nsp:
            p = join(self.names[0], self.nsp, '__init__.py')
            self.common_files['nsinit'] = p

    @classmethod
    def parse(cls, name):
        """
        :param name: e.g. "volkanic", "joker.superuser"
        :return: a ProjectDirectoryMaker instance
        """
        mat = re.match(r'([_A-Za-z]\w+\.)?([_A-Za-z]\w+)', name)
        if not mat:
            raise ValueError('invalid pakcage name: ' + repr(name))
        return cls(mat.group(1)[:-1] or '', mat.group(2))

    def under_proj_dir(self, *paths):
        return join(self.names[0], *paths)

    def under_pkg_dir(self, *paths):
        return join(*(self.names + list(paths)))

    def locate(self, name):
        if name.endswith('/'):
            return self.common_dirs.get(name[:-1])
        return self.common_files.get(name)

    def make_dirs(self):
        for path in self.common_dirs.values():
            os.makedirs(path, exist_ok=True)
        for path in self.common_files.values():
            open(path, 'a').close()

    def sub(self, text):
        text = text.replace('__sus_h_name', self.names[0])
        text = text.replace('__sus_i_name', '.'.join(self.names[1:]))
        text = text.replace('__sus_u_name', '_'.join(self.names[1:]))
        text = text.replace('__sus_namespace', self.nsp)
        text = text.replace('__sus_package', self.pkg)
        return text

    def gettext_setup(self, template_path):
        template_path = template_path or under_asset_dir('setup.txt')
        code = open(template_path).read()
        return self.sub(code)

    def gettext_manifest(self):
        templates_path = os.path.sep.join(self.names[1:] + ['templates'])
        return os.linesep.join([
            'include requirements.txt',
            'exclude {}/*'.format(self.common_dirs['test']),
            'recursive-include {} *.html'.format(templates_path)
        ]) + os.linesep

    def write(self, name, content):
        path = self.common_files.get(name)
        if path and content:
            with open(path, 'a') as fout:
                fout.write(content + os.linesep)

    def write_nsinit(self, approach):
        self.write('nsinit', _nsinits.get(approach))

    def write_version_variable(self):
        self.write('__init__.py', "__version__ = '0.0'")

    def write_requirements(self, lines):
        self.write('requirements.txt', os.linesep.join(lines))

    def write_setup(self, template_path=''):
        self.write('setup.py', self.gettext_setup(template_path))

    def write_manifest(self):
        self.write('MANIFEST.in', self.gettext_manifest())

    def write_gitignore(self, path=''):
        path = path or under_asset_dir('gitignore.txt')
        self.write('.gitignore', open(path).read())


def make_project(name, setup, gitignore, require, ns_approach):
    name, query = (name.split('%', maxsplit=1) + [''])[:2]
    if query == 'nsinit':
        print(_nsinits.get(ns_approach, ''))
        return
    if query == 'gitignore':
        print(open(under_asset_dir('gitignore.txt')).read())
        return

    mkr = ProjectDirectoryMaker.parse(name)
    if query == 'sub':
        print(mkr.sub(sys.stdin.read()))
        return
    if query == 'setup':
        print(mkr.gettext_setup(setup))
        return
    if query == 'manifest':
        print(mkr.gettext_manifest())
        return

    try:
        return print(mkr.locate(query) + '')
    except TypeError:
        pass

    if query:
        raise ValueError('invalid query: ' + repr(query))

    mkr.make_dirs()
    mkr.write_setup(setup)
    mkr.write_gitignore(gitignore)
    mkr.write_requirements(require or [])
    mkr.write_manifest()
    mkr.write_nsinit(ns_approach)
    mkr.write_version_variable()


def run(prog=None, args=None):
    import argparse
    desc = 'Generate a python project structure'
    # s = ' (case sensitive)'
    epilog = '\n'.join([
        format_help_section('Namespace package approaches', _nsinits),
        'About namespace packages:',
        '  https://packaging.python.org/guides/packaging-namespace-packages/',
    ])
    pr = argparse.ArgumentParser(
        prog=prog, description=desc,  epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    pr.add_argument('-n', '--ns-approach', choices=['i', 'p', 'e'],
                    default='i', help='namespace package approach')

    pr.add_argument('-s', '--setup', metavar='template_setup.py',
                    help='path to a custom setup.py template')

    pr.add_argument('-g', '--gitignore', metavar='template_gitignore.txt',
                    help='path to a custom .gitignore template')

    pr.add_argument('-r', '--require', action='append', metavar='PACKAGE',
                    help='example: -r six -r numpy>=1.0.0')

    pr.add_argument('name', metavar='[NAMESPACE.]PACKAGE_NAME[%QUERY]')
    ns = pr.parse_args(args)

    try:
        make_project(**vars(ns))
    except ValueError as e:
        print(str(e), file=sys.stderr)
