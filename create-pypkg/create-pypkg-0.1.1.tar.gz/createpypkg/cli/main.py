#!/usr/bin/env python
"""
Python Package Scaffold Builder

Usage:
    create-pypkg -h|--help
    create-pypkg --version
    create-pypkg [--debug|--info] [--module=<name>] <path>

Options:
    -h, --help          Print help and exit
    --version           Print version and exit
    --debug, --info     Execute a command with debug|info messages
    --module=<name>     Specify a module name

Arguments:
    <path>              Path to a directory for a new repository directory
"""

import logging
import os
import re
from pathlib import Path

from docopt import docopt

from .. import __version__
from .util import (fetch_description_from_readme, fetch_git_config, print_log,
                   render_template, set_log_config)


def main():
    args = docopt(
        __doc__, version='create-pypkg {}'.format(__version__)
    )
    set_log_config(debug=args['--debug'], info=args['--info'])
    logger = logging.getLogger(__name__)
    logger.debug('args:{0}{1}'.format(os.linesep, args))
    _create_python_package_scaffold(args=args)


def _create_python_package_scaffold(args, include_package_data=True,
                                    create_dockerfile=True):
    repo_path = Path(args['<path>']).resolve()
    package_name = args['--module'] or repo_path.name
    package_path = repo_path.joinpath(re.sub(r'[\.\-]', '', package_name))
    if not repo_path.is_dir():
        raise FileNotFoundError('No such directory: {}'.format(repo_path))
    elif not package_path.is_dir():
        print_log('Make a directory:\t{}'.format(package_path))
        package_path.mkdir()
    else:
        pass
    readme_md_path = repo_path.joinpath('README.md')
    if readme_md_path.is_file():
        description = fetch_description_from_readme(
            md_path=str(readme_md_path)
        )
    else:
        description = ''
        render_template(
            data={'package_name': package_name},
            output_path=str(readme_md_path)
        )
    data = {
        'package_name': package_name, 'module_name': package_path.name,
        'include_package_data': str(include_package_data),
        'version': 'v0.0.1', 'description': description,
        **fetch_git_config(repo_path=str(repo_path))
    }
    gitignore = repo_path.joinpath('.gitignore')
    if not gitignore.is_file():
        render_template(
            output_path=str(gitignore), template='Python.gitignore'
        )
    dest_files = [
        'setup.py',
        *[(package_path.name + '/' + n) for n in ['__init__.py', 'cli.py']],
        'MANIFEST.in', 'Dockerfile', 'docker-compose.yml'
    ]
    for f in dest_files:
        render_template(output_path=str(repo_path.joinpath(f)), data=data)
    dockerignore = repo_path.joinpath('.dockerignore')
    if not dockerignore.is_file():
        print_log('Create a symlink:\t{}'.format(dockerignore))
        os.symlink('.gitignore', str(dockerignore))
