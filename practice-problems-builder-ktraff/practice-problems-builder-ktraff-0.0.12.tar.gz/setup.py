import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="practice-problems-builder-ktraff",
    version="0.0.12",
    author="Kyle Traff",
    author_email="ktraff@gmail.com",
    description="CLI tool for building practice programming problems",
    include_package_data=True,
    install_requires=['jinja2', 'PyYAML'],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ktraff/practice-problems-builder",
    scripts=['bin/ppb'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)