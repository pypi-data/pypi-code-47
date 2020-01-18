import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ezml",
    version="1.0.3",
    author="Chad M. Groom",
    author_email="chadgroom17@gmail.com",
    description="An (extremly) simple markup language, this is the parser!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chadgroom/EZML",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
