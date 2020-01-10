import os

from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='btc-simple-wizard',
    version='0.2',
    packages=['simple_wizard'],
    include_package_data=True,
    license='BSD License',
    description='A simple application with some classes and scripts for wizard implementation.',
    long_description=README,
    url='https://github.com/MEADez/btc-simple-manager',
    author='MEADez',
    author_email='m3adez@gmail.com',
    install_requires=['Django>=2.1.4'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
