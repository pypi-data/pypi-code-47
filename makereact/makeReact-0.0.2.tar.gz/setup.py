import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('makeReact/script.py').read(),
    re.M
    ).group(1)

# long_descr=""


# with open("README.rst", "rb") as f:
#     long_descr = f.read()
#  long_description_content_type="text/markdown",
# print(long_descr)


setup(
    name = "makeReact",
    packages = ["makeReact"],
    entry_points = {
        "console_scripts": ['makeReact = makeReact.script:main']
        },
    version = version,
    description = "makeReact is a python package which helps react and react-native developer to speed-up their develoment process.",
    long_description_content_type="text/markdown",
    author = "Hur Ali",
    author_email = "hurali97@gmail.com",
    )