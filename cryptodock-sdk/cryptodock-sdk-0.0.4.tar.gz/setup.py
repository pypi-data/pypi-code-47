from pathlib import Path
from setuptools import find_packages, setup

setup(
    name="cryptodock-sdk",
    version="0.0.4",
    description="SDK for CryptoDock's remote API. Included when bootstrapping a new strategy template with the CryptoDock desktop iOS app, and used in the CryptoDock remote backtesters.",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/the-launch-tech/cryptodock-sdk",
    author="Daniel Griffiths",
    author_email="daniel@thelaunch.tech",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "cryptodock_sdk=cryptodock_sdk.sdk.__main__:prove_instance",
        ]
    },
)
