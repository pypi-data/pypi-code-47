import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tpsisar18", # Replace with your own username
    version="0.0.2",
    author="Aryan Sindhi,Simarpreet Singh,Aryan Bhatia",
    author_email="asindhi_be17@thapar.edu",
    description="A small package that showcases topsis approach",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aryansindhi18/topsis_approach-aryansindhi18.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)