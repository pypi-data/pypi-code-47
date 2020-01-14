# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['swarm_regulator', 'swarm_regulator.event_types']

package_data = \
{'': ['*'], 'swarm_regulator': ['fixtures/*']}

install_requires = \
['aiodocker>=0.17.0,<0.18.0', 'pytest-asyncio>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'swarm-regulator',
    'version': '0.1.1',
    'description': 'The regulator of your Docker Swarm cluster',
    'long_description': '# Swarm Regulator\n\nRegulate your Docker Swarm cluster, with YOUR rules.\n\nTBD\n\n## Requirements\n\n- Docker Swarm Mode cluster\n\n## Install\n\nTBD\n\n## Run\n\nTBD\n\n## Example\n\n### `regulator.py`\n```py\nfrom swarm_regulator import consumer\n\n\ndef _extract_constraints(service_spec):\n    return service_spec["TaskTemplate"]["Placement"].get("Constraints", [])\n\n\ndef has_not_constraints(service_spec) -> bool:\n    constraints = _extract_constraints(service_spec)\n    return not len(constraints)\n\n\nasync def do_not_schedule_on_gpu(service_spec):\n    constraints = _extract_constraints(service_spec) + ["node.labels.gpu!=true"]\n    service_spec["TaskTemplate"]["Placement"]["Constraints"] = constraints\n    return service_spec\n\n\nconsumer.register_rule(\n    "service", has_not_constraints, do_not_schedule_on_gpu,\n)\n\nconsumer.run()\n```\n\n### Run\n\n```console\npython regulator.py\n```\n',
    'author': 'Paris Kasidiaris',
    'author_email': 'paris@sourcelair.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
