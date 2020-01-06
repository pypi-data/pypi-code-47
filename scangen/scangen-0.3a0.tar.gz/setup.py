import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="scangen",
    version="0.3a0",
    author="Levi Gruspe",
    author_email="mail.levig@gmail.com",
    description="Template-based scanner generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lggruspe/scangen",
    packages=["scangen"],
    install_requires=["jinja2"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux"
    ])
