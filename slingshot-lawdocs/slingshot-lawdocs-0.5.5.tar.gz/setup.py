from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name = "slingshot-lawdocs",
    packages = find_packages(),
    version = "0.5.5",
    license = "MIT",
    description = "Slingshot is a Python library bringed on by A Mosca team for creating reproducible procedural documents for Brazilian law-suits.",
    author = "A Mosca",
    author_email = "staff.amosca@gmail.com",
    url = "https://github.com/amosca-team/slingshot/",
    long_description = long_desc,
    long_description_content_type='text/markdown',
    install_requires = ["pdfkit",
                        "pypandoc",
                        "markdown"
                        ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7"
    ]
)