# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fsttest']

package_data = \
{'': ['*']}

install_requires = \
['blessings>=1.7,<2.0', 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['fsttest = fsttest.__main__:main']}

setup_kwargs = {
    'name': 'fsttest',
    'version': '0.2.1',
    'description': 'Test Foma FSTs',
    'long_description': 'fsttest\n=======\n\nTest your Foma FSTs!\n\nInstall\n-------\n\n    $ pip install fsttest\n\nUsage\n-----\n\nWrite `test_*.toml` scripts in a folder called `tests/`, then run:\n\n    $ fsttest\n\n\nDocumentation\n-------------\n\n * [How to specify the FST under test](./docs/fst-under-test\')\n\nTutorial\n--------\n\nIn your FST project, create a folder called `tests/`:\n\n    $ mkdir tests\n\nWithin this folder create a file called `test_{something}.toml` where\n`{something}` is something specific to your FST. For example,\n`test_phonology.toml`:\n\n    $ touch tests/test_phonology.toml\n\nUse the following template to create your test:\n\n```toml\n# tests/test_phonology.toml\n[fst]\neval = "rewrite_rules.xfscript"\ncompose = ["TInsertion", "NiTDeletion", "Cleanup"]\n\n[[tests]]\nupper = "ni<ayaa<n"\nexpect = "dayaan"\n\n[[tests]]\nlower = "ki<tayaa<n"\nexpect = "kiayaan"\n```\n\nThen run the test!\n\n    $ fsttest\n    1/1 tests passed! ✨ 🍰 ✨\n    \n\n### Line-by-line\n\nLet\'s breakdown this file, line-by-line.\n\n```toml\n[fst]\n```\n\nThis defines the **FST under test** — that is, the FST we want to use to\ntransduce and test its output.\n\n```toml\neval = "rewrite_rules.xfscript"\n```\n\nThis says that our FST under test can be created by running\n`rewrite_rules.xfscript` in Foma, creating an FST. As an example, let\'s\ntake the following `rewrite_rules.xfscript`:\n\n```xfscript\n# rewrite_rules.xfscript\ndefine Vowel    a | e | i | o | u ;\n\ndefine TInsertion [..] -> t || [n i | k i] "<" _ Vowel ;\ndefine NiTDeletion n i "<" t -> d || _ Vowel ;\ndefine Cleanup %< -> 0 ;\n```\n\nYours will be different!\n\n```toml\ncompose = ["TInsertion", "NiTDeletion"]\n```\n\nThis line says that the **FST under test** is the result of _composing_\nthe `TInsertion` regex with the `NiTDeletion` regex. That is, the FST\nputs its input into `TInsertion` and then passes the result to\n`NiTDeletion`. The result of passing it through both FSTs is the result\nwe want to test.\n\n```toml\n[[tests]]\n```\n\nNext we define one or more test cases. Begin every test case with\n`[[tests]]`: note the **two square brackets**!\n\n```toml\nupper = "ni<ayaa<n"\n```\n\nThis test case feeds the string `ni<ayaa<n` into the upper side of the\nFST. The upper side is conventionally the **analysis** side of the FST.\n\n```toml\nexpect = "dayaan"\n```\n\nThis says that we **expect** the lower side to be `dayaa<n`. That is,\nthis test case says that, given the analysis `ni<ayaa<n`, the FST should\nproduce `dayaa<n` among the possible **surface forms**.\n\n```toml\n[[tests]]\n```\n\nNext, we define another test case.\n\n```toml\nlower = "kitayaan"\n```\n\nIn contrast to the previous test, we feed the input to the **lower**\nside of the FST. In other words, we want to do a **lookup**.\nConventionally, this means we\'re providing a **surface form**, and\nasking the FST to return an analysis.\n\n```toml\nexpect = "ki<ayaa<n"\n```\n\nThis means we\'re **expecting** the analysis of `ki<tayaa<n` when we give\nthe FST the wordform of `kitayaan`\n\n\nLicense\n=======\n\nWritten in 2020 by Eddie Antonio Santos <Eddie.Santos@nrc-cnrc.gc.ca>.\n\nLicensed under the terms of the Mozilla Public License 2.0 (MPL-2.0).\n',
    'author': 'Eddie Antoio Santos',
    'author_email': 'Eddie.Santos@nrc-cnrc.gc.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/eddieantonio/fsttest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
