# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['doitlater']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'doitlater',
    'version': '0.1.2',
    'description': 'When you have to do something... later.',
    'long_description': '\n# DoItLater\n\nA simple python library to schedule work in the future with ability to loop infinitely. Does not depend on any 3rd party libraries.\n\n* [Installation](#installation)\n* [Usage](#usage)\n* [API](#api)\n___\n## Installation\nThe package can be simply installed using on of these methods:\n* `pip`: `pip install doitlater`\n* `poetry`: `poetry add doitlater`\n* `poetry`: `poetry add git+https://github.com/evalkaz/doitlater.git`\n---\n## Usage\nSimplest example:\n```python\nfrom datetime import datetime, timedelta\nfrom doitlater import Later\n\nlater = Later()\n\n@later.on(datetime(2021, 1, 1))\ndef say_hello():\n    print("Happy new years in 2021!")\n\nif __name__ == "__main__":\n    later.do()\n```\n\nTo call the same function every 10 seconds with 30 seconds cold start:\n```python\n@later.on(\n    datetime.now() + timedelta(seconds=30),\n    timedelta(seconds=10),\n    loop=True\n)\ndef repeatable_work():\n    print("Hello every 10 seconds!")\n```\nThe `later.on()` is stackable so this will work too (will be executed every 5 and every 7 days):\n```python\n@later.on(datetime(2021, 1, 1), timedelta(days=5))\n@later.on(datetime(2021, 1, 1), timedelta(weeks=1))\ndef say_hello():\n    print("Happy new years in 2021!")\n```\nYou can also pass a list of `datetime` or `timedelta` (or a mixed one) when to execute the function:\n```python\n@later.on(datetime(2021, 1, 1), [\n    datetime(2021, 2, 1),\n    datetime(2021, 3, 1),\n    timedelta(days=31)], loop=False)\ndef say_hello():\n    print("Happy new years in 2021!")\n```\nIf you want to stop executing the same function just return `False`:\n```python\n@later.on(datetime(2021, 1, 1), timedelta(seconds=5), loop=True)\ndef only_one_hello():\n    print("This will appear only once!")\n    return False\n```\nIf you have multiple functions and one of them throws an exception but you don\'t want to stop the work, pass `ignore_errors=True` to `Later()` object:\n```python\nlater = Later(ignore_errors=True)\n```\nBy default, library will output logs on errors. To change logging, use [`dictConfig`](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig):\n```python\nfrom datetime import datetime, timedelta\nfrom doitlater import Later\nfrom logging.config import dictConfig\n\ndictConfig(\n    {\n        "version": 1,\n        "formatters": {\n            "default": {\n                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",\n            }\n        },\n        "handlers": {\n            "default": {"class": "logging.StreamHandler", "formatter": "default",}\n        },\n        "root": {"level": "INFO", "handlers": ["default"]},\n    }\n)\n\nlater = Later()\n\n@later.on(datetime(2021, 1, 1))\ndef say_hello():\n    print("Happy new years in 2021!")\n\nif __name__ == "__main__":\n    later.do()\n```\n---\n## API\n`Later(workers, ignore_errors)` takes these parameters:\n* `workers` - number of threads to use, defaults to maximum number of threads supported by CPU.\n* `ignore_errors` - `False` will exit when one of the function throws an error, `True` - ignores exceptions and will resume the work.\n\n`later.on(exactly, repeat, loop)` function takes these parameters:\n* `exactly` - on which time perform the first function call.\n* `repeat` - a single value or a list of `datetime`, `timedelta` or both on when to repeat the call. If `None` is passed the function will not be called again. Defaults to `None`.\n* `loop` - whether repeat calling times from `repeat`. Defaults to `True`.\n\n`later.do()` does not take any parameters.\n',
    'author': 'Evaldas Kazlauskis',
    'author_email': 'evaldas@evalkaz.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/evalkaz/doitlater',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
