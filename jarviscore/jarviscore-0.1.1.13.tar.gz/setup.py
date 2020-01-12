import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()



setuptools.setup(
    name="jarviscore",
    version="0.1.1.13",
    author="Cubbei",
    author_email="author@example.com",
    description="A python package for creating Twitch Bots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dev.azure.com/cubbei/jarviscore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        # "LICENSE :: OSI APPROVED :: GNU GENERAL PUBLIC LICENSE (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)