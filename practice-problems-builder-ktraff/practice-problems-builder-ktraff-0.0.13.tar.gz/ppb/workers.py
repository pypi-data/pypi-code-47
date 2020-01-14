# MIT License

# Copyright (c) [year] [fullname]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import logging
import re
import os
import subprocess
from pkg_resources import resource_filename
from typing import List

import yaml
from jinja2 import Environment, PackageLoader

from ppb.exceptions import NotImplementedException, DependenciesNotMetException
from ppb.logging import setup_logger, set_log_level

_log = setup_logger(__name__)
_j2 = Environment(
    loader=PackageLoader('ppb', 'templates'),
)


def _check_if_executables_exist(*executables):
    for executable in executables:
        _log.info(f'Checking whether {executable} is installed.')
        output = subprocess.run(['which', executable], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        _log.debug(output)
        if executable not in output:
            raise DependenciesNotMetException(f'No suitable "{executable}" found. Please install and try again.')


def _check_python_dependencies(python_version):
    _check_if_executables_exist(python_version, 'virtualenv', 'make')


def _check_rust_dependencies():
    _check_if_executables_exist('rustup', 'rustc', 'cargo')
    version_info = subprocess.run(['rustc', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
    _log.debug(version_info)
    if not version_info:
        raise DependenciesNotMetException('rustc appears to be installed incorrectly.')


def _check_golang_dependencies():
    _check_if_executables_exist('go')


def _setup_python(problem_path: str):
    _log.info('Creating virtual environment for python')
    _log.debug(subprocess.run(
        ['make', 'venv_create'],
        stdout=subprocess.PIPE,
        cwd=os.path.join(problem_path, 'python')
    ).stdout.decode('utf-8'))
    _log.info('Building practice problems')
    _log.debug(subprocess.run(
        ['make', 'build'],
        stdout=subprocess.PIPE,
        cwd=os.path.join(problem_path, 'python')
    ).stdout.decode('utf-8'))


def _setup_rust():
    pass


def _setup_golang():
    pass


class Worker:

    def run(self):
        raise NotImplementedException()

    def _get_config(self, path: str):
        with open(os.path.join(path, 'config.yml'), 'r') as infile:
            return yaml.safe_load(infile.read())


class TemplateGenerator:
    """Helps workers to generate jinja templates.

    This class is intended to be used as a mixin for worker classes.
    """

    def _include_templates(self, path: str):
        """By default, every template is included.  Override this in your class to modify it's behavior."""
        return True

    def _generate_templates(
        self,
        template_args: dict,
        template_path: str,
        destination_path: str,
    ) -> None:
        """Walks a directory containing templates and renders them to a destination path.

        Args:
            - template_args: a list of variables to be passed into jinja templates during rendering.
            - template_path: the absolute path to the root folder where templates exist.  This path is
                             relative to the root path of the `_j2` template loader.
            - destination_path: where to save the templates
        """
        full_template_path = resource_filename('ppb', f'templates/{template_path}')
        for subdir, dirs, files in os.walk(full_template_path):
            relative_path = re.sub(re.compile(f'{full_template_path}/?'), '', subdir)
            # Substitute any variable names in paths
            interpolated_path = relative_path.format(**template_args)
            if self._include_templates(relative_path):
                for a_dir in dirs:
                    if self._include_templates(os.path.join(relative_path, a_dir)):
                        dir_path = os.path.join(destination_path, interpolated_path, a_dir.format(**template_args))
                        _log.debug(f'Creating directory {dir_path}')
                        os.makedirs(dir_path)
                for a_file in files:
                    template = _j2.get_template(os.path.join(template_path, relative_path, a_file))
                    # Remove the .j2 extension when saving the template to the destination
                    dest_file = re.sub(r'.j2$', '', a_file)
                    dest_path = os.path.join(destination_path, interpolated_path, dest_file)
                    with open(dest_path, 'w') as outfile:
                        _log.debug(f'Writing template {dest_path}')
                        outfile.write(template.render(**template_args))


class LogWorker(Worker):

    def __init__(self, debug=False):
        super().__init__()
        self.debug = debug

    def run(self):
        if self.debug:
            set_log_level(logging.DEBUG)
        else:
            set_log_level(logging.INFO)
        _log.debug(f'Logging initialized for level {logging.getLevelName(_log.getEffectiveLevel())}')


class LanguageSetupMixin:
    """Used to setup dependencies for workers that use multiple languages."""

    def _check_dependencies(self):
        if 'python' in self.languages:
            _check_python_dependencies(self.python_version)
        if 'rust' in self.languages:
            _check_rust_dependencies()
        if 'golang' in self.languages:
            _check_golang_dependencies()

    def _setup_languages(self):
        """Configures each programming languages with necessary tools and environment"""
        if 'python' in self.languages:
            _setup_python(self.problem_path)
        if 'rust' in self.languages:
            _setup_rust()
        if 'golang' in self.languages:
            _setup_golang()



class NewProblemWorker(Worker, TemplateGenerator, LanguageSetupMixin):
    """Creates a workspace for a new practice problem"""

    def __init__(
            self,
            problem_name: str,
            languages: List[str],
            target: str,
            title: str,
            description: str,
            difficulty: int,
            tags: List[str],
            resources: List[str],
            python_version: str,
            author_name: str,
            author_email: str,
            rust_compiler_edition: str,
            github_username: str
    ):
        super().__init__()
        self.problem_name = problem_name
        self.languages = languages
        self.target = target
        self.title = title
        self.description = description
        self.difficulty = difficulty
        self.tags = tags
        self.resources = resources
        self.python_version = python_version
        self.author_name = author_name
        self.author_email = author_email
        self.rust_compiler_edition = rust_compiler_edition
        self.github_username = github_username

    @property
    def problem_path(self):
        return f'{os.path.join(self.target, self.problem_name)}'

    def _include_templates(self, relative_path: str):
        """Returns True if the path to the provided template should be included when generating a new practice problem.

        Templates for languages that have not been included will be skipped.

        Arguments:
            relative_path (str): A path to a template directory, relative to the root of the template folder.
                                 This path shouldn't have any variable interpolation done on it, i.e. variable
                                 names in the path like "{problem_name}" should be passed without any substitutions
                                 made on them.
        """
        match = re.match(r'\{problem_name\}\/(python|golang|rust)', relative_path)
        if match:  # We are parsing a template folder for a specific language
            if match.group(1) in self.languages:
                return True
            return False
        return True

    def _create_workspace(self):
        """The main function for creating a new practice problem in the target destination"""
        template_args = {
            'problem_name': self.problem_name,
            'title': self.title,
            'description': self.description,
            'difficulty': self.difficulty,
            'tags': self.tags,
            'resources': self.resources,
            'python_version': self.python_version,
            'author_name': self.author_name,
            'author_email': self.author_email,
            'github_username': self.github_username,
            'rust_compiler_edition': self.rust_compiler_edition,
            'target': self.target,
        }
        self._generate_templates(template_args, 'create', self.target)    

    def run(self):
        _log.info(
            f'Creating a new problem "{self.problem_name}" with {", ".join(self.languages)} '
            f'into {self.problem_path}'
        )
        self._check_dependencies()
        self._create_workspace()
        self._setup_languages()


class AddProblemWorker(Worker, TemplateGenerator, LanguageSetupMixin):
    """Generates language template(s) for an existing practice problem."""

    def __init__(
        self,
        languages: List[str],
        target: str,
        python_version: str,
        rust_compiler_edition: str,
        github_username: str
    ):
        super().__init__()
        self.languages = languages
        self.target = target
        self.python_version = python_version
        self.rust_compiler_edition = rust_compiler_edition
        self.github_username = github_username

    def _create_workspace(self):
        template_args = self._get_config(self.target)
        template_args['python_version'] = self.python_version
        template_args['rust_compiler_edition'] = self.rust_compiler_edition
        template_args['github_username'] = self.github_username
        template_args['target'] = self.target
        for language in self.languages:
            dest_path = os.path.join(self.target, language)
            os.makedirs(dest_path)
            self._generate_templates(template_args, f'create/{{problem_name}}/{language}', dest_path)

    def run(self):
        _log.info(f'Adding {", ".join(self.languages)} to {self.target}')
        self._check_dependencies()
        self._create_workspace()
        self._setup_languages()
