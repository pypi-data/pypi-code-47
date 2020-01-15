import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sqlfaker',  
    version='0.5',
    author="Michael Kohlegger",
    author_email="michael.kohlegger@gmail.com",
    description="A fake sql database generator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://documentation.web.fh-kufstein.ac.at/sqlfaker/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )
