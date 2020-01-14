import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="quantumics",
    version="0.0.3",
    description="Library for processor agnostic quantum-classical data science and artificial intelligence",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/quantumics/quantumics",
    author="Jawad Bashorun",
    author_email="jaybashorun@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    #packages=find_packages(exclude=("test","test2","mobile-app","build","dist"), include=["."]),
    packages=["quantumics", "quantumics.qmaps", "quantumics.qchemistry", "quantumics.qnumpy", "quantumics.qpandas",
    "quantumics.qprocessors", "quantumics.qclouds", "quantumics.qmaterials", "quantumics.qoperators", "quantumics.qsklearn",
    "quantumics.qdatabases", "quantumics.qmodels", "quantumics.qviews", "quantumics.qhilbertspaces", "quantumics.qnanotech",
    "quantumics.qphysics"],
    include_package_data=True,
    install_requires=["numpy", "qiskit", "dwave-ocean-sdk", "theano", "pandas", "sklearn", "mongo"],
    entry_points={
        "console_scripts": [
            "quantumics=__entry__:main",
        ]
    },
)
