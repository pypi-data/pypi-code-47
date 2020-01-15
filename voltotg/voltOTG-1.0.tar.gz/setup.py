import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="voltOTG",
    version="1.0",
    author="Gbitur",
    author_email="theemosunrise@gmail.com",
    description="A package to communicate with the voltOTG usb volt-meter ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gbit-is/voltOTG",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)
