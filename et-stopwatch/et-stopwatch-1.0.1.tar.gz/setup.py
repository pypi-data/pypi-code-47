# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['et_stopwatch']
setup_kwargs = {
    'name': 'et-stopwatch',
    'version': '1.0.1',
    'description': 'A class for timing code (start/stop, context manager, decorator).',
    'long_description': '============\net-stopwatch\n============\n\nA class for timing code. A Stopwatch object can be used to time code using its ``start`` and\n``stop`` methods::\n\n    from et_stopwatch import Stopwatch\n\n    stopwatch = Stopwatch() # create and start the stopwatch\n    sleep(1)\n    stopwatch.stop()\n    print(stopwatch)\n\n    stopwatch : 1.003744 s\n\nUse as a **context manager**::\n\n    with Stopwatch(message=\'This took\') as sw: # using a custom message\n        for i in range(3):\n            sleep(1)\n            print(i, sw.stop(), \'s\') # stop() returns the time since the last call to start|stop in seconds\n\n    0 1.004943\n    1 1.004948\n    2 1.003404\n    This took :\n        total  : 3.0132949999999994 s\n        minimum: 1.003404 s\n        maximum: 1.004948 s\n        mean   : 1.004432 s\n        stddev : 0.000727 s\n        count  : 3\n\nSince stop was called more than once, some statistics are printed. Calling stop\nautomatically restarts the stopwatch and as a consequence the stopwatch also measures the overhead of\nthe iteration over i. To avoid this, explicitly call start::\n\n    with Stopwatch(message=\'This took\') as sw:\n        for i in range(3):\n            sw.start()               # restart the stopwatch\n            sleep(1)\n            print(i, sw.stop(), \'s\') # stop() returns the time since the last call to start|stop in seconds\n\n    0 1.004388\n    1 1.004173\n    2 1.003048\n    This took :\n        total  : 3.011609 s\n        minimum: 1.003048 s\n        maximum: 1.004388 s\n        mean   : 1.00387 s\n        stddev : 0.000588 s\n        count  : 3\n\nThis time, the timing are slightly shorter for each iteration.\n\nUse as a **decorator**::\n\n    @Stopwatch(name="say_hi_and_sleep_two_seconds", ndigits=3) # custom message, print only 3 digits.\n    def say_hi_and_sleep_two_seconds():\n        print("hi")\n        sleep(2)\n\n    say_hi_and_sleep_two_seconds()\n\n    hi\n    say_hi_and_sleep_two_seconds : 2.003 s\n\n* Free software: MIT license\n* Documentation: https://et-stopwatch.readthedocs.io.\n\n\n',
    'author': 'Engelbert Tijskens',
    'author_email': 'engelbert.tijskens@uantwerpen.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/etijskens/et-stopwatch',
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
