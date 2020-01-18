import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlalchemy-orderingitem",
    version="0.0.3",
    author="Dillon Bowen",
    author_email="dsbowen@wharton.upenn.edu",
    description="SQLAlchemy-OrderingItem provides an OrderingItem base for children of orderinglist relationships.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dsbowen/sqlalchemy-orderingitem",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'sqlalchemy==1.3.12',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)