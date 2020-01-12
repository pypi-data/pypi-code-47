# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pelican_xref']

package_data = \
{'': ['*']}

install_requires = \
['pelican>=4.2,<5.0']

extras_require = \
{'markdown': ['markdown>=3.1.1,<4.0.0']}

setup_kwargs = {
    'name': 'pelican-xref',
    'version': '0.1.0',
    'description': 'A Pelican plugin that allows you to cross-reference articles',
    'long_description': '# Pelican Xref: A Plugin for Pelican\n\nA Pelican plugin that allows you to cross-reference articles in an easy way\n\n## Motivation for this plugin\n\nIn Pelican, you can reference other articles in the following way:\n\n```markdown\nTitle: The second article\nDate: 2012-12-01 10:02\n\nSee below intra-site link examples in Markdown format.\n\n[a link relative to the current file]({filename}category/article1.rst)\n[a link relative to the content root]({filename}/category/article1.rst)\n```\n\nThe issue I have with this is that your file structure becomes very rigid.\nWhen you move or rename a file or directory all your references are broken.\n\nThat is why I created this plugin.\n\n## Usage\n\n### Step 1: Add `xref` attribute to your articles\n\nYou have to add an attribute named `xref` to the article attributes, which is only required for articles you want to reference to.\nThe attribute value can contain upper- and lowercase letters, numbers, hyphens (`-`) and underscores (`_`).\n\n```markdown\n---\nTitle: The first article\nxref: ref-1\n---\n\n...\n```\n\nAfter you add the `xref` attribute to an article, you can use it in other articles:\n\n```markdown\n---\nTitle: The second article\n---\n\nThis article references the first article with the following syntax: [xref:ref-1]\n```\n\nThe syntax has two optional attributes: `title` and `blank`.\nYou can use the `title` attribute if you want to use a custom text instead of the title of the referenced article.\nThe `blank` attribute is used in case you want the created link to open a new window.\n\nInput | Generated html\n--- | ---\n<code>[xref:ref-1]</code> | `<a href="/category/the-first-article">The first article</a>`\n<code>[xref:ref-1 title="Title override"]</code> | `<a href="/category/the-first-article">Title override</a>`\n<code>[xref:ref-1 blank=1]</code> | `<a href="/category/the-first-article" target="_blank">The first article</a>`\n<code>[xref:ref-1 title="Title override" blank=1]</code> | `<a href="/category/the-first-article" target="_blank">Title override</a>`\n\n## Installation\n\nThis plugin can be installed via:\n\n    pip install pelican-xref\n\n\n## Contributing\n\nContributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].\n\nTo start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.\n\n[existing issues]: https://github.com/johanvergeer/pelican-xref/issues\n[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html\n',
    'author': 'Johan Vergeer',
    'author_email': 'johanvergeer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/johanvergeer/pelican-xref',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
