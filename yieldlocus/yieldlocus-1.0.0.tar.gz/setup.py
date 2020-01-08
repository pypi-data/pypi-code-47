from setuptools import setup
import os





this_dir = os.path.dirname(__file__)

with open(os.path.join(this_dir, "README.md"), "rb") as fo:
    long_description = fo.read().decode("utf8")
setup(
    name='yieldlocus',
    package_dir={"": "source"},
    py_modules=['yieldlocus'],
    version="1.0.0",
    description='Plotting yield locus for various test results',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='omkar_salunke',
    author_email='ossalunke@gmail.com',
    url='https://github.com/omkar-salunke/yield_locus/',
    license="MIT",
    download_url=(
        'https://github.com/omkar-salunke/yield_locus/archive/v{}.tar.gz'

    ),
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
