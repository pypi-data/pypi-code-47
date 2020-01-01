# coding: utf-8
import os
from importlib.machinery import SourceFileLoader

from setuptools import setup, find_packages

module_name = "html2texttg"

try:
    version = SourceFileLoader(
        module_name,
        os.path.join(module_name, 'version.py')
    ).load_module()

    version_info = version.version_info
except FileNotFoundError:
    version_info = (0, 0, 0)

__version__ = '{}.{}.{}'.format(*version_info)


def load_requirements(fname):
    """ load requirements from a pip requirements file """
    with open(fname) as f:
        line_iter = (line.strip() for line in f.readlines())
        return [line for line in line_iter if line and line[0] != '#']


setup(
    name=module_name,
    version=__version__,
    description="Turn HTML into equivalent Markdown-structured text. Telegram adapted.",
    long_description=open('README.md').read(),
    author="Aaron Swartz",
    author_email="me@aaronsw.com",
    maintainer='Pavka Mosein',
    maintainer_email='pavkazzz@mail.ru',
    url='https://github.com/pavkazzz/html2text/',
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points="""
        [console_scripts]
        html2texttg=html2texttg.cli:main
    """,
    license='GNU GPL 3',
    install_requires=load_requirements('requirements.txt'),
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    long_description_content_type="text/markdown"
)
