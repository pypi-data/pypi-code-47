import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-address-checker",
    version="0.1.2",
    author="ramdani muksin",
    author_email="ramd4ni@gmail.com",
    description="A Simple Address checker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xhijack/simple-address-checker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)