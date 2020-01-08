from setuptools import setup
import pathlib

requires = []
VERSION = ""
_ROOT = pathlib.Path(__file__).parent
with open(str(_ROOT / 'pubsub_ncs' / '__init__.py')) as f:
    for line in f:
        print(line)
        if line.startswith('__version__ ='):
            _, _, version = line.partition('=')
            VERSION = version.strip(" \n'\"")
            break
    if VERSION == "":
        raise RuntimeError(
            'unable to read the version from pubsub_ncs/__init__.py')

packages = [
    "pubsub_ncs",
]
setup(
    name='pubsub_ncs',
    version=VERSION,
    description='PubSubサーバー接続モジュール',
    url='https://gitlab.com/python-utils1/tornado-broker.git',
    author='nozomi.nishinohara',
    author_email='nozomi.nishinohara@n-creativesystem.com',
    keywords='',
    packages=packages,
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
