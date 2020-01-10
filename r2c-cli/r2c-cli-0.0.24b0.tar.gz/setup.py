# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['r2c', 'r2c.cli', 'r2c.cli.commands']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'docker>=3.7,<4.0',
 'jsondiff>=1.1,<2.0',
 'r2c-lib==0.0.19-beta.2',
 'requests>=2.0,<3.0',
 'semantic-version>=2.6,<3.0']

entry_points = \
{'console_scripts': ['r2c = r2c.cli.__main__:main']}

setup_kwargs = {
    'name': 'r2c-cli',
    'version': '0.0.24b0',
    'description': 'A CLI for R2C',
    'long_description': '# r2c-cli\n\nThis is the CLI for interacting with the R2C platform.\n\n## Installation\n\n### Prerequisites\n\n- [Install Docker](https://docs.docker.com/install/) for your platform\n- [Python 3.7 and up](https://www.python.org/about/gettingstarted/) for your platform\n\n### Setup\n\n- Install r2c-cli, either via `pip` or via [`pipx`](https://pypi.org/project/pipx/) to provide better package isolation.\n\n  ```\n  pip3 install r2c-cli\n  ```\n\n- Run `r2c` to check that the CLI was installed properly. If installed properly, you should see our help text.\n\n## Documentation\n\nSee [docs.r2c.dev](https://docs.r2c.dev) for details on how write analyzer using `r2c-cli`.\n\n## Usage\n\n```bash\nr2c <command> [options]\n```\n\nYou can also run `r2c --help` or just `r2c` to see usage information.\n\nFor help with a command in particular, you can run `r2c <command> --help` and see help specifically for that command.\n\nFor the commands `run` `test` `push` and `unittest` they will require that you run them in an analyzer directory (i.e. a directory containing an `analyzer.json` and associated files).\n\n## Unit Testing\n\nInstructions to run unittests are defined `src/unittest.sh`. Make sure to add `mocha test` or `npm test` to enable\nunittesting for your analyzer.\n\n## Integration Testing\n\nIntegration tests should be defined in the `src/examples` directory.\nIntegration test on a github REPO@COMMIT could be defined as\n\n```json\n{\n  "target": "{REPO}",\n  "target_hash": "{COMMIT}",\n  "expected": []\n}\n```\n\n## Uploading new analyzer\n\nOnce you are done developing and testing your analyzer locally, you must update `version` in your\n`analyzer.json` and run\n\n```bash\nr2c push\n```\n\nto upload your analyzer to your repository.\n\n## Troubleshooting\n\n- If you run into issues running `r2c` commands, you can run with `--verbose` flag and reach out to `support@ret2.co` with the error log.\n',
    'author': 'R2C',
    'author_email': 'cli@ret2.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://ret2.co',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
