from distutils.core import setup

setup(
    name='py-nhl',
    version='0.0.1',
    author='Brian Devins-Suresh',
    author_email='badevins@gmail.com',
    packages=['nhl', 'nhl.test'],
    url='http://pypi.python.org/pypi/py-nhl/',
    license='Apache-2.0',
    description='NHL API Client',
    long_description=open('README.md').read(),
    install_requires=[],
)