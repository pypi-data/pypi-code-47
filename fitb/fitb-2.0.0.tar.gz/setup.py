from pathlib import Path
from setuptools import setup, find_packages


setup(
    name='fitb',
    version='2.0.0',
    packages=find_packages('src'),

    author='Austin Bingham',
    author_email='austin.bingham@gmail.com',
    description='Practical configuration system',
    license='MIT',
    keywords='',
    url='https://github.com/abingham/fitb',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
    ],
    platforms='any',
    include_package_data=True,
    package_dir={'': 'src'},
    # package_data={'fitb': . . .},
    install_requires=['stevedore'],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax, for
    # example: $ pip install -e .[dev,test]
    extras_require={
        'dev': ['bumpversion', 'twine'],
        # 'doc': ['sphinx', 'cartouche'],
        'test': ['hypothesis', 'pytest'],
    },
    entry_points={
        # 'console_scripts': [
        #    'fitb = fitb.cli:main',
        # ],
    },
    long_description=Path('README.rst').read_text(),
)
