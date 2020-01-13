"""Setuptools install script"""
from setuptools import setup, find_packages

setup(
    name="tekinstr",
    version="0.0.0",
    author="Lee Johnston",
    author_email="lee.johnston.100@gmail.com",
    description="Communication with Tektronix oscilloscopes",
    packages=find_packages(),
    license="MIT",
    install_requires=["numpy", "sympy", "unit_system", "pyvisa"],
)
