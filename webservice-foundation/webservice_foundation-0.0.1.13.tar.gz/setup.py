from setuptools import setup
import pathlib

requires = [
    "PyYAML==5.2",
    "tornado==6.0.3"
]
VERSION = "0.0.0"
_ROOT = pathlib.Path(__file__).parent
with open(str(_ROOT / 'webservice_foundation' / '__init__.py')) as f:
    for line in f:
        if line.startswith('__version__ ='):
            _, _, version = line.partition('=')
            VERSION = version.strip(" \n'\"")
            break
        else:
            raise RuntimeError(
                'unable to read the version from webservice_foundation/__init__.py')

packages = [
    "webservice_foundation",
]
setup(
    name='webservice_foundation',
    version=VERSION,
    description='webservice 基盤',
    url='https://gitlab.com/python-utils1/webservice_foundation.git',
    author='nozomi.nishinohara',
    author_email='nozomi.nishinohara@n-creativesystem.com',
    keywords='',
    packages=packages,
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        "console_scripts": [
            "miniweb-runner = webservice_foundation.webservice:main"
        ]
    }
)
