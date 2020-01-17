# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['wagtail_draftail_snippet']

package_data = \
{'': ['*'],
 'wagtail_draftail_snippet': ['static/wagtail_draftail_snippet/js/*',
                              'templates/*',
                              'templates/wagtail_draftail_snippet/*']}

setup_kwargs = {
    'name': 'wagtail-draftail-snippet',
    'version': '0.2.1',
    'description': 'Associate RichTextBlock text content to a snippet model.',
    'long_description': '# wagtail-draftail-snippet\n\nWagtail has support for adding numerous types of links to `RichTextBlock` content, but there is not a way to tie a link to an arbitrary `snippet` model currently. `wagtail-draftail-snippet` provides a way to add a new button to the Draftail rich text editor, which creates an `a href` element for a specific `snippet` model based on a template that can be provided.\n\n\n## Install\n\n1. Add `wagtail_draftail_snippet` to `INSTALLED_APPS` in Django settings\n1. Add `"snippet"` to the `features` keyword list argument when instantiating a `RichTextBlock`, e.g. `paragraph = RichTextBlock(features=["bold", "italic", "h1", "h2", "h3", "snippet"])`\n1. Create a frontend template to determine how the snippet model will be rendered. Frontend templates are required for a snippet to  be selected and are discovered when they match a path like `{app_name}/{model_name}_snippet.html`. For example, if you have an `Affiliate` snippet model in `affiliates/models.py`, then a file in `affiliates/templates/affiliates/affiliate_snippet.html` would be required.\n\n\n## Example use-case\n\nWagtail is used for a content site that will display articles that have affiliate links embedded inside the content. Affiliate links have a snippet data model to store information with a URL, start, and end dates; the urls need to be rendered in such a way that JavaScript can attach an event listener to their clicks for analytics.\n\nWhen the content gets rendered, it uses the specific affiliate model to get the URL stored in the snippet model. If the affiliate\'s URL ever changes, the snippet can be changed in the Wagtail admin, and the all of the content will use the correct link when rendered.\n\nAn example frontend template in `affiliates/templates/affiliates/affiliate_snippet.html` could be the following.\n```\n<a href="{{ object.url }}" data-vars-action="content-cta" data-vars-label="{{ object.slug }}" rel="sponsored">\n```\n\n\n## Build the library\n\n1. `poetry build`\n\n\n## Contributors\n\n- [Parbhat Puri](https://github.com/Parbhat)\n- [Adam Hill](https://github.com/adamghill/)\n\n\n## License\n\n[BSD](https://github.com/themotleyfool/wagtail-draftail-snippet/blob/master/LICENSE)\n',
    'author': 'Parbhat Puri',
    'author_email': 'me@parbhatpuri.com',
    'url': 'https://github.com/themotleyfool/wagtail-draftail-snippet',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
