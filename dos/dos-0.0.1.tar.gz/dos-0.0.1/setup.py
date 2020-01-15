import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dos",
    version="0.0.1",
    author="Peter Richards",
    author_email="prichards@cap-rx.com",
    description="2 in one",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pr/dos",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)