import ast
import re
import os
from setuptools import setup

PACKAGE_NAME = "kenetsu"

with open(os.path.join(PACKAGE_NAME, '__init__.py')) as f:
    match = re.search(r'__version__\s+=\s+(.*)', f.read())
version = str(ast.literal_eval(match.group(1)))

setup(
    name=PACKAGE_NAME,
    version=version,
    packages=[PACKAGE_NAME],
    python_requires=">=2.7",
    description="Maillog summarizer",
    long_description="Maillog summarization tool by mail status from Postfix",
    url="https://github.com/elastic-infra/kenetsu",
    author="Tomoya KABE",
    author_email="kabe@elastic-infra.com",
    license="MIT",
    classifiers=[
                 "Topic :: Communications :: Email",
                 "Topic :: Internet :: Log Analysis",
    ],
    extras_require={
        "dev": [
            "pytest>=3",
            "coverage",
            "tox",
            "twine",
        ],
    },
    entry_points="""
        [console_scripts]
        {app}={pkg}.cli:main
    """.format(app=PACKAGE_NAME.replace('_', '-'), pkg=PACKAGE_NAME)
)
