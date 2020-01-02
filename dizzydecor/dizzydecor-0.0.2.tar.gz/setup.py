import setuptools

with open("README.rst", "r") as fin:
    long_description = fin.read()

setuptools.setup(
    name="dizzydecor",
    version="0.0.2",
    author="Tyler Nullmeier",
    author_email="Tylerzeromaster@gmail.com",
    description="Web service decorators for tornado",
    python_requires='>=3',
    license="MIT",
    keywords="tornado webservice web service oriented SOA decorator",
    url="https://github.com/TylerZeroMaster/dizzydecor",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/x-rst",
    install_requires=["tornado"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
    ],
)
