import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MkNxGn_OpenScale",
    version="0.1.0.3",
    author="Mark Cartagena",
    author_email="mark@mknxgn.com",
    description="MkNxGn Sparkfun OpenScale Helper - Serial",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://mknxgn.com/",
    install_requires=['pyserial'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
