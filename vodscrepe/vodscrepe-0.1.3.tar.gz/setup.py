# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vodscrepe']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.8.2,<5.0.0', 'lxml>=4.4.2,<5.0.0', 'tqdm>=4.41.1,<5.0.0']

setup_kwargs = {
    'name': 'vodscrepe',
    'version': '0.1.3',
    'description': 'https://vods.co/ vod scraper',
    'long_description': '# `vodscrepe`\n\n[![](https://img.shields.io/pypi/v/vodscrepe.svg?style=flat)](https://pypi.org/pypi/vodscrepe/)\n[![](https://img.shields.io/pypi/dw/vodscrepe.svg?style=flat)](https://pypi.org/pypi/vodscrepe/)\n[![](https://img.shields.io/pypi/pyversions/vodscrepe.svg?style=flat)](https://pypi.org/pypi/vodscrepe/)\n[![](https://img.shields.io/pypi/format/vodscrepe.svg?style=flat)](https://pypi.org/pypi/vodscrepe/)\n[![](https://img.shields.io/pypi/l/vodscrepe.svg?style=flat)](https://github.com/dawsonbooth/vodscrepe/blob/master/LICENSE)\n\n# Description\n\nThis PyPI package is best described as a tool for scraping the [vods.co](https://vods.co/) website. Currently, the package only supports Super Smash Bros. Melee vods.\n\n# Installation\n\nWith [Python](https://www.python.org/downloads/) installed, simply run the following command to add the package to your project.\n\n```bash\npip install vodscrepe\n```\n\n# Usage\n\nThe following is an example usage of the package, which is also included in the repo as `example.py`:\n\n```python\nfrom vodscrepe import Scraper\nfrom tqdm import tqdm\n\ns = Scraper(\'melee\', debug=True)\n\npages = range(300)\ntry:\n    for vod in s.scrape(pages, show_progress=True):\n        if vod is not None:\n            tqdm.write(str(vod))\nexcept KeyboardInterrupt:\n    tqdm.write("Scraping terminated.")\n\n```\n\nThis example lists information about the vods from the most recent to page 300 in the following fashion:\n\n```bash\npython example.py > sets.txt\n```\n\nThen, the `sets.txt` file becomes populated with vod information...\n\n```txt\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - Mew2King (Sheik, Fox) vs Captain Faceroll (Sheik) - Grand Finals - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - n0ne (Captain Falcon) vs Captain Faceroll (Sheik) - Losers Finals - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - Spark (CA) (Sheik) vs Captain Faceroll (Sheik) - Losers Semis - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - n0ne (Captain Falcon) vs Mew2King (Sheik) - Winners Finals - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - Spark (CA) (Sheik) vs S2J (Captain Falcon) - Losers Quarters - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - Captain Faceroll (Sheik) vs Kalvar (Marth) - Losers Quarters - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - n0ne (Captain Falcon) vs S2J (Captain Falcon) - Winners Semis - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - Captain Faceroll (Sheik) vs Mew2King (Sheik) - Winners Semis - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - Spark (CA) (Sheik) vs TheSWOOPER (Samus) - Losers Top 8 - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - Voo (Falco) vs Kalvar (Marth) - Losers Top 8 - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - HiFi (Jigglypuff) vs TheSWOOPER (Samus) - Losers Round 3 - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - Colbol (Fox) vs Kalvar (Marth) - Losers Round 3 - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - Spark (CA) (Sheik) vs Captain Faceroll (Sheik) - Winners Quarters - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - S2J (Captain Falcon) vs Colbol (Fox) - Winners Quarters - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - n0ne (Captain Falcon) vs A Rookie (Mario) - Winners Quarters - Bo5"\n"[\'2019-11-17\'] DreamHack Atlanta 2019 - Mew2King (Fox) vs HiFi (Jigglypuff) - Winners Quarters - Bo5"\n"[\'2019-11-09\'] Genesis: BLACK - Lucky (Fox) vs S2J (Captain Falcon) - Grand Finals - Bo5"\n"[\'2019-11-09\'] Genesis: BLACK - Lucky (Fox) vs Captain Faceroll (Sheik) - Losers Finals - Bo5"\n"[\'2019-11-09\'] Genesis: BLACK - Lucky (Fox) vs KoDoRiN (Marth) - Losers Semis - Bo5"\n"[\'2019-11-09\'] Genesis: BLACK - S2J (Captain Falcon) vs Captain Faceroll (Sheik) - Winners Finals - Bo5"\n"[\'2019-11-09\'] Genesis: BLACK - Lucky (Fox) vs Panda (FL) (Fox) - Losers Quarters - Bo5"\n"[\'2019-11-09\'] Genesis: BLACK - Blassy (Fox) vs KoDoRiN (Marth) - Losers Quarters - Bo5"\n"[\'2019-11-09\'] Genesis: BLACK - Lucky (Fox) vs Captain Faceroll (Sheik) - Winners Semis - Bo5"\n"[\'2019-11-09\'] Genesis: BLACK - S2J (Captain Falcon) vs Blassy (Fox) - Winners Semis - Bo5"\nScraping terminated.\n```\n\n...while the terminal details the progress:\n\n```bash\nAll vods:   0%|                                                             | 0/300 [00:14<?, ?pages/s]\nPage 0:  40%|\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88                                  | 24/60 [00:14<00:22,  1.62vods/s]\n```\n\n# License\n\nThis software is released under the terms of [MIT license](LICENSE).\n',
    'author': 'Dawson Booth',
    'author_email': 'pypi@dawsonbooth.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dawsonbooth/vodscrepe',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
