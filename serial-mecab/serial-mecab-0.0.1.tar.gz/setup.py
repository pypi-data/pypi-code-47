"""Metadata of the package."""
from setuptools import setup, find_packages


setup(
    name='serial-mecab',
    version="0.0.1",
    description=('mecab-python3 Wrapper for serialization'),
    packages=find_packages(),
    install_requires=[
        'mecab-python3',
        'joblib'
    ],
    extras_require={
        'test': [
            'pytest'
        ],
        'dev': [
            'ipython',
            'python-language-server[all]'
        ],
        'doc': [
            'sphinx',
            'sphinx_rtd_theme'
        ]})
