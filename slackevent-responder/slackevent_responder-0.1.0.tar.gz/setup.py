# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['slackevent_responder']

package_data = \
{'': ['*']}

install_requires = \
['starlette>=0.13.0,<0.14.0']

setup_kwargs = {
    'name': 'slackevent-responder',
    'version': '0.1.0',
    'description': 'ASGI adapter for Slack Events API',
    'long_description': '# SlackEvent Responder\n\n[![Test Status](https://github.com/haeena/slackevent-responder/workflows/Test/badge.svg)](https://github.com/haeena/slackevent-responder/actions)\n[![codecov](https://codecov.io/gh/haeena/slackevent-responder/branch/master/graph/badge.svg)](https://codecov.io/gh/haeena/slackevent-responder)\n[![GitHub license](https://img.shields.io/github/license/haeena/slackevent-responder)](https://github.com/haeena/slackevent-responder/blob/master/LICENSE)\n\n## Introduction\n\nThe SlackEvents Responder is an ASGI adapter for [Slack’s Events API](https://api.slack.com/events-api) based on the [Starlette](https://www.starlette.io/) ASGI framework and works well with the [Responder](https://responder.readthedocs.io/en/latest/).\n\nThis library provides event subscription interface,\njust like Flask based [Slack Events API adapter](https://github.com/slackapi/python-slack-events-api),\nit would be easy to switch from it.\n\nOh, one more point, this library can handle both sync and async function for event callback :)\n\n## Installation\n\n```sh\npip install slackevent-responder\n```\n\n## Setup Slack App with Event Subscription\n\n[Follow the official document](https://github.com/slackapi/python-slack-events-api/blob/master/README.rst#--development-workflow) :)\n\n## Examples\n\n### Hello world using responder\n\n```python\nimport responder\nfrom slackevent_responder import SlackEventApp\n\nslack_events_app = SlackEventApp(\n    path="/events", slack_signing_secret=SLACK_SIGNING_SECRET\n)\n\n@slack_events_app.on("reaction_added")\ndef reaction_added(event_data):\n    event = event_data["event"]\n    emoji = event["reaction"]\n    print(emoji)\n\napi = responder.API()\napi.mount(\'/slack\', slack_events_app)\n\napi.run(port=3000)\n```\n\nMore examples can be found [here](./example/).\n\n## Change Logs\n\n### v0.1.0 (2020-01-17)\n\n- Initial Release 🎉\n',
    'author': 'Toshiaki Hatano',
    'author_email': 'haeena@haeena.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/haeena/slackevent-responder',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
