# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oapilib', 'oapilib.core']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.7.8,<0.8.0',
 'loguru>=0.3.2,<0.4.0',
 'pout>=0.7.9,<0.8.0',
 'pretty-json>=1.2,<2.0',
 'pydantic>=1.0,<2.0',
 'pygments>=2.4,<3.0',
 'structlog>=19.2,<20.0',
 'typing-extensions>=3.7,<4.0']

entry_points = \
{'console_scripts': ['oapi = cli.main:program.run']}

setup_kwargs = {
    'name': 'oapilib',
    'version': '0.0.1',
    'description': 'Toolkit for building clients of OGC API family of standards',
    'long_description': '# OAPILib\n\n## description\n\nTBD\n\n## Notes\n\napi.py\n------\n\n# import sys\n\n\n# from .util import StreamToLogger, jsonify\n\n# sys.stdout = StreamToLogger()\n\n\nclient.py\n---------\n\n# from httpx.models import BaseResponse\n\n# from typing_extensions import Literal\n\ncli/config.py\n---------\n\n# import sys\n\n# from loguru import logger\n\ncore/config.py\n--------------\n',
    'author': 'Francesco Bartoli',
    'author_email': 'xbartolone@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
