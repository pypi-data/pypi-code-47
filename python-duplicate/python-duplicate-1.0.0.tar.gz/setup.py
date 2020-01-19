from setuptools import setup, find_packages

setup(
    name="python-duplicate",
    version="1.0.0",
    url="https://github.com/Clement-O/python-duplicate",
    license="MIT",
    author="Clément Omont--Agnes",
    author_email="omont.clement@gmail.com",
    description="Handle duplicate in python",
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
    zip_safe=False,
    install_requires=["psycopg2-binary", "PyMySQL"],
    project_urls={
        "Documentation": "https://python-duplicate.readthedocs.io/en/latest/python-duplicate/",
        "Source": "https://github.com/Clement-O/python-duplicate",
    },
)
