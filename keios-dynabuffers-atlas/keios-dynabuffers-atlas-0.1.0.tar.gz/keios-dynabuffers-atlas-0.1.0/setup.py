# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['keios_dynabuffers_atlas',
 'keios_dynabuffers_atlas.classification',
 'keios_dynabuffers_atlas.dependency_parsing',
 'keios_dynabuffers_atlas.embedding',
 'keios_dynabuffers_atlas.lexical_normalization',
 'keios_dynabuffers_atlas.named_entity_recognition',
 'keios_dynabuffers_atlas.part_of_speech_tagging',
 'keios_dynabuffers_atlas.segmentizer',
 'keios_dynabuffers_atlas.sentencizer',
 'keios_dynabuffers_atlas.tokenizer']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'keios-dynabuffers-atlas',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'fridayy',
    'author_email': 'benjamin.krenn@leftshift.one',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
