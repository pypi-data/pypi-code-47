# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['textcaptcha']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.22.0,<3.0.0']

setup_kwargs = {
    'name': 'textcaptcha',
    'version': '0.1.0',
    'description': 'A library for using text-based CAPTCHAs from http://textcaptcha.com/.',
    'long_description': '# TextCaptcha\n\n> A Python library for using text-based CAPTCHAs from <http://textcaptcha.com/>.\n\nThis is a simple wrapper around the [TextCaptcha](http://textcaptcha.com/) API which is a service which provides text-based CAPTCHA questions which helps to prevent spam from robots.\n\nThis is designed to be implemented into a server-side application such as a Discord Bot, IRC, SMS, etc...\n\n**Note:** *The TextCaptcha API is only suitable for low traffic websites. For more than 5 requests per second, your usage will be rate limited.*\n\n## Installation\n\nUse `pip` to install on all systems:\n\n```bash\npip install textcaptcha\n```\n\n## Usage Example\n\nThis example will ask a CAPTCHA question and ask for an answer which is then checked against the actual answer.\n\n```python\nimport textcaptcha\n\n# Create a captcha fetcher to fetch captcha questions from the API\nfetcher = textcaptcha.CaptchaFetcher()\n# Fetch a new captcha from the API\ncaptcha = fetcher.fetch()\n\n# Print the captcha question to the console\nprint(captcha.question)\n# Get a response from the user\nanswer = input("Answer: ")\n\n# Check that the answer is correct\nif captcha.check_answer(answer):\n    print("You\'re not a robot!")\nelse:\n    print("You are a robot, sorry!")\n```\n\n## Development Setup\n\nThis project uses Poetry to manage dependencies and packaging. [Here](https://python-poetry.org/docs/#installation) are the installation instructions for Poetry.\n\n## Contributing\n\n1. Fork it (https://github.com/jake-walker/pytextcaptcha/fork)\n2. Create your feature branch (`git checkout -b feature/foobar`)\n3. Commit your changes (`git commit -am "Add some foobar"`)\n4. Push to the branch (`git push origin feature/foobar`)\n5. Create a new pull request\n',
    'author': 'Jake Walker',
    'author_email': 'hi@jakew.me',
    'maintainer': 'Jake Walker',
    'maintainer_email': 'hi@jakew.me',
    'url': 'https://github.com/jake-walker/pytextcaptcha',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
