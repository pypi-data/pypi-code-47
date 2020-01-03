"""C-Choir installation configuration."""
from pathlib import Path
from re import compile as re_compile
from subprocess import CalledProcessError
from subprocess import DEVNULL
from subprocess import check_output

from setuptools import setup


def get_git_version():
    """Get package version from git tags."""
    pattern = re_compile(
        r'^v(?P<version>\d*\.\d*\.\d*)(-\d*-g(?P<commit>\d*))?'
    )
    try:
        command = [
            'git', 'describe',
            '--tags',
            '--match', 'v[0-9]*.[0-9]*.[0-9]*'
        ]
        version = check_output(command, stderr=DEVNULL)
        version = version.decode('utf-8')
        match = pattern.match(version)
        commit = match.group('commit')
        version = match.group('version')
        if commit is not None:
            version = '{}.dev{}'.format(version, commit)
    except CalledProcessError:
        version = '0.0.0'
    return version.rstrip()


setup(
    name="cchoir",
    description="Lightweight container orchestrator using LXD",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    version=get_git_version(),
    keywords=['LXD', 'container', 'deployment'],
    packages=[
        'cchoir',
        'cchoir.commands',
    ],
    entry_points={
        'console_scripts': [
            'cchoir = cchoir.cli:main'
        ],
    },
    license='WTFPL',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        'aiolxd',
        'pofy'
    ],
    author="An Otter World",
    author_email="an-otter-world@ki-dour.org",
    url="http://github.com/an-otter-world/cchoir/",
    zip_safe=False,
)
