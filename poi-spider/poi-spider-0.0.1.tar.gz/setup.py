import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="poi-spider",
    version="0.0.1",
    author="soaringsoul",
    author_email="951683309@qq.com",
    description="an useful tool for getting poi data from baidu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xugongli/baidu-poi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)