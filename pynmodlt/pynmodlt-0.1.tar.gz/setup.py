from setuptools import setup

setup(name='pynmodlt',
      version='0.1',
      description='NMODL parsing and compiling tools, updated fork from borismarin pynmodl (http://github.com/borismarin/pynmodl)',
      url='http://github.com/tjbanks/pynmodl',
      author='Tyler Banks',
      author_email='tyler@tylerbanks.net',
      license='MIT',
      packages=['pynmodl'],
      package_data={'pynmodl': ['tests/sample_mods/*.mod', 'grammar/*.tx',
                                'tests/parsing/*.dat']},
      zip_safe=False,
      setup_requires=['pytest-runner'],
      install_requires=['textx==1.6.1', 'xmltodict'],
      tests_require=['pytest', 'textx', 'xmltodict'],
      )