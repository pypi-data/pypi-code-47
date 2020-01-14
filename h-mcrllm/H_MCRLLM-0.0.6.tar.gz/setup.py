import setuptools


setuptools.setup(
    name="H_MCRLLM",
    version="0.0.6",
    author="Ryan Gosselin",
    author_email="ryan.gosselin@usherbrooke.ca",
    packages=["H_MCRLLM"],
    description="H MCRLLM: Hierarchical Multivariate Curve Resolution by Log-Likelihood Maximization",
    long_description="H MCRLLM: Hierarchical Multivariate Curve Resolution by Log-Likelihood Maximization\
    \n\nX = CS\
    \nwhere\
    \nX(nxk): Spectroscopic data where n spectra acquired over k energy levels\
    \nC(nxa): Composition map based on a MCRLLM components\
    \nS(axk): Spectra of the a components as computed by MCRLLM\
    \n\n# Method first presented in\
    \nLavoie F.B., Braidy N. and Gosselin R. (2016) Including Noise Characteristics in MCR to improve Mapping and Component Extraction from Spectral Images, Chemometrics and Intelligent Laboratory Systems, 153, 40-50.\
    \n\n# Input data\"",
    long_description_content_type="text/markdown",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)