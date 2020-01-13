from distutils.core import setup

setup(
    name='pycliSOF',
    version='0.1.6',
    author='Harshit Babbar',
    author_email='harshitbabbar968@gmail.com',
    packages=['pystack'],
    url='http://pypi.python.org/pypi/pycliSOF/',
    license='LICENSE.txt',
    description='bash stack script',
    long_description=open('README.txt').read(),
    install_requires=[
        'bs4',
        'requests',
	'colorama',
	'texttable',
    ]
)
