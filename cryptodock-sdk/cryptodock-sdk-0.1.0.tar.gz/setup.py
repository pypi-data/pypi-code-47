from pathlib import Path
from setuptools import find_packages, setup

setup(
    name="cryptodock-sdk",
    version="0.1.0",
    description="SDK for CryptoDock's remote API. Includes an semantic API interface, a Strategy Wrapper, and a Backtest Wrapper. The SDK is mean to be leveraged with each strategy bootstrapped from the CryptoDock desktop iOS app interface. All strategy trading and backtesting is managed through the desktop interface, as well.",
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
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests"]
)
