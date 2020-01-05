import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cmd-colorizer",
    version="0.0.2",
    author="KoChan-s",
    author_email="needahentai@gmail.com",
    description="Python library for using color text in cmd",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KoChan-s/cmd_colorizer",
    packages=setuptools.find_packages(),
    license="MIT",
    keywords="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Github": "https://github.com/KoChan-s/cmd_colorizer",
        "Documentation": "https://github.com/KoChan-s/cmd_colorizer/blob/master/README.md",
    },
    python_requires=">=3",
    install_requires=[
        "colorama"
    ]
)
