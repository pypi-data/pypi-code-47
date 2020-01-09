import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rmprogress", 
    version="0.0.3",
    author="Rajan Mandanka",
    author_email="rajanmandanka@gmail.com",
    description="A terminal process package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rajanmandanka/process",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
