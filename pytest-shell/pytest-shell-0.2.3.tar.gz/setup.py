# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_shell', 'pytest_shell.tests']

package_data = \
{'': ['*']}

entry_points = \
{'pytest11': ['shell = pytest_shell']}

setup_kwargs = {
    'name': 'pytest-shell',
    'version': '0.2.3',
    'description': 'A pytest plugin for testing shell scripts and line-based processes',
    'long_description': '============\npytest-shell\n============\n\nA plugin for testing shell scripts and line-based processes with pytest.\n\nYou could use it to test shell scripts, or other commands that can be run\nthrough the shell that you want to test the usage of.\n\nNot especially feature-complete or even well-tested, but works for what I\nwanted it for. If you use it please feel free to file bug reports or feature\nrequests.\n\nFeatures\n--------\n\n* Easy access to a bash shell through a pytest fixture.\n* Set and check environment variables through Python code.\n* Automatically fail test on nonzero return codes by default.\n* Helpers for running shell scripts.\n* Mostly, all the great stuff pytest gives you with a few helpers to make it\n  work for bash.\n\n\nInstallation\n------------\n\nYou can install "pytest-shell" via `pip`_ from `PyPI`_::\n\n    $ pip install pytest-shell\n\nUsage\n-----\n\nYou can use a fixture called \'bash\' to get a shell process you can interact\nwith.\n\nTest a bash function::\n\n    def test_something(bash):\n        assert bash.run_function(\'test\') == \'expected output\'\n\nSet environment variables, run a .sh file and check results::\n\n    def test_something(bash):\n        with bash(envvars={\'SOMEDIR\': \'/home/blah\'}) as s:\n            s.run_script(\'dostuff.sh\', [\'arg1\', \'arg2\'])\n            assert s.path_exists(\'/home/blah/newdir\')\n            assert s.file_contents(\'/home/blah/newdir/test.txt\') == \'test text\'\n\nRun some inline script, check an environment variable was set::\n\n    def test_something(bash):\n        bash.run_script_inline([\'touch /tmp/blah.txt\', \'./another_script.sh\'])\n        assert bash.envvars.get(\'AVAR\') == \'success\'\n\nUse context manager to set environment variables::\n\n    def test_something(bash):\n        with bash(envvars={\'BLAH2\': \'something\'}):\n            assert bash.envvars[\'BLAH2\'] == \'something\'\n\nYou can run things other than bash (ssh for example), but there aren\'t specific\nfixtures and the communication with the process is very bash-specific.\n\nCreating file and directory structures\n--------------------------------------\n\npytest_shell.fs.create_files() is a helper to assemble a structure of files and\ndirectories. It is best used with the tmpdir pytest fixture so you don\'t have\nto clean up. It is used like so::\n\n    structure = [\'/a/directory\',\n                 {\'/a/directory/and/a/file.txt\': {\'content\': \'blah\'}},\n                 {\'/a/directory/and\': {\'mode\': 0o600}]\n    create_files(structure)\n\nwhich should create something like this::\n\n    |\n    + a\n       \\\n        + directory\n         \\\n          + and              # mode 600\n           \\\n            + a\n               \\\n                file.txt    # content equal to \'blah\'\n\nchroot helper\n-------------\n\nA context manager that creates a chroot environment is available through\nthe bash fixture::\n\n    with bash.chroot(tmpdir):\n        bash.send(\'mkdir /blah\')\n\nThe only reason to use this is if you need to test something that relies on a\ncertain path structure anchored at root. It is fairly flimsy, and of course\nrequires sudo. The best way to use it is with the tmpdir fixture provided by\npytest as no cleanup is done.\n\n/bin, /usr/bin, /lib and /lib64 are mounted into the chroot using a bind mount,\notherwise most things don\'t work. The chroot commands is called with --userspec\nfor the current user so the commands you run in there won\'t be run as root,\nbut nevertheless be careful and aware that the directories mounted in there are\nyour real system directories. There is no safety or security, it\'s just a\nhelper to test something that would be otherwise hard to test.\n\n\nTODO\n----\n\n* Helpers for piping, streaming.\n* Fixtures and helpers for docker and ssh.\n* Support for non-bash shells.\n* Shell instance in setup for e.g. basepath.\n\n\nRefactoring TODO\n----------------\n\n* Make Connection class just handle bytes, move line-based stuff into an\n  intermediary.\n* Make pattern stuff work line-based or on multiline streams (in a more\n  obvious way than just crafting the right regexes).\n* Make pattern stuff work on part of line if desired, leaving the rest.\n\nLicense\n-------\n\nDistributed under the terms of the `MIT`_ license, "pytest-shell" is free and\nopen source software\n\n.. _`MIT`: http://opensource.org/licenses/MIT\n.. _`pytest`: https://github.com/pytest-dev/pytest\n.. _`tox`: https://tox.readthedocs.io/en/latest/\n.. _`pip`: https://pypi.org/project/pip/\n.. _`PyPI`: https://pypi.org/project\n',
    'author': 'Daniel Murray',
    'author_email': 'daniel@darkdisco.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://hg.sr.ht/~danmur/pytest-shell',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
