from setuptools import setup

long_description = open('README.md').read()

setup(
    name='IcoCube',
    version='0.0.1-alpha.6',
    packages=['ICO3Core', 'ICO3Core.Node', 'ICO3Core.Module', 'ICO3Plugin', 'ICO3Plugin.Plugin', 'ICO3Plugin.Message',
              'ICO3Plugin.ConnectionManager', 'ICO3Server', 'ICO3Utilities', 'ICO3Utilities.Xml', 'ICO3Utilities.Debug',
              'ICO3PluginCollection', 'ICO3PluginCollection.MessageView'],
    data_files=[('bitmaps', ['ICO3Server/icocube.gif'])],
    url='',
    license='MIT',
    author='Gilles PREVOT',
    author_email='gilles.icocube@gmail.com',
    description='ICOCUBE Python Core',
    long_description=long_description
)
