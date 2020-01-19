# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bbfcapi']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp[speedups]>=3.6,<4.0',
 'beautifulsoup4>=4.8,<5.0',
 'fastapi>=0.44.1,<0.45.0',
 'uvicorn>=0.10.8,<0.11.0']

setup_kwargs = {
    'name': 'bbfcapi',
    'version': '1.0.1',
    'description': 'API service, library and parser for BBFC',
    'long_description': '# BBFC API\n\nWeb API and Python library for [BBFC](https://bbfc.co.uk/).\n\n## High-Level REST Web API\n\nTo use the REST API to query BBFC, first run the web server:\n\n```console\n$ uvicorn bbfcapi.apiweb:app\n```\n\nThen, to query the API using `curl`:\n\n```console\n$ curl "127.0.0.1:8000?title=interstellar&year=2014"\n{"title":"INTERSTELLAR","year":2014,"age_rating":"12"}\n```\n\nOr, to query the API from another web page:\n\n```js\nasync function call()\n{\n    const response = await fetch(\'http://127.0.0.1:8000/?title=interstellar&year=2014\');\n    const responseJson = await response.json();\n    console.log(JSON.stringify(responseJson));\n}\ncall();\n```\n\nAdditional notes:\n\n* HTTP 404 Not Found is returned when there is no film found.\n* Browse documentation @ <http://127.0.0.1:8000/redoc>.\n* Or, browse documentation @ <http://127.0.0.1:8000/docs>.\n\n## High-Level Python Library\n\nTo use the library to get results from BBFC *asynchronously*:\n\n```py\nfrom bbfcapi.apilib import top_search_result\nprint(await top_search_result(title="interstellar", year=2014))\n```\n\nTo use the library to get results from BBFC *synchronously*:\n\n```py\nimport asyncio\nfrom bbfcapi.apilib import top_search_result\nprint(asyncio.run(top_search_result(title="interstellar", year=2014)))\n```\n\n## Low-Level Python Library\n\nTo use the library to get raw HTML pages from BBFC *asynchronously*:\n\n```py\nfrom bbfcapi import client\nprint(await client.search(title="interstellar", year=2014))\n```\n\nTo use the library to get raw HTML pages from BBFC *synchronously*:\n\n```py\nimport asyncio\nfrom bbfcapi import client\nprint(asyncio.run(client.search(title="interstellar", year=2014)))\n```\n\nTo use the library to parse raw HTML pages from BBFC:\n\n```py\nfrom bbfcapi import parser\nprint(parser.parse_top_search_result(b"<BBFC search page byte-string>"))\n```\n\n## Development\n\n1. `poetry install` to set up the virtualenv (one-off)\n2. `poetry run uvicorn bbfcapi.apiweb:app --reload` to run the web server\n3. `make fix`, `make check`, and `make test` before committing\n\nThere is also `make test-live` which will run live integration tests against\nthe BBFC website.\n\n### Contributing\n\nPull requests are welcome :)\n\n### Publishing\n\nThis application is published on PyPi.\n\n1. Ensure you have configured the PyPi repository with Poetry (one-off)\n2. Run `make release` to execute the check-list\n\nTo publish to the test repository:\n\n1. Ensure you have configured the Test PyPi repository with Poetry (one-off)\n2. `poetry publish --build -r testpypi` to upload to the test repository\n\n## Changelog\n\n### Unreleased\n\n...\n\n### v1.0.1 - 2020-01-19\n\n- Fix parsing 12A age ratings\n\n### v1.0.0 - 2020-01-19\n\n- First release of bbfcapi\n',
    'author': 'QasimK',
    'author_email': 'noreply@QasimK.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Fustra/bbfcapi/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
