# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['quantized']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=19.3,<20.0',
 'cattrs>=1.0,<2.0',
 'click>=7.0,<8.0',
 'joblib>=0.14.1,<0.15.0',
 'loguru>=0.4.0,<0.5.0',
 'matplotlib>=3.1,<4.0',
 'numba>=0.43.0,<0.44.0',
 'numpy>=1.17,<2.0',
 'scipy>=1.3,<2.0',
 'tqdm>=4.39,<5.0']

entry_points = \
{'console_scripts': ['quantized = quantized.cli:cli']}

setup_kwargs = {
    'name': 'quantized',
    'version': '0.0.1a0',
    'description': 'Quantifying Probabilistic Electron Transit times.',
    'long_description': '# Transit-Chem\n\n[Documentation Home](https://transit-chem.readthedocs.io)\n\n\nLibrary for solving the time dependent schroedinger equation, \nand finding the probablilistic confidence of the time it takes for a quantum\nparticle to move from one place to another. Based on \n[this paper](https://www.worldscientific.com/doi/10.1142/S0219633618500463).\n\n## Features\n\n- Harmonic Oscillator Basis Functions\n- Functional API for Solving the Time Independent/Time Dependent Schroedinger Equation\n- Molecular manipulations: translation, rotation, etc\n- Guaranteed 90%+ test coverage\n- CLI for 1d transit time analysis\n- Caching and optimizations for overlap and hamiltonian integrals\n- Fully type hinted\n- Logging and input validation, with helpful error messages\n\n\n## License\n[License](LICENSE.md)\n',
    'author': 'Evan Curtin',
    'author_email': 'fakeemail@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
