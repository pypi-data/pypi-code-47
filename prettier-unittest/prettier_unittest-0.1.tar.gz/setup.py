"""Needed for package creation"""

from setuptools import setup

setup(
    name="prettier_unittest",
    version="0.1",
    description="A small package to easily setup unittests and have a better rendering",
    keywords="prettier pretty color unittest unit test",
    url="https://github.com/SpartanPlume/PrettierUnittestPython",
    author="Spartan Plu,e",
    author_email="spartan.plume@gmail.com",
    license="MIT",
    packages=["prettier_unittest"],
    scripts=["bin/prettier-unittest"],
    install_requires=["Pygments", "blessings"],
    zip_safe=False,
)

