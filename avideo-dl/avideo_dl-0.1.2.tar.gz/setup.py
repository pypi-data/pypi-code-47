# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['avideo_dl',
 'avideo_dl.extractor',
 'avideo_dl.extractor.modules',
 'avideo_dl.scripts']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['avideo_dl = avideo_dl.scripts.command:main']}

setup_kwargs = {
    'name': 'avideo-dl',
    'version': '0.1.2',
    'description': 'Fast adult video downloader with no dependent third party libraries.',
    'long_description': '# avideo-dl\n[![Downloads](https://pepy.tech/badge/avideo-dl)](https://pepy.tech/project/avideo-dl)\n[![Downloads](https://pepy.tech/badge/avideo-dl/month)](https://pepy.tech/project/avideo-dl/month)\n[![Downloads](https://pepy.tech/badge/avideo-dl/week)](https://pepy.tech/project/avideo-dl/week)\n\nFast adult video downloader with no dependent third party libraries.\n\n![Screen shot](https://user-images.githubusercontent.com/13160198/59921981-609f2f00-946a-11e9-9f57-2a1d3ff57650.png)\n\n## Installation\n```\n$ pip3 install avideo_dl\n```\n\n## Usage\nSpecify URL as argument and download.\n```\n$ avideo_dl <url>\n```\n\n## Supported video sites\n- [x] [XVideos](https://www.xvideos.com)\n- [ ] [Pornhub](https://jp.pornhub.com/)\n- [x] [Tube8](https://www.tube8.com/)\n- [x] [RedTube](https://www.redtube.com/)\n',
    'author': 'ksk001100',
    'author_email': 'hm.pudding0715@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ksk001100/avideo-dl',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
