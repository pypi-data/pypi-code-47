# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['yamltable']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=5.2,<6.0']

entry_points = \
{'console_scripts': ['yamltable = yamltable.main:main']}

setup_kwargs = {
    'name': 'yamltable',
    'version': '0.0.1',
    'description': 'Command line utility for list organized YAML files.',
    'long_description': '# YamlTable \n\n![](https://github.com/wolfgangwazzlestrauss/yamltable/workflows/build/badge.svg)\n\nYamlTable is a Python command line utility for working with YAML files organized similar to a\nrelational database table. It supports YAML files organized as a list of dictionaries, which share\nkey names and value types. YamlTable provides commands for listing, searching, sorting, etc. data\nfrom the supported files.\n\n\n## Getting Started\n\n### Installation\n\nYamlTable can be installed for Python 3.7+ with `pip`.\n\n```bash\npip install --user yamltable\n```\n\n### Commands\n\n\n\n## Contributing\n\nSince YamlTable is in an early development phase, it is not currently open to contributors.\n\n\n## License\n\nLicensed under the [MIT](license.txt) license.\n\n',
    'author': 'Macklan Weinstein',
    'author_email': 'wolfgangwazzlestrauss@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/wolfgangwazzlestrauss/yamltable',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
