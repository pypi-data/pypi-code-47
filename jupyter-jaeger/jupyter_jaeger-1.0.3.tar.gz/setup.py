#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['jupyter_jaeger']

package_data = \
{'': ['*']}

install_requires = \
['jaeger_browser', 'notebook', 'jupyter-server-proxy']

entry_points = \
{'jupyter_serverproxy_servers': ['jaeger = jupyter_jaeger:setup_jaeger_all',
                                 'jaeger_proxy = '
                                 'jupyter_jaeger:setup_jaeger_proxy']}

setup(name='jupyter_jaeger',
      version='1.0.3',
      description='Provides jupyter server proxy endpoints for launching Jaeger.',
      author='Saul Shanabrook',
      author_email='saul@quansight.com',
      url='https://github.com/Quansight/jupyter-browser',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      entry_points=entry_points,
      python_requires='>=3.6',
     )
