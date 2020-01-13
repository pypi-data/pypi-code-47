import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open('tax2peptide/version.py').read())

setuptools.setup(
    name="tax2peptide", 
    version=__version__,
    author="Juliane Schmachtenberg",
    author_email="jule-schmachtenberg@web.de",
    description="tax2peptide creates based on given taxon IDs and a reference database a taxon specific database in fasta format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jschmacht/tax2peptide",
    packages=setuptools.find_packages(),
    classifiers=[
        
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['biopython', 'tqdm', 'wget'],
    python_requires='~=3.6',
)