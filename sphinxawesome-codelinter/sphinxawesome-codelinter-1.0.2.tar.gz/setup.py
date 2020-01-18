# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sphinxawesome', 'sphinxawesome.codelinter']

package_data = \
{'': ['*']}

install_requires = \
['sphinx>=2.0,<3.0']

setup_kwargs = {
    'name': 'sphinxawesome-codelinter',
    'version': '1.0.2',
    'description': 'A Sphinx extension that enables running linters over code blocks',
    'long_description': "# Sphinx Awesome Codelinter\n\n[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)\n[![PyPI version](https://img.shields.io/pypi/v/sphinxawesome-codelinter)](https://img.shields.io/pypi/v/sphinxawesome-codelinter)\n[![Test Status](https://img.shields.io/github/workflow/status/kai687/sphinxawesome-codelinter/Run%20unit%20tests%20against%20different%20versions%20of%20Python?label=tests)](https://img.shields.io/github/workflow/status/kai687/sphinxawesome-codelinter/Run%20unit%20tests%20against%20different%20versions%20of%20Python?label=tests)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nThis extension for the Sphinx documentation suite allows you to iterate over code blocks\nand expose them to an external tool. This can be used to make sure, that code blocks are\nvalid. For more information about the Sphinx project, visit the website at\nhttp://www.sphinx-doc.org/.\n\nThis extension provides a new builder, `sphinx-build -b codelinter`.\n\n## Installation\n\nInstall the extension:\n\n```console\npip install sphinxawesome-codelinter\n```\n\nThis Sphinx extension should work with Python versions newer than 3.6 and recent Sphinx\nreleases. Unit tests are being run against Python 3.6, 3.7, 3.8 and Sphinx 2.0, 2.1,\n2.2, and 2.3.\n\n## Configuration\n\nTo enable this extension in Sphinx, add it to the list of extensions in the Sphinx\nconfiguration file `conf.py`:\n\n```python\nextensions = ['sphinxawesome.codelinter']\n```\n\nThe extension is configured via the `codelinter_languages` dictionary, which is empty by\ndefault. That is, no code blocks will be processed unless you provide the language and\nthe tool to process the language as a key/value pair. For example, to pass all JSON\nblocks to the python builtin JSON module, use:\n\n```python\ncodelinter_languages = {\n  'json': 'python -m json.tool'\n}\n```\n\nwhich would return an error for non-valid JSON code. For linting YAML code blocks, you\ncould install the `yamllint` tool and then add:\n\n```python\ncodelinter_languages = {\n  'yaml': 'yamllint -'\n}\n```\n\nThe `-` tells yamllint to read from `stdin`. You can also write your own tools, that can\nread from `stdin` and write to `stdout` or `stderr`. The only expectation is that any\ntools retun a value of 0, ifcno errors were found, a non-zero value otherwise.\n\nAfter configuring the extension, you can use `sphinx-build -b codelinter ...` like other\nSphinx builders. No output will be written to disk. If the linter exits with a non-zero\nreturn value, a warning will be logged. You can use the `sphinx-build -W` option to turn\nthose warnings into errors to stop the build process.\n\nYou can use any reStructuredText directive, that gets parsed as a `literal_block` node.\nFor example, you can use `.. code-block:: json` as well as `.. highlight:: json`.\n\nYou can also use the `..literalinclude:: <filename>` directive, to include code from\nfiles.\n\n```\n.. literalinclude:: code.json\n   :language: json\n```\n\n**Caution:** The value of the `codelinter_languages` dictionary will be used as\nprovided. No additional safe-guards are in place to prevent abuse.\n",
    'author': 'Kai Welke',
    'author_email': '17420240+kai687@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
