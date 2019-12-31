import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="Covariance-Descriptor", 
    version="1.0.4",
    author="Kongfei He",
    author_email="hekongfei@outlook.com",
    description="a image descriptor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KongfeiH/Covariance-Descriptor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy>=1.16.2','opencv-python>=3.4.1','scipy>=1.4.1'],
    python_requires='>=3.6',
)    
