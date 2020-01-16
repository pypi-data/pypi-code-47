import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='secursus-api',
    version='1.0.2',
    author="BRISSON Pierre-Alain",
    author_email="pab@secursus.com",
    description="Library PiP for Secursus api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/secursus_public/secursus_pip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
 )
