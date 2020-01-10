# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['djangorestframework_camel_case2']

package_data = \
{'': ['*']}

install_requires = \
['django>=2.2', 'djangorestframework>=3.9']

setup_kwargs = {
    'name': 'djangorestframework-camel-case2',
    'version': '0.3.0',
    'description': 'Camel case JSON support for Django REST framework',
    'long_description': "# Django REST Framework JSON CamelCase\n\n[![Build Status](https://travis-ci.org/jozo/djangorestframework-camel-case2.svg?branch=master)](https://travis-ci.org/jozo/djangorestframework-camel-case2)\n[![PyPI](https://img.shields.io/pypi/v/djangorestframework-camel-case2.svg)](https://pypi.org/project/djangorestframework-camel-case2/)\n\nCamel case JSON support for Django REST framework.\n\nCompatible with: \n* Python: Python 3.5+\n* Django: 2.2, 3.0+\n* Django REST framework: 3.9, 3.10, 3.11\n\n_Note: This is a replacement for\n[djangorestframework-camel-case](https://github.com/vbabiy/djangorestframework-camel-case)\nwhich seems currently unmaintained._\n\n## Installation\n\nAt the command line::\n```bash\n$ pip install djangorestframework-camel-case2\n```\n\nAdd the render and parser to your django settings file.\n\n```python\nREST_FRAMEWORK = {\n\n    'DEFAULT_RENDERER_CLASSES': (\n        'djangorestframework_camel_case2.render.CamelCaseJSONRenderer',\n        # Any other renders\n    ),\n\n    'DEFAULT_PARSER_CLASSES': (\n        'djangorestframework_camel_case2.parser.CamelCaseJSONParser',\n        # Any other parsers\n    ),\n}\n```\n\n## Swapping Renderer\n\nBy default the package uses `rest_framework.renderers.JSONRenderer`. If you want\nto use another renderer (the only possible alternative is\n`rest_framework.renderers.UnicodeJSONRenderer`, only available in DRF < 3.0), you must specify it in your django\nsettings file.\n\n```python\n# ...\nJSON_CAMEL_CASE = {\n    'RENDERER_CLASS': 'rest_framework.renderers.UnicodeJSONRenderer'\n}\n# ...\n```\n\n## Underscoreize Options\n\nAs raised in https://github.com/krasa/StringManipulation/issues/8#issuecomment-121203018\nthere are two conventions of snake case.\n\n```\n# Case 1 (Package default)\nv2Counter -> v_2_counter\nfooBar2 -> foo_bar_2\n\n# Case 2\nv2Counter -> v2_counter\nfooBar2 -> foo_bar2\n```\n\nBy default, the package uses the first case. To use the second case, specify it in your django settings file.\n\n```python\nREST_FRAMEWORK = {\n    # ...\n    'JSON_UNDERSCOREIZE': {\n        'no_underscore_before_number': True,\n    },\n    # ...\n}\n```\n\nAlternatively, you can change this behavior on a class level by setting `json_underscoreize`:\n\n```python\nfrom djangorestframework_camel_case2.parser import CamelCaseJSONParser\nfrom rest_framework.generics import CreateAPIView\n\nclass NoUnderscoreBeforeNumberCamelCaseJSONParser(CamelCaseJSONParser):\n    json_underscoreize = {'no_underscore_before_number': True}\n    \nclass MyView(CreateAPIView):\n    queryset = MyModel.objects.all()\n    serializer_class = MySerializer\n    parser_classes = (NoUnderscoreBeforeNumberCamelCaseJSONParser,)\n```\n\n## Running Tests\n\nTo run the current test suite, execute the following from the root of the project\n\n```bash\npoetry run pytest\n```\n",
    'author': 'jozo',
    'author_email': 'hi@jozo.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jozo/djangorestframework-camel-case2',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
