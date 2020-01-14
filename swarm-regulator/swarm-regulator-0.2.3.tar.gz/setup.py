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
    'version': '0.2.3',
    'description': 'The regulator of your Docker Swarm cluster',
    'long_description': '# Swarm Regulator\n\nRegulate your Docker Swarm cluster, according to YOUR rules. Use `async` Python functions to enforce rules like service placement and resource management on your Docker Swarm.\n\n## Concepts\n\n### Consumer\n\nEach regulator is based on top of a single consumer. The consumer responds to Docker events and instruments all components of the regulator.\n\n### Conditions\n\nA regulator needs to know when to apply its rules. This is what conditions are for. Conditions help us know when should a rule be applied on a Docker Swarm entity. In brief, a condition is a Python function (or callable) that accepts a Docker Swarm entity as a single argument and returns `True` when the rule should run, and `False` when it shouldn\'t.\n\n**🙌 Heads up**: In order to avoid infinite loops, a confition that initially returns `True`, should return `False`, when it gets the regulated entity as an argument. If this is not the case, the rule is being ignored.\n\n### Rules\n\nRules simply do the job. Rules are **`async`** Python functions that accept a Docker Swarm entity as an argument and return it modified, so it complies with the business logic we intend to enforce on our Docker Swarm cluster.\n\n## Requirements\n\n- Python 3.8+\n- Docker Swarm Mode cluster\n\n## Install\n\n### pipenv\n\n```\npipenv install swarm-regulator\n```\n\n### poetry\n\n```\npoetry add swarm-regulator\n```\n\n### pip\n\n```\npip install swarm-regulator\n```\n\n## Run\n\n1. Create a Python file (e.g. `regulator.py`)\n2. Import the `consumer` from the `swarm_regulator` package\n3. Register your rules that will run according to given conditions\n4. Run your regulator\n\n## Example\n\n### `regulator.py`\n```py\nfrom swarm_regulator import consumer\n\n\ndef _extract_constraints(service_spec):\n    return service_spec["TaskTemplate"]["Placement"].get("Constraints", [])\n\n\ndef has_not_constraints(service_spec) -> bool:\n    constraints = _extract_constraints(service_spec)\n    return not len(constraints)\n\n\nasync def do_not_schedule_on_gpu(service_spec):\n    constraints = _extract_constraints(service_spec) + ["node.labels.gpu!=true"]\n    service_spec["TaskTemplate"]["Placement"]["Constraints"] = constraints\n    return service_spec\n\n\nconsumer.register_rule(\n    "service", has_not_constraints, do_not_schedule_on_gpu,\n)\n\nconsumer.run()\n```\n\n### Run\n\n```console\npython regulator.py\n```\n',
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
