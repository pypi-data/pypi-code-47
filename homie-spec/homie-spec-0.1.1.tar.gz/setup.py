# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['homie_spec']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'homie-spec',
    'version': '0.1.1',
    'description': 'homie-spec is a Python library that handles the v4 Homie Convention',
    'long_description': '# homie-spec\n\n[![Build Status](https://travis-ci.com/Qu4tro/homie-spec.svg?branch=master)](https://travis-ci.com/Qu4tro/homie-spec)\n\nhomie-spec is a Python library that handles the v4 [Homie Convention](https://homieiot.github.io/).\n\nThis package has no dependencies other than **Python >=3.6**. Since it doesn\'t implement MQTT this also means it\'s fairly useless on it\'s own, as it has no ability to interact with any MQTT broker on it\'s own.\n\nThe goal of this package is to provide a data-driven library to easily create `devices`, `nodes` and `properties`. These can also be published to be used by anyone.\nAnother package (WIP), will bridge the MQTT protocol and `homie-spec`.\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install `homie-spec`.\n\n```bash\npip install homie-spec\n```\n\n## Usage\n\n```python\n\nfrom homie_spec import Device, Node, Property\nfrom homie_spec.properties import Datatype\n\n\nlocaltime = Node(\n    name="Local time",\n    typeOf="clock",\n    properties={\n        "color-repr": Property(\n            name="Color representation", datatype=Datatype.COLOR, get=lambda: "233,102,23"\n        ),\n        "time": Property(\n            name="HH:MM representation", datatype=Datatype.STRING, get=lambda: "20:20"\n        ),\n    },\n)\n\ndesktop = Device(id="desktop", name="Desktop Computer", nodes={"local-time": localtime})\n\nfor msg in desktop.messages():\n    print(msg.attrs)\nprint(desktop.getter_message(\'local-time/time\').attrs)\nprint(desktop.getter_message(\'local-time/color-repr\').attrs)\n\n"""\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/$state\',                          \'payload\': \'init\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/$name\',                           \'payload\': \'Desktop Computer\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/$homie\',                          \'payload\': \'4.0.0\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/$implementation\',                 \'payload\': \'homie-spec\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/$nodes\',                          \'payload\': \'local-time\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/local-time/$name\',                \'payload\': \'Local time\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/local-time/$type\',                \'payload\': \'clock\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/local-time/$properties\',          \'payload\': \'color-repr,time\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/local-time/color-repr/$name\',     \'payload\': \'Color representation\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/local-time/color-repr/$datatype\', \'payload\': \'color\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/local-time/time/$name\',           \'payload\': \'HH:MM representation\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/local-time/time/$datatype\',       \'payload\': \'string\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/$state\',                          \'payload\': \'ready\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/local-time/time\',                 \'payload\': \'20:20\'}\n{\'retained\': True, \'qos\': 1, \'topic\': \'homie/desktop/local-time/color-repr\',           \'payload\': \'233,102,23\'}\n"""\n```\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'Xavier Francisco',
    'author_email': 'xavier.n.francisco@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
