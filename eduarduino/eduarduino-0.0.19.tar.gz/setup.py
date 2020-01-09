import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eduarduino",
    version="0.0.19",
    author="Techurbana",
    author_email="techurbana@gmail.com",
    license='MIT',
    description="Arduino Nano + pyFirmata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/techurbana/pynano",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pyfirmata',
    ],
) 
