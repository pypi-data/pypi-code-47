# /usr/bin/env python3

from functools import lru_cache
from pathlib import Path
from shutil import rmtree

from setuptools import Command
from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install

PROJECT_NAME = 'dfmpy'
PROJECT_VERSION = '0.0.4'


@lru_cache(maxsize=2)
def get_repo_file_name(filename):
    """
    Returns the filename that is relative to the project directory as an
    absolute file path.

    :param Path|str filename: The relative file path.

    :rtype: str
    :return: The absolute path to the specified file.
    """
    project_directory = Path(__file__).resolve().parent
    filename = project_directory.joinpath(filename)
    return filename


@lru_cache(maxsize=2)
def read_repo_file(filename):
    """
    Reads the specified file and returns the full contents as a single string.

    :param Path|str filename: The file to read.

    :rtype: str
    :return: The full contents of the specified file.
    """
    filename = get_repo_file_name(filename)
    with open(filename) as f:
        return f.read()


def load_requirements(filename):
    """
    Loads the :code:`requirements.tx` dependency file and returns the
    dependencies as a sequence.

    The file can contain comments that follow the pound symbol (eg. '#').
    Comments will be removed, each line is stripped of leading and trailing
    whitespace, and empty lines are deleted.  Other than these basic
    transformations, the requirements are left intact.

    :param Path|str filename: The requirements file to read.

    :rtype: tuple
    :return: A sequence of requirements.
    """
    reqs = read_repo_file(filename).splitlines()
    reqs = [str(x).strip() for x in reqs]
    reqs = [x[:x.find('#')] for x in reqs if '#' in x]
    reqs = [x for x in reqs if len(x)]
    return tuple(reqs)


def get_dfmpy_packages():
    """
    Finds all packages within this project and only returns the production ready
    ones.  Meaning, test packages will not be included.

    :rtype tuple
    :return: A sequence of package names that will be built into the file
            distribution.
    """
    packages = find_packages()
    packages = [p for p in packages if not p.endswith('_test')]
    return tuple(packages)


class CleanCommand(Command):
    """
    A custom clean command that removes any intermediate build directories.
    """

    description = 'Custom clean command that forcefully removes build, dist,' \
                  ' and other similar directories.'
    user_options = []

    def __init__(self, *args, **kwargs):
        """Initialized the custom clean command with a list of directories."""
        super(CleanCommand, self).__init__(*args, **kwargs)
        project_path = Path(__file__).resolve().parent
        self._clean_paths = {'.eggs',
                             'build',
                             PROJECT_NAME + '.egg-info',
                             'dist',
                             }
        self._clean_paths = {project_path.joinpath(p)
                             for p in self._clean_paths}
        self._clean_paths = {d for d in self._clean_paths if d.exists()}

    def initialize_options(self):
        """Unused, but required when implementing :class:`Command`."""
        pass

    def finalize_options(self):
        """Unused, but required when implementing :class:`Command`."""
        pass

    def run(self):
        """Performs the actual removal of the intermediate build directories."""
        for d in self._clean_paths:
            print(f'Removing {d}')
            rmtree(d)


class InstallCommand(install):
    """
    Custom command to install dependencies cause setuptools sucks balls and does
    not honor the "install_requires" parameter.  Apparently the default
    functionality is to run in backward-compatibile mode, which does not install
    the project's dependencies  :-(

    @see https://github.com/pypa/setuptools/issues/456#issuecomment-202922033
    """
    def run(self):
        """
        Performs the installation of dependencies, based on the
        :code:`requirements.txt` and :code:`requirements-test.txt` files.
        """
        # Need to run the original "install" first.
        super().run()

        # Not sure why, but moving these up to the top-level, and use the
        # "from PACKAGE import NAME" format, did not work.
        import subprocess
        import sys
        files = ('requirements.txt', 'requirements-test.txt')
        files = [get_repo_file_name(f) for f in files]
        for req_file in files:
            print(f'Installing dependencies from: {req_file}')
            process = subprocess.Popen(['pip3', 'install', '-r', req_file],
                                       stdout=subprocess.PIPE)
            for c in iter(lambda: process.stdout.read(1), b''):
                sys.stdout.write(c.decode('UTF-8'))


setup(name=PROJECT_NAME,
      version=PROJECT_VERSION,
      author='Mike Durso',
      author_email='rbprogrammer@gmail.com',
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Natural Language :: English',
          'Operating System :: MacOS',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Operating System :: Unix',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities',
      ],
      cmdclass={
          'clean': CleanCommand,
          'install': InstallCommand,
      },
      description='Another dotfiles manager.',
      entry_points={
          'console_scripts': [
              'dfmpy = dfmpy.__main__:main',
          ]
      },
      install_requires=load_requirements('requirements.txt'),
      long_description=read_repo_file('README.md'),
      long_description_content_type='text/markdown',
      packages=get_dfmpy_packages(),
      package_data={'dfmpy.resources': ['*']},
      test_suite='dfmpy_test',
      tests_require=load_requirements('requirements-test.txt'),
      url='https://gitlab.com/rbprogrammer/dfmpy',
      )
