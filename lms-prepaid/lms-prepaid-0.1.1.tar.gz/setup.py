# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lms_prepaid']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'requests>=2.22.0,<3.0.0', 'tritise>=0.1.0,<0.2.0']

entry_points = \
{'console_scripts': ['lms-prepaid = lms_prepaid.lms_prepaid:query']}

setup_kwargs = {
    'name': 'lms-prepaid',
    'version': '0.1.1',
    'description': 'A script to query Last Mile Solutions prepaid card values',
    'long_description': '# lms-prepaid\n\nA python script to retrieve balances for last mile solutions electric car charging prepaid card (this includes Entega prepaid cards)\n\n## Installation\n\n`pip install lms-prepaid`\n\n## Development\n\n`lms-prepaid` uses [poetry](https://python-poetry.org/)\n\n## Usage\n\n`lms-prepaid -c AB-123456-X`\n\nSee also: `lms-prepaid --help`\n\n### Poetry setup\n\n- Install poetry: `pip install poetry` (see the poetry homepage for alternatives)\n- Install `lms-prepaid`: `poetry install`\n- Run: `poetry run lms-prepaid --help`\n\n\n## Environment variables\n\nThe script will use the following environment variables:\n\n- `LMS_PREPAID_DATABASE` for the path to the sqlite database\n  - defaults to `lms-prepaid.sqlite` int the CWD\n- `LMS_PREPAID_CARD` for the card number\n- `LMS_PREPAID_GOTIFY_URL` for the gotify notification server\n- `LMS_PREPAID_GOTIFY_TOKEN` for the gotify app token\n- `LMS_PREPAID_GOTIFY_PRIO` for the gotify notification priority\n\n## Docker usage\n\n- Build the docker image:\n  - `docker build -t lms-prepaid .`\n- Launch the image with with set environment variables:\n  - `docker run -e LMS_PREPAID_CARD=AB-CDE-123456-X lms-prepaid`',
    'author': 'asmw',
    'author_email': 'asmw@asmw.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/asmw/lms-prepaid',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
