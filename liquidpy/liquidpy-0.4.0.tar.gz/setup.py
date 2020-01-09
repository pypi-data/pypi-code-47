# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['liquid']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'liquidpy',
    'version': '0.4.0',
    'description': 'A port of liquid template engine for python',
    'long_description': '# liquidpy\nA port of [liquid][1] template engine for python\n\n[![Pypi][2]][9] [![Github][3]][10] [![PythonVers][4]][9] [![ReadTheDocs building][13]][8] [![Travis building][5]][11] [![Codacy][6]][12] [![Codacy coverage][7]][12]\n\n## Install\n```shell\npip install liquidpy\n```\n\n## Full Documentation\n[ReadTheDocs][8]\n\n## Baisic usage\n```python\nfrom liquid import Liquid\nliq = Liquid(\'{{a}}\')\nret = liq.render(a = 1)\n# ret == \'1\'\n\n# load template from a file\nliq = Liquid(\'/path/to/template\', from_file = True)\n```\nWith environments:\n```python\nliq = Liquid(\'{{a | os.path.basename}}\', os = __import__(\'os\'))\nret = liq.render(a = "path/to/file.txt")\n# ret == \'file.txt\'\n```\n\n[1]: https://shopify.github.io/liquid/\n[2]: https://img.shields.io/pypi/v/liquidpy.svg?style=flat-square\n[3]: https://img.shields.io/github/tag/pwwang/liquidpy.svg?style=flat-square\n[4]: https://img.shields.io/pypi/pyversions/liquidpy.svg?style=flat-square\n[5]: https://img.shields.io/travis/pwwang/liquidpy.svg?style=flat-square\n[6]: https://img.shields.io/codacy/grade/aed04c099cbe42dabda2b42bae557fa4?style=flat-square\n[7]: https://img.shields.io/codacy/coverage/aed04c099cbe42dabda2b42bae557fa4?style=flat-square\n[8]: https://liquidpy.readthedocs.io/en/latest/\n[9]: https://pypi.org/project/liquidpy/\n[10]: https://github.com/pwwang/liquidpy\n[11]: https://travis-ci.org/pwwang/liquidpy\n[12]: https://app.codacy.com/manual/pwwang/liquidpy/dashboard\n[13]: https://img.shields.io/readthedocs/liquidpy?style=flat-square\n',
    'author': 'pwwang',
    'author_email': 'pwwang@pwwang.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pwwang/liquidpy',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
