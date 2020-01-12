import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stickytoe_device",
    version="0.0.4",
    author="Ryan Chaiyakul",
    description="Stickytoe device abstract class and constants",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryanchaiyakul/stickytoe_device",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
