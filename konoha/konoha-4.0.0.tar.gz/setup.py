# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['konoha', 'konoha.word_tokenizers']

package_data = \
{'': ['*']}

extras_require = \
{'all': ['janome>=0.3.10,<0.4.0',
         'natto-py>=0.9.0,<0.10.0',
         'kytea>=0.1.4,<0.2.0',
         'sentencepiece>=0.1.85,<0.2.0',
         'sudachipy>=0.4.2,<0.5.0',
         'boto3>=1.11.0,<2.0.0'],
 'janome': ['janome>=0.3.10,<0.4.0'],
 'kytea': ['kytea>=0.1.4,<0.2.0'],
 'mecab': ['natto-py>=0.9.0,<0.10.0'],
 'remote': ['boto3>=1.11.0,<2.0.0'],
 'sentencepiece': ['sentencepiece>=0.1.85,<0.2.0'],
 'sudachi': ['sudachipy>=0.4.2,<0.5.0']}

setup_kwargs = {
    'name': 'konoha',
    'version': '4.0.0',
    'description': 'A tiny sentence/word tokenizer for Japanese text written in Python',
    'long_description': None,
    'author': 'himkt',
    'author_email': 'himkt@cookpad.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
