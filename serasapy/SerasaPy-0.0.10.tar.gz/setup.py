import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
    name="SerasaPy",
    version="0.0.10",
    author="FastDeploy",
    author_email="fastdeploy@dextra-sw.com",
    description="Biblioteca Fast Deploy",
    long_description=long_description,
    long_description_content_type="",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
