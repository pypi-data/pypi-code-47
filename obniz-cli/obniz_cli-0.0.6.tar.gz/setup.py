import setuptools
from codecs import open
from os import path
import re

root_dir = path.abspath(path.dirname(__file__))

with open("README.md", "r") as f:
    long_description = f.read()

with open(path.join(root_dir, 'obniz_cli_', '__version__.py')) as f:
    init_text = f.read()
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

setuptools.setup(
    name='obniz_cli',
    version=version,
    description='cli tool for obnizOS setup',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url='',
    install_requires=["esptool", "requests"],
    py_modules=['obniz_cli'],
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "obniz_cli=obniz_cli:main"
        ]
    }
)