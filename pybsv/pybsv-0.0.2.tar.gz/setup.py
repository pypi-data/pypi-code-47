from setuptools import setup

setup(
    name="pybsv",
    version="0.0.2",
    description="An easy to use Python BSV client.",
    url="http://github.com/jannainm/pybsv",
    author="jannainm",
    author_email="jannainm@gmail.com",
    license="MIT",
    packages=["pybsv"],
    install_requires=["bitsv<1"],
    zip_safe=False,
)
