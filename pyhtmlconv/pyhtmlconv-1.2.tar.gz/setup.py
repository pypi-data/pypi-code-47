"""
Setup file.
"""

import sys

sys.dont_write_bytecode = True

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.rst") as fp:
    DESCRIPTION = fp.read()

with open("requirements.txt") as fp:
    REQUIRES = fp.read().split()

setup(
    name="pyhtmlconv",
    license="MIT",
    author="Aprila Hijriyan",
    author_email="hijriyan23@gmail.com",
    version="1.2",
    packages=["pyhtmlconv"],
    url="https://github.com/aprilahijriyan/pyhtmlconv",
    description="pyhtmlconv: html converter (image / pdf)",
    long_description=DESCRIPTION,
    install_requires=REQUIRES,
    long_description_content_type="text/x-rst",
    keywords="html screenshot wkhtmltopdf converter image png jpeg pdf",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
