import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="confusion-metrics", # Replace with your own username
    version="0.0.4",
    author="Dr David Martin",
    author_email="d.m.a.martin@dundee.ac.uk",
    description="A collection of metrics for analysing confusion matrices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/davidmam/metrics.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)