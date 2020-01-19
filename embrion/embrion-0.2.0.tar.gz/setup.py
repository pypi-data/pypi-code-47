from setuptools import setup, find_packages
import io
import re

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("embrion/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

setup(
    name='embrion',
    version=version,
    license='MIT',
    long_description=readme,
    author='Izel Levy',
    author_email='izel93@gmail.com',
    url='https://gitlab.com/izel93/embrion',
    keywords=['development', 'environment', 'docker'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        embrion=embrion.cli:main
    '''
)
