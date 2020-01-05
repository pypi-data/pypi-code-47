import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ttchat",
    version="0.1.0",
    author="Adam Thompson-Sharpe",
    author_email="adamthompsonsharpe@gmail.com",
    description="Peer-to-peer chat software written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MysteryBlokHed/ttchat",
    packages=setuptools.find_packages(),
    install_requires=[
        "cryptography>=2.8"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)