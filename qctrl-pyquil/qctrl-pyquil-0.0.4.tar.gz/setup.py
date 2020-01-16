# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qctrlpyquil']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.16,<2.0',
 'pyquil>=2.9,<3.0',
 'qctrl-open-controls>=4.0.0,<5.0.0',
 'scipy>=1.3,<2.0',
 'toml>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'qctrl-pyquil',
    'version': '0.0.4',
    'description': 'Q-CTRL pyQuil Adapter',
    'long_description': "# Q-CTRL pyQuil Adapter\n\nThe aim of the Q-CTRL pyQuil Adapter package is to provide export functions allowing\nusers to deploy established error-robust quantum control protocols from the\nopen literature and defined in Q-CTRL Open Controls on Rigetti quantum hardware \nand simulators.\n\nAnyone interested in quantum control is welcome to contribute to this project.\n\n\n## Table of Contents\n\n- [Installation](#installation)\n- [Usage](#usage)\n- [Contributing](#contributing)\n- [Credits](#credits)\n- [License](#license)\n\n## Installation\n\nQ-CTRL pyQuil Adapter can be installed through `pip` or from source. We recommend\nthe `pip` distribution to get the most recent stable release. If you want the\nlatest features then install from source.\n\n### Requirements\n\nTo use Q-CTRL pyQuil Adapter you will need an installation of Python. We\nrecommend using the [Anaconda](https://www.anaconda.com/) distribution of\nPython. Anaconda includes standard numerical and scientific Python packages\nwhich are optimally compiled for your machine. Follow the [Anaconda\nInstallation](https://docs.anaconda.com/anaconda/install/) instructions and\nconsult the [Anaconda User\nguide](https://docs.anaconda.com/anaconda/user-guide/) to get started.\n\nWe use interactive jupyter notebooks for our usage examples. The Anaconda\npython distribution comes with editors for these files, or you can [install the\njupyter notebook editor](https://jupyter.org/install) on its own.\n\n### Using PyPi\n\nUse `pip` to install the latest version of Q-CTRL pyQuil Adapter.\n\n```shell\npip install qctrl-pyquil\n```\n\n### From Source\n\nThe source code is hosted on\n[Github](https://github.com/qctrl/python-pyquil). The repository can be\ncloned using\n\n```shell\ngit clone git@github.com:qctrl/python-pyquil.git\n```\n\nOnce the clone is complete, you have two options:\n\n1. Using setup.py\n\n   ```shell\n   cd python-pyquil\n   python setup.py develop\n   ```\n\n   **Note:** We recommend installing using `develop` to point your installation\n   at the source code in the directory where you cloned the repository.\n\n1. Using Poetry\n\n   ```shell\n   cd python-pyquil\n   ./setup-poetry.sh\n   ```\n\n   **Note:** if you are on Windows, you'll need to install\n   [Poetry](https://poetry.eustace.io) manually, and use:\n\n   ```bash\n   cd python-pyquil\n   poetry install\n   ```\n\nOnce installed via one of the above methods, test your installation by running\n`pytest`\nin the `python-pyquil` directory.\n\n```shell\npytest\n```\n\n## Usage\n\nSee the [Jupyter notebooks](https://github.com/qctrl/notebooks/tree/master/qctrl-open-controls).\n\n## Contributing\n\nFor general guidelines, see [Contributing](https://github.com/qctrl/.github/blob/master/CONTRIBUTING.md).\n\n### Building documentation\n\nDocumentation generation relies on [Sphinx](http://www.sphinx-doc.org). Automated builds are done by [Read The Docs](https://readthedocs.com).\n\nTo build locally:\n\n1. Ensure you have used one of the install options above.\n1. Execute the make file from the docs directory:\n\n    If using Poetry:\n\n    ```bash\n    cd docs\n    poetry run make html\n    ```\n\n    If using setuptools:\n\n    ```bash\n    cd docs\n    # Activate your virtual environment if required\n    make html\n    ```\n\nThe generated HTML will appear in the `docs/_build/html` directory.\n\n## Credits\n\nSee\n[Contributors](https://github.com/qctrl/python-pyquil/graphs/contributors).\n\n## License\n\nSee [LICENSE](LICENSE).\n",
    'author': 'Q-CTRL',
    'author_email': 'support@q-ctrl.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/qctrl/python-pyquil',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.4,<3.9',
}


setup(**setup_kwargs)
