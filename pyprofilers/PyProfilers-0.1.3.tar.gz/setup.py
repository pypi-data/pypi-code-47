from setuptools import setup

about = {}
with open("pyprofilers/__about__.py") as file:
    exec(file.read(), about)

with open("README.md") as file:
    readme = file.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    author=about["__author__"],
    license=about["__license__"],
    packages=["pyprofilers"],
    install_requires=[
        "cython",
        "line_profiler",
        "yappi",
    ],
    python_requires=">=3.6",
)
