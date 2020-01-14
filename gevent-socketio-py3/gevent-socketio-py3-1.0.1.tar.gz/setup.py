import os

from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

def get_reqs(*fns):
    lst = []
    for fn in fns:
        for package in open(os.path.join(CURRENT_DIR, fn)).readlines():
            package = package.strip()
            if not package:
                continue
            lst.append(package.strip())
    return lst

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        pytest.main(self.test_args)

setup(
    name="gevent-socketio-py3",
    version="1.0.1",
    description=(
        "SocketIO server based on the Gevent pywsgi server, "
        "a Python network library for Python 3"),
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Henok Alem",
    author_email="alemaye3@gmai.com",
    maintainer="Henok Alem",
    maintainer_email="alemaye3@gmail.com",
    license="BSD",
    url="https://github.com/henokalem/gevent-socketio-py3",
    download_url="https://github.com/henokalem/gevent-socketio-py3",
    install_requires=get_reqs('pip-requirements.txt'),
    setup_requires=('versiontools >= 1.7'),
    cmdclass = {'test': PyTest},
    tests_require=get_reqs('pip-requirements-test.txt'),
    packages=find_packages(exclude=["examples", "tests"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
    entry_points="""

    [paste.server_runner]
    paster = socketio.server:serve_paste

    """,
)
