# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pelican', 'pelican.plugins.pelican_jupyter_reader']

package_data = \
{'': ['*']}

install_requires = \
['nbconvert>=5.6.1,<6.0.0', 'nbformat>=4.4.0,<5.0.0', 'pelican>=4.2,<5.0']

extras_require = \
{'markdown': ['markdown>=3.1.1,<4.0.0']}

setup_kwargs = {
    'name': 'pelican-jupyter-reader',
    'version': '0.1.7',
    'description': 'Reader for ipynb files',
    'long_description': '# pelican-jupyter-reader: A Plugin for Pelican\n\nReader for ipynb files\n\nInstallation\n------------\n\nThis plugin can be installed via:\n\n    pip install pelican-jupyter-reader\n\nContributing\n------------\n\nContributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].\n\nTo start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.\n\n[existing issues]: https://github.com/chuckpr/pelican-jupyter-reader/issues\n[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html\n',
    'author': 'Chuck Pepe-Ranney',
    'author_email': 'chuck.peperanney@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chuckpr/pelican-jupyter-reader',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
