from pathlib import Path
from setuptools import find_packages, setup

setup(
    name="cryptodock-sdk",
    version="0.1.1",
    description="SDK for CryptoDock's remote API. Includes an semantic API interface, Strategy Wrapper and Backtest Wrapper. The SDK is meant to be leveraged with strategies bootstrapped from the CryptoDock desktop interface. Strategy trading and backtesting is managed through the desktop app interface.",
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
