import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Topsis-Ranker", # Replace with your own username
    version="1.0.2",
    author="Pulkit Khagta",
    author_email="khagtapulkit@gmail.com",
    description="A python package to get topsis rank of given dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PulkitKhagta/Topsis-Pyhton-Package",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "topsis = topsis.TOPSIS3410:main",
        ]
    },
)