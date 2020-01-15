# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['drf_action_permissions']

package_data = \
{'': ['*']}

install_requires = \
['django>=1.11', 'djangorestframework>=3.7,<4.0']

setup_kwargs = {
    'name': 'drf-action-permissions',
    'version': '0.1.1',
    'description': 'Flexible action level permissions for Django REST framework',
    'long_description': 'drf-action-permissions\n===\n\n| Release | CI | Coverage |\n|---------|----|----------|\n|[![pypi](https://img.shields.io/pypi/v/drf-action-permissions.svg)](https://pypi.python.org/pypi/drf-action-permissions)|[![build](https://img.shields.io/travis/com/abogoyavlensky/drf-action-permissions.svg)](https://travis-ci.com/abogoyavlensky/drf-action-permissions)|[![codecov](https://img.shields.io/codecov/c/github/abogoyavlensky/drf-action-permissions.svg)](https://codecov.io/gh/abogoyavlensky/drf-action-permissions)|\n\nFlexible ability to add action permissions on view level\nfor Django REST framework. Permissions can be as complex or simple as you want.\nIt can be a plain string or a function.\n\n## Requirements\n\n- Python (3.6+)\n- Django (1.11.x, 2.0+)\n- Django REST Framework (3.7+)\n\n## Installation\n\n```bash\n$ pip install drf-common-exceptions\n```\n\nYou cound define common permissions class for whole project:\n\n```\nREST_FRAMEWORK = {\n    ...\n    "DEFAULT_PERMISSION_CLASSES": (\n        "drf_action_permissions.DjangoActionPermissions",\n    )\n    ...\n}\n```\n\nOr use it just for particular viewset in combination with others:\n\n```python\nfrom rest_framework.permissions import IsAuthenticated\nfrom rest_framework.viewsets import ModelViewSet\n\nfrom drf_action_permissions import DjangoActionPermissions\n\nclass MyView(viewsets.ModelViewSet):\n    permission_classes = (IsAuthenticated, DjangoActionPermissions)\n    perms_map_action = {\n        \'retrieve\': [\'users.view_user\'],\n    }\n```\n\n## Usage examples\n\nPermission as string template or plain string:\n```python\nclass PostViewSet(ModelViewSet):\n    permission_classes = (IsAuthenticated, DjangoActionPermissions)\n    perms_map_action = {\n        \'likes\': [\'%(app_label)s.view_%(model_name)s_list\',\n                  \'%(app_label)s.view_like_list\'],\n    }\n```\n\nPermission as function with current object access:\n```python\ndef can_view_application(user, _view, obj):\n    """Can view only archived applications."""\n    if obj.is_archived:\n        return user.has_perm(\'applications.view_archived_application\')\n    return user.has_perm(\'applications.view_application\')\n\n\nclass ApplicationView(ModelViewSet):\n    permission_classes = (IsAuthenticated, DjangoActionPermissions)\n    perms_map_action_obj = {\n        \'retrieve\': [can_view_application],\n    }\n```\n\n\n## Development\n\nInstall poetry and requirements:\n\n```bash\n$ curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python\n$ python3 -m venv path/to/venv\n$ source path/to/venv/bin/activate\n$ poetry install\n```\n\nRun main commands:\n\n```bash\n$ make test\n$ make watch\n$ make clean\n$ make lint\n```\n\nPublish to pypi by default patch version:\n```bash\n$ make publish\n```\n\nor any level you want:\n```bash\n$ make publish minor\n```\n',
    'author': 'Andrey Bogoyavlensky',
    'author_email': 'abogoyavlensky@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abogoyavlensky/drf-action-permissions',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
