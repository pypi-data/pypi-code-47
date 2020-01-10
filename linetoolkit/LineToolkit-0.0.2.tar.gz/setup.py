import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="LineToolkit",
    version="0.0.2",
    author="Kirin Lin",
    author_email="chilin.lin@gmail.com",
    description="Some simple tools for Line Notify API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kirin-lin/LineToolkit",
    py_modules=['LineToolkit'],
)
