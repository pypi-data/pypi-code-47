# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['template_magic']

package_data = \
{'': ['*']}

install_requires = \
['ipython>=7.11.1,<8.0.0']

setup_kwargs = {
    'name': 'template-ipython-magic',
    'version': '0.1.2',
    'description': 'IPython magics to render cells as templates in a variety of different templating languages.',
    'long_description': "# Template IPython magics 🎩\n\nThis package provides simple IPython magics to render cells as templates in a variety of different templating languages. It currently supports [Mako][] and [Jinja2][].\n\n[Mako]: https://www.makotemplates.org/\n[Jinja2]: https://jinja.palletsprojects.com/\n\nTo use it, first install the package from PyPI, along with at least one of the supported templating languages. E.g. using `pipenv` (everyone should use [`pipenv`][pipenv]):\n\n```shell\npipenv install template-ipython-magic jinja2 mako\n```\n\n[pipenv]: https://pipenv.readthedocs.io/en/latest/\n\nIn your notebook, load the `template_magic` module:\n\n\n```python\n%load_ext template_magic\n```\n\nNote that the available templating languages are detected at the point of loading the extension, and each magic only enabled if the appropriate package is found. If neither Jinja2 or Mako are installed, there will be no magics!\n\nNow you can use `%jinja` as a line magic within any code block, with access to all variables in scope. The result is formatted as Markdown:\n\n\n```python\nimport sys\n\n%jinja Hello from **Jinja** on Python {{sys.version_info.major}}.{{sys.version_info.minor}}! 🐍\n```\n\n\nHello from **Jinja** on Python 3.8! 🐍\n\n\nIf you prefer, `%mako` is also available:\n\n\n```python\nimport datetime\nnow = datetime.datetime.now()\n\n%mako Hello from *Mako* at ${now.strftime('%I:%M %p')}... ⏰\n```\n\n\nHello from *Mako* at 08:39 PM... ⏰\n\n\nCell magics are also available for each language, which lets you render the entire cell as a template for convenient report generation:\n\n\n```python\n%%jinja\n\n{%- for x in ['spam'] * 7 + ['eggs', 'spam'] %}\n- {% if loop.last %}and {% endif %}{{x}}{%if not loop.last %},{% endif %}\n{%- endfor %}\n```\n\n\n\n- spam,\n- spam,\n- spam,\n- spam,\n- spam,\n- spam,\n- spam,\n- eggs,\n- and spam\n\n",
    'author': 'Jez Cope',
    'author_email': 'j.cope@erambler.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/jezcope/template-ipython-magic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
