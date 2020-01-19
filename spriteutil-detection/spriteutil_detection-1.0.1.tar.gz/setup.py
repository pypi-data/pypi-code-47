import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("LICENSE", "r") as li:
    license_text = li.read()


__author__ = "Phuong Duy PHUNG"
__copyright__ = "Copyright (C) 2019, Intek Institute"
__email__ = "duy.phung@f4.intek.edu.vn"
__license__ = "MIT"
__maintainer__ = "Phuong Duy PHUNG"
__version__ = "1.0.1"
__README__ = long_description


setup(
    name="spriteutil_detection",
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/intek-training-jsc/sprite-sheet-duyphungbatch3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "bleach==3.1.0",
        "certifi==2019.11.28",
        "cffi==1.13.2",
        "chardet==3.0.4",
        "cryptography==2.8",
        "docutils==0.16",
        "idna==2.8",
        "importlib-metadata==1.4.0; python_version < '3.8'",
        "jeepney==0.4.2; sys_platform == 'linux'",
        "keyring==21.1.0",
        "more-itertools==8.1.0",
        "numpy==1.18.1",
        "pillow==7.0.0",
        "pipfile==0.0.2",
        "pkginfo==1.5.0.1",
        "pycparser==2.19",
        "pygments==2.5.2",
        "readme-renderer==24.0",
        "requests==2.22.0",
        "requests-toolbelt==0.9.1",
        "secretstorage==3.1.2; sys_platform == 'linux'",
        "six==1.14.0",
        "toml==0.10.0",
        "tqdm==4.41.1",
        "twine==3.1.1",
        "urllib3==1.25.7",
        "webencodings==0.5.1",
        "wheel==0.33.6",
        "zipp==1.0.0",
    ],
    extras_require={
        "dev": [
            "appdirs==1.4.3",
            "astroid==2.3.3",
            "attrs==19.3.0",
            "black==19.10b0; python_version >= '3.6'",
            "cached-property==1.5.1",
            "cerberus==1.3.2",
            "certifi==2019.11.28",
            "chardet==3.0.4",
            "click==7.0",
            "colorama==0.4.1",
            "distlib==0.3.0",
            "first==2.0.2",
            "idna==2.8",
            "importlib-metadata==1.4.0; python_version < '3.8'",
            "isort==4.3.21",
            "lazy-object-proxy==1.4.3",
            "mccabe==0.6.1",
            "more-itertools==8.1.0",
            "orderedmultidict==1.0.1",
            "packaging==19.2",
            "pathspec==0.7.0",
            "pep517==0.8.1",
            "pip-shims==0.4.0",
            "pipenv-setup==2.2.5",
            "pipfile==0.0.2",
            "plette[validation]==0.2.3",
            "pylint==2.4.4",
            "pyparsing==2.4.6",
            "regex==2020.1.8",
            "requests==2.22.0",
            "requirementslib==1.5.3",
            "six==1.14.0",
            "toml==0.10.0",
            "tomlkit==0.5.8",
            "typed-ast==1.4.1; implementation_name == 'cpython' and python_version < '3.8'",
            "typing==3.7.4.1",
            "urllib3==1.25.7",
            "vistir==0.5.0",
            "wheel==0.33.6",
            "wrapt==1.11.2",
            "zipp==1.0.0",
        ]
    },
)
