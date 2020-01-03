# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scrapyu']

package_data = \
{'': ['*']}

install_requires = \
['fake-useragent==0.1.11',
 'html2text==2019.9.26',
 'path-py==12.4.0',
 'pymongo==3.10.0',
 'pytest-cov>=2.8,<3.0',
 'redis==3.3.11',
 'scrapy>=1.8,<2.0',
 'selenium==3.141.0',
 'testfixtures==6.10.3']

setup_kwargs = {
    'name': 'scrapyu',
    'version': '0.1.10',
    'description': 'Scrapy utils',
    'long_description': "# scrapyu\n\n[![Build Status](https://www.travis-ci.org/lin-zone/scrapyu.svg?branch=master)](https://www.travis-ci.org/lin-zone/scrapyu)\n[![codecov](https://codecov.io/gh/lin-zone/scrapyu/branch/master/graph/badge.svg)](https://codecov.io/gh/lin-zone/scrapyu)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/scrapyu?logo=python&logoColor=FBE072)](https://pypi.org/project/scrapyu/)\n[![GitHub](https://img.shields.io/github/license/lin-zone/scrapyu)](https://github.com/lin-zone/scrapyu/blob/master/LICENSE)\n[![GitHub stars](https://img.shields.io/github/stars/lin-zone/scrapyu?logo=github)](https://github.com/lin-zone/scrapyu)\n[![GitHub forks](https://img.shields.io/github/forks/lin-zone/scrapyu?logo=github)](https://github.com/lin-zone/scrapyu)\n\n## UserAgentMiddleware\n\n```python\n# settings.py\nUSERAGENT_TYPE = 'firefox'\nDOWNLOADER_MIDDLEWARES = {\n   'scrapyu.UserAgentMiddleware': 543,\n}\n```\n\n## MarkdownPipeline\n\n```python\n# settings.py\nMARKDOWNS_STORE = 'news'\nITEM_PIPELINES = {\n    'scrapyu.MarkdownPipeline': 300,\n}\n```\n\n```python\n# items.py\nimport scrapy\n\nclass MarkdownItem(scrapy.Item):\n    html = scrapy.Field()\n    filename = scrapy.Field()\n```\n\n## FirefoxCookiesMiddleware\n\n```python\n# settings.py\nGECKODRIVER_PATH = 'geckodriver'\nDOWNLOADER_MIDDLEWARES = {\n   'scrapyu.FirefoxCookiesMiddleware': 543,\n}\n```\n\n## MongoDBPipeline\n\n```python\n# settings.py\nMONGODB_URI = 'mongodb://localhost:27017'\n# or\n# MONGODB_HOST = 'localhost'\n# MONGODB_PORT = 27017\nMONGODB_DATABASE = 'scrapyu'\nMONGODB_COLLECTION = 'items'\nMONGODB_BUFFER_LENGTH = 100\nMONGODB_UNIQUE_KEY = 'title name'       # use only if no buffer\n# or\n# MONGODB_UNIQUE_KEY = ['title', 'name']\n# MONGODB_UNIQUE_KEY = ('title', 'name')\nITEM_PIPELINES = {\n    'scrapyu.MongoDBPipeline': 300,\n}\n```\n\n## RedisDupeFilter\n\n```python\n# settings.py\nDUPEFILTER_CLASS = 'scrapyu.RedisDupeFilter'\nREDIS_DUPE_HOST = 'localhost'\nREDIS_DUPE_PORT = 6379\nREDIS_DUPE_DATABASE = 0\nREDIS_DUPE_PASSWORD = 'password'\nREDIS_DUPE_KEY = 'requests'\nREDIS_DUPE_IGNORE_URL = r'http://scrapytest.org/\\d+'\n```\n",
    'author': 'lin-zone',
    'author_email': 'z_one10@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lin-zone/scrapyu',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
