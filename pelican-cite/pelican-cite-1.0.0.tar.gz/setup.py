# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pelican_cite']

package_data = \
{'': ['*'], 'pelican_cite': ['templates/*']}

install_requires = \
['jinja2>=2.10.3,<3.0.0', 'pelican>=4.2,<5.0', 'pybtex>=0.22.2,<0.23.0']

extras_require = \
{'markdown': ['markdown>=3.1.1,<4.0.0']}

setup_kwargs = {
    'name': 'pelican-cite',
    'version': '1.0.0',
    'description': 'Allows the use of BibTeX citations within a Pelican site',
    'long_description': 'pelican-cite\n==============\n\nAllows the use of BibTeX citations within a Pelican site.\n\n\nInstallation\n============\n\nTo install simply run `pip install pelican-cite` and add it to the `PLUGINS` section of `pelicanconf.py`\n\n```python\nPLUGINS = [\n    \'...\',\n    \'pelican.plugins.cite\'\n    \'...\',\n]\n```\n\n\n## How to Use\n\nThis plugin reads a user-specified BibTeX file and generates bibliographic\ninformation within your articles and pages.\n\nIf the file is present and readable, then content will be scanned for references\nto citation keys. These take the format `[@Bai2011]` or `[@@Bai2011]`. These\nwill be replaced by incline citations which provide links to the full\nbibliographic information at the end of the article. The former reference would\nbe replaced by a citation of the form "Bai & Stone (2011)", while the latter\nwould be replaced by "(Bai & Stone, 2011)".\n\nIf a citation key is used which does not exist within the BibTeX file then\na warning will be displayed.\n\n### Configuration\n\n#### `PUBLICATIONS_SRC`\n\nLocation of the BibTeX file.\n\nThe BibTeX file may, optionally, be provided or overridden on a per-article\nbasis by supplying the meta-data `publications_src`.\n\nThe BibTeX file may, optionally, be provided or overridden on a per-article\nbasis by supplying the meta-data `publications_src`.\n\n#### `BIBLIOGRAPHY_HEADER`\n\nHtml code for the headers shown for the bibliography on each article or page.\n\nDefault to\n\n```html\n<hr><h2>Bibliography</h2>\n```\n\n#### `BIBLIOGRAPHY_NAME_STYLE`\n\nDefines how names will be formatted in the output.\nStyles included in `"Pybtex"` are `"plain"` and `"lastfirst"`. Defaults to `None`.\n\n#### `BIBLIOGRAPHY_LABEL_STYLE`\n\nDefines how the labels will be formatted in the output.\n\n~~Styles included in `Pybtex` are `"alpha"` and `"number"`. Defaults to `"alpha"`~~\n\n> At this moment only `"author_year"` is supported!\n\nThere is also a custom style available called `"author_year"`.\nYou can use this by installing it with `pip install pybtex-author-year-label`.\n\n#### `BIBLIOGRAPHY_SORTING_STYLE`\n\nDefines how the bibliography will be sorted.\nStyles included in `Pybtex` are `"author_year_title"` and `"none"`. Defaults to `"author_year_title"`\n\n## Attribution\n`pelican-cite` is based on the\n[pelican-bibtex](https://github.com/vene/pelican-bibtex) plugin written by\n[Vlad Niculae](https://github.com/vene)\nand [pelican-cite](https://github.com/cmacmackin/pelican-cite) written by\n[Chris MacMackin](https://github.com/cmacmackin).\n',
    'author': 'Johan Vergeer',
    'author_email': 'johanvergeer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/johanvergeer/pelican-cite',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
