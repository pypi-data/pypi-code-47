import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="simple_ftw",
    version="0.0.4",
    author="Fiona Tahta-Wraith",
    author_email="fionatw@outlook.com",
    description="my first published package",
    long_description=long_description,
    loan_description_content_type="text/markdown",
    url="https://github.com/fiona-tw/ftw",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
