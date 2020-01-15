import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Moliere",
    version="0.0.2",
    author="Peter Menshih",
    author_email="p.menshih@gmail.com",
    description="Psycopg wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/pmenshih/pypg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)