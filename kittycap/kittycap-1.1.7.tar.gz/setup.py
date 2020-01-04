import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kittycap",
    version="1.1.7",
    author="KittyCore",
    author_email="code@kittycore.xyz",
    description="KittyCap python interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kittycore/kittycap",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'appdirs',
        'argparse',
    ],
    entry_points = {
        'console_scripts': ['kittycap=kittycore.cli:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)