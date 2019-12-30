# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quantworks',
 'quantworks.barfeed',
 'quantworks.broker',
 'quantworks.dataseries',
 'quantworks.examples',
 'quantworks.feed',
 'quantworks.optimizer',
 'quantworks.stratanalyzer',
 'quantworks.strategy',
 'quantworks.talibext',
 'quantworks.technical',
 'quantworks.tools',
 'quantworks.utils',
 'quantworks.websocket']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib==3.1.2',
 'numpy==1.18.0',
 'python-dateutil==2.8.1',
 'pytz==2019.3',
 'requests==2.22.0',
 'retrying==1.3.3',
 'scipy==1.4.1',
 'six==1.13.0',
 'tornado==6.0.3',
 'ws4py==0.3.4']

extras_require = \
{'TALib': ['TA-Lib>=0.4.17,<0.5.0']}

setup_kwargs = {
    'name': 'quantworks',
    'version': '0.21',
    'description': 'Python Algorithmic Trading Framework',
    'long_description': 'QuantWorks\n===========\n\n![PyPI](https://img.shields.io/pypi/v/quantworks)\n![Travis (.com)](https://img.shields.io/travis/com/ttymck/quantworks)\n[![Documentation Status](https://readthedocs.org/projects/quantworks/badge/?version=latest)](https://quantworks.readthedocs.io/en/latest/?badge=latest)\n![PyPI - License](https://img.shields.io/pypi/l/quantworks)\n\n<!-- [![Build Status](https://travis-ci.org/gbeced/pyalgotrade.png?branch=master)](https://travis-ci.org/gbeced/pyalgotrade)\n[![Coverage Status](https://coveralls.io/repos/gbeced/pyalgotrade/badge.svg?branch=master)](https://coveralls.io/r/gbeced/pyalgotrade?branch=master) -->\n\n\nQuantWorks is an **event driven algorithmic trading** framework. It is a fork of [PyAlgoTrade](https://gbeced.github.io/pyalgotrade/) (see [Motivation](#motivation)). \n\nQuantWorks provides a Python API for **strategy** authoring, **backtesting**, **paper trading**, and of course **live trading** via the `Broker` interface.\n\nTo get started using QuantWorks, please take a look at the original `PyAlgoTrade` [tutorial](http://gbeced.github.io/pyalgotrade/docs/v0.20/html/tutorial.html) and the [full documentation](http://gbeced.github.io/pyalgotrade/docs/v0.20/html/index.html).\n\n\nMain Features\n-------------\n\n * Python 3 development\n   * Python 2 support is **NOT** guaranteed in any capacity.\n * Event driven.\n * Supports Market, Limit, Stop and StopLimit orders.\n * Supports any type of time-series data in Pandas or CSV format (like Yahoo! Finance, Google Finance, Quandl and NinjaTrader), as well as database (i.e. sqlite).\n * Technical indicators and filters like SMA, WMA, EMA, RSI, Bollinger Bands, Hurst exponent and others.\n * Performance metrics like Sharpe ratio and drawdown analysis.\n * Event profiler.\n * TA-Lib integration.\n\n\nMotivation\n----------\n\nQuantWorks is a fork of `PyAlgoTrade` by [@gbeced](https://github.com/gbeced). This project aims to be:\n\n * **Modern**: first-class **Python 3** development ([Python 2 is EOL as of 2020](https://pythonclock.org/))\n * **Extensible**: as a framework, robust extension support is a must, and we encourage users of QuantWorks to give back by publishing their extensions (see [Extensions](#extensions))\n * **Easy to Develop**: state-of-the-art tooling (pytest, poetry, travis) and approachable design principles should make it easy for newcomers to contribute.\n * **Open**: as a fork of an Apache 2.0 license project, QuantWorks maintains the spirit of FOSS development. **CONTRIBUTING.md forthcoming**\n\n\nDevelopment\n------------\n\nQuantWorks is developed and tested using 3.7 and depends on:\n\n * [NumPy and SciPy](http://numpy.scipy.org/).\n * [pytz](http://pytz.sourceforge.net/).\n * [dateutil](https://dateutil.readthedocs.org/en/latest/).\n * [requests](http://docs.python-requests.org/en/latest/).\n * [matplotlib](http://matplotlib.sourceforge.net/) for plotting support.\n * [ws4py](https://github.com/Lawouach/WebSocket-for-Python) for Bitstamp support.\n * [tornado](http://www.tornadoweb.org/en/stable/) for Bitstamp support.\n * [tweepy](https://github.com/tweepy/tweepy) for Twitter support.\n\nDeveloper ergonomics are provided by \n \n * poetry\n * pytest\n * tox\n * travis-ci\n\n\nExtensions \n----------\n\n- [Bitstamp](https://www.bitstamp.net/) (bitcoin) live trading is implemented by the `quantworks-bitstamp` package (https://pypi.org/project/quantworks-bitcoin/)\n- Twitter real-time feeds are supported via the `quantworks-twitter` package (https://pypi.org/project/quantworks-twitter/)',
    'author': 'Tyler M Kontra',
    'author_email': 'tyler@tylerkontra.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
