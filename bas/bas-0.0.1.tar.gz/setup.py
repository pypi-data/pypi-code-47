from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
readme_filename = path.join(this_directory, 'README.md')

with open(readme_filename, encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bas',
    version='0.0.1',
    description='bas client and cli',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='youka.club@gmail.com',
    url='https://github.com/youka-club/bas',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click==7.0',
        'requests==2.21.0',
    ],
    entry_points='''
        [console_scripts]
        bas=bas.cli.cli:cli
    ''',
)