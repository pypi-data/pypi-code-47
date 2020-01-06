from setuptools import setup


with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="bver",
    py_modules=["bver"],
    version="v0.1.1",
    description="A simple Bible translation parser for human input",
    author="MotS",
    author_email="ted.jameson@pm.me",
    url="https://code.theres.life/heb12/bver",
    keywords=["bible", "json", "parser"]
)
