# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ofx_processor']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'ofxtools>=0.8.20,<0.9.0']

entry_points = \
{'console_scripts': ['ofxprocessor = ofx_processor.main:cli']}

setup_kwargs = {
    'name': 'ofx-processor',
    'version': '0.1.4',
    'description': 'Personal ofx processor',
    'long_description': '# ofx-processor\n\n## Usage\n\n```bash\nofxprocessor /path/to/ofxfile.ofx\n```\n\nIt will write a `processed.ofx` file in the same folder.\n\nIt will not overwrite the original ofx file.\n',
    'author': 'Gabriel Augendre',
    'author_email': 'gabriel@augendre.info',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
