import sys,setuptools,os
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="telnet2",
    version="1.0.0",
    author="AlaBouali",
    author_email="trap.leader.123@gmail.com",
    description="simple telnet interactive module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlaBouali/telnet",
    python_requires=">=2.7",
    packages=["telnet2"],
    license="MIT License",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License ",
    ],
)
