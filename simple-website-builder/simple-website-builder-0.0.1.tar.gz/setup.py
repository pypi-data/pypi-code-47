import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="simple-website-builder", # Replace with your own username
    version="0.0.1",
    author="Hoa Nguyen",
    author_email="hoanguyen@ucdavis.edu",
    description="A website builder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/takekoputa/simple-website-builder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.5',
)