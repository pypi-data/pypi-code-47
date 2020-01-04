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
    'version': '1.1.0',
    'description': 'Allows the use of BibTeX citations within a Pelican site',
    'long_description': 'pelican-cite\n==============\n\nAllows the use of BibTeX citations within a Pelican site. This plugin is based on the\n[pelican-bibtex](https://github.com/vene/pelican-bibtex) plugin written by\n[Vlad Niculae](https://github.com/vene)\nand [pelican-cite](https://github.com/cmacmackin/pelican-cite) written by\n[Chris MacMackin](https://github.com/cmacmackin) and aims to improve the following points:\n\n- More flexibility using configuration\n    - The user can use any label, soring and naming style\n    - The user can create their own Jinja2 template for bibliography and label (This is still a TODO)\n- Better maintainability\n- Everything is tested with PyTest\n\n\nInstallation\n============\n\nTo install simply run `pip install pelican-cite` and add it to the `PLUGINS` section of `pelicanconf.py`\n\n```python\nPLUGINS = [\n    \'...\',\n    \'pelican_cite\'\n    \'...\',\n]\n```\n\n\n## How to Use\n\nThis plugin reads a user-specified BibTeX file and generates bibliographic\ninformation within your articles and pages.\n\nIf the file is present and readable, then content will be scanned for references\nto citation keys. These take the format `[@Bai2011]`.\nThe format `[@@Bai2011]` is also possible for backwards compatibility with [pelican-cite](https://github.com/cmacmackin/pelican-cite) by\n[Chris MacMackin](https://github.com/cmacmackin).\n\nIf a citation key is used which does not exist within the BibTeX file then\na warning will be displayed.\n\n### Configuration\n\n#### `PUBLICATIONS_SRC`\n\nLocation of the BibTeX file.\n\nThe BibTeX file may, optionally, be appended on a per-article\nbasis by supplying the meta-data `publications_src`.\n\n#### `BIBLIOGRAPHY_NAME_STYLE`\n\nDefines how names will be formatted in the output.\nStyles included in `"Pybtex"` are `"plain"` and `"lastfirst"`. Defaults to `None`.\n\n#### `BIBLIOGRAPHY_LABEL_STYLE`\n\nDefines how the labels will be formatted in the output.\n\nStyles included in `Pybtex` are `"alpha"` and `"number"`. Defaults to `"alpha"`\n\n##### Author_year label style\n\nThere is also a custom style available called `"author_year_1"` and `"author_year_2"`.\nThe first will show labels like `(Author,year)`, the second will show labels like `Author (year)`\n\nYou can use this by installing it with `pip install pybtex-author-year-label`.\n\n#### `BIBLIOGRAPHY_SORTING_STYLE`\n\nDefines how the bibliography will be sorted.\nStyles included in `Pybtex` are `"author_year_title"` and `"none"`. Defaults to `"author_year_title"`\n\n### Usage in Pelican template\n\n#### Labels\n\nLabels are rendered with the `BIBLIOGRAPHY_LABEL_STYLE` setting, and you cannot set anything\nin the template.\n\n#### Bibliography\n\n##### Use out of the box template\n\nYou can add the bibliography anywhere in your template.\n`pelican_cite` comes with a rendered bibliography out of the box. Simply add the following to your template:\n\n```jinja2\n{% if article.bibliograpy %}\n    {{ article.bibliography.rendered }}\n{% endif %}\n```\n\nThis will use the template from `pelican_cite/templates/citations.html` to render a bibliography\n\n##### Create your own template\n\nYou can also create your own template. To do this `article.bibliography` has a `cites` attribute.\n\nAttribute | Description\n---|---\n`article.bibliography.cites.cite_key` | The id you used for the citation in your `.bib` file.\n`article.bibliography.cites.ref_id` | The `cite_key`, without spaces.\n`article.bibliography.cites.rendered_entry` | A rendered string containing the citation.\n`article.bibliography.cites.count` | The number of times the entry was cited in the article.\n\nHere is a template to get you started:\n\n```jinja2\n{% if article.bibliography %}\n<div id="citations">\n    <hr>\n    <h3>Citations</h3>\n    <ol class="references">\n        {% for cite in article.bibliography.cites %}\n            <li id="{{ cite.ref_id }}">\n                <span class="reference-text">{{ cite.rendered_entry }}</span>\n                {% for i in range(1, cite.count + 1) %}\n                    <a class="cite-backref" href="#ref-{{ cite.ref_id }}-{{ i }}"\n                       title="Jump back to reference {{ i }}">\n                        <sup>\n                            <i>\n                                <b>\n                                    {{ i }}\n                                </b>\n                            </i>\n                        </sup>\n                    </a>\n                {% endfor %}\n            </li>\n        {% endfor %}\n    </ol>\n</div>\n{% endif %}\n```\n',
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
