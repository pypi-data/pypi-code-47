from setuptools import setup
import re

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('discord/ext/boardgames/__init__.py') as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

with open('README.rst') as f:
    readme = f.read()

setup(
    name='discord-ext-boardgames',
    author='bijij',
    url='https://github.com/bijij/discord-ext-boardgames',
    version=version,
    packages=['discord/ext/boardgames'],
    license='MIT',
    description='Interactive board game session for discord.py',
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements
)
