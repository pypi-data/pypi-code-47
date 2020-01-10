import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyReadLabels",
    version="1.1.5",
    author="santh kumar tadi",
    author_email="santhtadi@gmail.com",
    description="Python Package to read labels from image",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/santhtadi/PyReadLabels",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    install_requires=["opencv-python","numpy"],
    include_package_data=True,
    license="MIT",
)