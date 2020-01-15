from distutils.core import setup
import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='sequelize_to_excel',
    version='1.0.10',
    py_modules=['sequelize_to_excel'],
    author='Darshan Bharat',
    author_email='mailshahdarshan@gmail.com',
    url='https://github.com/darshan99/sequelize_to_excel',
    keywords=['Node','excel','Sequelize'],
    description="map your sequelize columns to excel",
    long_description = long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.6'
)