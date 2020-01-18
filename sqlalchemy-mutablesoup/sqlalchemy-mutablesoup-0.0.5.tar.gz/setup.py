import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlalchemy-mutablesoup",
    version="0.0.5",
    author="Dillon Bowen",
    author_email="dsbowen@example.com",
    description="Mutable BeautifulSoup database type",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dsbowen/sqlalchemy-mutablesoup",
    packages=setuptools.find_packages(),
    install_requires=[
        'bs4==0.0.1',
        'flask==1.1.1',
        'sqlalchemy==1.3.12',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)