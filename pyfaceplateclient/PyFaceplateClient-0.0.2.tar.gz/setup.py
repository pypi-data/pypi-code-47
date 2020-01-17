import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyFaceplateClient", # Replace with your own username
    version="0.0.2",
    author="Rustam Krikbayev",
    author_email="rkrikbaev@gmail.com",
    description="Client for Faceplate powered by Ecomet database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rkrikbaev/pyfaceplateclient",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)