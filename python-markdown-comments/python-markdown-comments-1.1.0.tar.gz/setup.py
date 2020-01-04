# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_markdown_comments']

package_data = \
{'': ['*']}

install_requires = \
['markdown>=3.1.1,<4.0.0']

setup_kwargs = {
    'name': 'python-markdown-comments',
    'version': '1.1.0',
    'description': 'A Python-Markdown extension to ignore html comments opened by three dashes.',
    'long_description': 'mkdcomments\n===========\n\nOriginal plugin was created by [ryneeverett](https://github.com/ryneeverett/python-markdown-comments).\n\nA [Python-Markdown](https://github.com/waylan/Python-Markdown) preprocessor extension to ignore html comments opened by three dashes and any whitespace prior to them. I believe pandoc has similar functionality.\n\n```html\n<!-- This is a standard html comment which will remain in the output. -->\n<!--- This is a markdown comment which this extension removes. -->\n```\n\nInstallation\n------------\n\n```sh\npip install python-markdown-comments\n```\n\nExample\n-------\n```python\n>>> import markdown\n>>> from python_markdown_comments import CommentsExtension\n>>> comments = CommentsExtension()\n>>> markdowner = markdown.Markdown(extensions=[comments])\n>>> markdowner.convert("""\\\n... blah blah blah  <!--- inline comment -->\n...\n... <!---multiline comment\n... multiline comment\n... multiline comment-->\n...\n... even more text.""")\nu\'<p>blah blah blah</p>\\n<p>even more text.</p>\'\n```\n\nInfrequently Asked Questions\n----------------------------\n\n### How can I write about markdown comments without them being removed?\n\nIn order to render markdown comments, you must *(a)*use them in an html block (which are not processed as markdown) and *(b)*escape the brackets so the browser won\'t think they\'re html comments. E.g.:\n\n```html\n<pre>\n&lt;!--- meta markdown comment --&gt;\n</pre>\n```\n',
    'author': 'Johan Vergeer',
    'author_email': 'johanvergeer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/johanvergeer/python-markdown-comments',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
