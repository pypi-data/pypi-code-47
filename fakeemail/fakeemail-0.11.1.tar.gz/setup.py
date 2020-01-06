from setuptools import setup

with open("README.rst") as readme:
    long_description = readme.read()

setup(
    name='fakeemail',
    version='0.11.1',
    author='Tom Wardill',
    author_email='tom@howrandom.net',
    description='A fake Email Server with a Web Front End',
    long_description_content_type="text/x-rst",
    long_description=long_description,
    url='https://github.com/tomwardill/FakeEmail',
    zip_safe=True,
    packages=['fakeemail', 'twisted.plugins'],
    install_requires=[
        'Twisted',
        'jinja2',
        'six',
        'zope.interface>=3.6.0',
    ],
    package_data={
        'twisted': ['plugins/fakeemail.py'],
        'fakeemail': ['templates/*']
        },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'fakeemail=fakeemail.server:start'
        ]
    }
)
