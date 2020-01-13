# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['et_stopwatch']
setup_kwargs = {
    'name': 'et-stopwatch',
    'version': '0.2.0',
    'description': '<Enter a one-sentence description of this project here.>',
    'long_description': '============\net-stopwatch\n============\n\nA context manager for timing code.\n\nTypical use:\n\n.. code-block:: python\n\n    # Create a Stopwath with and end message string and printed 3 digits\n    with Stopwatch("time 5 times \'sleep(1)\': ",ndigits=3) as tmr:\n        for i in range(5):\n            sleep(1) # supposing there isn\'t anything more useful to oo ;-)\n            print(i,tmr.timelapse()) # time since last call to timelapse()\n\n    print(tmr.time) # the total time\n\nRunning this code yields:\n\n.. code-block:: bash\n\n    0 1.004\n    1 1.004\n    2 1.004\n    3 1.004\n    4 1.004\n    time 5 times \'sleep(1)\': 5.02 s\n    5.02\n\n* Free software: MIT license\n* Documentation: https://et-stopwatch.readthedocs.io.\n\n\n',
    'author': 'Engelbert Tijskens',
    'author_email': 'engelbert.tijskens@uantwerpen.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/etijskens/et-stopwatch',
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
