from setuptools import setup, find_packages
import distutils
import os

class LocalesCommand(distutils.cmd.Command):
    description='compile locale files'
    def run(self):
        command = ["make" "update-langs"]
        subprocess.check_call(command)


version_file = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'offlate', 'VERSION'))
version = version_file.read().strip()

setup (
    name="offlate",
    version=version,
    packages=find_packages(exclude=['.guix-profile*']),
    python_requires = '>=3',
    install_requires=['polib', 'ruamel.yaml', 'python-dateutil', 'PyQt5', 'pygit2',
        'python-gitlab', 'translation-finder', 'android-stringslib', 'watchdog',
        'PyGithub', 'lxml', 'pyenchant'],
    entry_points={
        'gui_scripts': [
            'offlate=offlate.ui.main:main',
        ]
    },

    package_data={'offlate': ['data.json', 'locales/*.qm', 'locales/*.ts', 'icon.png', 'VERSION']},
    cmdclass={
        'locales': LocalesCommand,
    },

    author="Julien Lepiller",
    author_email="julien@lepiller.eu",
    description="Offline translation interface for online translation tools.",
    long_description="""Offlate is a graphical interface designed for translators
of free and open source software.  Software projects in the free software community
use a wide range of online platforms (or no platform at all) to manage their
translations.  Offlate is able to connect to many different platforms, copy the
translations locally, and let you work on them on your computer, offline and in
a unified interface.""",
    license="GPLv3+",
    keywords="translation",
    url="https://framagit.org/tyreunom/offlate",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Localization',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],
    project_urls={
        "Bug Tracker": "https://framagit.org/tyreunom/offlate/issues",
        "Source Code": "https://framagit.org/tyreunom/offlate",
        #"Documentation": "https://docs.example.com/HelloWorld/",
    },
)
