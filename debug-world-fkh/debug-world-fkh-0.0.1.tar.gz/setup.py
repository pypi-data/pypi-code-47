import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="debug-world-fkh",  # 包的分发名称
    version="0.0.1",    # 版本号
    author="fangkanghua",
    author_email="fangkanghua@corp.netease.com",
    description="PyPI Tutorial",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=setuptools.find_packages(),
    clasaaifiers=[
        "Programming Language :: Python :: 3",              # 该软件包仅与Python3兼容
        "License :: OSI Approved :: MIT License",           # 根据MIT许可证开源
        "Operating System :: OS Independent",
    ],
)