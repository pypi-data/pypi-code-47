import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='matplot-for-finance',
    version='0.0.3',
    author='haupv',
    author_email='haupv@vietnamlab.vn',
    description='a package for plot finance data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/phavaha1/matplot-for-finance',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    install_requires=["matplotlib", "numpy"],
)
