import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyMAX31855", # Replace with your own username
    version="0.0.1",
    author="Patrick Menschel",
    author_email="menschel.p@posteo.de",
    description="A python 3 interface for MAX31855 thermocouple IC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/menschel/pyMAX31855",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta", #used for years without any problems
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Embedded Systems',
    ],
    python_requires='>=3.6',
    install_requires=["spidev"],
    keywords="temperature thermocouple max31855",

)
