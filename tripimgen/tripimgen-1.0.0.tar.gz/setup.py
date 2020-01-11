import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tripimgen",
    version="1.0.0",
    author="Vahid V.",
    author_email="vhid.vz@gmail.com",
    description="TF.Keras Image Generator for Triplet NNs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vhidvz/TripletImageGenerator/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
