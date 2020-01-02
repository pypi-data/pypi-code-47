import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-heideltime-krypton",
    version="0.0.2",
    author="Bharadwaj Srigiriraju",
    author_email="krishna.bharadwaj6@gmail.com",
    description="Python wrapper for Heideltime library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vetted/python-heideltime",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_dir={'HeidelTime': 'HeidelTime'},
    package_data={'HeidelTime': ['*.jar']}
)
