# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['homie_power_supply_node']

package_data = \
{'': ['*']}

install_requires = \
['homie-spec>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'homie-power-supply-node',
    'version': '0.1.2',
    'description': 'homie-power-supply-node is a Python package that uses homie-spec to provide a homie node implementation that can be used to create Homie-compliant messages from your power supply device.',
    'long_description': '# homie-power-supply-node\n\n**homie-power-supply-node** is a Python package that uses homie-spec to provide a homie node implementation that can be used to create Homie-compliant messages from your power supply device.\n\nThis package has no dependencies other than **Python >=3.6** and `homie-spec`. \nOnly Linux is supported at the moment, as it uses `/sys/class/power_supply/*/uevent` to read the power supply properties.\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install `homie-power-supply-node`.\n\n```bash\npip install homie-power-supply-node\n```\n\n## Usage\n```python\nfrom homie_spec import Device\nfrom homie_power_supply_node import PowerSupply\n\ndesktop = Device(\n    id="desktop",\n    name="Desktop Computer",\n    nodes={"battery": PowerSupply("BAT0").node(whitelist_properties=["capacity"])},\n)\n\nmessages = desktop.messages()\nassert next(messages).topic == "homie/desktop/$state"\nassert next(messages).topic == "homie/desktop/$name"\nassert next(messages).topic == "homie/desktop/$homie"\nassert next(messages).topic == "homie/desktop/$implementation"\nassert next(messages).topic == "homie/desktop/$nodes"\n\nmsg = next(messages)\nassert msg.topic == "homie/desktop/battery/$name"\nassert msg.payload == "BAT0"\n\nmsg = next(messages)\nassert msg.topic == "homie/desktop/battery/$type"\nassert msg.payload == "power-supply"\n\nmsg = next(messages)\nassert msg.topic == "homie/desktop/battery/$properties"\nassert msg.payload == "capacity"\n\nmsg = next(messages)\nassert msg.topic == "homie/desktop/battery/capacity/$name"\nassert msg.payload == "Capacity"\n\nmsg = next(messages)\nassert msg.topic == "homie/desktop/battery/capacity/$datatype"\nassert msg.payload == "integer"\n\nmsg = next(messages)\nassert msg.topic == "homie/desktop/battery/capacity/$unit"\nassert msg.payload == "%"\n\nmsg = next(messages)\nassert msg.topic == "homie/desktop/battery/capacity/$format"\nassert msg.payload == "0:100"\n\n\nprint(\n    "Current battery capacity: "\n    f"{format(desktop.getter_message(\'battery/capacity\').payload)}%"\n)\n"""\n```\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'Xavier Francisco',
    'author_email': 'xavier.n.francisco@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Qu4tro/homie-power-supply-node/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
