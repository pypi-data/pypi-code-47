# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['profanity_filter', 'profanity_filter.analysis']

package_data = \
{'': ['*'],
 'profanity_filter': ['data/en_profane_words.txt',
                      'data/en_profane_words.txt',
                      'data/ru_profane_words.txt',
                      'data/ru_profane_words.txt']}

install_requires = \
['cached-property>=1.5,<2.0',
 'more-itertools>=8.0,<9.0',
 'ordered-set-stubs>=0.1.3,<0.2.0',
 'ordered-set>=3.0,<4.0',
 'poetry-version>=0.1.3,<0.2.0',
 'pydantic>=1.3,<2.0',
 'redis>=3.2,<4.0',
 'ruamel.yaml>=0.15.89,<0.16.0',
 'spacy>=2.0,<3.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.6.0,<0.7.0'],
 'deep-analysis': ['hunspell>=0.5.5,<0.6.0',
                   'python-Levenshtein>=0.12.0,<0.13.0',
                   'regex>=2019.12.20,<2020.0.0'],
 'multilingual': ['polyglot>=16.7,<17.0', 'pycld2==0.31', 'PyICU>=2.4,<3.0'],
 'pymorphy2-ru': ['pymorphy2-dicts-ru>=2.4.404381,<3.0.0'],
 'pymorphy2-uk': ['pymorphy2-dicts-uk>=2.4.1,<3.0.0'],
 'web': ['appdirs>=1.4.3,<2.0.0',
         'fastapi>=0.45.0,<0.46.0',
         'uvicorn>=0.11.1,<0.12.0']}

setup_kwargs = {
    'name': 'profanity-filter',
    'version': '1.3.1',
    'description': 'A Python library for detecting and filtering profanity',
    'long_description': '# profanity-filter: A Python library for detecting and filtering profanity\n[![License](https://img.shields.io/pypi/l/profanity-filter.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/profanity-filter.svg)\n[![PyPI](https://img.shields.io/pypi/v/profanity-filter.svg)](https://pypi.org/project/profanity-filter/)\n\n## Table of contents\n<!--ts-->\n   * [profanity-filter: A Python library for detecting and filtering profanity](#profanity-filter-a-python-library-for-detecting-and-filtering-profanity)\n      * [Table of contents](#table-of-contents)\n      * [Overview](#overview)\n         * [Features](#features)\n         * [Caveats](#caveats)\n      * [Usage](#usage)\n         * [Basics](#basics)\n         * [Deep analysis](#deep-analysis)\n         * [Multilingual analysis](#multilingual-analysis)\n         * [Using as a part of Spacy pipeline](#using-as-a-part-of-spacy-pipeline)\n         * [Customizations](#customizations)\n         * [Console Executable](#console-executable)\n         * [RESTful web service](#restful-web-service)\n      * [Installation](#installation)\n         * [Basic installation](#basic-installation)\n         * [Deep analysis](#deep-analysis-1)\n         * [Other language support](#other-language-support)\n            * [Russian language support](#russian-language-support)\n               * [Pymorphy2](#pymorphy2)\n         * [Multilingual support](#multilingual-support)\n         * [RESTful web service](#restful-web-service-1)\n      * [Troubleshooting](#troubleshooting)\n      * [Credits](#credits)\n\n<!-- Added by: rominf, at: Сб мая 18 15:06:37 MSK 2019 -->\n\n<!--te-->\n\n## Overview\n`profanity-filter` is a universal library for detecting and filtering profanity. Support for English and Russian is \nincluded.\n\n### Features\n1. Full text or individual words censoring.\n2. Multilingual support, including profanity filtering in texts written in mixed languages.\n3. Deep analysis. The library detects not only the exact profane word matches but also derivative and distorted profane\nwords using the Levenshtein automata, ignoring dictionary words, containing profane words as a part.\n4. Spacy component for using the library as a part of the pipeline.\n5. Explanation of decisions (attribute `original_profane_word`).\n6. Partial word censoring.\n7. Extensibility support. New languages can be added by supplying dictionaries.\n8. RESTful web service.\n\n### Caveats\n1. Context-free. The library cannot detect using profane phrases consisted of decent words. Vice versa, the library\ncannot detect appropriate usage of a profane word.\n\n## Usage\nHere are the basic examples of how to use the library. For more examples please see `tests` folder.\n\n### Basics\n```python\nfrom profanity_filter import ProfanityFilter\n\npf = ProfanityFilter()\n\npf.censor("That\'s bullshit!")\n# "That\'s ********!"\n\npf.censor_word(\'fuck\')\n# Word(uncensored=\'fuck\', censored=\'****\', original_profane_word=\'fuck\')\n```\n\n### Deep analysis\n```python\nfrom profanity_filter import ProfanityFilter\n\npf = ProfanityFilter()\n\npf.censor("fuckfuck")\n# "********"\n\npf.censor_word(\'oofuko\')\n# Word(uncensored=\'oofuko\', censored=\'******\', original_profane_word=\'fuck\')\n\npf.censor_whole_words = False\npf.censor_word(\'h0r1h0r1\')\n# Word(uncensored=\'h0r1h0r1\', censored=\'***1***1\', original_profane_word=\'h0r\')\n```\n\n### Multilingual analysis\n```python\nfrom profanity_filter import ProfanityFilter\n\npf = ProfanityFilter(languages=[\'ru\', \'en\'])\n\npf.censor("Да бля, это просто shit какой-то!")\n# "Да ***, это просто **** какой-то!"\n```\n\n### Using as a part of Spacy pipeline\n```python\nimport spacy\nfrom profanity_filter import ProfanityFilter\n\nnlp = spacy.load(\'en\')\nprofanity_filter = ProfanityFilter(nlps={\'en\': nlp})  # reuse spacy Language (optional)\nnlp.add_pipe(profanity_filter.spacy_component, last=True)\n\ndoc = nlp(\'This is shiiit!\')\n\ndoc._.is_profane\n# True\n\ndoc[:2]._.is_profane\n# False\n\nfor token in doc:\n    print(f\'{token}: \'\n          f\'censored={token._.censored}, \'\n          f\'is_profane={token._.is_profane}, \'\n          f\'original_profane_word={token._.original_profane_word}\'\n    )\n# This: censored=This, is_profane=False, original_profane_word=None\n# is: censored=is, is_profane=False, original_profane_word=None\n# shiiit: censored=******, is_profane=True, original_profane_word=shit\n# !: censored=!, is_profane=False, original_profane_word=None\n```\n\n### Customizations\n```python\nfrom profanity_filter import ProfanityFilter\n\npf = ProfanityFilter()\n\npf.censor_char = \'@\'\npf.censor("That\'s bullshit!")\n# "That\'s @@@@@@@@!"\n\npf.censor_char = \'*\'\npf.custom_profane_word_dictionaries = {\'en\': {\'love\', \'dog\'}}\npf.censor("I love dogs and penguins!")\n# "I **** **** and penguins"\n\npf.restore_profane_word_dictionaries()\npf.is_clean("That\'s awesome!")\n# True\n\npf.is_clean("That\'s bullshit!")\n# False\n\npf.is_profane("That\'s bullshit!")\n# True\n\npf.extra_profane_word_dictionaries = {\'en\': {\'chocolate\', \'orange\'}}\npf.censor("Fuck orange chocolates")\n# "**** ****** **********"\n```\n\n### Console Executable\n```bash\n$ profanity_filter -h\nusage: profanity_filter [-h] [-t TEXT | -f PATH] [-l LANGUAGES] [-o OUTPUT_FILE] [--show]\n\nProfanity filter console utility\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -t TEXT, --text TEXT  Test the given text for profanity\n  -f PATH, --file PATH  Test the given file for profanity\n  -l LANGUAGES, --languages LANGUAGES\n                        Test for profanity using specified languages (comma\n                        separated)\n  -o OUTPUT_FILE, --output OUTPUT_FILE\n                        Write the censored output to a file\n  --show                Print the censored text\n```\n\n### RESTful web service\nRun:\n```shell\n$ uvicorn profanity_filter.web:app --reload\nINFO: Uvicorn running on http://127.0.0.1:8000\n...\n```\n\nGo to the `{BASE_URL}/docs` for interactive documentation.\n\n## Installation\nFirst two parts of installation instructions are designed for the users who want to filter English profanity.\nIf you want to filter profanity in another language you still need to read it.\n\n### Basic installation\nFor minimal setup you need to install `profanity-filter` with is bundled with `spacy` and download `spacy`\nmodel for tokenization and lemmatization:\n```shell\n$ pip install profanity-filter\n$ # Skip next line if you want to filter profanity in another language\n$ python -m spacy download en\n```\n\nFor more info about Spacy models read: https://spacy.io/usage/models/.\n\n### Deep analysis\nTo get deep analysis functionality install additional libraries and dictionary for your language.\n\nFirstly, install `hunspell` and `hunspell-devel` packages with your system package manager.\n\nFor Amazon Linux AMI run:\n```shell\n$ sudo yum install hunspell\n```\n\nFor openSUSE run:\n```shell\n$ sudo zypper install hunspell hunspell-devel\n```\n\nThen run:\n```shell\n$ pip install -U profanity-filter[deep-analysis] git+https://github.com/rominf/hunspell_serializable@49c00fabf94cacf9e6a23a0cd666aac10cb1d491#egg=hunspell_serializable git+https://github.com/rominf/pyffs@6c805fbfd7771727138b169b32484b53c0b0fad1#egg=pyffs\n$ # Skip next lines if you want deep analysis support for another language (will be covered in next section)\n$ cd profanity_filter/data\n$ wget https://cgit.freedesktop.org/libreoffice/dictionaries/plain/en/en_US.aff\n$ wget https://cgit.freedesktop.org/libreoffice/dictionaries/plain/en/en_US.dic\n$ mv en_US.aff en.aff\n$ mv en_US.dic en.dic\n```\n\n### Other language support\nLet\'s take Russian for example on how to add new language support.\n\n#### Russian language support\nFirstly, we need to provide file `profanity_filter/data/ru_badwords.txt` which contains a newline separated list of\nprofane words. For Russian it\'s already present, so we skip file generation.\n\nNext, we need to download the appropriate Spacy model. Unfortunately, Spacy model for Russian is not yet ready, so we \nwill use an English model for tokenization. If you had not install Spacy model for English, it\'s the right time to do \nso. As a consequence, even if you want to filter just Russian profanity, you need to specify English in \n`ProfanityFilter` constructor as shown in usage examples.\n\nNext, we download dictionaries in Hunspell format for deep analysis from the site \nhttps://cgit.freedesktop.org/libreoffice/dictionaries/plain/:\n```shell\n> cd profanity_filter/data\n> wget https://cgit.freedesktop.org/libreoffice/dictionaries/plain/ru_RU/ru_RU.aff\n> wget https://cgit.freedesktop.org/libreoffice/dictionaries/plain/ru_RU/ru_RU.dic\n> mv ru_RU.aff ru.aff\n> mv ru_RU.dic ru.dic\n```\n\n##### Pymorphy2\nFor Russian and Ukrainian languages to achieve better results we suggest you to install `pymorphy2`.\nTo install `pymorphy2` with Russian dictionary run:\n```shell\n$ pip install -U profanity-filter[pymorphy2-ru] git+https://github.com/kmike/pymorphy2@ca1c13f6998ae2d835bdd5033c17197dcba84cf4#egg=pymorphy2\n```\n\n### Multilingual support\nYou need to install `polyglot` package and it\'s requirements for language detection.\nSee https://polyglot.readthedocs.io/en/latest/Installation.html for more detailed instructions.\n\nFor Amazon Linux AMI run:\n```shell\n$ sudo yum install libicu-devel\n```\n\nFor openSUSE run:\n```shell\n$ sudo zypper install libicu-devel\n```\n\nThen run:\n```shell\n$ pip install -U profanity-filter[multilingual]\n```\n\n### RESTful web service\nRun:\n```shell\n$ pip install -U profanity-filter[web]\n```\n\n## Troubleshooting\nYou can always check will deep, morphological, and multilingual analyses work by inspecting the value of module\nvariable `AVAILABLE_ANALYSES`. If you\'ve followed all steps and installed support for all analyses you will see the\nfollowing:\n```python\nfrom profanity_filter import AVAILABLE_ANALYSES\n\nprint(\', \'.join(sorted(analysis.value for analysis in AVAILABLE_ANALYSES)))\n# deep, morphological, multilingual\n```\n\nIf something is not right, you can import dependencies yourself to see the import exceptions:\n```python\nfrom profanity_filter.analysis.deep import *\nfrom profanity_filter.analysis.morphological import *\nfrom profanity_filter.analysis.multilingual import *\n```\n\n## Credits\nEnglish profane word dictionary: https://github.com/areebbeigh/profanityfilter/ (author Areeb Beigh).\n\nRussian profane word dictionary: https://github.com/PixxxeL/djantimat (author Ivan Sergeev).\n',
    'author': 'Roman Inflianskas',
    'author_email': 'infroma@gmail.com',
    'maintainer': 'Roman Inflianskas',
    'maintainer_email': 'infroma@gmail.com',
    'url': 'https://github.com/rominf/profanity-filter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
