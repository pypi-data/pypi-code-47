import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CTPC", 
    version="0.0.1",
    author="Tser",
    author_email="807447312@qq.com",
    description="Chinese To Python Code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/big_touch/ctpc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    install_requires=[
        "selenium"
    ]
)