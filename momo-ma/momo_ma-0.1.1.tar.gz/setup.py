
from setuptools import setup, find_packages
import io
import re


with io.open("README.rst", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("momo/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

setup(
    name="momo_ma",
    version=version,
    packages = find_packages(),
    include_package_data = True,
    install_requires=[
        'click',
        'colorama',
        'selenium',
        'pyfiglet',

    ],
    entry_points='''
    [console_scripts]
    momo=momo.cli:momo
    ''',
    author="Weicai",
    author_email="liuweicai90s@126.com",
    long_description=readme,

)