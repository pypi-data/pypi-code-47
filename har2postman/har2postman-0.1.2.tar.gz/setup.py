# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['har2postman']

package_data = \
{'': ['*']}

install_requires = \
['jsonpath>=0.82.0,<0.83.0']

entry_points = \
{'console_scripts': ['harto = har2postman.cli:main']}

setup_kwargs = {
    'name': 'har2postman',
    'version': '0.1.2',
    'description': 'Convert HAR(HTTP Archive) to Postman Collection',
    'long_description': '## Har2Postman\n[![travis-ci](https://api.travis-ci.org/whitexie/Har2Postman.svg?branch=master)](https://travis-ci.org/whitexie/Har2toPostman)\n![coveralls](https://coveralls.io/repos/github/whitexie/Har2Postman/badge.svg?branch=master)\n> 将har文件转换为postman可导入文件\n\n## 安装\n```shell script\npip isntall Har2toPostman\n```\n\n## 使用\n1.将har文件转换为postman可导入文件\n```shell script\nharto postman_echo.har\n\n# INFO:root:read postman_echo.har\n# INFO:root:Generate postman collection successfully: postman_echo.json\n```\n2.在postman中导入postman_echo.json文件\n![](https://github.com/whitexie/Har2Postman/blob/master/postman_collection1.png)\n',
    'author': 'ysansan',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/whitexie/Har2Postman',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
