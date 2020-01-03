# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['class_settings']

package_data = \
{'': ['*']}

install_requires = \
['django', 'python-dotenv>=0.7']

setup_kwargs = {
    'name': 'django-class-settings',
    'version': '0.2.0',
    'description': 'Effortless class-based settings for Django.',
    'long_description': "# django-class-settings\n\n[![pypi][pypi-image]][pypi-url]\n[![django versions][django-version-image]][pypi-url]\n[![python][python-version-image]][pypi-url]\n[![build][travis-image]][travis-url]\n[![coverage][coverage-image]][coverage-url]\n[![license][license-image]][license-url]\n[![code style][code-style-image]][code-style-url]\n\ndjango-class-settings aims to simplify complicated settings layouts by using\nclasses instead of modules. Some of the benefits of using classes include:\n\n- Real inheritance\n- [Foolproof settings layouts][local_settings]\n- Properties\n- Implicit environment variable names\n\n## Example\n\n```bash\n# .env\nexport DJANGO_SECRET_KEY='*2#fz@c0w5fe8f-'\nexport DJANGO_DEBUG=true\n```\n\n```python\n# manage.py\nimport os\nimport sys\n\nimport class_settings\nfrom class_settings import env\n\nfrom django.core.management import execute_from_command_line\n\nif __name__ == '__main__':\n    env.read_env()\n    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')\n    os.environ.setdefault('DJANGO_SETTINGS_CLASS', 'MySettings')\n    class_settings.setup()\n    execute_from_command_line(sys.argv)\n```\n\n```python\n# myproject/settings.py\nfrom class_settings import Settings, env\n\n\nclass MySettings(Settings):\n    SECRET_KEY = env()\n    DEBUG = env.bool(default=False)\n    INSTALLED_APPS = [\n        'django.contrib.admin',\n        'django.contrib.auth',\n        'django.contrib.contenttypes',\n        'django.contrib.sessions',\n        'django.contrib.messages',\n        'django.contrib.staticfiles',\n    ]\n    ROOT_URLCONF = 'myproject.urls'\n    WSGI_APPLICATION = 'myproject.wsgi.application'\n```\n\n## Installation\n\nInstall it from [PyPI][pypi-url] with [pip][pip-url]:\n\n```bash\npip install django-class-settings\n```\n\n### Requirements\n\n- Django 1.11+\n- Python 3.5+\n\n## Resources\n\n- Documentation: https://django-class-settings.readthedocs.io/\n- Releases: https://pypi.org/project/django-class-settings/\n- Changelog: https://github.com/orlnub123/django-class-settings/blob/master/CHANGELOG.md\n- Code: https://github.com/orlnub123/django-class-settings\n- License: [MIT][license-url]\n\n[code-style-image]: https://img.shields.io/badge/code%20style-black-000000.svg\n[code-style-url]: https://github.com/ambv/black\n[coverage-image]: https://img.shields.io/codecov/c/gh/orlnub123/django-class-settings.svg\n[coverage-url]: https://codecov.io/gh/orlnub123/django-class-settings\n[django-version-image]: https://img.shields.io/pypi/djversions/django-class-settings.svg\n[license-image]: https://img.shields.io/pypi/l/django-class-settings.svg\n[license-url]: https://github.com/orlnub123/django-class-settings/blob/master/LICENSE\n[local_settings]: https://www.pydanny.com/using-executable-code-outside-version-control.html\n[pip-url]: https://pip.pypa.io/en/stable/quickstart/\n[pypi-image]: https://img.shields.io/pypi/v/django-class-settings.svg\n[pypi-url]: https://pypi.org/project/django-class-settings/\n[python-version-image]: https://img.shields.io/pypi/pyversions/django-class-settings.svg\n[travis-image]: https://img.shields.io/travis/orlnub123/django-class-settings.svg\n[travis-url]: https://travis-ci.org/orlnub123/django-class-settings\n",
    'author': 'orlnub123',
    'author_email': 'orlnub123@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/orlnub123/django-class-settings',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
