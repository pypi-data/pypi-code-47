import codecs
import os
import re
import sys

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("bscc# Unable to find version string.")


str_long_description = read('README.rst')

setup(
    name="bscc",
    version=find_version("src", "bscc", "__init__.py"),
    description="A shiphandling simulator interface for digital shipyard",
    long_description=str_long_description,

    license='MIT',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        #
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research ",
        #
        "License :: OSI Approved :: MIT License",
        #
        "Operating System :: OS Independent",
        #
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        #
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    
    url='https://github.com/bscc/bscc/wiki',
    keywords='bscc shipyard shipwright shiphandling simulator model ship',

    author='Kang Shumin',
    author_email='kangshumin800@gmail.com',

    package_dir={"": "src"},
    packages=find_packages(
        where="src",
        exclude=["contrib", "docs", "tests*", "tasks"],
    ),
    
    
    
    package_data={
        'bscc': ['package_data.dat'],
        "bscc._vendor.certifi": ["*.pem"],
        "bscc._vendor.distlib._backport": ["sysconfig.cfg"],
        "bscc._vendor.distlib": ["t32.exe", "t64.exe", "w32.exe", "w64.exe"],
    },
    data_files=[('my_data', ['data/data_file'])],  # Optional



    #To actually restrict what Python versions a project can be installed on
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',


    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # bscc# does not have any direct dependencies.
    #install_requires=['peppercorn'],  # Optional

    # to install these using the "extras" syntax, for example:
    #   $ pip install bscc[dev]
    extras_require={  # Optional
        "watchdog": ["watchdog"],
        "termcolor": ["termcolor"],
        "dev": [
            "pytest",
            "coverage",
            "tox",
            "sphinx",
            "pallets-sphinx-themes",
            "sphinx-issues",
        ],
    },
    
    

    entry_points={
        "console_scripts": [
            "shipwright=bscc.shipwright:main",
            "shipwright%s=bscc.shipwright:main" % sys.version_info[:1],
            "shipwright%s.%s=bscc.shipwright:main" % sys.version_info[:2],
            "bscc=bscc:main",
        ],
    },


    zip_safe=False,
)
