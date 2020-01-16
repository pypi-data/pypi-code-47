from setuptools import setup

long_description = open('README.md').read()
VERSION = open('VERSION').read().strip()

setup(
    name = 'smugapi',
    version = VERSION,
    description = 'helpful api endpoints for smug',
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/nod/smugapi',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        ],
    entry_points = { 'console_scripts': [ 'smugapi=smugapi.cli.main:cli'] },
    package_dir={'smugapi': 'src/smugapi'},
    packages=['smugapi', 'smugapi.cli', 'smugapi.lib', 'smugapi.handlers'],
    python_requires='>=3.6',
    install_requires=[
        'click',
        'pngcanvas',
        'requests',
        'tornado',
        'webpreview',
        ],
    )

